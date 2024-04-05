import sqlite3

def create_table(c):
    c.execute("CREATE TABLE IF NOT EXISTS Student(id_ INTEGER PRIMARY KEY ,name TEXT,gender TEXT)")
    print("Table created sucessfully.")

def insert_values(c):
    id_=int(input("Enter the ID:"))
    name=input("Enter the name:")
    gender=input("Enter the gender:")
    c.execute("INSERT INTO Student(id_,name,gender)VALUES(?,?,?)",(id_,name,gender))
    print("Values inserted sucessfully.")

def delete_row(c):
    id_=int(input("Enter the id of the student you want to delete:"))
    c.execute("DELETE FROM Student WHERE id_=?",(id_,))
    print("Roe deleted sucessfully")

def display_table(c):
    c.execute("SELECT * FROM Student")
    rows=c.fetchall()
    for i in rows:
        print(i)

def update_row(c):
    id_=int(input("Enter the id of the student whose details have to be updated:"))
    new_name=input("Enter the new name:")
    c.execute("UPDATE Student SET name=? WHERE id_=?",(new_name,id_))
    print("Row updated sucessfully")

def search_record(c):
    id_=input("Enter the id_ to search in the table:")
    c.execute("SELECT * FROM Student WHERE id_=?",(id_,))
    row=c.fetchone()
    if row:
        print("Record found:",row)
    else:
        print("Record not found.")

def main():
    conn=sqlite3.Connection("experiment07.db")
    c=conn.cursor()

    while True:
        print("\nMenu:")
        print("1. Create table \n2. Insert value \n3. Delete row \n4. Display table \n5. update value \n6. Search  \n7. Exit \n")

        choice=int(input("Enter your choice:"))

        if choice==1:
            create_table(c)
        elif choice==2:
            insert_values(c)
        elif choice==3:
            delete_row(c)
        elif choice==4:
            display_table(c)
        elif choice==5:
            update_row(c)
        elif choice==6:
            search_record(c)
        elif choice==7:
            break
        else:
            print("Invalid input:")

    conn.commit()
    conn.close()

if __name__=="__main__":
    main()
    
        
            



