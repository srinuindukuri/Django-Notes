
# Step - 1: pip3 install Django

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Step - 2: django-admin startproject PROJECT_NAME(Create a project using the command)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Step - 3: python manage.py startapp APP_NAME(Create an App using the command)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Step - 4: Add the app name inside the settings page, which is ''INSTALLED_APPS''
#               "INSTALLED_APPS" = ['APP_NAME '] - hello

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Step - 5: Create a Super User
#                - python manage.py createsuper < User_Name >
#               - Email address:                                 Enter the email Address
#               - Password:                                        Enter Password(U won't able to see password while Entering)
#               - Password(again):                            (Again enter the password)
#               - Superuser created successfully
#
#                 - To change user password CLI command changepassword for django
#                - python manage.py changepassword
#                                      OR
#                - django-admin changepassword

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                     VIEWS
# Step - 6 : To Represent any information on the web, we need to use the "views.py" to tell that to utilize this request.
#                - For this we will def an 'index' and give the argument 'request' and return HttpResponse("Hello, World!").
#                - This index the HttpResponse of the "Hello World".
#                - To use this 'HttpResponse', and we will also import 'render' we need to import it. Luckily django has many things where we can do things.
#                - from django.http  import HttpResponse
#                - Now we need to tell the app when should u actually response, where URL going to visit.

#                 from django.http import HttpResponse

#                 def index(request):

#                     return render (request, "hello/index.html")
#                 def greet (request, name):
#                    return render(request, "hello/greet.html", {
#                          "name": name.capitailize                        --> Here Capitalize is used for to have the first word as capital in the word.
#                     })

#               - We cannot write all the info we need to show on the webpage, so instead of this method we can use "templates".

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                                           TEMPLATES
# Step - 7 :Create a folder named Templates inside the templates folder create an another folder hello, now create the html file such as index.html, greet.html and many more as u wish. This hello.html file is used to write all the html code.


#                                                                HTML PAGE - greet.html
#                <!DOCTYPE html>
#                <html lang="en">
#                      <head>
#                                <title>Hello</title>
#                      </head>
#                      <body>
#                                <h1> Hello, {{ name }} </h1>     --> {{ name }} We will plugin the value.
#                      </body>
#                </html>

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                                                 URLS
# Step - 8 : In Django, we have a urls.py for all the project to manage. But, it's better to make a separate urls.py on the app directory              itself  which we make it easier if we create multiple apps.
#                 - Create a new file inside the hello app as urls.py
#                 - we need to import the path and the views from the current directory.

#                 - add urlpatterns with including path.
# urls.py folder in the app directory
#                   from django.urls import path
#                   from . import views
#                   urlpatterns = [
#                             path("", views.index, name="index")   --> This name will be useful for the future work to distinguish the file names.
#                             path("<str:name>", views.greet, name="greet")
#                   ]

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Step - 9 : Now, go to the main urls.py in the project directory to include this app urls.py
#                - Add the include keyword in the import urls line.
#                - Include the hello.urls in the path.
# urls.py folder in the django main directory
#                   from django.contrib import admin
#                   from django.urls import include, path
#                   urlpatterns = [
#                             path("admin/", admin.site.urls)         --> This takes us to the admin page which is by default.
#                     ]
#                             path("hello/", include("hello.urls"))  --> This takes us to the hello page which we created.
