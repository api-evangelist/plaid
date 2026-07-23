---
name: Authorize and create an ACH transfer idempotently
description: Risk-check and authorize a money movement, optionally score it with Signal, then create the transfer using an idempotency_key to prevent duplicates.
api: openapi/plaid-transfer--openapi.yml
operations: [transferAuthorizationCreate, transferCreate, transferGet, signalEvaluate]
---

# Authorize and create an ACH transfer idempotently

## Auth
`client_id` + `secret` in the body, `Plaid-Version: 2020-09-14`, and the Item `access_token` for the funding account.

## Steps
1. *(optional risk)* **`signalEvaluate`** (`POST /signal/evaluate`) — score ACH-return risk for the proposed debit; use the returned scores to decide guarantee/hold logic.
2. **`transferAuthorizationCreate`** (`POST /transfer/authorization/create`) — submit `access_token`, `account_id`, `type` (`debit`/`credit`), `network` (`ach`/`rtp`/`same-day-ach`), `amount`, and `user`. Returns an `authorization` with a `decision` (`approved`/`declined`) and a `decision_rationale`. Stop if declined.
3. **`transferCreate`** (`POST /transfer/create`) — pass the `authorization_id` from step 2, the `account_id`, `amount`, `description`, and an **`idempotency_key`**. Reusing the same `idempotency_key` with identical parameters returns the original transfer instead of creating a duplicate.
4. **`transferGet`** (`POST /transfer/get`) — poll or handle Transfer webhooks to track `status` (`pending` → `posted`/`settled` or `failed`/`returned`).

## Rules
- The `idempotency_key` is REQUIRED discipline for money movement — always generate one per logical transfer and retry with the SAME key. See `conventions/plaid-conventions.yml` (idempotency) and error_type `IDEMPOTENCY_ERROR`.
- Decline / return reasons: see `errors/plaid-decline-codes.yml`; API-level errors: `errors/plaid-problem-types.yml` (`TRANSFER_ERROR`).
