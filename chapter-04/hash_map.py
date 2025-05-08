class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_func(self, key):
        if isinstance(key, str):
            return sum(ord(ch) for ch in key) % self.size
        elif isinstance(key, int):
            return key % self.size
        else:
            return hash(key) % self.size

    def put(self, key, value):
        index = self.hash_func(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        index = self.hash_func(key)
        bucket = self.buckets[index]

        for (k, v) in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self.hash_func(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

    def containsKey(self, key):
        return self.get(key) is not None


my_hash_map = HashMap()

my_hash_map.put("firstname", "karl")
my_hash_map.get("firstname")

my_hash_map.put("lastname", "karlsen")

my_hash_map.remove("firstname")


my_person = {
    "firstName": "Karl"
}
my_person["firstName"] = "Hannah"
print(my_person)
