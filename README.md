# 🚚 Biztab Shipment Tracking & Delivery Management System

## 📌 Project Overview

The **Biztab Shipment Tracking & Delivery Management System** is a logistics-focused web application developed to manage and monitor the shipment lifecycle from dispatch to successful delivery.

This project simulates the **Shipment Tracking & Delivery Module (Steps 7–9)** of the Order-to-Delivery business workflow and provides real-time shipment status monitoring, courier assignment, customer notifications, and delivery completion management.

---

## 🎯 Problem Statement

Organizations require an efficient mechanism to:

* Track shipments throughout the delivery lifecycle
* Provide visibility into shipment status
* Manage delivery operations
* Handle delivery exceptions
* Improve customer communication

This project addresses these challenges through an interactive shipment tracking dashboard.

---

## 🏗️ System Architecture

Customer Order

↓

Shipment Creation

↓

Courier Assignment

↓

Shipment Tracking

↓

Customer Notifications

↓

Delivery Completion

---

## ✨ Key Features

### 🔐 Authentication

* Secure login portal
* Session-based access control

### 📦 Shipment Management

* Create new shipments
* Generate unique shipment IDs
* Capture shipment details

### 🚚 Courier Assignment

* Automatic courier allocation
* Vehicle information management
* Delivery ownership tracking

### 📍 Shipment Tracking

* Multi-stage shipment lifecycle
* Real-time status progression
* Visual delivery workflow

### 📩 Customer Notifications

* Shipment update simulation
* Status communication workflow

### ⚠️ Exception Handling

* Delivery failure simulation
* Reattempt scheduling workflow

### 📜 Shipment History

* Shipment activity records
* Delivery audit tracking

### ✅ Delivery Completion

* Final delivery confirmation
* Delivery summary dashboard

---

## 🛠️ Technology Stack

| Component               | Technology   |
| ----------------------- | ------------ |
| Frontend                | Streamlit    |
| Backend Logic           | Python       |
| Data Storage            | JSON         |
| Version Control         | Git & GitHub |
| Development Environment | VS Code      |

---

## 📂 Project Structure

```text
biztab_shipment_tracker/
│
├── assets/
│   └── delivery_agents.json
│
├── core/
│   ├── authentication.py
│   ├── notification_engine.py
│   └── shipment_engine.py
│
├── database/
│   ├── shipments.json
│   └── notifications.json
│
├── styles/
│   └── style.css
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/Nikithayyadav/biztab-shipment-tracking-system.git
```

### Navigate to Project

```bash
cd biztab-shipment-tracking-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🔑 Demo Credentials

Username:

```text
admin
```

Password:

```text
biztab2026
```

---

## 📈 Business Benefits

* Improved shipment visibility
* Better customer communication
* Delivery workflow transparency
* Operational efficiency
* Exception management support

---

## 🔮 Future Enhancements

* GPS-based live tracking
* Interactive maps integration
* SMS and Email notifications
* Database integration (MySQL/PostgreSQL)
* Multi-user role management
* Analytics and reporting dashboard

---

## 👨‍💻 Developer

**Chandavena Nikitha**

B.Tech – Computer Science & Engineering (Artificial Intelligence)

ICFAI University Hyderabad

GitHub: https://github.com/Nikithayyadav

---

## 📄 License

This project was developed for educational and technical assessment purposes.
