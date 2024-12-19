import sqlite3
con=sqlite3.connect('yt_videos.db')
cur=con.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    time TEXT NOT NULL
)
''')

def list_vid():
    cur.execute("SELECT * FROM videos")
    rows = cur.fetchall()
    if rows:  # Check if the list is not empty
        print("\nAvailable Videos:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Duration: {row[2]}")
    else:
        print("\nNo videos available.")


def add_vid(name,time):
  cur.execute("Insert into videos(name,time)values (?,?)",(name,time))
  con.commit()

def update_vid(index,new_name,new_time):
 
  cur.execute("Update videos set name=?,time=? where id=?",(new_name,new_time,index))
  con.commit()
  

def del_vid(index):
  
  cur.execute("Delete from videos where id=?",(index,))
  con.commit()

def main():
 while True:
    print("\nYoutube Manager with DB")
    print("1.List all youtube Videos")
    print("2.Add a Youtube Video")
    print("3.Update a Youtube Video Details")
    print("4.Delete a Youtube Video")
    print("5.Exit")
    choice=input("Enter your choice :")
    if choice=='1':
      list_vid()
    elif choice=='2':
      name= input("Enter video name: ")
      time=input("Enter video time: ")
      add_vid(name,time)
      print("Video added succesfully")

    elif choice=='3':
      list_vid()
      index=input("\nEnter video ID to update video: ")
      name= input("Enter updated name: ")
      time=input("Enter updated time: ")
      update_vid(index,name,time)
      print("Video updated succesfully")

    elif choice=='4':
      list_vid()
      index=input("\nEnter video ID to delete video: ")
      del_vid(index)
      print("Video deleted succesfully")
    
    elif choice=='5':
      break

    else:
      print("Invalid Choice")
 con.close()
if __name__=="__main__":
  main()