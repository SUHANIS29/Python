import time
import requests

def fetch_user():
    url = "https://api.freeapi.app/api/v1/public/randomjokes"
    retries = 3
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            data = response.json()
            
            if data.get("success") and "data" in data:
                joke_data = data["data"]
                joke_cat = joke_data.get("categories", "No category found")
                return joke_cat
            else:
                raise Exception("Failed to Fetch Joke Data")
        except requests.exceptions.Timeout:
            print(f"Timeout on attempt {attempt + 1}. Retrying...")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break
        time.sleep(2)  # Wait 2 seconds before retrying
    
    return None

def main():
    try:
        joke_cat = fetch_user()
        if joke_cat:
            print(f"Joke Category: {joke_cat}")
        else:
            print("Failed to fetch joke category after retries.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
