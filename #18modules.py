#modules contain related functions and methods

#module is imported using 

#import nameofmodele
#or
#from nameofmodule import specificmethod

#if imported whole module...it is an object then you can use it via dot 
#like nameofmodule.specificfunction()

#if imported a specific function only 
#use it directly by calling it like...
#specificfunction()

import utils


find=[1,4,7,2,8,2,3,7,3,10000,9,0,67,8]
utils.findmax(find)

print(max(find))