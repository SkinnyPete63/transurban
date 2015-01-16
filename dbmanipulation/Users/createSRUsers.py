from dbconnect.tabledefs.APPLICATIONAUTH import APPLICATIONAUTH
from dbconnect.tabledefs.GROUPUSER import GROUPUSER
from sqlalchemy import distinct, and_
from dbconnect import session_scope

userdict = {}
templist = []

def get_group_users(group):
    gu=[]
    with session_scope() as session:
        groupusers = session.query(distinct(GROUPUSER.userid)).filter(GROUPUSER.groupname == group).all()
        for x in groupusers:
            for y in x:
                gu.append(y)
    return gu

def check_dict(user):
    if user in userdict:
        return True
    else:
        return False

def get_users_groups(user):
    ug =[]
    with session_scope() as session:
        usersgroups = session.query(distinct(GROUPUSER.groupname)).filter(GROUPUSER.userid == user).all()
        for x in usersgroups:
            for y in x:
                ug.append(y)
    return ug
      
def add_groups(u, grplist):
    templist = userdict.get(u)
    for g in grplist:
        if g not in templist:
            templist.append(g)
    userdict[u] = templist
    
def get_users():
    with session_scope() as session:
        grps = session.query(distinct(APPLICATIONAUTH.groupname)).filter(APPLICATIONAUTH.app == 'CREATESR').all()
        #print grps
        for gn in grps:
            for n in gn:
                ulist = get_group_users(n)
                for u in ulist:
                    if not check_dict(u):
                        userdict[u]= []
                    grplist = get_users_groups(u)
                    add_groups(u, grplist)
    print userdict


if __name__ == '__main__':
   get_users()
