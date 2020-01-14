import os.path
from git import *
import git, os, shutil

# create local Repo/Folder
#UPLOAD_FOLDER = "F:\zealot"
UPLOAD_FOLDER = "F:\python\python_test1"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    print(UPLOAD_FOLDER)
new_path = os.path.join(UPLOAD_FOLDER)
DIR_NAME = new_path
REMOTE_URL = "https://github.com/Darth-Kordis/python_test.git"
#REMOTE_URL = "GitURL"  # if you already connected with server you dont need to give any credential
# REMOTE_URL looks "git@github.com:path of Repo"
# code for clone


class git_operation_clone():
    try:
        def __init__(self):
            self.DIR_NAME = DIR_NAME
            self.REMOTE_URL = REMOTE_URL

        def git_clone(self):
            if not os.path.exists(DIR_NAME):
                if os.path.isdir(DIR_NAME):
                    shutil.rmtree(DIR_NAME)
                os.mkdir(DIR_NAME)
            repo = git.Repo.init(DIR_NAME)
            origin = repo.create_remote('origin', REMOTE_URL)
            origin.fetch()
            origin.pull(origin.refs[0].remote_head)
    except Exception as e:
        print(str(e))


# code for push
class git_operation_push():
    def git_push_file(self):
        try:
            repo = Repo(DIR_NAME)
            commit_message = 'work in progress'
            # repo.index.add(u=True)
            repo.git.add('--all')
            repo.index.commit(commit_message)
            origin = repo.remote('origin')
            origin.push('master')
            repo.git.add(update=True)
            print("repo push succesfully")
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    a = git_operation_push()

    git_operation_clone()
    git_operation_clone.git_clone('')
    git_operation_push.git_push_file('')