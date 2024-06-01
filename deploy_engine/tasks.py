from subprocess import run

from celery import shared_task


@shared_task
def deployer_script(instance):
  # Access instance data if needed for the script
  # ...
  result = run("./shared.sh", shell=True)
  print('results .............', result)
  # Handle success or failure based on result.returncode
