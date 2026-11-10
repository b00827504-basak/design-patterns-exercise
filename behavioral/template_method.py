"""Template Method pattern: the same steps for different ETL pipelines."""
from abc import ABC, abstractmethod


class DataPipeline(ABC):
    def __init__(self, source):
        self.source = source
        self.data = []

    def run(self):
        print("Connecting to:", self.source)
        self.connect()
        try:
            self.data = self.extract()
            self.transform()
            self.validate()
            self.after_validation()
            self.load()
        finally:
            self.cleanup()
        return self.__class__.__name__ + " finished"

    def connect(self):
        print("Connected")

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    def validate(self):
        if not self.data:
            raise ValueError("No data")
        print("Validation passed")

    def after_validation(self):
        """Optional hook: subclasses may add a step here."""
        pass

    def load(self):
        print("Loaded", len(self.data), "records")

    def cleanup(self):
        self.data = []
        print("Cleanup complete")


class CSVPipeline(DataPipeline):
    def extract(self):
        return [{"id": 1, "name": "Alice", "age": "30"}]

    def transform(self):
        for row in self.data:
            row["age"] = int(row["age"])
            row["name"] = row["name"].upper()


class APIPipeline(DataPipeline):
    def after_validation(self):
        print("API data is ready to load")

    def extract(self):
        return [{"user_id": 101, "username": "CHARLIE", "score": "85"}]

    def transform(self):
        for row in self.data:
            row["score"] = int(row["score"])
            row["username"] = row["username"].lower()
            row["grade"] = "A" if row["score"] >= 90 else "B"


class DatabasePipeline(DataPipeline):
    def extract(self):
        return [{"product_id": 501, "product_name": "laptop", "price": "1200"}]

    def transform(self):
        for row in self.data:
            row["price"] = float(row["price"])
            row["product_name"] = row["product_name"].title()
            row["tax"] = row["price"] * 0.20


class XMLPipeline(DataPipeline):
    def extract(self):
        # Small example: no external XML file is needed.
        return [{"order_id": "12", "total": "50.0"}]

    def transform(self):
        for row in self.data:
            row["order_id"] = int(row["order_id"])
            row["total"] = float(row["total"])


if __name__ == "__main__":
    for pipeline in [CSVPipeline("users.csv"), APIPipeline("example API"),
                     DatabasePipeline("example database"), XMLPipeline("orders.xml")]:
        print(pipeline.run())
        print()
