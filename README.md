# Plaid

<!-- API-EVANGELIST-PROVENANCE:BEGIN -->
> ### About this repository
>
> **This is not our API.** This repository is an independent, third-party profile of a company's
> **publicly available** API surface, maintained by [API Evangelist](https://apievangelist.com).
> API Evangelist does not operate, host, resell, or support this company's APIs, and is not
> affiliated with or endorsed by the company unless stated on the profile.
>
> **Where the information came from.** Everything here is assembled from material a member of the
> public can reach with a browser and no credentials — the company's own website, developer portal
> and documentation, the specifications it publishes for public use (OpenAPI, AsyncAPI, JSON Schema,
> `apis.json`, `llms.txt` and similar), its public repositories, and its public status, pricing and
> changelog pages. **Nothing here is obtained by breaching a system, defeating an access control, or
> using credentials of any kind.**
>
> **The rating is an independent assessment.** The Kin Score and Agent Readiness rating are
> independently calculated scores of a company's *public* API artifacts, produced by API Evangelist
> against a published rubric. They are not certifications, endorsements, security assessments, or
> audits, and they score published artifacts — not the quality, safety, or security of the software.
>
> **Corrections, re-scores, and removal are free.** No partnership, contract, or purchase is
> required, and you do not need to justify the request.
>
> - **Something wrong?** Open an issue on this repository, or email
>   [info@apievangelist.com](mailto:info@apievangelist.com).
> - **Published something new?** Ask for a re-score and we will re-run the rating.
> - **Want the listing taken down?** Say so and we will honor it. The profile is reduced to your
>   company name, a factual description, and a link to your own site, and the company is recorded as
>   **unrated** — never scored zero for having asked.
>
> **Response times.** Acknowledgement within **one business day**; removal or restriction within
> **two business days**; corrections and re-scores within **five business days**.
>
> **Not from the company, and here with a question?** You are welcome here — we would rather be the
> front line and point you the right way than have a good report go nowhere. What this repository
> can answer is narrow, though, so it is worth knowing who you are actually looking for:
>
> - **A question about how the API works, an account, billing, or a bug in the service** — that is
>   the company's own support, not us. We profile this API; we do not operate it and cannot see
>   your account.
> - **A bug in an open-source project we only catalog** — file it on that project's own repository.
>   This has happened with a real and correct bug report that reached us instead of the people who
>   could fix it, which helped nobody.
> - **Anything about this listing itself** — the description, the tags, the rating, a missing or
>   wrong artifact — is ours. Open an issue here.
> - **Not sure, or something general about API Evangelist or APIs.io** — open an issue on the
>   [APIs.io Inbox](https://github.com/api-search/inbox) and we will route it.
>
> **This repository contains no software, and we will never ask you to download anything.** There is
> no build, release, installer, or binary here — only text and machine-readable API descriptions, so
> there is nothing here that can be "corrupt" or need "repairing". Any issue, comment, or email
> claiming otherwise and offering a download link is not from us and is hostile. Do not follow the
> link; it is a lure. Report it to GitHub and, if you like, tell us at
> [info@apievangelist.com](mailto:info@apievangelist.com) so we can take it down.
>
> **On a security or compliance team?** Email
> [info@apievangelist.com](mailto:info@apievangelist.com) with *security* in the subject line and
> you will get a person, not a form. We will tell you exactly which public URLs this profile was
> built from so your team can see the same surface we did, and we will take the listing down on
> request while you work through it.
>
> Full detail: **[Where this data comes from](https://apievangelist.com/about/where-our-data-comes-from)**
<!-- API-EVANGELIST-PROVENANCE:END -->

Plaid is a US financial-technology company and data-network aggregator that provides an API platform for businesses to securely connect with their users' bank and financial accounts. Plaid acts as the interface between 12,000+ financial institutions and third-party applications, powering bank-account verification (Auth, Balance, Identity), transactions and enrichment, income and asset verification, lending data (Assets, Liabilities, Investments, Consumer Report/CRA), risk and fraud tooling (Signal, Beacon, Monitor watchlist screening, Identity Verification), and money movement (Transfer, Payment Initiation, Virtual Accounts). Developers integrate through Plaid Link, a self-serve dashboard, client credentials, per-Item access tokens, and a publicly published OpenAPI definition. In the US voluntary open-finance landscape Plaid is an aggregator, and it also operates Core Exchange, its FDX-aligned data-access API for data providers, positioning it for CFPB 1033 open-banking rules.

**Areas:** Finance · Fintech · Open Banking · Bank Accounts · Data Aggregation · Payments · United States

## Plaid on APIs.io

Everything profiled for Plaid is published on APIs.io rather than in this repository. Start at the provider page — **[apis.io/providers/plaid/](https://apis.io/providers/plaid/)** — or go straight to one of the APIs or properties below.

### APIs (7)

- [Plaid API](https://apis.io/apis/plaid/plaid-plaid-api/) — The Plaid REST API — the aggregator surface for bank-account, identity, transactions, income, assets, liabilities, investments, transfer, payment…
- [Plaid Account Information API](https://apis.io/apis/plaid/plaid-account-information-api/) — Search and view customer accounts
- [Plaid Account Statements API](https://apis.io/apis/plaid/plaid-account-statements-api/) — Search and retrieve account statements
- [Plaid Account Transactions API](https://apis.io/apis/plaid/plaid-account-transactions-api/) — Search and view account transactions
- [Plaid Asset Transfer Networks Information API](https://apis.io/apis/plaid/plaid-asset-transfer-networks-information-api/) — Search and view asset transfer networks
- [Plaid Payment Networks Information API](https://apis.io/apis/plaid/plaid-payment-networks-information-api/) — Search and view account payment networks
- [Plaid Personal Information API](https://apis.io/apis/plaid/plaid-personal-information-api/) — Search and view customer or customers

### Published properties

Each property below is a page on APIs.io carrying the machine-readable artifact and what it says.

#### AsyncAPI (2)

Event-driven and webhook contracts.

- [Plaid Webhooks](https://apis.io/asyncapis/plaid/plaid-webhooks/)
- [Plaid Webhooks](https://apis.io/asyncapis/plaid/plaid-webhooks--asyncapi-original/)

#### Event channels (52)

Individual events and webhooks the provider emits.

- [assets/error](https://apis.io/channels/plaid/assets-error/)
- [assets/productReady](https://apis.io/channels/plaid/assets-productready/)
- [auth/automaticallyVerified](https://apis.io/channels/plaid/auth-automaticallyverified/)
- [auth/bankTransfersEventsUpdate](https://apis.io/channels/plaid/auth-banktransferseventsupdate/)
- [auth/defaultUpdate](https://apis.io/channels/plaid/auth-defaultupdate/)
- [auth/productPermissionsRequired](https://apis.io/channels/plaid/auth-productpermissionsrequired/)
- [auth/smsMicrodepositsVerification](https://apis.io/channels/plaid/auth-smsmicrodepositsverification/)
- [auth/verificationExpired](https://apis.io/channels/plaid/auth-verificationexpired/)
- [beacon/duplicateDetected](https://apis.io/channels/plaid/beacon-duplicatedetected/)
- [beacon/reportCreated](https://apis.io/channels/plaid/beacon-reportcreated/)
- [beacon/reportSyndicationCreated](https://apis.io/channels/plaid/beacon-reportsyndicationcreated/)
- [beacon/reportUpdated](https://apis.io/channels/plaid/beacon-reportupdated/)
- [beacon/userStatusUpdated](https://apis.io/channels/plaid/beacon-userstatusupdated/)
- [entityScreening/statusUpdated](https://apis.io/channels/plaid/entityscreening-statusupdated/)
- [holdings/defaultUpdate](https://apis.io/channels/plaid/holdings-defaultupdate/)
- [identity/defaultUpdate](https://apis.io/channels/plaid/identity-defaultupdate/)
- [identity/productPermissionsRequired](https://apis.io/channels/plaid/identity-productpermissionsrequired/)
- [identityVerification/retried](https://apis.io/channels/plaid/identityverification-retried/)
- [identityVerification/statusUpdated](https://apis.io/channels/plaid/identityverification-statusupdated/)
- [identityVerification/stepUpdated](https://apis.io/channels/plaid/identityverification-stepupdated/)
- [income/bankIncomeComplete](https://apis.io/channels/plaid/income-bankincomecomplete/)
- [income/bankIncomeRefreshComplete](https://apis.io/channels/plaid/income-bankincomerefreshcomplete/)
- [income/bankIncomeRefreshUpdate](https://apis.io/channels/plaid/income-bankincomerefreshupdate/)
- [income/incomeVerification](https://apis.io/channels/plaid/income-incomeverification/)
- [income/incomeVerificationRefreshReconnectNeeded](https://apis.io/channels/plaid/income-incomeverificationrefreshreconnectneeded/)
- …and 27 more published on APIs.io

#### GraphQL (1)

GraphQL schemas.

- [Moved to /providers/plaid/](https://apis.io/graphqls/plaid/plaid-graphql/)

#### MCP servers (1)

Model Context Protocol servers that expose the API to agents.

- [plaid-mcp.yml](https://apis.io/servers/plaid/plaid-mcp-yml/)

#### Agentic access (1)

Which operations an agent can call, which act, and which need a human in the loop.

- [Plaid Agentic Access](https://apis.io/agentic-access/plaid/plaid-agentic-access/)

#### JSON Schema (14)

The data models the API reads and writes.

- [Account Contact entity](https://apis.io/schemas/plaid/plaid-account-contact/)
- [Payment Networks entity](https://apis.io/schemas/plaid/plaid-account-payment-network-list/)
- [Account With Details entity](https://apis.io/schemas/plaid/plaid-account-with-details/)
- [Accounts entity](https://apis.io/schemas/plaid/plaid-accounts/)
- [BetaPartnerCustomerV1CreateRequest](https://apis.io/schemas/plaid/plaid-beta-partner-customer-v1-create-request/)
- [Customer entity](https://apis.io/schemas/plaid/plaid-customer/)
- [Moved to /providers/plaid/](https://apis.io/schemas/plaid/plaid-deposit-switch-get-response/)
- [Moved to /providers/plaid/](https://apis.io/schemas/plaid/plaid-link-token-create-request/)
- [Moved to /providers/plaid/](https://apis.io/schemas/plaid/plaid-partner-customer-create-request/)
- [ProcessorSignalEvaluateRequest](https://apis.io/schemas/plaid/plaid-processor-signal-evaluate-request/)
- [Moved to /providers/plaid/](https://apis.io/schemas/plaid/plaid-signal-evaluate-request/)
- [Transactions entity](https://apis.io/schemas/plaid/plaid-transactions/)
- [Moved to /providers/plaid/](https://apis.io/schemas/plaid/plaid-transfer-authorization-create-request/)
- [Moved to /providers/plaid/](https://apis.io/schemas/plaid/plaid-transfer-create-request/)

#### JSON-LD (1)

Linked-data contexts for the provider's vocabulary.

- [Moved to /providers/plaid/](https://apis.io/jsonld/plaid/plaid-context/)

#### Collections (62)

Postman and Open Collection request collections.

- [Plaid accounts/](https://apis.io/collections/plaid/open-plaid-accounts-/)
- [Plaid asset report/](https://apis.io/collections/plaid/open-plaid-asset-report-/)
- [Plaid auth/](https://apis.io/collections/plaid/open-plaid-auth-/)
- [Plaid bank transfer/](https://apis.io/collections/plaid/open-plaid-bank-transfer-/)
- [Plaid beacon/](https://apis.io/collections/plaid/open-plaid-beacon-/)
- [Plaid categories/](https://apis.io/collections/plaid/open-plaid-categories-/)
- [Plaid cra/](https://apis.io/collections/plaid/open-plaid-cra-/)
- [Plaid credit/](https://apis.io/collections/plaid/open-plaid-credit-/)
- [Plaid deposit switch/](https://apis.io/collections/plaid/open-plaid-deposit-switch-/)
- [Plaid employers/](https://apis.io/collections/plaid/open-plaid-employers-/)
- [Plaid fdx/](https://apis.io/collections/plaid/open-plaid-fdx-/)
- [Plaid identity/](https://apis.io/collections/plaid/open-plaid-identity-/)
- [Plaid identity verification/](https://apis.io/collections/plaid/open-plaid-identity-verification-/)
- [Plaid income/](https://apis.io/collections/plaid/open-plaid-income-/)
- [Plaid institutions/](https://apis.io/collections/plaid/open-plaid-institutions-/)
- [Plaid investments/](https://apis.io/collections/plaid/open-plaid-investments-/)
- [Plaid item/](https://apis.io/collections/plaid/open-plaid-item-/)
- [Plaid liabilities/](https://apis.io/collections/plaid/open-plaid-liabilities-/)
- [Plaid link/](https://apis.io/collections/plaid/open-plaid-link-/)
- [Plaid link delivery/](https://apis.io/collections/plaid/open-plaid-link-delivery-/)
- [Plaid partner/](https://apis.io/collections/plaid/open-plaid-partner-/)
- [Plaid payment initiation/](https://apis.io/collections/plaid/open-plaid-payment-initiation-/)
- [Plaid payment profile/](https://apis.io/collections/plaid/open-plaid-payment-profile-/)
- [Plaid processor/](https://apis.io/collections/plaid/open-plaid-processor-/)
- [Plaid sandbox/](https://apis.io/collections/plaid/open-plaid-sandbox-/)
- …and 37 more published on APIs.io

#### Overlays (4)

OpenAPI overlays, including conversational phrasing for each operation.

- [Plaid Core Exchange Overlay](https://apis.io/overlays/plaid/plaid-core-exchange-overlay/)
- [Plaid Plaid Api Overlay](https://apis.io/overlays/plaid/plaid-plaid-api-overlay/)
- [Plaid Plaid Api Phrasing Overlay](https://apis.io/overlays/plaid/plaid-plaid-api-phrasing-overlay/)
- [Plaid Transfer Overlay](https://apis.io/overlays/plaid/plaid-transfer-overlay/)

#### Governance rules (3)

Spectral rulesets for the provider's contracts.

- [Plaid — asyncapi rules](https://apis.io/rules/plaid/plaid-asyncapi-spectral-rules/)
- [Moved to /providers/plaid/](https://apis.io/rules/plaid/plaid-rules/)
- [Plaid API Rules](https://apis.io/rules/plaid/plaid-spectral-rules/)

#### Security (4)

Authentication, trust centre, and vulnerability disclosure.

- [Plaid Authentication](https://apis.io/security/plaid/plaid-authentication/)
- [Plaid Domain Security](https://apis.io/security/plaid/plaid-domain-security/)
- [Plaid Trust Center](https://apis.io/security/plaid/plaid-trust-center/)
- [Moved to /providers/plaid/](https://apis.io/security/plaid/plaid-vulnerability-disclosure/)

#### OAuth scopes (1)

The permissions the API asks for.

- [Plaid Scopes](https://apis.io/scopes/plaid/plaid-scopes/)

#### Plans and pricing (1)

Published plans, tiers and prices.

- [Plaid Plans Pricing](https://apis.io/plans/plaid/plaid-plans-pricing/)

#### Rate limits (1)

Published request limits.

- [Plaid Rate Limits](https://apis.io/rate-limits/plaid/plaid-rate-limits/)

#### FinOps (1)

What the API costs to run, by operation.

- [Plaid Finops](https://apis.io/finops/plaid/plaid-finops/)

## Where to find this API

Links to the company's own pages. This repository publishes no copy of their specifications — the canonical document is theirs and lives at the URLs below.

- [Website](https://plaid.com/)
- [Documentation](https://plaid.com/docs/api/)
- [Getting started](https://plaid.com/docs/payment-initiation/payment-initiation-one-time/user-onboarding-and-account-funding/index.html)
- [API reference](https://plaid.com/docs/api/)
- [Pricing](https://plaid.com/pricing/)
- [Sign up](https://dashboard.plaid.com/signup)
- [Support](https://plaid.com/docs/support/)
- [Blog](https://plaid.com/blog/)
- [Security](https://plaid.com/careers/openings/security/security-engineer-grc/)
- [Terms of service](https://plaid.com/legal/)
- [Privacy policy](https://plaid.com/legal/#privacy-policy)
- [GitHub](https://github.com/plaid)
- [Status](https://status.plaid.com/)

## API Evangelist rating

**Kin Score 84.6** — exemplar · rubric 0.25.0 · scored 2026-10-23

| Facet | Score |
|---|---|
| Discoverability | 81.7 |
| Contract quality | 69.2 |
| Contract governance | 35.6 |
| Operational transparency | 92.1 |
| Developer ergonomics | 85.1 |
| Access clarity | 85.5 |

**Agent readiness 52.1** — agent-native

| Agent-readiness dimension | Result |
|---|---|
| Spec Presence | yes |
| Agentic Access | derived (partial credit) |
| Reversibility Documented | verified |
| MCP Server | documented (partial credit) |
| Auth Clarity | negotiable (partial credit) |
| Idempotency | verified |
| Error Semantics | documented (partial credit) |
| OpenAPI Examples | verified |
| Rate Limit Signal | documented (partial credit) |
| Event Surface Described | yes |
| Agent Skills | derived (partial credit) |
| Well Known Catalog | — |
| Consent Identity | — |
| Agent Card | — |
| Dry Run Mode | — |
| Delegated Identity | documented (partial credit) |
| Protected Resource Metadata | — |
| Dynamic Client Registration | — |
| Agentic Commerce | — |
| Pagination Ratio | na |
| Operation Distinctiveness | mostly (partial credit) |

**Regulatory alignment 57.5** — Banking & Open Finance

The rubric is published at [github.com/api-evangelist/kin-score](https://github.com/api-evangelist/kin-score). The per-check breakdown behind these numbers — which checks were earned, partial or missed — along with score history and how this provider compares to its peers, is available at [apis.io/providers/plaid/](https://apis.io/providers/plaid/).

## How this profile is made

API Evangelist profiles a company's public API surface the way a developer would find it: the website, developer portal and documentation, the specifications it publishes, its public repositories, and its pricing, status and changelog pages. From that it derives the properties above — contracts split per API, workflows, schemas, collections, governance rules, plans and rate limits — and scores them against the published [Kin Score rubric](https://github.com/api-evangelist/kin-score).

The artifacts are published on [APIs.io](https://apis.io), not in this repository. This repository is the public record for Plaid: the place to say something is wrong, missing or out of date, and to ask for a re-score or a removal.

## Open an issue

- **Something about this listing** — a wrong description, a missing API, a stale artifact or a question about the rating: [open an issue on this repository](https://github.com/api-evangelist/plaid/issues/new).
- **A new API, or one that is not in the catalog yet** — [submit it on APIs.io](https://apis.io/add/).
- **Anything else** — [the APIs.io inbox](https://github.com/api-search/inbox/issues/new) or [info@apievangelist.com](mailto:info@apievangelist.com).
