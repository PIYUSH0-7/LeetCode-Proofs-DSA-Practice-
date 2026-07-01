import json
import urllib.request
import urllib.error
import sys
import os
import time
import argparse

def get_gemini_solution(title, content, starter_code, api_key):
    try:
        import google.generativeai as genai
    except ImportError:
        print("Error: google-generativeai package is not installed. Run 'pip install google-generativeai'")
        sys.exit(1)

    genai.configure(api_key=api_key)
    # Using gemini-1.5-flash as it is fast, cheap/free, and excellent at coding tasks
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
You are an regular software engineer solving a LeetCode problem.
Write a clean, optimal Python3 solution for the following LeetCode problem.

IMPORTANT STEALTH REQUIREMENTS:
1. DO NOT write any verbose AI comments like "Time Complexity: O(N)", "Explanation:", or "Here is the code".
2. DO NOT include docstrings inside the methods.
3. Write ONLY standard code. Keep comments minimal or absent (just like a normal developer submitting on LeetCode).
4. Use standard, natural variable names.
5. Wrap your solution EXACTLY within the starter code structure provided. Do not rename the class or the function.
6. Return ONLY the code inside your answer. No markdown formatting blocks (like ```python ... ```), just raw code.

Problem Title: {title}
Problem Description:
{content}

Starter Code Template:
{starter_code}
"""

    try:
        response = model.generate_content(prompt)
        code = response.text.strip()
        # Strip code block markdown if the model added it despite instructions
        if code.startswith("```python"):
            code = code[9:]
        if code.endswith("```"):
            code = code[:-3]
        return code.strip()
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return None

def fetch_unsolved_problems(cookie_str, csrf_token):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "Cookie": cookie_str,
        "x-csrftoken": csrf_token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    list_query = """
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
      problemsetQuestionList: questionList(
        categorySlug: $categorySlug
        limit: $limit
        skip: $skip
        filters: $filters
      ) {
        questions: data {
          frontendQuestionId: questionFrontendId
          isPaidOnly
          status
          title
          titleSlug
        }
      }
    }
    """
    
    variables = {
        "categorySlug": "",
        "skip": 0,
        "limit": 100,
        "filters": {
            "difficulty": "EASY"
        }
    }

    payload = json.dumps({"query": list_query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            res_json = json.loads(response.read().decode("utf-8"))
            questions = res_json.get("data", {}).get("problemsetQuestionList", {}).get("questions", [])
    except Exception as e:
        print(f"Error fetching problem list: {e}")
        return []

    unsolved = []
    for q in questions:
        status = q.get("status")
        is_paid = q.get("isPaidOnly")
        if not is_paid:
            if not status or status.lower() != "ac":
                unsolved.append(q)
                if len(unsolved) == 3:
                    break
    return unsolved

def fetch_problem_details(slug, cookie_str, csrf_token):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "Cookie": cookie_str,
        "x-csrftoken": csrf_token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    detail_query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        title
        content
        difficulty
        codeSnippets {
          lang
          langSlug
          code
        }
      }
    }
    """

    det_payload = json.dumps({"query": detail_query, "variables": {"titleSlug": slug}}).encode("utf-8")
    det_req = urllib.request.Request(url, data=det_payload, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(det_req, timeout=15) as det_resp:
            det_json = json.loads(det_resp.read().decode("utf-8"))
            q_data = det_json.get("data", {}).get("question", {})
            
            py_snippet = ""
            for snippet in q_data.get("codeSnippets", []):
                if snippet["langSlug"] == "python3":
                    py_snippet = snippet["code"]
                    break
            
            return {
                "id": q_data.get("questionFrontendId"),
                "questionId": q_data.get("questionId"),
                "title": q_data.get("title"),
                "titleSlug": slug,
                "content": q_data.get("content"),
                "starterCode": py_snippet
            }
    except Exception as e:
        print(f"Error fetching details for {slug}: {e}")
        return None

def submit_solution(title_slug, question_id, solution_code, cookie_str, csrf_token):
    submit_url = f"https://leetcode.com/problems/{title_slug}/submit/"
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{title_slug}/",
        "Cookie": cookie_str,
        "x-csrftoken": csrf_token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    body = {
        "lang": "python3",
        "question_id": str(question_id),
        "typed_code": solution_code
    }
    
    payload = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(submit_url, data=payload, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            res_json = json.loads(response.read().decode("utf-8"))
            return res_json.get("submission_id")
    except Exception as e:
        print(f"Submit request failed for {title_slug}: {e}")
        return None

def check_submission(submission_id, cookie_str, csrf_token):
    check_url = f"https://leetcode.com/submissions/detail/{submission_id}/check/"
    check_headers = {
        "Cookie": cookie_str,
        "x-csrftoken": csrf_token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    check_req = urllib.request.Request(check_url, headers=check_headers, method="GET")
    
    for _ in range(12):
        time.sleep(5)
        try:
            with urllib.request.urlopen(check_req, timeout=15) as response:
                res_json = json.loads(response.read().decode("utf-8"))
                state = res_json.get("state")
                if state == "SUCCESS":
                    status_code = res_json.get("status_code")
                    status_msg = res_json.get("status_msg")
                    return status_code == 10 and status_msg == "Accepted", res_json
        except Exception:
            pass
    return False, {"error": "Timeout"}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_key", help="Gemini API Key (optional if GEMINI_API_KEY environment variable is set)")
    args = parser.parse_args()

    # Determine Gemini API key
    gemini_key = args.api_key or os.environ.get("GEMINI_API_KEY")
    if not gemini_key:
        print("Error: GEMINI_API_KEY is not set. Get a free key from Google AI Studio.")
        sys.exit(1)

    # Determine LeetCode credentials
    cookie_str = os.environ.get("LEETCODE_SESSION_COOKIE")
    csrf_token = os.environ.get("LEETCODE_CSRF_TOKEN")

    # If not in environment, try reading local user.json config
    if not cookie_str or not csrf_token:
        config_path = "C:/Users/gangw/.lc/leetcode/user.json"
        if os.path.exists(config_path):
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    user_data = json.load(f)
                cookie_str = user_data.get("cookie")
                csrf_token = user_data.get("sessionCSRF")
            except Exception as e:
                print(f"Error reading local user.json: {e}")

    if not cookie_str or not csrf_token:
        print("Error: LeetCode session credentials not found in environment or local config.")
        sys.exit(1)

    print("Fetching 3 unsolved Easy problems...")
    problems = fetch_unsolved_problems(cookie_str, csrf_token)
    if not problems:
        print("No unsolved Easy problems found.")
        sys.exit(0)

    solved_count = 0
    workspace_dir = os.path.dirname(os.path.abspath(__file__))

    for q in problems:
        slug = q["titleSlug"]
        print(f"\n--- Processing: {q['title']} ---")
        
        details = fetch_problem_details(slug, cookie_str, csrf_token)
        if not details:
            print(f"Failed to fetch details for {slug}")
            continue

        print("Generating solution via Gemini...")
        solution = get_gemini_solution(details["title"], details["content"], details["starterCode"], gemini_key)
        if not solution:
            print(f"Failed to generate solution for {slug}")
            continue

        # Format code to match LeetCode VS Code extension layout
        formatted_code = f"""#
# @lc app=leetcode id={details['id']} lang=python3
#
# [{details['id']}] {details['title']}
#

# @lc code=start
{solution}
# @lc code=end
"""

        print("Submitting to LeetCode...")
        sub_id = submit_solution(slug, details["questionId"], solution, cookie_str, csrf_token)
        if not sub_id:
            continue

        print(f"Submission ID: {sub_id}. Polling results...")
        accepted, result_details = check_submission(sub_id, cookie_str, csrf_token)
        
        if accepted:
            print(f"Accepted! Runtime: {result_details.get('status_runtime')}, Memory: {result_details.get('status_memory')}")
            
            # Save file to workspace
            file_name = f"{details['id']}.{slug}.py"
            file_path = os.path.join(workspace_dir, file_name)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(formatted_code)
            print(f"Saved solution to {file_path}")
            
            # Stage the file in git
            os.system(f'git add "{file_name}"')
            solved_count += 1
            
            # Sleep to look human (spacing out attempts)
            print("Waiting 60 seconds before next problem to simulate typing delay...")
            time.sleep(60)
        else:
            print(f"Submission failed or not accepted: {result_details.get('status_msg', 'Unknown status')}")

    if solved_count > 0:
        print(f"\nSuccessfully solved {solved_count} problems.")
        # Commit and push
        os.system('git commit -m "Auto-solve daily LeetCode Easy problems"')
        os.system('git push')
        print("Committed and pushed code changes to GitHub.")
    else:
        print("\nNo problems were successfully solved.")

if __name__ == "__main__":
    main()
