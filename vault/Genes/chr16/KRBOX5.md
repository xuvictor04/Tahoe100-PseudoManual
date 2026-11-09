---
symbol: "KRBOX5"
type: "gene"
col: 12378
ensembl_id: "ENSG00000197302"
name: "KRAB domain containing 5"
location: "16p11.2"
module: 23
arm: "+"
pooled_cpm: 39.97
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# KRBOX5

*KRAB domain containing 5* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.34× (z +33.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.375× (z -13.7, q 8e-40, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01004]] (+0.83, fdr 1e-05), [[THAP2]] (+0.79, fdr 1e-05), [[PPP1R12A-AS2]] (+0.75, fdr 1e-04); moves opposite to [[CAMK2G]] (-0.69, fdr 1e-04), [[PARP1]] (-0.67, fdr 3e-05), [[LRFN3]] (-0.66, fdr 2e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12378.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.34×** | +33.1 | 0e+00 | 46/48 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +29.2 | 0e+00 | 45/48 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +18.5 | 0e+00 | 43/48 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +16.6 | 0e+00 | 39/48 (HEC-1-A, HOP62, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +16.3 | 0e+00 | 41/47 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +14.0 | 2e-42 | 36/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +12.8 | 2e-35 | 39/48 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.22×** | +7.7 | 9e-13 | 22/48 (J82, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.26×** | +6.4 | 1e-08 | 20/48 (CFPAC-1, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.26×** | +6.0 | 8e-08 | 24/47 (J82, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.24×** | +6.0 | 1e-07 | 21/48 (J82, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +5.2 | 8e-06 | 18/48 (A-172, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.20×** | +5.1 | 2e-05 | 19/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.17× | +4.3 | 6e-04 | 12/48 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.2 | 8e-04 | 17/48 (A498, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.16× | +4.0 | 0.002 | 10/47 (LS 180, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +3.8 | 0.004 | 13/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.09× | +3.3 | 0.027 | 3/48 (Hs 766T, SW 1088, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.13× | +3.3 | 0.030 | 6/48 (PANC-1, A549, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.033 | 5/48 (COLO 205, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.054 | 3/48 (RPMI-7951, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12378.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.375×** | -13.7 | 8e-40 | 44/49 (PANC-1, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.441×** | -11.4 | 1e-27 | 36/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.736×** | -8.4 | 6e-15 | 25/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.787×** | -6.6 | 5e-09 | 22/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.819×** | -5.5 | 4e-06 | 20/48 (NCI-H460, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.813×** | -5.5 | 4e-06 | 23/47 (SK-MEL-2, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.822×** | -5.4 | 5e-06 | 22/47 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.716×** | -4.7 | 2e-04 | 17/47 (C32, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | 0.852× | -4.1 | 0.003 | 19/45 (NCI-H1573, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.869× | -3.9 | 0.006 | 15/48 (SHP-77, SW48, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.888× | -3.3 | 0.047 | 10/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.920× | -3.3 | 0.047 | 10/48 (PANC-1, CHP-212, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.791×** | -3.3 | 0.047 | 13/44 (C-33 A, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Canagliflozin (drug)]] 0.05 µM |  | 0.883× | -3.2 | 0.056 | 12/47 (RPMI-7951, SW48, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.888× | -3.1 | 0.062 | 11/48 (NCI-H1573, BT-474, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.924× | -3.1 | 0.071 | 1/48 (Hs 766T) | all doses, flat |  |
| [[OTS514 (drug)]] 5 µM |  | **0.806×** | -3.0 | 0.087 | 8/45 (Hs 766T, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 50.9 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.1) | [[Digitoxin (drug)]] 5 µM 0.459× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.467× (z -10.4) |
| [[HOP62 (line)]] | alt | 26.7 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.04× (z +26.6) | — |
| [[J82 (line)]] | alt | 33.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +22.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 68.9 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.3) | [[TAK-901 (drug)]] 5 µM 0.220× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 45.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +18.4) | — |
| [[NCI-H460 (line)]] | wt | 40.8 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[SW480 (line)]] | alt | 51.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +18.2) | — |
| [[A-172 (line)]] | wt | 30.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +14.5) | — |
| [[LoVo (line)]] | wt | 45.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +20.9) | — |
| [[LS 180 (line)]] | wt | 44.3 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.187× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 63.8 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.0977× (z -25.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.226× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 23.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.87× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 57.6 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.169× (z -8.6) |
| [[SW 900 (line)]] | alt | 28.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 43.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +14.1) | — |
| [[A498 (line)]] | wt | 15.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.9) | — |
| [[A549 (line)]] | wt | 34.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 55.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 60.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[C32 (line)]] | wt | 40.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +14.8) | — |
| [[CFPAC-1 (line)]] | alt | 18.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 46.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +16.5) | — |
| [[HT-29 (line)]] | alt | 41.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +12.1) | — |
| [[KATO III (line)]] | alt | 48.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +14.0) | — |
| [[LOX-IMVI (line)]] | wt | 17.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 27.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 34.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +14.8) | — |
| [[Panc 03.27 (line)]] | alt | 32.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 31.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +13.4) | — |
| [[SHP-77 (line)]] | alt | 61.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 54.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +16.7) | — |
| [[SNU-423 (line)]] | alt | 53.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +19.4) | — |
| [[A-427 (line)]] | wt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 19.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 44.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 57.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.2) | — |
| [[NCI-H2347 (line)]] | alt | 22.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01004]] | +0.83 | +0.84 / +0.54 | both halves | 1e-05 |  |
| [[THAP2]] | +0.79 | +0.82 / +0.50 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.75 | +0.79 / +0.33 | both halves | 1e-04 |  |
| [[RFX3-DT]] | +0.72 | +0.78 / +0.25 | both halves | 4e-04 |  |
| [[RC3H2]] | +0.71 | +0.78 / +0.35 | both halves | 1e-04 |  |
| [[CFAP53]] | +0.71 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[CASS4]] | +0.71 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[TAS2R4]] | +0.71 | +0.71 / +0.38 | both halves | 6e-05 |  |
| [[ATF5]] | +0.70 | +0.69 / +0.38 | both halves | 6e-05 |  |
| [[PBLD]] | +0.70 | +0.71 / +0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[ANKRD17-DT]] | +0.69 | +0.73 / +0.35 | both halves | 1e-04 |  |
| [[SEPTIN7-DT]] | +0.69 | +0.74 / +0.25 | both halves | 4e-04 |  |
| [[ATE1OSP]] | +0.69 | +0.71 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMK2G]] | -0.69 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[PARP1]] | -0.67 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[LRFN3]] | -0.66 | -0.62 / -0.30 | both halves | 2e-04 |  |
| [[SKP2]] | -0.65 | -0.69 / -0.46 | both halves | 3e-05 |  |
| [[PLXND1]] | -0.65 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[CASP2]] | -0.64 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[LPCAT4]] | -0.64 | -0.69 / -0.23 | both halves | 5e-04 |  |
| [[LRRC20]] | -0.63 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[TAF5L]] | -0.62 | -0.70 / -0.34 | both halves | 1e-04 |  |
| [[ELP1]] | -0.62 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[NDRG3]] | -0.62 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[WASF3]] | -0.62 | -0.63 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KRBOX5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AIF1L]] | B | AIF1L activity raises KRBOX5's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 1.49× lower at baseline in the lines without AIF1L | 0.089 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |
| [[RNFT2]] | C | RNFT2 activity raises KRBOX5's level | lines that do not express RNFT2 (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without RNFT2 | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF37, CSRP1-AS1, DBNDD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.757). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.2, 12.2); signed map (23.0, -10.4). **Vector** length 105, 25.8% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +33.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +18.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +16.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +29.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +12.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +16.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +2.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.5 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.2 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.4 | -11.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.2 | -13.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.8 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | KRAB domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:31,713,229-31,794,869 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZNF720, KRBOX5 |
| Gene groups (HGNC) | KRAB domain containing |
| Matched by | ensembl_id |

UniProt [Q7Z2F6](https://www.uniprot.org/uniprotkb/Q7Z2F6) carries no function annotation.

**Summary**, from NCBI Gene [124411](https://www.ncbi.nlm.nih.gov/gene/124411):

> Predicted to enable DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26987) · Entrez [124411](https://www.ncbi.nlm.nih.gov/gene/124411) · UniProt [Q7Z2F6](https://www.uniprot.org/uniprotkb/Q7Z2F6) · Ensembl [ENSG00000197302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197302)

## Data

Gene col 12378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12378); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12378]; `tensor/DDL_lfc|DDL_z.npy` [12378]; `embed/gene_vectors.npy` [12378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12378 or target_col == 12378). Every well: [[KRBOX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRBOX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
