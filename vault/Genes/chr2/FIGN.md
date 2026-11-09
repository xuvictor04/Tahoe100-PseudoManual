---
symbol: "FIGN"
type: "gene"
col: 11267
ensembl_id: "ENSG00000182263"
name: "fidgetin, microtubule severing factor"
location: "2q24.3"
module: 9
arm: "+"
pooled_cpm: 32.56
n_lines_expressing: 34
n_dd_up: 44
n_dd_down: 9
n_dd_up_clean: 41
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 76
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# FIGN

*fidgetin, microtubule severing factor* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.02× (z +14.8, q 0e+00, up in 23 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[PF-06260933 (drug)]] 5 µM: 0.523× (z -4.8, q 9e-04, down in 15 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFHX4]] (+0.67, fdr 7e-06), [[NFIB]] (+0.66, fdr 7e-06), [[ANGPT1]] (+0.65, fdr 1e-05); moves opposite to [[MYO9B]] (-0.62, fdr 7e-06), [[TMEM255B]] (-0.56, fdr 1e-05), [[SLCO4A1]] (-0.55, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NFIA]] → it (grade B ⚠); 76 go from it, the strongest it → cells under [[AZD2858 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11267.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +14.8 | 0e+00 | 23/32 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.29×** | +12.3 | 2e-32 | 23/32 (NCI-H23, H4, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +10.8 | 4e-25 | 25/32 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.97×** | +10.1 | 1e-21 | 25/32 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +8.7 | 5e-16 | 18/32 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.72×** | +8.1 | 8e-14 | 24/31 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.7 | 2e-09 | 20/31 (NCI-H23, H4, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +6.2 | 3e-08 | 19/32 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +5.6 | 1e-06 | 19/32 (NCI-H23, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +5.6 | 1e-06 | 16/31 (NCI-H2347, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.11×** | +5.5 | 2e-06 | 17/32 (NCI-H460, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +5.4 | 3e-06 | 17/31 (HOP62, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +5.4 | 3e-06 | 14/31 (HepG2/C3A, C32, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.3 | 5e-06 | 16/32 (NCI-H2347, J82, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +5.1 | 1e-05 | 16/32 (NCI-H23, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +5.1 | 1e-05 | 14/31 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11267.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | **0.523×** | -4.8 | 9e-04 | 15/30 (LOX-IMVI, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.751×** | -4.3 | 0.005 | 13/31 (SW 900, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.756×** | -4.2 | 0.005 | 14/30 (BT-474, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **0.827×** | -4.0 | 0.007 | 11/32 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.766×** | -4.0 | 0.007 | 15/31 (SK-MEL-2, NCI-H1792, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.761×** | -3.9 | 0.008 | 12/32 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.768×** | -3.8 | 0.011 | 13/31 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.725×** | -3.4 | 0.041 | 10/32 (A498, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.801×** | -3.3 | 0.054 | 7/31 (A498, HEC-1-A, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.867× | -3.0 | 0.13 | 7/32 (HEC-1-A, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 84.9 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -15.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.279× (z -11.9) |
| [[A-427 (line)]] | wt | 46.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +19.2) | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[NCI-H2030 (line)]] | alt | 139 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.410× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 47.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +24.4) | — |
| [[SHP-77 (line)]] | alt | 70.5 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 164 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 98.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -10.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.330× (z -9.5) |
| [[BT-474 (line)]] | alt | 18.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +10.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.154× (z -8.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 70.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 56.6 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -11.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[PANC-1 (line)]] | alt | 32.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +10.9) | — |
| [[A-172 (line)]] | wt | 9.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +11.2) | — |
| [[H4 (line)]] | wt | 20.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.20× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 34.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 10.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.02 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFHX4]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[NFIB]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ANGPT1]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[CRISPLD1]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[TGFB2]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[EPHA5]] | +0.61 | +0.57 / +0.63 | both halves | 8e-06 |  |
| [[MAPK10]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[ZNF618]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[MID1]] | +0.58 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ATF7IP]] | +0.57 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[CSRNP3]] | +0.57 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[RHOBTB3]] | +0.57 | +0.62 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9B]] | -0.62 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[TMEM255B]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SLCO4A1]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[TMEM132B]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[TNNT1]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[RHBDF2]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[BCLAF3]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[PDE2A]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[TMEM44]] | -0.53 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[FAM131A]] | -0.52 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[GNAI3]] | -0.52 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[RABGEF1]] | -0.52 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFIA]] | B | NFIA activity raises FIGN's level | lines that do not express NFIA (11) vs lines expressing it (39) | 1.74× lower at baseline in the lines without NFIA | 0.093 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[CHN1]] | B | CHN1 activity raises FIGN's level | lines that do not express CHN1 (10) vs lines expressing it (40) | 3.72× lower at baseline in the lines without CHN1 | 0.093 | ⚠ within organs, on part of the lines; also absent: GXYLT2, HHIPL2, CARMIL2; maybe low, not absent |
| [[PRKD1]] | C | PRKD1 activity raises FIGN's level | lines that do not express PRKD1 (13) vs lines expressing it (37) | 7.63× lower at baseline in the lines without PRKD1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SPART, KCTD16, DMD; co-absent with the target |

### Downstream of this gene

*76 arrows, 76 of them with an alert ⚠; grade A 0, B 0, C 76. Shown: the 12 strongest; 64 more arrows (64 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[AZD2858 (drug)]] 5 µM | C | FIGN activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.35× the cells of the other lines | 0.004 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| cells under [[Dihydroartemisinin (drug)]] 5 µM | C | FIGN activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.33× the cells of the other lines | 0.004 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| cells under [[Glasdegib (drug)]] 5 µM | C | FIGN activity lowers the cells' numbers under Glasdegib 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.22× the cells of the other lines | 0.004 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART; cell counts less trustworthy |
| cells under [[Sulfatinib (drug)]] 0.5 µM | C | FIGN activity lowers the cells' numbers under Sulfatinib 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.21× the cells of the other lines | 0.004 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| cells under [[Benproperine (phosphate) (drug)]] 0.05 µM | C | FIGN activity lowers the cells' numbers under Benproperine (phosphate) 0.05 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.17× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| cells under [[Pimozide (drug)]] 0.05 µM | C | FIGN activity lowers the cells' numbers under Pimozide 0.05 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.17× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| cells under [[Menadione (drug)]] 0.5 µM | C | FIGN activity lowers the cells' numbers under Menadione 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.16× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| cells under [[Mozavaptan (drug)]] 0.5 µM | C | FIGN activity lowers the cells' numbers under Mozavaptan 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.25× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| cells under [[Penfluridol (drug)]] 5 µM | C | FIGN activity lowers the cells' numbers under Penfluridol 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.18× the cells of the other lines | 0.009 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| cells under [[Bortezomib (drug)]] 5 µM | C | FIGN activity lowers the cells' numbers under Bortezomib 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.69× the cells of the other lines | 0.009 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | FIGN activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.23× the cells of the other lines | 0.010 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| cells under [[Vismodegib (drug)]] 5 µM | C | FIGN activity lowers the cells' numbers under Vismodegib 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.30× the cells of the other lines | 0.011 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.504). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.3, 31.4); signed map (47.8, 19.9). **Vector** length 110, 32.5% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +10.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.9 | +10.8 |
|  | [[NG25 (drug)]] 5 µM |  | +4.3 | +5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.3 | +12.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.4 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +5.3 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.3 | -2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -4.0 | -3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.7 | -4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.3 | -4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | fidgetin, microtubule severing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.3 — chr2:163,593,396-163,736,012 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | AAA ATPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5HY92](https://www.uniprot.org/uniprotkb/Q5HY92) (Fidgetin):

> ATP-dependent microtubule severing protein. Severs microtubules along their length and depolymerizes their ends, primarily the minus-end, that may lead to the suppression of microtubule growth from and attachment to centrosomes. Microtubule severing may promote rapid reorganization of cellular microtubule arrays and the release of microtubules from the centrosome following nucleation. Microtubule release from the mitotic spindle poles may allow depolymerization of the microtubule end proximal …

**Summary**, from NCBI Gene [55137](https://www.ncbi.nlm.nih.gov/gene/55137):

> Predicted to enable ATP hydrolysis activity and microtubule severing ATPase activity. Predicted to be involved in microtubule severing. Predicted to be located in nuclear matrix. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13285](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13285) · Entrez [55137](https://www.ncbi.nlm.nih.gov/gene/55137) · UniProt [Q5HY92](https://www.uniprot.org/uniprotkb/Q5HY92) · Ensembl [ENSG00000182263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182263)

## Data

Gene col 11267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11267); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11267]; `tensor/DDL_lfc|DDL_z.npy` [11267]; `embed/gene_vectors.npy` [11267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11267 or target_col == 11267). Every well: [[FIGN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FIGN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
