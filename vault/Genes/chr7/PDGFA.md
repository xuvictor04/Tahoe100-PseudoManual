---
symbol: "PDGFA"
type: "gene"
col: 12402
ensembl_id: "ENSG00000197461"
name: "platelet derived growth factor subunit A"
location: "7p22.3"
module: 206
arm: "+"
pooled_cpm: 90.0
n_lines_expressing: 41
n_dd_up: 1
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# PDGFA

*platelet derived growth factor subunit A* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.56× (z +7.7, q 5e-12, up in 22 of 39 measured lines) ⚠ cell-cycle shift, explains ~69% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (AsPC-1 13.8×, Panc 03.27 10.6×, SW 900 10.9×, J82 3.39×, …; ⚠ cell-cycle shift, explains ~69% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (RPMI-7951 7.24×, NCI-H1792 7.67×, Panc 03.27 8.18×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (AsPC-1 4.18×); [[Auranofin (drug)]] 5 µM in 1 line (A-172 3.40×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.339× (z -13.3, q 2e-37, down in 39 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDGFB]] (+0.61, fdr 8e-06), [[PHLDA2]] (+0.57, fdr 1e-05), [[N4BP3]] (+0.57, fdr 1e-05); moves opposite to [[EXOSC10]] (-0.53, fdr 2e-05), [[ADPGK]] (-0.53, fdr 4e-05), [[KAT7]] (-0.51, fdr 3e-05).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LMO3]] → it (grade B ⚠); 4 go from it, the strongest it → [[LAG3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12402.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (AsPC-1 13.8×, Panc 03.27 10.6×, SW 900 10.9×, J82 3.39×, …; ⚠ cell-cycle shift, explains ~69% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (RPMI-7951 7.24×, NCI-H1792 7.67×, Panc 03.27 8.18×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (AsPC-1 4.18×); [[Auranofin (drug)]] 5 µM in 1 line (A-172 3.40×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.56×** | +7.7 | 5e-12 | 22/39 (AsPC-1, Panc 03.27, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12402.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.339×** | -13.3 | 2e-37 | 39/39 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.358×** | -12.6 | 7e-34 | 38/39 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.500×** | -8.5 | 4e-15 | 35/39 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.618×** | -8.3 | 1e-14 | 28/39 (Hs 766T, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.693×** | -4.2 | 0.004 | 18/39 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.722×** | -4.0 | 0.006 | 19/39 (C-33 A, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.572×** | -3.6 | 0.028 | 21/39 (HOP62, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.761×** | -3.3 | 0.059 | 19/39 (NCI-H2347, SW1417, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.766×** | -3.3 | 0.070 | 20/39 (SW480, HOP62, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.609×** | -3.2 | 0.084 | 15/40 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.775×** | -3.1 | 0.095 | 16/39 (Hs 766T, A549, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.834× | -3.1 | 0.095 | 16/39 (SW480, HOP62, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.771×** | -3.1 | 0.095 | 16/38 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.781× | -3.0 | 0.10 | 15/39 (Hs 766T, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12402. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 424 | 0 | 28 (12 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0620× (z -23.8) |
| [[A549 (line)]] | wt | 151 | 0 | 12 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0916× (z -15.4) |
| [[C-33 A (line)]] | alt | 92.9 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 126 | 4 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +29.0) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.18× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.175× (z -13.5) |
| [[HOP62 (line)]] | alt | 84.1 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.7) ⚠ cell-cycle shift, explains ~69% of this change | [[Adagrasib (drug)]] 0.05 µM 0.612× (z -14.3) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.196× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 85.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -13.9) |
| [[J82 (line)]] | alt | 49.2 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +15.0) ⚠ cell-cycle shift, explains ~69% of this change | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 54.4 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 278 | 1 (1 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 7.67× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.337× (z -9.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.250× (z -8.8) |
| [[Hs 766T (line)]] | wt | 125 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.5) ⚠ cell-cycle shift, explains ~69% of this change | [[Selinexor (drug)]] 5 µM 0.326× (z -10.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.243× (z -9.7) |
| [[LoVo (line)]] | wt | 63.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.265× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 281 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0965× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 25.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +19.8) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[SW 1271 (line)]] | alt | 192 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0427× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0725× (z -10.3) |
| [[SW1417 (line)]] | alt | 77.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -12.2) |
| [[A-172 (line)]] | wt | 58.9 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.40× (z +10.0) | — |
| [[A498 (line)]] | wt | 69.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.322× (z -10.6) |
| [[BT-474 (line)]] | alt | 44.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.195× (z -9.9) |
| [[H4 (line)]] | wt | 57.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +10.4) ⚠ cell-cycle shift, explains ~69% of this change | [[Belzutifan (drug)]] 5 µM 0.0677× (z -8.5) |
| [[HS-578T (line)]] | alt | 43.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.265× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 33.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.231× (z -9.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.276× (z -8.5) |
| [[PANC-1 (line)]] | alt | 91.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 37.2 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.24× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 65.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.205× (z -10.1) |
| [[A-427 (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 70.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.339× (z -8.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HepG2_C3A (line)]] | wt | 41.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +9.2) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[KATO III (line)]] | alt | 45.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +14.5) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -8.9) |
| [[SW 900 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +16.2) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[AN3 CA (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 56.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12402), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDGFB]] | +0.61 | +0.58 / +0.60 | both halves | 8e-06 | same gene group; pathway: Constitutive Signaling by Aberrant PI3K in Cancer; STRING 998 |
| [[PHLDA2]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[N4BP3]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[KDM7A]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[FAM43A]] | +0.53 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[DRAP1]] | +0.51 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ZSWIM5]] | +0.51 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[ING1]] | +0.51 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[EHD1]] | +0.51 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[KCNMB4]] | +0.50 | +0.47 / +0.35 | both halves | 1e-04 |  |
| [[ACAP1]] | +0.50 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[CYTH4]] | +0.49 | +0.53 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOSC10]] | -0.53 | -0.49 / -0.52 | both halves | 2e-05 |  |
| [[ADPGK]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[KAT7]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PRPS1]] | -0.48 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[ZZZ3]] | -0.48 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[EIF2B1]] | -0.47 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[NNT]] | -0.47 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[SPAG16]] | -0.46 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[RPE]] | -0.46 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[ANAPC10]] | -0.46 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[MRPS27]] | -0.46 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[NAA50]] | -0.46 | -0.33 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMO3]] | B | LMO3 activity lowers PDGFA's level | lines that do not express LMO3 (36) vs lines expressing it (14) | 1.43× higher at baseline in the lines without LMO3 | 0.085 | ⚠ within organs, on part of the lines; also absent: MUC6, LINC02566, APOD; maybe low, not absent |
| [[MMP17]] | B | MMP17 activity raises PDGFA's level | lines that do not express MMP17 (17) vs lines expressing it (33) | 1.62× lower at baseline in the lines without MMP17 | 0.093 | ⚠ within organs, on part of the lines; also absent: NOVA2, TUB, RIMKLB |
| [[HCN2]] | C | HCN2 activity raises PDGFA's level | lines that do not express HCN2 (6) vs lines expressing it (44) | 2.46× lower at baseline in the lines without HCN2 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, USP31, PRELID3A; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAG3]] | B | PDGFA activity raises LAG3's level | lines that do not express PDGFA (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without PDGFA | 0.016 | ⚠ within organs, on part of the lines; also absent: HCN2; maybe low, not absent |
| [[EFNA2]] | B | PDGFA activity raises EFNA2's level | lines that do not express PDGFA (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without PDGFA | 0.033 | ⚠ within organs, on part of the lines; also absent: HCN2; maybe low, not absent |
| [[ZBTB46]] | B | PDGFA activity raises ZBTB46's level | lines that do not express PDGFA (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without PDGFA | 0.050 | ⚠ within organs, on part of the lines; also absent: HCN2; maybe low, not absent |
| [[HCN2]] | C | PDGFA activity raises HCN2's level | lines that do not express PDGFA (9) vs lines expressing it (41) | 1.87× lower at baseline in the lines without PDGFA | 0.026 | ⚠ within organs, on part of the lines; also absent: HCN2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.3, -2.9); signed map (0.2, 32.6). **Vector** length 106, 26.8% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +8.6 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | -3.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -6.8 | -8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.0 | -2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | -0.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | +0.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.6 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.6 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | platelet derived growth factor subunit A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:497,258-520,296 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PDGF1, PDGF-A |
| Gene groups (HGNC) | PDGF family ligands |
| Hallmark sets | ANGIOGENESIS, P53_PATHWAY |
| Reactome | 25 pathways, smallest: NFE2L2 regulating tumorigenic genes; Downstream signal transduction; Signaling by PDGF |
| Matched by | ensembl_id |

**Function**, from UniProt [P04085](https://www.uniprot.org/uniprotkb/P04085) (Platelet-derived growth factor subunit A):

> Growth factor that plays an essential role in the regulation of embryonic development, cell proliferation, cell migration, survival and chemotaxis. Potent mitogen for cells of mesenchymal origin. Required for normal lung alveolar septum formation during embryogenesis, normal development of the gastrointestinal tract, normal development of Leydig cells and spermatogenesis. Required for normal oligodendrocyte development and normal myelination in the spinal cord and cerebellum. Plays an important …

**Summary**, from NCBI Gene [5154](https://www.ncbi.nlm.nih.gov/gene/5154):

> This gene encodes a member of the protein family comprised of both platelet-derived growth factors (PDGF) and vascular endothelial growth factors (VEGF). The encoded preproprotein is proteolytically processed to generate platelet-derived growth factor subunit A, which can homodimerize, or alternatively, heterodimerize with the related platelet-derived growth factor subunit B. These proteins bind and activate PDGF receptor tyrosine kinases, which play a role in a wide range of developmental …

**Accessions** — [HGNC:8799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8799) · Entrez [5154](https://www.ncbi.nlm.nih.gov/gene/5154) · UniProt [P04085](https://www.uniprot.org/uniprotkb/P04085) · Ensembl [ENSG00000197461](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197461)

## Data

Gene col 12402: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12402); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12402, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12402]; `tensor/DDL_lfc|DDL_z.npy` [12402]; `embed/gene_vectors.npy` [12402]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12402 or target_col == 12402). Every well: [[PDGFA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDGFA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
