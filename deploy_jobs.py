import psycopg2
import subprocess


# Establishing a db connection
conn = psycopg2.connect(database = "deployer", 
                        user = "postgres", 
                        host= "158.220.114.235",
                        password = "postgres",
                        port = 6432)

cur = conn.cursor()

sql = "SELECT * FROM public.deploy_engine_appdeploymenthistory WHERE build_status = 'Active';"
cur.execute(sql)
rows = cur.fetchall()
conn.commit()
conn.close()
for row in rows:
    try:
        output = subprocess.call(["/root/xtremeanalytix/deployer/deployer/jobs/data_bridge.sh"])
        
    except Exception as e:
        print(e)
    print('ROW : ------------> ', row)
    print('OUTPUT : ------------> ', output)

print("Hey I might get called.........")