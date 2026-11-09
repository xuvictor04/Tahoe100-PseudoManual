"""links - the web addresses of the explorer (the searchable site, pipeline stage `explorer`), shared by every
surface that points into it: the vault notes, the map, the look-ups and the explorer itself.

    site = links.site_url(None)                  # the default: https://<owner>.github.io/<repo>/ of this checkout
    links.gene(site, "TRIM72", "drugs")          # https://.../#/gene/TRIM72/drugs
    links.gene(site, "TRIM72", sub=("line", "HepG2/C3A"))   # https://.../#/gene/TRIM72/line/HepG2%2FC3A
    links.drug(site, "Idarubicin (hydrochloride)")          # https://.../#/drug/Idarubicin%20%28hydrochloride%29
    links.map_gene(site, "TRIM72")               # https://.../map/gene_map.html#TRIM72

Where the addresses come from. The explorer is published on GitHub Pages (the `site` branch of the code's GitHub
repository) and its per-line data in a second repository named <repo>-data, read through raw.githubusercontent.com
(docs/explorer.md). The owner and the repository are read from `git remote get-url origin` of the code checkout, in
any of its forms: https (https://github.com/OWNER/REPO.git), ssh (git@github.com:OWNER/REPO.git,
ssh://git@github.com/OWNER/REPO), or a local git proxy (http://proxy@127.0.0.1:PORT/git/OWNER/REPO). A site URL
given by the user (--site-url) wins; '', 'none' or 'off' means there is no site.

Without a site URL (no git, no GitHub remote, or switched off) every builder returns None, and a caller says where
the explorer is on disk instead (local_hint: 'explorer: open OUT/explorer/web/index.html').

Every route is a hash route (#/...), so the same address works on GitHub Pages and in a folder opened from disk. Each
path segment is percent-encoded with q() (urllib.parse.quote with no safe characters): a space, '(', ')', '/', '#',
'?' and '%' are all encoded, so a label such as 'Idarubicin (hydrochloride)' or 'HepG2/C3A' stays one segment, and
the address also works inside a Markdown link (a bare ')' would end it). The explorer decodes each segment with
decodeURIComponent.
"""

import os
import re
import urllib.parse

from .common import find_git, git_out

CODE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENE_TABS = ("overview", "drugs", "lines", "corr", "partners", "direction", "baseline", "annotation", "downloads")
GENE_SUBS = ("line", "drug", "dd")
OFF = ("", "none", "off", "no", "false")
LOCAL_INDEX = "OUT/explorer/web/index.html"

# a GitHub remote: https://github.com/O/R(.git), git@github.com:O/R(.git), ssh://git@github.com(:22)/O/R(.git)
_GITHUB = re.compile(r"github\.com(?::\d+)?[:/]+([^/\s:]+)/([^/\s]+?)(?:\.git)?/*$", re.I)
# a local git proxy in front of GitHub: http(s)://user@127.0.0.1:PORT/git/O/R(.git)
_PROXY = re.compile(r"^https?://[^/\s]+/git/([^/\s]+)/([^/\s]+?)(?:\.git)?/*$", re.I)
_NAME = re.compile(r"^[A-Za-z0-9._-]+$")


def parse_remote(url):
    """(owner, repo) of a GitHub remote URL in https, ssh or local-proxy form; None for anything else."""
    url = str(url or "").strip()
    if not url:
        return None
    m = _GITHUB.search(url) or _PROXY.match(url)
    if not m:
        return None
    owner, repo = m.group(1), m.group(2)
    if not (_NAME.match(owner) and _NAME.match(repo)) or repo in (".", ".."):
        return None
    return owner, repo


def github_repo(code_root=None):
    """(owner, repo) of the code checkout's `origin` remote (git remote get-url origin), or None when there is no
    git, no origin, or it is not a GitHub repository."""
    root = code_root or CODE_ROOT
    url = git_out(find_git(), root, "remote", "get-url", "origin", timeout=20)
    return parse_remote(url)


def site_url_default(code_root=None):
    """https://<owner>.github.io/<repo>/ (GitHub Pages of the code's repository), or None."""
    r = github_repo(code_root)
    return f"https://{r[0]}.github.io/{r[1]}/" if r else None


def data_url_default(code_root=None):
    """https://raw.githubusercontent.com/<owner>/<repo>-data/main/ (the explorer's data repository), or None."""
    r = github_repo(code_root)
    return f"https://raw.githubusercontent.com/{r[0]}/{r[1]}-data/main/" if r else None


def norm_url(url):
    """A base URL as the builders use it: stripped, ending in '/'; None for '', 'none', 'off' (no site)."""
    if url is None:
        return None
    u = str(url).strip()
    if u.lower() in OFF:
        return None
    return u if u.endswith("/") else u + "/"


def site_url(url=None, code_root=None):
    """The site URL a surface links to: the one given (normalised; '', 'none', 'off' = no site), else the default of
    the code checkout (site_url_default), else None."""
    if url is not None:
        return norm_url(url)
    return site_url_default(code_root)


def data_url(url=None, code_root=None):
    """The data repository's base URL: the one given (normalised), else data_url_default, else None."""
    if url is not None:
        return norm_url(url)
    return data_url_default(code_root)


def local_hint(out=None):
    """What to do without a site URL: 'explorer: open OUT/explorer/web/index.html' (with the real folder when out
    is given)."""
    p = os.path.join(out, "explorer", "web", "index.html") if out else LOCAL_INDEX
    return f"explorer: open {p}"


def q(s):
    """One path segment, percent-encoded (urllib.parse.quote(str(s), safe=''))."""
    return urllib.parse.quote(str(s), safe="")


def gene(site, label, tab=None, sub=None):
    """A gene's page: #/gene/<label>[/<tab>]; sub = ('line', cell name) | ('drug', drug name) | ('dd', dd) for
    #/gene/<label>/line/<cell>, /drug/<drug> or /dd/<dd>. tab is one of GENE_TABS (given with sub: an error)."""
    if not site:
        return None
    if tab is not None and sub is not None:
        raise ValueError("links.gene: give a tab or a sub-page, not both")
    if tab is not None and tab not in GENE_TABS:
        raise ValueError(f"links.gene: unknown tab {tab!r} (one of {', '.join(GENE_TABS)})")
    u = f"{site}#/gene/{q(label)}"
    if tab:
        u += "/" + tab
    if sub is not None:
        kind, value = sub
        if kind not in GENE_SUBS:
            raise ValueError(f"links.gene: unknown sub-page {kind!r} (one of {', '.join(GENE_SUBS)})")
        u += f"/{kind}/{q(value)}"
    return u


def drug(site, name, tab=None):
    """A drug's page: #/drug/<name>[/<tab>]."""
    return f"{site}#/drug/{q(name)}" + (f"/{tab}" if tab else "") if site else None


def dd(site, dd_, tab=None):
    """A drug-dose's page: #/dd/<dd>[/<tab>] (dd = the drug-dose row, atlas/effects/drugdose.csv)."""
    return f"{site}#/dd/{q(dd_)}" + (f"/{tab}" if tab else "") if site else None


def line(site, cell_name, tab=None):
    """A cell line's page: #/line/<cell name>[/<tab>]."""
    return f"{site}#/line/{q(cell_name)}" + (f"/{tab}" if tab else "") if site else None


def module(site, m):
    """A module's page: #/module/<m>."""
    return f"{site}#/module/{q(m)}" if site else None


def group(site, gid):
    """A direction group's page (direction/groups.parquet group_id): #/group/<group_id>."""
    return f"{site}#/group/{q(gid)}" if site else None


def pair(site, a, b):
    """Two genes side by side: #/pair/<A>/<B>."""
    return f"{site}#/pair/{q(a)}/{q(b)}" if site else None


def browse(site, what):
    """A complete table: #/browse/<genes|drugs|drugdoses|lines|modules|groups|arrows>."""
    return f"{site}#/browse/{q(what)}" if site else None


def search(site, text):
    """Every match of a search: #/search/<text>."""
    return f"{site}#/search/{q(text)}" if site else None


def files(site):
    """The 'What is where' page: #/files."""
    return f"{site}#/files" if site else None


def home(site):
    """The explorer's home page."""
    return site or None


def map_gene(site, label=None):
    """The map with a gene selected: <site>map/gene_map.html#<label> (the map without label)."""
    if not site:
        return None
    return f"{site}map/gene_map.html" + (f"#{q(label)}" if label is not None and label != "" else "")


def data_gene_path(col):
    """A gene's per-line file in the data repository (explorer data volume): x/NN/CCCCC.js, NN = col // 1000."""
    col = int(col)
    return f"x/{col // 1000:02d}/{col:05d}.js"


def data_dd_path(dd_):
    """A drug-dose's all-genes file in the data repository: p/NN/DDDD.js, NN = dd // 100."""
    dd_ = int(dd_)
    return f"p/{dd_ // 100:02d}/{dd_:04d}.js"
