# Installation and Setup

To run the Django API, you need to follow these steps:

1. Install `pip` if it is not already installed on your system.

2. Install the required dependencies using `pip`:

```shell
pip install -r requirements.txt
```

3. Apply the database migrations:

```shell
python manage.py migrate
```

4. Start the Django development server:

```shell
python manage.py runserver
```

5. Open your web browser and visit `http://localhost:8000` to access the API.

**Note for Unix Systems:**

For Unix systems, the command to use python is `python3` not just `python`.
