import prefect
from prefect import task, Flow
from prefect.tasks.shell import ShellTask
from prefect.storage.git import Git

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("howdy")
    return 'touch howdy-from-git-hub'

run_in_shell = ShellTask(name = 'shell_test')

with Flow("hello-flow") as flow:
    cmd = hello_task()
    run_in_shell(command = cmd)

flow.storage = Git(flow_path = '/flows/flow.py', 
                   repo = 'daniel-davee/my_prefect_test',
                   repo_host = 'github.com')