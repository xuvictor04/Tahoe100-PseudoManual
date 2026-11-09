---
symbol: "MAML1"
type: "gene"
col: 8411
ensembl_id: "ENSG00000161021"
name: "mastermind like transcriptional coactivator 1"
location: "5q35.3"
module: 144
arm: "+"
pooled_cpm: 52.48
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# MAML1

*mastermind like transcriptional coactivator 1* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.64× (z +11.9, q 8e-30, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.649× (z -10.0, q 7e-21, down in 29 of 41 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SNU-1 0.195×, H4 0.278×, Hs 766T 0.315×, C-33 A 0.387×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 0.280×, Panc 03.27 0.351×, HCT15 0.319×, HS-578T 0.402×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.318×; ⚠ cell-cycle shift, explains ~14% of this change); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (HCT15 0.358×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RUNDC1]] (+0.57, fdr 2e-05), [[ZFTRAF1]] (+0.53, fdr 3e-05), [[LZTS2]] (+0.53, fdr 1e-05); moves opposite to [[SH3KBP1]] (-0.49, fdr 4e-05), [[TMEM241]] (-0.48, fdr 1e-04), [[MAP1B]] (-0.47, fdr 6e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MYO5A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8411.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +11.9 | 8e-30 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.22×** | +10.1 | 2e-21 | 42/49 (HS-578T, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +9.2 | 6e-18 | 34/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +7.9 | 4e-13 | 26/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +7.8 | 7e-13 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +7.8 | 8e-13 | 33/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +6.4 | 1e-08 | 26/48 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.7 | 2e-04 | 21/48 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.20× | +4.0 | 0.003 | 21/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.9 | 0.007 | 17/47 (A-172, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.035 | 17/48 (SW48, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.082 | 15/47 (SW480, H4, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8411.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SNU-1 0.195×, H4 0.278×, Hs 766T 0.315×, C-33 A 0.387×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 0.280×, Panc 03.27 0.351×, HCT15 0.319×, HS-578T 0.402×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.318×; ⚠ cell-cycle shift, explains ~14% of this change); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (HCT15 0.358×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.649×** | -10.0 | 7e-21 | 29/41 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.664×** | -9.2 | 9e-18 | 32/49 (SNU-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -4.1 | 0.008 | 17/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.900× | -3.6 | 0.040 | 16/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.859× | -3.5 | 0.045 | 17/48 (NCI-H1573, C32, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | 0.856× | -3.5 | 0.048 | 17/45 (SW 900, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.872× | -3.3 | 0.072 | 6/48 (HepG2/C3A, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.4 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +15.1) | — |
| [[SW480 (line)]] | alt | 53.8 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +14.4) | — |
| [[A-427 (line)]] | wt | 76.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -12.3) ⚠ cell-cycle shift, explains ~14% of this change |
| [[A498 (line)]] | wt | 37.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 60.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.358× (z -8.6) |
| [[HS-578T (line)]] | alt | 42.1 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -8.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 57.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 41.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +11.5) | — |
| [[C-33 A (line)]] | alt | 80.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -8.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 67.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -9.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 42.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -9.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 40.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.135× (z -10.4) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 58.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 52.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -15.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 77.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.351× (z -11.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 43.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -10.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 98.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[A-172 (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8411), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUNDC1]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ZFTRAF1]] | +0.53 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[LZTS2]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[GPR146]] | +0.53 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[CRAMP1]] | +0.51 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[BCKDHA]] | +0.51 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[POLDIP3]] | +0.50 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[YY1AP1]] | +0.49 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[ZBTB25]] | +0.49 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[CTDNEP1]] | +0.49 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[SH2B1]] | +0.49 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[ZNF580]] | +0.49 | +0.47 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3KBP1]] | -0.49 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[TMEM241]] | -0.48 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[MAP1B]] | -0.47 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[APOO]] | -0.45 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[DYNC1I1]] | -0.45 | -0.37 / -0.49 | both halves | 7e-05 |  |
| [[IBTK]] | -0.44 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[ZDHHC21]] | -0.43 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[HSP90AA1]] | -0.42 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[HSPD1]] | -0.42 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[MYO5A]] | -0.42 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[GNPNAT1]] | -0.42 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[PSMD14]] | -0.41 | -0.38 / -0.33 | both halves | 1e-04 | pathway: Formation of paraxial mesoderm |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO5A]] | B | MYO5A activity raises MAML1's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without MYO5A | 0.086 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.8, -40.2); signed map (-29.9, 28.5). **Vector** length 85.7, 17.7% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.8 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.2 | +11.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.9 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +2.7 | +7.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.6 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +4.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.8 | +2.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.9 | -9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | mastermind like transcriptional coactivator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:179,732,822-179,777,283 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0200, Mam-1 |
| Gene groups (HGNC) | Mastermind like transcriptional coactivator family |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING |
| Reactome | 28 pathways, smallest: NOTCH2 intracellular domain regulates transcription; RUNX3 regulates NOTCH signaling; Regulation of gene expression in late stage (branching morphogenesis) pancreatic bud precursor cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92585](https://www.uniprot.org/uniprotkb/Q92585) (Mastermind-like protein 1):

> Acts as a transcriptional coactivator for NOTCH proteins. Has been shown to amplify NOTCH-induced transcription of HES1. Enhances phosphorylation and proteolytic turnover of the NOTCH intracellular domain in the nucleus through interaction with CDK8. Binds to CREBBP/CBP which promotes nucleosome acetylation at NOTCH enhancers and activates transcription. Induces phosphorylation and localization of CREBBP to nuclear foci. Plays a role in hematopoietic development by regulating NOTCH-mediated …

**Summary**, from NCBI Gene [9794](https://www.ncbi.nlm.nih.gov/gene/9794):

> This protein is the human homolog of mastermind, a Drosophila protein that plays a role in the Notch signaling pathway involved in cell-fate determination. There is in vitro evidence that the human homolog forms a complex with the intracellular portion of human Notch receptors and can increase expression of a Notch-induced gene. This evidence supports its proposed function as a transcriptional co-activator in the Notch signaling pathway. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13632](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13632) · Entrez [9794](https://www.ncbi.nlm.nih.gov/gene/9794) · UniProt [Q92585](https://www.uniprot.org/uniprotkb/Q92585) · Ensembl [ENSG00000161021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161021)

## Data

Gene col 8411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8411); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8411, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8411]; `tensor/DDL_lfc|DDL_z.npy` [8411]; `embed/gene_vectors.npy` [8411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8411 or target_col == 8411). Every well: [[MAML1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAML1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
