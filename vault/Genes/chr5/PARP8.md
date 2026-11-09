---
symbol: "PARP8"
type: "gene"
col: 7576
ensembl_id: "ENSG00000151883"
name: "poly(ADP-ribose) polymerase family member 8"
location: "5q11.1"
module: 2
arm: "-"
pooled_cpm: 128.34
n_lines_expressing: 44
n_dd_up: 3
n_dd_down: 25
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PARP8

*poly(ADP-ribose) polymerase family member 8* — 5q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 1.41× (z +3.7, q 0.071, up in 18 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 4.60×, BT-474 2.21×; ⚠ cell-cycle shift, explains ~18% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 3.51×, BT-474 3.12×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (HS-578T 2.73×, SW 900 2.55×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.197× (z -33.6, q 0e+00, down in 42 of 42 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF827]] (+0.61, fdr 2e-05), [[CDC14A]] (+0.60, fdr 3e-05), [[LINC01145-1]] (+0.59, fdr 3e-05); moves opposite to [[KCTD21]] (-0.60, fdr 9e-05), [[SAMD4B]] (-0.56, fdr 4e-05), [[AP1M1]] (-0.56, fdr 6e-05).
> It sits in the **-** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PCDH7]] → it (grade B ⚠); 3 go from it, the strongest it → [[LINC00623]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7576.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 4.60×, BT-474 2.21×; ⚠ cell-cycle shift, explains ~18% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 3.51×, BT-474 3.12×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (HS-578T 2.73×, SW 900 2.55×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.071 | 18/42 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.071 | 18/43 (SW480, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.26×** | +3.4 | 0.091 | 16/42 (PANC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.091 | 15/41 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +3.3 | 0.096 | 11/43 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.17× | +3.3 | 0.10 | 15/43 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.12 | 18/42 (A-427, BT-474, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.12 | 11/42 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.13 | 4/42 (A498, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7576.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.197×** | -33.6 | 0e+00 | 42/42 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.211×** | -32.3 | 0e+00 | 42/42 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.277×** | -25.6 | 0e+00 | 34/36 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.292×** | -25.5 | 0e+00 | 41/42 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.299×** | -25.0 | 0e+00 | 39/43 (AN3 CA, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.388×** | -18.1 | 0e+00 | 35/39 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.573×** | -11.1 | 1e-26 | 36/41 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.600×** | -10.5 | 4e-24 | 35/42 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.630×** | -9.5 | 9e-20 | 34/42 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.652×** | -8.8 | 6e-17 | 34/43 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.688×** | -7.7 | 6e-13 | 31/42 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.760×** | -5.7 | 7e-07 | 24/42 (C32, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.596×** | -5.6 | 9e-07 | 30/43 (CFPAC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.769×** | -5.4 | 3e-06 | 24/42 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.772×** | -5.3 | 4e-06 | 24/41 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.782×** | -5.1 | 1e-05 | 24/42 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.640×** | -4.8 | 5e-05 | 27/42 (C32, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.796×** | -4.7 | 8e-05 | 22/42 (HT-29, AsPC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.799×** | -4.6 | 1e-04 | 22/41 (AsPC-1, NCI-H1792, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.799×** | -4.4 | 3e-04 | 21/42 (C32, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.806×** | -4.3 | 5e-04 | 20/42 (AsPC-1, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 200 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -22.7) |
| [[NCI-H460 (line)]] | wt | 96.5 | 0 | 13 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -19.8) |
| [[AsPC-1 (line)]] | alt | 344 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0670× (z -30.1) |
| [[NCI-H1792 (line)]] | alt | 542 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -32.4) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.114× (z -28.7) |
| [[NCI-H2347 (line)]] | alt | 294 | 2 (2 ⚠) | 8 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.121× (z -32.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.155× (z -29.4) |
| [[HT-29 (line)]] | alt | 139 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -23.0) |
| [[Panc 03.27 (line)]] | alt | 268 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0947× (z -29.5) |
| [[SNU-423 (line)]] | alt | 140 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -26.2) |
| [[LoVo (line)]] | wt | 143 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -22.2) |
| [[A-427 (line)]] | wt | 88.0 | 2 (2 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +23.3) ⚠ cell-cycle shift, explains ~18% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.326× (z -13.1) |
| [[A498 (line)]] | wt | 91.0 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -20.8) |
| [[AN3 CA (line)]] | alt | 329 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0147× (z -35.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.233× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 259 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -25.1) |
| [[COLO 205 (line)]] | alt | 230 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -21.0) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.144× (z -16.7) |
| [[HS-578T (line)]] | alt | 231 | 2 (2 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.73× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.123× (z -21.6) |
| [[PANC-1 (line)]] | alt | 119 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -20.5) |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.227× (z -15.4) |
| [[SW480 (line)]] | alt | 152 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0923× (z -36.1) |
| [[BT-474 (line)]] | alt | 57.4 | 4 (4 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 3.12× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.268× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 89.8 | 1 (1 ⚠) | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.168× (z -24.8) |
| [[J82 (line)]] | alt | 110 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -19.5) |
| [[LOX-IMVI (line)]] | wt | 175 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -22.4) |
| [[LS 180 (line)]] | wt | 92.6 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -22.1) |
| [[NCI-H1573 (line)]] | alt | 61.1 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -14.9) |
| [[NCI-H2030 (line)]] | alt | 89.4 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.229× (z -14.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.263× (z -13.4) |
| [[SW48 (line)]] | wt | 158 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -17.1) |
| [[H4 (line)]] | wt | 137 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0976× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.157× (z -16.5) |
| [[HCT15 (line)]] | alt | 123 | 1 (1 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.277× (z -12.3) |
| [[RKO (line)]] | wt | 200 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -24.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.217× (z -19.4) |
| [[SHP-77 (line)]] | alt | 148 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -18.1) |
| [[SNU-1 (line)]] | wt | 116 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.235× (z -12.8) |
| [[SW 900 (line)]] | alt | 85.2 | 1 (1 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.55× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -15.3) |
| [[hTERT-HPNE (line)]] | wt | 88.8 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -13.0) |
| [[Hs 766T (line)]] | wt | 54.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -11.7) |
| [[KATO III (line)]] | alt | 94.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -19.9) |
| [[HOP62 (line)]] | alt | 32.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -11.9) |
| [[SW 1271 (line)]] | alt | 163 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0832× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.205× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 37.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -8.7) |
| [[A-172 (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 26.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 99.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF827]] | +0.61 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[CDC14A]] | +0.60 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[LINC01145-1]] | +0.59 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[LINC00623]] | +0.57 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[MGST2]] | +0.57 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[MEIS2]] | +0.57 | +0.40 / +0.57 | both halves | 4e-05 |  |
| [[TIFA]] | +0.54 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[PCDH7]] | +0.52 | +0.38 / +0.48 | both halves | 7e-05 |  |
| [[ATP23]] | +0.52 | +0.27 / +0.41 | both halves | 3e-04 |  |
| [[PPP1R3B-DT]] | +0.52 | +0.39 / +0.37 | both halves | 7e-05 |  |
| [[TLR3]] | +0.52 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[SH2D4A]] | +0.51 | +0.38 / +0.45 | both halves | 7e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD21]] | -0.60 | -0.37 / -0.60 | both halves | 9e-05 |  |
| [[SAMD4B]] | -0.56 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[AP1M1]] | -0.56 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[DIP2A]] | -0.54 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[GPSM1]] | -0.52 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[SIN3B]] | -0.51 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[STK25]] | -0.50 | -0.29 / -0.48 | both halves | 3e-04 |  |
| [[HEMK1]] | -0.50 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[TPCN2]] | -0.49 | -0.24 / -0.47 | both halves | 4e-04 |  |
| [[DVL1]] | -0.49 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[PACS2]] | -0.49 | -0.22 / -0.49 | both halves | 6e-04 |  |
| [[DCAKD]] | -0.48 | -0.38 / -0.51 | both halves | 7e-05 | pathway: Metabolism of vitamins and cofactors |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH7]] | B | PCDH7 activity raises PARP8's level | lines that do not express PCDH7 (18) vs lines expressing it (32) | 1.72× lower at baseline in the lines without PCDH7 | 0.073 | ⚠ within organs, on part of the lines; also absent: ADGRL4, KCNQ5, ST8SIA4 |
| [[MECOM]] | B | MECOM activity raises PARP8's level | lines that do not express MECOM (18) vs lines expressing it (32) | 1.91× lower at baseline in the lines without MECOM | 0.094 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00623]] | B | PARP8 activity raises LINC00623's level | lines that do not express PARP8 (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without PARP8 | 0.011 | ⚠ within organs, on part of the lines; also absent: ITPKB, ZNF785 |
| [[MECOM]] | B | PARP8 activity raises MECOM's level | lines that do not express PARP8 (6) vs lines expressing it (44) | 4.07× lower at baseline in the lines without PARP8 | 0.067 | ⚠ within organs, on part of the lines; also absent: ITPKB, ZNF785 |
| [[PCDH7]] | B | PARP8 activity raises PCDH7's level | lines that do not express PARP8 (6) vs lines expressing it (44) | 3.62× lower at baseline in the lines without PARP8 | 0.078 | ⚠ within organs, on part of the lines; also absent: ITPKB, ZNF785 |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **-** arm (projection on the module's main direction -0.460). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-1.1, -25.9); signed map (44.7, -0.4). **Vector** length 114, 35.0% of its response variance represented; |z| ≥ 3 in 1,345 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +12.2 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | -0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | -1.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | -0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.6 | +0.5 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -2.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.9 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.8 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.5 | -5.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -4.4 | -5.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.9 | -3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.7 | -8.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | poly(ADP-ribose) polymerase family member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.1 — chr5:50,665,899-50,846,519 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21308, pART16, ARTD16 |
| Gene groups (HGNC) | Poly(ADP-ribose) polymerases |
| Reactome | 12 pathways, smallest: Maturation of nucleoprotein_9683610; Maturation of nucleoprotein_9694631; Nicotinate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3A8](https://www.uniprot.org/uniprotkb/Q8N3A8) (Protein mono-ADP-ribosyltransferase PARP8):

> Mono-ADP-ribosyltransferase that mediates mono-ADP-ribosylation of target proteins.

**Summary**, from NCBI Gene [79668](https://www.ncbi.nlm.nih.gov/gene/79668):

> Enables NAD+-protein mono-ADP-ribosyltransferase activity. Involved in protein auto-ADP-ribosylation. Predicted to be active in endoplasmic reticulum tubular network; membrane; and nuclear envelope. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26124](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26124) · Entrez [79668](https://www.ncbi.nlm.nih.gov/gene/79668) · UniProt [Q8N3A8](https://www.uniprot.org/uniprotkb/Q8N3A8) · Ensembl [ENSG00000151883](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151883)

## Data

Gene col 7576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7576); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7576]; `tensor/DDL_lfc|DDL_z.npy` [7576]; `embed/gene_vectors.npy` [7576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7576 or target_col == 7576). Every well: [[PARP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
