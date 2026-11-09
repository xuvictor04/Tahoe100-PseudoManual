---
symbol: "RNF144A"
type: "gene"
col: 7552
ensembl_id: "ENSG00000151692"
name: "ring finger protein 144A"
location: "2p25.1"
module: 104
arm: "+"
pooled_cpm: 54.13
n_lines_expressing: 43
n_dd_up: 0
n_dd_down: 34
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# RNF144A

*ring finger protein 144A* — 2p25.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 3.05×, A498 3.58×, NCI-H23 2.82×, LoVo 1.99×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 9.53×, NCI-H460 3.78×; ⚠ cell-cycle shift, would explain all of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 4.85×, NCI-H460 2.81×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.329× (z -20.2, q 0e+00, down in 32 of 41 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.482× (z -9.4, q 1e-18, down in 32 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRPX]] (+0.55, fdr 1e-05), [[LOXL3]] (+0.50, fdr 3e-05), [[COL6A3]] (+0.49, fdr 3e-05); moves opposite to [[TMC4]] (-0.50, fdr 3e-05), [[TMEM125]] (-0.49, fdr 5e-05), [[PRR15-DT]] (-0.47, fdr 4e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BCAS1]] → it (grade B ⚠); 2 go from it, the strongest it → [[STK31]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7552.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 3.05×, A498 3.58×, NCI-H23 2.82×, LoVo 1.99×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 9.53×, NCI-H460 3.78×; ⚠ cell-cycle shift, would explain all of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 4.85×, NCI-H460 2.81×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.30× | +3.1 | 0.34 | 14/41 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.28× | +3.1 | 0.34 | 18/41 (LOX-IMVI, AsPC-1, …) | two highest doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.27× | +3.1 | 0.34 | 12/41 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.0 | 0.34 | 17/41 (PANC-1, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7552.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.329×** | -20.2 | 0e+00 | 32/41 (C32, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.446×** | -10.4 | 1e-22 | 37/41 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.469×** | -9.7 | 4e-20 | 33/40 (CHP-212, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.482×** | -9.4 | 1e-18 | 32/41 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.470×** | -9.3 | 1e-18 | 35/41 (A-427, LOX-IMVI, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.276×** | -8.6 | 5e-16 | 33/42 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.546×** | -7.8 | 6e-13 | 31/41 (C32, RPMI-7951, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.606×** | -6.4 | 8e-09 | 25/41 (A-172, LoVo, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.614×** | -6.3 | 2e-08 | 23/41 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.613×** | -6.1 | 8e-08 | 26/39 (CHP-212, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.409×** | -6.0 | 1e-07 | 27/40 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.627×** | -6.0 | 1e-07 | 29/41 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.659×** | -5.4 | 4e-06 | 28/41 (AN3 CA, C32, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.649×** | -5.2 | 6e-06 | 24/41 (H4, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.665×** | -5.2 | 6e-06 | 28/41 (LOX-IMVI, RKO, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.756×** | -5.1 | 1e-05 | 24/41 (NCI-H2347, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -4.4 | 3e-04 | 20/42 (NCI-H1792, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.715×** | -4.3 | 4e-04 | 22/41 (C32, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.728×** | -4.1 | 0.001 | 21/41 (LOX-IMVI, C32, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.812×** | -3.8 | 0.003 | 19/42 (A-172, H4, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.752×** | -3.7 | 0.005 | 24/42 (H4, HepG2/C3A, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.773×** | -3.3 | 0.017 | 19/40 (LOX-IMVI, A-172, …) | inconsistent across doses | position effect removed |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.837× | -3.3 | 0.022 | 19/42 (SHP-77, SW 900, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.789×** | -3.1 | 0.042 | 14/41 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7552. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 241 | 0 | 18 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -24.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -16.3) |
| [[C32 (line)]] | wt | 205 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -27.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0698× (z -21.6) |
| [[LOX-IMVI (line)]] | wt | 132 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -21.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 132 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0708× (z -25.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -12.3) |
| [[HOP62 (line)]] | alt | 79.0 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -24.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -17.1) |
| [[NCI-H1792 (line)]] | alt | 155 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0750× (z -25.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -14.1) |
| [[CHP-212 (line)]] | wt | 107 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0533× (z -18.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 75.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -25.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -13.7) |
| [[A-427 (line)]] | wt | 65.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -24.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0284× (z -17.5) |
| [[H4 (line)]] | wt | 107 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0536× (z -23.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.163× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 34.0 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -15.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 49.3 | 4 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +15.7) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.413× (z -8.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[RKO (line)]] | wt | 41.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 169 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -25.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -11.8) |
| [[SNU-1 (line)]] | wt | 39.2 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -16.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 55.6 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -17.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -12.3) |
| [[HS-578T (line)]] | alt | 72.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -16.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -13.2) |
| [[SHP-77 (line)]] | alt | 207 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -10.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -10.0) |
| [[A498 (line)]] | wt | 21.0 | 3 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.53× (z +14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +11.8) | — |
| [[C-33 A (line)]] | alt | 54.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -8.8) |
| [[LoVo (line)]] | wt | 55.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[MIA PaCa-2 (line)]] | alt | 39.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -18.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0739× (z -9.6) |
| [[SNU-423 (line)]] | alt | 29.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0906× (z -23.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.207× (z -10.8) |
| [[AN3 CA (line)]] | alt | 56.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -9.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.163× (z -8.9) |
| [[HCT15 (line)]] | alt | 39.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 23.4 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.449× (z -8.5) |
| [[SW 1088 (line)]] | alt | 83.4 | 0 | 2 | — | [[Erlotinib (drug)]] 0.5 µM 0.0592× (z -8.8) |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 50.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H1573 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -11.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[Panc 03.27 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 50.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -8.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.80 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.73 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.66 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.52 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.36 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.24 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7552), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPX]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[LOXL3]] | +0.50 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[COL6A3]] | +0.49 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[PDGFRA]] | +0.49 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[GNB4]] | +0.48 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[FLT1]] | +0.46 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[COL4A2]] | +0.46 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[FN1]] | +0.46 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[GAS7]] | +0.45 | +0.39 / +0.42 | both halves | 5e-05 |  |
| [[GHR]] | +0.45 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[ZCCHC24]] | +0.44 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[ITGA8]] | +0.44 | +0.40 / +0.44 | both halves | 5e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMC4]] | -0.50 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[TMEM125]] | -0.49 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[PRR15-DT]] | -0.47 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[POF1B]] | -0.47 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[LGALS4]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[HNF1A-AS1]] | -0.45 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[PROM2]] | -0.44 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[CYP4F12]] | -0.44 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[C11orf54]] | -0.44 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[BCAS1]] | -0.44 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[GPRIN2]] | -0.44 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[MIR4713HG]] | -0.43 | -0.48 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAS1]] | B | BCAS1 activity lowers RNF144A's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 2.16× higher at baseline in the lines without BCAS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STK31]] | B | RNF144A activity lowers STK31's level | lines that do not express RNF144A (7) vs lines expressing it (43) | 2.09× higher at baseline in the lines without RNF144A | 0.062 | ⚠ within organs, on part of the lines; also absent: PTPRU |
| [[PDLIM7]] | B | RNF144A activity raises PDLIM7's level | lines that do not express RNF144A (7) vs lines expressing it (43) | 1.73× lower at baseline in the lines without RNF144A | 0.073 | ⚠ within organs, on part of the lines; also absent: PTPRU |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.424). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (54.2, 24.8); signed map (25.7, 40.1). **Vector** length 94.7, 26.0% of its response variance represented; |z| ≥ 3 in 1,329 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +3.9 | -6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.7 | -0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | +3.3 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | -5.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | -0.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.0 | -5.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -4.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -0.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 144A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:6,917,412-7,068,286 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBCE7IP4, KIAA0161, hUIP4; previously RNF144 |
| Gene groups (HGNC) | Ring finger proteins; RBR E3 ubiquitin ligases |
| Reactome | 2 pathways, smallest: E3 ubiquitin ligases ubiquitinate target proteins; Protein ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [P50876](https://www.uniprot.org/uniprotkb/P50876) (E3 ubiquitin-protein ligase RNF144A):

> E3 ubiquitin-protein ligase which accepts ubiquitin from E2 ubiquitin-conjugating enzymes UBE2L3 and UBE2L6 in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Mediates the ubiquitination and degradation of the DNA damage kinase PRKDC during DNA damage. Positively regulates DNA virus or exogenous cytosolic DNA-triggered innate immune response by mediating STING1 ubiquitination and increasing its 'Lys-6'-linked ubiquitination and translocation from the …

**Summary**, from NCBI Gene [9781](https://www.ncbi.nlm.nih.gov/gene/9781):

> This gene encodes a member of a family of RING finger domain-containing E3 ubiquitin ligases that also includes parkin and parc. The expression of this gene is induced by DNA damage. The encoded protein interacts with the cytoplasmic DNA-dependent protein kinase, catalytic subunit (DNA-PKcs) and promotes its degradation through ubiquitination. The orthologous mouse protein has been shown to interact with a ubiquitin-conjugating enzyme involved in embryonic development. [provided by RefSeq, Mar …

**Accessions** — [HGNC:20457](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20457) · Entrez [9781](https://www.ncbi.nlm.nih.gov/gene/9781) · UniProt [P50876](https://www.uniprot.org/uniprotkb/P50876) · Ensembl [ENSG00000151692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151692)

## Data

Gene col 7552: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7552); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7552, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7552]; `tensor/DDL_lfc|DDL_z.npy` [7552]; `embed/gene_vectors.npy` [7552]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7552 or target_col == 7552). Every well: [[RNF144A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF144A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
