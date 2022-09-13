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

def railfenceen(arr,key):
    # railMatrix=[["//"]*len(arr)]*key
    railMatrix=[["\n" for i in range(len(arr))]for j in range(key)]
    # for i in range(len(railMatrix)):
    #     for j in range(len(railMatrix[i])):
    #         print(railMatrix[i][j])
    row,col,k=0,0,-1
    enresult=""
    for i in range(len(arr)):
        railMatrix[row][col]=arr[i]
        col+=1
        if row==0 or row==key-1:
            k=k*(-1)
        row=row+k
    # print(railMatrix)    
    for i in range(key):
        for j in range(len(arr)):
            if railMatrix[i][j]!="\n":
                # print(railMatrix[i][j])
                enresult+=railMatrix[i][j]
    return enresult                

def RailFencede(enarr,key):
        railMatrix=[["//" for i in range(len(enarr))]for j in range(key)]
        row,col,k,m=0,0,-1,0
        result=""
        for i in range(len(enarr)):
            railMatrix[row][col]="*"
            col+=1
            if row==0 or row==key-1:
                k=k*(-1)
            row=row+k
        for i in range(key):
            for j in range(len(enarr)):
                if railMatrix[i][j]=="*":
                    railMatrix[i][j]=enarr[m]
                    m+=1
        row,col=0,0
        k=-1
        for i in range(len(enarr)):
            result+=railMatrix[row][col]
            col+=1
            if row==0 or row==key-1:
                k=k*(-1)
            row=row+k       
        return result

       
    
