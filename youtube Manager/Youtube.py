import json

def load_data():
  try:
    with open('youtube.txt','r') as file:
      test=json.load(file)
      # print(type(test))
      return test
  except FileNotFoundError:
    print("File not found. Returning an empty list.")
    return []

def save_data(videos):
  with open('youtube.txt','w') as file:
    json.dump(videos , file)

def list_vid(videos):
    print("\n")
    print("*"*70)
    for index, video in enumerate(videos,start=1):
      print(f"{index}.{video['name']}, Duration:{video['time']}")  #created dict of name and time as mapping req
    print("\n")
    print("*"*70)

def add_vid(videos):
  name=input("Enter video name:\n")
  time=input("Enter video time:")
  videos.append({'name':name,'time':time})
  save_data(videos)
  print("Video added Succesfully!")
  
def update_vid(videos):
  list_vid(videos)
  index=int(input("Enter the video number to update:"))
  if 1<=index<=len(videos):
    name=input("Enter name of new video: ")
    time=input("Enter time of new video: ")
    videos[index-1]={'name':name,'time':time}
    save_data(videos)
    print("Video updated Succesfully!")
    
    

  else:
    print("Invalid Video Index selected")


def del_vid(videos):
  list_vid(videos)
  index=int(input("Enter the video number to delete the video:"))
  if 1<=index<=len(videos):
    del videos[index-1]
    save_data(videos)
    print("Video deleted Succesfully!")

  else:
    print("Invalid Video Index selected")


def main():


  videos=load_data()
  while True:
    print("\nYoutube Manager")
    print("1.List all youtube Videos")
    print("2.Add a Youtube Video")
    print("3.Update a Youtube Video Details")
    print("4.Delete a Youtube Video")
    print("5.Exit")
    choice=input("Enter your choice :")
    # print(videos)
    match choice:
      case '1':
        list_vid(videos)
      case '2':
        add_vid(videos)
      case '3':
        update_vid(videos)
      case '4':
        del_vid(videos)
      case '5': 
        break
      case _:
        print("Invalid choice") 
if __name__=="__main__":
  main()