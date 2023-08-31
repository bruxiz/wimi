import subprocess

def get_latest_tag():
    try:
        return subprocess.getoutput("git describe --tags --abbrev=0").lstrip('v')
    except Exception as e:
        print(f"Error fetching latest tag: {e}")
        exit(1)

def count_commits_since_last_tag(latest_tag):
    try:
        return int(subprocess.getoutput(f"git rev-list v{latest_tag}..HEAD --count"))
    except ValueError as e:
        print(f"Error counting commits: {e}")
        exit(1)

if __name__ == "__main__":
    latest_tag = get_latest_tag()

    if "fatal:" in latest_tag:
        print("No tags found.")
        exit(1)

    try:
        major, minor, patch = map(int, latest_tag.split('.'))
    except ValueError as e:
        print(f"Error parsing latest tag into major, minor, patch: {e}")
        exit(1)

    new_patch = count_commits_since_last_tag(latest_tag)

    new_version = f"v{major}.{minor}.{new_patch}"
    print(new_version)
