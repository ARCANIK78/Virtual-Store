# 🛒 Virtual-Store  
**Django Project with PostgreSQL**  

Welcome to **Virtual-Store**, a web application built with Django and PostgreSQL.  

## 📌 Features  
- ✅ Django-based web application  
- ✅ PostgreSQL database integration  
- ✅ Virtual environment for dependency management  

## 🚀 Installation  

### 1️⃣ Clone the repository  
```sh
git clone https://github.com/your-username/Virtual-Store.git  
cd Virtual-Store  

2️⃣ Create and activate a virtual environment

python -m venv env  
source env/bin/activate  # On Windows use: env\Scripts\activate  

3️⃣ Install dependencies

pip install -r requirements.txt  

4️⃣ Configure PostgreSQL

Make sure PostgreSQL is installed and running. Then, create a database:

CREATE DATABASE virtual_store;  

Edit the settings.py file and configure the database:

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': 'virtual_store',  
        'USER': 'your_username',  
        'PASSWORD': 'your_password',  
        'HOST': 'localhost',  
        'PORT': '5432',  
    }  
}  

5️⃣ Apply migrations

python manage.py makemigrations  
python manage.py migrate  

6️⃣ Create a superuser (optional)

python manage.py createsuperuser  

7️⃣ Run the server

python manage.py runserver  

🔗 Access the application at: http://127.0.0.1:8000/
🛠 Tech Stack

🚀 Framework: Django
🗄 Database: PostgreSQL
💻 Environment: Virtualenv
📜 License

This project is licensed under the MIT License.

🙌 Feel free to contribute and improve this project!
