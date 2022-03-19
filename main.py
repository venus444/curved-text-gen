def htmlgen():
    num = 0
    for letter in text:
        num += 1
        print('<span class="char'+ str(num) +'">'+letter+'</span>')

def cssgen():
    angle = -100 # startpos of text
    num = 0
    for letter in text:
        num +=1
        angle += 6 # change in angle of text
        print('.char'+str(num)+'{ transform: rotate('+str(angle)+'deg); }')


text = "welcome to this website" # text to curve       
htmlgen()
cssgen()
