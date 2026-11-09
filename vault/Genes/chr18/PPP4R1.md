---
symbol: "PPP4R1"
type: "gene"
col: 7846
ensembl_id: "ENSG00000154845"
name: "protein phosphatase 4 regulatory subunit 1"
location: "18p11.22"
module: 214
arm: "+"
pooled_cpm: 97.26
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/214"]
generated_by: "tahoemap"
---

# PPP4R1

*protein phosphatase 4 regulatory subunit 1* — 18p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.74× (z +10.5, q 8e-23, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.331× (z -21.0, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KPNA1]] (+0.70, fdr 1e-05), [[ARHGAP17]] (+0.63, fdr 1e-05), [[PDS5B]] (+0.61, fdr 1e-05); moves opposite to [[MYSM1]] (-0.61, fdr 2e-05), [[SCFD1]] (-0.55, fdr 1e-05), [[ARF4]] (-0.54, fdr 8e-05).
> It is in [[Module 214]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7846.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +10.5 | 8e-23 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +8.0 | 4e-13 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +7.5 | 2e-11 | 33/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.08×** | +7.2 | 7e-11 | 33/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +6.8 | 8e-10 | 31/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +6.5 | 6e-09 | 35/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 2e-04 | 24/48 (PANC-1, LoVo, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +4.7 | 2e-04 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.003 | 22/48 (LS 180, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.7 | 0.012 | 11/49 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.017 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.021 | 21/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.023 | 10/48 (NCI-H1573, SNU-423, …) | all doses, flat | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.026 | 17/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.039 | 15/48 (SNU-423, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 1.20× | +3.2 | 0.041 | 14/49 (A-427, J82, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.073 | 16/48 (NCI-H2030, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7846.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.331×** | -21.0 | 0e+00 | 46/48 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.340×** | -20.5 | 0e+00 | 46/48 (A549, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.467×** | -14.5 | 4e-45 | 46/48 (A549, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -10.9 | 1e-25 | 39/49 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.578×** | -10.4 | 3e-23 | 38/49 (AsPC-1, Hs 766T, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.591×** | -9.6 | 7e-20 | 32/44 (NCI-H23, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.612×** | -8.6 | 5e-16 | 30/45 (A-172, LoVo, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.662×** | -7.8 | 3e-13 | 33/48 (HEC-1-A, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.655×** | -7.7 | 7e-13 | 36/50 (Panc 03.27, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.752×** | -7.7 | 1e-12 | 25/48 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.753×** | -7.6 | 1e-12 | 32/48 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.659×** | -7.6 | 1e-12 | 37/48 (SW480, SW 1271, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.704×** | -6.4 | 6e-09 | 31/47 (NCI-H2347, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.736×** | -5.8 | 2e-07 | 29/48 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.764×** | -5.1 | 1e-05 | 30/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.794×** | -4.4 | 4e-04 | 22/48 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.813×** | -3.9 | 0.003 | 18/48 (NCI-H1573, A-172, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.877× | -3.5 | 0.012 | 17/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.838× | -3.4 | 0.021 | 21/49 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.839× | -3.3 | 0.021 | 16/48 (A-172, RPMI-7951, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.745×** | -2.9 | 0.081 | 16/48 (RPMI-7951, HT-29, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7846. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 224 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -16.8) |
| [[A-172 (line)]] | wt | 96.9 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 190 | 2 (1 ⚠) | 8 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.30× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.21× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -24.5) |
| [[NCI-H460 (line)]] | wt | 83.4 | 2 | 8 (3 ⚠) | [[Digitoxin (drug)]] 0.05 µM 2.09× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.282× (z -16.5) |
| [[Panc 03.27 (line)]] | alt | 164 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -21.4) |
| [[SW480 (line)]] | alt | 66.5 | 6 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.256× (z -18.1) |
| [[PANC-1 (line)]] | alt | 71.3 | 6 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +16.1) | [[Panobinostat (drug)]] 5 µM 0.286× (z -18.3) |
| [[AsPC-1 (line)]] | alt | 212 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -20.7) |
| [[BT-474 (line)]] | alt | 144 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -14.2) |
| [[Hs 766T (line)]] | wt | 181 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0939× (z -24.4) |
| [[A-427 (line)]] | wt | 200 | 2 (1 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.90× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.280× (z -16.8) |
| [[A549 (line)]] | wt | 101 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -22.2) |
| [[HOP62 (line)]] | alt | 156 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -17.5) |
| [[LoVo (line)]] | wt | 74.6 | 1 (1 ⚠) | 4 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.77× (z +11.1) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.295× (z -13.9) |
| [[NCI-H2030 (line)]] | alt | 112 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.397× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 93.8 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.339× (z -12.6) |
| [[SW1417 (line)]] | alt | 110 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 46.7 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -13.4) |
| [[J82 (line)]] | alt | 78.3 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -13.2) |
| [[A498 (line)]] | wt | 58.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -14.7) |
| [[C-33 A (line)]] | alt | 89.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -9.9) |
| [[COLO 205 (line)]] | alt | 45.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -14.2) |
| [[KATO III (line)]] | alt | 80.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -15.7) |
| [[LOX-IMVI (line)]] | wt | 81.5 | 1 | 2 | [[TAK-901 (drug)]] 0.05 µM 2.58× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.314× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 97.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 82.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.425× (z -9.2) |
| [[HS-578T (line)]] | alt | 80.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -9.4) |
| [[HT-29 (line)]] | alt | 73.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -10.6) |
| [[SNU-423 (line)]] | alt | 53.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.405× (z -9.1) |
| [[SW 900 (line)]] | alt | 74.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -9.4) |
| [[AN3 CA (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[C32 (line)]] | wt | 66.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -8.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 57.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HepG2_C3A (line)]] | wt | 63.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 57.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.1) |
| [[RKO (line)]] | wt | 68.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SK-MEL-2 (line)]] | alt | 60.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -9.4) |
| [[SW 1088 (line)]] | alt | 59.4 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.5 µM 0.0600× (z -9.0) |
| [[SW 1271 (line)]] | alt | 62.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0713× (z -9.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CHP-212 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 74.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 332 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 86.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7846), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA1]] | +0.70 | +0.56 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[ARHGAP17]] | +0.63 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[PDS5B]] | +0.61 | +0.69 / +0.50 | both halves | 1e-05 | same gene group |
| [[XPR1]] | +0.60 | +0.72 / +0.39 | both halves | 5e-05 |  |
| [[AGFG1]] | +0.58 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[LRRFIP2]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[MBD2]] | +0.56 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[DENND1B]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[NCKAP1]] | +0.56 | +0.76 / +0.46 | both halves | 2e-05 |  |
| [[NAA16]] | +0.56 | +0.59 / +0.39 | both halves | 6e-05 | same gene group |
| [[SPIN1]] | +0.55 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SESTD1]] | +0.55 | +0.62 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYSM1]] | -0.61 | -0.63 / -0.46 | both halves | 2e-05 |  |
| [[SCFD1]] | -0.55 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ARF4]] | -0.54 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[ARFIP2]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[CUL7]] | -0.53 | -0.25 / -0.59 | both halves | 4e-04 |  |
| [[GOSR1]] | -0.53 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[TM9SF4]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[NEU3]] | -0.52 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[USP8]] | -0.52 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ZNF432]] | -0.51 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[GPATCH2L]] | -0.51 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[THUMPD3-AS1]] | -0.51 | -0.70 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 214]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-9.0, -7.2); signed map (-28.6, -16.4). **Vector** length 87.9, 26.7% of its response variance represented; |z| ≥ 3 in 1,321 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.9 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.5 | -10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.4 | -9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.9 | -8.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | -0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.7 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +0.3 |
| fall | [[Selinexor (drug)]] 0.5 µM |  | -4.2 | -5.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.2 | -7.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -7.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.3 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | +1.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 4 regulatory subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.22 — chr18:9,546,791-9,615,240 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP4R1 |
| Gene groups (HGNC) | Protein phosphatase 4 regulatory subunits; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TF05](https://www.uniprot.org/uniprotkb/Q8TF05) (Serine/threonine-protein phosphatase 4 regulatory subunit 1):

> Regulatory subunit of serine/threonine-protein phosphatase 4. May play a role in regulation of cell division in renal glomeruli. The PPP4C-PPP4R1 PP4 complex may play a role in dephosphorylation and regulation of HDAC3. Plays a role in the inhibition of TNF-induced NF-kappa-B activation by regulating the dephosphorylation of TRAF2.; (Microbial infection) Participates in merkel polyomavirus-mediated inhibition of NF-kappa-B by bridging viral small tumor antigen with NEMO.

**Summary**, from NCBI Gene [9989](https://www.ncbi.nlm.nih.gov/gene/9989):

> This gene encodes one of several alternate regulatory subunits of serine/threonine protein phosphatase 4 (PP4). The protein features multiple HEAT repeats. This protein forms a complex with PP4RC. This complex may have a distinct role from other PP4 complexes, including regulation of HDAC3 (Zhang et al., PMID: 15805470). There is also a transcribed pseudogene on chromosome 20. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:9320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9320) · Entrez [9989](https://www.ncbi.nlm.nih.gov/gene/9989) · UniProt [Q8TF05](https://www.uniprot.org/uniprotkb/Q8TF05) · Ensembl [ENSG00000154845](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154845)

## Data

Gene col 7846: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7846); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7846, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7846]; `tensor/DDL_lfc|DDL_z.npy` [7846]; `embed/gene_vectors.npy` [7846]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7846 or target_col == 7846). Every well: [[PPP4R1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP4R1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
