class User:
    websites = ["Twitter", "FaceBook", "Youtube"]
    avg_dict = {}
    for website in websites:
        avg_dict[website] = 0


    def __init__(self, times):
        self.websites = websites
        self.web_dict = {websites[i]: times[i] for i in range(len(websites))}
        self.calculateAverage(times)

    def calculateAverage(self, times):
        for website in websites:
            avg_dict[websites[website]] = (avg_dict.get(websites[website]) + times[website])/2

    def addWebsite(self, website):
        websites.append(website)
        self.websites.append(website)
        self.web_dict[self.website] = 0

    def removeWebsite(self, website):
        self.websites.pop(website)
        self.web_dict.pop(website)

    def updateWebsite(self, website, time):
        self.wed_dict[website] = time
        calculateAverage(time)



quit = False
websites = ["Twitter", "FaceBook", "Youtube"]
u1 = User([0,0,0])
while(not quit):
    action = input("user> ")
    if(action == "add_website"):
        website = input("enter website: ")
        u1.addWebsite(website)
    elif(action == "remove_website"):
        website = input("what website do you want to give to? ")
        u1.removeWebsite(website)
    elif(action == "update_website"):
        website = input("enter website: ")
        time = input("enter time: ")
        u1.updateWebsite(website, time)
    elif(action == "quit"):
        quit = True
