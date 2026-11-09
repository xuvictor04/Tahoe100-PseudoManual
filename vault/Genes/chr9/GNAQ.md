---
symbol: "GNAQ"
type: "gene"
col: 7946
ensembl_id: "ENSG00000156052"
name: "G protein subunit alpha q"
location: "9q21.2"
module: 18
arm: "+"
pooled_cpm: 232.81
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# GNAQ

*G protein subunit alpha q* — 9q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.34× (z +8.2, q 2e-13, up in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.27× (z +7.0, q 7e-10, up in 29 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Ixazomib citrate (drug)]] 5 µM in 8 lines (HOP62 2.23×, H4 2.73×, NCI-H460 1.68×, NCI-H1792 1.81×, …); [[Ixazomib citrate (drug)]] 0.5 µM in 3 lines (HOP62 2.07×, NCI-H460 1.58×, H4 2.33×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 1.48×, LoVo 1.42×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (C32 1.94×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.254× (z -41.1, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COP1]] (+0.63, fdr 7e-06), [[AHCYL2]] (+0.61, fdr 1e-05), [[BMPR1A]] (+0.59, fdr 1e-05); moves opposite to [[RFESD]] (-0.58, fdr 1e-05), [[N4BP3]] (-0.54, fdr 1e-05), [[APBB3]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7946.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Ixazomib citrate (drug)]] 5 µM in 8 lines (HOP62 2.23×, H4 2.73×, NCI-H460 1.68×, NCI-H1792 1.81×, …); [[Ixazomib citrate (drug)]] 0.5 µM in 3 lines (HOP62 2.07×, NCI-H460 1.58×, H4 2.33×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 1.48×, LoVo 1.42×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (C32 1.94×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +8.2 | 2e-13 | 35/47 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +7.0 | 7e-10 | 29/47 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +5.8 | 2e-06 | 24/47 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.15× | +4.1 | 0.006 | 15/46 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.29×** | +3.9 | 0.009 | 21/44 (NCI-H1792, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Penfluridol (drug)]] 5 µM |  | 1.14× | +3.7 | 0.024 | 12/46 (KATO III, A498, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.12× | +3.1 | 0.16 | 8/48 (AsPC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.16 | 11/48 (NCI-H460, SNU-423, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7946.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.254×** | -41.1 | 0e+00 | 47/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.276×** | -38.6 | 0e+00 | 46/47 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.417×** | -26.3 | 0e+00 | 46/47 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.675×** | -16.7 | 0e+00 | 38/47 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.592×** | -15.2 | 0e+00 | 35/43 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.656×** | -11.7 | 9e-30 | 35/44 (C-33 A, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.668×** | -11.7 | 2e-29 | 38/46 (HepG2/C3A, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.695×** | -11.0 | 4e-26 | 31/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.699×** | -10.8 | 3e-25 | 35/47 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.728×** | -9.6 | 6e-20 | 33/47 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.730×** | -9.5 | 2e-19 | 34/47 (SW1417, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.728×** | -9.2 | 2e-18 | 29/47 (A-172, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.785×** | -7.3 | 1e-11 | 25/47 (HepG2/C3A, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.864× | -6.2 | 2e-08 | 18/47 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.843× | -5.2 | 9e-06 | 23/47 (LoVo, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.854× | -4.8 | 7e-05 | 20/47 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.880× | -3.9 | 0.003 | 14/47 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.882× | -3.6 | 0.008 | 9/47 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.888× | -3.6 | 0.009 | 14/47 (RPMI-7951, HS-578T, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.923× | -3.5 | 0.014 | 0/48 | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.902× | -3.1 | 0.044 | 8/46 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.900× | -3.0 | 0.073 | 12/46 (RKO, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.908× | -2.9 | 0.073 | 8/48 (HOP62, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 394 | 2 (2 ⚠) | 12 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 2.57× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.158× (z -40.1) |
| [[A-172 (line)]] | wt | 274 | 1 | 11 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.57× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -30.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.325× (z -21.7) |
| [[C32 (line)]] | wt | 430 | 1 | 11 (5 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.94× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -22.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.305× (z -17.0) |
| [[LoVo (line)]] | wt | 274 | 0 | 12 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -33.1) |
| [[LOX-IMVI (line)]] | wt | 425 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -26.6) |
| [[Panc 03.27 (line)]] | alt | 201 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -25.0) |
| [[HOP62 (line)]] | alt | 173 | 2 | 8 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.23× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -25.1) |
| [[NCI-H460 (line)]] | wt | 238 | 3 (1 ⚠) | 7 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.68× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.228× (z -30.5) |
| [[SW48 (line)]] | wt | 250 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -20.6) |
| [[HT-29 (line)]] | alt | 322 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -29.4) |
| [[KATO III (line)]] | alt | 328 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -35.0) |
| [[A549 (line)]] | wt | 276 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -38.2) |
| [[HepG2_C3A (line)]] | wt | 312 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -27.5) |
| [[HS-578T (line)]] | alt | 130 | 1 | 7 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.87× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -19.9) |
| [[J82 (line)]] | alt | 300 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -28.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.246× (z -24.2) |
| [[LS 180 (line)]] | wt | 384 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -29.1) |
| [[SW1417 (line)]] | alt | 297 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -25.6) |
| [[SW480 (line)]] | alt | 220 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -43.7) |
| [[HEC-1-A (line)]] | alt | 384 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.241× (z -30.6) |
| [[hTERT-HPNE (line)]] | wt | 208 | 1 | 5 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.03× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -17.2) |
| [[NCI-H1573 (line)]] | alt | 111 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.335× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 163 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.4) ⚠ cell-cycle shift, explains ~31% of this change | [[Panobinostat (drug)]] 5 µM 0.136× (z -29.7) |
| [[RKO (line)]] | wt | 256 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -18.5) |
| [[H4 (line)]] | wt | 203 | 2 | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -15.1) |
| [[Hs 766T (line)]] | wt | 246 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -25.7) |
| [[NCI-H2030 (line)]] | alt | 160 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -12.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.462× (z -11.7) |
| [[PANC-1 (line)]] | alt | 154 | 2 (1 ⚠) | 3 | [[Ixazomib citrate (drug)]] 5 µM 1.57× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.393× (z -21.0) |
| [[SHP-77 (line)]] | alt | 189 | 1 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.226× (z -22.7) |
| [[SK-MEL-2 (line)]] | alt | 200 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -24.2) |
| [[SNU-1 (line)]] | wt | 315 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.411× (z -12.9) |
| [[SNU-423 (line)]] | alt | 222 | 1 (1 ⚠) | 4 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.73× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 5 µM 0.184× (z -28.2) |
| [[BT-474 (line)]] | alt | 236 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -20.2) |
| [[C-33 A (line)]] | alt | 283 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.282× (z -18.0) |
| [[CHP-212 (line)]] | wt | 194 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -13.6) |
| [[COLO 205 (line)]] | alt | 203 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -22.9) |
| [[NCI-H1792 (line)]] | alt | 220 | 1 | 3 | [[Ixazomib citrate (drug)]] 5 µM 1.81× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -23.6) |
| [[SW 900 (line)]] | alt | 150 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -16.9) |
| [[A-427 (line)]] | wt | 137 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.317× (z -16.5) |
| [[AN3 CA (line)]] | alt | 292 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.387× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 227 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -30.4) |
| [[NCI-H2347 (line)]] | alt | 136 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.392× (z -13.8) |
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.497× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 92.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.521× (z -8.7) |
| [[NCI-H661 (line)]] | alt | 230 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -9.4) |
| [[HCT15 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 251 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COP1]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[AHCYL2]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[BMPR1A]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[STIM1]] | +0.57 | +0.68 / +0.50 | both halves | 1e-05 | STRING 580 |
| [[NCOA2]] | +0.57 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[KPNA3]] | +0.57 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[RAP1GDS1]] | +0.57 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[SFMBT1]] | +0.56 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[ARHGEF11]] | +0.56 | +0.51 / +0.45 | both halves | 3e-05 | STRING 611 |
| [[PPP2R5E]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TCF12]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[MAN1A2]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFESD]] | -0.58 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[N4BP3]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[APBB3]] | -0.52 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[HIF1AN]] | -0.51 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[ZSCAN9]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[NFKB2]] | -0.49 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[INIP]] | -0.48 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[TAF1A]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[SCAT1]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ZMIZ2]] | -0.46 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[RARA]] | -0.46 | -0.49 / -0.36 | both halves | 9e-05 | STRING 777 |
| [[TBC1D10A]] | -0.46 | -0.33 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers GNAQ's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.288). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.0, 10.3); signed map (7.9, -1.7). **Vector** length 117, 38.0% of its response variance represented; |z| ≥ 3 in 1,517 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +8.8 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.7 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.3 | +0.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +7.1 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.6 | +5.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.2 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +4.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.8 | -41.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | -5.5 | -9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -5.5 | -11.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.5 | -38.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.6 | -3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.8 | -3.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit alpha q |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.2 — chr9:77,716,097-78,031,811 (-) |
| Ensembl biotype | protein_coding |
| Also known as | G-ALPHA-q, GAQ |
| Gene groups (HGNC) | G protein subunits alpha, group q |
| Reactome | 27 pathways, smallest: Fatty Acids bound to GPR40 (FFAR1) regulate insulin secretion; Acetylcholine regulates insulin secretion; Free fatty acids regulate insulin secretion |
| Matched by | ensembl_id |

**Function**, from UniProt [P50148](https://www.uniprot.org/uniprotkb/P50148) (Guanine nucleotide-binding protein G(q) subunit alpha):

> Guanine nucleotide-binding proteins (G proteins) function as transducers downstream of G protein-coupled receptors (GPCRs) in numerous signaling cascades. The alpha chain contains the guanine nucleotide binding site and alternates between an active, GTP-bound state and an inactive, GDP-bound state. Signaling by an activated GPCR promotes GDP release and GTP binding. The alpha subunit has a low GTPase activity that converts bound GTP to GDP, thereby terminating the signal. Both GDP release and …

**Summary**, from NCBI Gene [2776](https://www.ncbi.nlm.nih.gov/gene/2776):

> This locus encodes a guanine nucleotide-binding protein. The encoded protein, an alpha subunit in the Gq class, couples a seven-transmembrane domain receptor to activation of phospolipase C-beta. Mutations at this locus have been associated with problems in platelet activation and aggregation. A related pseudogene exists on chromosome 2.[provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:4390](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4390) · Entrez [2776](https://www.ncbi.nlm.nih.gov/gene/2776) · UniProt [P50148](https://www.uniprot.org/uniprotkb/P50148) · Ensembl [ENSG00000156052](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156052)

## Data

Gene col 7946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7946); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7946]; `tensor/DDL_lfc|DDL_z.npy` [7946]; `embed/gene_vectors.npy` [7946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7946 or target_col == 7946). Every well: [[GNAQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNAQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
