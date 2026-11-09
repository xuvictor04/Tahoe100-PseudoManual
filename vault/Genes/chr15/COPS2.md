---
symbol: "COPS2"
type: "gene"
col: 9261
ensembl_id: "ENSG00000166200"
name: "COP9 signalosome subunit 2"
location: "15q21.1"
module: 64
arm: "+"
pooled_cpm: 105.1
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# COPS2

*COP9 signalosome subunit 2* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.82× (z +18.0, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.797× (z -6.3, q 2e-07, down in 31 of 49 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.824× (z -5.4, q 1e-05, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-1 0.288×, C-33 A 0.358×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 0.606×, A498 0.597×; ⚠ cell-cycle shift, explains ~25% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SW 1271 0.0956×); [[Thymol (drug)]] 0.5 µM in 1 line (SNU-1 0.400×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNL1]] (+0.74, fdr 7e-06), [[CDC40]] (+0.73, fdr 7e-06), [[VIRMA]] (+0.66, fdr 1e-05); moves opposite to [[RELL1]] (-0.56, fdr 1e-05), [[SNRPB]] (-0.52, fdr 3e-05), [[MYL12A]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9261.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.82×** | +18.0 | 0e+00 | 48/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.53×** | +15.4 | 0e+00 | 46/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.67×** | +14.2 | 1e-43 | 44/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.05×** | +14.0 | 3e-42 | 47/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.10×** | +13.7 | 1e-40 | 48/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.95×** | +13.0 | 7e-37 | 47/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +11.5 | 8e-29 | 46/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +9.3 | 2e-18 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.56×** | +8.3 | 6e-15 | 40/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +7.6 | 2e-12 | 30/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +6.9 | 3e-10 | 36/48 (SW480, C32, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +6.4 | 9e-09 | 28/38 (NCI-H1573, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +6.3 | 1e-08 | 37/47 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.77×** | +5.8 | 2e-07 | 40/45 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.44×** | +5.1 | 1e-05 | 39/49 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.14× | +3.6 | 0.008 | 7/49 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.17× | +3.0 | 0.075 | 15/48 (J82, HS-578T, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9261.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-1 0.288×, C-33 A 0.358×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 0.606×, A498 0.597×; ⚠ cell-cycle shift, explains ~25% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SW 1271 0.0956×); [[Thymol (drug)]] 0.5 µM in 1 line (SNU-1 0.400×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.797×** | -6.3 | 2e-07 | 31/49 (A-172, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.759×** | -5.4 | 1e-05 | 30/48 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -5.4 | 1e-05 | 22/48 (SW1417, A498, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.696×** | -5.1 | 6e-05 | 32/48 (SW480, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.779×** | -4.9 | 1e-04 | 28/48 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | 0.837× | -3.4 | 0.074 | 21/44 (SNU-1, C-33 A, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.852× | -3.0 | 0.16 | 21/48 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.857× | -3.0 | 0.16 | 15/48 (SNU-1, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9261. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 88.3 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +20.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.36× (z +16.5) | — |
| [[SW480 (line)]] | alt | 111 | 11 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.07× (z +17.2) | — |
| [[NCI-H460 (line)]] | wt | 102 | 9 (5 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.59× (z +11.8) | — |
| [[A-172 (line)]] | wt | 83.8 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +12.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.40× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -9.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 94.6 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.65× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 103 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +18.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.04× (z +14.2) | — |
| [[HOP62 (line)]] | alt | 96.8 | 7 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.69× (z +11.7) | — |
| [[A498 (line)]] | wt | 133 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SK-MEL-2 (line)]] | alt | 83.5 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.84× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 121 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.62× (z +12.7) | — |
| [[hTERT-HPNE (line)]] | wt | 116 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.58× (z +10.4) | — |
| [[LoVo (line)]] | wt | 135 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.10× (z +14.8) | — |
| [[LS 180 (line)]] | wt | 116 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 7.72× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 79.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.78× (z +11.7) | — |
| [[A-427 (line)]] | wt | 57.0 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.89× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 145 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 4.08× (z +9.4) | — |
| [[KATO III (line)]] | alt | 99.3 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.44× (z +11.1) | — |
| [[SNU-1 (line)]] | wt | 134 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change · without an alert: [[Thymol (drug)]] 0.5 µM 0.400× (z -8.8) |
| [[SNU-423 (line)]] | alt | 80.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.67× (z +9.8) | — |
| [[A549 (line)]] | wt | 88.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.24× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 105 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 15.4× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 113 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.60× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 75.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.09× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 139 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.02× (z +10.0) | — |
| [[RKO (line)]] | wt | 128 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.0× (z +13.8) | — |
| [[AsPC-1 (line)]] | alt | 87.8 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.91× (z +11.1) | — |
| [[BT-474 (line)]] | alt | 83.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.22× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 95.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.82× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[H4 (line)]] | wt | 120 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.87× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 86.2 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.51× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 93.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.14× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 128 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.06× (z +10.8) | — |
| [[SW48 (line)]] | wt | 111 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.02× (z +11.3) | — |
| [[C32 (line)]] | wt | 80.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.87× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 137 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.90× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 88.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.37× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 74.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.36× (z +8.9) | — |
| [[J82 (line)]] | alt | 84.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.48× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 147 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.60× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 152 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.95× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 88.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.39× (z +9.3) | — |
| [[SW 1271 (line)]] | alt | 80.9 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0956× (z -9.3) |
| [[SW 900 (line)]] | alt | 109 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.40× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 131 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 181 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9261), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNL1]] | +0.74 | +0.74 / +0.71 | both halves | 7e-06 | pathway: RHOBTB GTPase Cycle |
| [[CDC40]] | +0.73 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[VIRMA]] | +0.66 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[COPS5]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 | same gene group; pathway: Cargo recognition for clathrin-mediated endocytosis; STRING 999 |
| [[PSMC2]] | +0.63 | +0.68 / +0.61 | both halves | 7e-06 | pathway: Neddylation |
| [[NUDT9]] | +0.62 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.61 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[EFCAB7]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[FAM204A]] | +0.61 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[TCTN1]] | +0.61 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[PLRG1]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[MRPL9]] | +0.60 | +0.65 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELL1]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SNRPB]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[MYL12A]] | -0.51 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[CD9]] | -0.51 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[ACER3]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[LINC01128]] | -0.50 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[ASF1B]] | -0.50 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[SEPTIN10]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[RCOR1]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises COPS2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ALDH2]] | B | ALDH2 activity raises COPS2's level | lines that do not express ALDH2 (9) vs lines expressing it (41) | 1.28× lower at baseline in the lines without ALDH2 | 0.079 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-18.9, -6.5); signed map (-26.7, -20.2). **Vector** length 92.8, 30.8% of its response variance represented; |z| ≥ 3 in 1,234 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.9 | +13.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +13.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.4 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +0.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -7.2 | +5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -6.4 | +4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | +7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.7 | +9.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | +1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | +0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | +1.4 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[vincristine (drug)]] 5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | COP9 signalosome subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:49,106,068-49,155,661 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRIP15, ALIEN, CSN2 |
| Gene groups (HGNC) | COP9 signalosome |
| Reactome | 16 pathways, smallest: RHOBTB1 GTPase cycle; RHOBTB GTPase Cycle; DNA Damage Recognition in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [P61201](https://www.uniprot.org/uniprotkb/P61201) (COP9 signalosome complex subunit 2):

> Component of the COP9 signalosome (CSN), a master regulator of the ubiquitin conjugation pathway. CSN mediates the deneddylation of the cullin subunits of all cullin-RING ligases. By reversing the activating neddylation on the cullin-RING ligase, the COP9 signalosome restores the ligase to its inactive state and resets it for substrate recognition. CSN is also involved in phosphorylation of p53/TP53, c-jun/JUN, IkappaBalpha/NFKBIA, ITPK1 and IRF8/ICSBP, possibly via its association with CK2 and …

**Summary**, from NCBI Gene [9318](https://www.ncbi.nlm.nih.gov/gene/9318):

> Predicted to enable transcription corepressor activity. Involved in protein deneddylation and protein phosphorylation. Located in cytoplasm; intercellular bridge; and nucleus. Part of COP9 signalosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30747](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30747) · Entrez [9318](https://www.ncbi.nlm.nih.gov/gene/9318) · UniProt [P61201](https://www.uniprot.org/uniprotkb/P61201) · Ensembl [ENSG00000166200](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166200)

## Data

Gene col 9261: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9261); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9261, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9261]; `tensor/DDL_lfc|DDL_z.npy` [9261]; `embed/gene_vectors.npy` [9261]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9261 or target_col == 9261). Every well: [[COPS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
