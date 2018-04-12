#/usr/bin/env python
#coding:utf-8
'''
date:2018-04-12
@auther:xiaoxin
'''


"""
堆栈先进后出

"""


stack = []

def pushit():
    stack.append(raw_input('Enter a new string:').strip())


def popit():
    if len(stack) == 0:
        print 'cannot pop from an empty stack'
    
    else:
        print 'remove [',`stack.pop()`,']' 
    
def viewstack():
    print stack

CMDS = {'u':pushit,'o':popit,'v':viewstack}

def showmenu():
    pr="""
    p(U)sh
    p(O)p
    (V)iew
    (Q)uit
    
    Enter choice: """
    
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            
            except(EOFError,KeyboardInterrupt,IndentationError):
                choice = 'q'
                
            print '\nYou picked:[%s]' %choice
            
            if choice not in 'uovq':
                print 'Invalid option,try again' 
            else:
                break;
            
        if choice == 'q':
            break;
        
        CMDS[choice]()
        
if __name__ == '__main__':
    showmenu()      
        
    
