# Django TODO List API

A simple RESTful API built with Django and Django REST Framework to manage a TODO list.

## Features

* List all tasks
* Create a new task
* View details of a specific task
* Update an existing task
* Delete a task
* Mark a task as completed/uncompleted (custom endpoints)

## Technologies Used

* [Python](https://www.python.org/) (version 3.11.9)
* [Django](https://www.djangoproject.com/) (version 5.2.1)
* [Django REST Framework](https://www.django-rest-framework.org/) (version 5.16.0)
* [SQLite](https://www.sqlite.org/index.html) (default database for development)

## Prerequisites

* Python 3.8+
* pip (Python package manager)
* Git

## Development Environment Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    # .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Make sure you have a `requirements.txt` file in your project. Generate it with `pip freeze > requirements.txt` with your virtual environment activated).*

4.  **Run database migrations:**
    ```bash
    python manage.py makemigrations api
    python manage.py migrate
    ```

5.  **(Optional) Create a superuser to access the Django Admin:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
    The API will be accessible at `http://127.0.0.1:8000/api/v1/`.

## API Endpoints

The base URL for the API is `/api/v1/`.

* `GET /tasks/`: Lists all tasks.
* `POST /tasks/`: Creates a new task.
    * Request body (JSON): `{"title": "New Task", "description": "Optional description"}`
* `GET /tasks/{id}/`: Returns details of a specific task.
* `PUT /tasks/{id}/`: Updates an existing task.
    * Request body (JSON): `{"title": "Updated Title", "description": "New Description", "completed": true}`
* `PATCH /tasks/{id}/`: Partially updates an existing task.
* `DELETE /tasks/{id}/`: Deletes a task.
* `POST /tasks/{id}/mark-completed/`: Marks a task as completed.
* `POST /tasks/{id}/mark-uncompleted/`: Marks a task as uncompleted.

## How to Contribute (Optional)

If you want to add a section on how others can contribute:

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License (Optional)

Distributed under the MIT License. See `LICENSE` for more information.
*(If you add a LICENSE file to your project)*

---

Developed by [Your Name/Nickname](link_to_your_github_profile_or_website)
