---
symbol: "TEKT4P2-1"
type: "gene"
col: 16554
ensembl_id: "ENSG00000291050"
name: ""
location: ""
module: 89
arm: "+"
pooled_cpm: 7.35
n_lines_expressing: 30
n_dd_up: 4
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# TEKT4P2-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.55× (z +6.0, q 1e-06, up in 15 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.705× (z -6.7, q 1e-08, down in 14 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 0.0668×, NCI-H23 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.325×, A-427 0.374×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.220×); [[Verapamil (drug)]] 0.05 µM in 1 line (CHP-212 0.0517×); [[Bosentan (hydrate) (drug)]] 0.05 µM in 1 line (A-172 0.0986×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAFIP]] (+0.72, fdr 7e-06), [[MED28]] (+0.58, fdr 3e-05), [[SLC25A17]] (+0.57, fdr 3e-05); moves opposite to [[EZH2]] (-0.49, fdr 2e-05), [[RELL1]] (-0.48, fdr 9e-05), [[SHOC2]] (-0.48, fdr 1e-04).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF790-AS1]] → it (grade B ⚠); 5 go from it, the strongest it → [[LINC01535]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16554.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +6.0 | 1e-06 | 15/28 (RPMI-7951, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +5.1 | 9e-05 | 0/11 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.78×** | +4.1 | 0.009 | 4/28 (A498, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.23×** | +3.9 | 0.013 | 5/28 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.31× | +3.3 | 0.12 | 1/26 (NCI-H23) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16554.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 0.0668×, NCI-H23 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.325×, A-427 0.374×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.220×); [[Verapamil (drug)]] 0.05 µM in 1 line (CHP-212 0.0517×); [[Bosentan (hydrate) (drug)]] 0.05 µM in 1 line (A-172 0.0986×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -6.7 | 1e-08 | 14/27 (SK-MEL-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.704×** | -4.3 | 0.004 | 8/28 (A498, H4, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **0.741×** | -4.1 | 0.008 | 13/24 (RPMI-7951, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.784× | -3.3 | 0.11 | 5/28 (A498, H4, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.843× | -3.3 | 0.11 | 3/28 (SHP-77, Panc 03.27, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | 0.795× | -3.1 | 0.16 | 3/28 (A498, RPMI-7951, …) | rises with dose |  |
| [[Hesperidin (drug)]] 0.05 µM |  | 0.783× | -3.1 | 0.16 | 9/28 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.783× | -3.0 | 0.16 | 14/27 (A-172, NCI-H23, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.733× | -3.0 | 0.16 | 6/28 (A-172, C32, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16554. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 26.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0668× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 4.66 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0986× (z -8.5) |
| [[A-427 (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 26.7 | 0 | 1 | — | [[Verapamil (drug)]] 0.05 µM 0.0517× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 62.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.158× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~55% of this change |
| [[SHP-77 (line)]] | alt | 4.12 | 0 | 1 | — | [[Apalutamide (drug)]] 0.05 µM 0.0697× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -10.1) |
| [[SNU-423 (line)]] | alt | 6.46 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.126× (z -8.5) ⚠ toxic |
| [[A549 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.978 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.921 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.859 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.899 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16554), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAFIP]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[MED28]] | +0.58 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[SLC25A17]] | +0.57 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[ZNF169]] | +0.57 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[MED9]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[UQCC1]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[DNAJC7]] | +0.54 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[PEX26]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ZSCAN20]] | +0.53 | +0.31 / +0.57 | both halves | 2e-04 |  |
| [[TRMT61B]] | +0.53 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[XPNPEP3]] | +0.53 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[ZSCAN25]] | +0.52 | +0.42 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EZH2]] | -0.49 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[RELL1]] | -0.48 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[SHOC2]] | -0.48 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[CDKL5]] | -0.46 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[SVIP]] | -0.45 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[TRIM36]] | -0.45 | -0.24 / -0.51 | both halves | 5e-04 |  |
| [[CRY1]] | -0.45 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[STK17B]] | -0.44 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[UACA]] | -0.44 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[TXNDC16]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[LFNG]] | -0.43 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[LNX2]] | -0.43 | -0.37 / -0.48 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF790-AS1]] | B | ZNF790-AS1 activity raises TEKT4P2-1's level | lines that do not express ZNF790-AS1 (26) vs lines expressing it (24) | 2.11× lower at baseline in the lines without ZNF790-AS1 | 0.056 | ⚠ within organs, on part of the lines; also absent: ZNF880, ZNF829, ZNF354C |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01535]] | B | TEKT4P2-1 activity raises LINC01535's level | lines that do not express TEKT4P2-1 (20) vs lines expressing it (30) | 1.80× lower at baseline in the lines without TEKT4P2-1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000291032, ENSG00000291065, IL1RAPL1 |
| [[EZH2]] | B | TEKT4P2-1 activity raises EZH2's level | lines that do not express TEKT4P2-1 (20) vs lines expressing it (30) | 1.13× lower at baseline in the lines without TEKT4P2-1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000291032, ENSG00000291065, IL1RAPL1 |
| [[EIF3M]] | B | TEKT4P2-1 activity raises EIF3M's level | lines that do not express TEKT4P2-1 (20) vs lines expressing it (30) | 1.20× lower at baseline in the lines without TEKT4P2-1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000291032, ENSG00000291065, IL1RAPL1 |
| [[ZNF322]] | B | TEKT4P2-1 activity raises ZNF322's level | lines that do not express TEKT4P2-1 (20) vs lines expressing it (30) | 1.12× lower at baseline in the lines without TEKT4P2-1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000291032, ENSG00000291065, IL1RAPL1 |
| [[ZNF790-AS1]] | B | TEKT4P2-1 activity raises ZNF790-AS1's level | lines that do not express TEKT4P2-1 (20) vs lines expressing it (30) | 2.08× lower at baseline in the lines without TEKT4P2-1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000291032, ENSG00000291065, IL1RAPL1 |

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.1, 10.2); signed map (-11.5, -18.9). **Vector** length 30.9, 3.65% of its response variance represented; |z| ≥ 3 in 519 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.5 | +6.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +1.6 | +3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +1.4 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.2 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.6 | +0.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +0.6 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.7 | -6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.0 | -3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -0.9 | -0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -0.9 | -3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.8 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.6 | -0.3 |
|  | [[NVP-BHG712 (drug)]] 0.5 µM |  | -0.6 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.6 | -0.3 |

## What is on record

> [!warning] No registry record
> TEKT4P2-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16554: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16554); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16554, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16554]; `tensor/DDL_lfc|DDL_z.npy` [16554]; `embed/gene_vectors.npy` [16554]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16554 or target_col == 16554). Every well: [[TEKT4P2-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEKT4P2-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
