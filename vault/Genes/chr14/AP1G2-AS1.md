---
symbol: "AP1G2-AS1"
type: "gene"
col: 15135
ensembl_id: "ENSG00000258727"
name: "AP1G2 antisense RNA 1"
location: "14q11.2"
module: 157
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# AP1G2-AS1

*AP1G2 antisense RNA 1* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +8.7, q 2e-15, up in 22 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0918×); [[Hesperidin (drug)]] 5 µM in 1 line (HEC-1-A 0.0897×); [[Daidzin (drug)]] 0.05 µM in 1 line (SNU-1 0.0494×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG22]] (+0.75, fdr 7e-06), [[RYR2]] (+0.71, fdr 7e-06), [[PCED1A]] (+0.70, fdr 3e-05); moves opposite to [[ISCA2]] (-0.60, fdr 1e-04), [[PAFAH1B3]] (-0.54, fdr 2e-04), [[RHPN2]] (-0.54, fdr 3e-04).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15135.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +8.7 | 2e-15 | 22/35 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +7.2 | 1e-10 | 2/3 (PANC-1, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +7.0 | 5e-10 | 6/15 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +6.5 | 1e-08 | 2/5 (PANC-1, NCI-H1792) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +6.1 | 2e-07 | 14/45 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +5.8 | 7e-07 | 12/27 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +4.6 | 3e-04 | 13/37 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.024 | 3/30 (SNU-1, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.033 | 5/45 (LOX-IMVI, H4, …) | two highest doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.066 | 5/36 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.05 µM |  | **1.41×** | +3.2 | 0.073 | 3/45 (PANC-1, H4, …) | inconsistent across doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.097 | 3/43 (PANC-1, BT-474, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15135.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0918×); [[Hesperidin (drug)]] 5 µM in 1 line (HEC-1-A 0.0897×); [[Daidzin (drug)]] 0.05 µM in 1 line (SNU-1 0.0494×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | 0.699× | -3.2 | 0.40 | 5/45 (CFPAC-1, RKO, …) | top dose only | position effect removed |
| [[Silodosin (drug)]] 5 µM |  | 0.701× | -3.2 | 0.40 | 7/34 (C-33 A, RPMI-7951, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15135. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.62 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0918× (z -9.7) |
| [[C-33 A (line)]] | alt | 6.47 | 0 | 1 | — | [[Irinotecan (drug)]] 0.05 µM 0.0562× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 3.25 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0897× (z -9.1) |
| [[LoVo (line)]] | wt | 2.66 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0908× (z -8.5) |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 1 | — | [[Daidzin (drug)]] 0.05 µM 0.0494× (z -8.6) |
| [[A-172 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15135), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 12 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG22]] | +0.75 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[RYR2]] | +0.71 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PCED1A]] | +0.70 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[HLA-H]] | +0.68 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[HFM1]] | +0.67 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[EME2]] | +0.67 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ZFHX2-AS1]] | +0.66 | +0.58 / +0.48 | both halves | 2e-05 | same gene group; ⚠ same locus (0.3 kb, same strand: neighbours can correlate without regulation) |
| [[STRN4]] | +0.66 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ADCK1]] | +0.65 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[GTF3C2-AS2]] | +0.65 | +0.51 / +0.46 | both halves | 2e-05 | same gene group |
| [[CCNL2]] | +0.65 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[RUSC1-AS1]] | +0.65 | +0.52 / +0.51 | both halves | 1e-05 | same gene group |
| [[TSSK3]] | +0.64 | +0.64 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISCA2]] | -0.60 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[PAFAH1B3]] | -0.54 | -0.31 / -0.31 | both halves | 2e-04 |  |
| [[RHPN2]] | -0.54 | -0.43 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AP1G2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-0.9, 23.1); signed map (32.3, -20.2). **Vector** length 42.0, 4.27% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +1.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.1 | +3.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.1 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | +0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.5 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.3 | -0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -0.1 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.1 | -1.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | AP1G2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q11.2 — chr14:23,561,097-23,568,073 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55442](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55442) · Entrez [102724814](https://www.ncbi.nlm.nih.gov/gene/102724814) · Ensembl [ENSG00000258727](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258727)

## Data

Gene col 15135: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15135); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15135, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15135]; `tensor/DDL_lfc|DDL_z.npy` [15135]; `embed/gene_vectors.npy` [15135]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15135 or target_col == 15135). Every well: [[AP1G2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP1G2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
