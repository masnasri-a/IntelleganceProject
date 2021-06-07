import pymongo
import json

myclient = pymongo.MongoClient("mongodb://root:root@localhost:27017/")
mydb = myclient["petanicode"]
mycol = mydb["user"]
class MongoConfig():
    def insertMongo(dictionary):
        print("test")
        mycol.insert_one(dictionary)

    def checkEmail(mail):
        result = 1
        try:
            query = {"email":mail}
            test = mycol.find_one(query)
            if test == None:
                result = 0
            else:
                result = 1
        except Exception as e:
            print(e)
        return result

    def checkNickname(nickname):
        result = 1
        try:
            query = {"nickname":nickname}
            test = mycol.find_one(query)
            if test == None:
                result = 0
            else:
                result = 1
        except Exception as e:
            print(e)
        return result

    def loginCheck(nickname,password):
        try:
            query = {'nickname':nickname,'password':password}
            test = mycol.find_one(query)
            if test == None:
                return "None"
            else:
                return test
        except Exception as e:
            print(e)