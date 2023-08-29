import subprocess

def get_latest_tag():
    return subprocess.getoutput("git describe --tags --abbrev=0").lstrip('v')

def count_commits_since_last_tag(latest_tag):
    return int(subprocess.getoutput(f"git rev-list v{latest_tag}..HEAD --count"))

if __name__ == "__main__":
    latest_tag = get_latest_tag()
    major, minor, patch = map(int, latest_tag.split('.'))
    new_patch = count_commits_since_last_tag(latest_tag)
    new_version = f"v{major}.{minor}.{new_patch}"
    print(new_version)
