from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib, os


class websiteServer(BaseHTTPRequestHandler):
    
    pathsToURL = { "home": "home.html",
    "home?answer" : ["1990", "stage2", "home?answer", "home", "Whoops! Incorrect, please try again", "In which year did our president join the university" ], 
    
    "stage2" : ["1985", "pathIfCorrect", "stage2?answer", "stage2",  "That was easy, here is a harder one", "What year was ADHC founded?"],
    "stage2?answer" : ["1985", "stage3", "stage2?answer","stage2", "Not quite.... try again", "What year was ADHC founded?"],

    "stage3" : ["my.njit.edu", "stage4", "stage3?answer", "stage3",  "Ready for a deep dive?", "What is the URL you would to go to see financial aid and register for classes. _._._, no http://"],
    "stage3?answer" : ["my.njit.edu", "stage4", "stage3?answer","stage3", "WRONG try again", "What is the URL you would to go to see financial aid and register for classes. _._._, no http://"],
    
    "stage4" : ["tutoring", "stage5", "stage4?answer", "stage4",  "Very nice very nice, im impressed", "There is a math professor whose last name rhymes with \"Borus\", what is he the director of?"],
    "stage4?answer" : ["tutoring", "stage5", "stage4?answer","stage4", "WRONG try again", "There is a math professor whose last name rhymes with \"Borus\", what is he the director of?"],

    "stage5" : ["america+east", "stage6", "stage5?answer", "stage5",  "The math tutoring center is a great resource!", "NJIT recently joined a new athleic confrence, what is its name?"],
    "stage5?answer" : ["america+east", "stage6", "stage5?answer","stage5", "WRONG try again", "NJIT recently joined a new athleic confrence, what is its name?"],

    "stage6" : ["19", "stage7", "stage6?answer", "stage6",  "When they open again, athleic games on campus are always fun!", "How many athletic teams (D1 and club) does NJIT have?"],
    "stage6?answer" : ["19", "stage7", "stage6?answer","stage6", "WRONG try again", "How many athletic teams (D1 and club) does NJIT have?"],

    "stage7" : ["gitc", "stage8", "stage7?answer", "stage7",  "GO HIGHLANDERS!!", "What is the north most building on our campus (Acronym)"],
    "stage7?answer" : ["gitc", "stage8", "stage7?answer","stage7", "WRONG try again", "What is the north most building on our campus (Acronym)"],

    "stage8" : ["2", "stage9", "stage8?answer", "stage8",  "GITC is where the makerspace is!", "What stage of the pandemic recovery is NJIT in?"],
    "stage8?answer" : ["2", "stage9", "stage8?answer","stage8", "WRONG try again", "What stage of the pandemic recovery is NJIT in?"],

    "stage9" : ["highlanderhub.com", "stage10", "stage9?answer", "stage9",  "Always stay up to date on NJIT's pandemic recovery efforts!", "If I want to search for clubs, what website do I go to? __._, no http://"],
    "stage9?answer" : ["highlanderhub.com", "stage10", "stage9?answer","stage9", "WRONG try again", "If I want to search for clubs, what website do I go to?  __._, no http://"],

    "stage10" : ["njitgreencontact%40gmail.com", "stage11", "stage10?answer", "stage10",  "Highlander hub is a great resource!", "What is the contact email for NJIT Green?"],
    "stage10?answer" : ["njitgreencontact%40gmail.com", "stage11", "stage10?answer","stage10", "WRONG try again", "What is the contact email for NJIT Green?"],

    "stage11" : ["is465", "stage12", "stage11?answer", "stage11",  "So you know how to use a search bar... lets see if you can solve riddles.", "What is the last course in this, alphabetically last, major's curriculum."],
    "stage11?answer" : ["is465", "stage12", "stage11?answer","stage11", "WRONG try again", "What is the last course in this, alphabetically last, major's curriculum."],

    "stage12" : ["911", "stage13", "stage12?answer", "stage12",  "That was tough... I will lighten up", "What phone number do you call if you have an emergency on campus?"],
    "stage12?answer" : ["911", "stage13", "stage12?answer","stage12", "WRONG try again... in true emergency’s  always call this number and state \"Im at NJIT\"", "What phone number do you call if you have an emergency on campus?"],

    "stage13" : ["2018", "stage14", "stage13?answer", "stage13",  "Not bad... 911 is something you should have known however...", "This honors scholar was \"incredibly appreciative\" for the honors college. What year did he graduate?"],
    "stage13?answer" : ["2018", "stage14", "stage13?answer","stage13", "WRONG try again...", "This honors scholar was \"incredibly appreciative\" for the honors college. What year did he graduate?"],

    "stage14" : ["34", "stage15", "stage14?answer", "stage14",  "Nice find. Some day that will be you!", "Im interested in the university's policy on research and intellectual property... how big (in KB) is the document im looking for?"],
    "stage14?answer" : ["34", "stage15", "stage14?answer","stage14", "WRONG try again...", "Im interested in the university's policy on research and intellectual property... how big (in KB) is the document im looking for?"],

    "stage15" : ["", "stage16", "stage15?answer", "stage15",  "", ""],
    "stage15?answer" : ["", "stage16", "stage15?answer","stage15", "WRONG try again...", ""],

    "stage16" : ["", "stage17", "stage16?answer", "stage16",  "", ""],
    "stage16?answer" : ["", "stage17", "stage16?answer","stage16", "WRONG try again...", ""],

    "stage17" : ["", "stage18", "stage17?answer", "stage17",  "", ""],
    "stage17?answer" : ["", "stage18", "stage17?answer","stage17", "WRONG try again...", ""],

    "stage18" : ["", "stage19", "stage18?answer", "stage18",  "", ""],
    "stage18?answer" : ["", "stage19", "stage18?answer","stage18", "WRONG try again...", ""],

    "stage19" : ["", "stage20", "stage19?answer", "stage19",  "", ""],
    "stage19?answer" : ["", "stage20", "stage19?answer","stage19", "WRONG try again...", ""],

    "stage20" : ["", "winner", "stage20?answer", "stage20",  "", ""],
    "stage20?answer" : ["", "winner", "stage20?answer","stage20", "WRONG try again...", ""]

    }

    host = "localhost:12345"
    def do_GET(self):
        reply = "def"
        path = str(self.path)[1:]
        print(path)
        pageFound = False
        for page in self.pathsToURL:
            if page == path:
                pageFound = True
                reply = self.getHtmlDocToReply(self.pathsToURL[page])

        if pageFound == False:
            i1 = path.find("=")
            if i1 > 0:
                pathNoAns = path[0:i1]
                ans = path[i1+1:].lower()
                print(pathNoAns, ans)
                for page in self.pathsToURL:
                    if page == pathNoAns:
                        pageFound = True
                        print(page, self.pathsToURL[page][0])

                        if ans == self.pathsToURL[page][0]:
                            correctPath = self.pathsToURL[page][1]
                            
                        else:
                            correctPath = self.pathsToURL[page][2]

                        if correctPath == "winner":
                            reply = self.getHtmlDocToReply("winner.html")
                        else:
                            genArray = self.pathsToURL[correctPath]

                            heading = genArray[3]
                            line1 = genArray[4]
                            line2 = genArray[5]

                            reply = self.generateQuestionHTML(heading, line1, line2)
                
        if pageFound == False:
            reply = self.getHtmlDocToReply("home.html")

        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(reply.encode())

    def _generateUrlFwdToPath(self, path):
        return "<meta http-equiv=\"refresh\" content=\"0; URL='http://"+self.host +"/"+ path + "'\" />"

    def getHtmlDocToReply(self, docName):
        f = open(docName, "r")
        file = f.read()
        f.close()
        return file

    def generateQuestionHTML(self, heading, line1, line2):
       
        f = open("template.html", "r")
        file = f.read()
        f.close()
        file = file.replace("||HEADING||", heading)
        file = file.replace("||LINE1||", line1)
        file = file.replace("||LINE2||", line2)
        return file




PORT = 12345
server_address = ('',PORT)     
httpd = HTTPServer(server_address, websiteServer)
print('running server on port', PORT )        
try:         
    httpd.serve_forever()     
except:         
    httpd.shutdown()         
    print("Shutdown server")          
