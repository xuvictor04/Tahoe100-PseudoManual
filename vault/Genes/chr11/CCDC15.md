---
symbol: "CCDC15"
type: "gene"
col: 7386
ensembl_id: "ENSG00000149548"
name: "coiled-coil domain containing 15"
location: "11q24.2"
module: 6
arm: "+"
pooled_cpm: 18.86
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CCDC15

*coiled-coil domain containing 15* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +15.6, q 0e+00, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.481× (z -12.7, q 5e-34, down in 32 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.485× (z -12.6, q 1e-33, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EME1]] (+0.64, fdr 7e-06), [[BRCA2]] (+0.64, fdr 7e-06), [[C1orf112]] (+0.63, fdr 7e-06); moves opposite to [[HDHD3]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC37A2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7386.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +15.6 | 0e+00 | 35/44 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.14×** | +12.6 | 4e-34 | 34/45 (SW480, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.90×** | +11.1 | 1e-26 | 35/47 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.65×** | +8.7 | 6e-16 | 31/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.56×** | +7.7 | 2e-12 | 29/47 (NCI-H23, KATO III, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.53×** | +7.1 | 1e-10 | 25/45 (SW480, SW1417, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.35×** | +5.2 | 1e-05 | 20/46 (SNU-423, C32, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.32×** | +4.6 | 3e-04 | 13/46 (RKO, HOP62, …) | all doses, stronger at high dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.30×** | +4.2 | 0.001 | 9/45 (KATO III, NCI-H460, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.29×** | +4.1 | 0.002 | 9/46 (RKO, NCI-H460, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.27×** | +4.0 | 0.004 | 12/46 (SNU-423, SW480, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.004 | 10/47 (SNU-423, NCI-H2030, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.005 | 11/47 (A-172, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.005 | 15/47 (KATO III, SW480, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.24×** | +3.7 | 0.009 | 7/47 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7386.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.481×** | -12.7 | 5e-34 | 32/45 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.485×** | -12.6 | 1e-33 | 35/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.498×** | -12.1 | 2e-31 | 34/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.483×** | -11.9 | 2e-30 | 33/45 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.551×** | -10.3 | 5e-23 | 28/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.580×** | -9.4 | 3e-19 | 29/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.602×** | -8.8 | 1e-16 | 28/47 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.385×** | -8.6 | 4e-16 | 28/44 (NCI-H2030, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.613×** | -8.1 | 2e-14 | 21/40 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.503×** | -6.2 | 3e-08 | 20/46 (PANC-1, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.556×** | -5.3 | 6e-06 | 17/36 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.739×** | -5.2 | 8e-06 | 23/47 (C-33 A, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.750×** | -5.0 | 3e-05 | 16/46 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.818×** | -4.9 | 3e-05 | 17/46 (LOX-IMVI, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.694×** | -4.5 | 2e-04 | 12/47 (A-172, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.845× | -4.1 | 0.001 | 12/47 (CFPAC-1, A-427, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.689×** | -3.4 | 0.023 | 8/44 (Hs 766T, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.827×** | -3.3 | 0.030 | 10/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7386. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.9 | 0 | 11 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -18.7) |
| [[NCI-H460 (line)]] | wt | 16.0 | 0 | 10 (5 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0816× (z -18.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.181× (z -12.9) |
| [[SW480 (line)]] | alt | 16.7 | 3 (2 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +11.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -13.0) |
| [[A-172 (line)]] | wt | 28.9 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +24.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 13.5× (z +15.1) | — |
| [[KATO III (line)]] | alt | 28.6 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.0592× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 22.0 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.209× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -8.7) |
| [[SW1417 (line)]] | alt | 16.4 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.275× (z -8.9) |
| [[Hs 766T (line)]] | wt | 61.8 | 0 | 3 (2 ⚠) | — | [[EX229 (drug)]] 5 µM 0.0468× (z -11.9) |
| [[HS-578T (line)]] | alt | 19.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +17.7) ⚠ cell-cycle shift, explains ~0% of this change | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0707× (z -9.3) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 36.9 | 0 | 3 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.366× (z -20.5) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.264× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 20.0 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.234× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 16.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0767× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 7.54 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.201× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 13.3 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Selinexor (drug)]] 5 µM 0.305× (z -8.7) |
| [[A-427 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 4.88 | 0 | 1 | — | [[Riluzole hydrochloride (drug)]] 0.5 µM 0.0625× (z -8.7) |
| [[COLO 205 (line)]] | alt | 18.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.144× (z -9.2) |
| [[H4 (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0853× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 7.21 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.2× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.142× (z -10.3) |
| [[RKO (line)]] | wt | 14.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 24.8 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.216× (z -9.2) |
| [[SNU-423 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +18.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7386), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EME1]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[BRCA2]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[C1orf112]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[REXO5]] | +0.63 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[CIP2A]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[VRK1]] | +0.61 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[ZWILCH]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[GPR19]] | +0.61 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[ESCO2]] | +0.61 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[PSMC3IP]] | +0.60 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[KNTC1]] | +0.60 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[ZGRF1]] | +0.60 | +0.50 / +0.67 | both halves | 1e-05 | STRING 402 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDHD3]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC37A2]] | B | SLC37A2 activity raises CCDC15's level | lines that do not express SLC37A2 (11) vs lines expressing it (39) | 2.36× lower at baseline in the lines without SLC37A2 | 0.007 | ⚠ within organs, on part of the lines; also absent: FAM111B; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CCDC15's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.518). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-40.5, -47.9); signed map (-43.5, -47.8). **Vector** length 92.2, 20.9% of its response variance represented; |z| ≥ 3 in 1,292 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +15.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.2 | +7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.7 | +12.6 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +2.5 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.5 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +0.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.7 | +4.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -5.6 | -11.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.1 | -12.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.8 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -8.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.2 | -5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -8.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:124,954,121-125,041,489 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13215 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0P6D6](https://www.uniprot.org/uniprotkb/Q0P6D6) (Coiled-coil domain-containing protein 15):

> Plays an important role in primary cilium assembly, maintenance, and length regulation. Interacts with centriole inner scaffold proteins to promote proper centriole size and integrity and assembly of functional cilia. Required for the recruitment of both the inner scaffold protein POC1B and the distal SFI1/CETN2 complex to centrioles.

**Summary**, from NCBI Gene [80071](https://www.ncbi.nlm.nih.gov/gene/80071):

> Involved in cilium assembly and positive regulation of centriole elongation. Located in centriole and centrosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25798](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25798) · Entrez [80071](https://www.ncbi.nlm.nih.gov/gene/80071) · UniProt [Q0P6D6](https://www.uniprot.org/uniprotkb/Q0P6D6) · Ensembl [ENSG00000149548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149548)

## Data

Gene col 7386: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7386); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7386, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7386]; `tensor/DDL_lfc|DDL_z.npy` [7386]; `embed/gene_vectors.npy` [7386]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7386 or target_col == 7386). Every well: [[CCDC15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
