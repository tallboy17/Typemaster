import random
app.background = 'dodgerBlue'

numWords = int(app.getTextInput('Enter how many words you want to type (less than 50): '))

word_bank = ['set','order','give','eye','because','new','over','both','need','the',
'think','still','own','right','then','again','after','would','without','much','get',
'in','increase','person','man','first','follow','tell','use','long','against','little',
'present','point','hand','leave','play','must','open','line','help','then','way']
list_of_words = []
labels = []
Label('Typing Game',200,25,size=30,bold=True,font='grenze',fill='white')

def displayWords(word_bank, numOfWords):
    for i in range(numOfWords):
        list_of_words.append(random.choice(word_bank))
    x = 50
    y = 75
    for word in list_of_words:
        for letter in word:
            l = Label(letter,x,y,fill='black',size=12,bold=True)
            labels.append(l)
            x += 8
        labels.append(Label('space',0,0,visible=False))
        x += 10
        if x > 350:
            y += 45
            x = 50

displayWords(word_bank,numWords)
app.i = 0
app.correct = 0
def onKeyPress(key):
    if (app.i <= len(labels)-1):
        l = labels[app.i]
        str = l.value
        app.i += 1
        if (key == str):
            l.fill = 'green'
            app.correct+=1
        else:
            l.fill = 'red'
    else:
        Rect(0,0,400,400,fill='white')
        Label('Congrats!', 200, 200,fill='black',size=50)
        score = int(pythonRound(float(app.correct/len(labels)), 2)*100)
        Label('You got: ', 200,300, fill='black',size=25)
        Label(score,200,350,fill='black',size=25)
        Label('percent', 200,375,fill='black',size=25)