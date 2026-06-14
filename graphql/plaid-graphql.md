# Plaid GraphQL

## Overview

**Provider:** Plaid  
**Type:** Conceptual GraphQL data model (no native public GraphQL endpoint)  
**Docs:** https://plaid.com/docs/api/  
**GitHub:** https://github.com/plaid

## Native GraphQL

Plaid does not offer a native public GraphQL API. All Plaid APIs are REST-based, accessed via POST requests to `https://production.plaid.com` with JSON request/response bodies and `client_id` / `secret` authentication headers.

## Conceptual Schema

The file `plaid-schema.graphql` provides a comprehensive GraphQL SDL schema derived from Plaid's REST API types. It covers the full breadth of Plaid's data model across its product surface:

- **Items and Accounts** — linked financial institution connections, account metadata and balances
- **Transactions** — individual and recurring transaction streams with enrichment and categorization
- **Identity** — KYC data including addresses, emails, and phone numbers
- **Income** — payroll income, bank income, and income verification
- **Assets** — asset reports for lending and credit underwriting
- **Investments** — holdings, securities, and investment transactions
- **Liabilities** — mortgage and student loan details
- **Transfers** — ACH transfer objects, authorizations, and ledger entries
- **Link** — Link token lifecycle and OAuth state
- **Institutions** — institution search and credential metadata
- **Watchlist Screening** — individual and entity AML/sanctions screening
- **Beacon** — fraud network user and account risk
- **Signal** — ACH risk scoring
- **Errors** — structured error envelope

## Usage

This schema is intended for tooling, catalog enrichment, documentation generation, and data-model mapping. It accurately reflects the types, relationships, and field-level semantics described in Plaid's official REST API documentation.
