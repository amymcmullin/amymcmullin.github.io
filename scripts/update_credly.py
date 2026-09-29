"""Refresh _data/credly.json from Amy's public Credly profile.

Run by .github/workflows/update-credly.yml (weekly, or on demand from the
Actions tab). Uses only the Python standard library.
"""
import json
import datetime
import pathlib
import urllib.request

USER = "amy-mcmullin"
PROFILE = f"https://www.credly.com/users/{USER}"
OUT = pathlib.Path(__file__).resolve().parent.parent / "_data" / "credly.json"
MAX_PAGES = 30


def fetch(page):
    req = urllib.request.Request(
        f"{PROFILE}/badges.json?page={page}",
        headers={"Accept": "application/json", "User-Agent": "amymcmullin.github.io badge sync"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def issuer_name(badge):
    entities = (badge.get("issuer") or {}).get("entities") or []
    primary = [e for e in entities if e.get("primary")] or entities
    for e in primary:
        name = (e.get("entity") or {}).get("name")
        if name:
            return name
    return "Other"


def main():
    today = datetime.date.today().isoformat()
    raw, seen = [], set()
    for page in range(1, MAX_PAGES + 1):
        payload = fetch(page)
        data = payload.get("data") or []
        new = [b for b in data if b.get("id") not in seen]
        if not new:
            break
        raw.extend(new)
        seen.update(b["id"] for b in new)
        meta = payload.get("metadata") or {}
        if meta.get("total_pages") and page >= meta["total_pages"]:
            break

    badges = []
    for b in raw:
        t = b.get("badge_template") or {}
        expires = b.get("expires_at_date")
        badges.append({
            "id": b["id"],
            "name": t.get("name", "").strip(),
            "issuer": issuer_name(b),
            "issued": b.get("issued_at_date"),
            "expires": expires,
            "status": "expired" if expires and expires < today else "active",
            "type": t.get("type_category") or "",
            "level": t.get("level") or "",
            "image": b.get("image_url") or t.get("image_url"),
            "url": f"https://www.credly.com/badges/{b['id']}",
        })
    badges.sort(key=lambda x: x["issued"] or "", reverse=True)

    if not badges:
        raise SystemExit("Credly returned no badges; leaving the existing file alone.")

    OUT.write_text(json.dumps({
        "updated": today,
        "profile": PROFILE,
        "badges": badges,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(badges)} badges to {OUT}")


if __name__ == "__main__":
    main()
