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

test-cov:
	poetry run coverage run --source='.' manage.py test
	poetry run coverage xml

check:
	make selfcheck
	make lint
	make test-cov

migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

dev-server:
	poetry run python3 manage.py runserver

db-clean:
	poetry run python3 manage.py flush --noinput

deploy:
	make install
	make db-clean
	make migrate

PORT ?= 8000
product-server:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi
