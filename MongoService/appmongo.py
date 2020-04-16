import time
from uuid import uuid4
from MongoService.storage import MongoService

storage = MongoService.get_instance()

for _ in range(5):
    dto = {
        "id": str(uuid4()),
        "payload": str(uuid4()),
        "field": int(time.time())
    }
    storage.save_data(dto)

for data in storage.get_data():
    print(data)
