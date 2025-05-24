import sqlite3

conn = sqlite3.connect('youtube_videos_db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_all_videos():
    print("\n")
    print("*" * 70)
    cursor.execute('SELECT * FROM videos')
    rows = cursor.fetchall()  # <-- Properly call fetchall()

    if not rows:  # <-- Check if the list is empty
        print("No videos in the table")
    else:
        for row in rows:
            print(row)

    print("*" * 70)


def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (? , ?)",(name,time)) 
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute('UPDATE videos SET   name = ?, time = ? WHERE id = ?',(new_name,new_time,video_id))
    conn.commit()
    
def delete_video(video_id):
    cursor.execute('DELETE FROM videos WHERE ID = ? ',(video_id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube manager app | Choose an option")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. exit app")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos()
            case "2":
                name = input("Enter name of the video: ")
                time = input("Enter time of the video")
                add_video(name,time)
            case "3":
                video_id = input("Enter the id of the video you want to update")
                name = input("Enter the new name of the video")
                time = input('Enter the new time of the video ')
                update_video(video_id,name,time)
            case "4":
                video_id = input("Enter the id of the video you want to update")
                delete_video(video_id)
            case "5":
                break
            case _:
                print("Invalid choice")

    conn.close()           
            



if __name__ == "__main__":
    main()