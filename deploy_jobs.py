import psycopg2
import subprocess
import time

# Establishing a db connection
conn = psycopg2.connect(database = "deployer", 
                        user = "postgres", 
                        host= "158.220.114.235",
                        password = "postgres",
                        port = 6432)

cur = conn.cursor()
select_sql = "SELECT * FROM public.deploy_engine_appdeploymenthistory WHERE build_status = 'Active';"
cur.execute(select_sql)
rows = cur.fetchall()

conn.commit()


def execute_deployment(app):
    output = None
    
    if app == 'theinnovativesolution/gatewayserver':
        output = subprocess.run(["/root/xtremeanalytix/deployer/deployer/jobs/microservices.sh", "gatewayserver"])
    elif app == 'theinnovativesolution/configserver':
        output = subprocess.run(["/root/xtremeanalytix/deployer/deployer/jobs/microservices.sh", "configserver"])
    elif app == 'theinnovativesolution/eurekaserver':
        output = subprocess.run(["/root/xtremeanalytix/deployer/deployer/jobs/microservices.sh", "eurekaserver"])
    elif app == 'theinnovativesolution/authservice':
        output = subprocess.run(["/root/xtremeanalytix/deployer/deployer/jobs/microservices.sh", "registrataionservice"])
    elif app == 'theinnovativesolution/dataanalytics':
        output = subprocess.run(["/root/xtremeanalytix/deployer/deployer/jobs/microservices.sh", "dataanalyticsservice"])
    elif app == 'theinnovativesolution/visualisation_multivariate':
        output = subprocess.run(["/root/xtremeanalytix/deployer/deployer/jobs/visualization.sh", "multivariate"])
    elif app == 'theinnovativesolution/visualisation_univariate':
        output = subprocess.run(["/root/xtremeanalytix/deployer/deployer/jobs/visualization.sh", "univariate"])
    elif app == 'theinnovativesolution/xtremeanalytix_data_bridge':
        output = subprocess.run(["/root/xtremeanalytix/deployer/deployer/jobs/data_bridge.sh"])
    
    return output

# [(34, 'authservice', 'theinnovativesolution/authservice', 'latest-dev', 'Active', datetime.datetime(2024, 6, 27, 17, 25, 16, 824239, tzinfo=datetime.timezone.utc), datetime.datetime(2024, 6, 27, 8, 14, 58, 414071, tzinfo=datetime.timezone.utc), '1719476097')]

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
            conn.commit()
conn.close()
