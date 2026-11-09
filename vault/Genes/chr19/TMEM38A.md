---
symbol: "TMEM38A"
type: "gene"
col: 1038
ensembl_id: "ENSG00000072954"
name: "transmembrane protein 38A"
location: "19p13.11"
module: 3
arm: "+"
pooled_cpm: 10.56
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 10
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TMEM38A

*transmembrane protein 38A* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +15.9, q 0e+00, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.586× (z -8.2, q 1e-13, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARK4]] (+0.70, fdr 7e-06), [[UBTD1]] (+0.68, fdr 1e-05), [[AGAP3]] (+0.65, fdr 1e-05); moves opposite to [[PDAP1]] (-0.63, fdr 1e-05), [[PIGO]] (-0.56, fdr 1e-04), [[ARAF]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC29A4]] → it (grade B ⚠); 2 go from it, the strongest it → [[ANKRD16]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1038.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +15.9 | 0e+00 | 38/45 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.11×** | +11.5 | 6e-28 | 32/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +9.4 | 1e-18 | 27/46 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +8.6 | 8e-16 | 33/43 (CFPAC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +8.5 | 2e-15 | 30/46 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +8.0 | 2e-13 | 31/46 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +7.6 | 3e-12 | 25/47 (A498, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +6.8 | 9e-10 | 20/45 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.3 | 1e-08 | 22/37 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.96×** | +5.4 | 4e-06 | 16/47 (MIA PaCa-2, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.003 | 11/47 (Panc 03.27, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.005 | 6/46 (Panc 03.27, NCI-H2030, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.006 | 9/46 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.27×** | +3.5 | 0.016 | 16/43 (SNU-423, SW480, …) | top dose only |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.029 | 3/46 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.14× | +2.9 | 0.091 | 5/47 (HEC-1-A, RPMI-7951, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.091 | 7/46 (PANC-1, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1038.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.586×** | -8.2 | 1e-13 | 27/45 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.800×** | -4.8 | 4e-04 | 17/45 (RKO, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.740×** | -4.4 | 0.001 | 15/45 (LOX-IMVI, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.749×** | -4.4 | 0.001 | 18/44 (Panc 03.27, SW1417, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.754×** | -4.2 | 0.004 | 17/46 (NCI-H23, PANC-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.633×** | -3.7 | 0.023 | 7/45 (RKO, SHP-77, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.799×** | -3.4 | 0.048 | 15/46 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.804×** | -3.4 | 0.056 | 14/46 (AN3 CA, LS 180, …) | two highest doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.796×** | -3.2 | 0.078 | 15/42 (C-33 A, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | **0.813×** | -3.2 | 0.088 | 8/47 (COLO 205, SW 1088, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.818× | -3.1 | 0.10 | 11/46 (BT-474, NCI-H2030, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1038. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 18.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 9.87 | 0 | 2 | — | [[Ferulic acid (drug)]] 0.05 µM 0.0712× (z -9.3) |
| [[Hs 766T (line)]] | wt | 7.03 | 0 | 2 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.109× (z -9.5) |
| [[PANC-1 (line)]] | alt | 9.59 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +8.7) | [[Pralsetinib (drug)]] 5 µM 0.0565× (z -10.5) |
| [[SHP-77 (line)]] | alt | 33.6 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.12× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0663× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.141× (z -11.7) |
| [[COLO 205 (line)]] | alt | 8.12 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -9.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[J82 (line)]] | alt | 9.79 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 5.33 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0834× (z -8.9) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H2030 (line)]] | alt | 7.66 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.155× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0765× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.328× (z -8.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RKO (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -9.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -8.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1038), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARK4]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[UBTD1]] | +0.68 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[AGAP3]] | +0.65 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[SPACDR]] | +0.65 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[RABGEF1P1]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[BAHD1]] | +0.61 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[SNHG25]] | +0.60 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[NRTN]] | +0.60 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[TBC1D22A-DT]] | +0.60 | +0.30 / +0.65 | both halves | 2e-04 |  |
| [[LINC02976]] | +0.59 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[CIB2]] | +0.59 | +0.27 / +0.57 | both halves | 3e-04 |  |
| [[DCTN6-DT]] | +0.59 | +0.42 / +0.65 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDAP1]] | -0.63 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[PIGO]] | -0.56 | -0.36 / -0.63 | both halves | 1e-04 |  |
| [[ARAF]] | -0.54 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[HUWE1]] | -0.54 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[CCT7]] | -0.54 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[MBTPS2]] | -0.53 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[LIN7C]] | -0.53 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[EIF4G2]] | -0.53 | -0.45 / -0.68 | both halves | 3e-05 |  |
| [[RUVBL1]] | -0.51 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[PABIR1]] | -0.51 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[SNX17]] | -0.51 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[PSMC3]] | -0.51 | -0.37 / -0.62 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC29A4]] | B | SLC29A4 activity raises TMEM38A's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.74× lower at baseline in the lines without SLC29A4 | 0.081 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD16]] | C | TMEM38A's natural level weakens ANKRD16's drug response | TMEM38A's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.06; direction not clear | 0.079 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| cells under [[Balsalazide (sodium hydrate) (drug)]] 5 µM | C | TMEM38A's natural level lowers the cells' numbers under Balsalazide (sodium hydrate) 5 µM (makes them more sensitive) | TMEM38A's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.73 | 0.206 over the table, 0.011 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.558). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.7, -3.7); signed map (-32.6, 17.2). **Vector** length 75.6, 13.0% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +15.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +7.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.1 | +3.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.2 | -4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -3.3 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 38A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:16,661,139-16,690,023 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3169, TRIC-A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6F2](https://www.uniprot.org/uniprotkb/Q9H6F2) (Trimeric intracellular cation channel type A):

> Intracellular monovalent cation channel required for maintenance of rapid intracellular calcium release. Acts as a potassium counter-ion channel that functions in synchronization with calcium release from intracellular stores (By similarity). Opened by a change of voltage within the sarcoplasmic reticulum lumen (By similarity).

**Summary**, from NCBI Gene [79041](https://www.ncbi.nlm.nih.gov/gene/79041):

> Predicted to enable potassium channel activity. Predicted to be involved in potassium ion transmembrane transport; regulation of release of sequestered calcium ion into cytosol; and release of sequestered calcium ion into cytosol by sarcoplasmic reticulum. Predicted to act upstream of or within several processes, including cellular response to caffeine; endoplasmic reticulum organization; and regulation of cardiac muscle contraction by regulation of the release of sequestered calcium ion. …

**Accessions** — [HGNC:28462](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28462) · Entrez [79041](https://www.ncbi.nlm.nih.gov/gene/79041) · UniProt [Q9H6F2](https://www.uniprot.org/uniprotkb/Q9H6F2) · Ensembl [ENSG00000072954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072954)

## Data

Gene col 1038: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1038); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1038, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1038]; `tensor/DDL_lfc|DDL_z.npy` [1038]; `embed/gene_vectors.npy` [1038]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1038 or target_col == 1038). Every well: [[TMEM38A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM38A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
