🏠 Affordable Housing Waitlist Tracker
A Django-powered web application designed to simplify the management of affordable housing properties, owners, and applicant waitlists. Built for housing authorities, property managers, and applicants seeking budget-friendly rentals.

✨ Key Features
🛠️ Admin Dashboard: Full CRUD for Houses, Owners, and Applicants via Django Admin.

👥 User Portal: Secure signup/login and housing application submission.

🔍 Smart Search: Filter listings by location, rent, and availability.

📱 Responsive Design: Clean, mobile-friendly UI using Bootstrap.

📸 Screenshots
(Add screenshots here to showcase the dashboard, application form, and search results.)

🧰 Tech Stack
Technology	Role
Django	Backend framework
SQLite	Default database
Bootstrap	Frontend styling
Python	Core language
HTML/CSS	UI templates
🚀 Getting Started
bash
# Clone the repository
git clone https://github.com/sudharshan59/affordable-housing-tracker.git
cd affordable-housing-tracker

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows
# Or use: source venv/bin/activate  # For macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Apply migrations and start server
python manage.py migrate
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to explore the app.

🧪 How to Use
Admins can log in via /admin to manage listings and users.

Applicants can register, browse listings, and apply for housing.

Use filters to find suitable housing options quickly.

📌 Roadmap
✅ Basic CRUD and user authentication

🔄 Waitlist prioritization logic

📧 Email notifications for application updates

📊 Analytics dashboard for property managers

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📄 License
This project is licensed under the MIT License.
# By Sudharshan
