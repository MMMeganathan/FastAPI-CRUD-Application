import motor.motor_asyncio


##client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://<username>:<password>@cluster.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://Meganathan045:<4445>@cluster0.u9hqu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.data_collection
items_collection = db.items
clock_in_collection = db.clock_in