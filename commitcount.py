from github3 import login
from github3.exceptions import ClientError
from github3.exceptions import AuthenticationFailed
from github3.exceptions import GitHubError
import requests
from io import BytesIO

with open('CREDS') as f:
    user = f.readline().strip()
    password = f.readline().strip()

gh = login(user, password=password)

if (gh is None):
    r = requests.Response()
    r.status_code = 401
    r.raw = BytesIO('Authentication Failed')
    raise AuthenticationFailed(r)

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

print '\nTotal commits: ' + str(cnt)
