#!/usr/bin/env python3
"""Build the Plaid API tube-style map.

~30 of Plaid's APIs grouped onto 6 product lines.
"""

import sys
from pathlib import Path

sys.path.insert(0, "/Users/kinlane/GitHub/all/.claude/skills")
from _subway_engine import build_subway  # noqa: E402

ABBREV = {
    "Identity Verification":  "Identity Verify",
    "Watchlist Screening":    "Watchlist",
    "Webhook Verification":   "Webhook Verify",
    "Bank Transfer":          "Bank Transfer",
    "Payment Initiation":     "Payment Init",
    "Consumer Report":        "Consumer Report",
}

LINES = [
    {
        "name": "Core & Items",
        "color": "#000000",  # Plaid black
        "stations": [
            ("Item",         (270, 200)),
            ("Accounts",     (440, 175)),
            ("Auth",         (610, 165)),
            ("Institutions", (790, 175)),
            ("Categories",   (970, 200)),
        ],
    },
    {
        "name": "Transactions & Banking",
        "color": "#0E9D6E",
        "stations": [
            ("Transactions",  (270, 295)),
            ("Liabilities",   (430, 320)),
            ("Investments",   (590, 295)),
            ("Bank Transfer", (760, 320)),
            ("Transfer",      (930, 295)),
        ],
    },
    {
        "name": "Identity & Risk",
        "color": "#C5318B",
        "stations": [
            ("Identity",              (270, 410)),
            ("Identity Verification", (440, 430)),
            ("Watchlist Screening",   (620, 430)),
            ("Beacon",                (790, 410)),
            ("Signal",                (940, 410)),
        ],
    },
    {
        "name": "Income & Reports",
        "color": "#1E5BD0",
        "stations": [
            ("Income",          (270, 530)),
            ("Asset Report",    (430, 510)),
            ("Base Report",     (580, 510)),
            ("Consumer Report", (730, 510)),
            ("Statements",      (870, 530)),
            ("Credit",          (1000, 555)),
        ],
    },
    {
        "name": "Payments",
        "color": "#E68B1F",
        "stations": [
            ("Payment Initiation", (350, 640)),
            ("Wallet",             (530, 615)),
            ("Deposit Switch",     (730, 640)),
            ("Employers",          (910, 615)),
        ],
    },
    {
        "name": "Platform",
        "color": "#7B3FE4",
        # Closed pentagon at bottom-right.
        "closed": True,
        "stations": [
            ("Application",          (820, 690)),
            ("Sandbox",              (893, 740)),
            ("Webhook Verification", (864, 815)),
            ("Link",                 (776, 815)),
            ("Processor",            (747, 740)),
        ],
    },
]

URL_OVERRIDES = {
    "Item":                   "https://apis.apis.io/apis/plaid/plaid-item-api/",
    "Accounts":               "https://apis.apis.io/apis/plaid/plaid-accounts-api/",
    "Auth":                   "https://apis.apis.io/apis/plaid/plaid-auth-api/",
    "Institutions":           "https://apis.apis.io/apis/plaid/plaid-institutions-api/",
    "Categories":             "https://apis.apis.io/apis/plaid/plaid-categories-api/",
    "Transactions":           "https://apis.apis.io/apis/plaid/plaid-transactions-api/",
    "Liabilities":            "https://apis.apis.io/apis/plaid/plaid-liabilities-api/",
    "Investments":            "https://apis.apis.io/apis/plaid/plaid-investments-api/",
    "Bank Transfer":          "https://apis.apis.io/apis/plaid/plaid-bank-transfer-api/",
    "Transfer":               "https://apis.apis.io/apis/plaid/plaid-transfer-api/",
    "Identity":               "https://apis.apis.io/apis/plaid/plaid-identity-api/",
    "Identity Verification":  "https://apis.apis.io/apis/plaid/plaid-entity-verification-api/",
    "Watchlist Screening":    "https://apis.apis.io/apis/plaid/plaid-watchlist-screening-api/",
    "Beacon":                 "https://apis.apis.io/apis/plaid/plaid-beacon-api/",
    "Signal":                 "https://apis.apis.io/apis/plaid/plaid-signal-api/",
    "Income":                 "https://apis.apis.io/apis/plaid/plaid-income-api/",
    "Asset Report":           "https://apis.apis.io/apis/plaid/plaid-asset-report-api/",
    "Base Report":            "https://apis.apis.io/apis/plaid/plaid-base-report-api/",
    "Consumer Report":        "https://apis.apis.io/apis/plaid/plaid-consumer-report-api/",
    "Statements":             "https://apis.apis.io/apis/plaid/plaid-statements-api/",
    "Credit":                 "https://apis.apis.io/apis/plaid/plaid-credit-api/",
    "Payment Initiation":     "https://apis.apis.io/apis/plaid/plaid-payment-initiation-api/",
    "Wallet":                 "https://apis.apis.io/apis/plaid/plaid-wallet-api/",
    "Deposit Switch":         "https://apis.apis.io/apis/plaid/plaid-deposit-switch-api/",
    "Employers":              "https://apis.apis.io/apis/plaid/plaid-employers-api/",
    "Application":            "https://apis.apis.io/apis/plaid/plaid-application-api/",
    "Sandbox":                "https://apis.apis.io/apis/plaid/plaid-sandbox-api/",
    "Webhook Verification":   "https://apis.apis.io/apis/plaid/plaid-webhook-verification-api/",
    "Link":                   "https://apis.apis.io/apis/plaid/plaid-link-api/",
    "Processor":              "https://apis.apis.io/apis/plaid/plaid-processor-api/",
}


def main():
    seen = set()
    n_unique = 0
    for ln in LINES:
        for (st, _) in ln["stations"]:
            if st not in seen:
                n_unique += 1
                seen.add(st)
    build_subway(
        title="The Plaid API · Underground Map",
        subtitle=f"{n_unique} APIs · {len(LINES)} functional lines · click any station for the apis.io page",
        lines=LINES,
        abbrev=ABBREV,
        source_label="Source: plaid/openapi/*.yml · github.com/api-evangelist/plaid",
        out_dir=Path(__file__).resolve().parent,
        out_basename="plaid-subway-map",
        provider_id="plaid",
        station_url_overrides=URL_OVERRIDES,
    )


if __name__ == "__main__":
    main()
