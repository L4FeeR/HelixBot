import requests
from urllib.parse import quote_plus

class GitInfo:
    def __init__(self, user):
        self.x = user
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }

    def get_gituserinfo(self):
        print(f"[+] Getting information about {self.x}...")
        url = f"https://api.github.com/users/{quote_plus(self.x)}"
        try:
            response = requests.get(url=url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return f"""
GitHub Info

👤 Username     : {data.get('login', 'N/A')}
🧑‍💼 Name         : {data.get('name', 'N/A')}
📝 Bio          : {data.get('bio', 'N/A')}
📦 Repos        : {data.get('public_repos', 'N/A')}
👥 Followers    : {data.get('followers', 'N/A')}
🔁 Following    : {data.get('following', 'N/A')}
📅 Created At   : {data.get('created_at', 'N/A')}
🌐 Profile      : {data.get('html_url', 'N/A')}
"""
            else:
                try:
                    msg = response.json().get('message', 'User not found')
                except Exception:
                    msg = 'User not found'
                return f"❌ Error: {response.status_code} - {msg}"
        except Exception as e:
            return f"❌ Error: Exception occurred - {str(e)}"

    def get_repoinfo(self):
        url = f"https://api.github.com/users/{self.x}/repos?per_page=100&page=1"
        reps = []
        try:
            response = requests.get(url=url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                for repo in data:
                    reps.append(repo.get('name', 'Unknown'))
            else:
                reps.append(f"❌ Error: {response.status_code}")
        except Exception as e:
            reps.append(f"❌ Exception: {str(e)}")
        return reps

    def get_repdet(self, repo):
        url = f"https://api.github.com/repos/{self.x}/{repo}"
        print(url)
        try:
            response = requests.get(url=url, headers=self.headers, timeout=10)
            if response.status_code != 200:
                try:
                    msg = response.json().get('message', 'Not found')
                except Exception:
                    msg = 'Not found'
                return f"""❌ Error: {response.status_code} - {msg}"""
            else:
                data = response.json()
                return f"""
            GitHub Repo Info

🧑‍💻 Owner       : {data.get('owner', {}).get('login', 'N/A')}
📝 Description : {data.get('description', 'No description')}
🔖 License     : {data.get('license', {}).get('name', 'None') if data.get('license') else 'None'}

⭐ Stars       : {data.get('stargazers_count', 0)}
🍴 Forks       : {data.get('forks_count', 0)}
👀 Watchers    : {data.get('watchers_count', 0)}
📂 Language    : {data.get('language', 'N/A')}
📅 Created     : {data.get('created_at', 'N/A')}
📅 Updated     : {data.get('updated_at', 'N/A')}
🌐 URL         : {data.get('html_url', 'N/A')}
"""
        except Exception as e:
            return f"❌ Error: Exception occurred - {str(e)}"
