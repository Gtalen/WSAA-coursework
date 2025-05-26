# WSAA-coursework
# Higher National Diploma in Science in Computing (Data Analytics)

## Web Service and Applications Module (8640: 2024-2025)

## Atlantic Technological University (ATU) Galway

## Author: Ebelechukwu Igwagu

---

## Description

This repository contains my assignments and project submissions for the Web Services and Applications module at ATU Galway. The aim of these assignments is to demonstrate my understanding of Application Programming Interfaces (APIs), particularly RESTful APIs, and how to interact with them using Python. The project demonstartes performing create, read, update and Delete (CRUD) operations on RestAPIs.

---

## Assignments

- Assignment 2:  A Python program that interacts with the [deck of card API](https://deckofcardsapi.com/). It shuffles a deck, draws cards, and displays each card's value and suit. This can be accessed here [Assignment2_carddraw.ipynb](https://github.com/Gtalen/WSAA-coursework/blob/main/WSAA_Assignments/Assignment2_carddraw.ipynb).

- Assignment 3: A Python program that retrieves the dataset for the Exchequer Account (Historical Series) from the CSO API. The data is stored in a file named  [cso.json](https://github.com/Gtalen/WSAA-coursework/blob/main/WSAA_Assignments/cso.json). The program can be accessed here [assignment03-cso.py](https://github.com/Gtalen/WSAA-coursework/blob/main/WSAA_Assignments/assignment03-cso.py).

- Assignment 4:  A Python program that reads a file from the repository [Gtalen/Authentication-testin](https://github.com/Gtalen/Authentication-testin/blob/main/ab.txt), replaces all occurrences of the text "andrew" with "ebele", and commits the updated file back to the repository. [assignment04-github.py](https://github.com/Gtalen/WSAA-coursework/blob/main/WSAA_Assignments/assignment04-github.py)

---

## Project - Investment Portfolio Management System(IPM)

This is a web service application for managing investment portfolios, including user accounts, stock information, and transactions. This webapplication is hosted (here)[https://gtalen.pythonanywhere.com/]

---

## Project Overview

The Investment Portfolio Management System (IPM) allows users to manage their stock investments through a user-friendly web interface and RESTful API backend. It supports user registration, stock management, and transaction tracking (buy/sell) which are implementation of CRUD operations using HTML methods. The app is designed with modular data access object classes to handle database operations using python. 

---

### Project Structure

The Investment portfolio database has three tables; Users, Stocks and transactions and the scripts for creating the database can be accessed (here)(https://github.com/Gtalen/WSAA-coursework/blob/main/WSAA_Project/db_schema.py).

The database design followed best practices and principles outlined by [(Kumaresh, 2024)](https://medium.com/@saikumaresh/a-comprehensive-guide-to-schema-design-in-sql-principles-best-practices-and-a-practical-use-case-d10f87777cef) and [Microsoft Database Design Basics](https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5)


```
ipm/
│
├── app.py                      # Flask application and routes
├── users_dao.py               # Data access for users
├── stocks_dao.py              # Data access for stocks
├── transactions_dao.py        # Data access for transactions
├── sql_connect.py             # MySQL database connection helper
├── templates/
│   ├── ipm_base.html          # Base HTML
│   ├── ipm_user.html          # User management UI
│   ├── ipm_stock.html         # Stock management UI
│   └── ipm_transaction.html   # Transaction management UI
├── static/                    # CSS, JS, images, etc.
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

```

The user table was initially populated using fake 50 user data generated with python Faker using the (Faker documentation)(Faker documentation.) [https://faker.readthedocs.io/en/master/fakerclass.html] and the useful article from (Datacamp)[https://www.datacamp.com/tutorial/creating-synthetic-data-with-python-faker-tutorial] as a guide. The individual scripts can be accessed from the (user_data)[https://github.com/Gtalen/WSAA-coursework/blob/main/WSAA_Project/user_data.py], (stock_data)[https://github.com/Gtalen/WSAA-coursework/blob/main/WSAA_Project/stocks_data.py] and (transactions_data)(https://github.com/Gtalen/WSAA-coursework/blob/main/WSAA_Project/transactions_data.py) for the respective tables. The stock data was populated using data gotten from (Yahoo Screener)(https://finance.yahoo.com/research-hub/screener/) via url (request)[https://github.com/Gtalen/WSAA-coursework/blob/main/WSAA_Project/stock_symbols.py]


Three classes of Data Access Object(DAO) was set up for the three tables and these were written with Pymysql. (Amos)( https://realpython.com/python3-object-oriented-programming/) overview of object oriented programming provided the much needed insight on on OOP and its Class use in DAO. The DAO can be accessed from (userDAO)[https://github.com/Gtalen/WSAA-coursework/blob/main/WSAA_Project/users_dao.py], (stocksDAO)[https://github.com/Gtalen/WSAA-coursework/blob/main/WSAA_Project/stocks_dao.py] and (transactionsdao)[https://github.com/Gtalen/WSAA-coursework/blob/main/WSAA_Project/transactions_dao.py].

The main application {"ipm_app.py"} was set up with Flask and the frontend using html, AJAX and CSS. W3 school tutorials provided useful sample codes and foundational knowledge in these languages such as for for creating html forms, tables and CSS styling used in the frontend development.

---

### IPM Features and API Endpoints

#### 👤 **User Management**

| **Features** | **API Endpoints** |
|--------------|-------------------|
| - Register new users  <br> - View user profiles  <br> - Reset passwords  <br> - Delete accounts | `GET /api/users` — Get all users  <br> `GET /api/users/<user_id>` — Get user by ID  <br> `GET /api/users/email?email=<email>` — Get user by email  <br> `POST /api/users/new-user` — Create new user  <br> `PUT /api/users/reset_password` — Reset password  <br> `DELETE /api/users/<user_id>` — Delete user |


#### 📈 **Stock Management**

| **Features** | **API Endpoints** |
|--------------|-------------------|
| - Create, view, update, delete stocks  <br> - Search by ID or symbol | `GET /api/stocks` — List all stocks  <br> `GET /api/stocks/<stock_id>` — Get stock by ID  <br> `GET /api/stocks/symbol/<symbol>` — Get stock by symbol  <br> `POST /api/stocks` — Create stock  <br> `PUT /api/stocks/<stock_id>` — Update stock  <br> `DELETE /api/stocks/<stock_id>` — Delete stock |

---

#### 💰 **Transaction Management**

| **Features** | **API Endpoints** |
|--------------|-------------------|
| - Create buy/sell transactions  <br> - View transactions by user or stock  <br> - Update or delete transactions | `GET /api/transactions/<transaction_id>` — Get by ID  <br> `GET /api/transactions/user/<user_id>` — Get by user  <br> `GET /api/transactions/stock/<stock_id>` — Get by stock  <br> `POST /api/transactions` — Create transaction  <br> `PUT /api/transactions/<transaction_id>/quantity` — Update quantity  <br> `PUT /api/transactions/<transaction_id>/price` — Update price  <br> `DELETE /api/transactions/<transaction_id>` — Delete transaction |

---

> 📌 **Note**: Not all endpoints are yet integrated with the frontend. Use tools like Postman or `curl` for testing.


## IPM Features - CRUD

- **User Management**
  - Register new users
  - View user profiles
  - Reset user passwords
  - Delete user accounts

- **Stock Management**
  - Create, view, update, and delete stock entries
  - Search stocks by ID or symbol
 
- **Transaction Management**
  - Create buy/sell transactions
  - View transactions by user or stock
  - Update transaction quantity
  - Delete transactions

- **Frontend**
  - Responsive HTML pages for Users, Stocks, and Transactions. 
  - AJAX-based CRUD operations for dynamic interaction.
  

---

### Technology Stack

- Backend: Python, Flask, PyMySQL
- Frontend: HTML, Bootstrap 5, jQuery AJAX
- Database: MySQL 
- Authentication: Password hashing with Werkzeug security
- API: RESTful endpoints for CRUD operations
- Others: Flask-CORS nabled to support frontend-backend communication during development.

---

### Setup & Installation

1. **Clone the repository:**

   ```bash
   https://github.com/Gtalen/WSAA-coursework.git
   cd WSAA-project

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

3. **Configure your MySQL database:**

- Create the database schema as per the sql/schema.sql file.
- Update your database connection settings in sql_connect.py.

4. **Run the Flask app:**`

   ```bash
   python ipm_app.py

5. Access the App: Open your browser and navigate to http://127.0.0.1:5000/

---

### API Endpoints

Note: All endpoints are not yet functional on the frontend, but all can be accessed with either curl or postman.

#### Users:

- GET /api/users — Get all users
- GET /api/users/<user_id> — Get user by ID
- GET /api/users/email?email=<email> — Get user by email
- POST /api/users/new-user — Create new user
- PUT /api/users/reset_password — Update user password
- DELETE /api/users/<user_id> — Delete user

#### Stocks:

- GET /api/stocks — List all stocks
- GET /api/stocks/<stock_id> — Get stock by ID
- GET /api/stocks/symbol/<symbol> — Get stock by symbol
- POST /api/stocks — Create new stock
- PUT /api/stocks/<stock_id> — Update stock
- DELETE /api/stocks/<stock_id> — Delete stock

#### Transactions:

- GET /api/transactions/<transaction_id> — Get transaction by ID
- GET /api/transactions/user/<user_id> — Get transactions by user
- GET /api/transactions/stock/<stock_id> — Get transactions by stock
- POST /api/transactions — Create new transaction
- PUT /api/transactions/<transaction_id>/quantity — Update transaction quantity
- PUT /api/transactions/<transaction_id>/price — Update transaction price
- DELETE /api/transactions/<transaction_id> — Delete transaction
---

---

#### Future Improvements:

- Add user authentication & session management
- Add detailed transaction analytics and portfolio summary

---

### Contributors

Author: Ebelechukwu Igwagu

---

### Additional Acknowledgement

ChatGPT AI (2025). Used to assist the author with technical explanations and productivity, particularly for debugging and implementing jQuery AJAX for front-end interaction. The scope, logic, and design decisions of the project remain fully original to the author. Some of the Prompts used were;

- How do I implement jQuery AJAX in my Flask app?

- Help me connect frontend user.html to my Flask backend.

- Why is my AJAX call not returning data from Flask.

- How do I use Bootstrap buttons and components.

- Is there a way to use python to generate fake fullname of people?

---

### Want to contribute?

This project is open to contributions! Feel free to fork the repository, submit issues, or create pull requests. All contributions are welcome.

---

### License

This project is available under the MIT license.

---

### References

- Amos, D. (2024). Object-Oriented Programming (OOP) in Python. Available at: https://realpython.com/python3-object-oriented-programming/

- Bootstrap Contributors (n.d.). Buttons. Available at: https://getbootstrap.com/docs/4.0/components/buttons/

- DataCamp (n.d.). Creating Synthetic Data with Python and Faker. Available at: https://www.datacamp.com/tutorial/creating-synthetic-data-with-python-faker-tutorial [Accessed 18 May 2025].

- Database design basics - Microsoft Support (n.d.). Available at: https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5

- Faker (2025). Using the Faker Class. Available at: https://pypi.org/project/Faker/

- Faker 37.3.0 documentation (n.d.). Using the Faker Class. Available at: https://faker.readthedocs.io/en/master/fakerclass.html

- Kumaresh, S. (2024). A Comprehensive Guide to Schema Design in SQL: Principles, Best Practices, and a Practical Use Case with Netflix. Medium, 19 November. Available at: https://medium.com/@saikumaresh/a-comprehensive-guide-to-schema-design-in-sql-principles-best-practices-and-a-practical-use-case-d10f87777cef

- Looka (n.d.). Logo created using Looka logo generator. Available at: https://looka.com [Accessed 24 May 2025].

- Product directory - Euronext exchange Live quotes (n.d.). Available at: https://live.euronext.com/en/markets/dublin/equities/list

- W3Schools.com (n.d. a). CSS Colors Reference. Available at: https://www.w3schools.com/cssref/css_colors.php

- W3Schools.com (n.d. b). CSS Default Styles. Available at: https://www.w3schools.com/css/default.asp

- W3Schools.com (n.d. c). AJAX Introduction. Available at: https://www.w3schools.com/js/js_ajax_intro.asp

- W3Schools.com (n.d. d). HTML Tables. Available at: https://www.w3schools.com/html/html_tables.asp

- Yahoo Finance Screeners (n.d.). Available at: https://finance.yahoo.com/research-hub/screener/ 
