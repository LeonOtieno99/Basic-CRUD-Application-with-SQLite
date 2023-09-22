import sqlite3
import sys

print('**************************************')
print('***  CRUD APPLICATION WITH SQLITE  ***')
print('**************************************')


#first page
def main():
    print('------MENU------')
    print('1.Create Records')
    print('2.Read Records')
    print('3.Update Records')
    print('4.Delete Records')
    print('5.Exit')

    task = int(input('Choose operation:\n'))

    match task:
        case 1:
            create()
        case 2:
            read()
        case 3:
            update()
        case 4:
            delete()
        case 5:
            exit()
        case _:
            print("Please select a value from the menu!")

class increment:
    def __init__(self):
        self.counter = 1
    def generate(self):
        current_id = self.counter
        self.counter += 1
        return current_id

id_generator = increment() #create instance of a class

def create():
    task_id = id_generator.generate() #assign method return to task_id
    task_name = input('Name of your task:\n')
    task_description = input('Describe your task:\n')

    cur.execute("INSERT INTO tasks VALUES (?,?,?)",
                (task_id, task_name, task_description))
    con.commit() #save
    print('Tasks created successfully')
    main()

def read():
    for row in cur.execute("SELECT Task_ID, Task_Name, Task_Description FROM tasks ORDER BY Task_ID"):
        task_id,task_name,task_desc = row
        print(f"|{task_id}| {task_name}: {task_desc}|")


    ans = input(('Want to go back to the main menu(y|n)'))
    if ans == 'y':
        main()
    else:
        exit()
    
def update():
    try:
        task_id = int(input('Enter Task ID number OF task you want to UPDATE:\n'))
        task_name = input('The updated name(Repeat name if you don\'t want to change):\n')
        task_description = input('Describe your updated task:\n')

        cur.execute("UPDATE tasks set Task_Name = ?, Task_Description = ? WHERE Task_ID = ?",
                        (task_name,task_description,task_id))
        con.commit()
        print('Tasks updated successfully')
        main()
    except:
        main()

def delete():
    try:
        task_id = int(input('Enter Task ID number of task you want to DELETE:\n'))

        cur.execute("DELETE FROM tasks WHERE Task_ID = ?",(task_id,))
        con.commit()
        print('Task Deleted successfully')
        main()
    except:
        main()

def exit():
    con.close()
    sys.exit()

con = sqlite3.connect("crud")
print('Succesfully connected to sqlite database')
cur = con.cursor()
table_name = "tasks"
try:
    cur.execute("CREATE TABLE tasks(Task_ID, Task_Name, Task_Description)")
    print(f'Table {table_name} created succesfully')
    main()
except:
    print(f'Table with similar name \'{table_name}\' already exist')
    main()




