# ConsumerAffairs Practical Test - The Eye

## Pre-requisites

1. Python 3.9.5
2. Docker and Docker Compose

## How to run the application

1. Define environment variables (rename .env.example to .env)
2. Run docker compose: \
   `docker-compose up -d --build`
3. Create a new user (remember to change the username): \
   `docker-compose exec web python the_eye/manage.py createsuperuser --username <username> --email <username>@email.com --noinput`
4. Generate authentication token to the new user (again, remeber to change the username):\
   `docker-compose exec web python the_eye/manage.py drf_create_token <username>`
5. The application will run locally at port 8080:
   - /api/events: \
     - GET: List all events with possibility to filter the results by session_id, category and timestamp range, usinf **start** and **end** fields
     - POST: Create a new event
   - /api/errors: \
     - GET: List all events

## Conclusions

- I tried to keep it simple not to consume much time. I started to configure and write some tests, but I was short on time and couldn't finish it.
- I used celery to process the events, so the application could handle a big amount of events/second. Already used Google Pub/Sub in a similar scenario and work fine as well.
