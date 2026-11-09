---
symbol: "MND1"
type: "gene"
col: 4259
ensembl_id: "ENSG00000121211"
name: "meiotic nuclear divisions 1"
location: "4q31.3"
module: 6
arm: "+"
pooled_cpm: 22.67
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 23
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MND1

*meiotic nuclear divisions 1* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.61× (z +8.1, q 5e-13, up in 26 of 46 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.05 µM: 1.27× (z +3.8, q 0.011, up in 14 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.449× (z -19.1, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLM]] (+0.83, fdr 7e-06), [[EXO1]] (+0.82, fdr 7e-06), [[DTL]] (+0.82, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4259.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.61×** | +8.1 | 5e-13 | 26/46 (SW480, PANC-1, …) | all doses, flat |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.26×** | +5.6 | 6e-06 | 19/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.28×** | +4.3 | 0.004 | 14/46 (SW480, RKO, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.28×** | +4.1 | 0.005 | 10/47 (SW480, RKO, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.28×** | +4.0 | 0.007 | 13/46 (SW480, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.29×** | +4.0 | 0.007 | 11/38 (SW1417, NCI-H2347, …) | inconsistent across doses | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.18× | +3.9 | 0.007 | 14/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.27×** | +3.8 | 0.011 | 14/43 (SW480, NCI-H2347, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.26×** | +3.8 | 0.011 | 15/32 (A549, A-172, …) | inconsistent across doses | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.024 | 9/47 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.23×** | +3.4 | 0.030 | 12/45 (PANC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.038 | 11/46 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.22×** | +3.3 | 0.038 | 14/47 (SW480, RKO, …) | all doses, flat |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.038 | 7/47 (SW480, A-172, …) | top dose only | plate-row cell shift |
| [[Methotrexate (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.065 | 4/47 (SW480, HOP62, …) | two highest doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.065 | 6/47 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.078 | 4/46 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.086 | 10/47 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.087 | 4/47 (SW480, A-172, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4259.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.449×** | -19.1 | 0e+00 | 40/47 (HEC-1-A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.456×** | -13.2 | 2e-37 | 33/46 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.580×** | -8.8 | 3e-16 | 28/47 (HEC-1-A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.440×** | -7.2 | 7e-11 | 28/45 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.451×** | -7.0 | 3e-10 | 23/47 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.676×** | -6.6 | 5e-09 | 22/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.696×** | -6.1 | 1e-07 | 20/46 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.717×** | -5.6 | 2e-06 | 21/46 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.741×** | -5.0 | 3e-05 | 21/45 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.815×** | -4.8 | 7e-05 | 17/47 (RPMI-7951, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.774×** | -4.3 | 1e-03 | 17/46 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.707×** | -4.1 | 0.002 | 15/47 (SW480, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.793×** | -3.9 | 0.005 | 14/44 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.797×** | -3.8 | 0.006 | 18/46 (A498, A-427, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.775×** | -3.8 | 0.006 | 10/47 (A-427, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.852× | -3.8 | 0.006 | 11/47 (SNU-423, HCT15, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.801×** | -3.7 | 0.007 | 18/47 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.679×** | -3.4 | 0.022 | 7/46 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.814×** | -3.3 | 0.028 | 15/44 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.690×** | -3.3 | 0.030 | 13/45 (H4, A-427, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.74 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4259. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 32.3 | 2 (2 ⚠) | 6 (2 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.70× (z +9.5) ⚠ toxic; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 51.1 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -20.9) |
| [[A498 (line)]] | wt | 22.0 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.286× (z -12.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -12.3) |
| [[A-427 (line)]] | wt | 48.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -20.4) |
| [[NCI-H460 (line)]] | wt | 20.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.6) |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 35.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -14.3) |
| [[A-172 (line)]] | wt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -10.4) |
| [[COLO 205 (line)]] | alt | 39.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -10.5) |
| [[H4 (line)]] | wt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -11.3) |
| [[Hs 766T (line)]] | wt | 9.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -9.1) |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 9.77 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.104× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 35.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -15.7) |
| [[LOX-IMVI (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.332× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 18.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 18.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0773× (z -9.9) |
| [[SNU-423 (line)]] | alt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -9.6) |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -12.9) |
| [[SW1417 (line)]] | alt | 19.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.5) |
| [[A549 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4259), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLM]] | +0.83 | +0.82 / +0.87 | both halves | 7e-06 | pathway: Meiosis; STRING 407 |
| [[EXO1]] | +0.82 | +0.80 / +0.85 | both halves | 7e-06 | STRING 878 |
| [[DTL]] | +0.82 | +0.79 / +0.83 | both halves | 7e-06 | STRING 742 |
| [[DNA2]] | +0.82 | +0.76 / +0.84 | both halves | 7e-06 |  |
| [[WDHD1]] | +0.81 | +0.78 / +0.83 | both halves | 7e-06 | STRING 487 |
| [[MMS22L]] | +0.81 | +0.80 / +0.83 | both halves | 7e-06 |  |
| [[POLQ]] | +0.81 | +0.80 / +0.83 | both halves | 7e-06 |  |
| [[FANCI]] | +0.81 | +0.82 / +0.79 | both halves | 7e-06 | STRING 451 |
| [[ATAD5]] | +0.80 | +0.76 / +0.82 | both halves | 7e-06 |  |
| [[GINS1]] | +0.80 | +0.76 / +0.82 | both halves | 7e-06 | STRING 644 |
| [[DSCC1]] | +0.80 | +0.78 / +0.82 | both halves | 7e-06 | STRING 477 |
| [[CENPK]] | +0.79 | +0.80 / +0.82 | both halves | 7e-06 | STRING 575 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises MND1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.63× lower at baseline in the lines without E2F8 | 0.011 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers MND1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FAM111B]] | B | FAM111B activity raises MND1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without FAM111B | 0.073 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises MND1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.04× lower at baseline in the lines without E2F2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises MND1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.60× lower at baseline in the lines without MCM10 | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises MND1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.38× lower at baseline in the lines without DSCC1 | 0.040 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[C21orf58]], [[CDC45]], [[CENPM]], [[SKA3]] | C | C21orf58, CDC45, CENPM, SKA3 activity raises MND1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.69× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CLSPN]] | C | CLSPN activity raises MND1's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.58× lower at baseline in the lines without CLSPN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; its own permutation p |
| [[MYBL2]] | C | MYBL2 activity raises MND1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.49× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[E2F1]] | C | E2F1 activity raises MND1's level | lines that do not express E2F1 (3) vs lines expressing it (47) | 2.48× lower at baseline in the lines without E2F1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |
| [[PKMYT1]] | C | PKMYT1 activity raises MND1's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.21× lower at baseline in the lines without PKMYT1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.823). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.8, -46.3); signed map (-39.0, -44.2). **Vector** length 111, 28.4% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.60 to 65); *DNA strand elongation* (reactome, mean cos +0.66 to 28); *DNA Replication* (reactome, mean cos +0.65 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +5.8 | +8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | +3.8 | +2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.4 | +3.4 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.4 | +5.6 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +3.1 | +3.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +3.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.0 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -19.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -5.6 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.2 | -3.3 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.2 | -3.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | meiotic nuclear divisions 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:153,344,649-153,415,118 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GAJ |
| Reactome | 4 pathways, smallest: Meiotic recombination; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWT6](https://www.uniprot.org/uniprotkb/Q9BWT6) (Meiotic nuclear division protein 1 homolog):

> Required for proper homologous chromosome pairing and efficient cross-over and intragenic recombination during meiosis (By similarity). Stimulates both DMC1- and RAD51-mediated homologous strand assimilation, which is required for the resolution of meiotic double-strand breaks.

**Summary**, from NCBI Gene [84057](https://www.ncbi.nlm.nih.gov/gene/84057):

> The product of the MND1 gene associates with HOP2 (MIM 608665) to form a stable heterodimeric complex that binds DNA and stimulates the recombinase activity of RAD51 (MIM 179617) and DMC1 (MIM 602721) (Chi et al., 2007 [PubMed 17639080]). Both the MND1 and HOP2 genes are indispensable for meiotic recombination.[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24839](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24839) · Entrez [84057](https://www.ncbi.nlm.nih.gov/gene/84057) · UniProt [Q9BWT6](https://www.uniprot.org/uniprotkb/Q9BWT6) · Ensembl [ENSG00000121211](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121211)

## Data

Gene col 4259: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4259); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4259, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4259]; `tensor/DDL_lfc|DDL_z.npy` [4259]; `embed/gene_vectors.npy` [4259]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4259 or target_col == 4259). Every well: [[MND1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MND1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
