##🏠 Affordable Housing Tracker

A Django-powered web app to help users discover affordable housing options with ease. Built for transparency, accessibility, and real-world impact.
![sample image](./github_rent_house.jpg)  


## 🔍 Features

- 🗺️ **Interactive Listings**: Browse housing options with images and location details.
- 📦 **SQLite Backend**: Lightweight database for quick setup and local testing.
- 🛠️ **Admin Dashboard**: Manage listings and media through Django’s built-in admin panel.
- 📁 **Modular Structure**: Clean separation of concerns for easy scaling and maintenance.

---

## 🚀 Tech Stack

| Layer        | Tools Used                          |
|--------------|-------------------------------------|
| Backend      | Django, SQLite                      |
| Frontend     | HTML, CSS (via Django templates)    |
| Media        | Static image hosting                |
| Environment  | Python 3.x, Virtualenv              |

---

## 🧰 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/sudharshan59/affordable-housing-tracker.git
   cd affordable-housing-tracker
##Create and activate virtual environment

bash
#1.python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
Install dependencies

bash
#2.pip install -r requirements.txt
#3.Run migrations

bash
#4.python manage.py migrate
#5.Start the server

bash
#6.python manage.py runserver


🖼️ Media & Assets
All housing images are stored in media/houses/

Static files are managed via Django’s default configuration

🛡️ Privacy & Local Deployment
This project is designed with local-first principles—no external APIs or cloud dependencies. Ideal for internal use or secure deployment in resource-constrained environments.


Made with ❤️ by Sudharshanmonith 🔗 GitHub Profile

📬 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📄 License
This project is open-source under the MIT License.
