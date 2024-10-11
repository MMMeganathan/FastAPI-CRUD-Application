FastAPI CRUD Application
This project is a FastAPI-based web service that handles CRUD operations for two entities: Items and User Clock-In Records. The application is integrated with MongoDB for data storage and is hosted on a free hosting platform (like Koyeb or Heroku). It follows FastAPI standards for validation, error handling, and automatic documentation via Swagger UI.

Features
Items CRUD Operations: Create, retrieve, update, and delete items.
Clock-In Records CRUD Operations: Create, retrieve, update, and delete user clock-in records.
Filtering: Both entities support filtering based on various fields.
Aggregation: MongoDB aggregation to count items by email.
MongoDB Integration: Uses MongoDB to store and manage data.
FastAPI Standards: Utilizes FastAPI's capabilities for Pydantic models, validation, and Swagger UI for API documentation.
Technologies Used
FastAPI: Web framework for building APIs.
MongoDB: NoSQL database for data storage.
Pymongo: MongoDB driver for Python.
Uvicorn: ASGI server for FastAPI.
Swagger: Auto-generated API documentation.
Requirements
Python 3.7+
FastAPI
Uvicorn
Pymongo
MongoDB (either Atlas or local instance)
Setup and Installation
Clone the repository:

bash
Copy code
git clone https://github.com/MMMeganathan/FastAPI-CRUD-Application.git
Navigate to the project directory:

bash
Copy code
cd fastapi-crud-app
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up MongoDB:

If using MongoDB Atlas, create a new cluster and get the connection string.
If using local MongoDB, ensure MongoDB is running on your machine.
Create a .env file in the root directory and add your MongoDB connection string:

bash
Copy code
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
Run the application:

bash
Copy code
uvicorn main:app --reload
Open the app in your browser:

Swagger UI documentation will be available at: http://127.0.0.1:8000/docs
Redoc documentation at: http://127.0.0.1:8000/redoc
API Endpoints
Items API
POST /items: Create a new item.
Body: name, email, item_name, quantity, expiry_date
GET /items/{id}: Get item by ID.
GET /items/filter: Filter items by email, expiry_date, insert_date, or quantity.
GET /items/aggregate: Aggregate items by email to get count.
PUT /items/{id}: Update item by ID (except for insert_date).
DELETE /items/{id}: Delete item by ID.
Clock-In Records API
POST /clock-in: Create a new clock-in entry.
Body: email, location
GET /clock-in/{id}: Get clock-in record by ID.
GET /clock-in/filter: Filter clock-in records by email, location, or insert_date.
PUT /clock-in/{id}: Update clock-in entry by ID (excluding insert_date).
DELETE /clock-in/{id}: Delete clock-in entry by ID.
How to Run the Project Locally
Ensure MongoDB is running and accessible via the MONGO_URI.
Install all dependencies using pip install -r requirements.txt.
Start the FastAPI server using uvicorn main:app --reload.
Access the APIs through the Swagger UI at http://127.0.0.1:8000/docs.
How to Deploy
The application can be deployed on free hosting platforms like Koyeb, Heroku, or Deta. Here's an example of deploying on Heroku:

Create a Procfile in the project root:

less
Copy code
web: uvicorn main:app --host 0.0.0.0 --port $PORT
Commit the changes and push to a Heroku app:

bash
Copy code
git add .
git commit -m "Deploying to Heroku"
git push heroku master
Set the MongoDB connection string on Heroku:

bash
Copy code
heroku config:set MONGO_URI=<your_mongodb_connection_string>
Visit the Heroku app URL and access the API documentation.

Environment Variables
MONGO_URI: MongoDB connection string. You can store this in .env locally and in hosting environment variables in production.
Hosting and Deployment Links
GitHub Repo: https://github.com/yourusername/fastapi-crud-app
Hosted Swagger Documentation: Hosted URL
License
This project is licensed under the MIT License - see the LICENSE file for details.

