"""Fetch research-radio podcast episodes -> {paper id: episode record}.

research-radio's episodes.json is keyed by the same `bibtex:` id the toread
feed uses, so this is a direct join — no normalisation needed.
"""
from __future__ import annotations

import requests

from .feed_client import github_raw_headers


def fetch_episodes(url: str, timeout: int = 30) -> dict[str, dict]:
    """Return a mapping of paper id ("bibtex:...") -> an episode record.

    Each record is a dict with `audio_url` (the standalone MP3), the optional
    per-episode `spotify_url` / `apple_url` platform links (None until
    research-radio publishes them), and the `own` flag. Only episodes that
    carry an `audio_url` are included.

    `url` is a GitHub Contents API URL — see `feed_client.github_raw_headers`
    for why the API is used instead of raw.githubusercontent.com."""
    resp = requests.get(url, headers=github_raw_headers(), timeout=timeout)
    resp.raise_for_status()
    data = resp.json()
    episodes = data if isinstance(data, list) else data.get("episodes", [])
    out: dict[str, dict] = {}
    for ep in episodes:
        ep_id = ep.get("id")
        audio = ep.get("audio_url") or ep.get("audioUrl")
        if ep_id and audio:
            out[ep_id] = {
                "audio_url": audio,
                "spotify_url": ep.get("spotify_url"),
                "apple_url": ep.get("apple_url"),
                "own": bool(ep.get("own", False)),
            }
    return out
