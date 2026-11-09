---
symbol: "NSFL1C"
type: "gene"
col: 1547
ensembl_id: "ENSG00000088833"
name: "NSFL1 cofactor"
location: "20p13"
module: 64
arm: "+"
pooled_cpm: 47.36
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# NSFL1C

*NSFL1 cofactor* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.87× (z +25.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.526× (z -21.9, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB5R1]] (+0.75, fdr 7e-06), [[PSMD3]] (+0.66, fdr 1e-05), [[PSMD6]] (+0.65, fdr 1e-05); moves opposite to [[PHC2-AS1]] (-0.56, fdr 5e-05), [[POC1B-AS1]] (-0.53, fdr 1e-04), [[DGKH]] (-0.52, fdr 2e-04).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1547.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.87×** | +25.4 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.76×** | +24.5 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.58×** | +21.5 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.55×** | +11.8 | 6e-30 | 44/49 (SW480, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.74×** | +9.5 | 3e-19 | 43/49 (PANC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.05×** | +9.1 | 1e-17 | 37/44 (CFPAC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.40×** | +8.0 | 8e-14 | 32/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.32×** | +6.4 | 8e-09 | 25/47 (COLO 205, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.20×** | +6.3 | 2e-08 | 23/48 (LS 180, BT-474, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +6.0 | 1e-07 | 27/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.28×** | +5.6 | 9e-07 | 25/48 (BT-474, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.25×** | +5.4 | 3e-06 | 24/48 (BT-474, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.24×** | +5.2 | 1e-05 | 23/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.22×** | +4.7 | 9e-05 | 21/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.21×** | +4.6 | 1e-04 | 21/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.20×** | +4.2 | 9e-04 | 19/48 (C32, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +4.1 | 0.001 | 16/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.017 | 14/47 (SNU-423, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.060 | 12/48 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.13× | +2.9 | 0.072 | 9/48 (NCI-H23, SNU-423, …) | two highest doses | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | 1.13× | +2.8 | 0.088 | 10/48 (Hs 766T, MIA PaCa-2, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1547.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.526×** | -21.9 | 0e+00 | 46/48 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -9.3 | 5e-18 | 41/48 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -6.5 | 1e-08 | 25/49 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.900× | -3.6 | 0.037 | 13/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.874× | -3.3 | 0.12 | 14/48 (RPMI-7951, HS-578T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.877× | -3.2 | 0.13 | 14/48 (NCI-H2030, NCI-H1573, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.880× | -3.1 | 0.15 | 6/49 (NCI-H23, A-172, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.915× | -3.1 | 0.15 | 4/48 (CFPAC-1, A549, …) | rises with dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 0.884× | -3.0 | 0.16 | 7/48 (CFPAC-1, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1547. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 64.2 | 4 | 3 | [[Ixazomib citrate (drug)]] 0.5 µM 3.26× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -16.8) |
| [[LS 180 (line)]] | wt | 39.4 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.7) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.70× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.0838× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[PANC-1 (line)]] | alt | 41.4 | 6 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.45× (z +15.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -11.0) |
| [[SW480 (line)]] | alt | 49.4 | 4 | 3 | [[Ixazomib citrate (drug)]] 0.5 µM 3.69× (z +17.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -13.8) |
| [[BT-474 (line)]] | alt | 45.5 | 6 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.29× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H460 (line)]] | wt | 49.8 | 3 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 3.10× (z +15.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -12.3) |
| [[A549 (line)]] | wt | 69.3 | 3 | 1 | [[Bortezomib (drug)]] 0.05 µM 2.60× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 41.9 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 44.2 | 3 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.46× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -9.1) |
| [[Hs 766T (line)]] | wt | 41.0 | 3 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.34× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.7) |
| [[HT-29 (line)]] | alt | 34.0 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.55× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -8.5) |
| [[LoVo (line)]] | wt | 32.1 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 4.23× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 31.2 | 3 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.57× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 41.1 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.89× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -15.9) |
| [[RPMI-7951 (line)]] | alt | 75.5 | 3 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.66× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.6) |
| [[SHP-77 (line)]] | alt | 55.8 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.86× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -11.2) |
| [[COLO 205 (line)]] | alt | 57.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.21× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 44.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.68× (z +14.4) | — |
| [[HS-578T (line)]] | alt | 84.4 | 2 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.39× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -10.6) |
| [[KATO III (line)]] | alt | 59.0 | 2 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.76× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 26.8 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.31× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 34.1 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.01× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -14.0) |
| [[SNU-1 (line)]] | wt | 57.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.34× (z +11.3) | — |
| [[A-172 (line)]] | wt | 71.5 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.07× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -11.8) |
| [[C32 (line)]] | wt | 45.9 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.03× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -11.7) |
| [[HCT15 (line)]] | alt | 34.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.39× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 94.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.88× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 44.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.37× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 34.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.40× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 60.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.20× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 41.1 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -10.5) |
| [[RKO (line)]] | wt | 66.9 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.56× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 45.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.16× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 59.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.73× (z +10.6) | — |
| [[SW 900 (line)]] | alt | 52.7 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.70× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -12.5) |
| [[A498 (line)]] | wt | 36.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.16× (z +8.5) | — |
| [[J82 (line)]] | alt | 37.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 40.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -10.3) |
| [[A-427 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1547), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5R1]] | +0.75 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[PSMD3]] | +0.66 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PSMD6]] | +0.65 | +0.56 / +0.79 | both halves | 1e-05 | STRING 410 |
| [[BLMH]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CAMK2G]] | +0.65 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[PLAA]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 | STRING 944 |
| [[MAPRE3]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[VPS50]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PHKB]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[MYG1]] | +0.62 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[PSMC1]] | +0.61 | +0.69 / +0.66 | both halves | 7e-06 | STRING 769 |
| [[POPDC3]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC2-AS1]] | -0.56 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[POC1B-AS1]] | -0.53 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[DGKH]] | -0.52 | -0.54 / -0.29 | both halves | 2e-04 |  |
| [[ZNF131]] | -0.51 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[TOB2]] | -0.51 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[MIRLET7A1HG]] | -0.51 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[ZNF800]] | -0.51 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[LNP1]] | -0.51 | -0.47 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NSFL1C's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 0.8% of all compounds | 0.010 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.572). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-20.8, -7.8); signed map (-24.1, -22.5). **Vector** length 102, 26.4% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +11.0 | +25.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.5 | +24.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.5 | +21.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.0 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | +4.5 | +3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.4 | +9.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.3 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.2 | -21.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -3.6 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.2 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.8 | -1.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | NSFL1 cofactor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:1,442,162-1,473,842 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ776F14.1, p47, UBXD10, UBX1, UBXN2C |
| Gene groups (HGNC) | UBX domain containing |
| Reactome | 4 pathways, smallest: RHOH GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNZ2](https://www.uniprot.org/uniprotkb/Q9UNZ2) (NSFL1 cofactor p47):

> Reduces the ATPase activity of VCP (By similarity). Necessary for the fragmentation of Golgi stacks during mitosis and for VCP-mediated reassembly of Golgi stacks after mitosis (By similarity). May play a role in VCP-mediated formation of transitional endoplasmic reticulum (tER) (By similarity). Inhibits the activity of CTSL (in vitro). Together with UBXN2B/p37, regulates the centrosomal levels of kinase AURKA/Aurora A during mitotic progression by promoting AURKA removal from centrosomes in …

**Summary**, from NCBI Gene [55968](https://www.ncbi.nlm.nih.gov/gene/55968):

> N-ethylmaleimide-sensitive factor (NSF) and valosin-containing protein (p97) are two ATPases known to be involved in transport vesicle/target membrane fusion and fusions between membrane compartments. A trimer of the protein encoded by this gene binds a hexamer of cytosolic p97 and is required for p97-mediated regrowth of Golgi cisternae from mitotic Golgi fragments. Alternative splicing results in multiple transcript variants. A related pseudogene has been identified on chromosome 8. [provided …

**Accessions** — [HGNC:15912](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15912) · Entrez [55968](https://www.ncbi.nlm.nih.gov/gene/55968) · UniProt [Q9UNZ2](https://www.uniprot.org/uniprotkb/Q9UNZ2) · Ensembl [ENSG00000088833](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088833)

## Data

Gene col 1547: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1547); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1547, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1547]; `tensor/DDL_lfc|DDL_z.npy` [1547]; `embed/gene_vectors.npy` [1547]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1547 or target_col == 1547). Every well: [[NSFL1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSFL1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
