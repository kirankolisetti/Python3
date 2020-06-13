def PLatin(word):
    if(word[0] in ['a','e','i','o','u']):
        print(word+'way')
    else:
        print(word[1:]+word[0]+'ay')

PLatin('apple')
PLatin('pig')
