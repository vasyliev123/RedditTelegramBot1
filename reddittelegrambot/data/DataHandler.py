import json

class DataHandler:
    def __init__(self, filename):
        self.filename = filename
    
    def read_dict(self):
        with open(self.filename, 'r') as f:
            data = json.load(f)
        return data
    
    def add_dict(self, new_dict):
        with open(self.filename, 'r+') as f:
            data = json.load(f)
            if data is None:
                data = {}
            data.update(new_dict)
            f.seek(0)
            json.dump(data, f, indent=4)
            
    def add_subreddits(self, user_id, subreddits):
        with open(self.filename, 'r+') as f:
            data = json.load(f)
            if data is None:
                data = {}
            data[user_id]["subreddits"] = subreddits
            f.seek(0)
            json.dump(data, f, indent=4)

    def  get_imported_by_user_id(self, user_id):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            return data[user_id]["imported_posts"]
