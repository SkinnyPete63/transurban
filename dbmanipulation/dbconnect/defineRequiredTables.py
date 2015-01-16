from dbconnect import session, MAXOBJECT
from dbconnect.maximo_attributes import primary_cols

def define_table(tblist):
    with open("temp_tabledefs.py", "wb") as f:        
        f.write("from sqlalchemy import *\n")
        f.write("from sqlalchemy.ext.declarative import declarative_base\n")
        f.write("from sqlalchemy.orm import create_session\n")
        f.write("from dbconnect.parameters import *\n")
        f.write("import base64\n")
        f.write("\n")
        f.write("decpass = base64.b64decode(dbpass)\n")
        f.write("\n")
        f.write("connectstring = 'mssql+pyodbc://' + dbuser + ':' + decpass + '@' + dbserver + '/' + db + ';Trusted_Connection=Yes' \n")
        f.write("Base = declarative_base()\n")
        f.write("engine = create_engine(connectstring)\n")
        f.write("metadata = MetaData(bind=engine)\n")
        f.write("session = create_session(bind=engine)\n")
        f.write("\n")
        for x in range(0, len(tblist))  :  
            marg = primary_cols(tblist[x])
            if marg is not None:
                marg = "\t" + marg
                f.write ("class " + tblist[x] + "(Base):\n")
                f.write("\t__table__ = Table('" + tblist[x] + "', metadata, autoload=True)\n")
                f.write(marg + "\n")
                f.write("\n")
    
#         
#         for x in range(0, len(tblist)):
#             mytb = getattr(mymod, tblist[x])
#             f.write(mytb + "\n\n")
if __name__ == "__main__":
    tblist = ["ASSET", "LOCATIONS"]
    define_table(tblist)