# Message Service

Install docker and docker compose
Intall python

Add credentials to docker-compose file

Run docker build . -t message_service
Run docker-compose up -d redis
Run docker-compose up -d message_service

To test run python test_pub.py rr_notifications <# of msgs> <phone number>
Ex: python test_pub.py rr_notifications 10 +11234567
