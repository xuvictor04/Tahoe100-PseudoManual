---
symbol: "ZFAND4"
type: "gene"
col: 10281
ensembl_id: "ENSG00000172671"
name: "zinc finger AN1-type containing 4"
location: "10q11.22"
module: 26
arm: "-"
pooled_cpm: 12.78
n_lines_expressing: 46
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# ZFAND4

*zinc finger AN1-type containing 4* — 10q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.77× (z +22.3, q 0e+00, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.922× (z -4.7, q 0.001, down in 7 of 44 measured lines) ⚠ position not correctable. The strongest without an alert is [[PF-06260933 (drug)]] 5 µM: 0.618× (z -4.2, q 0.005, down in 15 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 0.303×, HOP62 0.134×, Panc 03.27 0.224×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 0.334×, A-427 0.247×, A549 0.262×; ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-1 0.159×, NCI-H23 0.299×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB13]] (+0.69, fdr 7e-06), [[RSAD1]] (+0.67, fdr 1e-05), [[TMEM177]] (+0.63, fdr 1e-05); moves opposite to [[LINC02936]] (-0.64, fdr 4e-05), [[LINC02955]] (-0.63, fdr 5e-05), [[CFAP53]] (-0.63, fdr 6e-05).
> It sits in the **-** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZHX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10281.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.77×** | +22.3 | 0e+00 | 41/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.76×** | +22.2 | 0e+00 | 40/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.76×** | +17.0 | 0e+00 | 40/43 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.17×** | +13.0 | 2e-36 | 33/43 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +10.2 | 3e-22 | 31/44 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +8.5 | 1e-15 | 22/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +8.0 | 7e-14 | 25/41 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.28×** | +7.2 | 4e-11 | 21/43 (PANC-1, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.8 | 8e-05 | 11/39 (A-427, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +4.8 | 8e-05 | 16/42 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.32×** | +4.6 | 2e-04 | 10/43 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.31×** | +4.4 | 5e-04 | 13/36 (SW480, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.004 | 13/43 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.018 | 8/44 (NCI-H460, SW1417, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.021 | 4/43 (SNU-423, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10281.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 0.303×, HOP62 0.134×, Panc 03.27 0.224×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 0.334×, A-427 0.247×, A549 0.262×; ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-1 0.159×, NCI-H23 0.299×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -4.7 | 0.001 | 7/44 (HT-29, SNU-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.761×** | -4.6 | 0.001 | 18/43 (LoVo, SW480, …) | rises with dose | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.618×** | -4.2 | 0.005 | 15/38 (NCI-H23, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.784×** | -3.9 | 0.012 | 12/20 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.810×** | -3.5 | 0.047 | 13/41 (SW480, LoVo, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.818×** | -3.4 | 0.067 | 12/40 (COLO 205, A-172, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10281. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.5 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -13.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 11.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 5.88 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 8.68× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 14.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.70× (z +9.2) | [[AZD2858 (drug)]] 0.5 µM 0.102× (z -8.6) ⚠ toxic |
| [[SW480 (line)]] | alt | 18.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.50× (z +14.1) | — |
| [[A498 (line)]] | wt | 15.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0340× (z -20.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 8.26 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.59× (z +10.4) | — |
| [[A-427 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change |
| [[A549 (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change |
| [[AsPC-1 (line)]] | alt | 9.31 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.81× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 17.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.41× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 13.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.67× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 10.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.99× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.965 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10281), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB13]] | +0.69 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RSAD1]] | +0.67 | +0.52 / +0.60 | both halves | 1e-05 | STRING 593 |
| [[TMEM177]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[FXN]] | +0.62 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[BTBD3]] | +0.62 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[CHST10]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[REPS1]] | +0.62 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[COPG2]] | +0.59 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[DNMT3B]] | +0.59 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[MCOLN2]] | +0.59 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[SUGT1P4-STRA6LP]] | +0.59 | +0.37 / +0.62 | both halves | 8e-05 |  |
| [[ZNF30]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02936]] | -0.64 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[LINC02955]] | -0.63 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[CFAP53]] | -0.63 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[ATXN1L]] | -0.62 | -0.37 / -0.59 | both halves | 7e-05 |  |
| [[CCDC90B-AS1]] | -0.61 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[CPEB2-DT]] | -0.61 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[TBCE-1]] | -0.60 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[LINC00571]] | -0.59 | -0.24 / -0.57 | both halves | 4e-04 |  |
| [[C1S]] | -0.59 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[CD27-AS1]] | -0.59 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[TMEM269]] | -0.58 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[TTC41P]] | -0.57 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZHX2]] | B | ZHX2 activity lowers ZFAND4's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.81× higher at baseline in the lines without ZHX2 | 0.056 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **-** arm (projection on the module's main direction -0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-1.0, -2.5); signed map (-38.6, -17.0). **Vector** length 65.2, 11.0% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.5 | +22.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.4 | +8.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.3 | +17.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.2 | +13.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +7.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.1 | +1.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.1 | +0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | -1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change | -3.3 | -2.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -4.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger AN1-type containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.22 — chr10:45,615,500-45,672,780 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40185; previously ANUBL1 |
| Gene groups (HGNC) | Zinc fingers AN1-type |
| Matched by | ensembl_id |

UniProt [Q86XD8](https://www.uniprot.org/uniprotkb/Q86XD8) carries no function annotation.

**Summary**, from NCBI Gene [93550](https://www.ncbi.nlm.nih.gov/gene/93550):

> Predicted to enable zinc ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23504) · Entrez [93550](https://www.ncbi.nlm.nih.gov/gene/93550) · UniProt [Q86XD8](https://www.uniprot.org/uniprotkb/Q86XD8) · Ensembl [ENSG00000172671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172671)

## Data

Gene col 10281: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10281); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10281, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10281]; `tensor/DDL_lfc|DDL_z.npy` [10281]; `embed/gene_vectors.npy` [10281]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10281 or target_col == 10281). Every well: [[ZFAND4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFAND4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
