---
symbol: "MAN2A1"
type: "gene"
col: 3416
ensembl_id: "ENSG00000112893"
name: "mannosidase alpha class 2A member 1"
location: "5q21.3"
module: 59
arm: "-"
pooled_cpm: 146.23
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# MAN2A1

*mannosidase alpha class 2A member 1* — 5q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.52× (z +10.1, q 4e-21, up in 33 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.27× (z +8.5, q 4e-15, up in 28 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.606× (z -12.0, q 2e-30, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCC4]] (+0.66, fdr 7e-06), [[RAP1GDS1]] (+0.60, fdr 1e-05), [[TBC1D1]] (+0.60, fdr 1e-05); moves opposite to [[YY1AP1]] (-0.56, fdr 2e-05), [[DENND6B]] (-0.55, fdr 1e-05), [[DBP]] (-0.54, fdr 1e-05).
> It sits in the **-** arm of [[Module 059]] (Amino acids regulate mTORC1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3416.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +10.1 | 4e-21 | 33/47 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +9.7 | 9e-20 | 43/48 (MIA PaCa-2, HT-29, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +8.5 | 4e-15 | 28/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.40×** | +8.0 | 2e-13 | 33/47 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.37×** | +7.9 | 4e-13 | 33/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.27×** | +5.9 | 4e-07 | 29/47 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +4.6 | 3e-04 | 19/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.19× | +4.4 | 8e-04 | 20/47 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.2 | 0.002 | 17/48 (SHP-77, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.38×** | +3.7 | 0.013 | 14/45 (HT-29, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.033 | 19/49 (AsPC-1, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.15× | +3.4 | 0.036 | 16/47 (SW 900, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.14× | +3.2 | 0.066 | 16/49 (SHP-77, LoVo, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.076 | 9/48 (A498, Hs 766T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3416.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.606×** | -12.0 | 2e-30 | 35/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.720×** | -11.6 | 1e-28 | 33/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.666×** | -9.7 | 4e-20 | 34/47 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.695×** | -9.1 | 2e-17 | 34/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.713×** | -8.4 | 3e-15 | 35/48 (BT-474, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.738×** | -7.6 | 3e-12 | 34/48 (SW48, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.548×** | -6.8 | 7e-10 | 31/49 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.807×** | -5.4 | 6e-06 | 22/48 (SW48, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.817×** | -5.1 | 3e-05 | 24/48 (HepG2/C3A, AsPC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.819×** | -5.0 | 3e-05 | 25/48 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.778×** | -4.5 | 4e-04 | 26/48 (hTERT-HPNE, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.841× | -4.3 | 7e-04 | 18/48 (KATO III, LOX-IMVI, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.886× | -4.3 | 8e-04 | 12/48 (A498, NCI-H460, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | 0.845× | -4.2 | 0.001 | 22/48 (LoVo, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.856× | -3.9 | 0.004 | 12/48 (SW48, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.724×** | -3.7 | 0.008 | 21/48 (KATO III, C-33 A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.868× | -3.4 | 0.021 | 11/49 (HOP62, NCI-H23, …) | top dose only |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.827×** | -3.4 | 0.021 | 10/49 (HCT15, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.909× | -3.4 | 0.021 | 10/48 (NCI-H23, RKO, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.841× | -3.1 | 0.059 | 10/49 (NCI-H460, NCI-H661, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3416. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 129 | 12 (1 ⚠) | 2 | [[Cobimetinib (drug)]] 5 µM 2.36× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.472× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 246 | 4 (1 ⚠) | 5 (3 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.52× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -14.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.490× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 148 | 4 (2 ⚠) | 4 (4 ⚠) | [[Daptomycin (drug)]] 5 µM 2.58× (z +10.8) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.93× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.364× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[CFPAC-1 (line)]] | alt | 143 | 5 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.76× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 241 | 4 (1 ⚠) | 1 | [[Dexamethasone (drug)]] 0.5 µM 2.16× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.461× (z -9.6) |
| [[PANC-1 (line)]] | alt | 146 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -23.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.397× (z -15.7) |
| [[RKO (line)]] | wt | 172 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.252× (z -14.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.432× (z -8.9) |
| [[SW48 (line)]] | wt | 169 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -16.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.266× (z -13.5) |
| [[A549 (line)]] | wt | 129 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -23.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.445× (z -10.2) |
| [[BT-474 (line)]] | alt | 82.4 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 108 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -19.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.400× (z -12.3) |
| [[HT-29 (line)]] | alt | 126 | 3 (3 ⚠) | 1 | [[Bortezomib (drug)]] 0.05 µM 2.05× (z +9.7) ⚠ cell-cycle shift, explains ~58% of this change | [[Harringtonine (drug)]] 5 µM 0.525× (z -9.0) |
| [[KATO III (line)]] | alt | 139 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -13.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.422× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 122 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -19.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.311× (z -13.9) |
| [[A-172 (line)]] | wt | 167 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.04× (z +8.6) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -13.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.467× (z -9.2) |
| [[A-427 (line)]] | wt | 132 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.454× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 215 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.411× (z -13.1) |
| [[COLO 205 (line)]] | alt | 136 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.320× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 229 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.379× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 234 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -11.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.446× (z -10.4) |
| [[HOP62 (line)]] | alt | 74.4 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.60× (z +11.2) ⚠ toxic | — |
| [[J82 (line)]] | alt | 143 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -16.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 233 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.12× (z +10.0) ⚠ toxic | [[Harringtonine (drug)]] 5 µM 0.485× (z -9.7) |
| [[SHP-77 (line)]] | alt | 84.4 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.40× (z +12.0) | — |
| [[SNU-1 (line)]] | wt | 158 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 74.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HCT15 (line)]] | alt | 92.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -16.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[MIA PaCa-2 (line)]] | alt | 132 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.75× (z +12.7) ⚠ unreliable plate only | — |
| [[NCI-H1792 (line)]] | alt | 272 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -11.7) ⚠ cell-cycle shift, explains ~88% of this change |
| [[SK-MEL-2 (line)]] | alt | 172 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.570× (z -9.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SNU-423 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.16× (z +8.8) ⚠ toxic | — |
| [[SW 900 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -8.5) ⚠ cell-cycle shift, explains ~88% of this change |
| [[A498 (line)]] | wt | 168 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 112 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 171 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 95.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3416), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC4]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[RAP1GDS1]] | +0.60 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[TBC1D1]] | +0.60 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[TTL]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[FARP1]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[IPO7]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ATP11C]] | +0.55 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SLC38A1]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[PDS5A]] | +0.52 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[PTPN11]] | +0.52 | +0.43 / +0.55 | both halves | 3e-05 | pathway: SARS-CoV-2 Infection |
| [[ARPC5]] | +0.51 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[STK39]] | +0.51 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YY1AP1]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[DENND6B]] | -0.55 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[DBP]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TTI2]] | -0.54 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[LRRC27]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[YJU2B]] | -0.50 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[CWC25]] | -0.50 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ZNF136]] | -0.50 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[CBX8]] | -0.50 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ASB8]] | -0.49 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[NPHP1]] | -0.48 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[AKAP10]] | -0.48 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **-** arm (projection on the module's main direction -0.490). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.5, -35.1); signed map (-18.9, -49.4). **Vector** length 125, 35.4% of its response variance represented; |z| ≥ 3 in 1,318 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.0 | +9.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +8.5 | +10.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +7.3 | +8.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +6.9 | +7.9 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +6.8 | +5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.8 | +8.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +6.0 | +4.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.9 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +4.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.1 | -6.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -12.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.8 | -11.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.5 | -9.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | mannosidase alpha class 2A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q21.3 — chr5:109,689,927-109,869,625 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GOLIM7, MANII; previously MANA2 |
| Gene groups (HGNC) | Mannosidases alpha class 2 |
| Reactome | 14 pathways, smallest: Reactions specific to the complex N-glycan synthesis pathway; N-glycan antennae elongation in the medial/trans-Golgi; Intra-Golgi traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16706](https://www.uniprot.org/uniprotkb/Q16706) (Alpha-mannosidase 2):

> Catalyzes the first committed step in the biosynthesis of complex N-glycans. It controls conversion of high mannose to complex N-glycans; the final hydrolytic step in the N-glycan maturation pathway.

**Summary**, from NCBI Gene [4124](https://www.ncbi.nlm.nih.gov/gene/4124):

> This gene encodes a glycosyl hydrolase that localizes to the Golgi and catalyzes the final hydrolytic step in the asparagine-linked oligosaccharide (N-glycan) maturation pathway. Mutations in the mouse homolog of this gene have been shown to cause a systemic autoimmune disease similar to human systemic lupus erythematosus. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:6824](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6824) · Entrez [4124](https://www.ncbi.nlm.nih.gov/gene/4124) · UniProt [Q16706](https://www.uniprot.org/uniprotkb/Q16706) · Ensembl [ENSG00000112893](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112893)

## Data

Gene col 3416: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3416); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3416, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3416]; `tensor/DDL_lfc|DDL_z.npy` [3416]; `embed/gene_vectors.npy` [3416]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3416 or target_col == 3416). Every well: [[MAN2A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAN2A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
