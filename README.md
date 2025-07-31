# 🔍 OSINT Username Checker

A simple Flask-based web app that checks the availability of a given username across popular social media platforms. Great for **open-source intelligence (OSINT)** investigations or brand protection.

---

## 🌐 Features

- Checks usernames across **popular platforms** like Facebook, Instagram, Twitter (X), Reddit, GitHub, TikTok, etc.
- Beautiful **dark-themed UI** with clear ❌ / ✅ indicators
- Direct **links to the detected profiles**
- Basic suspicious flagging (can be expanded for threat intelligence)

---

## 📸 UI Preview

<img width="1920" height="887" alt="Screenshot 2025-07-31 175803" src="https://github.com/user-attachments/assets/876b7ea4-0c2f-4556-be89-7c34acd0c284" />


---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **Requests**
- **HTML5 + CSS3**

---

## 🚀 Getting Started

### 1. Install Dependencies

Make sure Python is installed (preferably Python 3.9+):

```
pip install flask requests
```

### 2. Run the App

```
python app.py
```

Visit: http://127.0.0.1:5000

## 📂 Project Structure

```
osint-username-checker/
│
├── app.py                  # Main Flask backend
├── templates/
│   └── index.html          # Frontend HTML
├── static/
│   └── style.css           # Dark theme styles
└── README.md
```

## 🔒 Platforms Checked
Facebook

Instagram

X (Twitter)

Reddit

GitHub

TikTok

Pinterest

## ✅ Example


#### Input:
```
username: Skanthasishanth
```

#### Output:

```
Platform	Status	Link	             Suspicious
Facebook	❌      Not Found	Visit	   No
Instagram	❌      Not Found	Visit	   No
GitHub	     ✅         Found	        Visit	    No
```		

## 📌 Notes

This tool only checks public profiles.

For private usernames or API-restricted platforms, detection may be limited.

Use responsibly for educational or legal OSINT purposes.

## 🙋‍♂️ Author
#### Developed by S Kantha Sishanth
