'''
The functions support After Log-in
'''

'''
Import
'''
import numpy as np
#from f_BeforeLogin import accFullName
#from f_BeforeLogin import readDictionary
import f_BeforeLogin as b_login

#Variables
pending_requests = {}
accFriends = {} #Will connect the friends list (below) to the username of user in a dictionary format
friendsList = [] #Will store the list of friends for a user
'''
Functions
'''

#This function to gives additional options after login is successful
def addOptions(username):

    ##ADD A VIEW PENDING FRIEND REQUEST OPTION
    ##That option should check the requests dictionary (that loaded from the requests.npy file) to see if their username has
    ##an attached requests (can be a function)

    print("\n")
    print("Welcome! What would you like to do?")
    print("1. Search for a job/internship")
    print("2. Find someone you know")
    print("3. Learn a new skill")
    print("4. InCollege Important Links")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Would you like to search or post a job/internship?")
        print("1. Search")
        print("2. Post a job")
        
        choiceJob = input("Enter your job choice: ")
        
        if choiceJob == "1":
            # Load job postings for searching
            loadJobPostings()
            print("Here are the available job postings:")
            for index, job in enumerate(jobPostings, start=1):
                print(f"Job {index}: {job['title']} - {job['description']} - {job['employer']} - {job['location']} - {job['salary']}")
                
        elif choiceJob == "2":            
            postJob(username)


    ##THIS IS WHERE THE FIND BY NAME, MAJOR, UNIVERSITY OPTION SHOULD GO
    elif choice == "2": 
        ##Must create a an option for user to store their major, university and last name in numpy file
        ##Should allow user to run through the numpy file of whichever option gets chosen to find username
        ##A list of full names will get printed (by association from usernames)
        ##Then it should allow the user to send a friend request to a chosen user which will store a pending request
        ##for that user in the requests.npy file

        print("Find someone you know option is currently under construction.")





    elif choice == "3":
        print("Here are 5 skills you can learn:")
        print("1. Programming")
        print("2. Prompt Engineering")
        print("3. 3D Modeling & Simulation")
        print("4. Data Analysis")
        print("5. Language Learning")
        print("6. Show my Network")
        print("7. Return to the previous level. . .")

        #Presents the user with the option to choose a skill
        choiceSkill = input("Enter your skill choice: ")

        if choiceSkill == "1":
            print("The Programming option is currently under construction.")

        elif choiceSkill == "2":
            print("The Prompt Engineering option is currently under construction.")

        elif choiceSkill == "3":
            print("The 3D Modeling & Simulation option is currently under construction.")

        elif choiceSkill == "4":
            print("The Data Analysis option is currently under construction.")

        elif choiceSkill == "5":
            print("The Language Learning option is currently under construction.")


        ##MOVE DIS   
        elif choiceSkill == "6":
            showMyNetwork(username)
            disconnectOption = input("Would you like to disconnect from anyone in your network? (yes/no): ")
            if disconnectOption.lower() == "yes": #Add the choice of asking who they want to disconnect from
                disconnectFromFriendOption(username) #Will not work without the choice of who the person wants to disconnect from



        else:
            print("7. Returning to the previous level. . .")
            addOptions(username)

    # elif choice == "4":
    #     guestControls(username)

    elif choice == "4":
        goingBackLoggedIn = handleImportantLinks(username)

        #Checks if the user wants to come back to main screen after clicking InCollege Important Links
        if goingBackLoggedIn == 0:
            addOptions(username)

        else: #Or go back to Important Links option
            handleImportantLinks()
        

    else:
        print("Invalid choice.")

    return 1

# Function to display connected friends
def showMyNetwork(username):
    if username in accFriends:
        print("Your network:")
        for friend in accFriends[username]:
            print(friend)
    else:
        print("You haven't connected with anyone yet.")

# Function to handle disconnection from friends
def disconnectFromFriend(username, friend_to_disconnect):
    if username in accFriends and friend_to_disconnect in accFriends[username]:
        accFriends[username].remove(friend_to_disconnect)
        if friend_to_disconnect in accFriends and username in accFriends[friend_to_disconnect]:
            accFriends[friend_to_disconnect].remove(username)
        print(f"You have disconnected from {friend_to_disconnect}.")
    else:
        print(f"You are not connected with {friend_to_disconnect}.")



# Function to post a job
def postJob(username):
    jobPostings = loadJobPostings()
    if len(jobPostings) >= 5:
        print("Maximum number of job postings reached.")
        return 0

    print("Posting a job:")
    title = input("Enter job title: ")
    description = input("Enter job description: ")
    employer = input("Enter employer name: ")
    location = input("Enter job location: ")
    salary = input("Enter job salary: ")

    job = {
        "title": title,
        "description": description,
        "employer": employer,
        "location": location,
        "salary": salary,
        "posted_by": username
    }

  

    job = np.array(job)  #Converts job to a numpy array 
    jobPostings = np.concatenate((jobPostings, np.expand_dims(job, axis=0)), axis=0) #Concatenates job array

    print("Job posted successfully.")

    # Save the updated job postings
    np.save("job_postings.npy", jobPostings)
    
    return 1

# Load job postings
def loadJobPostings():
    global jobPostings
    try:
        jobPostings = np.load("job_postings.npy", allow_pickle=True)
    except FileNotFoundError:
        jobPostings = []

    return jobPostings

# Dictionary to store user settings
user_settings = {}

# Function to load user settings
def loadUserSettings():
    global user_settings
    try:
        user_settings = np.load("user_settings.npy", allow_pickle=True).item()
    except FileNotFoundError:
        user_settings = {}


# Function to toggle features on and off
def toggleFeature(username, feature):
    if username not in user_settings:
        user_settings[username] = {"email": True, "sms": True, "targeted_advertising": True}

    if user_settings[username][feature]:
        user_settings[username][feature] = False
        print(f"{feature.capitalize()} notifications have been turned off.")
    else:
        user_settings[username][feature] = True
        print(f"{feature.capitalize()} notifications have been turned on.")

    # Save the updated user settings
    np.save("user_settings.npy", user_settings)
    return 1

        
# Function to handle guest controls
def guestControls(username):
    print("\nGuest Controls:")
    print("1. Email Notifications")
    print("2. SMS Notifications")
    print("3. Targeted Advertising")
    print("4. Return to the previous level. . .")

    choice = input("Enter your choice: ")

    if choice == "1":
        toggleFeature(username, "email")
        addOptions(username)
    elif choice == "2":
        toggleFeature(username, "sms")
        addOptions(username)
    elif choice == "3":
        toggleFeature(username, "targeted_advertising")
        addOptions(username)
    elif choice == "4":
        addOptions(username)
    else:
        print("Invalid choice.")
        guestControls(username)
    return 1




#Verifies if the user is inputting a number in the acceptable range (a more general purpose one needs to be made)
def inputValidation(prompt, valid_options):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in valid_options:
                return user_input
            print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


#Displays all the InCollege Important Links (if 5 is chosen)
def displayImportantLinks():
    print("\nInCollege Important Links:")
    print("1. Copyright Notice")
    print("2. About")
    print("3. Accessibility")
    print("4. User Agreement")
    print("5. Privacy Policy")
    print("6. Cookie Policy")
    print("7. Copyright Policy")
    print("8. Brand Policy")
    print("9. Guest Controls")
    print("10. Languages")
    print("0. Back")



 #Gives user the chance to go back up a level in the menu or exit entirely#
def userImportantExit(userChoice, username):
    if userChoice == 1:
        handleImportantLinks(username)
        
    else:
        return 0
    

#Names the files to be printed according to user selection
def returnFilename(number):
    if number == 1:
        file = "Copyright_Notice.txt"
    
    elif number == 2:
        file = "About.txt"

    elif number == 3:
        file = "About.txt"

    elif number == 4:
        file = "User_Agreement.txt"

    elif number == 5:
        file = "Privacy_Policy.txt"

    elif number == 6:
        file = "Cookie_Policy.txt"
    
    elif number == 7:
        file = "Copyright_Policy.txt"

    elif number == 8:
        file = "Brand_Policy.txt"

    return file


###Addded after Epic 3: Menus###

# Function to read user settings from a file
def readUserLangSettings():
    try:
        with open("Language_Choice.txt", "r") as file:
            language = file.read().strip()

    #If the file doesn't exist, it will return default language (English)
    except FileNotFoundError:
        language = "English"

    return language


#Function to save user language choice to a text file
def saveUserLangSettings(language):
    with open("Language_Choice.txt", "w") as file:
        file.write(language)

#Function to deal with the language selection
def langSelect():
    #has the user select their language preference
    print("Select your preferred language: \n")
    print("1. English\n")
    print("2. Spanish\n")
    langChoice = input("\nEnter your choice: ")

    #Sets the language choice to 1 if English and 2 if Spanish
    if langChoice == "1":
        return "English"
    
    elif langChoice == "2":
        return "Spanish"
    
    else:
        print("Invalid choice")
        return None



#Function to display file content
def getFile(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print(content)



#Takes the selection of user in main.py and if it is 5 (Important Links, then it displays the Important Links menu)
def handleImportantLinks(username):

    #This is to display the InCollege Important Links before the user is logged in 
    displayImportantLinks()
    back = 0

    #User chooses between 0 and 10 for various options
    importantLinkChoice = inputValidation("\n\nPlease select the number corresponding to your choice: ", list(range(11)))

    #Displays the content for every option chosen
    if importantLinkChoice == 1:

        
        print("\nCopyright Notice\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn, username)

    elif importantLinkChoice == 2:
        
        print("\nAbout\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn, username)

    elif importantLinkChoice == 3:
        print("\nAccessibility\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn, username)

    elif importantLinkChoice == 4:
        print("\nUser Agreement\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn, username)

    elif importantLinkChoice == 5:
        print("\nPrivacy Policy\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn, username)

    elif importantLinkChoice == 6:
        print("\nCookie Policy\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn, username)

    elif importantLinkChoice == 7:
        print("\nCopyright Policy\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn, username)

    elif importantLinkChoice == 8:
        print("\nBrand Policy\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn, username)

    elif importantLinkChoice == 9:
        print("\nGuest Controls\n")
        guestControls(username)
        
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn, username)

    elif importantLinkChoice == 10:
        print("\nLanguages\n")

        # Read user language choice
        userLanguage = readUserLangSettings()

        print("Welcome!")
        print("Your current language setting:", userLanguage)
        
        print("Please select an option:\n1. Select a new language setting \n2. Keep current language setting\n")
        option = input("Enter your choice: ")

        #If the user wants to change the language setting
        if option == "1":
            newLanguage = langSelect()

            #When user language choice is updated successfully
            if newLanguage:
                print("\nLanguage updated successfully!")
                saveUserLangSettings(newLanguage)

        #User does not change language setting
        elif option == "2":
            print("Your current language setting is still: ", userLanguage)

        else:
            print("Invalid option")
            
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn, username)

    elif importantLinkChoice == 0:
        return 0

   
    
    return back
        


##EPIC 4 ADD ON
def writeFriendsList():
    #Saves the names of people in the user's friends list to a numpy files
    np.save("accFriends.npy", accFriends)
    return 1

def readFriendsList():
    # print(" ")
    #Reads the names of people in the user's friends list from a numpy files and loads it into accFriends dictionary
    py_dict = np.load("accFriends.npy", allow_pickle = "TRUE")

    global accFriends

    accFriends = py_dict.item()
    return 1





















        
# Function to display connected friends
def showMyNetwork(username):
    if username in accFriends:
        print("Your network:")
        for friend in accFriends[username]:
            print(friend)
    else:
        print("You haven't connected with anyone yet.")

# Function to handle disconnection from friends
def disconnectFromFriendOption(username, friend_to_disconnect):
    if username in accFriends and friend_to_disconnect in accFriends[username]:
        accFriends[username].remove(friend_to_disconnect)
        accFriends[friend_to_disconnect].remove(username)
        print(f"You have disconnected from {friend_to_disconnect}.")
    else:
        print(f"You are not connected with {friend_to_disconnect}.")

# Function to find users by last name
def findUsersByLastName(last_name):
    # Load the full names and usernames from the file
    try:
        fullnames = np.load("fullnames.npy", allow_pickle=True).item()
    except FileNotFoundError:
        print("Error: Fullnames file not found.")
        return []

    # Search for users based on the last name
    matching_users = []
    for user, fullname in fullnames.items():
        # Check if the last name matches
        if last_name.lower() in fullname.lower():
            matching_users.append(user)

    return matching_users

# Function to find users by major
def findUsersByMajor(major):
    # Load user information
    user_info = b_login.readUserInformation()

    # Search for users based on the major
    matching_users = []
    for user, info in user_info.items():
        if 'major' in info and major.lower() in info['major'].lower():
            matching_users.append(user)

    return matching_users

# Function to find users by university
def findUsersByUniversity(university):
    # Load user information
    user_info = b_login.readUserInformation()

    # Search for users based on the university
    matching_users = []
    for user, info in user_info.items():
        if 'university' in info and university.lower() in info['university'].lower():
            matching_users.append(user)

    return matching_users

# Function to send friend request
def sendFriendRequest(sender, receiver):
    if receiver in pending_requests:
        pending_requests[receiver].append(sender)
    else:
        pending_requests[receiver] = [sender]
    print("Friend request sent successfully.")

# Function to display pending friend requests
def displayPendingRequests(username):
    if username in pending_requests:
        print("Pending friend requests:")
        for request in pending_requests[username]:
            print(request)
    else:
        print("No pending friend requests.")

# Function to handle accepting or rejecting friend requests
def handleFriendRequests(receiver, sender, decision):
    if decision.lower() == 'accept':
        # Add sender to receiver's friends list
        if receiver in accFriends:
            accFriends[receiver].append(sender)
        else:
            accFriends[receiver] = [sender]
        # Add receiver to sender's friends list
        if sender in accFriends:
            accFriends[sender].append(receiver)
        else:
            accFriends[sender] = [receiver]
        # Remove sender from pending requests of receiver
        if receiver in pending_requests:
            pending_requests[receiver].remove(sender)
        print("Friend request accepted.")
    elif decision.lower() == 'reject':
        # Remove sender from pending requests of receiver
        if receiver in pending_requests:
            pending_requests[receiver].remove(sender)
        print("Friend request rejected.")
    else:
        print("Invalid decision.")