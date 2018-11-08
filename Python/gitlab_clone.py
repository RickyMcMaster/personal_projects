from urllib.request import urlopen
import json, os, subprocess, shlex


# print('hi')
allProjects = urlopen("https://gitlab.plista.com/dataeng/da")

allProjectsDict = json.loads(allProjects.read().decode())
# for thisProject in allProjectsDict:
#     print(thisProject)
    # try:
    #     thisProjectURL  = thisProject['ssh_url_to_repo']
    #     command     = shlex.split('git clone %s' % thisProjectURL)
    #     resultCode  = subprocess.Popen(command)
    #
    # except Exception as e:
    #     print("Error on %s: %s" % (thisProjectURL, e.strerror))