#!/usr/bin/env python
import os
import shutil
import stat

def Start():
    while 1:
        inp = raw_input()
        l = inp.split(' ')
        if l.__len__() == 2 and l[1] != '-l' and l[0] == 'ls':		# i.e. inp=ls <name>
            if not os.path.isdir(l[1]):				# if inp=ls <file name>
                print l[1]
            else:							#if inp=ls <folder name>
                rec = os.listdir(l[1])
                rec.sort()
                for i in rec:
                    print i, "\t",
                print "\n",
        elif l.__len__() == 1 and l[0] == 'ls':				# if inp=ls
            rec = os.listdir('.')
            rec.sort()
            for i in rec:
                print i, "\t",
            print "\n",
        elif l.__len__() == 3 and l[0] == 'cp':				# i.e. inp= cp <source> <destination>
            if os.path.isdir(l[1]):
                print "cp : omitting directory '", l[1], "'",
            else:
                shutil.copy2(l[1], l[2])
        elif l.__len__() == 3 and l[0] == 'mv':				#if inp=mv src dest
            shutil.move(l[1], l[2])
        elif l.__len__() == 2 and l[0] == 'rm':				#if inp=rm file
            if os.path.isdir(l[1]):
                print "rm: cannot remove '", l[1], "': Is a directory",
            else:
                os.remove(l[1])
        elif l.__len__() == 4 and l[0] == 'cp' and l[1] == '-r':
            if os.path.isdir(l[2]):
                shutil.copytree(l[2], l[3])
            else:
                shutil.copy2(l[2], l[3])
"""		elif(l.__len__()==3 and l[0]=='ls' and l[1]=='-l'):
			rec = os.listdir(l[2])
			rec.sort()
			for i in rec.sort():
				row=""
				if(os.isdir(i)):
					row=row,'d',
				per=oct(os.stat(i).st_mode)[-3:]"""





if __name__ == "__main__":
    Start()
