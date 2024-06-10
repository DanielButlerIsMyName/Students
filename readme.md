# Installation and Setup

To run the Django API, you need to follow these steps:

1. Install the required dependencies using `pip`:

```shell
pip install -r requirements.txt
```

2. Apply the database migrations:

```shell
python manage.py migrate
```

3. Start the Django development server:

```shell
python manage.py runserver
```

4. Open your web browser and visit `http://localhost:8000` to access the API.

**Note for Unix Systems:**

For Unix systems, the command to use python is `python3` not just `python`.
