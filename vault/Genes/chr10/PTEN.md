---
symbol: "PTEN"
type: "gene"
col: 10177
ensembl_id: "ENSG00000171862"
name: "phosphatase and tensin homolog"
location: "10q23.31"
module: 45
arm: "+"
pooled_cpm: 239.26
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 15
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# PTEN

*phosphatase and tensin homolog* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.33× (z +9.0, q 2e-16, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.483× (z -14.9, q 0e+00, down in 41 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.744× (z -6.1, q 2e-07, down in 30 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MBNL2]] (+0.59, fdr 1e-05), [[KBTBD3]] (+0.57, fdr 1e-05), [[SNX2]] (+0.57, fdr 1e-05); moves opposite to [[DDX5]] (-0.55, fdr 4e-05), [[AVEN]] (-0.54, fdr 4e-05), [[DOCK1]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 15 go from it, the strongest it → cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10177.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.33×** | +9.0 | 2e-16 | 40/45 (Panc 03.27, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +8.9 | 2e-16 | 41/44 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +7.5 | 1e-11 | 38/44 (SNU-423, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +7.2 | 9e-11 | 34/44 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +6.2 | 7e-08 | 25/44 (MIA PaCa-2, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +5.6 | 2e-06 | 32/44 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +5.2 | 2e-05 | 36/45 (NCI-H23, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +4.7 | 2e-04 | 28/45 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +4.4 | 8e-04 | 24/44 (BT-474, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 9e-04 | 24/44 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.14× | +3.7 | 0.010 | 10/44 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.011 | 20/44 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.19× | +3.7 | 0.011 | 20/46 (NCI-H23, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.015 | 23/44 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.017 | 17/44 (NCI-H460, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.028 | 20/44 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.1 | 0.060 | 15/44 (HOP62, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10177.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.483×** | -14.9 | 0e+00 | 41/45 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.472×** | -14.8 | 0e+00 | 38/41 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.511×** | -12.8 | 5e-35 | 36/42 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.744×** | -6.1 | 2e-07 | 30/44 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.758×** | -5.7 | 1e-06 | 30/44 (AsPC-1, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.762×** | -5.6 | 2e-06 | 34/44 (A498, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.775×** | -5.2 | 1e-05 | 27/44 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.770×** | -5.2 | 2e-05 | 29/44 (NCI-H2030, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.791×** | -4.8 | 1e-04 | 29/44 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.863× | -4.3 | 0.001 | 20/45 (NCI-H1792, CHP-212, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.828×** | -3.7 | 0.010 | 20/44 (NCI-H2030, CFPAC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.840× | -3.5 | 0.026 | 17/44 (Panc 03.27, NCI-H460, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **0.748×** | -3.1 | 0.085 | 21/43 (MIA PaCa-2, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.748×** | -3.1 | 0.085 | 21/43 (NCI-H1792, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10177. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 194 | 10 | 2 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.75× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -9.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 256 | 2 | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -22.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 366 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.64× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.430× (z -11.2) |
| [[PANC-1 (line)]] | alt | 298 | 1 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 2.63× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -17.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 252 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.95× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -15.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 313 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.93× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 233 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -14.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 260 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.29× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -17.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 235 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.61× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -11.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 282 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.72× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -18.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 146 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +14.6) | — |
| [[NCI-H2030 (line)]] | alt | 212 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 202 | 3 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.78× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -10.1) ⚠ cell-cycle shift, explains ~9% of this change |
| [[NCI-H460 (line)]] | wt | 530 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.34× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -16.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 207 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -16.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 247 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.458× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 275 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -11.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 197 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 1.96× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 305 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.396× (z -11.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 138 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -10.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 239 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -17.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 200 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -13.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 582 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -18.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 195 | 2 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.74× (z +10.0) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.99× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -26.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 198 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -13.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 269 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.404× (z -12.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 148 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -15.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 216 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -10.7) ⚠ cell-cycle shift, explains ~9% of this change |
| [[AsPC-1 (line)]] | alt | 218 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[CHP-212 (line)]] | wt | 471 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -13.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 258 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.530× (z -9.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 176 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.282× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW48 (line)]] | wt | 236 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -15.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -8.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 341 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -13.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 203 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -14.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.472× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 238 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 166 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 17.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 245 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 112 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10177), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBNL2]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[KBTBD3]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[SNX2]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[FHIP1A]] | +0.56 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[ATP5PO]] ⚠ | +0.55 | +0.50 / +0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PREPL]] | +0.55 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[TBC1D8B]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[TP53TG1]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[PLEKHH3]] | +0.54 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[CXADR]] | +0.53 | +0.41 / +0.53 | both halves | 4e-05 | STRING 444 |
| [[SNAPC3]] | +0.53 | +0.37 / +0.45 | both halves | 9e-05 |  |
| [[CLGN]] | +0.53 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[FAM13A]] | +0.52 | +0.35 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.55 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[AVEN]] | -0.54 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[DOCK1]] | -0.53 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[E2F3]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 | STRING 559 |
| [[ZNF710]] | -0.51 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[BRD9]] | -0.51 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[EXOC7]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[TTL]] | -0.50 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[RBM19]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[KLHL21]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[QRICH2]] | -0.50 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[GHRLOS]] | -0.50 | -0.37 / -0.53 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM | C | [[ATAD1]], PTEN activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.68× the cells of the other lines | 0.012 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Ixazomib citrate (drug)]] 5 µM | C | [[ATAD1]], PTEN activity raises the cells' numbers under Ixazomib citrate 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.54× the cells of the other lines | 0.014 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Elimusertib hydrochloride (drug)]] 5 µM | C | [[ATAD1]], PTEN activity raises the cells' numbers under Elimusertib hydrochloride 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.61× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Daptomycin (drug)]] 0.5 µM | C | [[ATAD1]], PTEN activity raises the cells' numbers under Daptomycin 0.5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.62× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; cell counts less trustworthy; co-absent genes |
| cells under [[Cabozantinib (S-malate) (drug)]] 5 µM | C | [[ATAD1]], PTEN activity raises the cells' numbers under Cabozantinib (S-malate) 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.76× the cells of the other lines | 0.033 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Carbamazepine (drug)]] 0.5 µM | C | [[ATAD1]], PTEN activity raises the cells' numbers under Carbamazepine 0.5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.72× the cells of the other lines | 0.041 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Vemurafenib (drug)]] 5 µM | C | [[ATAD1]], PTEN activity lowers the cells' numbers under Vemurafenib 5 µM (makes them more sensitive) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 1.25× the cells of the other lines | 0.045 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Peretinoin (drug)]] 5 µM | C | [[ATAD1]], PTEN activity raises the cells' numbers under Peretinoin 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.76× the cells of the other lines | 0.055 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[NG25 (drug)]] 5 µM | C | [[ATAD1]], PTEN activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.56× the cells of the other lines | 0.059 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Peretinoin (drug)]] 0.5 µM | C | [[ATAD1]], PTEN activity raises the cells' numbers under Peretinoin 0.5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.62× the cells of the other lines | 0.076 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[vincristine (drug)]] 5 µM | C | [[ATAD1]], PTEN activity raises the cells' numbers under vincristine 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.55× the cells of the other lines | 0.092 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Citalopram (hydrobromide) (drug)]] 0.05 µM | C | [[ATAD1]], PTEN activity lowers the cells' numbers under Citalopram (hydrobromide) 0.05 µM (makes them more sensitive) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 1.32× the cells of the other lines | 0.093 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.2, -9.5); signed map (-25.8, -8.0). **Vector** length 99.1, 29.6% of its response variance represented; |z| ≥ 3 in 1,307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.3 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.7 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +4.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.4 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +3.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -5.1 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.8 | -2.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | phosphatase and tensin homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:87,862,638-87,971,930 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MMAC1, TEP1, PTEN1; previously BZS, MHAM |
| Gene groups (HGNC) | C2 tensin-type domain containing; PTEN protein phosphatases; Phosphoinositide phosphatases |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, UV_RESPONSE_DN, APICAL_JUNCTION |
| Reactome | 25 pathways, smallest: Regulation of PTEN localization; Regulation of PTEN mRNA translation; Synthesis of IP3 and IP4 in the cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [P60484](https://www.uniprot.org/uniprotkb/P60484) (Phosphatidylinositol 3,4,5-trisphosphate 3-phosphatase and dual-specificity protein phosphatase PTEN):

> Dual-specificity protein phosphatase, dephosphorylating tyrosine-, serine- and threonine-phosphorylated proteins. Also functions as a lipid phosphatase, removing the phosphate in the D3 position of the inositol ring of PtdIns(3,4,5)P3/phosphatidylinositol 3,4,5-trisphosphate, PtdIns(3,4)P2/phosphatidylinositol 3,4-diphosphate and PtdIns3P/phosphatidylinositol 3-phosphate with a preference for PtdIns(3,4,5)P3. Furthermore, this enzyme can also act as a cytosolic inositol 3-phosphatase acting on …

**Summary**, from NCBI Gene [5728](https://www.ncbi.nlm.nih.gov/gene/5728):

> This gene was identified as a tumor suppressor that is mutated in a large number of cancers at high frequency. The protein encoded by this gene is a phosphatidylinositol-3,4,5-trisphosphate 3-phosphatase. It contains a tensin like domain as well as a catalytic domain similar to that of the dual specificity protein tyrosine phosphatases. Unlike most of the protein tyrosine phosphatases, this protein preferentially dephosphorylates phosphoinositide substrates. It negatively regulates …

**Accessions** — [HGNC:9588](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9588) · Entrez [5728](https://www.ncbi.nlm.nih.gov/gene/5728) · UniProt [P60484](https://www.uniprot.org/uniprotkb/P60484) · Ensembl [ENSG00000171862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171862)

## Data

Gene col 10177: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10177); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10177, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10177]; `tensor/DDL_lfc|DDL_z.npy` [10177]; `embed/gene_vectors.npy` [10177]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10177 or target_col == 10177). Every well: [[PTEN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTEN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
