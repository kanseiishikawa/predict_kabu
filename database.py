import sqlite3

class database_python():
    def __init__(self, connnect_name):
        self.database_name = connnect_name
        self.db = sqlite3.connect(connnect_name)
        self.cursor = self.db.cursor()
        
    def cleatetable(self, table_name, data_element):
        base_command = "CREATE TABLE " + table_name + "("
        
        for i in range(0, len(data_element)):
            base_command += data_element[i]
            if i != len(data_element) - 1:
                base_command += ","
            else:
                base_command += ")"

        self.cursor.execute(base_command)

    def add(self, table_name, data):
        self.cursor.execute("SELECT * FROM " + table_name)
        element = self.cursor.description
        
        if len(element) != len(data):
            print("要素の数が違います")
            return False

        sql_command = "INSERT INTO " + table_name + "("
        value_command = "VALUES("
        for i in range(0, len(element)):
            sql_command += str(element[i][0])
            value_command += "?"
            if i != len(element) - 1:
                sql_command += ","
                value_command += ","
            else:
                sql_command += ") "
                value_command += ")"
                
        sql_command += value_command
        self.cursor.execute(sql_command, tuple(data))
        return True
    
def main():
    dp = database_python("test.db")
    aa = ["a", "b", "c"]
    dp.cleatetable("aaa", aa)
    dp.add("aaa", [1,2,3])
main()
