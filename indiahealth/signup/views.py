from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
from django.contrib import auth
config = {
    'apiKey' : "AIzaSyAxl6eKJhU3lZKIUECJQdaoYoUQ6y9e2sc",
    'authDomain' : "indiahealth-2e534.firebaseapp.com",
    'databaseURL' : "https://indiahealth-2e534.firebaseio.com",
    'projectId' : "indiahealth-2e534",
    'storageBucket' : "indiahealth-2e534.appspot.com",
    'messagingSenderId' : "136387651389"
}

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()

# def signin(request):
#     return render(request,'signuplogin/signuplogin.html',context=msg )
def signin(request):
    return render(request,'signuplogin/signuplogin.html')

def postsignin(request):
    email = request.POST.get("email")
    pwd = request.POST.get("pwd")

    dict = { "e": email,"p":pwd}

    try:
        user = authe.sign_in_with_email_and_password(email, pwd)

    except:
        msg = {'msg' : "Invalid Credentials"}
        return render(request, 'signuplogin/signuplogin.html', context=msg)
    # print(user)
    session_id = user['idToken']
    request.session['uid'] = str(session_id)

    return render(request, 'home/home.html',context = dict)




def signUp(request):
    return render(request, "signuplogin/signuplogin.html")


def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pwd')
    try:
        user = authe.create_user_with_email_and_password(email, passw)
        uid = user['localId']
        data = {"name": name, "status": "1"}
        database.child("users").child(uid).child("details").set(data)
        message = "Account Created succesfully"
    except:
        message = "Unable to create account try again"
        return render(request, "signuplogin/signuplogin.html", {"msg": message})

    return render(request, "signuplogin/signuplogin.html", {"msg": message})


def logout(request,):
    auth.logout(request)
    return render(request,'signuplogin/signin.html')

