from fastapi import FastAPI, Response, status
import uvicorn, re, smtplib, ssl, secrets
from model.registermodel import RegisterModel
from config.mongoconfig import MongoConfig
from services.serviceauth import auth
app = FastAPI()

@app.post("/register")
def register(model : RegisterModel, response:Response):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    try:
        email = model.email
        if re.search(regex,email):
            checkEmail = MongoConfig.checkEmail(email)
            checkNickname = MongoConfig.checkNickname(model.nickname)
            token = secrets.token_hex(16)
            if(checkEmail == 0 or checkNickname == 0):
                data = {
                    "nickname":model.nickname,
                    "fullname":model.fullname,
                    "email":model.email,
                    "password":model.password,
                    "verified":"0",
                    "token":token
                }
                try:
                    # auth.sendMail(model.email,token)
                    MongoConfig.insertMongo(data)
                except Exception as w:
                    print(w)
            else:
                response.status_code = status.HTTP_404_NOT_FOUND
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
    except Exception as e:
        response.status_code = status.HTTP_404_NOT_FOUND
        return e
    return "register API"

@app.post("/login")
def login(username:str,password:str, response:Response):
    try:
        returns  = MongoConfig.loginCheck(username,password)
        print(returns)
    except Exception as e:
        response.status_code = status.HTTP_404_NOT_FOUND

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8008)