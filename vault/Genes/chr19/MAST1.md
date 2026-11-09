---
symbol: "MAST1"
type: "gene"
col: 2627
ensembl_id: "ENSG00000105613"
name: "microtubule associated serine/threonine kinase 1"
location: "19p13.13"
module: 100
arm: "+"
pooled_cpm: 8.46
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 34
n_dd_up_clean: 16
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 12
direction_downstream: 16
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# MAST1

*microtubule associated serine/threonine kinase 1* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.73× (z +20.8, q 0e+00, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.572× (z -8.2, q 9e-14, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRTN]] (+0.72, fdr 7e-06), [[MAPT]] (+0.72, fdr 1e-05), [[AHDC1]] (+0.71, fdr 1e-05); moves opposite to [[ENOX2]] (-0.67, fdr 3e-05), [[SPRY3]] (-0.66, fdr 2e-05), [[CRPPA]] (-0.64, fdr 1e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); 16 go from it, the strongest it → cells under [[Vismodegib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2627.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.73×** | +20.8 | 0e+00 | 41/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.36×** | +17.8 | 0e+00 | 38/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.33×** | +17.7 | 0e+00 | 38/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.92×** | +15.8 | 0e+00 | 39/46 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.89×** | +15.6 | 0e+00 | 40/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.75×** | +14.9 | 0e+00 | 40/45 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +10.6 | 3e-24 | 23/43 (HS-578T, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.92×** | +9.6 | 5e-20 | 27/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.96×** | +8.3 | 5e-15 | 28/46 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +6.3 | 2e-08 | 21/46 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.47×** | +5.7 | 6e-07 | 18/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +5.1 | 2e-05 | 17/45 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.56×** | +4.6 | 2e-04 | 7/46 (SW480, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.002 | 9/45 (hTERT-HPNE, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.005 | 11/46 (RKO, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2627.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.572×** | -8.2 | 9e-14 | 27/46 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -8.2 | 9e-14 | 22/44 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.584×** | -7.9 | 6e-13 | 28/46 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.602×** | -7.4 | 1e-11 | 20/46 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.600×** | -7.2 | 7e-11 | 22/45 (SNU-423, SW 900, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -6.2 | 6e-08 | 17/35 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.750×** | -5.9 | 2e-07 | 21/47 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.673×** | -5.8 | 5e-07 | 21/45 (NCI-H23, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.672×** | -5.6 | 1e-06 | 17/43 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.688×** | -5.5 | 2e-06 | 12/46 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -5.1 | 2e-05 | 18/42 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.709×** | -5.0 | 2e-05 | 20/45 (NCI-H2030, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.549×** | -4.6 | 2e-04 | 11/46 (MIA PaCa-2, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.727×** | -4.5 | 3e-04 | 16/46 (MIA PaCa-2, C-33 A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.557×** | -4.5 | 3e-04 | 13/45 (A-172, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.752×** | -4.2 | 1e-03 | 11/45 (SW 1271, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.818×** | -4.1 | 0.001 | 19/46 (LOX-IMVI, SNU-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2627. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.1 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0937× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 3.10 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.142× (z -10.4) |
| [[C32 (line)]] | wt | 6.26 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +9.6) | [[Brimonidine (drug)]] 0.5 µM 0.0629× (z -10.3) |
| [[CHP-212 (line)]] | wt | 25.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0581× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[venetoclax (drug)]] 0.05 µM 0.0688× (z -8.5) |
| [[LoVo (line)]] | wt | 9.56 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +12.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.238× (z -8.9) |
| [[SW 900 (line)]] | alt | 6.10 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0424× (z -10.8) |
| [[SW480 (line)]] | alt | 7.72 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.70× (z +9.0) | — |
| [[A-427 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 4.55 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0814× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 3.21 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.88× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 5.19 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.26× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 8.11 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0705× (z -9.4) |
| [[HS-578T (line)]] | alt | 7.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +15.8) | — |
| [[LOX-IMVI (line)]] | wt | 9.11 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0628× (z -13.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 2.27 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 10.4× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -10.0) |
| [[PANC-1 (line)]] | alt | 6.54 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 4.95 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0354× (z -11.1) |
| [[SW48 (line)]] | wt | 12.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +10.4) | — |
| [[A549 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2627), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRTN]] | +0.72 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[MAPT]] | +0.72 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.71 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.69 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[CAMKK1]] | +0.69 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[SH3PXD2B]] | +0.68 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[SEPTIN6]] | +0.67 | +0.53 / +0.60 | both halves | 1e-05 | same gene group |
| [[CCDC112]] | +0.67 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[CFD]] | +0.65 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[CCDC88B]] | +0.65 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[ATP1A3]] | +0.65 | +0.38 / +0.62 | both halves | 7e-05 |  |
| [[TNNT1]] | +0.64 | +0.42 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | -0.67 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[SPRY3]] | -0.66 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[CRPPA]] | -0.64 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[NIPAL2]] | -0.64 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[DECR1]] | -0.62 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[AVEN]] | -0.62 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[ATR]] | -0.59 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[TOR1A]] | -0.59 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ALG8]] | -0.58 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[MSANTD2]] | -0.57 | -0.54 / -0.28 | both halves | 3e-04 |  |
| [[RXYLT1]] | -0.57 | -0.37 / -0.24 | both halves | 4e-04 |  |
| [[PRDM5]] | -0.57 | -0.39 / -0.42 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises MAST1's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without SEMA6B | 0.008 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[SH3GL3]] | B | SH3GL3 activity lowers MAST1's level | lines that do not express SH3GL3 (21) vs lines expressing it (29) | 1.20× higher at baseline in the lines without SH3GL3 | 0.019 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |
| [[SLC17A7]] | B | SLC17A7 activity raises MAST1's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 2.38× lower at baseline in the lines without SLC17A7 | 0.042 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[SLC29A4]] | B | SLC29A4 activity raises MAST1's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 2.51× lower at baseline in the lines without SLC29A4 | 0.055 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises MAST1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01518]] | B | LINC01518 activity raises MAST1's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 2.28× lower at baseline in the lines without LINC01518 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2 |
| [[TLE2]] | B | TLE2 activity raises MAST1's level | lines that do not express TLE2 (10) vs lines expressing it (40) | 2.10× lower at baseline in the lines without TLE2 | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KREMEN2]] | B | KREMEN2 activity raises MAST1's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 2.05× lower at baseline in the lines without KREMEN2 | 0.067 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[ADGRB2]] | B | ADGRB2 activity raises MAST1's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without ADGRB2 | 0.068 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[KIF1A]] | B | KIF1A activity raises MAST1's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.12× lower at baseline in the lines without KIF1A | 0.081 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[TSPAN33]] | B | TSPAN33 activity raises MAST1's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without TSPAN33 | 0.083 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[SFXN3]] | C | SFXN3 activity lowers MAST1's level | lines that do not express SFXN3 (3) vs lines expressing it (47) | 3.27× higher at baseline in the lines without SFXN3 | 0.072 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, GULP1, SMAD7 |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Vismodegib (drug)]] 5 µM | C | MAST1's natural level raises the cells' numbers under Vismodegib 5 µM (protects the cells) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.76 | 0.162 over the table, 0.002 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Glasdegib (drug)]] 5 µM | C | MAST1's natural level raises the cells' numbers under Glasdegib 5 µM (protects the cells) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.70 | 0.271 over the table, 0.052 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Neratinib (drug)]] 0.05 µM | C | MAST1's natural level raises the cells' numbers under Neratinib 0.05 µM (protects the cells) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.69 | 0.285 over the table, 0.059 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Rucaparib (phosphate) (drug)]] 5 µM | C | MAST1's natural level lowers the cells' numbers under Rucaparib (phosphate) 5 µM (makes them more sensitive) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.285 over the table, 0.076 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Sulfatinib (drug)]] 5 µM | C | MAST1's natural level lowers the cells' numbers under Sulfatinib 5 µM (makes them more sensitive) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.285 over the table, 0.040 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Penfluridol (drug)]] 5 µM | C | MAST1's natural level raises the cells' numbers under Penfluridol 5 µM (protects the cells) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.69 | 0.285 over the table, 0.082 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Piroxicam (drug)]] 0.05 µM | C | MAST1's natural level lowers the cells' numbers under Piroxicam 0.05 µM (makes them more sensitive) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.305 over the table, 0.055 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Citalopram (hydrobromide) (drug)]] 0.05 µM | C | MAST1's natural level lowers the cells' numbers under Citalopram (hydrobromide) 0.05 µM (makes them more sensitive) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.310 over the table, 0.047 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Digitoxin (drug)]] 0.05 µM | C | MAST1's natural level raises the cells' numbers under Digitoxin 0.05 µM (protects the cells) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.310 over the table, 0.062 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Hydroxyurea (drug)]] 0.5 µM | C | MAST1's natural level raises the cells' numbers under Hydroxyurea 0.5 µM (protects the cells) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.344 over the table, 0.078 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Imiquimod (hydrochloride) (drug)]] 0.05 µM | C | MAST1's natural level raises the cells' numbers under Imiquimod (hydrochloride) 0.05 µM (protects the cells) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.351 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Canagliflozin (drug)]] 5 µM | C | MAST1's natural level raises the cells' numbers under Canagliflozin 5 µM (protects the cells) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.360 over the table, 0.048 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.3, -1.5); signed map (-27.4, 22.1). **Vector** length 93.3, 19.7% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +20.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.0 | +14.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.7 | +15.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.7 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.4 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.3 | +5.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +3.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -7.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | -8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated serine/threonine kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,833,951-12,874,952 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAST, KIAA0973 |
| Gene groups (HGNC) | PDZ domain containing; MicroRNA protein coding host genes; Microtubule associated serine/threonine kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2H9](https://www.uniprot.org/uniprotkb/Q9Y2H9) (Microtubule-associated serine/threonine-protein kinase 1):

> Microtubule-associated protein essential for correct brain development. Appears to link the dystrophin/utrophin network with microtubule filaments via the syntrophins. Phosphorylation of DMD or UTRN may modulate their affinities for associated proteins (By similarity).

**Summary**, from NCBI Gene [22983](https://www.ncbi.nlm.nih.gov/gene/22983):

> This gene is a member of the microtubule-associated serine/threonine kinase (MAST) family. The protein encoded by this gene has an N-terminal serine/threonine kinase domain followed by a postsynaptic density protein-95/discs large/zona occludens-1 (PDZ) domain. In mouse and rat, the orthologous protein associates with the cytoskeleton and can bind both beta-2-syntrophin and neuronal nitric oxide synthase (nNOS) through its PDZ domain. In mouse and rat, this protein also co-localizes with …

**Accessions** — [HGNC:19034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19034) · Entrez [22983](https://www.ncbi.nlm.nih.gov/gene/22983) · UniProt [Q9Y2H9](https://www.uniprot.org/uniprotkb/Q9Y2H9) · Ensembl [ENSG00000105613](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105613)

## Data

Gene col 2627: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2627); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2627, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2627]; `tensor/DDL_lfc|DDL_z.npy` [2627]; `embed/gene_vectors.npy` [2627]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2627 or target_col == 2627). Every well: [[MAST1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAST1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
