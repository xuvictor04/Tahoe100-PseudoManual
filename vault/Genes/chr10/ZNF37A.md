---
symbol: "ZNF37A"
type: "gene"
col: 1117
ensembl_id: "ENSG00000075407"
name: "zinc finger protein 37A"
location: "10p11.1"
module: 4
arm: "+"
pooled_cpm: 72.92
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ZNF37A

*zinc finger protein 37A* — 10p11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.31× (z +6.7, q 1e-08, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.648× (z -15.2, q 0e+00, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.616× (z -12.0, q 5e-31, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF337]] (+0.67, fdr 7e-06), [[ANKAR]] (+0.65, fdr 1e-05), [[ZNF195]] (+0.62, fdr 1e-05); moves opposite to [[DHTKD1]] (-0.54, fdr 5e-05), [[CHEK2]] (-0.53, fdr 8e-05), [[TBC1D10A]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1117.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +6.7 | 1e-08 | 28/48 (C-33 A, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +6.0 | 7e-07 | 26/48 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.26×** | +5.5 | 7e-06 | 26/48 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.24×** | +5.4 | 7e-06 | 25/48 (COLO 205, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.7 | 2e-04 | 20/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.42×** | +4.6 | 5e-04 | 22/49 (RKO, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.16× | +3.6 | 0.025 | 16/48 (LoVo, A498, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.040 | 16/48 (HT-29, MIA PaCa-2, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.10× | +3.3 | 0.062 | 17/48 (A498, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.14× | +3.2 | 0.066 | 16/47 (A-427, J82, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +3.1 | 0.088 | 3/48 (NCI-H1573, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1117.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.648×** | -15.2 | 0e+00 | 31/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.606×** | -12.4 | 4e-33 | 39/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.616×** | -12.0 | 5e-31 | 39/48 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.628×** | -11.5 | 1e-28 | 40/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.649×** | -10.7 | 8e-25 | 39/48 (LOX-IMVI, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.674×** | -9.4 | 4e-19 | 37/48 (MIA PaCa-2, RKO, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.737×** | -7.6 | 3e-12 | 31/48 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.756×** | -6.7 | 2e-09 | 29/47 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -5.8 | 3e-07 | 2/50 (SW 1271, NCI-H2122) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.683×** | -4.9 | 4e-05 | 21/48 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.822×** | -4.8 | 7e-05 | 23/48 (SNU-423, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -4.8 | 7e-05 | 16/48 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.825×** | -4.8 | 8e-05 | 20/48 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.791×** | -4.2 | 0.001 | 20/48 (LS 180, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | 0.875× | -3.1 | 0.064 | 14/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 73.8 | 4 (4 ⚠) | 4 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | [[Belinostat (drug)]] 5 µM 0.438× (z -10.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.470× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 118 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -19.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.498× (z -8.9) |
| [[LoVo (line)]] | wt | 74.4 | 2 (2 ⚠) | 4 (4 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +11.2) ⚠ cell-cycle shift, explains ~73% of this change | [[Digitoxin (drug)]] 5 µM 0.484× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 91.8 | 1 (1 ⚠) | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +10.6) ⚠ cell-cycle shift, explains ~56% of this change | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -15.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.442× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 88.9 | 1 (1 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.55× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.439× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.482× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 76.0 | 1 (1 ⚠) | 5 (4 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.442× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.513× (z -9.6) |
| [[RKO (line)]] | wt | 208 | 1 (1 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +12.7) ⚠ cell-cycle shift, explains ~56% of this change | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -14.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.533× (z -8.7) |
| [[LS 180 (line)]] | wt | 67.4 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +17.3) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[A-172 (line)]] | wt | 126 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -12.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.533× (z -8.6) |
| [[BT-474 (line)]] | alt | 60.3 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.286× (z -12.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[CHP-212 (line)]] | wt | 135 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Futibatinib (drug)]] 5 µM 0.0838× (z -8.8) |
| [[SNU-423 (line)]] | alt | 66.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -11.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 87.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.364× (z -12.3) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A498 (line)]] | wt | 44.8 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +13.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 48.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -14.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C-33 A (line)]] | alt | 175 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.12× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 56.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -12.0) ⚠ cell-cycle shift, explains ~60% of this change |
| [[J82 (line)]] | alt | 71.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -11.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[PANC-1 (line)]] | alt | 53.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.447× (z -10.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[CFPAC-1 (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -11.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[H4 (line)]] | wt | 29.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[HOP62 (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -13.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[RPMI-7951 (line)]] | alt | 86.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -10.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 184 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 77.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.230× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 52.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -11.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 80.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.493× (z -10.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 122 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 103 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 143 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1117), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF337]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 | same gene group |
| [[ANKAR]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ZNF195]] | +0.62 | +0.52 / +0.53 | both halves | 1e-05 | same gene group |
| [[TSR1]] | +0.58 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[AIFM2]] | +0.56 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[BLOC1S2]] | +0.56 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[UQCC1]] | +0.56 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[PEX26]] | +0.55 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[LARP4]] | +0.55 | +0.55 / +0.39 | both halves | 6e-05 |  |
| [[WDR81]] | +0.55 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[UBXN8]] | +0.55 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[BAG2]] | +0.55 | +0.52 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHTKD1]] | -0.54 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[CHEK2]] | -0.53 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[TBC1D10A]] | -0.51 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[SLC35B2]] | -0.51 | -0.50 / -0.22 | both halves | 6e-04 |  |
| [[CDKN2D]] | -0.49 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[GUSBP18]] | -0.48 | -0.41 / -0.24 | both halves | 4e-04 |  |
| [[TYK2]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers ZNF37A's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.360). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-17.3, 16.8); signed map (11.3, -46.4). **Vector** length 111, 28.6% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +6.9 | +5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | +6.8 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +5.3 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +6.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +1.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.3 | -12.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.1 | -11.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.3 | -10.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.2 | -9.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -4.3 | -12.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -4.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | -4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 37A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.1 — chr10:38,094,334-38,150,293 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KOX21, ZNF37 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17032](https://www.uniprot.org/uniprotkb/P17032) (Zinc finger protein 37A):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7587](https://www.ncbi.nlm.nih.gov/gene/7587):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13102) · Entrez [7587](https://www.ncbi.nlm.nih.gov/gene/7587) · UniProt [P17032](https://www.uniprot.org/uniprotkb/P17032) · Ensembl [ENSG00000075407](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075407)

## Data

Gene col 1117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1117); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1117, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1117]; `tensor/DDL_lfc|DDL_z.npy` [1117]; `embed/gene_vectors.npy` [1117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1117 or target_col == 1117). Every well: [[ZNF37A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF37A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
