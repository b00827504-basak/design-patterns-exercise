# Notes about the original code

## Strategy: report formats

- A long `if/elif` block handles every format.
- Adding HTML means changing the old method.
- The same class handles formatting and saving.
- It is hard to test one format on its own.
- Changing format at runtime is not very clear.

**Solution:** Each format has its own class. `ReportGenerator` can switch strategies when needed. The new HTML class is added without changing the other format classes.

## Template Method: ETL pipelines

- Validation is repeated in three pipelines.
- Cleanup is repeated in three pipelines.
- The workflow steps are repeated in each `run()` method.
- Adding logging would mean editing several classes.
- Different classes might run the steps in a different order.

**Solution:** `DataPipeline.run()` sets the order of the steps once. Each subclass only writes its own extraction and transformation. `XMLPipeline` is a new example using the same workflow.

## Other patterns

- **Factory:** Different payment methods use separate processor classes.
- **Builder:** Employee data is added step by step instead of passing many arguments.
- **Singleton:** Configuration is loaded only once.
- **Adapter:** The legacy report stays unchanged. An adapter converts its XML output to JSON.
- **Decorator:** Order options are small classes that wrap one another. The order of the decorators decides the order of the price changes.
