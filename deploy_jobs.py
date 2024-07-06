import os
import psycopg2
import subprocess
import time
from dotenv import load_dotenv
load_dotenv()
# Establishing a db connection
conn = psycopg2.connect(database = os.getenv('DATABASE_NAME'), 
                        user = os.getenv('USER_NAME'), 
                        host= os.getenv('HOST'),
                        password = os.getenv('PASSWORD'),
                        port = os.getenv('PORT'))

cur = conn.cursor()
select_sql = "SELECT * FROM public.deploy_engine_appdeploymenthistory WHERE build_status = 'Active';"
cur.execute(select_sql)
rows = cur.fetchall()

conn.commit()


def execute_deployment(app):
    output = None
    
    if app == 'theinnovativesolution/visualisation_univariate':
        output = subprocess.run(["/root/xtremeanalytix/deployer/deployer/jobs/visualization.sh"])
    elif app == 'theinnovativesolution/visualisation_multivariate':
        output = subprocess.run(["/root/xtremeanalytix/deployer/deployer/jobs/visualization.sh"])
    elif app == 'theinnovativesolution/xtremeanalytix_data_bridge':
        output = subprocess.run(["/root/xtremeanalytix/deployer/deployer/jobs/data_bridge.sh"])
    else:
        output = subprocess.run(["/root/xtremeanalytix/deployer/deployer/jobs/microservices.sh"])
    
    return output

for row in rows:
    from confg import DEPLOYMENT_SOURCE
    if row[3] == DEPLOYMENT_SOURCE:
        try:
            output = execute_deployment(row[2])
            if output.returncode == 0:
                update_sql = f"UPDATE public.deploy_engine_appdeploymenthistory SET build_status = 'Success' WHERE id = {row[0]};"
                cur.execute(update_sql)
                conn.commit()
                time.sleep(5)
        except Exception as e:
            update_sql = f"UPDATE public.deploy_engine_appdeploymenthistory SET build_status = 'Failed' WHERE id = {row[0]};"
            cur.execute(update_sql)
            print("Exception: ", e)
            conn.commit()
conn.close()
