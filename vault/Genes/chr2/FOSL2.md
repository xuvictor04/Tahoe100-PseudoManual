---
symbol: "FOSL2"
type: "gene"
col: 1121
ensembl_id: "ENSG00000075426"
name: "FOS like 2, AP-1 transcription factor subunit"
location: "2p23.2"
module: 123
arm: "+"
pooled_cpm: 92.13
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 19
n_dd_up_clean: 23
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# FOSL2

*FOS like 2, AP-1 transcription factor subunit* — 2p23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.16× (z +18.8, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.376× (z -16.9, q 0e+00, down in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.669× (z -6.6, q 4e-09, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPH2]] (+0.75, fdr 7e-06), [[ETS2]] (+0.68, fdr 7e-06), [[BCL9L]] (+0.66, fdr 7e-06); moves opposite to [[FXYD5]] (-0.60, fdr 1e-05), [[GDAP2]] (-0.60, fdr 1e-05), [[AP3M2]] (-0.59, fdr 1e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[BHLHE41]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 3 with an alert ⚠; shown: the 15 strongest. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1121.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.16×** | +18.8 | 0e+00 | 40/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.90×** | +14.4 | 2e-44 | 48/49 (COLO 205, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.15×** | +12.7 | 8e-35 | 36/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +9.2 | 5e-18 | 34/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +7.7 | 2e-12 | 36/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +7.4 | 1e-11 | 35/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.43×** | +6.6 | 3e-09 | 36/50 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.01×** | +6.3 | 2e-08 | 31/48 (HOP62, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +5.4 | 4e-06 | 31/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +5.3 | 6e-06 | 29/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 9e-06 | 27/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 1e-04 | 30/49 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +4.7 | 1e-04 | 28/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +4.6 | 1e-04 | 26/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +4.5 | 2e-04 | 27/49 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1121.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.376×** | -16.9 | 0e+00 | 47/48 (A498, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.448×** | -13.9 | 2e-41 | 46/48 (A498, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.490×** | -12.3 | 1e-32 | 48/48 (HT-29, SW 900, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.627×** | -11.4 | 4e-28 | 38/49 (A498, SW 900, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.581×** | -9.0 | 2e-17 | 39/43 (LOX-IMVI, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.646×** | -7.6 | 4e-12 | 28/48 (HepG2/C3A, LOX-IMVI, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.669×** | -6.6 | 4e-09 | 34/48 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.693×** | -6.3 | 2e-08 | 32/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **0.686×** | -6.3 | 2e-08 | 32/47 (COLO 205, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.526×** | -5.8 | 4e-07 | 30/45 (SW 900, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.718×** | -5.5 | 2e-06 | 31/50 (SNU-423, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.757×** | -4.6 | 2e-04 | 25/48 (HT-29, A498, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.757×** | -4.6 | 2e-04 | 24/47 (C-33 A, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.766×** | -4.6 | 2e-04 | 26/48 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.858× | -3.8 | 0.006 | 15/49 (HT-29, KATO III, …) | all doses, flat | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.815×** | -3.5 | 0.013 | 15/48 (SW480, Panc 03.27, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.816×** | -3.5 | 0.014 | 25/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 0.838× | -3.1 | 0.059 | 12/48 (LoVo, SW48, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 124 | 8 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.48× (z +13.5) | [[Ixazomib citrate (drug)]] 5 µM 0.378× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.392× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 80.5 | 11 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +27.5) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[A498 (line)]] | wt | 147 | 5 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +25.4) | [[Panobinostat (drug)]] 5 µM 0.287× (z -16.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LOX-IMVI (line)]] | wt | 105 | 1 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.322× (z -11.0) |
| [[A-172 (line)]] | wt | 116 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[hTERT-HPNE (line)]] | wt | 112 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[NCI-H1573 (line)]] | alt | 98.9 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +24.0) | [[Panobinostat (drug)]] 5 µM 0.323× (z -12.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[COLO 205 (line)]] | alt | 153 | 2 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 22.0× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.233× (z -13.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HS-578T (line)]] | alt | 76.0 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +20.9) | [[Panobinostat (drug)]] 5 µM 0.429× (z -8.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 181 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -14.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.346× (z -10.0) |
| [[A549 (line)]] | wt | 125 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[CFPAC-1 (line)]] | alt | 152 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.369× (z -10.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 142 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -15.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 122 | 1 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 7.03× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.215× (z -14.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[RPMI-7951 (line)]] | alt | 133 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.328× (z -10.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW1417 (line)]] | alt | 102 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.332× (z -12.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2347 (line)]] | alt | 61.6 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.5× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -11.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 55.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.7) | — |
| [[SW480 (line)]] | alt | 99.8 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.12× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.345× (z -12.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-427 (line)]] | wt | 44.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[MIA PaCa-2 (line)]] | alt | 92.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +17.2) | — |
| [[Panc 03.27 (line)]] | alt | 74.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[SNU-423 (line)]] | alt | 95.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 110 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -17.0) ⚠ toxic; cell-cycle shift, explains ~40% of this change |
| [[J82 (line)]] | alt | 64.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.8) | — |
| [[KATO III (line)]] | alt | 123 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.276× (z -12.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 101 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -13.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 85.3 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.52× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.330× (z -10.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 50.7 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.0× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[C32 (line)]] | wt | 52.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +12.0) | — |
| [[H4 (line)]] | wt | 89.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 90.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[HepG2_C3A (line)]] | wt | 98.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[LS 180 (line)]] | wt | 85.7 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.314× (z -11.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 85.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 36.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 85.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.6) | — |
| [[BT-474 (line)]] | alt | 66.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -9.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.395× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[Hs 766T (line)]] | wt | 73.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPH2]] | +0.75 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[ETS2]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 606 |
| [[BCL9L]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[AJUBA]] | +0.65 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[ARID5B]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[AMOTL2]] | +0.64 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[REPIN1]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CPEB2]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[BCL3]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 415 |
| [[PPP1R3B]] | +0.61 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[TIGD2]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FXYD5]] | -0.60 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[GDAP2]] | -0.60 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[AP3M2]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[IQCB1]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ANKRD39]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[MFN1]] | -0.58 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[NAP1L4]] | -0.57 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[CTNNBIP1]] | -0.57 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[NAPG]] | -0.56 | -0.57 / -0.36 | both halves | 9e-05 |  |
| [[SMG1P5]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SCAI]] | -0.56 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[COG5]] | -0.56 | -0.53 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BHLHE41]] | B | BHLHE41 activity raises FOSL2's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without BHLHE41 | 0.010 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[CXCL2]] | B | CXCL2 activity raises FOSL2's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.51× lower at baseline in the lines without CXCL2 | 0.032 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[C3]] | B | C3 activity raises FOSL2's level | lines that do not express C3 (32) vs lines expressing it (18) | 1.38× lower at baseline in the lines without C3 | 0.041 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11 |
| [[KMO]] | B | KMO activity raises FOSL2's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without KMO | 0.043 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[ZC3H12A]] | B | ZC3H12A activity raises FOSL2's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 1.83× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[CFAP300]] | B | CFAP300 activity raises FOSL2's level | lines that do not express CFAP300 (18) vs lines expressing it (32) | 1.31× lower at baseline in the lines without CFAP300 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, ARID1A; also absent: MYPN, GATA3, CCL5 |
| [[TNFSF14]] | B | TNFSF14 activity raises FOSL2's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.37× lower at baseline in the lines without TNFSF14 | 0.076 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers FOSL2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DNAH5]] | B | DNAH5 activity raises FOSL2's level | lines that do not express DNAH5 (10) vs lines expressing it (40) | 1.44× lower at baseline in the lines without DNAH5 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC02966; maybe low, not absent |
| [[LINC02057]] | B | LINC02057 activity raises FOSL2's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 1.36× lower at baseline in the lines without LINC02057 | 0.086 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[ARID5B]] | B | ARID5B activity raises FOSL2's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without ARID5B | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[TNFAIP3]] | C | TNFAIP3 activity raises FOSL2's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 1.71× lower at baseline in the lines without TNFAIP3 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.9, 13.0); signed map (48.6, 12.8). **Vector** length 136, 45.2% of its response variance represented; |z| ≥ 3 in 1,427 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Signaling by Hippo* (reactome, mean cos +0.54 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.3 | +18.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.0 | +9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.4 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.0 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.9 | +14.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +7.1 | +4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +6.8 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.8 | +5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +6.7 | +4.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.8 | -6.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.0 | -6.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.5 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.3 | -16.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.7 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.1 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | FOS like 2, AP-1 transcription factor subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.2 — chr2:28,392,448-28,417,317 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FRA2, FLJ23306 |
| Gene groups (HGNC) | Fos transcription factor family |
| Hallmark sets | HYPOXIA, TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [P15408](https://www.uniprot.org/uniprotkb/P15408) (Fos-related antigen 2):

> Controls osteoclast survival and size (By similarity). As a dimer with JUN, activates LIF transcription (By similarity). Activates CEBPB transcription in PGE2-activated osteoblasts (By similarity).

**Summary**, from NCBI Gene [2355](https://www.ncbi.nlm.nih.gov/gene/2355):

> The Fos gene family consists of 4 members: FOS, FOSB, FOSL1, and FOSL2. These genes encode leucine zipper proteins that can dimerize with proteins of the JUN family, thereby forming the transcription factor complex AP-1. As such, the FOS proteins have been implicated as regulators of cell proliferation, differentiation, and transformation. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:3798](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3798) · Entrez [2355](https://www.ncbi.nlm.nih.gov/gene/2355) · UniProt [P15408](https://www.uniprot.org/uniprotkb/P15408) · Ensembl [ENSG00000075426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075426)

## Data

Gene col 1121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1121); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1121]; `tensor/DDL_lfc|DDL_z.npy` [1121]; `embed/gene_vectors.npy` [1121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1121 or target_col == 1121). Every well: [[FOSL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOSL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
