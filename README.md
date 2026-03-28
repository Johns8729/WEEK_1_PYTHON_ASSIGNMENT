# 🛒 Store Sales System (Python)

## 📌 Description

This Python program simulates a simple store sales registration system. It allows the user to input product sales one by one, validates the data entered, and generates a summary of all sales at the end of the day.

---

## ⚙️ Features

* Input and validation of:

  * Product name (cannot be empty or contain numbers)
  * Product price (must be a positive number)
  * Quantity sold (must be greater than 0)
* Calculates total per sale
* Accumulates total earnings for the day
* Stores all sales in a list
* Displays a complete summary at the end

---

## 🧠 How It Works

1. The program starts by welcoming the user.
2. It enters a loop where sales are registered.
3. For each sale:

   * The product name is validated.
   * The price is validated (must be numeric and non-negative).
   * The quantity is validated (must be an integer greater than 0).
4. The total for each sale is calculated and added to the daily total.
5. The sale is stored in a list as a tuple `(product, price, quantity)`.
6. The user is asked if they want to continue.
7. When finished, a summary of all sales and the total collected is displayed.

---

## ▶️ How to Run

1. Make sure you have Python installed (Python 3 recommended).
2. Save the code in a file, for example:

   ```bash
   store.py
   ```
3. Run the program:

   ```bash
   python store.py
   ```

---

## 📝 Example Output

```
...Welcome to the store...

Product name: Apple
Product price: 2.5
Quantity sold: 3
Sale registered.
Sale total: $7.50

Do you want to register another sale? (yes/no): no

Day summary:
Product: Apple | Price: 2.5 | Quantity: 3
Total collected during the day: $7.50
```

---

## 📦 Data Structure Used

* `store_products`: List that stores tuples with:

  * Product name
  * Price
  * Quantity
* Example:

  ```python
  [("Apple", 2.5, 3), ("Banana", 1.2, 5)]
  ```

---
## 🔄 Program Flow Diagram
<img width="570" height="1070" alt="QJ drawio" src="https://github.com/user-attachments/assets/8a7009c7-2c8b-4d86-b3d1-b14eae114cdd" /> 

--- 

Repository
https://github.com/Johns8729/WEEK_1_PYTHON_ASSIGNMENT/edit/main/README.md


