---
symbol: "SLC44A3-AS1"
type: "gene"
col: 13379
ensembl_id: "ENSG00000224081"
name: "SLC44A3 antisense RNA 1"
location: "1p21.3"
module: 8
arm: "+"
pooled_cpm: 28.96
n_lines_expressing: 37
n_dd_up: 26
n_dd_down: 26
n_dd_up_clean: 21
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 62
direction_downstream: 49
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SLC44A3-AS1

*SLC44A3 antisense RNA 1* — 1p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +6.9, q 4e-09, up in 15 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.371× (z -17.0, q 0e+00, down in 30 of 35 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.264× (z -16.2, q 0e+00, down in 35 of 35 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC44A3]] (+0.72, fdr 7e-06), [[PLCH1]] (+0.68, fdr 1e-05), [[SAMD12-AS1]] (+0.63, fdr 1e-05); moves opposite to [[DNAAF9]] (-0.57, fdr 3e-05), [[GCAT]] (-0.51, fdr 4e-05), [[EPOR]] (-0.50, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 62 arrows point to it, the strongest [[ERBB3]] → it (grade B ⚠); 49 go from it, the strongest it → [[ERBB3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13379.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.9 | 4e-09 | 15/35 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.71×** | +6.3 | 1e-07 | 24/33 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +5.4 | 1e-05 | 13/35 (RPMI-7951, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +5.4 | 1e-05 | 16/34 (J82, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.53×** | +5.1 | 3e-05 | 20/34 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.51×** | +4.9 | 9e-05 | 23/36 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.51×** | +4.8 | 1e-04 | 17/33 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 5e-04 | 19/35 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.45×** | +4.4 | 5e-04 | 19/36 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.32×** | +4.4 | 6e-04 | 20/35 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.3 | 8e-04 | 16/35 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.28×** | +4.2 | 0.002 | 15/35 (AsPC-1, A-427, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.003 | 12/35 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.003 | 17/33 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +3.9 | 0.004 | 9/33 (J82, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.004 | 13/35 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.004 | 13/35 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.40×** | +3.8 | 0.005 | 13/34 (SW480, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13379.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.371×** | -17.0 | 0e+00 | 30/35 (LoVo, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.264×** | -16.2 | 0e+00 | 35/35 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.298×** | -14.7 | 0e+00 | 31/33 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.339×** | -13.1 | 3e-37 | 29/34 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.377×** | -11.9 | 2e-30 | 31/33 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.423×** | -10.0 | 9e-22 | 29/34 (NCI-H1573, COLO 205, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.452×** | -9.7 | 4e-20 | 28/35 (LoVo, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.547×** | -7.3 | 2e-11 | 22/35 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.332×** | -7.0 | 2e-10 | 26/36 (HEC-1-A, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.579×** | -6.6 | 2e-09 | 24/35 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.567×** | -6.6 | 2e-09 | 21/31 (HCT15, SK-MEL-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.589×** | -6.4 | 6e-09 | 23/34 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.732×** | -5.4 | 3e-06 | 21/36 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.648×** | -5.3 | 5e-06 | 20/34 (NCI-H1573, A549, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.454×** | -5.0 | 2e-05 | 22/32 (SK-MEL-2, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.665×** | -5.0 | 2e-05 | 22/35 (NCI-H2030, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.689×** | -4.5 | 2e-04 | 14/34 (SK-MEL-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.689×** | -4.5 | 2e-04 | 22/35 (C32, SNU-423, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.775×** | -4.4 | 3e-04 | 14/36 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.718×** | -4.0 | 0.001 | 20/34 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.555×** | -3.7 | 0.004 | 15/32 (Panc 03.27, LoVo, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.69 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13379. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 111 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0725× (z -33.2) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.129× (z -18.4) |
| [[Panc 03.27 (line)]] | alt | 89.4 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -20.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.203× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 116 | 0 | 10 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.154× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -10.5) |
| [[LS 180 (line)]] | wt | 53.6 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -18.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 50.9 | 1 | 7 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.0965× (z -24.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 47.2 | 1 (1 ⚠) | 7 (4 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.64× (z +11.6) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -21.3) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0916× (z -16.1) |
| [[HT-29 (line)]] | alt | 50.0 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -17.9) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -12.2) |
| [[SW480 (line)]] | alt | 22.1 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.139× (z -14.9) |
| [[COLO 205 (line)]] | alt | 45.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0431× (z -28.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.186× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 81.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -20.7) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.325× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 37.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -14.7) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0959× (z -13.5) |
| [[AsPC-1 (line)]] | alt | 63.1 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0662× (z -20.8) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 44.1 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -13.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 46.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -14.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -9.6) |
| [[KATO III (line)]] | alt | 31.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -15.7) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.174× (z -10.7) |
| [[A-427 (line)]] | wt | 23.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -10.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 15.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -14.0) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SW1417 (line)]] | alt | 18.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -15.2) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -11.0) |
| [[A498 (line)]] | wt | 10.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0989× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.102× (z -9.2) |
| [[HCT15 (line)]] | alt | 36.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0432× (z -15.8) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[SW 900 (line)]] | alt | 28.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0278× (z -17.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -10.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SNU-423 (line)]] | alt | 10.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.05× (z +8.5) | — |
| [[SW48 (line)]] | wt | 18.1 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0868× (z -9.6) |
| [[A-172 (line)]] | wt | 5.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.80 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.18 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.99 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.29 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13379), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC44A3]] | +0.72 | +0.78 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[PLCH1]] | +0.68 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[SAMD12-AS1]] | +0.63 | +0.57 / +0.54 | both halves | 1e-05 | same gene group |
| [[HNF4G]] | +0.62 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[KLHL2P1]] | +0.62 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[PROM1]] | +0.62 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[FAM149A]] | +0.59 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[ACTR3C]] | +0.58 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[CCSER1]] | +0.58 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[SYK]] | +0.58 | +0.62 / +0.39 | both halves | 5e-05 |  |
| [[SPATA6L]] | +0.57 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[PLEKHS1]] | +0.57 | +0.46 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.57 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[GCAT]] | -0.51 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[EPOR]] | -0.50 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[POLM]] | -0.49 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[IFT88]] | -0.49 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[MTRES1]] | -0.47 | -0.29 / -0.38 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 60, C 2. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERBB3]] | B | ERBB3 activity raises SLC44A3-AS1's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 4.01× lower at baseline in the lines without ERBB3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[HSH2D]] | B | HSH2D activity raises SLC44A3-AS1's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 4.14× lower at baseline in the lines without HSH2D | 3e-04 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[TOX3]] | B | TOX3 activity raises SLC44A3-AS1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 3.39× lower at baseline in the lines without TOX3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[SPINT1-AS1]] | B | SPINT1-AS1 activity raises SLC44A3-AS1's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 3.52× lower at baseline in the lines without SPINT1-AS1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[FAAH2]] | B | FAAH2 activity raises SLC44A3-AS1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.55× lower at baseline in the lines without FAAH2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[TMPRSS2]] | B | TMPRSS2 activity raises SLC44A3-AS1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.07× lower at baseline in the lines without TMPRSS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[TMC4]] | B | TMC4 activity raises SLC44A3-AS1's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.84× lower at baseline in the lines without TMC4 | 0.002 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[GRHL2]] | B | GRHL2 activity raises SLC44A3-AS1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 3.17× lower at baseline in the lines without GRHL2 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[CATSPERB]] | B | CATSPERB activity raises SLC44A3-AS1's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 2.94× lower at baseline in the lines without CATSPERB | 0.003 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[PCAT1]] | B | PCAT1 activity raises SLC44A3-AS1's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 3.09× lower at baseline in the lines without PCAT1 | 0.004 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[PLEKHG1]] | B | PLEKHG1 activity raises SLC44A3-AS1's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.76× lower at baseline in the lines without PLEKHG1 | 0.004 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[NPNT]] | B | NPNT activity raises SLC44A3-AS1's level | lines that do not express NPNT (33) vs lines expressing it (17) | 3.02× lower at baseline in the lines without NPNT | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |

### Downstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 47, C 2. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERBB3]] | B | SLC44A3-AS1 activity raises ERBB3's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 4.65× lower at baseline in the lines without SLC44A3-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[SPINT1-AS1]] | B | SLC44A3-AS1 activity raises SPINT1-AS1's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.31× lower at baseline in the lines without SLC44A3-AS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[PLEKHG1]] | B | SLC44A3-AS1 activity raises PLEKHG1's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.28× lower at baseline in the lines without SLC44A3-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[STYK1]] | B | SLC44A3-AS1 activity raises STYK1's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.58× lower at baseline in the lines without SLC44A3-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[TMC4]] | B | SLC44A3-AS1 activity raises TMC4's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.96× lower at baseline in the lines without SLC44A3-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[OCLN]] | B | SLC44A3-AS1 activity raises OCLN's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 4.09× lower at baseline in the lines without SLC44A3-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[HSH2D]] | B | SLC44A3-AS1 activity raises HSH2D's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.20× lower at baseline in the lines without SLC44A3-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[FAAH2]] | B | SLC44A3-AS1 activity raises FAAH2's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.22× lower at baseline in the lines without SLC44A3-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[FRK]] | B | SLC44A3-AS1 activity raises FRK's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.99× lower at baseline in the lines without SLC44A3-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[PCAT1]] | B | SLC44A3-AS1 activity raises PCAT1's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without SLC44A3-AS1 | 0.017 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[GRHL2]] | B | SLC44A3-AS1 activity raises GRHL2's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.70× lower at baseline in the lines without SLC44A3-AS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[KSR2]] | B | SLC44A3-AS1 activity raises KSR2's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.88× lower at baseline in the lines without SLC44A3-AS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.6, 51.6); signed map (58.1, 0.4). **Vector** length 95.0, 24.9% of its response variance represented; |z| ≥ 3 in 1,141 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +6.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | -0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +4.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.8 | -6.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | -6.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | -7.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.1 | -9.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -5.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -0.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SLC44A3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p21.3 — chr1:94,672,918-94,674,161 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | ; previously LINC01057 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49057) · Entrez [101928079](https://www.ncbi.nlm.nih.gov/gene/101928079) · Ensembl [ENSG00000224081](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224081)

## Data

Gene col 13379: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13379); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13379, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13379]; `tensor/DDL_lfc|DDL_z.npy` [13379]; `embed/gene_vectors.npy` [13379]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13379 or target_col == 13379). Every well: [[SLC44A3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC44A3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
