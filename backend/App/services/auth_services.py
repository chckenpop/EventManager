def signup(username: str,password: str):
    #signup logic like insert the username and password into the db hash the password too ts simple af
    return {"message": "successfully signedup"}

def login(username: str,password:str):
    #login logic check if exists 
    return {"message": "sucessfully locked in"}