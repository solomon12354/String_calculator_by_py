
def evalute(string):
    big = 0
    mid = 0
    sml = 0
    dep = 0
    maxdep = 0
    
    isDigit = False
    
    isMul = False
    isDiv = False
    
    sign = []
    digit = []
    
    for element in range(0, len(string)):
        if(string[element] == '{'):
            big += 1
            sign.append('{')
            dep += 1
            isDigit = False
        elif(string[element] == '['):
            mid += 1
            sign.append('[')
            dep += 1
            isDigit = False
        elif(string[element] == '('):
            sml += 1
            sign.append('(')
            dep += 1
            isDigit = False
        elif(string[element].isnumeric()):
            if(isDigit):
                digit[len(digit) - 1] = digit[len(digit) - 1] * 10 + int(string[element])
                isDigit = True
            else:
                digit.append(int(string[element]))
                isDigit = True
        elif(string[element] == '+' or string[element] == '-'):
            if(sign and (sign[len(sign) - 1] == '*' or sign[len(sign) - 1] == '/')):
                if(sign[len(sign) - 1] == '*'):
                    Muled = digit.pop()
                    digit[len(digit) - 1] = digit[len(digit) - 1] * Muled
                else:
                    Dived = digit.pop()
                    digit[len(digit) - 1] = digit[len(digit) - 1] / Dived
                sign.pop()
                
            sign.append(string[element])
            isDigit = False
        elif((string[element] == '*' or string[element] == '/')):
            sign.append(string[element])
            isDigit = False
        elif(string[element] == '}'):
            if(big == 0):
                raise Exception
            while(sign and sign[len(sign) - 1] != '{'):
                if(sign and (sign[len(sign) - 1] == '*' or sign[len(sign) - 1] == '/')):
                    if(sign[len(sign) - 1] == '*'):
                        Muled = digit.pop()
                        digit[len(digit) - 1] = digit[len(digit) - 1] * Muled
                        
                    else:
                        Dived = digit.pop()
                        digit[len(digit) - 1] = digit[len(digit) - 1] / Dived
                elif(sign and (sign[len(sign) - 1] == '+' or sign[len(sign) - 1] == '-')):
                    if(sign[len(sign) - 1] == '+'):
                        added = digit.pop()
                        digit[len(digit) - 1] = digit[len(digit) - 1] + added
                    else:
                        subed = digit.pop()
                        digit[len(digit) - 1] = digit[len(digit) - 1] - subed
                sign.pop()
            big -= 1
            isDigit = False 
            sign.pop()
            if(sign and (sign[len(sign) - 1] == '*' or sign[len(sign) - 1] == '/')):
                if(sign[len(sign) - 1] == '*'):
                    Muled = digit.pop()
                    digit[len(digit) - 1] = digit[len(digit) - 1] * Muled
                        
                else:
                    Dived = digit.pop()
                    digit[len(digit) - 1] = digit[len(digit) - 1] / Dived
                sign.pop()
            dep -= 1
        elif(string[element] == ']'):
            if(mid == 0):
                raise Exception
            while(sign[len(sign) - 1] != '['):
                if(sign and (sign[len(sign) - 1] == '*' or sign[len(sign) - 1] == '/')):
                    if(sign[len(sign) - 1] == '*'):
                        Muled = digit.pop()
                        digit[len(digit) - 1] = digit[len(digit) - 1] * Muled
                        
                    else:
                        Dived = digit.pop()
                        digit[len(digit) - 1] = digit[len(digit) - 1] / Dived
                elif(sign and (sign[len(sign) - 1] == '+' or sign[len(sign) - 1] == '-')):
                    if(sign[len(sign) - 1] == '+'):
                        added = digit.pop()
                        digit[len(digit) - 1] = digit[len(digit) - 1] + added
                    else:
                        subed = digit.pop()
                        digit[len(digit) - 1] = digit[len(digit) - 1] - subed
                sign.pop()
            mid -= 1
            isDigit = False
            sign.pop()
            if(sign and (sign[len(sign) - 1] == '*' or sign[len(sign) - 1] == '/')):
                if(sign[len(sign) - 1] == '*'):
                    Muled = digit.pop()
                    digit[len(digit) - 1] = digit[len(digit) - 1] * Muled
                        
                else:
                    Dived = digit.pop()
                    digit[len(digit) - 1] = digit[len(digit) - 1] / Dived
                sign.pop() 
            dep -= 1
        elif(string[element] == ')'):
            if(sml == 0):
                raise Exception
            while(sign[len(sign) - 1] != '('):
                if(sign and (sign[len(sign) - 1] == '*' or sign[len(sign) - 1] == '/')):
                    if(sign[len(sign) - 1] == '*'):
                        Muled = digit.pop()
                        digit[len(digit) - 1] = digit[len(digit) - 1] * Muled
                        
                    else:
                        Dived = digit.pop()
                        digit[len(digit) - 1] = digit[len(digit) - 1] / Dived
                elif(sign and (sign[len(sign) - 1] == '+' or sign[len(sign) - 1] == '-')):
                    if(sign[len(sign) - 1] == '+'):
                        added = digit.pop()
                        digit[len(digit) - 1] = digit[len(digit) - 1] + added
                    else:
                        subed = digit.pop()
                        digit[len(digit) - 1] = digit[len(digit) - 1] - subed
                sign.pop()
            sml -= 1
            isDigit = False
            sign.pop()
            if(sign and (sign[len(sign) - 1] == '*' or sign[len(sign) - 1] == '/')):
                if(sign[len(sign) - 1] == '*'):
                    Muled = digit.pop()
                    digit[len(digit) - 1] = digit[len(digit) - 1] * Muled
                        
                else:
                    Dived = digit.pop()
                    digit[len(digit) - 1] = digit[len(digit) - 1] / Dived
                sign.pop()
            dep -= 1
        if(big < 0 or mid < 0 or sml < 0):
            raise Exception
        if(dep > maxdep):
            maxdep = dep
        #print(sign)
        #print(digit)
    for i in range(0, len(sign)):
        if(sign and (sign[i] == '*' or sign[i] == '/')):
            if(sign[i] == '*'):
                
                digit[i] = digit[i] * digit[i+1]
                        
            else:
                
                digit[i] = digit[i] / digit[i+1]
            digit = digit[0:i] + digit[i+2:len(digit)]
    #print(digit)
    #print(sign)
    while(sign):
        s = sign[0]
        
        if(s == '+'):
            added = digit[0]
            digit[1] = added + digit[1]
        elif(s == '-'):
            subed = digit[0]
            digit[1] = subed - digit[1]
        sign = sign[1:len(sign)]
        digit = digit[1:len(digit)]
    ans = []
    ans.append(int(digit[0]))
    ans.append(maxdep)
    return ans 

print(evalute("[3+1*5+7]+5*3-{4+2}")) #Write the string you want to calculate
