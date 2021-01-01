import json
import  random
flag=1
cache={}
class userFunctions:
    def create(self,key,data,path="default.txt"):
        dic={}
        fa = open(path, 'a')
        fr = open(path, 'r')
        fa.close()
        content =fr.read()
        if content=="":
            dic[key]=data
            fw=open(path,'w')
            fw.write(json.dumps(dic))
            fw.close()
        else:
            oldData=json.loads(content)
            oldData[key]=data
            fw=open(path,'w')
            fw.write(json.dumps(oldData))
            fw.close()
        print("Created successfully!")
        fr.close()
        self.cache(key,path)
    def cache(self,key,path):#stores the path of particular key
        fr=open('cache.txt','r')
        content=fr.read()
        if content == "":
            temp={}
            temp[key]=path
            fw = open('cache.txt', 'w')
            fw.write(json.dumps(temp))
            fw.close()
        else:
            dic = json.loads(content)
            dic[key]=path
            fw = open('cache.txt', 'w')
            fw.write(json.dumps(dic))
            fw.close()
        fr.close()
    def Ispresent(self,key):
        fr=open('cache.txt','r')
        content=fr.read()
        if content=="":
            return 0
        pathData=json.loads(content)
        fr.close()
        if key in pathData:
            return 1
        else:
            return 0
        fr.close()
    def read(self,key):#user read request
        if self.Ispresent(key):#checks is key is present or not
            path=self.getPath(key)
            #print(path)
            print("JSON Data for Requested key is:",self.getJson(path,key))
        else:
            print("Invalid Key! No such key exists")
    def getJson(self,path,key):#getting JSON Data for user read request
        fr=open(path,'r')
        content=fr.read()
        data=json.loads(content)
        fr.close()
        return data[key]
    def getPath(self,key):#Getting path of key
        fr = open('cache.txt', 'r')
        content = fr.read()
        pathdata=json.loads(content)
        fr.close()
        return pathdata[key]
    def createJson(self):#Generating random json
        s = dict()
        d = ["red", "black", "blue", "yellow", "voilet", "orange", "indigo", "green", "white", "purple", "brown",
                 "pink"]
        for i in range(10):
            s[i] = random.choice(d)
        return json.dumps(s)
    def delete(self,key):#User delete request
        if self.Ispresent(key):
            path=self.getPath(key)
            fr = open(path, 'r')
            content = fr.read()
            data = json.loads(content)
            del data[key]
            fw=open(path,'w')
            fw.write(json.dumps(data))
            fr=open('cache.txt','r')
            cacheData=json.loads(fr.read())
            del cacheData[key]
            fw=open('cache.txt','w')
            fw.write(json.dumps(cacheData))
            fr.close()
            fw.close()
            print("Deleted Successfully!")
        else:
            print("Invalid key! No such key exists")
obj=userFunctions() #creating object of class
while flag:
    print("PRESS '1' TO CREATE")
    print("PRESS '2' TO READ")
    print("PRESS '3' to DELETE")
    userChoice=int(input("ENTER YOUR CHOICE:"))
    if userChoice==1:
        key=input("Enter Key name:")
        if obj.Ispresent(key)==0:#checks if key is already present or not
            data=obj.createJson()
            path=input("Enter the path of file (optional):")
            data=json.loads(data)
            if path=='':
                obj.create(key,data)
            else:
                obj.create(key,data,path)
        else:
            print("Opps! This key already exits.")
    elif userChoice==2:
        key=input("Enter key name:")
        obj.read(key)
    elif userChoice==3:
        key=input("Enter key name:")
        obj.delete(key)
    else:
        print("Invalid request! Please try again")
    print('----------------------------------------------------------------------------------------------------')


