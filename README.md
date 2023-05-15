# peydayeri
Multi-Store project backend using DRF

This project is dockerized and uses the technologies below:
* Python programming language
* Django web framework
* Django rest framework
* Gunicorn WSGI HTTP server
* JWT Authentication
* PostgreSQL Database
* Redis cache
* RabbitMQ message broker
* Celery task queue
* ELK Stack
* MinIO Object Storage
* Docker & Docker compose
* Nginx web server
* IPPanel SMS Panel
* ZarrinPal payment gateway

You can run it quickly using the below command:
```commandline
docker compose --env-file ./backend/apps/core/.env up
```