# Contributing to the MINE Zettelkasten

This is the **MINE** team's shared Zettelkasten — a living archive of the papers
we read, summarized and cross-linked, and published as a website. You add to it
straight from Slack; no Git, no PRs.

**Browse it:** https://fabiogiglietto.github.io/mine-zettelkasten/

---

## How to add a paper

In the MINE Slack **`#zettelkasten`** channel, just **post a link to the paper**:

```
https://doi.org/10.1080/1369118X.2024.2349123
```

That's it — no hashtag, no command. A bot watches the channel (about every 30
minutes) and takes it from there. (Normal discussion is fine: only messages that
contain a paper **link or an attached PDF** are treated as submissions.)

### What the bot does

1. Reads the link and looks up the paper's details (title, authors, year) from
   Crossref / arXiv.
2. Tries to get the **full-text PDF**, in this order:
   - a PDF you attached to the message,
   - the arXiv PDF (if it's an arXiv link),
   - an **open-access** copy via Unpaywall (if it has a DOI).
3. If it finds one, it replies **✅ Added** in the thread. The paper is
   summarized and appears as a note on the site — within minutes, or by the next
   day at the latest.
4. If it **can't** find an open-access PDF, it replies in the thread asking you
   to **attach the PDF**. Just drop the PDF into that thread and the bot picks it
   up on its next pass.

### Open access only

We only archive papers we can store a full text for **legitimately** — an
open-access PDF, an arXiv preprint, or a PDF you're entitled to share. If a
paper is paywalled and you don't have a shareable PDF, please don't force it in.

### Tips

- **Include a DOI or arXiv link** when you can — it gives the cleanest metadata
  and the best shot at an automatic open-access PDF.
- **One paper per message.** Post separate messages for separate papers.
- **Fastest path:** attach the PDF to your message up front, and the bot won't
  need to go looking.

### Duplicates

If someone has already added the paper (or it's already in the archive from
Fabio's reading list), the bot replies **"already in the archive"** and skips
it — no duplicate notes. Re-posting something is harmless.

### Attribution

Your name (from your Slack profile) is recorded as the submitter and **shown on
the public note** for papers you add. If you'd rather not have your name
published, say so and we'll adjust.

---

## What happens behind the scenes

Your submission flows through a small two-repo pipeline:

- **[mine-toread](https://github.com/fabiogiglietto/mine-toread)** — reads the
  Slack channel, fetches the PDF, and publishes a feed of papers (your
  submissions plus Fabio's Paperpile reading list).
- **mine-zettelkasten** (this repo) — turns each new paper into a summarized,
  topic-linked note and builds the website.

Questions or something looks off? Ping Fabio in `#zettelkasten`.
