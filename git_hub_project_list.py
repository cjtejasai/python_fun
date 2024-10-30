import requests


def search_github_repos(keyword, num_results=10):
    headers = {"Authorization": "add ur key"}
    query = f"{keyword} in:readme"
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = response.json()['items'][:num_results]
        return [
            {"name": repo["name"], "stars": repo["stargazers_count"], "url": repo["html_url"]}
            for repo in repos
        ]
    else:
        print(f"Error: {response.status_code}")
        return []


# Use the function to search repositories
repos = search_github_repos("vision language model")
for repo in repos:
    print(f"{repo['name']} - Stars: {repo['stars']} - URL: {repo['url']}")
