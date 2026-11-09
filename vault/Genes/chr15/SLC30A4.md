---
symbol: "SLC30A4"
type: "gene"
col: 2422
ensembl_id: "ENSG00000104154"
name: "solute carrier family 30 member 4"
location: "15q21.1"
module: 14
arm: "+"
pooled_cpm: 11.92
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SLC30A4

*solute carrier family 30 member 4* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.83× (z +11.5, q 5e-28, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.850× (z -10.5, q 4e-23, down in 21 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.708× (z -6.5, q 2e-08, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC41A2]] (+0.65, fdr 7e-06), [[ELOVL7]] (+0.65, fdr 7e-06), [[GRHL1]] (+0.63, fdr 1e-05); moves opposite to [[COX10]] (-0.58, fdr 3e-05), [[POLR1A]] (-0.55, fdr 1e-05), [[FARS2]] (-0.53, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[APH1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2422.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +11.5 | 5e-28 | 31/47 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.73×** | +10.4 | 4e-23 | 30/48 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +10.4 | 6e-23 | 33/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +9.5 | 3e-19 | 24/45 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +8.6 | 7e-16 | 25/48 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +8.5 | 2e-15 | 26/48 (HOP62, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +7.4 | 1e-11 | 9/22 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +7.2 | 3e-11 | 19/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +7.0 | 2e-10 | 16/35 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +5.3 | 6e-06 | 11/48 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +4.9 | 5e-05 | 13/47 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +4.7 | 1e-04 | 14/41 (NCI-H2347, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +4.7 | 1e-04 | 12/48 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +4.6 | 1e-04 | 10/46 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.27×** | +4.4 | 5e-04 | 13/48 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.002 | 12/46 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +4.0 | 0.002 | 8/48 (NCI-H2030, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.004 | 2/48 (RKO, LoVo) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.19× | +3.8 | 0.005 | 5/48 (LoVo, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2422.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.850× | -10.5 | 4e-23 | 21/48 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.708×** | -6.5 | 2e-08 | 22/47 (LOX-IMVI, SNU-1, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.778×** | -4.7 | 4e-04 | 15/47 (SNU-1, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.627×** | -4.6 | 5e-04 | 15/45 (A-427, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.792×** | -4.4 | 0.001 | 16/45 (NCI-H2030, J82, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.797×** | -4.3 | 0.002 | 15/48 (PANC-1, HT-29, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2422. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 2 | — | [[Allantoin (drug)]] 0.5 µM 0.0901× (z -13.1) |
| [[A-427 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 5.67 | 0 | 1 | — | [[Nevirapine (drug)]] 0.05 µM 0.0653× (z -9.8) |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.117× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 8.56 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.163× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0982× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.185× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.111× (z -8.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2422), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC41A2]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ELOVL7]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[GRHL1]] | +0.63 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[OPTN]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[BTG1-DT]] | +0.58 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CPAMD8]] | +0.58 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[RTN4RL2]] | +0.58 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[PINK1]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[CRTAC1]] | +0.56 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[RGS9]] | +0.56 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[RAB8B]] | +0.56 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[C15orf48]] | +0.55 | +0.53 / +0.46 | both halves | 3e-05 | ⚠ same locus (30.8 kb: neighbours can correlate without regulation) |
| [[TMOD1]] | +0.54 | +0.34 / +0.54 | both halves | 1e-04 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX10]] | -0.58 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[POLR1A]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[FARS2]] | -0.53 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[NOL11]] | -0.53 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[NAT10]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[EIPR1]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[KLHDC4]] | -0.52 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[WDR4]] | -0.51 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[ALG8]] | -0.51 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[TBRG4]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[BYSL]] | -0.50 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[ARMC6]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APH1B]] | B | APH1B activity raises SLC30A4's level | lines that do not express APH1B (6) vs lines expressing it (44) | 1.66× lower at baseline in the lines without APH1B | 0.011 | ⚠ within organs, on part of the lines; also absent: PER3, DLG4, CCDC3 |
| [[HOTAIRM1]] | B | HOTAIRM1 activity raises SLC30A4's level | lines that do not express HOTAIRM1 (14) vs lines expressing it (36) | 1.25× lower at baseline in the lines without HOTAIRM1 | 0.052 | ⚠ within organs, on part of the lines; also absent: GXYLT2, HOXA5, SOBP |
| [[TMCC2]] | B | TMCC2 activity raises SLC30A4's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 1.57× lower at baseline in the lines without TMCC2 | 0.072 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.362). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.1, -0.3); signed map (39.9, 9.9). **Vector** length 60.6, 8.50% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +4.9 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.6 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -4.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.4 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 30 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:45,479,606-45,522,755 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZNT4 |
| Gene groups (HGNC) | Solute carrier family 30 |
| Matched by | ensembl_id |

**Function**, from UniProt [O14863](https://www.uniprot.org/uniprotkb/O14863) (Probable proton-coupled zinc antiporter SLC30A4):

> Probable proton-coupled zinc ion antiporter mediating zinc import from cytoplasm potentially into the endocytic compartment. Controls zinc deposition in milk (By similarity).

**Summary**, from NCBI Gene [7782](https://www.ncbi.nlm.nih.gov/gene/7782):

> Zinc is the second most abundant trace metal in the human body. It is an essential element, serving both a structural role, as in the formation of zinc fingers in DNA-binding proteins, and a catalytic role in metalloenzymes, such as pancreatic carboxypeptidases (e.g., MIM 114852), alkaline phosphatases (e.g., MIM 171760), various dehydrogenases, and superoxide dismutases (e.g., MIM 147450). SLC30A4, or ZNT4, belongs to the ZNT family of zinc transporters. ZNTs are involved in transporting zinc …

**Accessions** — [HGNC:11015](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11015) · Entrez [7782](https://www.ncbi.nlm.nih.gov/gene/7782) · UniProt [O14863](https://www.uniprot.org/uniprotkb/O14863) · Ensembl [ENSG00000104154](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104154)

## Data

Gene col 2422: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2422); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2422, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2422]; `tensor/DDL_lfc|DDL_z.npy` [2422]; `embed/gene_vectors.npy` [2422]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2422 or target_col == 2422). Every well: [[SLC30A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC30A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
