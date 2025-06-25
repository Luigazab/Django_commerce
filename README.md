Shoemart: A Django E-commerce Website

Shoemart is a modern, feature-rich e-commerce web application built with Django. Inspired by sites like Skechers, this platform allows users to browse and purchase shoes, manage wishlists and carts, and track their orders. It supports both guest and authenticated users, offering a seamless and responsive online shopping experience.

![Shoemart Screenshot](https://github.com/user-attachments/assets/9678ce7a-7e09-4b0a-b3a2-d6973ce4df06)


---

Features

User Accounts
- Registration & login system
- User profiles with editable personal and shipping info
- Order history and order detail pages

Shopping Experience
- Product browsing by category
- Product variants (e.g. color, size)
- Image gallery per product
- Add to cart (guest & signed-in users)

Checkout & Payments
- Shipping information form
- Order summary with total computation
- PayPal integration (with cancel & success redirection)
- Toast notifications for feedback

 Admin Panel
- Django admin for managing users, products, variants, orders, and shipping records
- Fully customized admin interface

---

Tech Stack

- **Backend:** Django, MySQL
- **Frontend:** HTML, Bootstrap 5, JavaScript, CSS
- **Payments:** PayPal JS SDK
- **Deployment:** PythonAnywhere ->https://mercemart.pythonanywhere.com

---

Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/Luigazab/Django_commerce.git
cd Django_commerce

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a MySQL database named shoemart
CREATE DATABASE shoemart;

# 5. Edit User, Password, host, and port on Django_commerce/settings.py according to your own.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shoemart',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# 6. Run migrations
python manage.py makemigrations
python manage.py migrate

# 7. Create an admin user to access the admin page.
python manage.py createsuperuser

# 8. Start the development Server
python manage.py runserver


Built with ❤️ for final project


