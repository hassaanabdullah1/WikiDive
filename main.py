import wikipedia
import webbrowser
import requests
selected_result = ""
print("---WikiDive v1.0---")

def search_topic(topic):
    try:
        searching = wikipedia.search(topic) #searches for topic entered by user
        #changes all members of the list to lower case
        low_searching = []
        for x in searching:
            low_searching.append(x.lower())

        #prints the results as a numbered list
        print("Search results:")
        for number, result in enumerate(searching, start=1):
            print(f"{number}.{result}")

        return low_searching
    except wikipedia.exceptions.DisambiguationError:
         print("Your search was too broad!")
         return None
    except Exception as e:
        print(f"Failed to get results error: {e}")
        main()

def select_result(topic):
    #prompts the user to select which result to view article about
    results = search_topic(topic)
    if results == None:
        print("NO results found!")
        return
    else:
        while True:
            try:
                ask_user_result =  input("Select the topic you want to view: ")
                if ask_user_result.isdigit(): #if user enters digit, selects result at that index
                    ask_user_result = int(ask_user_result) - 1
                    selected_result = results[ask_user_result]
                    get_summary(selected_result)
                    break
                else:
                    ask_user_result = results.index(ask_user_result.lower())
                    selected_result = results[ask_user_result]
                    get_summary(selected_result)
                    break
            except IndexError:
                print(f"Plese enter numbers from 1-{len(results)}")
            except ValueError:
                print(f"Please only enter the search results or enter numbers from 1-{len(results)}")
        return selected_result        
    
#gives the summary of the topic selected by user
def get_summary(topic):
    while True:    
        try:
            summary = wikipedia.summary(topic)
            if summary:
                print(f"\n'{topic.title()}' summary:")
                print(summary.strip()+"\n")
                break
        except wikipedia.exceptions.PageError:
            print("Page Not Found! Try another search.")
            new_topic = input("Enter a new topic: ").strip()
            select_result(new_topic) 
            

#displays full page if user wants (prompted in main() function)
def full_page(topic):
    try:        
        full_page = input("Do you want to see full page? (Y/N)")
        if full_page.lower() == "y":
            print("Directing to full page...")
            page = wikipedia.page(topic)
            webbrowser.open(page.url)
    except wikipedia.exceptions.PageError:
        print("Page doesn't exist!")

#checks if the internet is connected, called in the main function after getting input
def check_internet():
    url = 'https://www.duckduckgo.com/'
    time_out = 10
    try:
        request = requests.get(url, timeout=time_out)
        if request:
            return True
    except (requests.ConnectionError, requests.Timeout):
        return False

#takes the initial input from user and prompts if user wants to view full page afterwards
def main():
    while True:
        topic = input("Enter topic to search for: ").strip().lower()
        if topic == "":
            print("Please enter term to search!")
        else:
            internet = check_internet()
            if internet == True:
                selected_result = select_result(topic)
                full_page(selected_result)
                again = input("Do you want to search for another? (Y/N)").strip().lower()
                if again != "y":
                    break
                else:
                    print("OK...Let's go!")
            else:
                print('\nPlease connect to the internet!\n')

#start the program
if __name__ == '__main__':
    main()
