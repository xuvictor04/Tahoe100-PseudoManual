---
symbol: "HTT"
type: "gene"
col: 12393
ensembl_id: "ENSG00000197386"
name: "huntingtin"
location: "4p16.3"
module: 30
arm: "+"
pooled_cpm: 110.24
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# HTT

*huntingtin* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.06× (z +14.6, q 3e-45, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.733× (z -5.8, q 1e-06, down in 34 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.753× (z -5.8, q 1e-06, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SNU-1 0.251×, SW48 0.269×, NCI-H23 0.471×, A-172 0.431×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.191×, SNU-1 0.321×, HEC-1-A 0.476×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.337×, NCI-H1573 0.419×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (SW480 0.428×, HOP62 0.531×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 0.659×, HOP62 0.646×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SW 1088 0.0849×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDRG3]] (+0.65, fdr 2e-05), [[VDAC3]] (+0.65, fdr 1e-05), [[NBAS]] (+0.65, fdr 7e-06); moves opposite to [[SKIL]] (-0.66, fdr 1e-05), [[PNRC2]] (-0.61, fdr 1e-05), [[KDSR]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FZD7]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12393.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.06×** | +14.6 | 3e-45 | 47/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.83×** | +11.6 | 2e-28 | 46/48 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +11.2 | 7e-27 | 47/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +10.5 | 9e-24 | 45/48 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +10.5 | 1e-23 | 46/48 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +8.9 | 5e-17 | 45/48 (Panc 03.27, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +7.2 | 5e-11 | 40/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +6.2 | 3e-08 | 38/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.51×** | +5.2 | 1e-05 | 33/49 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.9 | 6e-05 | 26/48 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +4.9 | 6e-05 | 35/49 (LoVo, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +4.8 | 8e-05 | 30/48 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.2 | 9e-04 | 25/48 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +4.1 | 0.001 | 27/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.9 | 0.004 | 25/45 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.5 | 0.014 | 15/49 (A498, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12393.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SNU-1 0.251×, SW48 0.269×, NCI-H23 0.471×, A-172 0.431×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.191×, SNU-1 0.321×, HEC-1-A 0.476×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.337×, NCI-H1573 0.419×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (SW480 0.428×, HOP62 0.531×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 0.659×, HOP62 0.646×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SW 1088 0.0849×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.733×** | -5.8 | 1e-06 | 34/45 (RKO, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.742×** | -5.8 | 1e-06 | 34/47 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.753×** | -5.8 | 1e-06 | 31/48 (SW480, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.761×** | -5.5 | 4e-06 | 26/49 (C-33 A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.790×** | -4.6 | 5e-04 | 23/44 (SNU-1, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.803×** | -4.5 | 8e-04 | 30/49 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.861× | -4.3 | 0.001 | 17/48 (CFPAC-1, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.871× | -4.0 | 0.005 | 19/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.843× | -3.5 | 0.032 | 20/48 (C32, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | 0.851× | -3.3 | 0.058 | 19/48 (RPMI-7951, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.896× | -3.2 | 0.080 | 5/48 (SHP-77, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12393. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 75.7 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +14.9) | — |
| [[NCI-H1573 (line)]] | alt | 145 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.40× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -10.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 119 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 2.35× (z +11.0) | [[Auranofin (drug)]] 5 µM 0.428× (z -11.0) |
| [[C32 (line)]] | wt | 112 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.54× (z +11.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.431× (z -10.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[COLO 205 (line)]] | alt | 78.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.66× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 121 | 3 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.71× (z +13.7) | [[Auranofin (drug)]] 5 µM 0.531× (z -8.8) |
| [[HT-29 (line)]] | alt | 85.0 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.91× (z +11.7) | — |
| [[KATO III (line)]] | alt | 84.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.85× (z +12.5) | — |
| [[LoVo (line)]] | wt | 95.5 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.90× (z +13.2) | — |
| [[HEC-1-A (line)]] | alt | 126 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.476× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 121 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.07× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.471× (z -9.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 179 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.69× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -11.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 131 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.41× (z +11.0) | — |
| [[A498 (line)]] | wt | 106 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.33× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 120 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.77× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 154 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.17× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.474× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 103 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.02× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.588× (z -8.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 81.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +11.7) | — |
| [[H4 (line)]] | wt | 199 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.28× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.448× (z -8.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LS 180 (line)]] | wt | 171 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.34× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 112 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.11× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 114 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.659× (z -9.1) |
| [[RKO (line)]] | wt | 151 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +16.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -15.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 97.5 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.276× (z -13.2) ⚠ transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SNU-1 (line)]] | wt | 154 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -13.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.431× (z -9.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 91.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.04× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -11.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 93.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.10× (z +8.8) | — |
| [[SW 1088 (line)]] | alt | 82.1 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0849× (z -9.0) |
| [[A549 (line)]] | wt | 84.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 124 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 105 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 84.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12393), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | +0.65 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[VDAC3]] | +0.65 | +0.68 / +0.51 | both halves | 1e-05 | STRING 402 |
| [[NBAS]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PHKB]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[ECI2]] | +0.64 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[UBAC1]] | +0.63 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[KATNB1]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[UNC45A]] | +0.62 | +0.67 / +0.36 | both halves | 1e-04 | same gene group |
| [[NMRAL1]] | +0.62 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[EPS15L1]] | +0.61 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[GDAP2]] | +0.61 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[ATP5F1C]] | +0.61 | +0.66 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKIL]] | -0.66 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.61 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[KDSR]] | -0.61 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[C21orf91]] | -0.60 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[LEKR1]] | -0.59 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[PCF11]] | -0.59 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[KBTBD2]] | -0.58 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[LINC02340]] | -0.58 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[MIRLET7A1HG]] | -0.57 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[SERTAD1]] | -0.57 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[HELQ]] | -0.56 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[XIAP]] | -0.56 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FZD7]] | C | FZD7 activity raises HTT's level | lines that do not express FZD7 (3) vs lines expressing it (47) | 1.45× lower at baseline in the lines without FZD7 | 0.095 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.5, -9.8); signed map (-34.5, -5.8). **Vector** length 121, 38.0% of its response variance represented; |z| ≥ 3 in 1,151 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.1 | +14.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.7 | +11.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.7 | +11.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.9 | +10.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.3 | +10.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.8 | +5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -9.4 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.9 | -5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.3 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -5.7 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | huntingtin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:3,041,363-3,243,957 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IT15; previously HD |
| Gene groups (HGNC) | Receptor ligands; Armadillo like helical domain containing; Centriolar satellite proteins |
| Reactome | 2 pathways, smallest: Regulation of MECP2 expression and activity; Transcriptional Regulation by MECP2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P42858](https://www.uniprot.org/uniprotkb/P42858) (Huntingtin):

> [Huntingtin]: May play a role in microtubule-mediated transport or vesicle function.; [Huntingtin, myristoylated N-terminal fragment]: Promotes the formation of autophagic vesicles.

**Summary**, from NCBI Gene [3064](https://www.ncbi.nlm.nih.gov/gene/3064):

> Huntingtin is a disease gene linked to Huntington's disease, a neurodegenerative disorder characterized by loss of striatal neurons. This is thought to be caused by an expanded, unstable trinucleotide repeat in the huntingtin gene, which translates as a polyglutamine repeat in the protein product. A fairly broad range of trinucleotide repeats (9-35) has been identified in normal controls, and repeat numbers in excess of 40 have been described as pathological. The huntingtin locus is large, …

**Accessions** — [HGNC:4851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4851) · Entrez [3064](https://www.ncbi.nlm.nih.gov/gene/3064) · UniProt [P42858](https://www.uniprot.org/uniprotkb/P42858) · Ensembl [ENSG00000197386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197386)

## Data

Gene col 12393: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12393); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12393, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12393]; `tensor/DDL_lfc|DDL_z.npy` [12393]; `embed/gene_vectors.npy` [12393]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12393 or target_col == 12393). Every well: [[HTT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HTT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
