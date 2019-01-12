# python -m pip install --upgrade pip
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.db import connection
from food.models import User
from food.models import Review



import datetime

root_user = {'username':"John Doe",'isloggedin':"false",'password':''}
curr_res = ""

# Create your views here.

def logout(request):
    users = User.objects
    for i in users:
        if(i.username==root_user["username"] and i.password==root_user["password"]):
            i.isloggedin = "false"
            i.save()
            root_user["username"] = "John Doe"
            root_user["isloggedin"] = "false"
            return render(request, 'food/login.html',{'message':'Successfully logged out!'}) 
        
    


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        users = User.objects
        for i in users:
            if(i.username==username and i.password==password):
                i.isloggedin = "true"
                i.save()
                root_user["username"] = i.username
                root_user["isloggedin"] = "true"
                root_user["password"] = i.password

                return render(request, 'food/index.html',{'username':username}) 
        
        return render(request, 'food/login.html',{'message':'Credentials Invalid!'})

        # if user is not None:
        #     print("User is valid, active and authenticated")
        #     return render(request, 'food/search.html')
        # else:
        #     print("The username and password were incorrect.")
        #     return render(request, 'food/login.html')
    else:
        return render(request, 'food/login.html',{'message':''})


def signup(request):
    print("signup function")
    if request.method == 'POST':
        print("inside post")
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        emailid = request.POST['emailid']
        username = request.POST['username']
        password = request.POST['password']
        print("hello")
        print(firstname)
        print(lastname)

        
        user = User()
        user.firstname = firstname
        user.lastname = lastname
        user.emailid = emailid
        user.username = username
        user.password = password
        user.save()
        return render(request, 'food/login.html',{'message':'Succesfully Registered!'})
    else:
        return render(request, 'food/signup.html')

def search(request):
    print(root_user)
    if(root_user["isloggedin"]=="true"):
        if request.method == 'POST':
            print('index post')
            cui_name = request.POST.get('cui_name')
            cui_id = request.POST.get('cui_id')
            cat_name = request.POST.get('cat_name')
            cat_id = request.POST.get('cat_id')
            res_type = request.POST.get('res_type')
            res_id = request.POST.get('res_id')



            print(cui_name)
            print(cui_id)
            print(cat_name)
            print(cat_id)
            print(res_type)
            print(res_id)

            return render(request, 'food/res.html',{'username':root_user["username"],'cuisine_name':cui_name,'cuisine_id':cui_id,'res_type':res_type,'res_id':res_id,'cat_id':cat_id,'cat_name':cat_name} )
        else:
            print("xxx")
            return render(request, 'food/index.html')
    else:
        return render(request, 'food/login.html',{'message':'Log In First!'})

def res(request):
    return render(request, 'food/res.html')
def rev2(request):
    return render(request, 'food/rev2.html')

def restuarant(request):
    print(request.POST.get('review_text'))
    if request.POST.get('review_text') == None:
        res_det = request.POST.get('res_det')
        curr_res = res_det
        reviews = Review.objects

        return render(request, 'food/restuarant.html',{'username':root_user["username"],'res_det':res_det,'reviews':reviews})
    else:
        review_text = request.POST.get('review_text')
        rating_text = request.POST.get('rating_text')
        rating = request.POST.get('rating')
        res_id = request.POST.get('res_id')
        username = root_user["username"]
        root_user["username"] = username
        print(rating)
        print("rating")

        if float(rating) <= 1:
            rating_color = "CB202D"
        elif float(rating) <= 2:
            rating_color = "FF7800"

        elif float(rating) <= 3:
            rating_color = "CDD614"
        
        elif float(rating) <=4:
            rating_color = "5BA829"
        elif float(rating) <=5:
            rating_color = "305D02"

        reviews = Review()
        reviews.review_text = review_text
        reviews.rating_text = rating_text
        reviews.rating = rating
        reviews.res_id = res_id
        reviews.username = username
        reviews.rating_color = rating_color

        reviews.save()
        reviews = Review.objects
        

        return render(request, 'food/restuarant.html',{'username':root_user["username"],'res_det':res_id,'reviews':reviews})







# def demo(request):
#     print("demo")
#     if request.method == 'POST':
#        firstname = request.POST['firstname']
#        lastname = request.POST['lastname']
#        emailid = request.POST['emailid']
#        username = request.POST['username']
#        password = request.POST['password']
       
#        user = User()
#        user.firstname = firstname
#        user.lastname = lastname
#        user.emailid = emailid
#        user.username = username
#        user.password = password
#        user.save()

#        users = User.objects



#        return render(request, 'food/demo3.html', {'Users': users})

        
        
# def demo2(request):
#     return render(request, 'food/demo2.html')
# def demo3(request):
#     return render(request, 'food/demo3.html')
