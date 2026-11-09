---
symbol: "THBS3"
type: "gene"
col: 9779
ensembl_id: "ENSG00000169231"
name: "thrombospondin 3"
location: "1q22"
module: 153
arm: "+"
pooled_cpm: 13.18
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 36
n_dd_up_clean: 4
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# THBS3

*thrombospondin 3* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 1.54× (z +4.7, q 0.002, up in 21 of 48 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Bimiralisib (drug)]] 5 µM: 1.90× (z +3.7, q 0.051, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (18 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.442× (z -9.0, q 1e-16, down in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.548× (z -6.7, q 3e-09, down in 27 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHD3]] (+0.65, fdr 1e-05), [[PLA2G6]] (+0.61, fdr 2e-05), [[GAA]] (+0.60, fdr 1e-05); moves opposite to [[CBR1]] (-0.54, fdr 5e-05), [[SIMC1]] (-0.54, fdr 4e-05), [[ZNF215]] (-0.52, fdr 4e-05).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9779.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.54×** | +4.7 | 0.002 | 21/48 (NCI-H23, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **1.90×** | +3.7 | 0.051 | 12/46 (NCI-H2030, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.097 | 14/48 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.097 | 13/48 (NCI-H2030, A-427, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.097 | 14/48 (NCI-H2030, A-427, …) | all doses, flat | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 19 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9779.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.442×** | -9.0 | 1e-16 | 37/47 (A-172, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.490×** | -7.9 | 9e-13 | 34/47 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.507×** | -7.5 | 1e-11 | 29/47 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.533×** | -7.0 | 5e-10 | 31/47 (LS 180, COLO 205, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.548×** | -6.7 | 3e-09 | 27/44 (NCI-H1573, A549, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.553×** | -6.6 | 5e-09 | 33/45 (A549, HEC-1-A, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.541×** | -6.5 | 5e-09 | 30/46 (COLO 205, CFPAC-1, …) | rises with dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **0.549×** | -6.4 | 1e-08 | 22/40 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.557×** | -6.1 | 8e-08 | 30/46 (NCI-H1573, A549, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.583×** | -6.0 | 1e-07 | 30/47 (COLO 205, H4, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.594×** | -5.7 | 5e-07 | 26/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.600×** | -5.6 | 8e-07 | 25/47 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.624×** | -5.2 | 8e-06 | 24/47 (COLO 205, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.648×** | -4.8 | 7e-05 | 26/47 (COLO 205, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.658×** | -4.6 | 1e-04 | 21/47 (J82, Hs 766T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.664×** | -4.3 | 7e-04 | 19/47 (BT-474, HCT15, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.486×** | -4.2 | 1e-03 | 22/43 (Hs 766T, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.681×** | -4.0 | 0.002 | 19/47 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **0.612×** | -3.9 | 0.003 | 21/45 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.517×** | -3.8 | 0.004 | 14/47 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.718×** | -3.6 | 0.007 | 17/47 (MIA PaCa-2, SNU-1, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.535×** | -3.6 | 0.007 | 12/44 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.553×** | -3.4 | 0.014 | 13/44 (RPMI-7951, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.733×** | -3.4 | 0.014 | 19/46 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.810×** | -3.3 | 0.022 | 18/48 (CHP-212, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.762×** | -2.9 | 0.068 | 9/48 (MIA PaCa-2, RPMI-7951, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9779. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 20.4 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0524× (z -13.5) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.143× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 15.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -10.0) |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0984× (z -8.9) |
| [[C32 (line)]] | wt | 5.40 | 0 | 1 | — | [[Tolmetin (drug)]] 5 µM 0.0622× (z -8.7) |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 7.41 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0884× (z -9.9) |
| [[A-172 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9779), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHD3]] | +0.65 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PLA2G6]] | +0.61 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[GAA]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ZBTB22]] | +0.60 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[TPP1]] | +0.60 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CCNL2]] | +0.59 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[FBRS]] | +0.59 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[CCDC159]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[INPPL1]] | +0.57 | +0.37 / +0.54 | both halves | 8e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[TCTA]] | +0.57 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CRTC2]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CYB5D2]] | +0.57 | +0.41 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBR1]] | -0.54 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[SIMC1]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ZNF215]] | -0.52 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[TXNDC17]] | -0.52 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[MRPL12]] | -0.51 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[KCTD20]] | -0.51 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[HAUS7]] | -0.50 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[POLR3K]] | -0.50 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[SNRPD1]] | -0.50 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[RNF216]] | -0.50 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[MRPL36]] | -0.49 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[DCTPP1]] | -0.49 | -0.33 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K2]] | B | MAP2K2 activity lowers THBS3's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers THBS3's level | compounds that target MAP2K1: 2 of 4 raise it (Binimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.1, -22.1); signed map (16.5, -21.0). **Vector** length 67.7, 12.0% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.2 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | +0.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.8 | +4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +3.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.9 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.2 | -9.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | -2.9 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -5.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.3 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.3 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -5.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.8 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | thrombospondin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,195,588-155,209,051 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Thrombospondin family |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 2 pathways, smallest: Signaling by PDGF; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [P49746](https://www.uniprot.org/uniprotkb/P49746) (Thrombospondin-3):

> Adhesive glycoprotein that mediates cell-to-cell and cell-to-matrix interactions. Can bind to fibrinogen, fibronectin, laminin and type V collagen.

**Summary**, from NCBI Gene [7059](https://www.ncbi.nlm.nih.gov/gene/7059):

> The protein encoded by this gene belongs to the thrombospondin family. Thrombospondin family members are adhesive glycoproteins that mediate cell-to-cell and cell-to-matrix interactions. This protein forms a pentameric molecule linked by a single disulfide bond. This gene shares a common promoter with metaxin 1. Alternate splicing results in coding and non-coding transcript variants. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:11787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11787) · Entrez [7059](https://www.ncbi.nlm.nih.gov/gene/7059) · UniProt [P49746](https://www.uniprot.org/uniprotkb/P49746) · Ensembl [ENSG00000169231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169231)

## Data

Gene col 9779: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9779); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9779, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9779]; `tensor/DDL_lfc|DDL_z.npy` [9779]; `embed/gene_vectors.npy` [9779]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9779 or target_col == 9779). Every well: [[THBS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THBS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
