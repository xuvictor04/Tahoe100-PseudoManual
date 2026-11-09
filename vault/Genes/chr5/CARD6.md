---
symbol: "CARD6"
type: "gene"
col: 5305
ensembl_id: "ENSG00000132357"
name: "caspase recruitment domain family member 6"
location: "5p13.1"
module: 7
arm: "+"
pooled_cpm: 3.76
n_lines_expressing: 33
n_dd_up: 27
n_dd_down: 14
n_dd_up_clean: 20
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 12
direction_downstream: 25
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CARD6

*caspase recruitment domain family member 6* — 5p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.31× (z +7.7, q 8e-12, up in 1 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.69× (z +7.4, q 4e-11, up in 13 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.259× (z -13.4, q 5e-38, down in 23 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF189]] (+0.68, fdr 1e-05), [[C11orf58]] (+0.64, fdr 3e-05), [[ZNF629]] (+0.64, fdr 1e-05); moves opposite to [[ELP1]] (-0.63, fdr 2e-05), [[BCKDHB]] (-0.62, fdr 3e-05), [[GMCL1]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SAMD9L]] → it (grade B ⚠); 25 go from it, the strongest it → [[SAMD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5305.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +7.7 | 8e-12 | 1/9 (J82) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.69×** | +7.4 | 4e-11 | 13/30 (SW 900, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.92×** | +6.5 | 2e-08 | 12/30 (A498, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.88×** | +6.2 | 6e-08 | 16/30 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +6.2 | 8e-08 | 3/8 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.7 | 1e-06 | 6/24 (SW1417, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +5.6 | 1e-06 | 13/28 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +5.6 | 1e-06 | 11/26 (A498, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +5.3 | 6e-06 | 11/30 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +4.5 | 3e-04 | 11/29 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.61×** | +4.4 | 6e-04 | 10/25 (NCI-H1792, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +4.4 | 6e-04 | 2/15 (J82, Panc 03.27) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +4.3 | 8e-04 | 9/29 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +4.0 | 0.003 | 10/26 (HT-29, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.72×** | +3.8 | 0.005 | 4/14 (RKO, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.005 | 4/31 (A498, NCI-H2030, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.005 | 7/27 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.007 | 3/30 (SK-MEL-2, HepG2/C3A, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.010 | 7/30 (NCI-H2347, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5305.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.259×** | -13.4 | 5e-38 | 23/30 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.268×** | -13.0 | 2e-36 | 23/30 (C32, COLO 205, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.274×** | -12.8 | 3e-35 | 24/30 (COLO 205, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.422×** | -7.6 | 4e-12 | 17/30 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.386×** | -4.9 | 1e-04 | 15/28 (AsPC-1, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.626×** | -4.6 | 3e-04 | 15/25 (COLO 205, RKO, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.760×** | -3.8 | 0.010 | 7/29 (SW1417, COLO 205, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.761×** | -3.8 | 0.010 | 8/29 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.491×** | -3.7 | 0.014 | 9/21 (AsPC-1, SNU-423, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.690×** | -3.7 | 0.014 | 8/28 (COLO 205, SNU-423, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **0.723×** | -3.2 | 0.068 | 4/30 (HCT15, NCI-H2347, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.729×** | -3.1 | 0.078 | 8/30 (KATO III, SW 900, …) | rises with dose |  |
| [[Goserelin (acetate) (drug)]] 5 µM |  | **0.800×** | -3.1 | 0.078 | 4/31 (NCI-H2347, J82, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.802×** | -3.1 | 0.086 | 11/30 (H4, NCI-H2347, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5305. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0402× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 6.61 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -10.2) |
| [[SNU-423 (line)]] | alt | 9.77 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0231× (z -16.7) |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0827× (z -10.7) |
| [[C32 (line)]] | wt | 4.23 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0290× (z -10.9) |
| [[RKO (line)]] | wt | 5.92 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0620× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 12.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -9.3) |
| [[HOP62 (line)]] | alt | 2.05 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0338× (z -9.8) |
| [[Hs 766T (line)]] | wt | 12.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0912× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 10.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0933× (z -11.1) |
| [[A-172 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.700 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.892 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.585 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.451 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.551 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5305), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF189]] | +0.68 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[C11orf58]] | +0.64 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[ZNF629]] | +0.64 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ZSCAN29]] | +0.62 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[HDX]] | +0.62 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[TLR1]] | +0.61 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[BMPR1B]] | +0.61 | +0.36 / +0.48 | both halves | 9e-05 |  |
| [[RNF6]] | +0.61 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[CASP7]] | +0.61 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[SLC9A8]] | +0.61 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[ZC3HC1]] | +0.60 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ZFY]] | +0.60 | +0.37 / +0.48 | both halves | 8e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP1]] | -0.63 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[BCKDHB]] | -0.62 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[GMCL1]] | -0.61 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TTC3]] | -0.61 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[COL18A1]] | -0.60 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[SEC63]] | -0.58 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PRRC1]] | -0.58 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[PIK3R2]] | -0.58 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[NAA35]] | -0.58 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[NT5DC3]] | -0.58 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[MMS19]] | -0.57 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ABHD12]] | -0.57 | -0.43 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD9L]] | B | SAMD9L activity raises CARD6's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.65× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[NTN4]] | B | NTN4 activity raises CARD6's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 2.23× lower at baseline in the lines without NTN4 | 0.013 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[SAMD9]] | B | SAMD9 activity raises CARD6's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.42× lower at baseline in the lines without SAMD9 | 0.025 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[ABCA1]] | B | ABCA1 activity raises CARD6's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 2.23× lower at baseline in the lines without ABCA1 | 0.034 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7 |
| [[TLR6]] | B | TLR6 activity raises CARD6's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without TLR6 | 0.046 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| [[TLR1]] | B | TLR1 activity raises CARD6's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 2.11× lower at baseline in the lines without TLR1 | 0.050 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises CARD6's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 2.28× lower at baseline in the lines without ZNF341-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity raises CARD6's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 2.10× lower at baseline in the lines without NMRAL2P-1 | 0.075 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[IFI16]] | C | IFI16 activity raises CARD6's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.70× lower at baseline in the lines without IFI16 | 5e-04 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF; co-absent with the target |
| [[RBPMS]] | C | RBPMS activity raises CARD6's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 2.20× lower at baseline in the lines without RBPMS | 0.007 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2; co-absent with the target |
| [[LINC02057]] | C | LINC02057 activity raises CARD6's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 2.41× lower at baseline in the lines without LINC02057 | 0.011 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6; co-absent with the target |
| [[KYNU]] | C | KYNU activity raises CARD6's level | lines that do not express KYNU (29) vs lines expressing it (21) | 2.44× lower at baseline in the lines without KYNU | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 21, C 4. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD1]] | B | CARD6 activity lowers SAMD1's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.70× higher at baseline in the lines without CARD6 | 0.004 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[ARMC2]] | B | CARD6 activity lowers ARMC2's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.83× higher at baseline in the lines without CARD6 | 0.007 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[SAMD9]] | B | CARD6 activity raises SAMD9's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 3.26× lower at baseline in the lines without CARD6 | 0.009 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[TTC3]] | B | CARD6 activity strengthens TTC3's drug response | lines that do not express CARD6 (17) vs lines expressing it (31) | the lines without CARD6 respond 0.64× as strongly (z diff +2.36); strongest at Ouabain (Octahydrate) 5 µM: 0.82x vs 0.61x (z diff +3.8) | 0.014 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU; target measured in part of the lines; artifact flags |
| [[SAMD9L]] | B | CARD6 activity raises SAMD9L's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 3.78× lower at baseline in the lines without CARD6 | 0.019 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[NTN4]] | B | CARD6 activity raises NTN4's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 2.57× lower at baseline in the lines without CARD6 | 0.029 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[RNASEL]] | B | CARD6 activity raises RNASEL's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.59× lower at baseline in the lines without CARD6 | 0.032 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[ZBTB40]] | B | CARD6 activity lowers ZBTB40's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.33× higher at baseline in the lines without CARD6 | 0.037 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[ZNF594]] | B | CARD6 activity lowers ZNF594's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.87× higher at baseline in the lines without CARD6 | 0.038 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[ZNF341-AS1]] | B | CARD6 activity raises ZNF341-AS1's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.62× lower at baseline in the lines without CARD6 | 0.047 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[CASP4]] | B | CARD6 activity raises CASP4's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 2.18× lower at baseline in the lines without CARD6 | 0.049 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[LINC01829]] | B | CARD6 activity raises LINC01829's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.74× lower at baseline in the lines without CARD6 | 0.052 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.586). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-2.6, 2.2); signed map (18.3, -21.9). **Vector** length 65.1, 14.2% of its response variance represented; |z| ≥ 3 in 694 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +6.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +4.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.0 | -13.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.3 | -7.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.2 | -4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -4.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.1 | -13.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.7 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -3.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.5 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | caspase recruitment domain family member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.1 — chr5:40,841,308-40,860,175 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CINCIN1 |
| Gene groups (HGNC) | Caspase recruitment domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BX69](https://www.uniprot.org/uniprotkb/Q9BX69) (Caspase recruitment domain-containing protein 6):

> May be involved in apoptosis.

**Summary**, from NCBI Gene [84674](https://www.ncbi.nlm.nih.gov/gene/84674):

> This gene encodes a protein that contains a caspase recruitment domain (CARD), an antiparallel six-helical bundle that mediates homotypic protein-protein interactions. The encoded protein is a microtubule-associated protein that has been shown to interact with receptor-interacting protein kinases and positively modulate signal transduction pathways converging on activation of the inducible transcription factor NF-kB. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16394](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16394) · Entrez [84674](https://www.ncbi.nlm.nih.gov/gene/84674) · UniProt [Q9BX69](https://www.uniprot.org/uniprotkb/Q9BX69) · Ensembl [ENSG00000132357](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132357)

## Data

Gene col 5305: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5305); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5305, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5305]; `tensor/DDL_lfc|DDL_z.npy` [5305]; `embed/gene_vectors.npy` [5305]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5305 or target_col == 5305). Every well: [[CARD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
