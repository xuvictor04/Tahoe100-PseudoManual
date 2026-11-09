---
symbol: "LGALS9"
type: "gene"
col: 9732
ensembl_id: "ENSG00000168961"
name: "galectin 9"
location: "17q11.2"
module: 32
arm: "+"
pooled_cpm: 8.03
n_lines_expressing: 37
n_dd_up: 14
n_dd_down: 22
n_dd_up_clean: 12
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 66
direction_downstream: 37
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# LGALS9

*galectin 9* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.95× (z +6.4, q 8e-08, up in 1 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 1.48× (z +4.6, q 0.001, up in 15 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.436× (z -8.3, q 7e-14, down in 24 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO39]] (+0.76, fdr 7e-06), [[TNFSF10]] (+0.75, fdr 7e-06), [[OAS1]] (+0.75, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 66 arrows point to it, the strongest [[ITGB6]] → it (grade B ⚠); 37 go from it, the strongest it → [[SEC16B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9732.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +6.4 | 8e-08 | 1/11 (NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.48×** | +4.6 | 0.001 | 15/30 (AsPC-1, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.011 | 17/32 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.011 | 9/32 (LS 180, HepG2/C3A, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.018 | 7/25 (SW1417, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.021 | 14/33 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.029 | 15/31 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.42×** | +3.3 | 0.064 | 8/31 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.064 | 8/32 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.077 | 11/28 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.086 | 0/32 | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.086 | 8/21 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.094 | 8/32 (NCI-H1792, Hs 766T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.0 | 0.094 | 3/22 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9732.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.436×** | -8.3 | 7e-14 | 24/33 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.593×** | -7.4 | 4e-11 | 19/32 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.499×** | -6.9 | 7e-10 | 19/27 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.502×** | -6.9 | 8e-10 | 20/29 (KATO III, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.512×** | -6.4 | 1e-08 | 17/29 (SW480, AsPC-1, …) | top dose only | cell-cycle shift (explains ~25% here); composition shift |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.530×** | -6.3 | 2e-08 | 18/31 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.672×** | -5.6 | 2e-06 | 17/32 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.572×** | -5.6 | 2e-06 | 18/32 (CFPAC-1, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.589×** | -5.3 | 8e-06 | 20/30 (AsPC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.420×** | -4.5 | 3e-04 | 17/27 (KATO III, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.643×** | -4.4 | 5e-04 | 17/30 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.734×** | -4.4 | 6e-04 | 15/32 (AsPC-1, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.660×** | -4.1 | 0.001 | 13/30 (BT-474, AsPC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.687×** | -3.7 | 0.007 | 11/32 (AsPC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.693×** | -3.5 | 0.016 | 7/31 (RPMI-7951, AsPC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.707×** | -3.3 | 0.032 | 10/28 (BT-474, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.722×** | -3.2 | 0.033 | 11/32 (BT-474, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9732. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 74.5 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -19.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0594× (z -10.4) |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0527× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.125× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.199× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0650× (z -11.4) |
| [[COLO 205 (line)]] | alt | 43.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.139× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 37.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -11.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0903× (z -18.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 29.0 | 0 | 3 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.281× (z -10.6) |
| [[HT-29 (line)]] | alt | 6.72 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0812× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.0921× (z -8.7) |
| [[LoVo (line)]] | wt | 9.24 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0602× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 0.5 µM 0.0874× (z -10.8) |
| [[A-172 (line)]] | wt | 8.46 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0662× (z -10.1) |
| [[A-427 (line)]] | wt | 2.56 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0404× (z -9.4) |
| [[LS 180 (line)]] | wt | 9.62 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0686× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 5.15 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 5.15 | 0 | 1 | — | [[Nevirapine (drug)]] 0.5 µM 0.0472× (z -8.7) |
| [[A498 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9732), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO39]] | +0.76 | +0.65 / +0.82 | both halves | 7e-06 |  |
| [[TNFSF10]] | +0.75 | +0.71 / +0.78 | both halves | 7e-06 | STRING 618 |
| [[OAS1]] | +0.75 | +0.65 / +0.81 | both halves | 7e-06 | STRING 463 |
| [[HSH2D]] | +0.75 | +0.72 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[NRIR]] | +0.74 | +0.66 / +0.81 | both halves | 7e-06 |  |
| [[PLSCR1]] | +0.74 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[ETV7]] | +0.73 | +0.55 / +0.82 | both halves | 1e-05 |  |
| [[MX1]] | +0.73 | +0.61 / +0.80 | both halves | 7e-06 | STRING 492 |
| [[OAS2]] | +0.73 | +0.64 / +0.79 | both halves | 7e-06 | STRING 458 |
| [[EPSTI1]] | +0.73 | +0.62 / +0.80 | both halves | 7e-06 |  |
| [[IFI44]] | +0.73 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[CMPK2]] | +0.72 | +0.62 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*66 arrows, 66 of them with an alert ⚠; grade A 0, B 64, C 2. Shown: the 12 strongest; 54 more arrows (54 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB6]] | B | ITGB6 activity raises LGALS9's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 3.48× lower at baseline in the lines without ITGB6 | 8e-04 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[ADGRF1]] | B | ADGRF1 activity raises LGALS9's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.56× lower at baseline in the lines without ADGRF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[WFDC2]] | B | WFDC2 activity raises LGALS9's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 3.66× lower at baseline in the lines without WFDC2 | 0.003 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[MUC5B]] | B | MUC5B activity raises LGALS9's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 3.61× lower at baseline in the lines without MUC5B | 0.004 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[TNFSF10]] | B | TNFSF10 activity raises LGALS9's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 2.83× lower at baseline in the lines without TNFSF10 | 0.004 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[ALOX5]] | B | ALOX5 activity raises LGALS9's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.67× lower at baseline in the lines without ALOX5 | 0.004 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[STEAP4]] | B | STEAP4 activity raises LGALS9's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 3.58× lower at baseline in the lines without STEAP4 | 0.004 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[LCN2]] | B | LCN2 activity raises LGALS9's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 3.13× lower at baseline in the lines without LCN2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[SIDT1]] | B | SIDT1 activity raises LGALS9's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.72× lower at baseline in the lines without SIDT1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[VNN1]] | B | VNN1 activity raises LGALS9's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.53× lower at baseline in the lines without VNN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[SAMD12-AS1]] | B | SAMD12-AS1 activity raises LGALS9's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without SAMD12-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[MMP7]] | B | MMP7 activity raises LGALS9's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.73× lower at baseline in the lines without MMP7 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 36, C 1. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEC16B]] | B | LGALS9 activity raises SEC16B's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.33× lower at baseline in the lines without LGALS9 | 0.008 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[GBP4]] | B | LGALS9 activity raises GBP4's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.77× lower at baseline in the lines without LGALS9 | 0.008 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[DAPK2]] | B | LGALS9 activity raises DAPK2's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.61× lower at baseline in the lines without LGALS9 | 0.012 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[TNFSF10]] | B | LGALS9 activity raises TNFSF10's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 3.73× lower at baseline in the lines without LGALS9 | 0.024 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[EPB41L1]] | B | LGALS9 activity raises EPB41L1's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.66× lower at baseline in the lines without LGALS9 | 0.024 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[GBP1]] | B | LGALS9 activity raises GBP1's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.78× lower at baseline in the lines without LGALS9 | 0.028 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[TC2N]] | B | LGALS9 activity raises TC2N's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 3.49× lower at baseline in the lines without LGALS9 | 0.034 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[ITGB6]] | B | LGALS9 activity raises ITGB6's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 3.64× lower at baseline in the lines without LGALS9 | 0.034 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[PSMB10]] | B | LGALS9 activity strengthens PSMB10's drug response | lines that do not express LGALS9 (13) vs lines expressing it (34) | the lines without LGALS9 respond 0.48× as strongly (z diff +1.82); strongest at Panobinostat 0.5 µM: 0.73x vs 0.29x (z diff +3.6) | 0.036 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IFI27]] | B | LGALS9 activity raises IFI27's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 3.77× lower at baseline in the lines without LGALS9 | 0.037 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[PSMB10]] | B | LGALS9 activity raises PSMB10's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without LGALS9 | 0.040 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[C6orf132]] | B | LGALS9 activity raises C6orf132's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 3.45× lower at baseline in the lines without LGALS9 | 0.040 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.9, 56.5); signed map (67.9, 32.1). **Vector** length 95.6, 25.6% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.60 to 56); *interferon gamma response* (hallmark, mean cos +0.61 to 60); *interferon* (control, mean cos +0.65 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +4.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.3 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +4.6 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -5.0 | -7.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.2 | -5.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.0 | -6.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.0 | -5.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.7 | -6.9 |

## What is on record

|  |  |
|---|---|
| Name | galectin 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:27,629,798-27,649,560 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LGALS9A |
| Gene groups (HGNC) | Receptor ligands; Galectins |
| Reactome | 3 pathways, smallest: Interleukin-2 family signaling; Signaling by Interleukins; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [O00182](https://www.uniprot.org/uniprotkb/O00182) (Galectin-9):

> Binds galactosides. Has high affinity for the Forssman pentasaccharide. Ligand for HAVCR2/TIM3. Binding to HAVCR2 induces T-helper type 1 lymphocyte (Th1) death. Also stimulates bactericidal activity in infected macrophages by causing macrophage activation and IL1B secretion which restricts intracellular bacterial growth (By similarity). Ligand for P4HB; the interaction retains P4HB at the cell surface of Th2 T-helper cells, increasing disulfide reductase activity at the plasma membrane, …

**Summary**, from NCBI Gene [3965](https://www.ncbi.nlm.nih.gov/gene/3965):

> The galectins are a family of beta-galactoside-binding proteins implicated in modulating cell-cell and cell-matrix interactions. The protein encoded by this gene is an S-type lectin. It is overexpressed in Hodgkin's disease tissue and might participate in the interaction between the H&RS cells with their surrounding cells and might thus play a role in the pathogenesis of this disease and/or its associated immunodeficiency. Multiple alternatively spliced transcript variants have been found for …

**Accessions** — [HGNC:6570](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6570) · Entrez [3965](https://www.ncbi.nlm.nih.gov/gene/3965) · UniProt [O00182](https://www.uniprot.org/uniprotkb/O00182) · Ensembl [ENSG00000168961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168961)

## Data

Gene col 9732: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9732); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9732, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9732]; `tensor/DDL_lfc|DDL_z.npy` [9732]; `embed/gene_vectors.npy` [9732]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9732 or target_col == 9732). Every well: [[LGALS9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LGALS9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
