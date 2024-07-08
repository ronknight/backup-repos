<p><a target="_blank" href="https://app.eraser.io/workspace/ylnmyhe3avCgFCbxxDp6" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>


<h1 align="center"><a href="https://github.com/ronknight/backup-repos">Backup GitHub Repositories</a></h1>

<h4 align="center">This Python script clones and archives all GitHub repositories for a user.</h4>

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/ronknight/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
<a href="https://github.com/ronknight/ronknight/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
<a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/ronknight/backup-repos/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/backup-repos/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

<p align="center">
  <a href="#requirements">Requirements</a> •
  <a href="#usage">Usage</a> •
  <a href="#script">Script</a> •
  <a href="#disclaimer">Disclaimer</a> •
  <a href="#diagrams">Diagrams</a>
</p>

---

## Requirements
- Python 3.x
- `requests`  library
- `python-dotenv`  library
- Git
Install the required Python libraries using:

```
pip install requests python-dotenv
```

## Usage
1. Clone this repository:git clone https://github.com/ronknight/backup-repos.git
cd backup-repos
2. Create a `.env`  file in the same directory as the script with your GitHub credentials:GITHUB_ACCESS_TOKEN=your_github_access_token
GITHUB_USERNAME=your_github_username
3. Run the script:python backup_repos.py
The script will clone all your GitHub repositories into a `repos` folder and create a zip archive named `repositories_backup.zip`.

## Script
The `backup_repos.py` script performs the following actions:

1. Fetches all repositories for the authenticated user using the GitHub API.
2. Clones each repository into a `repos`  folder.
3. Creates a zip archive of all cloned repositories.

## Disclaimer
This script is for personal use and backup purposes only. Please respect GitHub's terms of service and API rate limits when using this script.

<!-- eraser-additional-content -->
## Diagrams
<!-- eraser-additional-files -->
<a href="/README-Backup GitHub Repositories Flowchart-1.eraserdiagram" data-element-id="por_TtmEsP8KnFivkvoWa"><img src="/.eraser/ylnmyhe3avCgFCbxxDp6___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----3f0324b45fb8d604639b4851506d5ca3-Backup-GitHub-Repositories-Flowchart.png" alt="" data-element-id="por_TtmEsP8KnFivkvoWa" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/ylnmyhe3avCgFCbxxDp6 --->