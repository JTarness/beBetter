class User:
    websites = ["Twitter", "FaceBook", "Youtube"]



    def __init__(self, times):
        self.websites = User.websites
        self.web_dict = {}
        for i, website in zip(times, self.websites):
            self.web_dict[website] = times[i]
        #User.calculateAverage(times)

    #@classmethod
    #def calculateAverage(cls, times):
     #   for i, website in zip(times, websites):
      #      cls.avg_dict[website] = (cls.avg_dict.get(website) + times[i])/2

    def addWebsite(self, website):
        User.websites.append(website)
        self.websites.append(website)
        self.web_dict[self.website] = 0

    def removeWebsite(self, website):
        self.websites.pop(website)
        self.web_dict.pop(website)

    def updateWebsite(self, website, time):
        self.web_dict[website] = time
        #User.calculateAverage(time)

    def viewData(self):
        print(self.web_dict)



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
        print("Time was updated")
    elif(action == "view"):
        u1.viewData()
    elif(action == "quit"):
        quit = True
