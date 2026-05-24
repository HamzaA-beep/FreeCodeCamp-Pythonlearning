class HashTable:
    def __init__(self):
        self.collection = {}
    def hash(self, key_string):
        new_hash = 0
        for letter in key_string:
            new_hash += int(ord(letter))
        return new_hash
    def add(self, key, value):
        key_hash = self.hash(key)
        if key_hash in self.collection.keys():
            self.collection[key_hash].update({key : value})
        else:
            self.collection[key_hash] = {key: value}

    def remove(self, key):
        key_hash = self.hash(key)

        if key_hash in self.collection:
            bucket = self.collection[key_hash]
            if key in bucket:
                del bucket[key]
                if len(bucket) == 0:
                    del self.collection[key_hash]
        return

    def lookup(self, key):
        key_hash = self.hash(key)
        if key_hash in self.collection.keys() and list(self.collection[key_hash].keys())[0] == key:
            return self.collection[key_hash][key]
        else:
            return None