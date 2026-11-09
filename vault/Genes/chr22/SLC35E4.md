---
symbol: "SLC35E4"
type: "gene"
col: 1851
ensembl_id: "ENSG00000100036"
name: "solute carrier family 35 member E4"
location: "22q12.2"
module: 34
arm: "+"
pooled_cpm: 20.73
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 5
n_dd_up_clean: 25
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# SLC35E4

*solute carrier family 35 member E4* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.02× (z +17.9, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.725× (z -5.0, q 3e-04, down in 17 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.581× (z -4.6, q 8e-04, down in 15 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM184B]] (+0.68, fdr 2e-05), [[MYO9B]] (+0.63, fdr 3e-05), [[DUSP18]] (+0.63, fdr 3e-05, ⚠ same locus), [[PLAUR]] (+0.62, fdr 1e-05); moves opposite to [[FUBP1]] (-0.62, fdr 9e-05), [[NNT]] (-0.59, fdr 1e-05), [[EXOSC10]] (-0.56, fdr 6e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[UNC5B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1851.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.02×** | +17.9 | 0e+00 | 44/47 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.96×** | +17.6 | 0e+00 | 43/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.90×** | +17.2 | 0e+00 | 45/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +12.5 | 9e-34 | 31/44 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.02×** | +11.4 | 7e-28 | 37/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.95×** | +10.8 | 5e-25 | 35/45 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +10.3 | 5e-23 | 28/45 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +7.0 | 2e-10 | 29/46 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +6.2 | 4e-08 | 24/46 (SW480, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +6.2 | 4e-08 | 21/41 (RKO, SW1417, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +6.0 | 1e-07 | 20/44 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +5.3 | 7e-06 | 18/47 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +5.0 | 3e-05 | 15/47 (SW480, NCI-H2347, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.38×** | +4.9 | 3e-05 | 18/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.74×** | +4.7 | 1e-04 | 16/47 (A498, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +4.7 | 1e-04 | 15/46 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1851.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.725×** | -5.0 | 3e-04 | 17/29 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.581×** | -4.6 | 8e-04 | 15/42 (HS-578T, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.819×** | -4.6 | 8e-04 | 21/47 (Hs 766T, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.628×** | -3.9 | 0.012 | 10/45 (A498, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.655×** | -3.6 | 0.039 | 17/47 (Hs 766T, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.827× | -3.1 | 0.18 | 14/46 (Hs 766T, HS-578T, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.808× | -3.1 | 0.18 | 11/46 (NCI-H23, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1851. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 15.1 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +12.0) | — |
| [[SW480 (line)]] | alt | 21.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.82× (z +13.1) | — |
| [[A549 (line)]] | wt | 14.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 10.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +10.2) | — |
| [[SW1417 (line)]] | alt | 38.7 | 4 | 0 | [[Belinostat (drug)]] 5 µM 3.00× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 70.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.35× (z +9.7) ⚠ unreliable plate only | [[Selinexor (drug)]] 5 µM 0.318× (z -13.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 17.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.94× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 19.3 | 2 | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 4.09× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -16.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 17.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.13× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 9.08 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.67× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 23.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +8.5) | — |
| [[RKO (line)]] | wt | 39.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.3) |
| [[SW48 (line)]] | wt | 62.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 23.1 | 0 | 1 | — | [[Tolmetin (drug)]] 0.05 µM 0.0610× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.53× (z +8.5) ⚠ unreliable plate only | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +8.9) | — |
| [[LoVo (line)]] | wt | 44.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 27.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +9.5) | — |
| [[A-172 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.74 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1851), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM184B]] | +0.68 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[MYO9B]] | +0.63 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[DUSP18]] | +0.63 | +0.43 / +0.62 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PLAUR]] | +0.62 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[RDH13]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[PLEKHG5]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[LRRFIP1]] | +0.61 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[EPN2]] | +0.60 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[AGPAT2]] | +0.60 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[DLGAP4]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[HMOX2]] | +0.59 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[CSNK1E]] | +0.59 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[DENND2C]] | +0.59 | +0.58 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUBP1]] | -0.62 | -0.36 / -0.60 | both halves | 9e-05 |  |
| [[NNT]] | -0.59 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[EXOSC10]] | -0.56 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[CUL4B]] | -0.56 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[STAG2]] | -0.55 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[SH3BGRL]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ATP1A1-AS1]] | -0.54 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[BCLAF1]] | -0.54 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[SUCLG2-DT]] | -0.52 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[WBP11]] | -0.52 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[CPNE1]] | -0.52 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[ANTXR1]] | -0.51 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC5B]] | B | UNC5B activity raises SLC35E4's level | lines that do not express UNC5B (6) vs lines expressing it (44) | 1.80× lower at baseline in the lines without UNC5B | 0.043 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMC6]] | B | TMC6 activity lowers SLC35E4's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 1.50× higher at baseline in the lines without TMC6 | 0.077 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.4, 31.3); signed map (-5.9, 43.6). **Vector** length 98.5, 22.8% of its response variance represented; |z| ≥ 3 in 1,090 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.2 | +10.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +17.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +11.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +5.3 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +3.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.7 | -4.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[NG25 (drug)]] 5 µM |  | -4.2 | -4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -5.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.7 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member E4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,635,781-30,669,016 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Solute carrier family 35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ICL7](https://www.uniprot.org/uniprotkb/Q6ICL7) (Solute carrier family 35 member E4):

> Putative transporter.

**Summary**, from NCBI Gene [339665](https://www.ncbi.nlm.nih.gov/gene/339665):

> Predicted to enable antiporter activity. Predicted to be involved in transmembrane transport. Predicted to be located in membrane. Predicted to be active in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17058](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17058) · Entrez [339665](https://www.ncbi.nlm.nih.gov/gene/339665) · UniProt [Q6ICL7](https://www.uniprot.org/uniprotkb/Q6ICL7) · Ensembl [ENSG00000100036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100036)

## Data

Gene col 1851: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1851); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1851, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1851]; `tensor/DDL_lfc|DDL_z.npy` [1851]; `embed/gene_vectors.npy` [1851]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1851 or target_col == 1851). Every well: [[SLC35E4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35E4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
