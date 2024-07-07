import os
import subprocess
import requests
import shutil
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ACCESS_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')
USERNAME = os.getenv('GITHUB_USERNAME')
HEADERS = {'Authorization': f'token {ACCESS_TOKEN}'}

# Function to get all repositories
def get_repositories():
    repos = []
    page = 1
    while True:
        url = f'https://api.github.com/user/repos?page={page}&per_page=100'
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            raise Exception(f'Error fetching repos: {response.json()}')
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

# Function to clone repositories
def clone_repositories(repos):
    if not os.path.exists('repos'):
        os.makedirs('repos')
    os.chdir('repos')
    for repo in repos:
        clone_url = repo['clone_url']
        repo_name = repo['name']
        print(f'Cloning {repo_name}...')
        result = subprocess.run(['git', 'clone', clone_url])
        if result.returncode != 0:
            print(f'Failed to clone {repo_name}.')
    os.chdir('..')

# Function to archive repositories
def archive_repositories():
    shutil.make_archive('repositories_backup', 'zip', 'repos')

def main():
    repos = get_repositories()
    clone_repositories(repos)
    archive_repositories()
    print('All repositories have been cloned and archived successfully.')

if __name__ == '__main__':
    main()
