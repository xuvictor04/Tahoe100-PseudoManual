---
symbol: "CASC15"
type: "gene"
col: 15712
ensembl_id: "ENSG00000272168"
name: "cancer susceptibility 15"
location: "6p22.3"
module: 19
arm: "+"
pooled_cpm: 56.95
n_lines_expressing: 26
n_dd_up: 11
n_dd_down: 22
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CASC15

*cancer susceptibility 15* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.50× (z +20.0, q 0e+00, up in 8 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.563× (z -8.9, q 4e-16, down in 19 of 23 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.777× (z -3.9, q 0.005, down in 17 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LSAMP]] (+0.67, fdr 1e-05), [[TRPA1]] (+0.63, fdr 2e-05), [[DOK6]] (+0.63, fdr 2e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TNFRSF11B]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GPC6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15712.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +20.0 | 0e+00 | 8/24 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.98×** | +14.9 | 0e+00 | 18/24 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +12.7 | 2e-34 | 7/23 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.08×** | +11.3 | 3e-27 | 20/23 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.2 | 8e-08 | 3/20 (SW 900, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +4.5 | 7e-04 | 5/22 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.30×** | +4.0 | 0.005 | 12/24 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.20× | +3.9 | 0.007 | 8/24 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.057 | 10/23 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.24×** | +3.3 | 0.065 | 9/23 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.068 | 8/23 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.074 | 1/23 (NCI-H2347) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15712.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.563×** | -8.9 | 4e-16 | 19/23 (A-172, C-33 A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.634×** | -7.0 | 5e-10 | 18/24 (C-33 A, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.700×** | -5.5 | 6e-06 | 17/24 (A-172, C-33 A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.713×** | -5.0 | 7e-05 | 16/23 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.764×** | -4.2 | 0.004 | 12/24 (NCI-H460, CHP-212, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.769×** | -4.1 | 0.004 | 13/23 (A-172, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.774×** | -4.0 | 0.005 | 13/23 (CHP-212, NCI-H2030, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.775×** | -4.0 | 0.005 | 9/23 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.776×** | -3.9 | 0.005 | 16/24 (NCI-H1792, CHP-212, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.777×** | -3.9 | 0.005 | 17/24 (RPMI-7951, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.785×** | -3.7 | 0.010 | 14/23 (SHP-77, CHP-212, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.635×** | -3.7 | 0.011 | 13/23 (A-172, NCI-H2030, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.790×** | -3.7 | 0.011 | 15/23 (CHP-212, C-33 A, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.6 | 0.012 | 8/24 (NCI-H460, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.856× | -3.4 | 0.024 | 14/25 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.805×** | -3.4 | 0.026 | 7/23 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.805×** | -3.4 | 0.026 | 11/25 (A-172, A498, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.859× | -3.3 | 0.027 | 9/24 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.815×** | -3.2 | 0.044 | 10/23 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.821×** | -3.0 | 0.062 | 5/24 (NCI-H1792, SHP-77, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.823×** | -3.0 | 0.064 | 11/23 (A498, NCI-H1792, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.695×** | -2.9 | 0.079 | 8/23 (BT-474, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.828×** | -2.9 | 0.082 | 6/23 (NCI-H1792, SHP-77, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.700×** | -2.9 | 0.089 | 10/25 (A-172, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 315 | 0 | 13 (10 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0898× (z -25.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -18.8) |
| [[C-33 A (line)]] | alt | 1,349 | 0 | 12 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0751× (z -24.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -19.9) |
| [[NCI-H460 (line)]] | wt | 155 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -14.3) |
| [[CHP-212 (line)]] | wt | 617 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 114 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -16.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -12.1) |
| [[SHP-77 (line)]] | alt | 67.9 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 58.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -9.8) |
| [[A498 (line)]] | wt | 42.3 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -11.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[AN3 CA (line)]] | alt | 206 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.177× (z -9.8) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 18.7 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.04× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.56× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 21.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.327× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 1 | 0 | [[Trametinib (drug)]] 0.5 µM 3.23× (z +8.5) | — |
| [[A-427 (line)]] | wt | 5.75 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.02 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.30 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.20 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.72 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.26 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.41 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.24 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.80 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.78 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 86.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.55 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.96 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.83 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.75 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.53 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.53 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSAMP]] | +0.67 | +0.55 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[TRPA1]] | +0.63 | +0.68 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[DOK6]] | +0.63 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[CDH7]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[SOX6]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[PDE7B]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[FBXL7]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[TEX41]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 | same gene group |
| [[FRMPD4]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[FYB1]] | +0.59 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[IQCM]] | +0.59 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[NOVA1]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF11B]] | B | TNFRSF11B activity raises CASC15's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without TNFRSF11B | 0.064 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12 |
| [[ZNF804A]] | B | ZNF804A activity raises CASC15's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 2.32× lower at baseline in the lines without ZNF804A | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA |
| [[COL8A1]] | C | COL8A1 activity raises CASC15's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 2.10× lower at baseline in the lines without COL8A1 | 0.041 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[EDIL3]] | C | EDIL3 activity raises CASC15's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 2.22× lower at baseline in the lines without EDIL3 | 0.042 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC; co-absent with the target |
| [[GPC6]] | C | GPC6 activity raises CASC15's level | lines that do not express GPC6 (26) vs lines expressing it (24) | 3.26× lower at baseline in the lines without GPC6 | 0.080 | ⚠ within organs, on part of the lines; also absent: TRPA1, GALNT13, ZMAT4; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPC6]] | C | CASC15 activity raises GPC6's level | lines that do not express CASC15 (24) vs lines expressing it (26) | 5.49× lower at baseline in the lines without CASC15 | 0.049 | ⚠ within organs, on part of the lines; also absent: RAB39A, RARB, TRPA1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.0, 33.3); signed map (41.9, 40.4). **Vector** length 85.5, 24.9% of its response variance represented; |z| ≥ 3 in 787 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +12.2 | +12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.7 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.7 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.5 | +14.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +20.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.7 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.6 | -4.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.4 | -2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -3.0 | -1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -2.7 | -3.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.6 | -1.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | cancer susceptibility 15 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p22.3 — chr6:21,664,184-22,654,455 (+) |
| Ensembl biotype | lncRNA |
| Also known as | lnc-SOX4-1; previously LINC00340 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [401237](https://www.ncbi.nlm.nih.gov/gene/401237):

> This gene produces a long non-coding RNA that may regulate cell proliferation. This RNA is upregulated in hepatocellular carcinoma, where it is thought to function as an oncogene. However, some splice variants of this gene may function as a tumor suppressor in neuroblastoma and other tumor types. Circular RNA variants were observed at this gene. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:28245](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28245) · Entrez [401237](https://www.ncbi.nlm.nih.gov/gene/401237) · Ensembl [ENSG00000272168](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272168)

## Data

Gene col 15712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15712); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15712]; `tensor/DDL_lfc|DDL_z.npy` [15712]; `embed/gene_vectors.npy` [15712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15712 or target_col == 15712). Every well: [[CASC15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASC15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
