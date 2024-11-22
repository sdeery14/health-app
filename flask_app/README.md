# Health App - Flask Backend

## Introduction
This is the backend for the Health App, built using Flask. The backend handles creating the database, data storage, user authentication, and provides APIs for the frontend to interact with.

## Setup

### Tools
- Python 3.12
- Poetry
- Flask
- SQLAlchemy
- PostgreSQL

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/health-app.git
    cd health-app/flask_app
    ```

2. Install Poetry if you haven't already:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. Install the required packages and create a virtual environment using Poetry:
    ```bash
    poetry install
    ```

4. Start the PostgreSQL database using Docker Compose:
    ```bash
    docker-compose up -d
    ```

5. Enter the Poetry shell:
    ```bash
    poetry shell
    ```

6. Initialize and upgrade the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

7. Run the Flask development server:
    ```bash
    flask run
    ```

### Verify Database Schema

To verify that the database schema was created successfully, follow these steps:

1. **Log into the PostgreSQL Docker Container**:

Run the following command to access the PostgreSQL container:

```bash
docker exec -it flask_db_service psql -U flask_user -d flask_db
```

2. **Check the Schema**:

Once you are inside the `psql` shell, list all tables to verify that the schema was created:

```sql
\dt
```

You should see a table named `data` in the list. To view the columns of the `data` table, use:

```sql
\d data
```

This will display the structure of the `data` table, including the columns `id`, `name`, and `value`.

3. **Exit the `psql` Shell**:

To exit the `psql` shell, type:

```sql
\q
```


### Database Architecture
1. Key Tables and Relationships:
    From the field descriptions, the database will likely include:
    - **Food**: Main table for food items.
    - **Nutrient**: Nutrient details (e.g., protein, vitamins).
    - **FoodNutrient**: Many-to-many relationship between food and nutrients.
    - **Category**: Categories for food items.
    - **MeasureUnit**: Units for measuring nutrient amounts.
    - **DataSource**: Information about where the data originates.
    - **FoodCategory**: High-level categorization of foods.

2. Relationships Overview:
    - **FoodCategory → Food**:
        - A food item belongs to one category.
        - One category can contain many food items.
    - **Food ↔ Nutrient**:
        - A many-to-many relationship exists via FoodNutrient.
        - Foods contain nutrients with specific amounts.
    - **MeasureUnit**:
        - Units used to measure nutrient amounts (e.g., grams, milligrams).
    - **DataSource → Food**:
        - Links foods to their data sources (e.g., SR Legacy, Foundation Foods).

### Database Implementation
1. Configure the database URI in `config.py`:
    ```python
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/health_app'  # Update with your Postgres credentials
    ```

2. Start the PostgreSQL database using Docker Compose:
    ```bash
    docker-compose up -d
    ```

3. Initialize and upgrade the database:
    ```bash
    poetry shell
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

4. Making Changes in `models.py` with SQLAlchemy:
    - To make changes to your database models, edit the `models.py` file.
    - After making changes, create a new migration:
        ```bash
        flask db migrate -m "Description of changes"
        ```
    - Apply the migration to the database:
        ```bash
        flask db upgrade
        ```

### Running the App
1. Set the Flask app environment variable:
    ```bash
    export FLASK_APP=app.py  # On Windows use `set FLASK_APP=app.py`
    ```

2. Run the Flask development server:
    ```bash
    flask run
    ```

## Project Structure
```
flask_app/
│
├── app.py              # Main application file
├── config.py           # Configuration file
├── models.py           # Database models
├── routes.py           # API routes
├── requirements.txt    # Python dependencies
└── migrations/         # Database migrations
```

## API Endpoints
- `GET /api/health`: Check the health of the application.
- `POST /api/register`: Register a new user.
- `POST /api/login`: Authenticate a user.
- `GET /api/user`: Get user details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
