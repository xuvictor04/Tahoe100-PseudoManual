# The MTAP / Gankyrin trial (earlier work, already run)


```bash
python3 tahoe_mtap_gankyrin.py all --limit-files 30                       # quick trial
nohup python3 tahoe_mtap_gankyrin.py all > /dev/null 2>&1 &               # full run (reuses the trial's work)
python3 tahoe_mtap_gankyrin.py coreg                                      # optional, slow: genome-wide co-regulation
```
Windows: `C:\tahoe\.venv\Scripts\python.exe tahoe_mtap_gankyrin.py all`. The log is `mtap_gankyrin/mtap_gankyrin.log`.
Check section 1 of `mtap_gankyrin/results/summary.txt` first: H1 should be the top well for MTAP, D10 for
Gankyrin, and plate 2 should top the Gankyrin DMSO list. If not, the well positions read from the cell barcodes
are wrong: get the plate layout as a CSV with `sample` and `well` columns and rerun with `--layout layout.csv`
(the atlas and the panel take the same `--layout` option).

Method v3: `tahoe mtap` (or `python3 tahoe_mtap_gankyrin.py analyze`, minutes) redoes the analysis of an earlier
trial on its extract. Like the panel, it takes the composition shift and plate factors from the atlas computed with
v3 (`--atlas DIR|none`), so compute the atlas first; it writes `results/run_info.json` (method version 3).

Other options: `--workers N`, `--mtap-null LINE1,LINE2`, `--extra-genes MAT2A,PRMT5`, `--min-cells N` (default 30),
`--unreliable-plates LIST|none` (default `plate13`).

