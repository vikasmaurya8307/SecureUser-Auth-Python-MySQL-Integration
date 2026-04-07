# SecureUser-Auth-Python-MySQL-Integration

📌 Project Overview
Yeh ek robust User Authentication System hai jo Python aur MySQL ke integration par based hai. Is project mein secure Sign-Up, Login, aur User Management functionalities ko handle kiya gaya hai. Iska primary objective relational database connectivity aur backend logic building ko showcase karna hai.

🚀 Key Features
Secure Sign-Up: Users ka data directly MySQL database mein store karne ke liye INSERT queries ka use.

User Authentication: Login system jo input credentials ko database record se match karta hai.

Database Management: Connection pooling aur exception handling ka use taaki connectivity stable rahe.

User Listing: Admin functionality ke taur par saare registered users ko fetch karne ka feature.

Modular Code: Har feature ke liye alag module (login.py, signup.py, etc.) taaki code maintainable rahe.

🛠️ Tech Stack
Language: Python 3.x

Database: MySQL (Relational DBMS)

Libraries: mysql-connector-python, pandas

📁 File Structure
database1.py: Database connection settings aur connectivity logic.

menu.py: Main entry point jahan se user choice select karta hai.

signup.py: Naye users ko register karne ka module.

login.py: Existing users ko authenticate karne ka logic.

show_user.py: Database se saare users ko display karne ka function.

⚙️ How to Setup
Apne local system mein MySQL install karein aur ek database banayein jiska naam login_system ho.

Ek table create karein:

SQL
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);
database1.py mein apne MySQL credentials (host, user, password) update karein.

menu.py file ko run karein:

Bash
python menu.py
👨‍💻 Developed By
Vikas Maurya

Data Analyst | Python Developer

GitHub: @vikasmaurya8307
