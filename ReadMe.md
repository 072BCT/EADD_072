# Installation Notes:
1. Check out a project in Pycharm - [see here for help](Open%20lms%20folder%20using%20Pycharm)
URL of the remote repository: **https://github.com/072BCT/EADD_072.git**
4.  [Create Virtual Environment](https://www.jetbrains.com/help/pycharm-edu/creating-virtual-environment.html)
5. Restart Pycharm
6. On the Pycharm's terminal run the following code to Install Requirements : **pip install -r requirements.txt**

7.  Migrate Database: **python manage.py makemigrations WebApp** <br>
Please Ensure that you delete 'db.sqlite3' database and Migrations folder inside WebApp before clean Migration.
8. Migrate Database: **python manage.py migrate**
9. After that, run the app using Django manage.py: **python manage.py runserver**
10. Access the homepage on     http://localhost:8000
 
## Creating an admin user
First we’ll need to create a user who can login to the admin site. Run the following command:

`$ python manage.py createsuperuser` <br>
Enter your desired username and press enter. <br>

`Username: admin ` <br>
You will then be prompted for your desired email address: <br>

`Email address: admin@example.com` <br>
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first. <br>

```
Password: **********<br>
Password (again): *********<br>
Superuser created successfully.<br>
```


## Django Admin
The Django admin site is activated by default after running `$ python manage.py runserver`<br>
Now, open a Web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/. You should see the admin’s login screen.


## APIs
Visit http://127.0.0.1:8000/api/v1/ to explore the API. You only can explore APIs after you login to Django Admin screen using superuser access.


# Live Deployment:
Check  http://eadd-072.sushant.info.np for latest updated website. The website gets automically updated after around 5 minutes of commits pushed to Gitlab.
Username: 072bct500 Password: 072bct500

# Project Management Links
### Gitlab Board > [https://github.com/072BCT/EADD_072/projects/1](https://github.com/072BCT/EADD_072/projects/1)
### G Docs > [https://docs.google.com/document/d/1kRNxCuid3WVKMRKJzClc3a-CWSU6PLWqj7KpCW-C1gQ/edit](https://docs.google.com/document/d/1kRNxCuid3WVKMRKJzClc3a-CWSU6PLWqj7KpCW-C1gQ/edit)

