import pyodbc as odbc




#connection string components
server = "localhost"
database = "mydb"
username = "sa"
password = r"N\VHs8*DJV"
driver = "/opt/homebrew/lib/libmsodbcsql.18.dylib"



#connection string
connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes"

try:
    cnxn = odbc.connect(connection_string)
    print("Connected successfully!")
except odbc.Error as ex:
    print("Connection failed:", ex)
# Connection
#conn = odbc.connect(connection_string)