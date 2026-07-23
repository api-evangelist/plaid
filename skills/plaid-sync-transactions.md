---
name: Sync transactions incrementally with a cursor
description: Pull an Item's transactions incrementally using the /transactions/sync cursor pattern, persisting the cursor to resume.
api: openapi/plaid-transactions--openapi.yml
operations: [transactionsSync, transactionsGet]
---

# Sync transactions incrementally with a cursor

## Auth
`client_id` + `secret` in the body, `Plaid-Version: 2020-09-14` header, plus the Item's `access_token`.

## Steps (recommended: cursor sync)
1. **`transactionsSync`** (`POST /transactions/sync`) — first call omits `cursor` (or sends `null`). Read `added`, `modified`, `removed`, `next_cursor`, and `has_more`.
2. Persist `next_cursor`. While `has_more` is `true`, call `transactionsSync` again passing the last `next_cursor` until `has_more` is `false`.
3. On the next poll (or on a `SYNC_UPDATES_AVAILABLE` webhook), resume from the stored `next_cursor` — you only receive the delta.

## Alternative (date-range)
- **`transactionsGet`** (`POST /transactions/get`) — pass `start_date`/`end_date` and page with `options.offset`/`options.count`; read `total_transactions` to know when to stop.

## Rules
- Prefer `transactionsSync` over `transactionsGet` for freshness and dedupe correctness.
- A newly linked Item may return `PRODUCT_NOT_READY` until the initial pull completes — retry after the `INITIAL_UPDATE`/`HISTORICAL_UPDATE` webhook.
- See pagination + tracing details in `conventions/plaid-conventions.yml`.
