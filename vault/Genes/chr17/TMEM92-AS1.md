---
symbol: "TMEM92-AS1"
type: "gene"
col: 14744
ensembl_id: "ENSG00000251179"
name: "TMEM92 antisense RNA 1"
location: "17q21.33"
module: 52
arm: "+"
pooled_cpm: 5.89
n_lines_expressing: 34
n_dd_up: 2
n_dd_down: 34
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 14
direction_downstream: 35
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# TMEM92-AS1

*TMEM92 antisense RNA 1* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.89× (z +6.0, q 1e-06, up in 13 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (18 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.125× (z -18.7, q 0e+00, down in 26 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF841]] (+0.70, fdr 7e-06), [[GPR173]] (+0.59, fdr 1e-05), [[KCNK6]] (+0.58, fdr 1e-05); moves opposite to [[TBC1D5]] (-0.61, fdr 1e-05), [[ARID2]] (-0.57, fdr 7e-05), [[DENND1A]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[RFX8]] → it (grade B ⚠); 35 go from it, the strongest it → [[USP24]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14744.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +6.0 | 1e-06 | 13/29 (LoVo, A498, …) | top dose only |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.49×** | +3.6 | 0.097 | 7/31 (BT-474, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.43× | +3.4 | 0.14 | 9/29 (BT-474, LS 180, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14744.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.125×** | -18.7 | 0e+00 | 26/30 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.346×** | -14.0 | 4e-42 | 22/28 (A498, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.256×** | -12.7 | 7e-35 | 25/32 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.258×** | -12.7 | 1e-34 | 27/32 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.273×** | -12.1 | 8e-32 | 23/29 (H4, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.285×** | -11.7 | 8e-30 | 24/32 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.425×** | -11.3 | 1e-27 | 24/28 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.300×** | -11.2 | 2e-27 | 26/32 (NCI-H1792, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.410×** | -8.3 | 6e-15 | 19/25 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.389×** | -7.7 | 1e-12 | 23/31 (A-172, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.400×** | -7.4 | 5e-12 | 23/29 (BT-474, HOP62, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.446×** | -7.2 | 2e-11 | 20/26 (A498, NCI-H2347, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.489×** | -6.4 | 6e-09 | 18/27 (CFPAC-1, H4, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.491×** | -6.4 | 7e-09 | 19/29 (BT-474, H4, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.275×** | -6.3 | 1e-08 | 15/28 (hTERT-HPNE, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.275×** | -6.3 | 1e-08 | 20/28 (SNU-423, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.548×** | -5.6 | 7e-07 | 15/30 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.573×** | -5.2 | 6e-06 | 16/30 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.658×** | -3.9 | 0.002 | 12/30 (H4, A-172, …) | all doses, stronger at high dose |  |
| [[Gefitinib (drug)]] 5 µM |  | **0.662×** | -3.8 | 0.003 | 8/32 (NCI-H460, H4, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.628×** | -3.8 | 0.004 | 12/29 (LoVo, H4, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.547×** | -2.9 | 0.063 | 11/25 (A-172, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.716×** | -2.9 | 0.063 | 12/29 (NCI-H1792, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.727×** | -2.8 | 0.082 | 5/28 (A549, HT-29, …) | top dose only |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.740×** | -2.8 | 0.089 | 6/29 (SW 1088, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14744. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 42.5 | 0 | 17 (12 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0401× (z -17.0) |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 11 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.00609× (z -28.1) |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0249× (z -20.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0846× (z -9.1) |
| [[HOP62 (line)]] | alt | 10.1 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -14.1) |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 10 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0307× (z -14.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -13.5) |
| [[A498 (line)]] | wt | 19.8 | 0 | 9 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0171× (z -28.7) |
| [[SNU-423 (line)]] | alt | 16.7 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0397× (z -18.6) |
| [[A-172 (line)]] | wt | 15.0 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0703× (z -19.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0970× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 6.64 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0341× (z -20.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0922× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 8.86 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0400× (z -11.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0523× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -11.6) |
| [[A549 (line)]] | wt | 7.04 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0426× (z -17.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0770× (z -9.5) |
| [[HT-29 (line)]] | alt | 5.04 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0929× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 4.59 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -11.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW 900 (line)]] | alt | 7.32 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0328× (z -12.0) |
| [[J82 (line)]] | alt | 4.55 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0742× (z -9.1) |
| [[KATO III (line)]] | alt | 3.80 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0482× (z -8.7) |
| [[LoVo (line)]] | wt | 3.25 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0492× (z -8.6) |
| [[A-427 (line)]] | wt | 0.468 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.964 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.820 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.38 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14744), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF841]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[GPR173]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[KCNK6]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SWI5]] | +0.58 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[NLRP1]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SLC25A42]] | +0.57 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ZNF568]] | +0.57 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[PCYT1A]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ZNF417]] | +0.55 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[EDNRA]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[TFAP2E]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[C19orf25]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D5]] | -0.61 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[ARID2]] | -0.57 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[DENND1A]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[DPY19L1P1]] | -0.52 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[PARD3B]] | -0.51 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[VPS13A]] | -0.51 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[CDH2]] | -0.50 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[TMEM123]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[CDK6]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[PDE3B]] | -0.50 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[PEG10]] | -0.50 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[NFIB]] | -0.50 | -0.47 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 11, C 3. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFX8]] | B | RFX8 activity raises TMEM92-AS1's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.81× lower at baseline in the lines without RFX8 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[LINC01705]] | B | LINC01705 activity raises TMEM92-AS1's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 2.31× lower at baseline in the lines without LINC01705 | 0.004 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[APCDD1L]] | B | APCDD1L activity raises TMEM92-AS1's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 3.21× lower at baseline in the lines without APCDD1L | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[NLRP1]] | B | NLRP1 activity raises TMEM92-AS1's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 2.27× lower at baseline in the lines without NLRP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[LOX]] | B | LOX activity raises TMEM92-AS1's level | lines that do not express LOX (31) vs lines expressing it (19) | 3.12× lower at baseline in the lines without LOX | 0.019 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[TREM1]] | B | TREM1 activity raises TMEM92-AS1's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.45× lower at baseline in the lines without TREM1 | 0.021 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[COL5A1]] | B | COL5A1 activity raises TMEM92-AS1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.68× lower at baseline in the lines without COL5A1 | 0.025 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[LINC02257]] | B | LINC02257 activity raises TMEM92-AS1's level | lines that do not express LINC02257 (15) vs lines expressing it (35) | 2.21× lower at baseline in the lines without LINC02257 | 0.031 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent |
| [[DAB2]] | B | DAB2 activity raises TMEM92-AS1's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 2.25× lower at baseline in the lines without DAB2 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3 |
| [[SYNDIG1]] | B | SYNDIG1 activity raises TMEM92-AS1's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 3.56× lower at baseline in the lines without SYNDIG1 | 0.069 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1 |
| [[KCNK6]] | B | KCNK6 activity raises TMEM92-AS1's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.78× lower at baseline in the lines without KCNK6 | 0.081 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[EDNRA]] | C | EDNRA activity raises TMEM92-AS1's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 2.85× lower at baseline in the lines without EDNRA | 0.003 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 32, C 3. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP24]] | B | TMEM92-AS1 activity lowers USP24's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.40× higher at baseline in the lines without TMEM92-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[SELENOS]] | B | TMEM92-AS1 activity raises SELENOS's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without TMEM92-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[MIR22HG]] | B | TMEM92-AS1 activity raises MIR22HG's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.88× lower at baseline in the lines without TMEM92-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[METRNL]] | B | TMEM92-AS1 activity raises METRNL's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 2.32× lower at baseline in the lines without TMEM92-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[SDF2]] | B | TMEM92-AS1 activity raises SDF2's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.24× lower at baseline in the lines without TMEM92-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| cells under [[TAK-733 (drug)]] 0.05 µM | B | TMEM92-AS1 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express TMEM92-AS1 (16) vs lines expressing it (32) | the lines without TMEM92-AS1: 1.15× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[GSDME]] | B | TMEM92-AS1 activity strengthens GSDME's drug response | lines that do not express TMEM92-AS1 (11) vs lines expressing it (22) | the lines without TMEM92-AS1 respond 0.50× as strongly (z diff +2.74); strongest at Homoharringtonine 5 µM: 1.46x vs 0.51x (z diff +7.0) | 0.041 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2; target measured in part of the lines; artifact flags |
| [[KCTD21]] | B | TMEM92-AS1 activity raises KCTD21's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.30× lower at baseline in the lines without TMEM92-AS1 | 0.042 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[LINC02257]] | B | TMEM92-AS1 activity raises LINC02257's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 2.21× lower at baseline in the lines without TMEM92-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[ACBD3]] | B | TMEM92-AS1 activity raises ACBD3's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.43× lower at baseline in the lines without TMEM92-AS1 | 0.047 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[NAGK]] | B | TMEM92-AS1 activity raises NAGK's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.49× lower at baseline in the lines without TMEM92-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[LINC01705]] | B | TMEM92-AS1 activity raises LINC01705's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 3.32× lower at baseline in the lines without TMEM92-AS1 | 0.053 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (19.3, -36.9); signed map (-31.7, 38.3). **Vector** length 84.1, 22.1% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.6 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.7 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.5 | -2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +1.8 | -7.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.5 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -11.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -18.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.4 | -12.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.4 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -0.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.8 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | TMEM92 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.33 — chr17:50,281,577-50,287,855 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-893F2.9, lncRNA-508851, TCONS_00025237 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50442](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50442) · Entrez [103752589](https://www.ncbi.nlm.nih.gov/gene/103752589) · Ensembl [ENSG00000251179](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251179)

## Data

Gene col 14744: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14744); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14744, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14744]; `tensor/DDL_lfc|DDL_z.npy` [14744]; `embed/gene_vectors.npy` [14744]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14744 or target_col == 14744). Every well: [[TMEM92-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM92-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
