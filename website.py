from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib, os


class websiteServer(BaseHTTPRequestHandler):
    
    pathsToURL = { "home": "home.html",
    "home?answer" : ["1990", "stage2", "home?answer", "home", "Whoops! Incorrect, please try again", "In which year did our president join the university" ], 
    
    "stage2" : ["1985", "pathIfCorrect", "stage2?answer", "stage2",  "That was easy, heres a harder one", "What year was ADHC founded?"],
    "stage2?answer" : ["1985", "stage3", "stage2?answer","stage2", "Not quite.... try again", "What year was ADHC founded?"],
    
    "stage3" : ["my.njit.edu", "stage4", "stage3?answer", "stage3",  "Ready for a deep dive?", "What is the URL you would to go to see financial aid and register for classes"],
    "stage3?answer" : ["my.njit.edu", "stage4", "stage3?answer","stage3", "WRONG try again", "What is the URL you would to go to see financial aid and register for classes"],
    
    "stage4" : ["tutoring", "winner", "stage4?answer", "stage4",  "Very nice very nice, im impressed", "There is a math professor whose last name rhymes with \"Borus\", what is he the director of?"],
    "stage4?answer" : ["tutoring", "winner", "stage4?answer","stage4", "WRONG try again", "There is a math professor whose last name rhymes with \"Borus\", what is he the director of?"]}

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
                ans = path[i1+1:]
                print(pathNoAns, ans)
                for page in self.pathsToURL:
                    if page == pathNoAns:
                        pageFound = True
                        print(page, ans == self.pathsToURL[page][0])

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
