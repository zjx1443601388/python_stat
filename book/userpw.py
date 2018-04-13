#/usr/bin/env python
#coding:utf-8
'''
@auther:xiaoxin
date:2018-04-13
'''


db={}

def newuser():
    prompt = ' login desired: '
    while True:
        name=raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken, try another '
            continue
        else:
            break
        
    pwd=raw_input("passwd: ") 
    db[name]=pwd
    
def olduser():
    name = raw_input('login: ')
    if name in db.keys():
        pwd = raw_input('passwd: ')
        passwd = db.get(name)
        if pwd == passwd:
            print "welcome back", name
        else:
            print("login incorrect")
    else:
        print('you not login in')
        newuser()
        
def showmenu():
    prompt="""
    (N)ew User Login
    (E)exit User Login
    (Q)uit
    Enter choice: """
    
    done=False
    
    while not done:
        chosen=False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice= 'q'
            print('\nYou picked: [%s]' %choice)
            if choice not in 'neq':
                print('Invalid option,try again')
            else:
                chosen=True
                
        if choice == 'q':done=True
        if choice == 'n':newuser()
        if choice == 'e':olduser()
        
        
if __name__ == '__main__':
    showmenu()