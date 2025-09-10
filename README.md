# Bike_Rental_System

A Python application that simulates a bike rental shop.  
Customers can rent different types of bikes (`Mountain`, `Road`, `Touring`) on an **hourly, daily, or weekly** basis.  
The system also supports discounts, coupon codes, and generates end-of-day reports.

---

## ✨ Features
- Rent **Mountain**, **Road**, or **Touring** bikes
- Rental options:
  - Hourly ($5/hour)
  - Daily ($20/day)
  - Weekly ($60/week)
- **Family discount**: 25% off for 3–5 bikes rented together
- **Coupon support**: 10% off with valid coupon code (`***BBP`)
- Inventory tracking (reduces stock when rented, adds back when returned)
- End-of-day report showing:
  - Total bikes rented
  - Total revenue earned

---

## 🛠️ Technologies Used
- Python 3
- Built-in `datetime` module

---

## ▶️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/MarcelBlasingame/bike-rental-system.git
   cd bike-rental-system
