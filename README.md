# Customer Data Import & Validation Service

A synthetic customer import accepts CSV and JSON, checks types and duplicates, normalizes rows, and persists accepted records with rejection reports.

An Inkplain practical case: a real project built step by step.

## How this repository works

Every step of the lesson has its own branch, and each one contains all steps up to it:

```bash
git clone https://github.com/Inkplain-Practical-Cases/practical--customer-data-import-validation-service.git
cd practical--customer-data-import-validation-service
git branch -r            # list the step branches
git checkout step-01-…   # code after step 1
```

`main` holds the final, complete version.
