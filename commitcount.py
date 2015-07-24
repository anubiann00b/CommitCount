from github3 import login
from github3.exceptions import ClientError
from github3.exceptions import AuthenticationFailed
from io import BytesIO
import requests
import sys

def displayHelp():
    print 'help'

if (len(sys.argv) == 2):
    if (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        displayHelp()
        sys.exit()
    try:
        with open(sys.argv[1]) as f:
            user = f.readline().strip()
            password = f.readline().strip()
    except IOError as e:
        print 'Failed to open file: ' + sys.argv[1]
        sys.exit()
elif (len(sys.argv) == 3):
    user = sys.argv[1]
    password = sys.argv[2]
else:
    with open('CREDS') as f:
        user = f.readline().strip()
        password = f.readline().strip()

gh = login(user, password=password)

try:
    account = gh.me()
except AuthenticationFailed as e:
    print 'Authentication Failed for user ' + user + '.'
    sys.exit()

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