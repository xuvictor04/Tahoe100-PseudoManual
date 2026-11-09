---
symbol: "LSP1P4"
type: "gene"
col: 6741
ensembl_id: "ENSG00000143429"
name: "LSP1 pseudogene 4"
location: "2p11.2"
module: 14
arm: "+"
pooled_cpm: 6.25
n_lines_expressing: 43
n_dd_up: 5
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# LSP1P4

*LSP1 pseudogene 4* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.89× (z +8.4, q 3e-14, up in 19 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.401× (z -16.9, q 0e+00, down in 33 of 37 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.612× (z -9.1, q 2e-17, down in 23 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LSP1P5-1]] (+0.79, fdr 7e-06, ⚠ same locus), [[TRIP4]] (+0.61, fdr 1e-05), [[NDUFAF7]] (+0.59, fdr 1e-05), [[EXO5-DT]] (+0.58, fdr 5e-05); moves opposite to [[PER2]] (-0.59, fdr 3e-05), [[CGGBP1]] (-0.57, fdr 1e-05), [[OMA1]] (-0.57, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); 2 go from it, the strongest it → [[RNF149]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6741.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +8.4 | 3e-14 | 19/39 (A498, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.47×** | +5.1 | 1e-04 | 16/38 (A-427, NCI-H1573, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.023 | 9/40 (LS 180, NCI-H1792, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.30×** | +3.5 | 0.059 | 12/41 (LS 180, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.32×** | +3.5 | 0.062 | 7/37 (LS 180, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6741.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.401×** | -16.9 | 0e+00 | 33/37 (LOX-IMVI, A498, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.464×** | -10.0 | 3e-21 | 18/23 (LOX-IMVI, CFPAC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.452×** | -10.0 | 4e-21 | 26/40 (A498, LOX-IMVI, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.612×** | -9.1 | 2e-17 | 23/36 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.492×** | -8.9 | 6e-17 | 17/29 (LOX-IMVI, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.571×** | -7.3 | 3e-11 | 20/41 (LOX-IMVI, H4, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.603×** | -6.1 | 8e-08 | 8/12 (HOP62, LOX-IMVI, …) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.626×** | -6.1 | 8e-08 | 18/40 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.640×** | -5.8 | 4e-07 | 17/36 (C-33 A, H4, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.891× | -5.2 | 1e-05 | 10/41 (LoVo, SW 1271, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **0.689×** | -4.8 | 7e-05 | 13/27 (HepG2/C3A, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.723×** | -4.2 | 0.001 | 15/41 (LOX-IMVI, RPMI-7951, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.640×** | -4.2 | 0.001 | 9/36 (NCI-H1573, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.744×** | -3.8 | 0.005 | 14/31 (NCI-H1792, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **0.750×** | -3.7 | 0.007 | 12/37 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.675×** | -3.7 | 0.009 | 4/30 (Panc 03.27, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **0.755×** | -3.6 | 0.009 | 8/36 (RKO, LS 180, …) | inconsistent across doses | position effect removed |
| [[Decitabine (drug)]] 0.05 µM |  | **0.747×** | -3.5 | 0.014 | 11/35 (SNU-1, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.781×** | -3.2 | 0.038 | 6/36 (H4, COLO 205, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.784×** | -3.2 | 0.042 | 8/38 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Atazanavir (sulfate) (drug)]] 0.5 µM |  | **0.788×** | -3.1 | 0.050 | 10/38 (NCI-H2030, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.777×** | -3.0 | 0.057 | 12/33 (RKO, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6741. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 32.7 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -19.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -15.9) |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0517× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -11.5) |
| [[A498 (line)]] | wt | 11.3 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0573× (z -18.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[CFPAC-1 (line)]] | alt | 8.38 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -9.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2030 (line)]] | alt | 6.23 | 0 | 2 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.142× (z -9.0) |
| [[SW 900 (line)]] | alt | 9.68 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -11.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.0878× (z -9.2) |
| [[SW480 (line)]] | alt | 10.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -11.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 8.32 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -9.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 5.44 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0836× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0664× (z -10.9) ⚠ transcription drop; cell-cycle shift, explains ~56% of this change |
| [[NCI-H1573 (line)]] | alt | 6.33 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -10.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 3.40 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -9.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 6.78 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0785× (z -9.0) |
| [[SW1417 (line)]] | alt | 4.24 | 0 | 1 | — | [[Almonertinib (mesylate) (drug)]] 0.05 µM 0.0663× (z -8.9) |
| [[A-172 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6741), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSP1P5-1]] | +0.79 | +0.75 / +0.81 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TRIP4]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NDUFAF7]] | +0.59 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[EXO5-DT]] | +0.58 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[SDHAP4-1]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CCNY-AS1]] | +0.57 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[DIP2A]] | +0.57 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[RNF216P1]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[GPR89A]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[AP2A2]] | +0.56 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ZNF512]] | +0.55 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[MED10]] | +0.55 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[OTULIN]] | +0.55 | +0.54 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PER2]] | -0.59 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[CGGBP1]] | -0.57 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[OMA1]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[HIVEP2]] | -0.56 | -0.57 / -0.43 | both halves | 4e-05 |  |
| [[SLC12A2]] | -0.56 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[TMEM107]] | -0.53 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[ZNF608]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[DCAF8]] | -0.52 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[ANAPC13]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[LINC01091]] | -0.51 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[NFKB1]] | -0.51 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[METTL25B]] | -0.51 | -0.61 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers LSP1P4's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LSP1P5-1]] | C | LSP1P5-1 activity raises LSP1P4's level | lines that do not express LSP1P5-1 (6) vs lines expressing it (44) | 3.61× lower at baseline in the lines without LSP1P5-1 | 0.084 | ⚠ within organs, on part of the lines; also absent: LSP1P4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF149]] | B | LSP1P4 activity raises RNF149's level | lines that do not express LSP1P4 (7) vs lines expressing it (43) | 1.75× lower at baseline in the lines without LSP1P4 | 0.060 | ⚠ within organs, on part of the lines; also absent: LSP1P5-1; maybe low, not absent; its own permutation p |
| [[LSP1P5-1]] | C | LSP1P4 activity raises LSP1P5-1's level | lines that do not express LSP1P4 (7) vs lines expressing it (43) | 2.92× lower at baseline in the lines without LSP1P4 | 0.060 | ⚠ within organs, on part of the lines; also absent: LSP1P5-1; maybe low, not absent; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction -0.415). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.0, -5.3); signed map (-37.0, -7.4). **Vector** length 58.5, 8.22% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.3 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.2 | +3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | +2.7 | +3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.3 | -16.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.2 | -10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -3.7 | -10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | -3.2 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -2.5 | -6.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | LSP1 pseudogene 4 |
| Locus type | pseudogene |
| Location | 2p11.2 — chr2:91,636,684-91,659,961 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53915](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53915) · Entrez [654342](https://www.ncbi.nlm.nih.gov/gene/654342) · Ensembl [ENSG00000143429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143429)

## Data

Gene col 6741: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6741); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6741, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6741]; `tensor/DDL_lfc|DDL_z.npy` [6741]; `embed/gene_vectors.npy` [6741]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6741 or target_col == 6741). Every well: [[LSP1P4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSP1P4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
