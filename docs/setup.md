# Setup


The download is about 430 GB (4,427 files), plus ~25 GB for the outputs (atlas ~20 GB, gene panel ~3 GB): check the
free space first.

**Linux / macOS:** `bash 00_download_tahoe.sh` (or `bash 00_download_tahoe.sh /data/Tahoe-100M`) installs the packages
and downloads into `~/Tahoe-100M`.

**Windows (PowerShell):** check the free space with `Get-PSDrive C` first. Use the Python of your environment directly
(here `C:\tahoe\.venv`):
```powershell
C:\tahoe\.venv\Scripts\python.exe -m pip install -U huggingface_hub hf_xet "brotli>=1.2.0" numpy pandas pyarrow duckdb scipy psutil
C:\tahoe\.venv\Scripts\hf.exe download tahoebio/Tahoe-100M --repo-type dataset --local-dir C:\tahoe\Tahoe-100M
```
Rerunning the download resumes it. On a `process() takes no keyword arguments` error run
`C:\tahoe\.venv\Scripts\python.exe -m pip uninstall -y brotli brotlicffi` and download again. Optional, for higher rate
limits: `$env:HF_TOKEN="hf_xxx"` first. In the commands below, Windows users type `C:\tahoe\.venv\Scripts\python.exe`
where Linux shows `python3` (if the path has spaces, PowerShell needs `& "C:\path with spaces\python.exe" ...`).

Each script indexes the download once (reads only the file footers; `file_index.json` in its output folder) and
indexes it again by itself when parquet files appear or vanish later, e.g. when the download finished after an
earlier run; `--reindex` forces it. Folders that hold a `file_index.json` (the scripts' outputs) are never read as data.

**Logs and long runs.** Every long command writes its own log into its output folder (`atlas/atlas.log`,
`atlas/agents.log`, `gene_panel/gene_panel.log`, `gene_panel/agents.log`, `mtap_gankyrin/mtap_gankyrin.log`), including
worker lines and a crash traceback, and keeps the computer from sleeping while it runs (Windows: power request; macOS:
caffeinate; Linux: systemd-inhibit where available). A laptop still sleeps when its lid is closed: keep it plugged in,
lid open.
- Linux/macOS, to survive logout: `nohup python3 tahoe_atlas.py compute > /dev/null 2>&1 &`, then
  `tail -f atlas/atlas.log` (Ctrl-C stops watching, not the run).
- Windows: run the command in a PowerShell window and leave it open (no nohup needed); follow the log from a second
  window with `Get-Content atlas\atlas.log -Wait`. Clicking inside the window can pause the run (QuickEdit
  "Select" in the title bar): press Esc to resume.
The scripts print the exact commands for your computer (`check`, and the end of every run).

