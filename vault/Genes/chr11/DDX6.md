---
symbol: "DDX6"
type: "gene"
col: 3132
ensembl_id: "ENSG00000110367"
name: "DEAD-box helicase 6"
location: "11q23.3"
module: 95
arm: "+"
pooled_cpm: 139.13
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# DDX6

*DEAD-box helicase 6* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.03× (z +16.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.273× (z -29.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C11orf58]] (+0.78, fdr 7e-06), [[MED12]] (+0.74, fdr 2e-05), [[RC3H2]] (+0.73, fdr 1e-05); moves opposite to [[TMEM120B]] (-0.75, fdr 1e-05), [[ETHE1]] (-0.72, fdr 1e-05), [[MPST]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3132.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.03×** | +16.2 | 0e+00 | 46/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +15.3 | 0e+00 | 42/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.67×** | +11.8 | 1e-29 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +11.1 | 2e-26 | 40/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +10.5 | 9e-24 | 40/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +10.1 | 6e-22 | 41/48 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +8.0 | 1e-13 | 34/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +7.7 | 9e-13 | 34/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +7.2 | 5e-11 | 37/49 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.97×** | +6.7 | 1e-09 | 40/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +6.7 | 1e-09 | 36/48 (SW48, RKO, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +4.6 | 2e-04 | 26/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.6 | 0.015 | 16/48 (SW480, KATO III, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.032 | 13/48 (HEC-1-A, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | 1.16× | +3.2 | 0.049 | 12/47 (AN3 CA, H4, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3132.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.273×** | -29.6 | 0e+00 | 48/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.280×** | -29.0 | 0e+00 | 48/48 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.319×** | -26.1 | 0e+00 | 48/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.517×** | -15.1 | 0e+00 | 48/48 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.635×** | -10.4 | 4e-23 | 46/48 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.782×** | -7.9 | 3e-13 | 37/48 (SW480, SW 900, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.500×** | -6.9 | 5e-10 | 44/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | 0.861× | -3.3 | 0.076 | 16/48 (A-427, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.1 | 0.13 | 14/49 (CHP-212, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 153 | 10 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +15.0) | [[Panobinostat (drug)]] 5 µM 0.250× (z -24.7) |
| [[LoVo (line)]] | wt | 92.6 | 8 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +18.9) | [[Panobinostat (drug)]] 5 µM 0.350× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 251 | 5 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -16.9) |
| [[NCI-H460 (line)]] | wt | 101 | 6 (1 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.277× (z -20.9) |
| [[HT-29 (line)]] | alt | 143 | 5 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -20.7) |
| [[KATO III (line)]] | alt | 288 | 3 (1 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.181× (z -22.7) |
| [[SW48 (line)]] | wt | 142 | 5 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -16.4) |
| [[A498 (line)]] | wt | 78.8 | 4 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -19.3) |
| [[HS-578T (line)]] | alt | 97.7 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.7) | [[Panobinostat (drug)]] 5 µM 0.249× (z -17.7) |
| [[Panc 03.27 (line)]] | alt | 137 | 3 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.231× (z -21.8) |
| [[A549 (line)]] | wt | 111 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.230× (z -20.1) |
| [[COLO 205 (line)]] | alt | 116 | 3 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.6) | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 160 | 2 | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -23.5) |
| [[LS 180 (line)]] | wt | 117 | 4 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +15.5) | [[Panobinostat (drug)]] 5 µM 0.264× (z -16.8) |
| [[PANC-1 (line)]] | alt | 208 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -21.8) |
| [[RKO (line)]] | wt | 144 | 2 | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.248× (z -17.9) |
| [[AsPC-1 (line)]] | alt | 139 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +16.3) | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -19.4) |
| [[CFPAC-1 (line)]] | alt | 154 | 2 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -18.5) |
| [[HOP62 (line)]] | alt | 108 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.226× (z -23.0) |
| [[Hs 766T (line)]] | wt | 134 | 2 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -19.5) |
| [[LOX-IMVI (line)]] | wt | 141 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.220× (z -20.3) |
| [[NCI-H2030 (line)]] | alt | 164 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.320× (z -16.2) |
| [[NCI-H2347 (line)]] | alt | 158 | 2 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -19.2) |
| [[SNU-423 (line)]] | alt | 145 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.190× (z -24.4) |
| [[SW 900 (line)]] | alt | 126 | 2 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.272× (z -17.7) |
| [[SW1417 (line)]] | alt | 196 | 2 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.285× (z -19.4) |
| [[A-172 (line)]] | wt | 88.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -22.8) |
| [[BT-474 (line)]] | alt | 115 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -11.7) |
| [[C32 (line)]] | wt | 186 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.322× (z -15.0) |
| [[A-427 (line)]] | wt | 92.5 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.344× (z -13.3) |
| [[C-33 A (line)]] | alt | 173 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -16.7) |
| [[HCT15 (line)]] | alt | 181 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.229× (z -16.5) |
| [[HepG2_C3A (line)]] | wt | 103 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.260× (z -14.1) |
| [[hTERT-HPNE (line)]] | wt | 129 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.214× (z -18.0) |
| [[MIA PaCa-2 (line)]] | alt | 158 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.182× (z -22.1) |
| [[NCI-H1792 (line)]] | alt | 103 | 1 | 3 | [[Harringtonine (drug)]] 5 µM 2.18× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 151 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -18.4) |
| [[RPMI-7951 (line)]] | alt | 103 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -16.9) |
| [[SK-MEL-2 (line)]] | alt | 79.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -12.5) |
| [[SNU-1 (line)]] | wt | 133 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.306× (z -11.9) |
| [[H4 (line)]] | wt | 130 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -16.2) |
| [[J82 (line)]] | alt | 83.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -16.0) |
| [[SHP-77 (line)]] | alt | 96.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -15.5) |
| [[AN3 CA (line)]] | alt | 143 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -11.1) |
| [[CHP-212 (line)]] | wt | 169 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -10.3) |
| [[SW 1088 (line)]] | alt | 150 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -8.9) |
| [[SW 1271 (line)]] | alt | 171 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -9.4) |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf58]] | +0.78 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[MED12]] | +0.74 | +0.46 / +0.71 | both halves | 2e-05 |  |
| [[RC3H2]] | +0.73 | +0.62 / +0.53 | both halves | 1e-05 | STRING 404 |
| [[ZNF564]] | +0.73 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.73 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.72 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[EIF4G2]] | +0.72 | +0.50 / +0.64 | both halves | 1e-05 | STRING 466 |
| [[ZBTB1]] | +0.72 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[HNRNPK]] | +0.72 | +0.48 / +0.65 | both halves | 2e-05 | STRING 748 |
| [[ZFX]] | +0.71 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[INO80D]] | +0.71 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.71 | +0.62 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM120B]] | -0.75 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[ETHE1]] | -0.72 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[MPST]] | -0.69 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.68 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[MPG]] | -0.67 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[LPCAT4]] | -0.67 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[COG5]] | -0.67 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[TOMM5]] | -0.67 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.65 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[TSEN54]] | -0.65 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[SLC37A3]] | -0.65 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[CARD19]] | -0.64 | -0.41 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DDX6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises DDX6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.744). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-8.8, 3.4); signed map (17.7, -22.6). **Vector** length 109, 35.4% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chromatin organization* (reactome, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.8 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +15.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.4 | +6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.4 | -0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.7 | +2.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.4 | +0.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.5 | -10.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.4 | -15.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.4 | -26.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -29.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -29.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.2 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -7.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -0.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,747,763-118,791,164 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RCK, Rck/p54; previously HLR2 |
| Gene groups (HGNC) | DEAD-box helicases; RNA decapping and exonuclease complex subunits |
| Reactome | 3 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Deadenylation-dependent mRNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P26196](https://www.uniprot.org/uniprotkb/P26196) (Probable ATP-dependent RNA helicase DDX6):

> Essential for the formation of P-bodies, cytosolic membrane-less ribonucleoprotein granules involved in RNA metabolism through the coordinated storage of mRNAs encoding regulatory functions. Plays a role in P-bodies to coordinate the storage of translationally inactive mRNAs in the cytoplasm and prevent their degradation. In the process of mRNA degradation, plays a role in mRNA decapping. Blocks autophagy in nutrient-rich conditions by repressing the expression of ATG-related genes through …

**Summary**, from NCBI Gene [1656](https://www.ncbi.nlm.nih.gov/gene/1656):

> This gene encodes a member of the DEAD box protein family. The protein is an RNA helicase found in P-bodies and stress granules, and functions in translation suppression and mRNA degradation. It is required for microRNA-induced gene silencing. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:2747](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2747) · Entrez [1656](https://www.ncbi.nlm.nih.gov/gene/1656) · UniProt [P26196](https://www.uniprot.org/uniprotkb/P26196) · Ensembl [ENSG00000110367](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110367)

## Data

Gene col 3132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3132); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3132]; `tensor/DDL_lfc|DDL_z.npy` [3132]; `embed/gene_vectors.npy` [3132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3132 or target_col == 3132). Every well: [[DDX6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
