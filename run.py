from typing import Dict, Any, List
from datetime import datetime

from mongo_config import users, cars

user_data: Dict[str, Any] = {
    "name": "Kofi",
    "password": "password",
    "email": "mail@mail.com"
}

cars_data: List[Dict[str, Any]] = [{
    "model": "camry",
    "brand": "toyota",
    "year": datetime.utcnow()},
    {
        "model": "corolla",
        "brand": "toyota",
        "year": datetime.utcnow()}
]

if __name__ == "__main__":
    new_user = users.insert_one(user_data)
    print(f"New user => {new_user}")

    for car in cars_data:
        car.setdefault("owner", new_user.inserted_id)

    new_cars = cars.insert_many(cars_data)
    print(f"New cars => {new_cars}")
