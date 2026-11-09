---
symbol: "FRAS1"
type: "gene"
col: 6228
ensembl_id: "ENSG00000138759"
name: "Fraser extracellular matrix complex subunit 1"
location: "4q21.21"
module: 8
arm: "+"
pooled_cpm: 54.98
n_lines_expressing: 28
n_dd_up: 26
n_dd_down: 18
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 9
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# FRAS1

*Fraser extracellular matrix complex subunit 1* — 4q21.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.69× (z +46.9, q 0e+00, up in 24 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.580× (z -11.7, q 6e-29, down in 23 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPD52L1]] (+0.56, fdr 8e-06), [[SLC44A3-AS1]] (+0.52, fdr 3e-05), [[CCSER1]] (+0.52, fdr 2e-05); moves opposite to [[PAOX]] (-0.55, fdr 3e-05), [[ZNF559-ZNF177]] (-0.53, fdr 2e-04), [[ZNF177]] (-0.52, fdr 8e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HGD]] → it (grade B ⚠); 9 go from it, the strongest it → [[TPD52L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6228.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.69×** | +46.9 | 0e+00 | 24/26 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +12.3 | 2e-32 | 12/26 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +11.6 | 6e-29 | 14/28 (A-172, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.40×** | +10.1 | 7e-22 | 19/26 (NCI-H2347, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +9.6 | 1e-19 | 9/26 (C-33 A, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +9.2 | 4e-18 | 10/26 (C-33 A, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +9.1 | 5e-18 | 20/26 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +7.5 | 3e-12 | 11/26 (LoVo, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.88×** | +7.1 | 1e-10 | 12/26 (A-172, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +6.6 | 2e-09 | 13/26 (NCI-H1573, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +6.5 | 3e-09 | 17/26 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +5.4 | 3e-06 | 4/26 (C-33 A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +5.1 | 2e-05 | 2/22 (A-172, CFPAC-1) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +4.8 | 7e-05 | 7/26 (SNU-1, Hs 766T, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.25×** | +4.7 | 1e-04 | 12/26 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +4.6 | 1e-04 | 13/26 (HepG2/C3A, A-172, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.48×** | +4.3 | 4e-04 | 8/26 (A549, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +4.2 | 8e-04 | 5/26 (CFPAC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.001 | 14/26 (NCI-H2347, RKO, …) | two highest doses |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.001 | 1/26 (C-33 A) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +4.1 | 0.001 | 5/26 (SW480, NCI-H2347, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6228.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.580×** | -11.7 | 6e-29 | 23/26 (SW48, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.576×** | -11.4 | 1e-27 | 21/26 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.688×** | -11.4 | 1e-27 | 21/26 (RKO, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.631×** | -9.9 | 6e-21 | 23/26 (LoVo, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.655×** | -9.1 | 1e-17 | 16/26 (RKO, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.704×** | -7.5 | 4e-12 | 21/26 (LoVo, HCT15, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.705×** | -7.5 | 5e-12 | 20/26 (SW48, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.720×** | -7.1 | 1e-10 | 17/26 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.773×** | -5.6 | 2e-06 | 18/26 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.617×** | -5.4 | 3e-06 | 10/26 (SW1417, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.783×** | -5.3 | 7e-06 | 13/26 (RKO, SW48, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.631×** | -5.2 | 1e-05 | 12/26 (RKO, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.800×** | -4.8 | 7e-05 | 16/26 (SW48, SHP-77, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.797×** | -4.7 | 1e-04 | 12/26 (SNU-423, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -4.4 | 4e-04 | 7/26 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | 0.844× | -3.5 | 0.013 | 6/26 (SW480, H4, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | 0.862× | -3.1 | 0.053 | 6/26 (HCT15, RKO, …) | top dose only |  |
| [[Futibatinib (drug)]] 0.05 µM |  | 0.865× | -3.0 | 0.077 | 3/26 (SNU-423, H4, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.870× | -2.9 | 0.083 | 3/26 (HT-29, HepG2/C3A, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | 0.866× | -2.9 | 0.085 | 5/26 (Hs 766T, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6228. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 138 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -23.0) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.204× (z -14.2) |
| [[SW48 (line)]] | wt | 578 | 0 | 14 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0602× (z -24.0) |
| [[SHP-77 (line)]] | alt | 133 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.230× (z -15.2) |
| [[A549 (line)]] | wt | 76.8 | 1 (1 ⚠) | 8 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.12× (z +8.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -20.5) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.248× (z -11.7) |
| [[KATO III (line)]] | alt | 38.7 | 1 (1 ⚠) | 8 (5 ⚠) | [[Selinexor (drug)]] 5 µM 2.44× (z +9.5) ⚠ cell-cycle shift, explains ~39% of this change | [[Dinaciclib (drug)]] 5 µM 0.100× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.273× (z -9.9) |
| [[LoVo (line)]] | wt | 58.5 | 2 (1 ⚠) | 7 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +14.1) | [[Digitoxin (drug)]] 5 µM 0.118× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 118 | 0 | 9 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.182× (z -15.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.283× (z -12.2) |
| [[SW1417 (line)]] | alt | 128 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -18.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.266× (z -12.9) |
| [[SW480 (line)]] | alt | 207 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -16.7) |
| [[HCT15 (line)]] | alt | 239 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.340× (z -9.4) |
| [[A-172 (line)]] | wt | 17.9 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.13× (z +16.9) | — |
| [[NCI-H1573 (line)]] | alt | 46.9 | 1 | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +17.2) | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.216× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 175 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -16.9) |
| [[HepG2_C3A (line)]] | wt | 147 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -15.4) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.343× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 106 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -13.2) |
| [[HT-29 (line)]] | alt | 99.7 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +11.5) | [[Digitoxin (drug)]] 5 µM 0.272× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 32.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +14.1) | — |
| [[SNU-1 (line)]] | wt | 28.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +9.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -8.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SNU-423 (line)]] | alt | 14.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +12.0) | — |
| [[BT-474 (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +13.2) | — |
| [[C-33 A (line)]] | alt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 57.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.67× (z +21.6) | — |
| [[H4 (line)]] | wt | 13.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.89× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 66.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -8.5) |
| [[NCI-H596 (line)]] | alt | 75.2 | 1 | 0 | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 14.8× (z +15.0) | — |
| [[SW 900 (line)]] | alt | 23.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.65× (z +14.9) | — |
| [[A-427 (line)]] | wt | 4.55 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.48 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.78 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.26 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.31 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.24 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.13 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.52 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 7.53 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.00 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6228), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L1]] | +0.56 | +0.60 / +0.57 | both halves | 8e-06 |  |
| [[SLC44A3-AS1]] | +0.52 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[CCSER1]] | +0.52 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[MKX]] | +0.52 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[ZNRF3]] | +0.51 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[KIF26B]] | +0.51 | +0.44 / +0.37 | both halves | 8e-05 |  |
| [[HUNK]] | +0.49 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[STEAP2]] | +0.49 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[LRRC8D]] | +0.48 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[HOXB8]] | +0.48 | +0.44 / +0.32 | both halves | 2e-04 |  |
| [[PGAP4]] | +0.48 | +0.35 / +0.29 | both halves | 3e-04 |  |
| [[ADAMTS19]] | +0.48 | +0.51 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAOX]] | -0.55 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ZNF559-ZNF177]] | -0.53 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[ZNF177]] | -0.52 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[SNAP29]] | -0.49 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[HAUS3]] | -0.48 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[ENDOV]] | -0.48 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[POLM]] | -0.47 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[NPHP1]] | -0.47 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[DENND6B]] | -0.47 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[WIPF2]] | -0.46 | -0.54 / -0.23 | both halves | 5e-04 |  |
| [[ZNF559]] | -0.46 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[ANKRD24]] | -0.45 | -0.24 / -0.39 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HGD]] | B | HGD activity raises FRAS1's level | lines that do not express HGD (15) vs lines expressing it (35) | 3.56× lower at baseline in the lines without HGD | 0.042 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[SLC12A8]] | B | SLC12A8 activity raises FRAS1's level | lines that do not express SLC12A8 (17) vs lines expressing it (33) | 2.30× lower at baseline in the lines without SLC12A8 | 0.088 | ⚠ within organs, on part of the lines; also absent: ANK3, LYPD6B, SAMD12-AS1; maybe low, not absent |
| [[PTGFRN]] | B | PTGFRN activity raises FRAS1's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 3.07× lower at baseline in the lines without PTGFRN | 0.091 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| [[MYO5C]] | C | MYO5C activity raises FRAS1's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 4.53× lower at baseline in the lines without MYO5C | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent; co-absent with the target |
| [[SYK]] | C | SYK activity raises FRAS1's level | lines that do not express SYK (30) vs lines expressing it (20) | 3.82× lower at baseline in the lines without SYK | 0.042 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14; co-absent with the target |
| [[ANXA3]] | C | ANXA3 activity raises FRAS1's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.39× lower at baseline in the lines without ANXA3 | 0.049 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPD52L1]] | B | FRAS1 activity raises TPD52L1's level | lines that do not express FRAS1 (22) vs lines expressing it (28) | 1.55× lower at baseline in the lines without FRAS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ANO9, ELF3, FAAH2 |
| [[SEL1L3]] | B | FRAS1 activity raises SEL1L3's level | lines that do not express FRAS1 (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without FRAS1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ANO9, ELF3, FAAH2 |
| [[ZNF559-ZNF177]] | B | FRAS1 activity lowers ZNF559-ZNF177's level | lines that do not express FRAS1 (22) vs lines expressing it (28) | 1.45× higher at baseline in the lines without FRAS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ANO9, ELF3, FAAH2 |
| [[ZNF177]] | B | FRAS1 activity lowers ZNF177's level | lines that do not express FRAS1 (22) vs lines expressing it (28) | 1.43× higher at baseline in the lines without FRAS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ANO9, ELF3, FAAH2 |
| [[ACTR3C]] | B | FRAS1 activity raises ACTR3C's level | lines that do not express FRAS1 (22) vs lines expressing it (28) | 2.13× lower at baseline in the lines without FRAS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ANO9, ELF3, FAAH2 |
| [[MYO5C]] | C | FRAS1 activity raises MYO5C's level | lines that do not express FRAS1 (22) vs lines expressing it (28) | 3.19× lower at baseline in the lines without FRAS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ANO9, ELF3, FAAH2; co-absent with the target |
| [[ANXA3]] | C | FRAS1 activity raises ANXA3's level | lines that do not express FRAS1 (22) vs lines expressing it (28) | 4.02× lower at baseline in the lines without FRAS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ANO9, ELF3, FAAH2; co-absent with the target |
| [[SYK]] | C | FRAS1 activity raises SYK's level | lines that do not express FRAS1 (22) vs lines expressing it (28) | 2.68× lower at baseline in the lines without FRAS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ANO9, ELF3, FAAH2; co-absent with the target |
| [[PROM1]] | C | FRAS1 activity raises PROM1's level | lines that do not express FRAS1 (22) vs lines expressing it (28) | 2.74× lower at baseline in the lines without FRAS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ANO9, ELF3, FAAH2; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.265). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.4, 27.4); signed map (57.4, -2.0). **Vector** length 92.8, 24.8% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +46.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +11.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +9.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +12.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.6 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +7.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +1.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -11.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -7.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -7.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.1 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -5.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | Fraser extracellular matrix complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.21 — chr4:78,057,323-78,544,269 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22031, FLJ14927, KIAA1500 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XX4](https://www.uniprot.org/uniprotkb/Q86XX4) (Extracellular matrix organizing protein FRAS1):

> Involved in extracellular matrix organization (By similarity). Required for the regulation of epidermal-basement membrane adhesion responsible for proper organogenesis during embryonic development (By similarity). Involved in brain organization and function (By similarity).

**Summary**, from NCBI Gene [80144](https://www.ncbi.nlm.nih.gov/gene/80144):

> This gene encodes an extracellular matrix protein that appears to function in the regulation of epidermal-basement membrane adhesion and organogenesis during development. Mutations in this gene cause Fraser syndrome, a multisystem malformation that can include craniofacial, urogenital and respiratory system abnormalities. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:19185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19185) · Entrez [80144](https://www.ncbi.nlm.nih.gov/gene/80144) · UniProt [Q86XX4](https://www.uniprot.org/uniprotkb/Q86XX4) · Ensembl [ENSG00000138759](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138759)

## Data

Gene col 6228: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6228); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6228, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6228]; `tensor/DDL_lfc|DDL_z.npy` [6228]; `embed/gene_vectors.npy` [6228]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6228 or target_col == 6228). Every well: [[FRAS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRAS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
