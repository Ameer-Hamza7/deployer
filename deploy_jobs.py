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
for row in rows:
    try:
        output = subprocess.call(["/root/xtremeanalytix/deployer/deployer/jobs/data_bridge.sh"])
        update_sql = f"UPDATE public.deploy_engine_appdeploymenthistory SET build_status = 'Success' WHERE id = {row[0]};"
        cur.execute(update_sql)
        conn.commit()
        time.sleep(2)
    except Exception as e:
        update_sql = f"UPDATE public.deploy_engine_appdeploymenthistory SET build_status = 'Success' WHERE id = {row[0]};"
        cur.execute(update_sql)
        conn.commit()
        print(e)
    print('ROW : ------------> ', row)
    print('OUTPUT : ------------> ', output)
conn.close()

print("Hey I might get called.........")