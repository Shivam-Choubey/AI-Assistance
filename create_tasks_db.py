from pymongo import MongoClient

# MongoDB connection string
MONGO_URI = "mongodb+srv://Choubey:<db_password>@cluster0.66ldgap.mongodb.net/"  # Replace with MongoDB Atlas connection if needed

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Specify the database and collection (they will be created automatically if they don't exist)
db = client["task_manager_db"]
tasks_collection = db["tasks"]

# Sample task data to insert into the collection for testing
sample_task = {"task": "Sample Task: Set up MongoDB", "status": "pending"}

# Insert the sample task (this will create the collection if it doesn't exist)
tasks_collection.insert_one(sample_task)

# Retrieve the inserted task to verify the connection
task = tasks_collection.find_one({"task": "Sample Task: Set up MongoDB"})

# Output the inserted task
print(f"Inserted task: {task}")

# Close the connection
client.close()

print("Database initialized and sample task inserted successfully.")
