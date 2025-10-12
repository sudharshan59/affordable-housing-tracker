🏠 Affordable Housing Waitlist Tracker
A modern Django web app that empowers housing authorities and property managers to manage affordable housing listings, owners, and applicant waitlists — while giving renters a simple, transparent way to apply for homes.

🌟 Why This Project Matters
Affordable housing is a critical need in many communities. Long waitlists, outdated systems, and lack of transparency make it harder for people to find safe, affordable places to live. This app solves that by:

📋 Digitizing housing applications

🧮 Prioritizing waitlists fairly

🔍 Helping renters find homes that match their needs

🛠️ Giving property managers full control over listings and applicants

🚀 Live Demo
Coming soon — deployable on platforms like Heroku, Render, or Railway.

🧰 Tech Stack
Layer	Technology
Backend	Django (Python)
Frontend	HTML, CSS, Bootstrap
Database	SQLite (default) or PostgreSQL
Auth	Django's built-in system
UI Framework	Bootstrap 5
🔧 Installation & Setup
Prerequisites
Python 3.8+

pip

Git

Steps
bash
# Clone the repo
git clone https://github.com/sudharshan59/affordable-housing-tracker.git
cd affordable-housing-tracker

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# Or: source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
Visit http://127.0.0.1:8000/ to explore the app.

🧪 How It Works
👤 For Applicants
Sign up and log in

Browse available housing

Filter by location, rent, and availability

Submit applications and track status

🏘️ For Admins
Access /admin dashboard

Add/edit/delete Houses, Owners, Applicants

View and manage waitlists

Approve or reject applications

📁 Project Structure
Code
affordable-housing-tracker/
├── housing/              # Core app logic
│   ├── models.py         # Data models
│   ├── views.py          # Views and logic
│   ├── urls.py           # Routing
│   └── templates/        # HTML templates
├── users/                # Authentication
├── static/               # CSS, JS, images
├── templates/            # Global templates
├── manage.py             # Django CLI
└── requirements.txt      # Dependencies
📸 Screenshots
(Add screenshots to your repo and embed them here)

markdown
![Home Page](screenshots/home.png)

🛣️ Roadmap
✅ Admin CRUD for Houses, Owners, Applicants

✅ User authentication and housing applications

✅ Search and filter functionality

🔄 Waitlist prioritization algorithm

📧 Email notifications

📊 Analytics dashboard

🌍 Multi-language support

🤝 Contributing
We welcome contributions from developers, designers, and housing experts!

How to Contribute
Fork the repo

Create a feature branch (git checkout -b feature-name)

Make your changes

Commit and push (git commit -m "Add feature")

Open a pull request

Please follow the Contributor Covenant code of conduct.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
