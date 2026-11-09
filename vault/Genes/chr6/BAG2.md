---
symbol: "BAG2"
type: "gene"
col: 3335
ensembl_id: "ENSG00000112208"
name: "BAG cochaperone 2"
location: "6p12.1"
module: 135
arm: "+"
pooled_cpm: 20.32
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# BAG2

*BAG cochaperone 2* — 6p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.76× (z +20.2, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.759× (z -5.5, q 2e-05, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.238×, SHP-77 0.286×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.373×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.406×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO30]] (+0.71, fdr 1e-05), [[YIPF7]] (+0.71, fdr 2e-05), [[TYW3]] (+0.69, fdr 1e-05); moves opposite to [[DHTKD1]] (-0.65, fdr 3e-05), [[MCRIP1]] (-0.64, fdr 1e-05), [[SH3GL1]] (-0.62, fdr 7e-05).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF382]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3335.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.76×** | +20.2 | 0e+00 | 42/46 (LoVo, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.58×** | +18.9 | 0e+00 | 42/47 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.57×** | +18.8 | 0e+00 | 42/47 (LoVo, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +13.1 | 5e-37 | 38/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.88×** | +11.9 | 2e-30 | 40/47 (AsPC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.76×** | +11.3 | 2e-27 | 37/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +10.7 | 1e-24 | 26/38 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +9.9 | 2e-21 | 31/47 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +9.9 | 3e-21 | 24/47 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +9.4 | 2e-19 | 29/48 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +9.3 | 1e-18 | 6/48 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +9.1 | 3e-18 | 25/45 (LoVo, H4, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +7.5 | 3e-12 | 25/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.9 | 2e-10 | 16/33 (NCI-H2030, HT-29, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +6.9 | 2e-10 | 23/48 (J82, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +5.6 | 8e-07 | 21/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +5.0 | 2e-05 | 21/47 (LOX-IMVI, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.9 | 3e-05 | 12/48 (A-172, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 1e-04 | 17/48 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.004 | 6/48 (HOP62, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3335.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.238×, SHP-77 0.286×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.373×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.406×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.759×** | -5.5 | 2e-05 | 23/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -3.5 | 0.16 | 20/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.856× | -3.1 | 0.21 | 8/48 (H4, A-427, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.857× | -3.1 | 0.21 | 9/46 (CHP-212, H4, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.857× | -3.1 | 0.21 | 7/46 (COLO 205, HS-578T, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.854× | -3.1 | 0.21 | 8/46 (RPMI-7951, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3335. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 27.8 | 3 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.52× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.373× (z -10.1) |
| [[A498 (line)]] | wt | 12.3 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.61× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 16.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 8.51× (z +13.2) | — |
| [[LoVo (line)]] | wt | 23.4 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.89× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 21.8 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.57× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 20.2 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.01× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.52× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 19.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.88× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 36.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.74× (z +11.6) | — |
| [[A-172 (line)]] | wt | 13.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.51× (z +9.6) | — |
| [[A549 (line)]] | wt | 13.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.34× (z +9.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 11.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.09× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 12.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 13.3× (z +9.8) | — |
| [[J82 (line)]] | alt | 17.5 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.43× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.10× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.39× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.44× (z +10.5) | — |
| [[RKO (line)]] | wt | 36.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.75× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -8.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 26.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.44× (z +9.1) | — |
| [[A-427 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3335), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO30]] | +0.71 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[YIPF7]] | +0.71 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[TYW3]] | +0.69 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[PARD6G-AS1]] | +0.68 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[RHBDD3]] | +0.67 | +0.73 / +0.32 | both halves | 2e-04 |  |
| [[CAP2]] | +0.67 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[POLR2M]] | +0.66 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[AP5M1]] | +0.66 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[FKBP4]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 | pathway: Cellular response to heat stress |
| [[AIFM2]] | +0.65 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[HTATIP2]] | +0.65 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[RNF6]] | +0.65 | +0.63 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHTKD1]] | -0.65 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[MCRIP1]] | -0.64 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[SH3GL1]] | -0.62 | -0.61 / -0.37 | both halves | 7e-05 |  |
| [[MINK1]] | -0.59 | -0.52 / -0.43 | both halves | 4e-05 |  |
| [[LCMT1]] | -0.59 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[PI4KA]] | -0.58 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[EFHC1]] | -0.58 | -0.55 / -0.29 | both halves | 3e-04 |  |
| [[ANAPC11]] | -0.57 | -0.55 / -0.29 | both halves | 3e-04 |  |
| [[CDKN2D]] | -0.56 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[B3GAT3]] | -0.56 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[TXNDC17]] | -0.55 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[COX6A1]] | -0.55 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF382]] | B | ZNF382 activity raises BAG2's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 1.29× lower at baseline in the lines without ZNF382 | 0.085 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[LINC00839]] | B | LINC00839 activity raises BAG2's level | lines that do not express LINC00839 (24) vs lines expressing it (26) | 1.09× lower at baseline in the lines without LINC00839 | 0.094 | ⚠ within organs, on part of the lines; also absent: PRR16, CCNYL2, PCDH10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.738). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-16.5, 10.5); signed map (21.4, -25.0). **Vector** length 87.8, 17.8% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.6 | +20.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.9 | +18.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.7 | +11.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +18.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.8 | +6.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +4.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +3.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.3 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | -2.6 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -1.3 | -2.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Aprepitant (drug)]] 0.05 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | BAG cochaperone 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.1 — chr6:57,172,326-57,189,833 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | BAG cochaperones |
| Reactome | 7 pathways, smallest: Regulation of HSF1-mediated heat shock response; Dengue Virus Genome Translation and Replication; Cellular response to heat stress |
| Matched by | ensembl_id |

**Function**, from UniProt [O95816](https://www.uniprot.org/uniprotkb/O95816) (BAG family molecular chaperone regulator 2):

> Co-chaperone for HSP70 and HSC70 chaperone proteins. Acts as a nucleotide-exchange factor (NEF) promoting the release of ADP from the HSP70 and HSC70 proteins thereby triggering client/substrate protein release.

**Summary**, from NCBI Gene [9532](https://www.ncbi.nlm.nih.gov/gene/9532):

> BAG proteins compete with Hip for binding to the Hsc70/Hsp70 ATPase domain and promote substrate release. All the BAG proteins have an approximately 45-amino acid BAG domain near the C terminus but differ markedly in their N-terminal regions. The predicted BAG2 protein contains 211 amino acids. The BAG domains of BAG1, BAG2, and BAG3 interact specifically with the Hsc70 ATPase domain in vitro and in mammalian cells. All 3 proteins bind with high affinity to the ATPase domain of Hsc70 and …

**Accessions** — [HGNC:938](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:938) · Entrez [9532](https://www.ncbi.nlm.nih.gov/gene/9532) · UniProt [O95816](https://www.uniprot.org/uniprotkb/O95816) · Ensembl [ENSG00000112208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112208)

## Data

Gene col 3335: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3335); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3335, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3335]; `tensor/DDL_lfc|DDL_z.npy` [3335]; `embed/gene_vectors.npy` [3335]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3335 or target_col == 3335). Every well: [[BAG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
