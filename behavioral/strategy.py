"""Strategy pattern: choose a report format at runtime."""
from abc import ABC, abstractmethod
import json
from pathlib import Path


class FormatStrategy(ABC):
    extension = ".txt"

    @abstractmethod
    def format(self, data):
        pass


class PDFFormatStrategy(FormatStrategy):
    # This is a text preview, not a real PDF file.
    def format(self, data):
        lines = ["PDF REPORT (text preview)", "=" * 30]
        lines += [f"{item['name']}: {item['value']}" for item in data]
        return "\n".join(lines)


class ExcelFormatStrategy(FormatStrategy):
    # This is a text preview, not a real Excel spreadsheet.
    def format(self, data):
        return "EXCEL REPORT (text preview)\nName\tValue\n" + "\n".join(
            f"{item['name']}\t{item['value']}" for item in data)


class CSVFormatStrategy(FormatStrategy):
    extension = ".csv"

    def format(self, data):
        return "name,value\n" + "\n".join(f"{item['name']},{item['value']}" for item in data)


class JSONFormatStrategy(FormatStrategy):
    extension = ".json"

    def format(self, data):
        return json.dumps(data, indent=2)


class HTMLFormatStrategy(FormatStrategy):
    extension = ".html"

    def format(self, data):
        lines = ["<table>", "<tr><th>Name</th><th>Value</th></tr>"]
        lines += [f"<tr><td>{item['name']}</td><td>{item['value']}</td></tr>" for item in data]
        return "\n".join(lines + ["</table>"])


class ReportGenerator:
    def __init__(self, data):
        self.data = data
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def generate_report(self):
        if self.strategy is None:
            raise ValueError("Choose a strategy first")
        return self.strategy.format(self.data)

    def save_report(self, filename):
        # Use a real extension only for the real CSV, JSON, and HTML outputs.
        path = Path(filename + self.strategy.extension)
        path.write_text(self.generate_report(), encoding="utf-8")
        return path


if __name__ == "__main__":
    data = [{"name": "Sales Q1", "value": 15000}, {"name": "Sales Q2", "value": 18000}]
    report = ReportGenerator(data)
    for strategy in [PDFFormatStrategy(), ExcelFormatStrategy(), CSVFormatStrategy(), JSONFormatStrategy(), HTMLFormatStrategy()]:
        report.set_strategy(strategy)
        print("\n", report.generate_report())
