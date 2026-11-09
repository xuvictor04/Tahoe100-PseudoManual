---
symbol: "RBM25"
type: "gene"
col: 4106
ensembl_id: "ENSG00000119707"
name: "RNA binding motif protein 25"
location: "14q24.2"
module: 12
arm: "+"
pooled_cpm: 424.9
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# RBM25

*RNA binding motif protein 25* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.87× (z +15.1, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.02× (z +12.0, q 7e-31, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.838× (z -4.3, q 0.010, down in 24 of 49 measured lines) ⚠ cell-cycle shift, explains ~5% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.785× (z -4.1, q 0.010, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC2]] (+0.70, fdr 7e-06), [[EIF5B]] (+0.68, fdr 7e-06), [[PNN]] (+0.68, fdr 7e-06); moves opposite to [[BSG]] (-0.61, fdr 1e-05), [[FKBP1A]] (-0.59, fdr 2e-05), [[GNS]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → [[METAP2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4106.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.87×** | +15.1 | 0e+00 | 46/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +13.3 | 4e-38 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.05×** | +12.2 | 8e-32 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +12.0 | 7e-31 | 47/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +10.4 | 2e-23 | 48/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.69×** | +8.9 | 6e-17 | 48/48 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.58×** | +7.7 | 8e-13 | 48/48 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +7.6 | 3e-12 | 45/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.58×** | +7.5 | 4e-12 | 41/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +7.2 | 4e-11 | 46/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.97×** | +6.0 | 9e-08 | 44/45 (RKO, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +5.9 | 2e-07 | 39/48 (A-427, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.62×** | +5.9 | 2e-07 | 46/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.39×** | +5.3 | 4e-06 | 36/47 (NCI-H1792, COLO 205, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.81×** | +5.3 | 5e-06 | 38/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.37×** | +5.1 | 2e-05 | 35/47 (SW48, BT-474, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.9 | 3e-05 | 36/48 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.2 | 7e-04 | 31/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.018 | 40/48 (SW480, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.020 | 25/48 (HT-29, HCT15, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.023 | 30/48 (NCI-H1792, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.023 | 36/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.024 | 38/48 (NCI-H460, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.024 | 41/48 (LS 180, SHP-77, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4106.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.838× | -4.3 | 0.010 | 24/49 (SW48, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.785×** | -4.1 | 0.010 | 35/48 (SW48, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.799×** | -3.8 | 0.023 | 36/49 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.802×** | -3.8 | 0.023 | 33/48 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.863× | -3.6 | 0.040 | 11/48 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.832× | -3.1 | 0.15 | 23/48 (NCI-H23, LoVo, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4106. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 302 | 11 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +26.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.65× (z +16.6) | — |
| [[NCI-H460 (line)]] | wt | 339 | 10 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +15.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +11.8) | — |
| [[COLO 205 (line)]] | alt | 316 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +20.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 406 | 9 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +21.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +14.4) | — |
| [[SW480 (line)]] | alt | 480 | 9 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.68× (z +16.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.93× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 250 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.44× (z +10.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 585 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.53× (z +12.4) | — |
| [[A-172 (line)]] | wt | 407 | 7 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.26× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.01× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 445 | 7 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.88× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.61× (z +12.1) | — |
| [[C32 (line)]] | wt | 288 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +19.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +13.3) | — |
| [[H4 (line)]] | wt | 346 | 7 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.81× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.23× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 419 | 6 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +15.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.10× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.631× (z -10.0) ⚠ cell-cycle shift, explains ~5% of this change |
| [[PANC-1 (line)]] | alt | 364 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +15.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.52× (z +13.5) | — |
| [[A549 (line)]] | wt | 339 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +18.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.29× (z +13.7) | — |
| [[CFPAC-1 (line)]] | alt | 405 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +19.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +14.7) | — |
| [[LoVo (line)]] | wt | 508 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +14.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.77× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 376 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.51× (z +11.8) | — |
| [[NCI-H23 (line)]] | alt | 513 | 6 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.57× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 318 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.5) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.63× (z +11.6) | — |
| [[SW 900 (line)]] | alt | 468 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +16.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +11.5) | — |
| [[A498 (line)]] | wt | 315 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.97× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -10.5) ⚠ cell-cycle shift, explains ~5% of this change |
| [[HepG2_C3A (line)]] | wt | 497 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.85× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 353 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +11.9) | — |
| [[Hs 766T (line)]] | wt | 261 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.33× (z +10.6) | — |
| [[KATO III (line)]] | alt | 295 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +15.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.95× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 426 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +13.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.94× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 517 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 238 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +14.1) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.42× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 489 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.8) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[RKO (line)]] | wt | 534 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 1.93× (z +9.7) | — |
| [[SNU-1 (line)]] | wt | 474 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +9.6) | — |
| [[A-427 (line)]] | wt | 395 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.01× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.446× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 466 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.33× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 262 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 332 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.19× (z +10.2) | — |
| [[J82 (line)]] | alt | 412 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.07× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 724 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.29× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 787 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.6) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 398 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +16.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 526 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +9.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW48 (line)]] | wt | 866 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.68× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -12.4) ⚠ cell-cycle shift, explains ~5% of this change |
| [[AN3 CA (line)]] | alt | 546 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.60× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 537 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.99× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 405 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 383 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 440 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 445 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 388 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 377 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 492 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4106), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC2]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[EIF5B]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[PNN]] | +0.68 | +0.75 / +0.61 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 812 |
| [[EIF3A]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[IWS1]] | +0.65 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[ZC3H13]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 | STRING 519 |
| [[DDX27]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 | STRING 458 |
| [[PRPF38B]] | +0.62 | +0.65 / +0.50 | both halves | 1e-05 | STRING 837 |
| [[PRRC2C]] | +0.61 | +0.68 / +0.50 | both halves | 1e-05 | STRING 999 |
| [[PPIG]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 627 |
| [[SRSF11]] ⚠ | +0.60 | +0.58 / +0.56 | both halves | 1e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 967; ⚠ in the vector space only through flagged drug-doses |
| [[MRPL45P2]] | +0.60 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[NEMF]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 | STRING 407 |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BSG]] | -0.61 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[FKBP1A]] | -0.59 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[GNS]] | -0.58 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[MDH2]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[AP2M1]] | -0.57 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[EDEM1]] | -0.57 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[PGAM1]] | -0.55 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[LAMP2]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[NAGA]] | -0.54 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[CREG1]] | -0.54 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[CD164]] | -0.54 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[ITM2C]] | -0.54 | -0.54 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises RBM25's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[METAP2]] | C | RBM25's natural level weakens METAP2's drug response | RBM25's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.17; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.402). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-39.5, -0.5); signed map (-1.8, -18.3). **Vector** length 97.0, 43.8% of its response variance represented; |z| ≥ 3 in 1,436 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.7 | +10.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.9 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +4.6 | +15.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.3 | +5.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.1 | +6.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +3.8 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +4.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +3.3 | +2.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.4 | +5.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.3 | +7.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.9 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.9 | -2.4 |
|  | [[Lopinavir (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -2.6 | -1.7 |
|  | [[Erlotinib (drug)]] 5 µM |  | -2.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:73,058,532-73,123,899 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S164, fSAP94, NET52, Snu71; previously RNPC7 |
| Gene groups (HGNC) | RNA binding motif containing; Spliceosomal A complex |
| Reactome | 6 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P49756](https://www.uniprot.org/uniprotkb/P49756) (RNA-binding protein 25):

> RNA-binding protein that acts as a regulator of alternative pre-mRNA splicing. Involved in apoptotic cell death through the regulation of the apoptotic factor BCL2L1 isoform expression. Modulates the ratio of pro-apoptotic BCL2L1 isoform S to anti-apoptotic BCL2L1 isoform L mRNA expression. When overexpressed, stimulates pro-apoptotic BCL2L1 isoform S 5'-splice site (5'-ss) selection, whereas its depletion caused the accumulation of anti-apoptotic BCL2L1 isoform L. Promotes BCL2L1 isoform S …

**Summary**, from NCBI Gene [58517](https://www.ncbi.nlm.nih.gov/gene/58517):

> Enables mRNA binding activity. Involved in regulation of alternative mRNA splicing, via spliceosome and regulation of apoptotic process. Located in nuclear speck. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23244) · Entrez [58517](https://www.ncbi.nlm.nih.gov/gene/58517) · UniProt [P49756](https://www.uniprot.org/uniprotkb/P49756) · Ensembl [ENSG00000119707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119707)

## Data

Gene col 4106: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4106); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4106, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4106]; `tensor/DDL_lfc|DDL_z.npy` [4106]; `embed/gene_vectors.npy` [4106]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4106 or target_col == 4106). Every well: [[RBM25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
