---
symbol: "MAST4"
type: "gene"
col: 909
ensembl_id: "ENSG00000069020"
name: "microtubule associated serine/threonine kinase family member 4"
location: "5q12.3"
module: 81
arm: "+"
pooled_cpm: 95.52
n_lines_expressing: 39
n_dd_up: 22
n_dd_down: 44
n_dd_up_clean: 20
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 17
direction_downstream: 18
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# MAST4

*microtubule associated serine/threonine kinase family member 4* — 5q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +19.9, q 0e+00, up in 27 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.433× (z -14.3, q 8e-44, down in 26 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.463× (z -14.3, q 1e-43, down in 34 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL2A1]] (+0.74, fdr 7e-06), [[MYH16]] (+0.66, fdr 7e-06), [[CORO2B]] (+0.65, fdr 1e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[ENKUR]] → it (grade B ⚠); 18 go from it, the strongest it → [[C3orf52]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 909.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +19.9 | 0e+00 | 27/37 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +9.8 | 3e-20 | 23/37 (SNU-423, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +8.7 | 6e-16 | 25/37 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.38×** | +8.5 | 2e-15 | 21/38 (SHP-77, Panc 03.27, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.58×** | +8.5 | 2e-15 | 28/37 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.55×** | +7.8 | 4e-13 | 27/37 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +5.9 | 4e-07 | 20/38 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.48×** | +5.6 | 1e-06 | 22/37 (Panc 03.27, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +5.3 | 6e-06 | 20/37 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM |  | **1.34×** | +5.2 | 1e-05 | 22/37 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.2 | 1e-05 | 18/37 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +5.0 | 2e-05 | 20/37 (LOX-IMVI, RKO, …) | rises with dose | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.65×** | +4.6 | 2e-04 | 17/36 (SW480, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.29×** | +4.5 | 2e-04 | 20/37 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.64×** | +4.5 | 2e-04 | 15/37 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 5e-04 | 17/37 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.2 | 8e-04 | 16/37 (NCI-H2347, RKO, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 59 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 909.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.433×** | -14.3 | 8e-44 | 26/34 (RKO, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.463×** | -14.3 | 1e-43 | 34/37 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -12.4 | 3e-33 | 32/37 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.509×** | -12.0 | 4e-31 | 28/32 (CFPAC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.552×** | -11.0 | 5e-26 | 27/37 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.575×** | -10.2 | 1e-22 | 28/36 (COLO 205, RKO, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.577×** | -10.2 | 2e-22 | 27/37 (H4, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.649×** | -8.0 | 9e-14 | 18/38 (RKO, H4, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.654×** | -7.9 | 2e-13 | 23/37 (H4, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.663×** | -7.6 | 2e-12 | 21/37 (A549, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.675×** | -7.3 | 2e-11 | 21/37 (RKO, H4, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.509×** | -6.1 | 4e-08 | 23/37 (RKO, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.712×** | -6.0 | 7e-08 | 19/37 (RKO, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.760×** | -5.9 | 2e-07 | 20/37 (RKO, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.787×** | -5.7 | 5e-07 | 18/37 (RKO, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.805×** | -5.7 | 5e-07 | 19/37 (H4, NCI-H1792, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.818×** | -5.2 | 5e-06 | 21/37 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.754×** | -5.2 | 6e-06 | 16/37 (NCI-H1792, H4, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.780×** | -5.2 | 7e-06 | 13/39 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 909. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 589 | 1 | 37 (14 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.05× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -24.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.216× (z -19.5) |
| [[H4 (line)]] | wt | 283 | 0 | 33 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0805× (z -17.8) |
| [[HOP62 (line)]] | alt | 55.2 | 1 | 15 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.92× (z +9.2) | [[Adagrasib (drug)]] 0.05 µM 0.519× (z -16.4) ⚠ position not correctable · without an alert: [[Dexamethasone (drug)]] 0.5 µM 0.238× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 214 | 0 | 16 (6 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.562× (z -17.4) ⚠ position not correctable · without an alert: [[Triamcinolone (drug)]] 0.5 µM 0.310× (z -10.1) |
| [[A498 (line)]] | wt | 25.1 | 15 (10 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 20.4× (z +24.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.74× (z +15.9) | — |
| [[NCI-H460 (line)]] | wt | 33.4 | 14 (8 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +27.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.54× (z +14.5) | — |
| [[LoVo (line)]] | wt | 144 | 6 (3 ⚠) | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.41× (z +24.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.30× (z +17.4) | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.313× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 179 | 2 | 9 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.19× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.322× (z -10.0) |
| [[SW480 (line)]] | alt | 173 | 1 | 10 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.206× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 206 | 8 (2 ⚠) | 2 (2 ⚠) | [[Peretinoin (drug)]] 5 µM 3.48× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -17.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 81.5 | 3 (1 ⚠) | 5 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +11.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 2.27× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.124× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -13.2) |
| [[LS 180 (line)]] | wt | 70.3 | 3 (3 ⚠) | 5 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.09× (z +15.1) ⚠ cell-cycle shift, explains ~31% of this change | [[Digitoxin (drug)]] 0.5 µM 0.159× (z -17.7) |
| [[CFPAC-1 (line)]] | alt | 226 | 3 (1 ⚠) | 4 (4 ⚠) | [[Peretinoin (drug)]] 5 µM 2.90× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -19.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 194 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -18.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 129 | 2 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.295× (z -12.1) |
| [[A-427 (line)]] | wt | 58.5 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -13.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 151 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0622× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -14.1) |
| [[CHP-212 (line)]] | wt | 109 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0506× (z -15.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 153 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 144 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -12.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 131 | 1 | 3 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.41× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 190 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 56.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.2) | [[Adagrasib (drug)]] 0.05 µM 0.648× (z -11.4) ⚠ position not correctable |
| [[HT-29 (line)]] | alt | 57.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +13.2) | — |
| [[SW1417 (line)]] | alt | 33.7 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.76× (z +13.6) | — |
| [[SW48 (line)]] | wt | 66.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.8) | [[Digitoxin (drug)]] 0.5 µM 0.163× (z -11.1) |
| [[BT-474 (line)]] | alt | 61.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +14.0) | — |
| [[HCT15 (line)]] | alt | 50.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 56.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 79.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.1) | — |
| [[J82 (line)]] | alt | 94.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.4) | — |
| [[KATO III (line)]] | alt | 54.9 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.03× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.639× (z -9.2) ⚠ position not correctable |
| [[RPMI-7951 (line)]] | alt | 50.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -8.7) |
| [[SW 900 (line)]] | alt | 80.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +14.0) | — |
| [[A-172 (line)]] | wt | 15.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 22.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 22.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.17 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 350 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 23.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 32.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 909), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2A1]] | +0.74 | +0.76 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[MYH16]] | +0.66 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.65 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[LINC00973]] | +0.64 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[MSANTD3]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[TMCC3]] | +0.64 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[KBTBD8]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[FAM43A]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[HBEGF]] | +0.63 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[ZNF697]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[TOMM34]] | +0.62 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[LINC01204]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 14, C 3. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENKUR]] | B | ENKUR activity raises MAST4's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.47× lower at baseline in the lines without ENKUR | 0.001 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[ICAM2]] | B | ICAM2 activity raises MAST4's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 3.00× lower at baseline in the lines without ICAM2 | 0.010 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[PLEK2]] | B | PLEK2 activity raises MAST4's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.93× lower at baseline in the lines without PLEK2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[IL11]] | B | IL11 activity raises MAST4's level | lines that do not express IL11 (27) vs lines expressing it (23) | 2.11× lower at baseline in the lines without IL11 | 0.035 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |
| [[MAP2K1]] | B | MAP2K1 activity raises MAST4's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.8% of all compounds | 0.038 | ⚠ off-target possible; 4 compounds |
| [[BMP2]] | B | BMP2 activity raises MAST4's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.29× lower at baseline in the lines without BMP2 | 0.045 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[KIAA1217]] | B | KIAA1217 activity raises MAST4's level | lines that do not express KIAA1217 (10) vs lines expressing it (40) | 2.59× lower at baseline in the lines without KIAA1217 | 0.049 | ⚠ within organs, on part of the lines; also absent: FAM107B, MET, S100A16 |
| [[LAMB3]] | B | LAMB3 activity raises MAST4's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 2.32× lower at baseline in the lines without LAMB3 | 0.055 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[IL31RA]] | B | IL31RA activity raises MAST4's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 1.90× lower at baseline in the lines without IL31RA | 0.058 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1 |
| [[GNA15]] | B | GNA15 activity raises MAST4's level | lines that do not express GNA15 (25) vs lines expressing it (25) | 1.93× lower at baseline in the lines without GNA15 | 0.063 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent |
| [[NIPAL1]] | B | NIPAL1 activity raises MAST4's level | lines that do not express NIPAL1 (5) vs lines expressing it (45) | 4.75× lower at baseline in the lines without NIPAL1 | 0.070 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[ADTRP]] | B | ADTRP activity raises MAST4's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 1.64× lower at baseline in the lines without ADTRP | 0.092 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 17, C 1. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C3orf52]] | B | MAST4 activity raises C3orf52's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without MAST4 | 0.007 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[KIAA1217]] | B | MAST4 activity raises KIAA1217's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 2.70× lower at baseline in the lines without MAST4 | 0.010 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[AMOTL1]] | B | MAST4 activity raises AMOTL1's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without MAST4 | 0.022 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[NIPAL1]] | B | MAST4 activity raises NIPAL1's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without MAST4 | 0.022 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[CA13]] | B | MAST4 activity raises CA13's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 2.27× lower at baseline in the lines without MAST4 | 0.030 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[DTNA]] | B | MAST4 activity raises DTNA's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 2.63× lower at baseline in the lines without MAST4 | 0.039 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[ENKUR]] | B | MAST4 activity raises ENKUR's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 2.49× lower at baseline in the lines without MAST4 | 0.050 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[PKIA]] | B | MAST4 activity raises PKIA's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 3.18× lower at baseline in the lines without MAST4 | 0.057 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[DNAH17]] | B | MAST4 activity raises DNAH17's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 2.12× lower at baseline in the lines without MAST4 | 0.072 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[ITGA2]] | B | MAST4 activity raises ITGA2's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 2.22× lower at baseline in the lines without MAST4 | 0.085 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[SCAT1]] | B | MAST4 activity raises SCAT1's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 2.00× lower at baseline in the lines without MAST4 | 0.086 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[ICAM2]] | B | MAST4 activity raises ICAM2's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 1.63× lower at baseline in the lines without MAST4 | 0.089 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.4, 1.4); signed map (13.3, 45.5). **Vector** length 135, 41.8% of its response variance represented; |z| ≥ 3 in 1,668 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +19.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.3 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.6 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +5.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +9.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.4 | +7.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.9 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +2.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +5.0 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.7 | -11.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.4 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.0 | -14.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.8 | -5.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -4.5 | -3.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.4 | -5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.3 | -7.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.3 | -1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.2 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated serine/threonine kinase family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.3 — chr5:66,596,380-67,169,593 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0303 |
| Gene groups (HGNC) | PDZ domain containing; Microtubule associated serine/threonine kinase family |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

UniProt [O15021](https://www.uniprot.org/uniprotkb/O15021) carries no function annotation.

**Summary**, from NCBI Gene [375449](https://www.ncbi.nlm.nih.gov/gene/375449):

> This gene encodes a member of the microtubule-associated serine/threonine protein kinases. The proteins in this family contain a domain that gives the kinase the ability to determine its own scaffold to control the effects of their kinase activities. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:19037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19037) · Entrez [375449](https://www.ncbi.nlm.nih.gov/gene/375449) · UniProt [O15021](https://www.uniprot.org/uniprotkb/O15021) · Ensembl [ENSG00000069020](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069020)

## Data

Gene col 909: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 909); `tables/drug_effects.parquet` (82 rows, flagged included); `relations/gene_relations.parquet` (col_a == 909, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 909]; `tensor/DDL_lfc|DDL_z.npy` [909]; `embed/gene_vectors.npy` [909]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 909 or target_col == 909). Every well: [[MAST4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAST4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
