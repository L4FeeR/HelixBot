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
        response = requests.get(url=url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            return f"""
GitHub Info

👤 Username     : {data['login']}
🧑‍💼 Name         : {data.get('name', 'N/A')}
📝 Bio          : {data.get('bio', 'N/A')}
📦 Repos        : {data['public_repos']}
👥 Followers    : {data['followers']}
🔁 Following    : {data['following']}
📅 Created At   : {data['created_at']}
🌐 Profile      : {data['html_url']}
"""
        else:
            return f"❌ Error: {response.status_code} - {response.json().get('message', 'User not found')}"

    def get_repoinfo(self):
        url=f"https://api.github.com/users/{self.x}/repos?per_page=1000&page=1"
        response=requests.get(url=url, headers=self.headers)
        data=response.json()
        reps=[]
        for repo in data:
            reps.append(repo['name'])
        return reps



    def get_repdet(self, repo):
        url=f"https://api.github.com/repos/{self.x}/{repo}"
        print(url)
        response=requests.get(url=url, headers=self.headers)
        if response.status_code !=200:
            return f"""❌ Error: {response.status_code} - {response.json().get('message', 'Not found')}"""
        else:
            data=response.json()
            return f"""
            Githuh Repo Info

🧑‍💻 Owner       : {data['owner']['login']}
📝 Description : {data.get('description', 'No description')}
🔖 License     : {data['license']['name'] if data['license'] else 'None'}

⭐ Stars       : {data['stargazers_count']}
🍴 Forks       : {data['forks_count']}
👀 Watchers    : {data['watchers_count']}
📂 Language    : {data['language'] or 'N/A'}
📅 Created     : {data['created_at']}
📅 Updated     : {data['updated_at']}

🌐 URL         : {data['html_url']}
"""



