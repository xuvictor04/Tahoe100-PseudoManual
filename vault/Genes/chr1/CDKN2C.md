---
symbol: "CDKN2C"
type: "gene"
col: 4396
ensembl_id: "ENSG00000123080"
name: "cyclin dependent kinase inhibitor 2C"
location: "1p32.3"
module: 22
arm: "+"
pooled_cpm: 7.18
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CDKN2C

*cyclin dependent kinase inhibitor 2C* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.59× (z +17.2, q 0e+00, up in 39 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.449× (z -7.6, q 2e-11, down in 29 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.462× (z -7.3, q 7e-11, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[REXO5]] (+0.63, fdr 7e-06), [[CDKN1B]] (+0.62, fdr 7e-06), [[FBXO5]] (+0.61, fdr 1e-05); moves opposite to [[MTG1]] (-0.62, fdr 1e-05), [[NBPF20]] (-0.57, fdr 1e-05), [[SEH1L]] (-0.55, fdr 1e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CPPED1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4396.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.59×** | +17.2 | 0e+00 | 39/41 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +6.9 | 1e-09 | 27/40 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +6.0 | 3e-07 | 24/40 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.97×** | +5.4 | 8e-06 | 21/43 (SNU-423, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.75×** | +5.2 | 3e-05 | 18/44 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **1.60×** | +4.5 | 7e-04 | 13/32 (SW1417, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.29×** | +4.1 | 0.003 | 17/38 (J82, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.0 | 0.005 | 14/33 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.30×** | +3.5 | 0.024 | 11/46 (SW 900, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.43×** | +3.4 | 0.036 | 10/41 (J82, SNU-423, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.25× | +3.0 | 0.12 | 14/42 (PANC-1, A549, …) | top dose only | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4396.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.449×** | -7.6 | 2e-11 | 29/45 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.462×** | -7.3 | 7e-11 | 31/44 (HCT15, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.533×** | -6.0 | 4e-07 | 25/44 (A-172, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.565×** | -5.4 | 9e-06 | 23/45 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.682×** | -5.1 | 3e-05 | 21/46 (A-172, Hs 766T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.586×** | -5.1 | 4e-05 | 24/40 (HCT15, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.599×** | -4.9 | 1e-04 | 18/44 (SW480, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.708×** | -4.6 | 3e-04 | 19/46 (A-172, CFPAC-1, …) | rises with dose | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.418×** | -4.3 | 9e-04 | 18/41 (H4, J82, …) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.444×** | -4.0 | 0.003 | 12/46 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.445×** | -4.0 | 0.003 | 18/42 (J82, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.640×** | -4.0 | 0.003 | 15/44 (HCT15, NCI-H1573, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.670×** | -3.8 | 0.006 | 15/45 (KATO III, LOX-IMVI, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.677×** | -3.7 | 0.009 | 17/44 (LS 180, A-427, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.698×** | -3.4 | 0.025 | 10/45 (A-172, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.722×** | -3.1 | 0.070 | 12/46 (SNU-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.543×** | -3.0 | 0.078 | 16/44 (LOX-IMVI, SW 900, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4396. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 6.86 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0343× (z -10.4) |
| [[A-172 (line)]] | wt | 21.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.177× (z -8.9) |
| [[A498 (line)]] | wt | 8.38 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.242× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 6.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.117× (z -10.1) |
| [[HS-578T (line)]] | alt | 9.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 3.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.11× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 6.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.75× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 7.09 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0530× (z -10.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-1 (line)]] | wt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0804× (z -8.5) |
| [[SNU-423 (line)]] | alt | 8.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.38× (z +10.4) | — |
| [[SW480 (line)]] | alt | 5.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +10.3) | — |
| [[A-427 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4396), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REXO5]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CDKN1B]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 956 |
| [[FBXO5]] | +0.61 | +0.52 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[SNHG31]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[CHD6]] | +0.60 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[FANCM]] | +0.58 | +0.39 / +0.68 | both halves | 5e-05 |  |
| [[KIF11]] | +0.58 | +0.60 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[CDC25C]] | +0.57 | +0.35 / +0.74 | both halves | 1e-04 |  |
| [[NUSAP1]] | +0.57 | +0.53 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[SHCBP1]] | +0.56 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[HMGB2]] | +0.56 | +0.55 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[C21orf58]] | +0.56 | +0.46 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTG1]] | -0.62 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[NBPF20]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[SEH1L]] | -0.55 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[LYPLA1]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[DFFA]] | -0.54 | -0.37 / -0.63 | both halves | 8e-05 |  |
| [[TMEM241]] | -0.54 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[PSEN2]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[TOP1MT]] | -0.52 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[SIN3B]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ANKS6]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 | same gene group |
| [[C7orf50]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PFDN2]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPPED1]] | B | CPPED1 activity lowers CDKN2C's level | lines that do not express CPPED1 (5) vs lines expressing it (45) | 1.83× higher at baseline in the lines without CPPED1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CCDC144CP |
| [[TOP2A]] | B | TOP2A activity lowers CDKN2C's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.487). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.6, -51.9); signed map (-47.8, -49.2). **Vector** length 89.9, 19.9% of its response variance represented; |z| ≥ 3 in 896 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +17.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.0 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +3.8 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.6 | +2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -7.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | -3.7 | -3.7 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -7.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase inhibitor 2C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:50,960,745-50,974,634 (+) |
| Ensembl biotype | protein_coding |
| Also known as | INK4C, p18 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Cyclin dependent kinase inhibitor 2 family |
| Hallmark sets | ADIPOGENESIS, G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 11 pathways, smallest: Oncogene Induced Senescence; Cyclin D associated events in G1; G1 Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [P42773](https://www.uniprot.org/uniprotkb/P42773) (Cyclin-dependent kinase 4 inhibitor C):

> Interacts strongly with CDK6, weakly with CDK4. Inhibits cell growth and proliferation with a correlated dependence on endogenous retinoblastoma protein RB.

**Summary**, from NCBI Gene [1031](https://www.ncbi.nlm.nih.gov/gene/1031):

> The protein encoded by this gene is a member of the INK4 family of cyclin-dependent kinase inhibitors. This protein has been shown to interact with CDK4 or CDK6, and prevent the activation of the CDK kinases, thus function as a cell growth regulator that controls cell cycle G1 progression. Ectopic expression of this gene was shown to suppress the growth of human cells in a manner that appears to correlate with the presence of a wild-type RB1 function. Studies in the knockout mice suggested the …

**Accessions** — [HGNC:1789](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1789) · Entrez [1031](https://www.ncbi.nlm.nih.gov/gene/1031) · UniProt [P42773](https://www.uniprot.org/uniprotkb/P42773) · Ensembl [ENSG00000123080](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123080)

## Data

Gene col 4396: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4396); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4396, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4396]; `tensor/DDL_lfc|DDL_z.npy` [4396]; `embed/gene_vectors.npy` [4396]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4396 or target_col == 4396). Every well: [[CDKN2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKN2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
