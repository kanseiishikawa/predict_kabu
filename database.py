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
        self.db.commit()
        
        return True

    def take_out(self, key_select, key_conditions, table_name):
        sql_command = "SELECT "
        
        for i in range(0, len(key_select)):
            sql_command += key_select[i]
            if i != len(key_select) - 1:
                sql_command += ","

            sql_command += " "
            
        sql_command += "FROM " + table_name

        if(len(key_conditions) != 0):
            sql_command += " WHERE"
            for i in range(0, len(key_conditions)):
                sql_command += " " + key_conditions[i]
                if i != len(key_conditions) - 1:
                    sql_command += " AND"
        print(sql_command)
        self.cursor.execute(sql_command)
        return list(self.cursor.fetchall())
    
def main():
    dp = database_python("test.db")
    aa = ["a", "b", "c", "d"]
    dp.cleatetable("aaa", aa)
    dp.add("aaa", [1,2,3,4])
    dp.add("aaa", [3,2,3,5])
    ss = dp.take_out(["a", "b"], ["a=1", "b=2"],"aaa")
    print(ss[0])
main()
