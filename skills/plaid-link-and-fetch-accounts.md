---
name: Link a bank account and fetch accounts + balances
description: Initialize Plaid Link, exchange the public_token for an access_token, then read the connected accounts, balances, and ACH numbers.
api: openapi/plaid-link--openapi.yml
operations: [linkTokenCreate, itemPublicTokenExchange, accountsGet, accountsBalanceGet, authGet]
---

# Link a bank account and fetch accounts + balances

## Auth
Every request sends `client_id` and `secret` in the JSON body and a `Plaid-Version: 2020-09-14` header. Start in `sandbox.plaid.com`, then move to `production.plaid.com`. See `authentication/plaid-authentication.yml`.

## Steps
1. **`linkTokenCreate`** (`POST /link/token/create`) — pass `user.client_user_id`, `products` (e.g. `["auth"]`), `country_codes`, `language`, and a `webhook` URL. Returns a short-lived `link_token`.
2. Hand the `link_token` to the Plaid Link front-end SDK (see `packages/`). After the user authenticates with their bank, Link returns a `public_token`.
3. **`itemPublicTokenExchange`** (`POST /item/public_token/exchange`) — exchange the `public_token` for a durable `access_token` + `item_id`. Persist the `access_token` securely; it does not expire.
4. **`accountsGet`** (`POST /accounts/get`) — with the `access_token`, list the Item's `accounts` (ids, names, types, subtypes, masks).
5. **`accountsBalanceGet`** (`POST /accounts/balance/get`) — force a real-time balance refresh when you need current `available`/`current` balances.
6. **`authGet`** (`POST /auth/get`) — retrieve ACH `account` + `routing` numbers for payment setup.

## Rules
- Handle `ITEM_LOGIN_REQUIRED` (error_type `ITEM_ERROR`) by re-launching Link in **update mode** with a new `link_token` for the existing Item.
- Respect the default 100 req/day/Item rate limit; back off on `RATE_LIMIT_EXCEEDED`.
- Errors follow the Plaid envelope (`error_type`/`error_code`/`request_id`) — see `errors/plaid-problem-types.yml`.
