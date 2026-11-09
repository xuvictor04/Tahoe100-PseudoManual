---
symbol: "API5"
type: "gene"
col: 9256
ensembl_id: "ENSG00000166181"
name: "apoptosis inhibitor 5"
location: "11p12"
module: 25
arm: "+"
pooled_cpm: 67.83
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# API5

*apoptosis inhibitor 5* — 11p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.10× (z +16.5, q 0e+00, up in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.95× (z +15.4, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.736× (z -4.8, q 1e-03, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP3M1]] (+0.77, fdr 7e-06), [[USP14]] (+0.75, fdr 7e-06), [[DLD]] (+0.74, fdr 7e-06); moves opposite to [[SNHG9]] (-0.75, fdr 7e-06), [[MIA]] (-0.65, fdr 3e-05), [[TMEM258]] (-0.65, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9256.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +16.5 | 0e+00 | 41/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.97×** | +15.7 | 0e+00 | 44/49 (SW480, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.95×** | +15.4 | 0e+00 | 45/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.88×** | +14.5 | 1e-45 | 45/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +13.5 | 9e-40 | 46/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.84×** | +13.3 | 3e-38 | 44/48 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +13.3 | 3e-38 | 38/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.26×** | +13.1 | 3e-37 | 47/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +12.9 | 2e-36 | 47/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +12.8 | 1e-35 | 41/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +12.1 | 8e-32 | 37/45 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.69×** | +11.8 | 2e-30 | 43/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +10.5 | 4e-24 | 38/48 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +7.7 | 6e-13 | 30/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +7.6 | 1e-12 | 36/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +7.3 | 7e-12 | 30/48 (J82, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +5.6 | 5e-07 | 26/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.33×** | +4.5 | 2e-04 | 24/49 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.5 | 0.009 | 13/48 (LOX-IMVI, SW48, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.015 | 20/47 (HEC-1-A, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9256.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.736×** | -4.8 | 1e-03 | 26/48 (RPMI-7951, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.834× | -4.2 | 0.008 | 21/48 (hTERT-HPNE, SW48, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.794×** | -3.6 | 0.046 | 19/47 (HEC-1-A, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.894× | -3.6 | 0.046 | 14/49 (J82, BT-474, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.897× | -3.5 | 0.054 | 6/49 (SW 900, SHP-77, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.804×** | -3.4 | 0.063 | 16/48 (NCI-H661, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.869× | -3.2 | 0.096 | 11/48 (SW 1271, NCI-H1573, …) | two highest doses |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.909× | -3.1 | 0.13 | 4/49 (NCI-H1792, SW48, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | 0.869× | -3.1 | 0.13 | 11/48 (NCI-H661, NCI-H1573, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.825× | -3.0 | 0.15 | 15/48 (SW 1271, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9256. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 87.0 | 13 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +12.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.93× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 59.2 | 11 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.86× (z +14.4) | — |
| [[SW480 (line)]] | alt | 108 | 8 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.03× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 53.6 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.39× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 78.9 | 6 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.40× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 69.0 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 55.8 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.65× (z +11.7) | — |
| [[LOX-IMVI (line)]] | wt | 50.9 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +11.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.76× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 51.2 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.81× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 55.5 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.25× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.92× (z +8.6) | — |
| [[A-427 (line)]] | wt | 69.8 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.22× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 64.4 | 3 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.61× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 72.9 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.82× (z +11.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.46× (z +10.0) | — |
| [[A-172 (line)]] | wt | 68.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.21× (z +8.6) | — |
| [[A498 (line)]] | wt | 52.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 65.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.6) | — |
| [[KATO III (line)]] | alt | 94.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 90.2 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 49.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.55× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 65.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.27× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 88.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 68.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +13.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 77.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +10.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 61.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 35.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +10.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 70.2 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.122× (z -11.8) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 43.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HCT15 (line)]] | alt | 86.4 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0740× (z -9.2) ⚠ toxic |
| [[HT-29 (line)]] | alt | 70.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +9.3) | — |
| [[J82 (line)]] | alt | 95.7 | 1 | 0 | [[Selinexor (drug)]] 5 µM 1.66× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.26× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 51.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW 1088 (line)]] | alt | 61.7 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0689× (z -8.7) |
| [[SW 1271 (line)]] | alt | 71.0 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0993× (z -9.3) |
| [[AN3 CA (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 79.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 79.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 77.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9256), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP3M1]] | +0.77 | +0.68 / +0.81 | both halves | 7e-06 |  |
| [[USP14]] | +0.75 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[DLD]] | +0.74 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[EFTUD2]] | +0.73 | +0.45 / +0.79 | both halves | 3e-05 |  |
| [[UBQLN1]] | +0.72 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[OPA1]] | +0.72 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[GPN1]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[DLAT]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[IPO8]] | +0.70 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[LIN7C]] | +0.69 | +0.48 / +0.78 | both halves | 2e-05 |  |
| [[OCRL]] | +0.68 | +0.37 / +0.77 | both halves | 9e-05 |  |
| [[XRCC6]] | +0.68 | +0.76 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG9]] | -0.75 | -0.61 / -0.76 | both halves | 7e-06 |  |
| [[MIA]] | -0.65 | -0.46 / -0.65 | both halves | 3e-05 |  |
| [[TMEM258]] | -0.65 | -0.48 / -0.72 | both halves | 2e-05 |  |
| [[INAFM1]] | -0.64 | -0.53 / -0.73 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.63 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[ING2]] | -0.63 | -0.25 / -0.79 | both halves | 4e-04 |  |
| [[POLR1H]] | -0.62 | -0.35 / -0.66 | both halves | 1e-04 |  |
| [[SNHG19]] | -0.62 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[MSX1]] | -0.62 | -0.16 / -0.72 | ⚠ one half (not replicated) | 0.001 |  |
| [[EIF1B]] | -0.62 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[TESK2]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[HOTAIRM1]] | -0.61 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.60 | -0.43 / -0.63 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.775). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.0, -14.8); signed map (-16.2, -43.1). **Vector** length 103, 29.4% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *oxidative phosphorylation* (hallmark, mean cos +0.52 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.3 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +9.1 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +12.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.2 | +15.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.2 | +13.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +12.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.6 | +11.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +3.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +2.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.3 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +1.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -4.5 | +4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.2 | -2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.1 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | apoptosis inhibitor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p12 — chr11:43,311,963-43,344,529 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AAC-11, API5L1, AAC11 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZZ5](https://www.uniprot.org/uniprotkb/Q9BZZ5) (Apoptosis inhibitor 5):

> Antiapoptotic factor that may have a role in protein assembly. Negatively regulates ACIN1. By binding to ACIN1, it suppresses ACIN1 cleavage from CASP3 and ACIN1-mediated DNA fragmentation. Also known to efficiently suppress E2F1-induced apoptosis. Its depletion enhances the cytotoxic action of the chemotherapeutic drugs.

**Summary**, from NCBI Gene [8539](https://www.ncbi.nlm.nih.gov/gene/8539):

> This gene encodes an apoptosis inhibitory protein whose expression prevents apoptosis after growth factor deprivation. This protein suppresses the transcription factor E2F1-induced apoptosis and also interacts with, and negatively regulates Acinus, a nuclear factor involved in apoptotic DNA fragmentation. Its depletion enhances the cytotoxic action of the chemotherapeutic drugs. Multiple alternatively spliced transcript variants encoding different isoforms have been identified. [provided by …

**Accessions** — [HGNC:594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:594) · Entrez [8539](https://www.ncbi.nlm.nih.gov/gene/8539) · UniProt [Q9BZZ5](https://www.uniprot.org/uniprotkb/Q9BZZ5) · Ensembl [ENSG00000166181](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166181)

## Data

Gene col 9256: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9256); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9256, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9256]; `tensor/DDL_lfc|DDL_z.npy` [9256]; `embed/gene_vectors.npy` [9256]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9256 or target_col == 9256). Every well: [[API5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/API5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
