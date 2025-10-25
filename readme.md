# 📝 Blogging API (ALX Project)

A simple RESTful Blogging API built with **Django** and **Django REST Framework (DRF)**.  
This project allows users to register, log in, and manage blog posts, categories, and comments.

---

## 🚀 Features

- 🔐 User registration and login (Token Authentication)
- 📰 CRUD operations for blog posts
- 🗂️ Category management
- 💬 Commenting system
- 🌐 RESTful API structure
- 📜 OpenAPI schema endpoint for documentation

---

## 🏗️ Tech Stack

- **Backend:** Django 5+, Django REST Framework  
- **Database:** SQLite (default)  
- **Authentication:** Token-based (DRF Auth Token)  
- **Documentation:** DRF Schema + OpenAPI  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/blogging-api-ALX.git
cd blogging-api-ALX

2️⃣ Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate   # for Windows
# source venv/bin/activate   # for macOS/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

If requirements.txt doesn’t exist, install manually:
pip install django djangorestframework django-filter djangorestframework-simplejwt

4️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create a superuser (optional)
python manage.py createsuperuser

6️⃣ Run the development server
python manage.py runserver

🧭 API Endpoints
Method	Endpoint	Description	Auth Required
POST	/api/users/register/	Register new user	❌ No
POST	/api/users/login/	Login and get token	❌ No
GET	/api/categories/	List all categories	❌ No
POST	/api/categories/	Create new category	✅ Yes
GET	/api/posts/	List all posts	❌ No
POST	/api/posts/	Create new post	✅ Yes
GET	/api/posts/{id}/	Retrieve a post	❌ No
PUT	/api/posts/{id}/	Update a post	✅ Yes
DELETE	/api/posts/{id}/	Delete a post	✅ Yes
GET	/api/comments/	List all comments	❌ No
POST	/api/comments/	Create new comment	✅ Yes
GET	/openapi/	View API schema	❌ No

🧠 Project Structure
blogging-api-ALX/
│
├── blog/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
└── README.md

👨‍💻 Author

Alaa Mohamed Okasha Mohamed