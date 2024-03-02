To document the steps taken to set up the project locally and the CURL commands for testing routes, you can follow these guidelines:

### Setting Up the Project Locally:

1. **Install Required Packages:** added requirements.txt
   - Django 1.11.17
   - Postgres 13
   - SQLAlchemy 1.3.17
   - Alembic 0.9.9
   - Django REST Framework 3.8.2

2. **Create Django Project:**
   - Initialize a new Django project using Django 1.11.17.
   - Set up a PostgreSQL database named `practice_data` with owner `practice_rw`.
   - Configure the Django project to connect to the PostgreSQL database.
   - Install Dependices
   ```
   pip install -r requirements.txt
   ```

```sql
-- 1. Log in to PostgreSQL
psql -U postgres

-- 2. Create a new database named practice_data
CREATE DATABASE practice_data;

-- 3. Create a new user named practice_rw with a password
CREATE USER practice_rw WITH PASSWORD 'your_password_here';

-- 4. Grant ownership of the practice_data database to the practice_rw user
ALTER DATABASE practice_data OWNER TO practice_rw;

-- 5. Optionally, grant all privileges on the practice_data database to the practice_rw user
GRANT ALL PRIVILEGES ON DATABASE practice_data TO practice_rw;

-- 6. Exit PostgreSQL
\q
```

3. **Run Migrations:**
   - Apply migrations to create the necessary database tables.

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start Development Server:**
   - Run the Django development server to test the application locally.

### CURL Commands for Testing Routes:  Need to Enter Records 

1. **GET Request to Retrieve Patients:**
   ```bash
   curl http://127.0.0.1:8000/api/patients/
   ```

2. **POST Request to Create a Patient:**
   ```bash
   curl -X POST http://127.0.0.1:8000/api/patients/ -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "phone_number": "1234567890", "date_of_birth": "1990-01-01"}'
   ```

3. **PUT Request to Update a Patient:**
   ```bash
   curl -X PUT http://127.0.0.1:8000/api/patients/1/ -H "Content-Type: application/json" -d '{"first_name": "Updated First Name", "last_name": "Updated Last Name", "email": "updated_email@example.com", "phone_number": "1234567890", "date_of_birth": "1990-01-01"}'
   ```

4. **PATCH Request to Partially Update a Patient:**
   ```bash
   curl -X PATCH http://127.0.0.1:8000/api/patients/1/ -H "Content-Type: application/json" -d '{"first_name": "Updated First Name"}'
   ```

5. **DELETE Request to Delete a Patient:**
   ```bash
   curl -X DELETE http://127.0.0.1:8000/api/patients/1/
   ```

These steps and CURL commands provide a comprehensive guide to setting up the project locally and testing the routes using CURL commands.