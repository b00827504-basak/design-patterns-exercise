# Design Patterns Exercise

This project is my Python design patterns exercise for the OOP course.

I first planned the class diagrams and then wrote simple Python examples. The goal is to make the code easier to read and change.

## Exercises

### 1. Creational patterns

- **Factory:** A payment system with credit card, bank transfer and PayPal.
- **Builder:** An employee onboarding system with small builder methods.
- **Singleton:** One configuration manager shared by the application.

### 2. Structural patterns

- **Adapter:** Change a legacy XML report into JSON for a new dashboard.
- **Decorator:** Add shipping, insurance, gift wrap and discounts to an order.

### 3. Behavioral patterns

- **Strategy:** Choose PDF, Excel, CSV, JSON or HTML report formats.
- **Template Method:** Use the same ETL workflow for CSV, API, database and XML data.

**Note:** The PDF and Excel format examples print text previews. They do not create real PDF or Excel files. The ETL examples use sample data instead of connecting to live services.

## Files

- `creational/`: Factory, Builder and Singleton examples.
- `structural/`: Adapter and Decorator examples.
- `behavioral/`: Strategy and Template Method examples.
- `DIAGRAMS.md`: UML class diagrams for the patterns.
- `NOTES.md`: Problems in the old code and short explanations.

## How to run

You need Python 3. No extra packages are needed.

```bash
python3 creational/factory.py
python3 creational/builder.py
python3 creational/singleton.py
python3 structural/adapter.py
python3 structural/decorator.py
python3 behavioral/strategy.py
python3 behavioral/template_method.py
```

The scripts print small examples so it is easy to see how each pattern works.
