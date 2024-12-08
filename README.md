<h1 align="center">
    Ibrary2
</h1>
<p align="center">
    Davi Silveira Siqueira<br>
    Thiago Melato Fonseca<br>
    GAC116-10A
</p>

## Built with

![Django]

## Prerequisites

- [Python](https://www.python.org/downloads/) (3.x)
- [Django](https://www.djangoproject.com/download/) (5.x ou superior)

## Setup environment

1. Clone the repository:
```bash
git clone https://github.com/davisiqueira1/ibrary2-progweb.git
```
2. Create the virtual environment
```bash
python3 -m venv venv
```
3. Activate the virtual environment
```bash
source venv/bin/activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Run the database migrations
```bash
python3 manage.py migrate
```
6. Create a super user
```bash
python3 manage.py createsuperuser
```

## Run the server
```bash
python3 manage.py runserver
```

[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green