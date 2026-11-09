---
symbol: "CPQ"
type: "gene"
col: 2440
ensembl_id: "ENSG00000104324"
name: "carboxypeptidase Q"
location: "8q22.1"
module: 13
arm: "+"
pooled_cpm: 47.67
n_lines_expressing: 35
n_dd_up: 11
n_dd_down: 35
n_dd_up_clean: 7
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 8
direction_downstream: 5
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CPQ

*carboxypeptidase Q* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.05 µM: 1.27× (z +4.2, q 0.013, up in 19 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.338× (z -20.0, q 0e+00, down in 33 of 33 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.417× (z -11.4, q 4e-28, down in 25 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTS2]] (+0.58, fdr 1e-05), [[MSC-AS1]] (+0.58, fdr 1e-05), [[APBB1IP]] (+0.57, fdr 1e-05); moves opposite to [[GRB7]] (-0.51, fdr 1e-04), [[TMC4]] (-0.50, fdr 3e-05), [[ESRP1]] (-0.50, fdr 6e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[SDC2]] → it (grade B ⚠); 5 go from it, the strongest it → [[CCDC149]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2440.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 0.013 | 19/33 (HOP62, RKO, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +3.8 | 0.032 | 4/24 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.37×** | +3.8 | 0.032 | 18/33 (RKO, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.035 | 15/32 (RKO, hTERT-HPNE, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.68×** | +3.6 | 0.040 | 13/33 (RKO, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.052 | 15/32 (HepG2/C3A, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.058 | 10/33 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.063 | 14/33 (LS 180, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +3.2 | 0.095 | 9/33 (LoVo, C32, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.27×** | +3.1 | 0.095 | 10/33 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.095 | 13/33 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +3.0 | 0.11 | 10/33 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +3.0 | 0.11 | 10/33 (LoVo, C32, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.11 | 7/33 (LS 180, HCT15, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 21 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2440.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.338×** | -20.0 | 0e+00 | 33/33 (HepG2/C3A, C32, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.369×** | -13.0 | 4e-36 | 32/33 (A-172, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.339×** | -12.5 | 2e-33 | 28/33 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.401×** | -11.9 | 1e-30 | 30/33 (HepG2/C3A, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.401×** | -11.9 | 1e-30 | 31/33 (HepG2/C3A, RKO, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.414×** | -11.5 | 2e-28 | 31/33 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.417×** | -11.4 | 4e-28 | 25/33 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.441×** | -10.7 | 1e-24 | 32/33 (HepG2/C3A, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.521×** | -8.5 | 1e-15 | 27/33 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.529×** | -8.3 | 7e-15 | 28/33 (RKO, SW 1271, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.647×** | -8.0 | 7e-14 | 23/33 (HS-578T, C32, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.543×** | -7.9 | 1e-13 | 26/33 (LS 180, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.575×** | -7.2 | 3e-11 | 25/33 (NCI-H661, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.551×** | -6.9 | 3e-10 | 24/31 (J82, NCI-H2030, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.369×** | -6.8 | 4e-10 | 28/34 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.402×** | -6.2 | 2e-08 | 23/33 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.671×** | -5.2 | 7e-06 | 25/33 (RKO, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.687×** | -4.9 | 3e-05 | 21/33 (HepG2/C3A, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.687×** | -4.9 | 3e-05 | 24/33 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.751×** | -3.7 | 0.005 | 16/33 (SW 1088, RKO, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.819×** | -3.6 | 0.006 | 19/33 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.013 | 18/34 (RPMI-7951, RKO, …) | rises with dose | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.605×** | -3.4 | 0.013 | 19/33 (A498, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.751×** | -3.3 | 0.018 | 15/33 (H4, RKO, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.768×** | -3.2 | 0.025 | 16/33 (HepG2/C3A, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.750×** | -3.1 | 0.034 | 15/32 (NCI-H2030, NCI-H23, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2440. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 158 | 0 | 16 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -18.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.273× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 162 | 0 | 14 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -25.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.304× (z -10.6) |
| [[A-172 (line)]] | wt | 105 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -17.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -14.2) |
| [[J82 (line)]] | alt | 93.6 | 0 | 11 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -22.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.365× (z -8.8) |
| [[HOP62 (line)]] | alt | 57.3 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -20.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -11.6) |
| [[PANC-1 (line)]] | alt | 70.9 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -24.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -14.2) |
| [[C32 (line)]] | wt | 272 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -24.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -17.8) |
| [[NCI-H460 (line)]] | wt | 39.8 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -24.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -21.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0961× (z -17.6) |
| [[SK-MEL-2 (line)]] | alt | 126 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -19.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.310× (z -10.8) |
| [[HS-578T (line)]] | alt | 302 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -20.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -14.2) |
| [[SNU-423 (line)]] | alt | 57.8 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -23.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.286× (z -8.6) |
| [[A498 (line)]] | wt | 89.0 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -23.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -8.5) |
| [[LS 180 (line)]] | wt | 58.9 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -16.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.246× (z -11.5) |
| [[A549 (line)]] | wt | 23.7 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 88.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -13.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 26.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -18.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -12.1) |
| [[H4 (line)]] | wt | 61.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 18.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 15.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.133× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[NCI-H661 (line)]] | alt | 54.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.0726× (z -9.2) |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0838× (z -10.5) |
| [[LoVo (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -11.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -9.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW 1088 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW 1271 (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0683× (z -9.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW 900 (line)]] | alt | 42.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0642× (z -9.4) |
| [[A-427 (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.16 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.81 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.63 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.80 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.74 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.69 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2440), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS2]] | +0.58 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[MSC-AS1]] | +0.58 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[APBB1IP]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ARHGEF6]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[PRRX1]] | +0.54 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[MIR137HG]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[PTGFR]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ABCA1]] | +0.54 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[FBN1]] | +0.53 | +0.48 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_COAGULATION |
| [[DZIP1L]] | +0.52 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[ABI3BP]] | +0.52 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[ADAM12]] | +0.50 | +0.61 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRB7]] | -0.51 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[TMC4]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ESRP1]] | -0.50 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[ITGB4]] | -0.47 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[INAVA]] | -0.47 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[B3GNT3]] | -0.46 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[SPINT1]] | -0.45 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[TMC6]] | -0.45 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[TMEM45B]] | -0.45 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[TMPRSS4]] | -0.45 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[EPS8L3]] | -0.45 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[HSD17B2]] | -0.44 | -0.43 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDC2]] | B | SDC2 activity raises CPQ's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 3.81× lower at baseline in the lines without SDC2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH |
| [[ARHGEF6]] | B | ARHGEF6 activity raises CPQ's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 3.61× lower at baseline in the lines without ARHGEF6 | 0.018 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[TEX41]] | B | TEX41 activity raises CPQ's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 3.17× lower at baseline in the lines without TEX41 | 0.032 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[ZNF354C]] | B | ZNF354C activity raises CPQ's level | lines that do not express ZNF354C (23) vs lines expressing it (27) | 2.42× lower at baseline in the lines without ZNF354C | 0.067 | ⚠ within organs, on part of the lines; also absent: CPEB1, MPDZ, NALCN |
| [[FRMD4A]] | B | FRMD4A activity raises CPQ's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 3.25× lower at baseline in the lines without FRMD4A | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[ADAMTS2]] | B | ADAMTS2 activity raises CPQ's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 3.32× lower at baseline in the lines without ADAMTS2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1 |
| [[GRB7]] | B | GRB7 activity lowers CPQ's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 2.64× higher at baseline in the lines without GRB7 | 0.083 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[GRIN2A]] | B | GRIN2A activity raises CPQ's level | lines that do not express GRIN2A (39) vs lines expressing it (11) | 4.52× lower at baseline in the lines without GRIN2A | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000237268, ENSG00000234426, AMPH |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC149]] | B | CPQ activity raises CCDC149's level | lines that do not express CPQ (15) vs lines expressing it (35) | 2.63× lower at baseline in the lines without CPQ | 0.036 | ⚠ within organs, on part of the lines; also absent: NETO2, LINC01725, KMO; maybe low, not absent |
| [[ADAM12]] | B | CPQ activity raises ADAM12's level | lines that do not express CPQ (15) vs lines expressing it (35) | 3.35× lower at baseline in the lines without CPQ | 0.047 | ⚠ within organs, on part of the lines; also absent: NETO2, LINC01725, KMO; maybe low, not absent |
| [[SDC2]] | B | CPQ activity raises SDC2's level | lines that do not express CPQ (15) vs lines expressing it (35) | 4.06× lower at baseline in the lines without CPQ | 0.063 | ⚠ within organs, on part of the lines; also absent: NETO2, LINC01725, KMO; maybe low, not absent |
| [[ARHGEF6]] | B | CPQ activity raises ARHGEF6's level | lines that do not express CPQ (15) vs lines expressing it (35) | 2.04× lower at baseline in the lines without CPQ | 0.081 | ⚠ within organs, on part of the lines; also absent: NETO2, LINC01725, KMO; maybe low, not absent |
| [[ZNF354C]] | B | CPQ activity raises ZNF354C's level | lines that do not express CPQ (15) vs lines expressing it (35) | 1.88× lower at baseline in the lines without CPQ | 0.090 | ⚠ within organs, on part of the lines; also absent: NETO2, LINC01725, KMO; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.435). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.1, 20.7); signed map (28.6, 45.9). **Vector** length 80.1, 20.5% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.9 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.7 | -0.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.7 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +3.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.6 | -7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.0 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.7 | -13.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -2.7 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | carboxypeptidase Q |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:96,645,242-97,149,654 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LDP, PGCP |
| Gene groups (HGNC) | M14 carboxypeptidases |
| Hallmark sets | COAGULATION, COMPLEMENT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y646](https://www.uniprot.org/uniprotkb/Q9Y646) (Carboxypeptidase Q):

> Carboxypeptidase that may play an important role in the hydrolysis of circulating peptides. Catalyzes the hydrolysis of dipeptides with unsubstituted terminals into amino acids. May play a role in the liberation of thyroxine hormone from its thyroglobulin (Tg) precursor.

**Summary**, from NCBI Gene [10404](https://www.ncbi.nlm.nih.gov/gene/10404):

> This gene encodes a metallopeptidase that belongs to the peptidase M28 family. The encoded protein may catalyze the cleavage of dipeptides with unsubstituted terminals into amino acids. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:16910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16910) · Entrez [10404](https://www.ncbi.nlm.nih.gov/gene/10404) · UniProt [Q9Y646](https://www.uniprot.org/uniprotkb/Q9Y646) · Ensembl [ENSG00000104324](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104324)

## Data

Gene col 2440: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2440); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2440, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2440]; `tensor/DDL_lfc|DDL_z.npy` [2440]; `embed/gene_vectors.npy` [2440]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2440 or target_col == 2440). Every well: [[CPQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
