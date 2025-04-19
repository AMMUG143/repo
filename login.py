def login_page(username,password,retypepassword):
    if password == retypepassword:
        return"Login successful of the user "+username
    else:
        return "retype password"
    


if __name__ == "__main__":
    var=login_page("ammu","56789","12345")
    print(var)