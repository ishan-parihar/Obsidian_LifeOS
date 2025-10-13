---
accountName: "Primary Checking"
accountType: checking
status: active
balance: 0
currency: USD
tags: [financial-account, money-flow]
---

# Financial Account - {{accountName}}

## 📊 Account Details
- **Account Name**: {{accountName}}
- **Account Type**: {{accountType}} (checking/savings/credit/investment)
- **Status**: {{status}}
- **Current Balance**: {{balance}} {{currency}}
- **Currency**: {{currency}}

## 💰 Transaction Log
```dataview
TABLE date, description, amount, category, balanceAfter
FROM "03 - The Workbench/Act III - The Ledger/Financial Transactions"
WHERE account = "{{accountName}}"
SORT date DESC
```

## 📈 Account Metrics
- **Monthly Average Balance**:
- **Transaction Frequency**:
- **Largest Transaction**:
- **Category Breakdown**:

## 🔗 Related Items
- **All Financial Transactions**: [[Financial Transactions Dashboard]]
- **Monthly Financial Reviews**: [[Month - Financial Review]]
- **Quarterly Financial Goals**: [[Quarterly Goal - Financial]]

## 📝 Notes
- Bank details, account numbers, important contacts
- Special considerations or restrictions
- Integration with other financial systems

> **Maintenance Tip**: Update balance after each transaction. Categorize all transactions for accurate financial insights.