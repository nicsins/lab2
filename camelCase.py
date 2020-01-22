def getInput():

    words=input('Please Enter a SenTence').lower()
    return words.split()

def printOutput(words):
    [ print(word.title(),end='')if word != words[0] else print(word.lower(),end='') for word in words]

def display_banner():
	""" Display program name in banner """
	msg = 'AWSOME camelCaseGenerator PROGRAM'
	stars = '*' * len(msg)
	print(f'\n {stars} \n {msg} \n {stars}\n') 


# stuff
if __name__ == '__main__':
    display_banner()
    words=getInput()
    printOutput(words)