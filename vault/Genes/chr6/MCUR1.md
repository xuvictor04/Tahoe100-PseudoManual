---
symbol: "MCUR1"
type: "gene"
col: 564
ensembl_id: "ENSG00000050393"
name: "mitochondrial calcium uniporter regulator 1"
location: "6p23"
module: 188
arm: "+"
pooled_cpm: 28.95
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/188", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# MCUR1

*mitochondrial calcium uniporter regulator 1* — 6p23

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.33× (z +13.3, q 1e-37, up in 33 of 38 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (KATO III 5.24×, HOP62 3.48×, LS 180 4.05×, NCI-H460 3.19×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW480 2.84×, KATO III 3.72×, HOP62 3.15×, PANC-1 2.58×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (A-172 0.265×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.205×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-1 0.224×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMOD2]] (+0.64, fdr 1e-05), [[RNF2]] (+0.62, fdr 1e-05), [[PRXL2C]] (+0.61, fdr 2e-05); moves opposite to [[RBBP6]] (-0.55, fdr 5e-05), [[SPAG4]] (-0.52, fdr 1e-04), [[BOLA1]] (-0.52, fdr 5e-04).
> It is in [[Module 188]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CEMIP2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 564.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (KATO III 5.24×, HOP62 3.48×, LS 180 4.05×, NCI-H460 3.19×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW480 2.84×, KATO III 3.72×, HOP62 3.15×, PANC-1 2.58×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +13.3 | 1e-37 | 33/38 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +12.3 | 2e-32 | 40/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +6.4 | 4e-08 | 29/43 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.35×** | +4.7 | 4e-04 | 24/47 (HT-29, NCI-H1792, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +4.1 | 0.004 | 25/45 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +4.1 | 0.004 | 20/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.24×** | +3.5 | 0.032 | 13/45 (H4, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.23×** | +3.3 | 0.062 | 16/48 (C32, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.3 | 0.072 | 14/48 (LS 180, CFPAC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.2 | 0.089 | 0/48 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.21× | +3.1 | 0.10 | 15/48 (CFPAC-1, C32, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | 1.43× | +3.1 | 0.10 | 13/48 (A-172, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.10 | 11/48 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.10 | 3/48 (A498, SW1417, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (A-172 0.265×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.205×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-1 0.224×; ⚠ toxic; transcription drop).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 564. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 31.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +10.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 29.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.24× (z +12.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 37.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.50× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 19.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.88× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 29.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.205× (z -9.1) |
| [[Hs 766T (line)]] | wt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 21.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -8.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 29.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 564), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMOD2]] | +0.64 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[RNF2]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[PRXL2C]] | +0.61 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[QDPR]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SSX2IP]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[AKTIP]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[SERAC1]] | +0.56 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[STX2]] | +0.56 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[ZFAND4]] | +0.55 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[STX7]] | +0.55 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[GCSH]] | +0.55 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[SPAST]] | +0.55 | +0.43 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP6]] | -0.55 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[SPAG4]] | -0.52 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[BOLA1]] | -0.52 | -0.24 / -0.54 | both halves | 5e-04 |  |
| [[SON]] | -0.50 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[INTS6]] | -0.49 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[FANK1]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[ZNF586]] | -0.48 | -0.52 / -0.24 | both halves | 4e-04 |  |
| [[TTC41P]] | -0.48 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[TM9SF4]] | -0.48 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ZNF432]] | -0.48 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[FAM120B]] | -0.47 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[ARMC5]] | -0.47 | -0.30 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEMIP2]] | C | CEMIP2 activity lowers MCUR1's level | lines that do not express CEMIP2 (4) vs lines expressing it (46) | 1.59× higher at baseline in the lines without CEMIP2 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIFC3, SMARCA2, PLSCR2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-5.8, -3.4); signed map (-36.7, -18.0). **Vector** length 69.0, 13.6% of its response variance represented; |z| ≥ 3 in 625 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.0 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -0.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial calcium uniporter regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p23 — chr6:13,786,557-13,814,568 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20958; previously C6orf79, CCDC90A |
| Gene groups (HGNC) | MCU complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AQ8](https://www.uniprot.org/uniprotkb/Q96AQ8) (Mitochondrial calcium uniporter regulator 1):

> Key regulator of mitochondrial calcium uniporter (MCU) required for calcium entry into mitochondrion. Plays a direct role in uniporter-mediated calcium uptake via a direct interaction with MCU. Probably involved in the assembly of the membrane components of the uniporter complex (uniplex).

**Summary**, from NCBI Gene [63933](https://www.ncbi.nlm.nih.gov/gene/63933):

> Predicted to enable protein-macromolecule adaptor activity. Involved in calcium import into the mitochondrion; calcium ion import; and positive regulation of mitochondrial calcium ion concentration. Located in mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21097) · Entrez [63933](https://www.ncbi.nlm.nih.gov/gene/63933) · UniProt [Q96AQ8](https://www.uniprot.org/uniprotkb/Q96AQ8) · Ensembl [ENSG00000050393](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000050393)

## Data

Gene col 564: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 564); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 564, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 564]; `tensor/DDL_lfc|DDL_z.npy` [564]; `embed/gene_vectors.npy` [564]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 564 or target_col == 564). Every well: [[MCUR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCUR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
