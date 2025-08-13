from typing import List

from app.models.todo import TodoItem
from app.models.user import UserCreate

import json
import os


class JsonController:
    def build_path(self, file_name: str):
        curr_dir = os.path.abspath(
            os.path.dirname(
                __file__
            )
        )

        one_up = os.path.abspath(os.path.dirname(curr_dir))
        data_dir = os.path.join(one_up, "data")

        if not os.path.isdir(data_dir):
            os.makedirs(data_dir, exist_ok=True)

        json_file = os.path.join(data_dir, file_name)

        if not os.path.isfile(json_file):
            self.create_json_file(json_file)
            return json_file

        return json_file
    
    def create_json_file(self, file_path: str):
        default_dict = {
            'username': '',
            'password': '',
            'items': []
        }

        with open(file_path, 'w+', encoding="utf-8-sig") as new:
            json.dump(default_dict, new, indent=2)
        
        return file_path
    
    def save_todo_item(self, new_item: TodoItem) -> bool:
        if not new_item:
            return False
        
        file_path = self.build_path("user.json")

        with open(file_path, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            data["items"].append(new_item)

            with open(file_path, 'w+', encoding="utf-8-sig") as new:
                json.dump(data, new, indent=2)

        return True
    
    def get_todo_items(self) -> List:
        file_path = self.build_path("user.json")

        with open(file_path, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            return data["items"]
        
    def get_todo_item(self, item_id: int) -> TodoItem:
        file_path = self.build_path("user.json")

        with open(file_path, 'r', encoding="utf-8-sig")as f:
            data = json.load(f)

            todo_item = None

            for item in data["items"]:
                if item.get("item_id") == int(item_id):
                    todo_item = TodoItem(
                        item_id = item["item_id"],
                        title = item["title"],
                        details = item["details"],
                        priority = item["priority"],
                        created_at = item["created_at"],
                        is_completed = item["is_completed"]
                    )
                    
                    break
                
            return todo_item
        
    def update_item(self, updated_item: TodoItem) -> bool:
        file_path = self.build_path("user.json")

        with open(file_path, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            for index, item in enumerate(data["items"]):
                if item["item_id"] == updated_item.item_id:
                    data["items"][index]["title"] = updated_item.title
                    data["items"][index]["details"] = updated_item.details
                    data["items"][index]["priority"] = updated_item.priority
                    data["items"][index]["is_completed"] = updated_item.is_completed

                    with open(file_path, 'w+', encoding="utf-8-sig") as new:
                        json.dump(data, new, indent=2)

                    return True

    def update_items(self, new_items: List[TodoItem]) -> bool:
        file_path = self.build_path("user.json")

        with open(file_path, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            data["items"] = new_items

            with open(file_path, 'w+', encoding="utf-8-sig") as new:
                json.dump(data, new, indent=2)

        return True
