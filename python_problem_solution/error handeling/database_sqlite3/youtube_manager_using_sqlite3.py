import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL                      
    )
''')

def list_videos():
    cursor.execute(" SELECT * FROM videos ")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute(" INSERT INTO videos (name, time) values (?, ?)", (name, time))   
    cursor.commit()

def update_video(video_ID, new_name, new_time):
    cursor.execute(" UPDATE videos SET name = ?, time = ? WHERE id = ?", (video_ID,new_name,new_time))
    cursor.commit()

def delet_video(video_ID):
    cursor.execute(" DELETE FROM videos WHERE id = ?", (video_ID, ))
    cursor.commit()

def main():
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Upadate a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice : ")


        if choice == 1:
            list_videos() 

        elif choice == 2:
            name = input(" Enter the new video name : ")
            time = input(" Enter the new video time : ")
            add_video(name,time)

        elif choice == 3:
            video_ID = input(" Enter video ID to update : ")
            name = input(" Enter the new video name : ")
            time = input(" Enter the new video time : ")
            update_video(video_ID,name,time)

        elif choice == 4:
            video_ID = input(" Enter video ID to delet : ")
            delet_video(video_ID)

        elif choice == 5:
            break

        else:
            print(" Invalid choice ")

    conn.close()

if __name__ == '__main__':
    main()