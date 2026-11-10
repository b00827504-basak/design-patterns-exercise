"""Builder pattern: create employees step by step."""
from dataclasses import dataclass


@dataclass
class Employee:
    first_name: str
    last_name: str
    email: str
    department: str
    position: str
    salary: float
    laptop: bool = False
    parking: bool = False
    vpn: bool = False
    admin: bool = False
    start_date: str = ""
    manager_id: int | None = None
    phone: str | None = None
    address: str | None = None
    emergency_contact: str | None = None
    office_location: str | None = None
    contract_type: str = "permanent"


class EmployeeBuilder:
    def __init__(self):
        self.info = {}
        self.equipment = {"laptop": False, "parking": False}
        self.access = {"vpn": False, "admin": False}

    def with_name(self, first_name, last_name):
        self.info.update(first_name=first_name, last_name=last_name)
        return self

    def with_email(self, email):
        self.info["email"] = email
        return self

    def with_job(self, department, position, salary):
        self.info.update(department=department, position=position, salary=salary)
        return self

    def with_equipment(self, laptop=False, parking=False):
        self.equipment = {"laptop": laptop, "parking": parking}
        return self

    def with_access(self, vpn=False, admin=False):
        self.access = {"vpn": vpn, "admin": admin}
        return self

    def with_start_date(self, date):
        self.info["start_date"] = date
        return self

    def with_manager(self, manager_id):
        self.info["manager_id"] = manager_id
        return self

    def with_contact(self, phone=None, address=None, emergency_contact=None):
        self.info.update(phone=phone, address=address, emergency_contact=emergency_contact)
        return self

    def with_office(self, location, contract_type="permanent"):
        self.info.update(office_location=location, contract_type=contract_type)
        return self

    def build(self):
        required = ["first_name", "last_name", "email", "department", "position", "salary"]
        if any(not self.info.get(name) and self.info.get(name) != 0 for name in required):
            raise ValueError("Missing required employee information")
        if "@" not in self.info["email"] or self.info["salary"] < 0:
            raise ValueError("Invalid email or salary")
        return Employee(**self.info, **self.equipment, **self.access)


class DeveloperBuilder(EmployeeBuilder):
    def __init__(self, first_name, last_name, email):
        super().__init__()
        self.with_name(first_name, last_name).with_email(email)
        self.with_job("Engineering", "Developer", 75000)
        self.with_office("Paris HQ")
        self.with_equipment(laptop=True).with_access(vpn=True, admin=True)


if __name__ == "__main__":
    employee = (EmployeeBuilder().with_name("Jane", "Smith")
                .with_email("jane@example.com").with_job("Marketing", "Intern", 15000)
                .with_equipment(laptop=True).with_start_date("2026-11-10")
                .with_office("Paris HQ", contract_type="internship").build())
    print(employee)
    print(DeveloperBuilder("John", "Doe", "john@example.com").build())
