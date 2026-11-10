# UML Class Diagrams

These UML diagrams describe the main classes before the Python implementation.

## Factory Pattern

```mermaid
classDiagram
    class PaymentProcessor {
        <<abstract>>
        +validate(details)
        +process(amount, details)
    }
    class CreditCardProcessor
    class BankTransferProcessor
    class PayPalProcessor
    class PaymentFactory {
        +get_processor(payment_type)
    }
    PaymentProcessor <|-- CreditCardProcessor
    PaymentProcessor <|-- BankTransferProcessor
    PaymentProcessor <|-- PayPalProcessor
    PaymentFactory ..> PaymentProcessor : creates
```

## Builder Pattern

```mermaid
classDiagram
    class Employee {
        +first_name
        +last_name
        +email
        +department
        +position
        +salary
    }
    class EmployeeBuilder {
        +with_name(first_name, last_name)
        +with_email(email)
        +with_job(department, position, salary)
        +with_equipment(laptop, parking)
        +with_access(vpn, admin)
        +build() Employee
    }
    class DeveloperBuilder
    EmployeeBuilder <|-- DeveloperBuilder
    EmployeeBuilder ..> Employee : builds
```

## Singleton Pattern

```mermaid
classDiagram
    class ConfigManager {
        -_instance
        -config
        +get_instance() ConfigManager
        +get(key)
    }
```

## Adapter Pattern

```mermaid
classDiagram
    class ReportGeneratorInterface {
        <<abstract>>
        +generate(data) str
    }
    class LegacyReportGenerator {
        +generate_report(data) str
    }
    class LegacyReportAdapter {
        -legacy
        +generate(data) str
    }
    class AnalyticsDashboard {
        +display(json_data)
    }
    ReportGeneratorInterface <|-- LegacyReportAdapter
    LegacyReportAdapter --> LegacyReportGenerator : wraps
    AnalyticsDashboard ..> ReportGeneratorInterface : receives JSON from
```

## Decorator Pattern

```mermaid
classDiagram
    class OrderComponent {
        <<abstract>>
        +get_cost() float
        +get_description() str
    }
    class BaseOrder
    class OrderDecorator {
        -order
    }
    class ExpressShippingDecorator
    class InsuranceDecorator
    class GiftWrapDecorator
    class DiscountDecorator
    class PremiumMemberDecorator
    OrderComponent <|-- BaseOrder
    OrderComponent <|-- OrderDecorator
    OrderDecorator --> OrderComponent : wraps
    OrderDecorator <|-- ExpressShippingDecorator
    OrderDecorator <|-- InsuranceDecorator
    OrderDecorator <|-- GiftWrapDecorator
    OrderDecorator <|-- DiscountDecorator
    OrderDecorator <|-- PremiumMemberDecorator
```

## Strategy Pattern

```mermaid
classDiagram
    class FormatStrategy {
        <<abstract>>
        +format(data) str
    }
    class ReportGenerator {
        -data
        -strategy
        +set_strategy(strategy)
        +generate_report() str
        +save_report(filename)
    }
    class PDFFormatStrategy
    class ExcelFormatStrategy
    class CSVFormatStrategy
    class JSONFormatStrategy
    class HTMLFormatStrategy
    ReportGenerator --> FormatStrategy : uses
    FormatStrategy <|-- PDFFormatStrategy
    FormatStrategy <|-- ExcelFormatStrategy
    FormatStrategy <|-- CSVFormatStrategy
    FormatStrategy <|-- JSONFormatStrategy
    FormatStrategy <|-- HTMLFormatStrategy
```

## Template Method Pattern

```mermaid
classDiagram
    class DataPipeline {
        <<abstract>>
        +run()
        +connect()
        +extract()*
        +transform()*
        +validate()
        +load()
        +cleanup()
    }
    class CSVPipeline
    class APIPipeline
    class DatabasePipeline
    class XMLPipeline
    DataPipeline <|-- CSVPipeline
    DataPipeline <|-- APIPipeline
    DataPipeline <|-- DatabasePipeline
    DataPipeline <|-- XMLPipeline
```
