---
symbol: "HMG20A"
type: "gene"
col: 6398
ensembl_id: "ENSG00000140382"
name: "high mobility group 20A"
location: "15q24.3"
module: 11
arm: "+"
pooled_cpm: 51.12
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# HMG20A

*high mobility group 20A* — 15q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.03× (z +16.3, q 0e+00, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.636× (z -12.7, q 5e-34, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLK4]] (+0.69, fdr 7e-06), [[UQCRFS1]] (+0.67, fdr 2e-05), [[METTL18]] (+0.66, fdr 7e-06); moves opposite to [[TPST2]] (-0.67, fdr 1e-05), [[DIP2A]] (-0.65, fdr 1e-05), [[STX2]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6398.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.03×** | +16.3 | 0e+00 | 40/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +13.1 | 6e-37 | 40/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +12.3 | 1e-32 | 30/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +9.2 | 5e-18 | 34/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +6.9 | 5e-10 | 28/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +6.2 | 6e-08 | 26/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.7 | 7e-07 | 19/48 (MIA PaCa-2, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.13× | +4.7 | 2e-04 | 13/48 (HOP62, A498, …) | rises with dose | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | **1.35×** | +4.4 | 7e-04 | 11/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.15× | +3.9 | 0.006 | 12/49 (A498, A549, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.13× | +3.3 | 0.045 | 4/48 (NCI-H1573, RPMI-7951, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.12× | +3.3 | 0.051 | 10/48 (A549, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.12× | +3.2 | 0.061 | 16/48 (LS 180, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6398.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.636×** | -12.7 | 5e-34 | 40/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.645×** | -11.3 | 2e-27 | 29/45 (RKO, KATO III, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.694×** | -10.2 | 4e-22 | 36/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.733×** | -8.7 | 6e-16 | 27/49 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.764×** | -7.5 | 5e-12 | 30/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | **0.798×** | -6.3 | 3e-08 | 24/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.807×** | -6.0 | 2e-07 | 22/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | **0.801×** | -5.9 | 2e-07 | 24/47 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.816×** | -5.7 | 8e-07 | 23/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | **0.823×** | -5.2 | 9e-06 | 22/47 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.824×** | -5.1 | 2e-05 | 21/48 (SW 1088, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.841× | -4.8 | 6e-05 | 18/48 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.837× | -4.8 | 8e-05 | 13/48 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.855× | -4.2 | 0.001 | 17/47 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | 0.864× | -3.9 | 0.003 | 19/43 (SW480, LoVo, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | 0.872× | -3.8 | 0.005 | 18/48 (SNU-423, COLO 205, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.880× | -3.6 | 0.011 | 14/48 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.917× | -3.4 | 0.019 | 8/49 (CFPAC-1, H4, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.891× | -3.2 | 0.038 | 11/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.858× | -3.0 | 0.061 | 6/49 (SHP-77, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.902× | -2.9 | 0.090 | 8/48 (NCI-H1792, RPMI-7951, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.929× | -2.9 | 0.090 | 3/48 (H4, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 45.9 | 0 | 9 (8 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.342× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~10% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.500× (z -9.3) |
| [[SW480 (line)]] | alt | 60.9 | 2 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.26× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.469× (z -10.8) |
| [[LoVo (line)]] | wt | 72.6 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.11× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.649× (z -9.1) |
| [[PANC-1 (line)]] | alt | 70.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +17.7) | — |
| [[HEC-1-A (line)]] | alt | 58.7 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.19× (z +10.5) | [[Lonafarnib (drug)]] 5 µM 0.251× (z -10.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.517× (z -9.2) |
| [[A-172 (line)]] | wt | 33.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +15.9) | — |
| [[A549 (line)]] | wt | 63.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 66.3 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.88× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 74.2 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.32× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 60.3 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.43× (z +9.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 37.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.5) | — |
| [[KATO III (line)]] | alt | 56.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -13.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 39.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.81× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.371× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~10% of this change |
| [[A498 (line)]] | wt | 32.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 57.4 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.190× (z -8.8) |
| [[C32 (line)]] | wt | 72.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -9.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 51.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -9.2) |
| [[HT-29 (line)]] | alt | 54.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.36× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 50.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.349× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~10% of this change |
| [[Panc 03.27 (line)]] | alt | 43.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -9.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 61.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -16.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.315× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~10% of this change |
| [[SNU-1 (line)]] | wt | 64.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -13.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.260× (z -8.8) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -11.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLK4]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[UQCRFS1]] | +0.67 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[METTL18]] | +0.66 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.65 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[COQ5]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ZNF620]] | +0.64 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PEX12]] | +0.64 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[FUNDC1]] | +0.64 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ZNF518A]] | +0.64 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[PYM1]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ZBTB6]] | +0.63 | +0.62 / +0.49 | both halves | 2e-05 |  |
| [[LINC00265]] | +0.63 | +0.66 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST2]] | -0.67 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[DIP2A]] | -0.65 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[STX2]] | -0.60 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[SMG1P2]] | -0.60 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[CORO7]] | -0.59 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[INPP4A]] | -0.58 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[CYTH3]] | -0.57 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[SLC27A4]] | -0.57 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[SMG1P5]] | -0.56 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[MAST2]] | -0.56 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[STRN]] | -0.55 | -0.62 / -0.28 | both halves | 3e-04 |  |
| [[TCF3]] | -0.55 | -0.56 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-32.4, 6.9); signed map (3.7, -20.7). **Vector** length 106, 24.9% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.7 | +13.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +9.2 | +16.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +12.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.5 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.7 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | -0.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +2.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.5 | -12.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -10.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.1 | -5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | -3.8 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -6.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.5 | -4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group 20A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.3 — chr15:77,420,412-77,485,607 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HMGX1, FLJ10739, HMGXB1 |
| Gene groups (HGNC) | Non-canonical high mobility group |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP66](https://www.uniprot.org/uniprotkb/Q9NP66) (High mobility group protein 20A):

> Plays a role in neuronal differentiation as chromatin-associated protein. Acts as inhibitor of HMG20B. Overcomes the repressive effects of the neuronal silencer REST and induces the activation of neuronal-specific genes. Involved in the recruitment of the histone methyltransferase KMT2A/MLL1 and consequent increased methylation of histone H3 lysine 4 (By similarity).

**Summary**, from NCBI Gene [10363](https://www.ncbi.nlm.nih.gov/gene/10363):

> Enables identical protein binding activity. Predicted to be involved in regulation of gene expression. Predicted to act upstream of or within negative regulation of neuron differentiation; negative regulation of protein sumoylation; and negative regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:5001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5001) · Entrez [10363](https://www.ncbi.nlm.nih.gov/gene/10363) · UniProt [Q9NP66](https://www.uniprot.org/uniprotkb/Q9NP66) · Ensembl [ENSG00000140382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140382)

## Data

Gene col 6398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6398); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6398]; `tensor/DDL_lfc|DDL_z.npy` [6398]; `embed/gene_vectors.npy` [6398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6398 or target_col == 6398). Every well: [[HMG20A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMG20A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
