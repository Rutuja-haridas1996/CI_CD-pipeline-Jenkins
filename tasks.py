from invoke import task, call


@task(name="webopener")
def webopener(c, url=None):
    if url:
        c.run(f"google-chrome {url}")
    else:
        print("I need a url to run it")


@task
def firststep(c):
    print("Going to perform the first step!")


@task
def thirdstep(c, name="This is the default name!"):
    print("Going to perform the third step!")
    print(f"We go the argument name = {name}")


@task(pre=[firststep], post=[call(thirdstep, name="This is chained!")])
# @task(pre = [firststep], post=[thirdstep])
def secondstep(c):
    print("This is the main happening!")
