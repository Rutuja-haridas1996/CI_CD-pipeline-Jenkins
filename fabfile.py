from __future__ import with_statement
from fabric.api import local, settings, abort, run, get
from fabric.contrib.console import confirm


# def test():
#     with settings(warn_only=True):
#         result = local('pytest -v', capture=True)
#     if result.failed and not confirm("Tests failed. Continue anyway?"):
#         abort("Aborting at user request.")
#
# def commit():
#     local("git add -p && git commit")
#
# def push():
#     local("git push origin master")
#
# def prepare_deploy():
#     test()
#     commit()
#     push()

def make_dir():
    # run("mkdir /home/rutujaharidas/PycharmProjects/jenkins_3/CI_CD-pipeline-Jenkins/run_file_demo/")
    # get(remote_path="/home/rutujaharidas/Desktop/28_09.zip", local_path="/home/rutujaharidas/PycharmProjects/jenkins_3/CI_CD-pipeline-Jenkins/run_file_demo/")
    # get("mongodump --db mooveit_db --gzip","./db.gz")
    run("mongodump --db mooveit_db --gzip -o /home/rutujaharidas/Desktop")
    get(remote_path="/home/rutujaharidas/Desktop/mooveit_db",
        local_path="/home/rutujaharidas/PycharmProjects/jenkins_3/CI_CD-pipeline-Jenkins/run_file_demo/")


def pwd():
    run("pwd")
