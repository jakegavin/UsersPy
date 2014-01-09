import re
import sys
import os

class User:
    def __init__(self, fn, ln, em):
        self.id = str(GenID())
        self.fn = fn
        self.ln = ln
        match = re.search('\w[\w\.]*@[\w\.]+\.+\w+', em)
        if match:
            self.em = em
        else:
            print('Invalid Email')
            sys.exit(1)
            
def Add(fn, ln, em):
    tmp = User(fn, ln, em)
    f = open('users.txt', 'a')
    f.write('id:'+ tmp.id + ' fn:' + tmp.fn + ' ln:' + tmp.ln + ' em:' + tmp.em + ' \n')
    f.close()

def GenID():
    if not os.path.exists('users.txt'):
        print 'Please create database file: users.txt'
        sys.exit(1)
    else:
        pass
    
    f = open('users.txt', 'r')
    user_text = f.read()
    ids_s = re.findall('id:(\d+)', user_text)
    ids = []
    for id in ids_s:
        ids.append(int(id))
    if not ids:
        newID = 1
    else:       
        newID = max(ids) + 1
    f.close()
    return newID

def ShowAllUsers():
    f = open('users.txt', 'r')
    for lines in f:
        info = re.findall('id:(\d+) fn:(\S+) ln:(\S*) em:(\S+)', lines)
        print 'ID: %s  Name: %s %s  Email: %s' % (info[0][0], info[0][1], info[0][2], info[0][3])

def DBID(idn):
    '''Delete a user from the list, given their ID number'''    
    if not isinstance(idn, basestring):
        idn = str(idn)
    else:
        pass
    
    f = open('users.txt', 'r')
    text = f.read()
    id_in = re.search('id:' + idn, text)
    f.close 
    
    if not id_in: 
        print 'ID not in database'
    else:
        f = open('users.txt', 'r')
        lines = f.readlines()    
        f.close()
        f = open('users.txt', 'w')
        for line in lines:
            if 'id:' + idn not in line:
                f.write(line)
            else:
                pass
        f.close()

def DBFN(fnn):
    '''Delete a user from the list, given their first name'''    
    f = open('users.txt', 'r')
    text = f.read()
    id_in = re.search('fn:' + fnn, text)
    f.close 
    
    if not id_in: 
        print 'Firstname not in database'
    else:
        f = open('users.txt', 'r')
        lines = f.readlines()    
        f.close()
        f = open('users.txt', 'w')
        for line in lines:
            if 'fn:' + fnn not in line:
                f.write(line)
            else:
                pass
        f.close()
    

def main():
    # Example showing how add function works
    Add('asd', 'sdf', 'sdf@sdf.com')
    Add('a12sd', 'sdf', 'sd3434f@sdf.com')
    Add('as12324d', 'sd342f', 'sd3434f@sdfo.m')
    ShowAllUsers()
    
    
    # Example showing how delete by ID works
    DBID('36')
    
    # Example showing how delete by first name works
    DBFN('asd')
    
    ShowAllUsers()

if __name__ == '__main__':
    main()