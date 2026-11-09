---
symbol: "ANXA3"
type: "gene"
col: 6235
ensembl_id: "ENSG00000138772"
name: "annexin A3"
location: "4q21.21"
module: 8
arm: "+"
pooled_cpm: 93.45
n_lines_expressing: 26
n_dd_up: 16
n_dd_down: 21
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 63
direction_downstream: 92
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ANXA3

*annexin A3* — 4q21.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.82× (z +10.9, q 8e-25, up in 8 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.39× (z +8.7, q 5e-16, up in 17 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.190× (z -31.4, q 0e+00, down in 24 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf116]] (+0.66, fdr 7e-06), [[SYK]] (+0.64, fdr 7e-06), [[C6orf132]] (+0.64, fdr 7e-06); moves opposite to [[ADAMTS10]] (-0.52, fdr 1e-05), [[TSHZ3]] (-0.49, fdr 1e-04), [[ST3GAL2]] (-0.48, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 63 arrows point to it, the strongest [[SLC44A3]] → it (grade B ⚠); 92 go from it, the strongest it → [[EZR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6235.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +10.9 | 8e-25 | 8/23 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +9.8 | 4e-20 | 7/25 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.39×** | +8.7 | 5e-16 | 17/25 (NCI-H1573, LS 180, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.58×** | +8.3 | 2e-14 | 19/24 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.54×** | +8.1 | 6e-14 | 20/24 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +7.4 | 1e-11 | 6/23 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.43×** | +6.8 | 1e-09 | 13/24 (NCI-H1573, LS 180, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.42×** | +6.6 | 4e-09 | 18/24 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.39×** | +6.3 | 2e-08 | 17/24 (NCI-H1573, A-172, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 0.002 | 12/24 (NCI-H1573, COLO 205, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +4.2 | 0.002 | 9/24 (A-172, NCI-H2347, …) | two highest doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.0 | 0.003 | 7/19 (NCI-H2347, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.007 | 9/24 (NCI-H1573, Hs 766T, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.007 | 9/24 (NCI-H1573, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.009 | 5/24 (A498, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.052 | 10/25 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.066 | 7/24 (COLO 205, LS 180, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.084 | 8/24 (A549, A498, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.084 | 3/24 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Cysteamine (hydrochloride) (drug)]] 5 µM |  | 1.12× | +2.9 | 0.088 | 3/25 (NCI-H1573, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6235.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.190×** | -31.4 | 0e+00 | 24/24 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.208×** | -29.7 | 0e+00 | 24/24 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.248×** | -26.4 | 0e+00 | 24/24 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.424×** | -16.2 | 0e+00 | 22/24 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.637×** | -12.1 | 2e-31 | 22/25 (SW480, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.542×** | -11.6 | 3e-29 | 23/24 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.621×** | -9.0 | 1e-17 | 21/24 (SW48, HCT15, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.440×** | -8.1 | 3e-14 | 21/25 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.731×** | -5.7 | 6e-07 | 19/24 (SW480, LS 180, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.748×** | -5.5 | 2e-06 | 17/24 (Panc 03.27, HepG2/C3A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.782×** | -4.7 | 2e-04 | 18/24 (NCI-H2347, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.788×** | -4.5 | 3e-04 | 18/24 (SW480, NCI-H1573, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.638×** | -4.5 | 4e-04 | 17/24 (Panc 03.27, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.800×** | -4.1 | 0.002 | 13/24 (HepG2/C3A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.05 µM |  | **0.813×** | -3.9 | 0.003 | 10/24 (J82, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.832×** | -3.5 | 0.015 | 15/24 (Panc 03.27, HepG2/C3A, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.711×** | -3.4 | 0.023 | 4/24 (NCI-H460, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.717×** | -3.3 | 0.028 | 8/25 (Panc 03.27, Hs 766T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.721×** | -3.2 | 0.033 | 12/25 (KATO III, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.888× | -3.2 | 0.037 | 10/24 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.893× | -3.0 | 0.059 | 5/24 (Panc 03.27, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.49 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6235. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 240 | 0 | 16 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0392× (z -38.6) |
| [[LoVo (line)]] | wt | 200 | 0 | 15 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0465× (z -29.1) |
| [[SW48 (line)]] | wt | 248 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0435× (z -28.7) |
| [[HEC-1-A (line)]] | alt | 376 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0670× (z -33.0) |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 10 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0747× (z -17.1) |
| [[Panc 03.27 (line)]] | alt | 214 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0685× (z -25.0) |
| [[KATO III (line)]] | alt | 264 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0293× (z -37.2) |
| [[LS 180 (line)]] | wt | 160 | 1 | 8 (4 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.17× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.0589× (z -23.0) |
| [[NCI-H1573 (line)]] | alt | 83.4 | 4 (2 ⚠) | 5 (2 ⚠) | [[Peretinoin (drug)]] 5 µM 6.60× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.101× (z -14.4) |
| [[HT-29 (line)]] | alt | 235 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0797× (z -21.7) |
| [[SW1417 (line)]] | alt | 183 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0707× (z -27.2) |
| [[A-172 (line)]] | wt | 28.3 | 4 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 3.82× (z +9.7) | [[Belinostat (drug)]] 5 µM 0.139× (z -14.9) |
| [[A498 (line)]] | wt | 37.9 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.11× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 3.28× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 179 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0459× (z -30.9) |
| [[BT-474 (line)]] | alt | 131 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0982× (z -18.5) |
| [[COLO 205 (line)]] | alt | 139 | 1 (1 ⚠) | 6 (3 ⚠) | [[Daptomycin (drug)]] 0.5 µM 4.01× (z +8.5) ⚠ unreliable plate only | [[Panobinostat (drug)]] 5 µM 0.0600× (z -17.3) |
| [[A549 (line)]] | wt | 65.4 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -17.5) |
| [[CFPAC-1 (line)]] | alt | 157 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -19.4) |
| [[HCT15 (line)]] | alt | 143 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -19.0) |
| [[NCI-H2347 (line)]] | alt | 141 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -17.5) |
| [[SNU-1 (line)]] | wt | 234 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0492× (z -29.2) |
| [[NCI-H460 (line)]] | wt | 31.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -12.6) |
| [[Hs 766T (line)]] | wt | 124 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0832× (z -21.2) |
| [[J82 (line)]] | alt | 34.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -14.0) |
| [[A-427 (line)]] | wt | 6.56 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.91 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.73 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.11 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.51 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.95 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.02 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 22.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.39 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.09 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.38 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 20.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.92 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 13.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6235), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf116]] | +0.66 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[SYK]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[C6orf132]] | +0.64 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[MACC1]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[LINC00857]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[INAVA]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[KRT80]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[B3GNT3]] | +0.61 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ST6GALNAC5]] | +0.61 | +0.59 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[EPS8L3]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[LINC02474]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CLIC5]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS10]] | -0.52 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[TSHZ3]] | -0.49 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[ST3GAL2]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ZNF8-DT]] | -0.47 | -0.44 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*63 arrows, 63 of them with an alert ⚠; grade A 0, B 10, C 53. Shown: the 12 strongest; 51 more arrows (51 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3]] | B | SLC44A3 activity raises ANXA3's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.48× lower at baseline in the lines without SLC44A3 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises ANXA3's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 4.01× lower at baseline in the lines without TJP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[LMO7]] | B | LMO7 activity raises ANXA3's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 3.27× lower at baseline in the lines without LMO7 | 0.022 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[BRSK1]] | B | BRSK1 activity lowers ANXA3's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 6.29× higher at baseline in the lines without BRSK1 | 0.033 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[PSORS1C1]] | B | PSORS1C1 activity raises ANXA3's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 3.25× lower at baseline in the lines without PSORS1C1 | 0.041 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[NOSTRIN]] | B | NOSTRIN activity raises ANXA3's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.99× lower at baseline in the lines without NOSTRIN | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[LINC01186]] | B | LINC01186 activity raises ANXA3's level | lines that do not express LINC01186 (12) vs lines expressing it (38) | 3.71× lower at baseline in the lines without LINC01186 | 0.079 | ⚠ within organs, on part of the lines; also absent: LINC01836, STXBP2, EEPD1 |
| [[EPS8L1]] | B | EPS8L1 activity raises ANXA3's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.41× lower at baseline in the lines without EPS8L1 | 0.084 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[MET]] | B | MET activity raises ANXA3's level | lines that do not express MET (9) vs lines expressing it (41) | 3.50× lower at baseline in the lines without MET | 0.088 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[TMEM184A]] | B | TMEM184A activity raises ANXA3's level | lines that do not express TMEM184A (8) vs lines expressing it (42) | 2.83× lower at baseline in the lines without TMEM184A | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, ENSG00000284716, GPRC5C; maybe low, not absent; its own permutation p |
| [[C1orf116]] | C | C1orf116 activity raises ANXA3's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 10.39× lower at baseline in the lines without C1orf116 | 1e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[INAVA]], [[MROH3P]] | C | INAVA, MROH3P activity raises ANXA3's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 8.03× lower at baseline in the lines without INAVA, MROH3P | 2e-05 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent with the target; co-absent genes |

### Downstream of this gene

*92 arrows, 92 of them with an alert ⚠; grade A 0, B 39, C 53. Shown: the 12 strongest; 80 more arrows (80 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EZR]] | B | ANXA3 activity raises EZR's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 2.93× lower at baseline in the lines without ANXA3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[EPS8L1]] | B | ANXA3 activity raises EPS8L1's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.25× lower at baseline in the lines without ANXA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[BRSK1]] | B | ANXA3 activity lowers BRSK1's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.29× higher at baseline in the lines without ANXA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[LMO7]] | B | ANXA3 activity raises LMO7's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.95× lower at baseline in the lines without ANXA3 | 0.002 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[SH3D19]] | B | ANXA3 activity raises SH3D19's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 2.29× lower at baseline in the lines without ANXA3 | 0.002 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[SLC44A3]] | B | ANXA3 activity raises SLC44A3's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 2.57× lower at baseline in the lines without ANXA3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[UNC13D]] | B | ANXA3 activity raises UNC13D's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.18× lower at baseline in the lines without ANXA3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[TMEM184A]] | B | ANXA3 activity raises TMEM184A's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 2.41× lower at baseline in the lines without ANXA3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[TJP1]] | B | ANXA3 activity raises TJP1's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without ANXA3 | 0.004 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[TJP2]] | B | ANXA3 activity raises TJP2's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.10× lower at baseline in the lines without ANXA3 | 0.004 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[TMEM39B]] | B | ANXA3 activity lowers TMEM39B's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 1.64× higher at baseline in the lines without ANXA3 | 0.005 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[PATJ]] | B | ANXA3 activity raises PATJ's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.21× lower at baseline in the lines without ANXA3 | 0.006 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.473). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.6, 52.3); signed map (55.8, 5.7). **Vector** length 117, 40.9% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.9 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.5 | +8.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.5 | +8.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +5.2 | +6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.7 | +6.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +3.5 | +4.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -11.6 |
|  | [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.7 | -16.2 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.6 | -2.6 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | annexin A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.21 — chr4:78,551,747-78,610,451 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ANX3 |
| Gene groups (HGNC) | Annexins |
| Matched by | ensembl_id |

**Function**, from UniProt [P12429](https://www.uniprot.org/uniprotkb/P12429) (Annexin A3):

> Inhibitor of phospholipase A2, also possesses anti-coagulant properties. Also cleaves the cyclic bond of inositol 1,2-cyclic phosphate to form inositol 1-phosphate.

**Summary**, from NCBI Gene [306](https://www.ncbi.nlm.nih.gov/gene/306):

> This gene encodes a member of the annexin family. Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways. This protein functions in the inhibition of phopholipase A2 and cleavage of inositol 1,2-cyclic phosphate to form inositol 1-phosphate. This protein may also play a role in anti-coagulation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:541](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:541) · Entrez [306](https://www.ncbi.nlm.nih.gov/gene/306) · UniProt [P12429](https://www.uniprot.org/uniprotkb/P12429) · Ensembl [ENSG00000138772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138772)

## Data

Gene col 6235: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6235); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6235, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6235]; `tensor/DDL_lfc|DDL_z.npy` [6235]; `embed/gene_vectors.npy` [6235]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6235 or target_col == 6235). Every well: [[ANXA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANXA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
