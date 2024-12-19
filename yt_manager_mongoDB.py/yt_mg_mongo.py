import pymongo
from bson import ObjectId


client = pymongo.MongoClient("mongodb+srv://youtubepy:root@cluster0.mfzqj.mongodb.net/")
db = client["ytmanager"]
video_collection = db["videos"]
# print(video_collection)
def list_vid():
    for vid in video_collection.find():
        print(f"id: {vid['_id']}, Name: {vid['name']}, Time: {vid['time']}")

def add_vid(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_vid(index, new_name, new_time):
    video_collection.update_one({'_id': ObjectId(index)}, {"$set": {"name": new_name, "time": new_time}})

def del_vid(index):
    video_collection.delete_one({"_id": ObjectId(index)})

def main():
    while True:
        print("\nYoutube Manager")
        print("1. List all YouTube Videos")
        print("2. Add a YouTube Video")
        print("3. Update a YouTube Video Details")
        print("4. Delete a YouTube Video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            list_vid()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_vid(name, time)
            print("Video added successfully.")
        elif choice == '3':
            list_vid()
            index = input("\nEnter video ID to update video: ")
            name = input("Enter updated name: ")
            time = input("Enter updated time: ")
            update_vid(index, name, time)
            print("Video updated successfully.")
        elif choice == '4':
            list_vid()
            index = input("\nEnter video ID to delete video: ")
            del_vid(index)
            print("Video deleted successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()
