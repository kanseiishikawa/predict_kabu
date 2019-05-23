import numpy as np
import sys
sys.path.append( "../" )
import database

class manegement():
    
    def __init__( self, money, database_name ):
        self.my_money = money
        self.database_access = database.database_python( database_name )

    def buy( self, num, year, month, day, math ):
        year = "year=" + year
        
        
        

        
