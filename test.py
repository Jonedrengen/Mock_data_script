import pyodbc
#w
server = 'localhost'
database = 'mydb'
username = 'sa'
password = 'Slotved2314!' 
# direct path: "/opt/homebrew/lib/libmsodbcsql.18.dylib"
driver ='{ODBC Driver 18 for SQL Server}'
#connection_string = r'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'.format(driver=driver, server=server, database=database, username=username, password=password)
#driver = '/opt/homebrew/lib/libmsodbcsql.18.dylib'
print(pyodbc.drivers())
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
conn = pyodbc.connect(connection_string)
#print("Connected successfully")

