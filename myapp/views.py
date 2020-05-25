from django.shortcuts import render
import pyrebase

config = {
    'apiKey': "AIzaSyABeKgX058uUu3TMMRq-c24nUvsqs_Uw64",
    'authDomain': "hrms-f37e9.firebaseapp.com",
    'databaseURL': "https://hrms-f37e9.firebaseio.com",
    'projectId': "hrms-f37e9",
    'storageBucket': "hrms-f37e9.appspot.com",
    'messagingSenderId': "1061307293870",
    'appId': "1:1061307293870:web:ff015eb7ca4694cbc84d3f",
    'measurementId': "G-Q8CP1PFLR9"
}
firebase = pyrebase.initialize_app(config)
# firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def login(request):
    return render(request, 'login.html')


def postsign(request):
    email = request.POST.get('email')
    pss = request.POST.get('pass')
    user = auth.sign_in_with_email_and_password(email, pss)

    return render(request, 'hi.html', {'e': email})


def register(request):
    return render(request, 'signup.html')


def send_code_verify(request):
    # phone = request.POST.get('phone')
    # pyrebase.auth().sign_in_with_num
    return render(request, 'send_code_verify.html')


def verify_sms(request):
    return render(request, 'send_code_verify.html')