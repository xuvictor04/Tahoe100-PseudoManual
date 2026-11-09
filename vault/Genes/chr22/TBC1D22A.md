---
symbol: "TBC1D22A"
type: "gene"
col: 612
ensembl_id: "ENSG00000054611"
name: "TBC1 domain family member 22A"
location: "22q13.31"
module: 40
arm: "+"
pooled_cpm: 326.0
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# TBC1D22A

*TBC1 domain family member 22A* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.49× (z +4.5, q 0.002, up in 32 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.434× (z -26.4, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BIRC6]] (+0.59, fdr 7e-06), [[BIN3]] (+0.59, fdr 1e-05), [[RUVBL2]] (+0.59, fdr 8e-05); moves opposite to [[TAPT1]] (-0.58, fdr 1e-05), [[RNF146]] (-0.58, fdr 3e-05), [[OXCT1]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANKRD18A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 612.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.49×** | +4.5 | 0.002 | 32/49 (HS-578T, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.48×** | +4.4 | 0.002 | 38/48 (HOP62, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.23×** | +4.2 | 0.004 | 27/48 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.006 | 27/48 (HS-578T, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.036 | 19/47 (SW480, RKO, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.3 | 0.099 | 22/48 (SHP-77, LoVo, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.11× | +3.2 | 0.12 | 2/48 (NCI-H1792, NCI-H2347) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.17 | 14/47 (HOP62, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 612.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.434×** | -26.4 | 0e+00 | 47/49 (A549, SW 900, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.475×** | -23.6 | 0e+00 | 42/48 (C32, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.322×** | -22.7 | 0e+00 | 47/48 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.372×** | -22.2 | 0e+00 | 47/49 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.364×** | -20.3 | 0e+00 | 44/44 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.416×** | -18.2 | 0e+00 | 45/45 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.450×** | -16.0 | 0e+00 | 45/47 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.520×** | -14.7 | 0e+00 | 45/48 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.488×** | -14.4 | 3e-45 | 40/47 (NCI-H1573, H4, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.551×** | -13.4 | 5e-39 | 43/48 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.553×** | -13.3 | 1e-38 | 41/48 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -10.7 | 3e-25 | 39/48 (C32, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.653×** | -9.6 | 5e-20 | 41/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.660×** | -9.3 | 5e-19 | 39/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.649×** | -8.7 | 2e-16 | 38/50 (SK-MEL-2, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.828×** | -4.2 | 7e-04 | 25/49 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.880× | -4.1 | 0.001 | 15/48 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.829×** | -3.9 | 0.003 | 22/47 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.734×** | -3.5 | 0.010 | 23/49 (C32, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | 0.865× | -3.3 | 0.024 | 17/48 (A549, HOP62, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.873× | -3.1 | 0.048 | 13/47 (CFPAC-1, H4, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.779×** | -2.8 | 0.092 | 15/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 612. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 271 | 0 | 16 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -19.1) |
| [[SW 900 (line)]] | alt | 490 | 0 | 16 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -23.4) |
| [[H4 (line)]] | wt | 357 | 0 | 15 (10 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.193× (z -18.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.215× (z -17.4) |
| [[C32 (line)]] | wt | 641 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -35.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.112× (z -22.5) |
| [[CFPAC-1 (line)]] | alt | 447 | 0 | 14 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -20.5) |
| [[C-33 A (line)]] | alt | 298 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -19.0) |
| [[HOP62 (line)]] | alt | 249 | 0 | 13 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.317× (z -16.5) |
| [[LoVo (line)]] | wt | 311 | 1 | 12 (8 ⚠) | [[Auranofin (drug)]] 5 µM 1.81× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -26.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -21.3) |
| [[MIA PaCa-2 (line)]] | alt | 314 | 0 | 13 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -23.7) |
| [[PANC-1 (line)]] | alt | 241 | 0 | 13 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -18.4) |
| [[A549 (line)]] | wt | 419 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -24.8) |
| [[HEC-1-A (line)]] | alt | 416 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -22.5) |
| [[KATO III (line)]] | alt | 384 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -17.8) |
| [[SK-MEL-2 (line)]] | alt | 259 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -21.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -18.2) |
| [[SW480 (line)]] | alt | 439 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -22.3) |
| [[AsPC-1 (line)]] | alt | 285 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -25.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.195× (z -20.6) |
| [[HS-578T (line)]] | alt | 335 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -22.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.213× (z -20.1) |
| [[hTERT-HPNE (line)]] | wt | 256 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -30.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.167× (z -21.3) |
| [[NCI-H1573 (line)]] | alt | 973 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0858× (z -31.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.290× (z -15.8) |
| [[SNU-1 (line)]] | wt | 460 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -21.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.191× (z -18.9) |
| [[SNU-423 (line)]] | alt | 360 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -29.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -21.8) |
| [[NCI-H1792 (line)]] | alt | 326 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -30.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -22.1) |
| [[RPMI-7951 (line)]] | alt | 288 | 0 | 10 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.191× (z -18.9) |
| [[COLO 205 (line)]] | alt | 438 | 1 | 8 (5 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.91× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -14.8) |
| [[HepG2_C3A (line)]] | wt | 525 | 0 | 9 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.149× (z -22.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -21.0) |
| [[Hs 766T (line)]] | wt | 332 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.321× (z -14.7) |
| [[LS 180 (line)]] | wt | 436 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -16.7) |
| [[A-172 (line)]] | wt | 165 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -15.5) |
| [[CHP-212 (line)]] | wt | 286 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -12.8) |
| [[HCT15 (line)]] | alt | 919 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0947× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -17.9) |
| [[RKO (line)]] | wt | 250 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.195× (z -20.4) |
| [[SW1417 (line)]] | alt | 197 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -16.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -13.4) |
| [[BT-474 (line)]] | alt | 209 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.380× (z -13.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -10.6) |
| [[J82 (line)]] | alt | 186 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -21.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -20.2) |
| [[LOX-IMVI (line)]] | wt | 179 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -17.2) |
| [[NCI-H2030 (line)]] | alt | 246 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -17.6) |
| [[NCI-H23 (line)]] | alt | 290 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -25.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -13.9) |
| [[A498 (line)]] | wt | 165 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -22.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.294× (z -17.2) |
| [[HT-29 (line)]] | alt | 244 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 166 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -14.0) |
| [[SHP-77 (line)]] | alt | 340 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.21× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -14.6) |
| [[SW48 (line)]] | wt | 400 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.4) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -16.9) |
| [[A-427 (line)]] | wt | 140 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.440× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 204 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -13.1) |
| [[AN3 CA (line)]] | alt | 211 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -9.2) |
| [[SW 1088 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW 1271 (line)]] | alt | 209 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -10.7) |
| [[NCI-H2122 (line)]] | alt | 352 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 387 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 153 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 612), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIRC6]] | +0.59 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[BIN3]] | +0.59 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[RUVBL2]] | +0.59 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[EPS15L1]] | +0.58 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[LINC03009-1]] | +0.57 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[VPS53]] | +0.56 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[RBAK-RBAKDN]] | +0.56 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[SAMD4B]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[EIF1AD]] | +0.55 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[ATG4B]] | +0.55 | +0.51 / +0.33 | both halves | 1e-04 |  |
| [[FERMT3]] | +0.55 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[SPATC1L]] | +0.54 | +0.42 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAPT1]] | -0.58 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[RNF146]] | -0.58 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[OXCT1]] | -0.57 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[CFAP418]] | -0.56 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[SIAH1]] | -0.55 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[UBXN2A]] | -0.55 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[RDX]] | -0.54 | -0.57 / -0.40 | both halves | 4e-05 |  |
| [[NHLRC2]] | -0.53 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ANKRD18A]] | -0.52 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[NFYB]] | -0.52 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[RNF138]] | -0.52 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[LRRC57]] | -0.51 | -0.56 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD18A]] | B | ANKRD18A activity raises TBC1D22A's level | lines that do not express ANKRD18A (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without ANKRD18A | 0.092 | ⚠ within organs, on part of the lines; also absent: LRRC61, SLC27A2, CHMP4C |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.322). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (2.0, -23.4); signed map (-46.5, 3.5). **Vector** length 111, 44.2% of its response variance represented; |z| ≥ 3 in 1,596 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.0 | +3.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +9.2 | +4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | +7.9 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.1 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.5 | +4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.8 | +0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +4.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.0 | -9.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.0 | -16.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -14.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -22.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -26.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.8 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | +0.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 22A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:46,762,617-47,175,699 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C22orf4 |
| Gene groups (HGNC) | TBC1 domain family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUA7](https://www.uniprot.org/uniprotkb/Q8WUA7) (TBC1 domain family member 22A):

> May act as a GTPase-activating protein for Rab family protein(s).

**Summary**, from NCBI Gene [25771](https://www.ncbi.nlm.nih.gov/gene/25771):

> Enables 14-3-3 protein binding activity and protein homodimerization activity. Predicted to be active in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1309) · Entrez [25771](https://www.ncbi.nlm.nih.gov/gene/25771) · UniProt [Q8WUA7](https://www.uniprot.org/uniprotkb/Q8WUA7) · Ensembl [ENSG00000054611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054611)

## Data

Gene col 612: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 612); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 612, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 612]; `tensor/DDL_lfc|DDL_z.npy` [612]; `embed/gene_vectors.npy` [612]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 612 or target_col == 612). Every well: [[TBC1D22A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D22A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
