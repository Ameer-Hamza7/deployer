from subprocess import run

from celery import shared_task


@shared_task
def deployer_script():
  # Access instance data if needed for the script
  # ...
  print('deploying .............')
  result = run("sh shared.sh", check=True)
  print('results .............', result)
  # Handle success or failure based on result.returncode
