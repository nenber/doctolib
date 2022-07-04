set up the virtual environement
	python -m venv .venv
	. .venv/bin/activate
	pip install -r requirements.txt
	
check si les modules installés sont les même que sur le requirements.txt avec pip freeze

pour lancer le serveur
cd src
python manage.py migrate
python manage.py runserver
