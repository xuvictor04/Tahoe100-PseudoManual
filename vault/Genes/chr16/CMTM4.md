---
symbol: "CMTM4"
type: "gene"
col: 11443
ensembl_id: "ENSG00000183723"
name: "CKLF like MARVEL transmembrane domain containing 4"
location: "16q22.1-q22.3"
module: 18
arm: "+"
pooled_cpm: 58.08
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CMTM4

*CKLF like MARVEL transmembrane domain containing 4* — 16q22.1-q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 1.25× (z +5.9, q 2e-06, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H460 1.82×, A498 1.82×, LS 180 1.61×, A549 1.84×; ⚠ cell-cycle shift, explains ~41% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A498 2.79×, LS 180 2.30×, A549 2.58×, NCI-H460 1.90×; ⚠ cell-cycle shift, explains ~26% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 4.10×, HS-578T 2.55×; ⚠ cell-cycle shift, explains ~30% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.621× (z -18.0, q 0e+00, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.508× (z -17.4, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A15]] (+0.69, fdr 7e-06), [[ADCY3]] (+0.68, fdr 7e-06), [[MACROD1]] (+0.67, fdr 7e-06); moves opposite to [[CREB3]] (-0.61, fdr 1e-05), [[GOLGB1]] (-0.60, fdr 1e-05), [[CCDC148]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MVB12B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11443.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H460 1.82×, A498 1.82×, LS 180 1.61×, A549 1.84×; ⚠ cell-cycle shift, explains ~41% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A498 2.79×, LS 180 2.30×, A549 2.58×, NCI-H460 1.90×; ⚠ cell-cycle shift, explains ~26% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 4.10×, HS-578T 2.55×; ⚠ cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +5.9 | 2e-06 | 25/48 (KATO III, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.22×** | +5.3 | 4e-05 | 15/47 (A-172, SW480, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 1.14× | +5.0 | 9e-05 | 16/48 (A549, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.5 | 9e-04 | 18/41 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +4.2 | 0.003 | 17/48 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.1 | 0.003 | 15/47 (H4, NCI-H23, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.1 | 0.004 | 18/47 (KATO III, Panc 03.27, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.16× | +3.9 | 0.006 | 10/48 (A-172, A549, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 1.14× | +3.4 | 0.048 | 12/48 (SK-MEL-2, A498, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.14× | +3.3 | 0.050 | 16/47 (A498, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.13× | +3.2 | 0.067 | 10/49 (HT-29, SW1417, …) | all doses, stronger at high dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.12× | +3.1 | 0.085 | 1/49 (HEC-1-A) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.11 | 7/48 (Hs 766T, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11443.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.621×** | -18.0 | 0e+00 | 31/48 (RKO, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.508×** | -17.4 | 0e+00 | 41/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.370×** | -13.9 | 2e-41 | 42/49 (NCI-H2030, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.700×** | -9.5 | 2e-19 | 30/48 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.770×** | -7.0 | 3e-10 | 23/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.607×** | -7.0 | 3e-10 | 27/48 (LS 180, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.822×** | -5.3 | 1e-05 | 19/48 (SW480, SHP-77, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.824×** | -5.2 | 2e-05 | 22/48 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.832×** | -4.9 | 5e-05 | 21/48 (NCI-H2030, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.828×** | -4.9 | 7e-05 | 23/47 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -4.5 | 3e-04 | 21/48 (LoVo, BT-474, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.843× | -3.3 | 0.050 | 13/48 (KATO III, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.918× | -3.3 | 0.050 | 11/48 (LoVo, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 67.4 | 2 (2 ⚠) | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +12.7) ⚠ cell-cycle shift, explains ~41% of this change | [[Harringtonine (drug)]] 5 µM 0.220× (z -21.7) |
| [[LoVo (line)]] | wt | 90.6 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -11.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.260× (z -10.0) |
| [[LS 180 (line)]] | wt | 80.3 | 2 (2 ⚠) | 4 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change | [[Harringtonine (drug)]] 5 µM 0.342× (z -13.5) |
| [[A549 (line)]] | wt | 47.4 | 2 (2 ⚠) | 3 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -16.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.278× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 80.1 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.73× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.218× (z -18.2) |
| [[A-427 (line)]] | wt | 73.9 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.378× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 92.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -18.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.294× (z -17.5) |
| [[J82 (line)]] | alt | 34.2 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.251× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 147 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.375× (z -13.2) |
| [[PANC-1 (line)]] | alt | 39.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -20.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.321× (z -15.5) |
| [[RKO (line)]] | wt | 61.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -21.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -11.1) |
| [[A498 (line)]] | wt | 48.6 | 3 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +12.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 42.2 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0586× (z -10.0) |
| [[SW48 (line)]] | wt | 96.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -13.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -11.3) |
| [[A-172 (line)]] | wt | 46.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -13.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -9.6) |
| [[BT-474 (line)]] | alt | 94.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -9.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 42.4 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.201× (z -16.2) |
| [[MIA PaCa-2 (line)]] | alt | 72.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.413× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 36.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +17.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 26.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.312× (z -9.3) |
| [[C-33 A (line)]] | alt | 99.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 32.9 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.287× (z -8.7) |
| [[HOP62 (line)]] | alt | 37.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.387× (z -9.5) |
| [[HS-578T (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HT-29 (line)]] | alt | 80.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -12.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 46.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.356× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 49.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.483× (z -8.7) |
| [[SHP-77 (line)]] | alt | 46.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 58.9 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0801× (z -9.4) |
| [[AN3 CA (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 80.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A15]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ADCY3]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[MACROD1]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ABCB10]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[NAE1]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[TMTC4]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[SLC41A3]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CBFB]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[GK5]] | +0.61 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[SEPHS1]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[TMEM181]] | +0.60 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[FAM20B]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREB3]] | -0.61 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[GOLGB1]] | -0.60 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[CCDC148]] | -0.57 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[LINC02968]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[KDM5A]] | -0.55 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[SNAPIN]] | -0.54 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[GORAB]] | -0.54 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[YIPF3]] | -0.53 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[OASL]] | -0.53 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.53 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[LENG1]] | -0.52 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[IFIT2]] | -0.52 | -0.57 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MVB12B]] | B | MVB12B activity raises CMTM4's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.92× lower at baseline in the lines without MVB12B | 0.085 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.717). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.3, -36.5); signed map (-2.1, -53.3). **Vector** length 113, 28.1% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +5.1 | +5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +4.1 | +5.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.9 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +2.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.4 | -13.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.9 | -17.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.1 | -7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.0 | -18.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.4 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | CKLF like MARVEL transmembrane domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1-q22.3 — chr16:66,614,750-66,696,743 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CKLFSF4 |
| Gene groups (HGNC) | CKLF like MARVEL transmembrane domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZR5](https://www.uniprot.org/uniprotkb/Q8IZR5) (CKLF-like MARVEL transmembrane domain-containing protein 4):

> Acts as a backup for CMTM6 to regulate plasma membrane expression of PD-L1/CD274, an immune inhibitory ligand critical for immune tolerance to self and antitumor immunity. May protect PD-L1/CD274 from being polyubiquitinated and targeted for degradation.

**Summary**, from NCBI Gene [146223](https://www.ncbi.nlm.nih.gov/gene/146223):

> This gene belongs to the chemokine-like factor gene superfamily, a novel family that is similar to the chemokine and the transmembrane 4 superfamilies of signaling molecules. This gene is one of several chemokine-like factor genes located in a cluster on chromosome 16. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19175) · Entrez [146223](https://www.ncbi.nlm.nih.gov/gene/146223) · UniProt [Q8IZR5](https://www.uniprot.org/uniprotkb/Q8IZR5) · Ensembl [ENSG00000183723](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183723)

## Data

Gene col 11443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11443); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11443]; `tensor/DDL_lfc|DDL_z.npy` [11443]; `embed/gene_vectors.npy` [11443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11443 or target_col == 11443). Every well: [[CMTM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMTM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
