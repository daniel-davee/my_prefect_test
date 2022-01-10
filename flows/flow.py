from os import name
import prefect
from prefect import task, Flow
from prefect.tasks.shell import ShellTask

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")
    return 'touch howdy'

run_in_shell = ShellTask(name = 'shell_test')

with Flow("hello-flow") as flow:
    cmd = hello_task()
    run_in_shell(command = cmd)

flow.run()
