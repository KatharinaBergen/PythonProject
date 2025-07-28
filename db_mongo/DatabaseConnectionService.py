from mongoengine import connect

# Connect to MongoDB (replace params with your own)
connect(
    db="mongo-db",
    username="user",
    password="password",
    host="localhost",
    port=27017,
    authentication_source='admin'  # or the db where your user is defined
)
