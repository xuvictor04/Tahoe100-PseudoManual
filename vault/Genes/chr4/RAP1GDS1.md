---
symbol: "RAP1GDS1"
type: "gene"
col: 6218
ensembl_id: "ENSG00000138698"
name: "Rap1 GTPase-GDP dissociation stimulator 1"
location: "4q23"
module: 18
arm: "+"
pooled_cpm: 97.66
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# RAP1GDS1

*Rap1 GTPase-GDP dissociation stimulator 1* — 4q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.35× (z +6.1, q 5e-07, up in 34 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.25× (z +4.5, q 6e-04, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.626× (z -13.6, q 3e-39, down in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 0.765× (z -3.9, q 0.005, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NLN]] (+0.72, fdr 7e-06), [[KPNA3]] (+0.71, fdr 7e-06), [[CDC123]] (+0.66, fdr 9e-06); moves opposite to [[YY1AP1]] (-0.64, fdr 1e-05), [[APBA3]] (-0.63, fdr 7e-06), [[TNFRSF14]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TRABD2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6218.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +6.1 | 5e-07 | 34/48 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.32×** | +5.7 | 4e-06 | 30/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.33×** | +5.2 | 4e-05 | 31/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.27×** | +4.9 | 1e-04 | 28/48 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +4.5 | 6e-04 | 25/48 (COLO 205, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.16× | +4.2 | 0.003 | 22/49 (NCI-H460, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.003 | 27/48 (A498, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.22×** | +4.1 | 0.003 | 22/48 (NCI-H1573, NCI-H2030, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.22×** | +4.0 | 0.005 | 25/48 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.010 | 25/49 (HT-29, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.010 | 9/48 (MIA PaCa-2, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.20× | +3.7 | 0.010 | 20/48 (NCI-H1573, NCI-H2030, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.042 | 17/47 (C32, NCI-H2030, …) | two highest doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.17× | +3.3 | 0.044 | 15/48 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.18× | +3.2 | 0.048 | 17/48 (SW480, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6218.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.626×** | -13.6 | 3e-39 | 38/48 (A-172, J82, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.627×** | -9.2 | 1e-17 | 38/48 (NCI-H460, J82, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.679×** | -7.9 | 4e-13 | 35/48 (HOP62, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.760×** | -5.2 | 3e-05 | 29/45 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.792×** | -4.8 | 2e-04 | 26/48 (BT-474, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.793×** | -4.7 | 2e-04 | 26/48 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.804×** | -4.5 | 6e-04 | 26/49 (C-33 A, HCT15, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.820×** | -4.1 | 0.003 | 25/48 (NCI-H460, LoVo, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.820×** | -3.9 | 0.005 | 22/44 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.765×** | -3.9 | 0.005 | 24/48 (SW480, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.699×** | -3.8 | 0.006 | 23/45 (SNU-1, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.772×** | -3.8 | 0.007 | 25/47 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.849× | -3.4 | 0.033 | 17/48 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.898× | -3.1 | 0.069 | 4/49 (A549, RKO, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.809×** | -3.1 | 0.070 | 21/48 (SNU-1, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.812×** | -3.0 | 0.082 | 18/48 (Panc 03.27, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 91.2 | 2 (2 ⚠) | 6 (6 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.10× (z +10.3) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -15.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 106 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -22.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[J82 (line)]] | alt | 114 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -20.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-427 (line)]] | wt | 279 | 2 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.14× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.444× (z -11.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 134 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.545× (z -9.2) |
| [[HS-578T (line)]] | alt | 76.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -18.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H1573 (line)]] | alt | 96.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0947× (z -27.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 74.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -18.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SW48 (line)]] | wt | 141 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -12.7) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.396× (z -8.8) |
| [[A549 (line)]] | wt | 90.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -17.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[BT-474 (line)]] | alt | 94.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.343× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -11.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -11.1) ⚠ cell-cycle shift, explains ~47% of this change |
| [[LOX-IMVI (line)]] | wt | 114 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -18.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[PANC-1 (line)]] | alt | 86.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -16.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[RKO (line)]] | wt | 164 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -10.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SNU-1 (line)]] | wt | 162 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -11.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 84.8 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.22× (z +10.3) ⚠ unreliable plate only | — |
| [[AsPC-1 (line)]] | alt | 77.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -10.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[C32 (line)]] | wt | 175 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -9.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[CFPAC-1 (line)]] | alt | 60.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +8.8) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[HCT15 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -9.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 69.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -9.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[LoVo (line)]] | wt | 81.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.473× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -11.1) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H23 (line)]] | alt | 86.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -18.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H2347 (line)]] | alt | 97.1 | 1 | 0 | [[Clobetasol propionate (drug)]] 5 µM 2.16× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 92.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -9.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SK-MEL-2 (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -17.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[AN3 CA (line)]] | alt | 114 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 88.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 85.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 86.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 65.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLN]] | +0.72 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[KPNA3]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 | same gene group |
| [[CDC123]] | +0.66 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[COP1]] | +0.64 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[HACD3]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[TTL]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ABCC4]] | +0.62 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[FARP1]] | +0.62 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CCT3]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[NCK2]] | +0.62 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[EXOC2]] | +0.62 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[UBE3C]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YY1AP1]] | -0.64 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[APBA3]] | -0.63 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[TNFRSF14]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[BTN3A1]] | -0.60 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[ABCA5]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[TEF]] | -0.57 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[NFKB2]] | -0.57 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[BCL3]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[STAP2]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[KMT2E]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ETFRF1]] | -0.56 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[METTL25B]] | -0.56 | -0.60 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRABD2B]] | B | TRABD2B activity raises RAP1GDS1's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.31× lower at baseline in the lines without TRABD2B | 0.076 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |
| [[HDAC6]] | B | HDAC6 activity lowers RAP1GDS1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers RAP1GDS1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ANKRD13B]] | C | ANKRD13B activity raises RAP1GDS1's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 1.59× lower at baseline in the lines without ANKRD13B | 0.097 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.2, -35.1); signed map (-18.6, -49.7). **Vector** length 118, 34.6% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.7 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +7.4 | +5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.8 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +4.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | +4.7 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | +4.6 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.4 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.8 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -11.7 | -13.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.2 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -5.9 | -4.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | -5.0 | -7.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.2 | -3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.1 | -3.4 |
|  | [[Docetaxel (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | Rap1 GTPase-GDP dissociation stimulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q23 — chr4:98,261,384-98,443,858 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SmgGDS |
| Gene groups (HGNC) | Armadillo repeat containing |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 4 pathways, smallest: RHOT1 GTPase cycle; RHOT2 GTPase cycle; Miro GTPase Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P52306](https://www.uniprot.org/uniprotkb/P52306) (Rap1 GTPase-GDP dissociation stimulator 1):

> Acts as a GEF (guanine nucleotide exchange factor) for the Rho family of small GTP-binding proteins (G proteins) that stimulates the dissociation of GDP to enable subsequent binding of GTP. Additionally, appears to chaperone the processing and/or trafficking of small GTPases containing a C-terminal polybasic region independently of GEF activity. Targets include RAP1A/RAP1B, RHOA, RHOB, RHOC, RAC1 and KRAS. Regulates mitochondrial dynamics by controlling RHOT function to promote mitochondrial …

**Summary**, from NCBI Gene [5910](https://www.ncbi.nlm.nih.gov/gene/5910):

> The smg GDP dissociation stimulator (smgGDS) protein is a stimulatory GDP/GTP exchange protein with GTPase activity (Riess et al., 1993 [PubMed 8262526]).[supplied by OMIM, Feb 2010]

**Accessions** — [HGNC:9859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9859) · Entrez [5910](https://www.ncbi.nlm.nih.gov/gene/5910) · UniProt [P52306](https://www.uniprot.org/uniprotkb/P52306) · Ensembl [ENSG00000138698](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138698)

## Data

Gene col 6218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6218); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6218]; `tensor/DDL_lfc|DDL_z.npy` [6218]; `embed/gene_vectors.npy` [6218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6218 or target_col == 6218). Every well: [[RAP1GDS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAP1GDS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
