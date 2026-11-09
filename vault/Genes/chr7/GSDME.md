---
symbol: "GSDME"
type: "gene"
col: 2688
ensembl_id: "ENSG00000105928"
name: "gasdermin E"
location: "7p15.3"
module: 13
arm: "+"
pooled_cpm: 22.49
n_lines_expressing: 35
n_dd_up: 4
n_dd_down: 28
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 22
direction_downstream: 3
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# GSDME

*gasdermin E* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.41× (z +6.7, q 2e-08, up in 15 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 2.54×; ⚠ cell-cycle shift, explains ~48% of this change).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.338× (z -20.9, q 0e+00, down in 26 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VSTM4]] (+0.61, fdr 1e-05), [[ATP6V0D2]] (+0.60, fdr 1e-05), [[ADAM7-AS1]] (+0.59, fdr 1e-05); moves opposite to [[MARK2]] (-0.46, fdr 4e-05), [[ANK3]] (-0.45, fdr 4e-05), [[SRGN]] (-0.42, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[LINC01705]] → it (grade B ⚠); 3 go from it, the strongest it → [[GPR161]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2688.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 2.54×; ⚠ cell-cycle shift, explains ~48% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +6.7 | 2e-08 | 15/32 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.4 | 0.003 | 11/33 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.23×** | +4.1 | 0.007 | 8/32 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.020 | 9/31 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.20×** | +3.6 | 0.030 | 11/33 (PANC-1, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2688.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.338×** | -20.9 | 0e+00 | 26/33 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.368×** | -19.2 | 0e+00 | 26/33 (SNU-423, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.398×** | -17.7 | 0e+00 | 28/33 (A549, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.451×** | -14.7 | 0e+00 | 28/33 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.523×** | -12.5 | 1e-33 | 26/33 (SNU-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.573×** | -10.7 | 1e-24 | 26/30 (AN3 CA, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.688×** | -10.1 | 3e-22 | 17/32 (A549, H4, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.368×** | -10.1 | 5e-22 | 27/32 (NCI-H1792, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.599×** | -9.9 | 4e-21 | 23/33 (A549, H4, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.649×** | -8.3 | 5e-15 | 22/33 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.660×** | -8.0 | 7e-14 | 21/33 (SW 1088, H4, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.458×** | -7.9 | 2e-13 | 19/32 (SW 900, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.715×** | -6.4 | 6e-09 | 19/33 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.725×** | -6.2 | 3e-08 | 15/31 (A549, H4, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.817×** | -5.5 | 2e-06 | 13/33 (SNU-423, Hs 766T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.802×** | -4.2 | 7e-04 | 10/33 (SNU-423, A498, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.802×** | -4.2 | 7e-04 | 14/33 (A498, RPMI-7951, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.812×** | -4.0 | 0.002 | 15/33 (A498, H4, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.867× | -3.8 | 0.003 | 11/33 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Arbutin (drug)]] 5 µM |  | **0.814×** | -3.8 | 0.003 | 5/33 (SW 1271, LOX-IMVI, …) | top dose only | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.820×** | -3.6 | 0.006 | 13/33 (A498, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.830×** | -3.5 | 0.008 | 9/33 (A498, HS-578T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2688. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 108 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -18.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.237× (z -18.1) |
| [[A549 (line)]] | wt | 65.9 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -26.3) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0950× (z -20.8) |
| [[HOP62 (line)]] | alt | 31.6 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.185× (z -15.6) |
| [[H4 (line)]] | wt | 82.1 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -24.2) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -12.9) |
| [[SNU-423 (line)]] | alt | 59.2 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0842× (z -23.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.121× (z -19.6) |
| [[SW 900 (line)]] | alt | 57.9 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -13.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.228× (z -13.1) |
| [[CFPAC-1 (line)]] | alt | 27.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -14.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.258× (z -11.1) |
| [[A-172 (line)]] | wt | 57.3 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.191× (z -14.3) |
| [[HepG2_C3A (line)]] | wt | 54.6 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.168× (z -14.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.223× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 53.2 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -12.3) |
| [[NCI-H1792 (line)]] | alt | 32.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.330× (z -8.7) |
| [[SNU-1 (line)]] | wt | 25.7 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0835× (z -13.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.121× (z -11.3) |
| [[HS-578T (line)]] | alt | 30.5 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -12.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.231× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 23.5 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.115× (z -15.1) |
| [[RPMI-7951 (line)]] | alt | 64.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.229× (z -10.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.234× (z -10.3) |
| [[AN3 CA (line)]] | alt | 39.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0438× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H2347 (line)]] | alt | 23.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -14.3) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.364× (z -9.5) |
| [[SW 1088 (line)]] | alt | 74.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0776× (z -11.2) ⚠ cell-cycle shift, explains ~48% of this change |
| [[J82 (line)]] | alt | 27.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.120× (z -11.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 7.16 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.8) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2688), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VSTM4]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ATP6V0D2]] | +0.60 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[ADAM7-AS1]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[LINC01705]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[LINC01411]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[CYP26B1]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[KCNIP1]] | +0.56 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[CRTAC1]] | +0.55 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[SH3BP5]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[KCNMA1]] | +0.55 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[TMOD1]] | +0.54 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SLC41A2]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARK2]] | -0.46 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ANK3]] | -0.45 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[SRGN]] | -0.42 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[CCND3]] | -0.42 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[ABHD2]] | -0.41 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[SHROOM3]] | -0.41 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[CAVIN2]] | -0.41 | -0.28 / -0.49 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 21, C 1. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01705]] | B | LINC01705 activity raises GSDME's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 3.25× lower at baseline in the lines without LINC01705 | 0.009 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[LRRC49]] | B | LRRC49 activity raises GSDME's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 4.10× lower at baseline in the lines without LRRC49 | 0.019 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[ABI3BP]] | B | ABI3BP activity raises GSDME's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 3.32× lower at baseline in the lines without ABI3BP | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent |
| [[IL1B]] | B | IL1B activity raises GSDME's level | lines that do not express IL1B (30) vs lines expressing it (20) | 3.12× lower at baseline in the lines without IL1B | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[VSTM4]] | B | VSTM4 activity raises GSDME's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 3.73× lower at baseline in the lines without VSTM4 | 0.030 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2 |
| [[ENTHD1]] | B | ENTHD1 activity raises GSDME's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 3.77× lower at baseline in the lines without ENTHD1 | 0.037 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |
| [[CD5L]] | B | CD5L activity raises GSDME's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.63× lower at baseline in the lines without CD5L | 0.041 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity strengthens GSDME's drug response | lines that do not express TMEM92-AS1 (11) vs lines expressing it (22) | the lines without TMEM92-AS1 respond 0.50× as strongly (z diff +2.74); strongest at Homoharringtonine 5 µM: 1.46x vs 0.51x (z diff +7.0) | 0.041 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2; target measured in part of the lines; artifact flags |
| [[EVC2]] | B | EVC2 activity raises GSDME's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 3.03× lower at baseline in the lines without EVC2 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7 |
| [[PTGFR]] | B | PTGFR activity raises GSDME's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 3.46× lower at baseline in the lines without PTGFR | 0.057 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX |
| [[NR3C1]] | B | NR3C1 activity lowers GSDME's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[ITIH5]] | B | ITIH5 activity raises GSDME's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 3.04× lower at baseline in the lines without ITIH5 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR161]] | B | GSDME activity raises GPR161's level | lines that do not express GSDME (15) vs lines expressing it (35) | 2.39× lower at baseline in the lines without GSDME | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000285804, FBXO17, PYGO1 |
| [[LRRC49]] | B | GSDME activity raises LRRC49's level | lines that do not express GSDME (15) vs lines expressing it (35) | 3.11× lower at baseline in the lines without GSDME | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000285804, FBXO17, PYGO1 |
| [[LOXL2]] | C | GSDME activity raises LOXL2's level | lines that do not express GSDME (15) vs lines expressing it (35) | 5.64× lower at baseline in the lines without GSDME | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000285804, FBXO17, PYGO1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.462). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.3, -3.1); signed map (23.0, 51.9). **Vector** length 84.2, 19.0% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +2.8 | -4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.7 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.6 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +0.3 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -7.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.0 | -9.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -10.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.4 | -12.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -2.3 | -10.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.2 | -2.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.0 | -3.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | gasdermin E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:24,698,355-24,757,940 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ICERE-1; previously DFNA5 |
| Gene groups (HGNC) | Gasdermins |
| Hallmark sets | DNA_REPAIR |
| Reactome | 12 pathways, smallest: Release of apoptotic factors from the mitochondria; Regulation of TLR by endogenous ligand; Apoptotic factor-mediated response |
| Matched by | ensembl_id |

**Function**, from UniProt [O60443](https://www.uniprot.org/uniprotkb/O60443) (Gasdermin-E):

> [Gasdermin-E]: Precursor of a pore-forming protein that converts non-inflammatory apoptosis to pyroptosis. This form constitutes the precursor of the pore-forming protein: upon cleavage, the released N-terminal moiety (Gasdermin-E, N-terminal) binds to membranes and forms pores, triggering pyroptosis.; [Gasdermin-E, N-terminal]: Pore-forming protein produced by cleavage by CASP3 or granzyme B (GZMB), which converts non-inflammatory apoptosis to pyroptosis or promotes granzyme-mediated …

**Summary**, from NCBI Gene [1687](https://www.ncbi.nlm.nih.gov/gene/1687):

> Hearing impairment is a heterogeneous condition with over 40 loci described. The protein encoded by this gene is expressed in fetal cochlea, however, its function is not known. Nonsyndromic hearing impairment is associated with a mutation in this gene. Three transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2810](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2810) · Entrez [1687](https://www.ncbi.nlm.nih.gov/gene/1687) · UniProt [O60443](https://www.uniprot.org/uniprotkb/O60443) · Ensembl [ENSG00000105928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105928)

## Data

Gene col 2688: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2688); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2688, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2688]; `tensor/DDL_lfc|DDL_z.npy` [2688]; `embed/gene_vectors.npy` [2688]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2688 or target_col == 2688). Every well: [[GSDME — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSDME.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
