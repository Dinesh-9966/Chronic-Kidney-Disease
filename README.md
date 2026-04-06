# 🔄 Project Update

This project was originally a desktop-based Machine Learning application.
I have upgraded and improved it with the following changes:

## ✅ Changes Made

* Converted GUI-based project → **Flask Web Application**
* Fixed deprecated sklearn functions (`plot_confusion_matrix`)
* Fixed dataset path issues
* Handled missing dependencies and environment setup
* Added frontend UI using HTML
* Added **Auto-fill demo feature**
* Fixed model input (24 features issue)
* Converted output (`1.0`) → **Readable result (CKD / NOT CKD)**
* Deployed application on **AWS EC2**

---

# 🩺 Kidney Disease Prediction (Flask Web App)

---

## 📌 Project Overview

This project predicts **Chronic Kidney Disease (CKD)** using Machine Learning.

It is now a **web-based application** built using Flask and deployed on cloud.

---

## 🧠 Machine Learning Details

* Algorithm: **Naive Bayes (GaussianNB)**
* Features: **24 medical parameters**
* Output:

  * CKD (Kidney Disease Detected)
  * NOT CKD (Healthy)

---

## 🚀 Features

* 🌐 Web-based interface (Flask)
* 📊 Real-time prediction
* ⚡ Auto-fill demo button
* ☁️ AWS EC2 deployment

---

## 📂 Project Structure

```
Chronic-Kidney-Disease/
│
├── dataset/
├── model/
├── templates/
│   └── index.html
├── webapp.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run on Server (EC2 / Linux)

### 🧩 Step 1: Connect to EC2

```bash
ssh ubuntu@YOUR-IP
```

---

### 🧩 Step 2: Clone repository

```bash
git clone https://github.com/Dinesh-9966/Chronic-Kidney-Disease.git
cd Chronic-Kidney-Disease
```

---

### 🧩 Step 3: Install system dependencies

```bash
sudo apt update
sudo apt install python3-pip python3.12-venv -y
```

---

### 🧩 Step 4: Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 🧩 Step 5: Install dependencies

```bash
pip install -r requirements.txt
pip install flask
```

---

### 🧩 Step 6: Run application

```bash
python3 webapp.py
```

---

### 🌍 Step 7: Open in browser

```
http://YOUR-IP:5000
```

---

## 🎯 Output

* CKD (Kidney Disease Detected)
* NOT CKD (Healthy)

---

## 👨‍💻 About Me

Hi, I'm **Dinesh** 👋
Machine Learning Enthusiast | Web Developer

* Interested in AI & ML
* Built and deployed on AWS EC2

---

## 🔗 Connect with Me

* GitHub: https://github.com/Dinesh-9966

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
