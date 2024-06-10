# Installation and Setup

To run the Django API, you need to follow these steps:

1. Install `pip` if it is not already installed on your system.

2. Install the required dependencies using `pip`:

```shell
python3 -m pip install -r requirements.txt --break-system-packages
```

3. Apply the database migrations:

```shell
python3 manage.py makemigrations students
python3 manage.py migrate
```

4. Start the Django development server:

```shell
python3 manage.py runserver
```

5. Open your web browser and visit `http://localhost:8000` to access the API.

**Note for Windows Users:**

If you are using Windows, the commands might be slightly different. Instead of using `python3`, you can use `python` to run the commands. For example:

```shell
python -m pip install -r requirements.txt --break-system-packages
```

Make sure to adjust the commands accordingly when following the installation and setup steps.

