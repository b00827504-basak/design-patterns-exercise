"""Adapter pattern: convert the old XML report into JSON."""
from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET


# External legacy class: kept unchanged.
class LegacyReportGenerator:
    def generate_report(self, data: dict) -> str:
        xml = "<report>\n"
        for key, value in data.items():
            xml += f"  <{key}>{value}</{key}>\n"
        xml += "</report>"
        return xml


class AnalyticsDashboard:
    def display(self, json_data: str):
        data = json.loads(json_data)
        print("=== Analytics Dashboard ===")
        for key, value in data.items():
            print(f"  {key}: {value}")


class ReportGeneratorInterface(ABC):
    @abstractmethod
    def generate(self, data) -> str:
        pass


class LegacyReportAdapter(ReportGeneratorInterface):
    def __init__(self, legacy):
        self.legacy = legacy

    def generate(self, data) -> str:
        xml_report = self.legacy.generate_report(data)
        root = ET.fromstring(xml_report)
        result = {}
        for item in root:
            # Restore the simple numeric data used in these reports.
            text = item.text or ""
            try:
                value = float(text) if "." in text else int(text)
            except ValueError:
                value = text
            result[item.tag] = value
        return json.dumps(result)


if __name__ == "__main__":
    generator = LegacyReportAdapter(LegacyReportGenerator())
    dashboard = AnalyticsDashboard()
    dashboard.display(generator.generate({"total_sales": 150000, "orders": 1234}))
    dashboard.display(generator.generate({"total_items": 5000, "low_stock": 45}))
