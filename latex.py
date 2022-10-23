import json

class Latex():

    def __init__(self):
        pass

    # read text file and write over with new result
    def readFromFile(self, filename, jsonname):
        with open(filename, "r") as r:
            text = r.read()
        f = open('replace.json')
        data = json.load(f)

        for value in data[jsonname]:
            find = value['find']
            replace = value['replace']
        end_result = text.replace(find, replace)

        with open("output.txt", "w") as w:
            w.write("".join(end_result))
            return end_result

    # After . make new line
    def changePunk(self, filename):
        self.readFromFile(filename, "replace_punkt")

    # After , make new line
    def changeComma(self):
        self.readFromFile("output.txt", "replace_comma")

    # After % make new line
    def changeProc(self):
        self.readFromFile("output.txt", "replace_proc")

    # Look for the world, return True or False
    def findWord(self, word, string):
        wordIn = False
        if word in string:
            wordIn = True
        return wordIn

    # Adding tap
    def addTaps(self, line):
        return "\t" + line

    # Check for begin{ and end{ with findWord. If its true add tab.
    def tabBeginEnd(self, filename):

        with open(filename, "r") as r:
            text = r.read()

        result = ""
        isBool = False

        for line in text.split("\n"):
            if self.findWord("begin{", line) and not(self.findWord("document", line)) and not(self.findWord("%\begin", line)):
                result += line + "\n"
                isBool = True
                continue
            elif isBool:
                if self.findWord("end{", line) and not(self.findWord("document", line)) and not(self.findWord("%\end", line)):
                    result += line + "\n"
                    isBool = False
                    continue
                else:
                    result += self.addTaps(line) + "\n"
            else:
                result += line + "\n"

        with open("output.txt", "w") as w:
            w.write("".join(result))

    
    def all_file(self):
        inpFileName = input("Write filename: ")
        try:
            self.changePunk(inpFileName)
            print("\nFILE HAS BEEN VALIDATED!!")
        except:
             print("NO FILE WITH THAT NAME!!.")
        self.changeComma()
        self.changeProc()
        self.tabBeginEnd("output.txt")


def main():
    la = Latex()
    la.all_file()
