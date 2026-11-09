---
symbol: "NCS1"
type: "gene"
col: 2827
ensembl_id: "ENSG00000107130"
name: "neuronal calcium sensor 1"
location: "9q34.11"
module: 18
arm: "+"
pooled_cpm: 24.1
n_lines_expressing: 44
n_dd_up: 37
n_dd_down: 3
n_dd_up_clean: 27
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 31
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# NCS1

*neuronal calcium sensor 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.41× (z +13.0, q 8e-36, up in 35 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.27× (z +12.1, q 3e-31, up in 36 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.609× (z -7.4, q 1e-10, down in 26 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSI1]] (+0.57, fdr 2e-05), [[TMEM64]] (+0.56, fdr 2e-05), [[SPTBN2]] (+0.56, fdr 2e-05); moves opposite to [[KDM5A]] (-0.54, fdr 1e-05), [[KIAA0319L]] (-0.52, fdr 4e-05), [[USP8]] (-0.50, fdr 5e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GAS6]] → it (grade B ⚠); 31 go from it, the strongest it → [[NCLN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2827.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +13.0 | 8e-36 | 35/40 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.27×** | +12.1 | 3e-31 | 36/42 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.00×** | +10.2 | 3e-22 | 37/41 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +9.7 | 3e-20 | 19/27 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.87×** | +9.2 | 3e-18 | 32/41 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.86×** | +9.1 | 6e-18 | 33/41 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +8.6 | 4e-16 | 31/41 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +7.8 | 4e-13 | 29/39 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +7.5 | 6e-12 | 21/37 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +6.9 | 3e-10 | 23/41 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +6.5 | 6e-09 | 22/42 (SNU-423, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +5.8 | 3e-07 | 20/42 (BT-474, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.03×** | +5.4 | 2e-06 | 23/39 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.43×** | +5.3 | 6e-06 | 19/41 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +5.0 | 2e-05 | 19/42 (NCI-H460, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.38×** | +4.7 | 7e-05 | 20/42 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +4.6 | 1e-04 | 16/41 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 5e-04 | 17/40 (SK-MEL-2, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +4.3 | 5e-04 | 19/42 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **1.73×** | +4.2 | 7e-04 | 16/39 (A498, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.49×** | +4.2 | 8e-04 | 14/42 (NCI-H460, RPMI-7951, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2827.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.609×** | -7.4 | 1e-10 | 26/42 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -7.2 | 1e-10 | 23/41 (MIA PaCa-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.618×** | -7.1 | 2e-10 | 24/42 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.802× | -3.3 | 0.12 | 10/41 (HOP62, SK-MEL-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.802× | -3.3 | 0.12 | 18/41 (SW48, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | 0.673× | -3.1 | 0.17 | 12/39 (H4, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.749× | -3.1 | 0.17 | 13/40 (HEC-1-A, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.3 | 9 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.28× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.90× (z +15.0) | — |
| [[HOP62 (line)]] | alt | 24.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.78× (z +11.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 54.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -13.6) |
| [[RKO (line)]] | wt | 106 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.365× (z -10.5) |
| [[SW480 (line)]] | alt | 15.2 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.65× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.88× (z +11.8) | — |
| [[J82 (line)]] | alt | 49.2 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 15.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 51.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.162× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 26.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 8.51 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0587× (z -12.5) |
| [[SNU-423 (line)]] | alt | 35.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +10.8) | — |
| [[A498 (line)]] | wt | 68.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -11.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 35.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.173× (z -9.3) |
| [[HS-578T (line)]] | alt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +8.6) | — |
| [[LoVo (line)]] | wt | 16.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.99× (z +9.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 34.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -12.4) |
| [[SNU-1 (line)]] | wt | 42.2 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.350× (z -8.7) |
| [[A-172 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSI1]] | +0.57 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[TMEM64]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[SPTBN2]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[RBPMS2]] | +0.55 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[MTA1]] | +0.55 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[MAPK12]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[AGPAT3]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[ADCY3]] | +0.53 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[CPNE7]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[MAPKAPK3]] | +0.53 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[MACROD1]] | +0.52 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[PSEN2]] | +0.52 | +0.47 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM5A]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[KIAA0319L]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[USP8]] | -0.50 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[MMUT]] | -0.50 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[CRNKL1]] | -0.50 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[ERCC5]] | -0.49 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[GOLGB1]] | -0.49 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[RSPRY1]] | -0.48 | -0.53 / -0.49 | both halves | 2e-05 |  |
| [[TOX4]] | -0.48 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[SENP2]] | -0.48 | -0.56 / -0.29 | both halves | 3e-04 |  |
| [[ASB8]] | -0.47 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[YIPF5]] | -0.47 | -0.47 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAS6]] | B | GAS6 activity raises NCS1's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.94× lower at baseline in the lines without GAS6 | 0.046 | ⚠ within organs, on part of the lines |
| [[PARD6G]] | B | PARD6G activity raises NCS1's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.59× lower at baseline in the lines without PARD6G | 0.047 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[LRP3]] | B | LRP3 activity raises NCS1's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 2.59× lower at baseline in the lines without LRP3 | 0.055 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[LAMC3]] | B | LAMC3 activity raises NCS1's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.61× lower at baseline in the lines without LAMC3 | 0.085 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[ADAMTS7]] | B | ADAMTS7 activity raises NCS1's level | lines that do not express ADAMTS7 (17) vs lines expressing it (33) | 1.91× lower at baseline in the lines without ADAMTS7 | 0.093 | ⚠ within organs, on part of the lines; also absent: VASH1, FHL1, ANTXR1; maybe low, not absent |
| [[PPARGC1B]] | C | PPARGC1B activity raises NCS1's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 5.21× lower at baseline in the lines without PPARGC1B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 29, C 2. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCLN]] | B | NCS1 activity raises NCLN's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.05× lower at baseline in the lines without NCS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[MRPS25]] | B | NCS1 activity raises MRPS25's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.00× lower at baseline in the lines without NCS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[NDST1]] | B | NCS1 activity raises NDST1's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.50× lower at baseline in the lines without NCS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[GAS6]] | B | NCS1 activity raises GAS6's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.94× lower at baseline in the lines without NCS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[CARM1]] | B | NCS1 activity raises CARM1's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.63× lower at baseline in the lines without NCS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[ADCY3]] | B | NCS1 activity raises ADCY3's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.88× lower at baseline in the lines without NCS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[MAPK12]] | B | NCS1 activity raises MAPK12's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.15× lower at baseline in the lines without NCS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[LIMK1]] | B | NCS1 activity raises LIMK1's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.83× lower at baseline in the lines without NCS1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[PUS7]] | B | NCS1 activity raises PUS7's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without NCS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[TMEM64]] | B | NCS1 activity raises TMEM64's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.41× lower at baseline in the lines without NCS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[XPO5]] | B | NCS1 activity raises XPO5's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without NCS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[GARNL3]] | B | NCS1 activity raises GARNL3's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 3.07× lower at baseline in the lines without NCS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.0, -28.5); signed map (2.8, -56.3). **Vector** length 95.1, 22.6% of its response variance represented; |z| ≥ 3 in 1,018 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.6 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.5 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | +8.1 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +10.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.5 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +6.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.6 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | -0.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +4.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | +5.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -1.7 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.5 | -0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | neuronal calcium sensor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:130,172,404-130,237,303 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NCS-1; previously FREQ |
| Gene groups (HGNC) | EF-hand domain containing |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [P62166](https://www.uniprot.org/uniprotkb/P62166) (Neuronal calcium sensor 1):

> Neuronal calcium sensor, regulator of G protein-coupled receptor phosphorylation in a calcium dependent manner. Directly regulates GRK1 (RHOK), but not GRK2 to GRK5. Can substitute for calmodulin (By similarity). Stimulates PI4KB kinase activity (By similarity). Involved in long-term synaptic plasticity through its interaction with PICK1 (By similarity). May also play a role in neuron differentiation through inhibition of the activity of N-type voltage-gated calcium channel (By similarity).

**Summary**, from NCBI Gene [23413](https://www.ncbi.nlm.nih.gov/gene/23413):

> This gene is a member of the neuronal calcium sensor gene family, which encode calcium-binding proteins expressed predominantly in neurons. The protein encoded by this gene regulates G protein-coupled receptor phosphorylation in a calcium-dependent manner and can substitute for calmodulin. The protein is associated with secretory granules and modulates synaptic transmission and synaptic plasticity. Multiple transcript variants encoding different isoforms have been found for this gene. [provided …

**Accessions** — [HGNC:3953](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3953) · Entrez [23413](https://www.ncbi.nlm.nih.gov/gene/23413) · UniProt [P62166](https://www.uniprot.org/uniprotkb/P62166) · Ensembl [ENSG00000107130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107130)

## Data

Gene col 2827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2827); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2827]; `tensor/DDL_lfc|DDL_z.npy` [2827]; `embed/gene_vectors.npy` [2827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2827 or target_col == 2827). Every well: [[NCS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
