Shoemart: A Django E-commerce Website

Shoemart is a modern, feature-rich e-commerce web application built with Django. Inspired by sites like Skechers, this platform allows users to browse and purchase shoes, manage wishlists and carts, and track their orders. It supports both guest and authenticated users, offering a seamless and responsive online shopping experience.

![Shoemart Screenshot]()

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

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create a superuser
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
Visit http://localhost:8000/ to explore the site!



Built with ❤️ for final project


