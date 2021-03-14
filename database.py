#!/usr/bin/python3
# All Database connectors are here. Just call and run.
import pymongo
from datetime import datetime
import bcrypt
import json

class Connection:
    """A connection to the database."""

    def __init__(self, app, host="0.0.0.0", port=27017):
        self.app = app
        self.client = pymongo.MongoClient(host, port)
        self.db = self.client['dash-app']
        self.speed_dial = self.db['speed_dial']

    # Message functions
    def get_sites(self, max=25):
        """Retrieves the sites from a chatroom."""
        results = self.speed_dial.find({}, limit=max)  # Get the sites
        # Sort by date in ascending order by Title
        results = results.sort('title', pymongo.ASCENDING)
        return list(results)
        
    def add_message(self, groups, title, bg_color, url, img):
        """Adds a message to the database."""
        if self.speed_dial.count_documents({'url': url}) == 0:
            message = {
                'url': url,
                'title': title,
                'bg-color': bg_color,
                'groups': groups,
                'img': img
            }
            self.speed_dial.insert_one(message)
            return True  # Insertion was successful
        else:
            self.app.logger.warning(
                'Bookmark Already Exist: %s', url)
            return False  # Insertion was unsuccessful

    def load_json_to_db(self, json_path):
        # Loading or Opening the json file
        with open(json_path) as file:
            file_data = json.load(file)
        # if JSON contains data more than one entry
        # insert_many is used else inser_one is used
        if isinstance(file_data, list):
            self.speed_dial.insert_many(file_data)
        else:
            self.speed_dial.insert_one(file_data)
