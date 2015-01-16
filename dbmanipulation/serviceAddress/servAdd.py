from dbconnect import session_scope
from dbconnect.tabledefs.SERVICEADDRESS import SERVICEADDRESS
import binascii

with session_scope() as session:
    sa = session.query(SERVICEADDRESS).all()

    for row in sa:
        print row.addresscode, binascii.hexlify(bytearray(row.rowstamp))