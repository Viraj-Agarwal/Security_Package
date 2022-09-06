def caesaren(str,k):
    key = int(k)
    temp=list(str)
    #print(key)
    for i in range(0,len(temp)):
        

        temp[i] = chr((ord(temp[i])+key-32)%95 +32)
    
    
    return "".join(temp) 
    
def caesarde(str,k):
    key=int(k)
    temp=list(str)
    
    for i in range(0,len(temp)):

        temp[i] = chr((ord(temp[i])-key-32)%95 +32)
    
    
    return "".join(temp) 

def monoalphen(str):
    temp=""
    key="qwertyuiopasdfghjklzxcvbnm"
 
    for i in range(0,len(str)):
        char=str[i]
      
        try:
            temp+= key[ord(char)-97]
        except:
            print(char)
    return temp

# def readkey():
#     file=open("key.txt","r")
#     return file.read()

def monoalphde(str):
    temp=""
    key="qwertyuiopasdfghjklzxcvbnm"
   
    for i in range(0,len(str)):
        char=str[i]
        # if(char.isupper()):
        try:
            temp+=chr(key.find(char) + 97)
        except:
            print(char)
    return temp

def transposen(str,key):
    arr=[]
    j=0
    temp=[]
    for i in range(0,len(str)):
        if(j<int(key[0])):
            temp.append(str[i])
            j+=1
        else:
            arr.append(temp)
            temp=[]
            temp.append(str[i])
            j=1
        if(i==len(str)-1):
            for i in range(0,int(key[0])-j):
                temp.append(' ')
            arr.append(temp)
    str=""        
    for i in range(0,int(key[0])):
        j=0
        try:
            while(arr[j][i]):
                str+=arr[j][i]
                j+=1
        except:
            continue
    i ="% s"%len(arr)
    key.append(i)   
    print(arr)    
    return str,key
    
def transposde(str,key):
    c="% s"%key[0]
    r="% s"%key[1]
    arr=[]
    j=0
    temp=[]
    for i in range(0,len(str)):
        if(j<int(key[1])):
            temp.append(str[i])
            j+=1
        else:
            arr.append(temp)
            temp=[]
            temp.append(str[i])
            j=1
        if(i==len(str)-1):
                arr.append(temp)
    print(arr)
    str=""        
    for i in range(0,int(key[1])):
        j=0
        try:
            while(arr[j][i]):
                str+=arr[j][i]
                j+=1
        except:
            continue
            
    return str


       
    