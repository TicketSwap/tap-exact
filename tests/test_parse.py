"""Offline tests for parsing Exact Atom feeds."""

from __future__ import annotations

import requests

from tap_exact.tap import TapExact

FEED = """<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"
      xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices">
{entries}
</feed>"""

ENTRY = """<entry><id>{id}</id><content type="application/xml"><m:properties>
<d:ID m:type="Edm.Guid">{id}</d:ID><d:Division m:type="Edm.Int32">3490573</d:Division>
</m:properties></content></entry>"""


def _records(n: int) -> list[dict]:
    tap = TapExact(config={"client_id": "x", "client_secret": "x", "divisions": ["3490573"]}, validate_config=False)
    stream = tap.streams["gl_accounts"]
    response = requests.Response()
    response._content = FEED.format(entries="".join(ENTRY.format(id=i) for i in range(n))).encode()
    return [stream.post_process(row) for row in stream.parse_response(response)]


def test_single_entry() -> None:
    """A feed with one entry yields one record."""
    assert _records(1) == [{"ID": "0", "Division": 3490573}]


def test_multiple_entries() -> None:
    """Entries are parsed in feed order."""
    assert [r["ID"] for r in _records(2)] == ["0", "1"]


def test_no_entries() -> None:
    """An empty feed yields no records."""
    assert _records(0) == []
