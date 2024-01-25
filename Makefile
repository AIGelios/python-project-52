install:
	poetry install

loc-upd:
	django-admin makemessages -l ru

loc-com:
	django-admin compilemessages

selfcheck:
	poetry check

shell:
	poetry run python3 manage.py shell_plus --ipython

lint:
	poetry run flake8 task_manager --exclude migrations

test:
	poetry run python3 manage.py test

check:
	make selfcheck
	make lint
	make test

migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

dev-server:
	poetry run python3 manage.py runserver

deploy:
	make install
	make migrate

PORT ?= 8000
product-server:
	poetry run gunicorn -w 5 0.0.0.0:$(PORT) task_manager.wsgi
