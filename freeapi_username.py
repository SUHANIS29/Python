import requests

def fetch_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        user_country = user_data["location"]["country"]
        return user_name, user_country
    else:
        raise Exception("Failed to Fetch User Data")

def main():
    try:
        user_name, user_country = fetch_user()
        
        print(f"Username: {user_name}\nCountry: {user_country}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
