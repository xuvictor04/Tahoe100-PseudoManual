---
symbol: "BFAR"
type: "gene"
col: 2366
ensembl_id: "ENSG00000103429"
name: "bifunctional apoptosis regulator"
location: "16p13.12"
module: 119
arm: "+"
pooled_cpm: 47.92
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# BFAR

*bifunctional apoptosis regulator* — 16p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.50× (z +10.1, q 4e-21, up in 38 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.550× (z -17.7, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM11]] (+0.72, fdr 7e-06), [[MIEF1]] (+0.69, fdr 1e-05), [[MTF1]] (+0.66, fdr 1e-05); moves opposite to [[CLASP1-AS1]] (-0.53, fdr 2e-05), [[HACD2]] (-0.53, fdr 2e-05), [[SUGT1P3]] (-0.52, fdr 3e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2366.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.50×** | +10.1 | 4e-21 | 38/49 (RKO, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +5.9 | 9e-07 | 28/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 5e-04 | 28/48 (PANC-1, NCI-H2030, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.041 | 16/48 (NCI-H2030, PANC-1, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.077 | 15/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.3 | 0.077 | 6/48 (NCI-H460, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2366.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.550×** | -17.7 | 0e+00 | 44/48 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.738×** | -9.0 | 7e-17 | 39/48 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.679×** | -8.1 | 1e-13 | 34/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.711×** | -7.1 | 1e-10 | 28/47 (NCI-H1573, A-427, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.717×** | -7.0 | 4e-10 | 29/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.697×** | -6.9 | 7e-10 | 31/48 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.709×** | -6.7 | 2e-09 | 27/45 (RPMI-7951, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.726×** | -6.1 | 9e-08 | 23/40 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.785×** | -5.1 | 3e-05 | 24/48 (SW 900, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.832×** | -3.8 | 0.007 | 22/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.838× | -3.7 | 0.011 | 19/48 (J82, SK-MEL-2, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.835× | -3.4 | 0.031 | 17/47 (AsPC-1, SW 1271, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.739×** | -3.3 | 0.042 | 12/48 (A498, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.855× | -3.3 | 0.043 | 12/48 (A498, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.855× | -3.3 | 0.043 | 15/48 (J82, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | 0.856× | -3.0 | 0.098 | 12/48 (SW1417, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 60.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -14.2) |
| [[J82 (line)]] | alt | 62.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -15.2) |
| [[PANC-1 (line)]] | alt | 84.9 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.503× (z -11.5) |
| [[COLO 205 (line)]] | alt | 45.8 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.82× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.3) |
| [[A-427 (line)]] | wt | 49.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.429× (z -12.0) |
| [[A498 (line)]] | wt | 70.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 70.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -13.0) |
| [[KATO III (line)]] | alt | 50.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -12.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 32.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.98× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.367× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 38.2 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 6.14× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 48.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.9) |
| [[SNU-1 (line)]] | wt | 48.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.320× (z -11.1) |
| [[SW480 (line)]] | alt | 38.0 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.87× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -11.6) |
| [[A549 (line)]] | wt | 67.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -11.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 42.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -11.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 38.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 49.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 43.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 55.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -9.8) |
| [[HOP62 (line)]] | alt | 35.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 39.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 36.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0521× (z -30.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 41.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 29.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 38.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 35.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -12.0) |
| [[RKO (line)]] | wt | 51.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.36× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 48.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -14.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 45.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -9.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 56.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -13.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 57.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -16.0) |
| [[SW1417 (line)]] | alt | 59.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -12.5) |
| [[AN3 CA (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11]] | +0.72 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[MIEF1]] | +0.69 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[MTF1]] | +0.66 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[NCBP2AS2]] | +0.66 | +0.39 / +0.67 | both halves | 6e-05 |  |
| [[GID4]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[SDHAF1]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[IGBP1]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[KIAA1143]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[C19orf12]] | +0.59 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[GSTO1]] | +0.58 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[C16orf91]] | +0.58 | +0.28 / +0.60 | both halves | 3e-04 |  |
| [[WDR53]] | +0.58 | +0.37 / +0.59 | both halves | 7e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLASP1-AS1]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[HACD2]] | -0.53 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[SUGT1P3]] | -0.52 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[RMRP]] | -0.52 | -0.25 / -0.57 | both halves | 4e-04 |  |
| [[ABLIM1]] | -0.51 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[CD83]] | -0.51 | -0.39 / -0.61 | both halves | 5e-05 |  |
| [[NOTCH2NLC]] | -0.51 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ACADVL]] | -0.50 | -0.26 / -0.54 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises BFAR's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.8, -8.9); signed map (-11.1, -10.7). **Vector** length 100, 23.4% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.0 | +10.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.5 | +1.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.2 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -17.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.2 | -7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | -6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -9.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -1.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | bifunctional apoptosis regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.12 — chr16:14,632,931-14,669,236 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BAR, RNF47 |
| Gene groups (HGNC) | Ring finger proteins; Sterile alpha motif domain containing; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZS9](https://www.uniprot.org/uniprotkb/Q9NZS9) (Bifunctional apoptosis regulator):

> Membrane-bound E3 ubiquitin ligase that plays a role in several processes including apoptosis regulation or reticulum endoplasmic stress. Has anti-apoptotic activity, both for apoptosis triggered via death-receptors and via mitochondrial factors. Contributes to the dynamic control of IRE1/ERN1 signaling during ER stress by inducing BAX inhibitor 1/TMBIM6 proteasomal degradation. Promotes the activation of TGF-beta signaling by mediating the 'Lys-63'-linked ubiquitination of TGFBR1 which is …

**Summary**, from NCBI Gene [51283](https://www.ncbi.nlm.nih.gov/gene/51283):

> Enables caspase binding activity; protein-macromolecule adaptor activity; and ubiquitin protein ligase activity. Involved in negative regulation of IRE1-mediated unfolded protein response; proteasome-mediated ubiquitin-dependent protein catabolic process; and protein ubiquitination. Acts upstream of or within negative regulation of apoptotic process. Located in endoplasmic reticulum and membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17613](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17613) · Entrez [51283](https://www.ncbi.nlm.nih.gov/gene/51283) · UniProt [Q9NZS9](https://www.uniprot.org/uniprotkb/Q9NZS9) · Ensembl [ENSG00000103429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103429)

## Data

Gene col 2366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2366); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2366]; `tensor/DDL_lfc|DDL_z.npy` [2366]; `embed/gene_vectors.npy` [2366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2366 or target_col == 2366). Every well: [[BFAR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BFAR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
