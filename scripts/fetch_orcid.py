#!/usr/bin/env python3
"""
Fetch publications from ORCID public API and retrieve BibTeX from CrossRef.
Writes output to assets/ref.bib.

Usage:
    python scripts/fetch_orcid.py

ORCID_ID can be overridden via environment variable.
"""

import os
import re
import sys
import time
import requests

ORCID_ID = os.environ.get("ORCID_ID", "0000-0002-8145-800X")
OUTPUT_FILE = "assets/ref.bib"
CROSSREF_MAILTO = "js.brown@utoronto.ca"


def normalize_doi(raw: str) -> str:
    raw = raw.strip()
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", raw, flags=re.IGNORECASE)


def fetch_orcid_works() -> list[dict]:
    url = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"
    resp = requests.get(url, headers={"Accept": "application/json"}, timeout=30)
    resp.raise_for_status()

    results = []
    for group in resp.json().get("group", []):
        # Prefer the group-level DOI (deduplicated across sources); fall back to work-summary
        doi = None
        for eid in group.get("external-ids", {}).get("external-id", []):
            if eid.get("external-id-type") == "doi":
                doi = normalize_doi(eid.get("external-id-value", ""))
                break

        summaries = group.get("work-summary", [])
        if not summaries:
            continue
        s = summaries[0]  # use preferred (first) source per group

        if not doi:
            for eid in s.get("external-ids", {}).get("external-id", []):
                if eid.get("external-id-type") == "doi":
                    doi = normalize_doi(eid.get("external-id-value", ""))
                    break

        title = ((s.get("title") or {}).get("title") or {}).get("value", "Unknown")
        year = ((s.get("publication-date") or {}).get("year") or {}).get("value", "")
        results.append({"doi": doi, "title": title, "year": year})

    return results


def fetch_bibtex(doi: str) -> str | None:
    url = f"https://api.crossref.org/works/{doi}/transform/application/x-bibtex"
    headers = {
        "Accept": "application/x-bibtex",
        "User-Agent": f"BrownLabUofT-website/1.0 (mailto:{CROSSREF_MAILTO})",
    }
    try:
        resp = requests.get(url, headers=headers, timeout=20)
        if resp.status_code == 200:
            return resp.text.strip()
        print(f"  CrossRef returned {resp.status_code} for {doi}", file=sys.stderr)
    except requests.RequestException as exc:
        print(f"  Request error for {doi}: {exc}", file=sys.stderr)
    return None


def main() -> None:
    print(f"Fetching works for ORCID {ORCID_ID} ...")
    works = fetch_orcid_works()
    print(f"Found {len(works)} work(s) on ORCID.")

    entries: list[str] = []
    skipped: list[str] = []

    for i, w in enumerate(works, 1):
        doi, title = w["doi"], w["title"]
        if not doi:
            print(f"  [{i}/{len(works)}] No DOI — skipping: {title[:70]}")
            skipped.append(title)
            continue

        print(f"  [{i}/{len(works)}] {doi}")
        bib = fetch_bibtex(doi)
        if bib:
            entries.append(bib)
        else:
            print(f"    No BibTeX — skipping: {title[:70]}", file=sys.stderr)
            skipped.append(title)

        time.sleep(0.5)  # polite rate for CrossRef

    if not entries:
        print("ERROR: No BibTeX entries retrieved. Not overwriting ref.bib.", file=sys.stderr)
        sys.exit(1)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(entries) + "\n")

    n = len(entries)
    print(f"\nWrote {n} entr{'y' if n == 1 else 'ies'} to {OUTPUT_FILE}.")
    if skipped:
        print(f"Skipped {len(skipped)} work(s) (no DOI or no CrossRef BibTeX):")
        for t in skipped:
            print(f"  - {t[:80]}")


if __name__ == "__main__":
    main()
