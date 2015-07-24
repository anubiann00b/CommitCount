from github3 import login
from github3.exceptions import ClientError
from github3.exceptions import AuthenticationFailed
from io import BytesIO
import requests
import sys

if (len(sys.argv) == 2):
    print
    print "    Include a 'CREDS' file with username and password on the first two lines."
    print "    Or pass username and password as arguments to this script."
    print "    See https://github.com/anubiann00b/CommitCount for more info."
    sys.exit()
elif (len(sys.argv) == 3):
    user = sys.argv[1]
    password = sys.argv[2]
else:
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

print '\nTotal commits: ' + str(cnt)
