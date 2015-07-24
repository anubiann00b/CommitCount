from github3 import login
from github3.exceptions import ClientError

with open('CREDS') as f:
    user = f.readline().strip()
    password = f.readline().strip()

gh = login(user, password=password)

account = gh.me()

cnt = 0
for repo in gh.repositories(type='all'):
    repocnt = 0
    try:
        for commit in repo.commits(author='skraman1999@gmail.com'):
            repocnt += 1
    except ClientError as e: # Handles empty repos
        pass

    cnt += repocnt

    repoName = str(repo)
    nums = '{0:<{2}}{1:>}'.format(repocnt, cnt, 10-len(str(cnt)))
    print repoName + '{:>{}}'.format(nums, 60-len(repoName))