# import psycopg2


# # Establishing a db connection
# conn = psycopg2.connect(database = "deployer", 
#                         user = "postgres", 
#                         host= "158.220.114.235",
#                         password = "postgres",
#                         port = 6432)

# cur = conn.cursor()

# sql = "SELECT * FROM public.deploy_engine_appdeploymenthistory WHERE build_status = 'Active';"
# cur.execute(sql)
# rows = cur.fetchall()
# conn.commit()
# conn.close()
# for row in rows:
#     print(row)

# import subprocess
# output = subprocess.call(["source jobs/shared.sh"])
# print(output)

print("Hello World")