# API FastAPI standard functions

# Installation

### [Python 3](https://www.python.org/downloads/) must be already installed
### You need to substitute your data into variables in database.py line 5 and alembic.ini line  63
```shell
git clone https://github.com/Ilyakson/FastAPIDefaultProject.git
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
alembic revision --autogenerate -m "Migration description"
uvicorn main:app --reload
```