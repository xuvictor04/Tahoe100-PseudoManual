---
symbol: "TBKBP1"
type: "gene"
col: 12746
ensembl_id: "ENSG00000198933"
name: "TBK1 binding protein 1"
location: "17q21.32"
module: 138
arm: "+"
pooled_cpm: 4.97
n_lines_expressing: 45
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# TBKBP1

*TBK1 binding protein 1* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.49× (z +4.5, q 0.003, up in 4 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 1.38× (z +3.8, q 0.023, up in 8 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.218× (z -18.0, q 0e+00, down in 38 of 42 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.468× (z -9.0, q 3e-17, down in 27 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTX3]] (+0.66, fdr 1e-05), [[MSI1]] (+0.66, fdr 1e-05), [[PRDM11]] (+0.63, fdr 4e-05); moves opposite to [[PIBF1]] (-0.62, fdr 3e-05), [[TXNDC17]] (-0.53, fdr 1e-04), [[EFHC1]] (-0.52, fdr 9e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FAXC]] → it (grade B ⚠); 3 go from it, the strongest it → [[UBE2Q2P1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12746.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.5 | 0.003 | 4/11 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.30×** | +4.4 | 0.003 | 12/42 (HOP62, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.023 | 8/36 (NCI-H460, NCI-H1792, …) | two highest doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 1.34× | +3.3 | 0.12 | 7/40 (A-172, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 1.70× | +3.3 | 0.12 | 2/20 (A-172, NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12746.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.218×** | -18.0 | 0e+00 | 38/42 (A-172, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.245×** | -16.7 | 0e+00 | 36/42 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.263×** | -15.8 | 0e+00 | 36/42 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.468×** | -9.0 | 3e-17 | 27/42 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.600×** | -5.8 | 6e-07 | 18/38 (SW 900, RKO, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.643×** | -5.0 | 4e-05 | 8/29 (SW1417, NCI-H2347, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.687×** | -4.5 | 7e-04 | 14/36 (HEC-1-A, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.507×** | -4.2 | 0.002 | 17/40 (SK-MEL-2, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.706×** | -4.1 | 0.002 | 11/40 (NCI-H661, NCI-H2030, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.710×** | -4.1 | 0.003 | 9/42 (BT-474, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.790×** | -4.0 | 0.004 | 15/42 (A-427, A549, …) | top dose only | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.558×** | -3.6 | 0.014 | 11/34 (LOX-IMVI, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.761×** | -3.2 | 0.051 | 11/41 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.764×** | -3.2 | 0.057 | 4/42 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.601×** | -3.2 | 0.060 | 10/41 (LOX-IMVI, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.60 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12746. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0924× (z -12.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 6.00 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0626× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Rosiglitazone (drug)]] 5 µM 0.0770× (z -11.2) |
| [[HS-578T (line)]] | alt | 6.64 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.101× (z -10.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LoVo (line)]] | wt | 4.83 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0659× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 3.93 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 3.84 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 3.72 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0718× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[BT-474 (line)]] | alt | 4.28 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0544× (z -8.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[C-33 A (line)]] | alt | 8.81 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0334× (z -12.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[C32 (line)]] | wt | 5.29 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0779× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HEC-1-A (line)]] | alt | 4.10 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0678× (z -11.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 7.42 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0740× (z -10.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 6.99 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0324× (z -14.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 5.71 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0815× (z -9.2) |
| [[RKO (line)]] | wt | 6.29 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0723× (z -9.1) |
| [[SHP-77 (line)]] | alt | 6.27 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0691× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 5.95 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0640× (z -9.0) |
| [[SW 900 (line)]] | alt | 7.45 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0772× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12746), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTX3]] | +0.66 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[MSI1]] | +0.66 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[PRDM11]] | +0.63 | +0.54 / +0.40 | both halves | 4e-05 |  |
| [[ZFTA]] | +0.61 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[ZNF391]] | +0.60 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[PYGO1]] | +0.60 | +0.49 / +0.37 | both halves | 9e-05 |  |
| [[SGSH]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ADAP2]] | +0.59 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[DEF8]] | +0.58 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TSSK3]] | +0.58 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[STRN4]] | +0.57 | +0.55 / +0.38 | both halves | 7e-05 |  |
| [[LRRN2]] | +0.57 | +0.46 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIBF1]] | -0.62 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[TXNDC17]] | -0.53 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[EFHC1]] | -0.52 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[LINC01572]] | -0.52 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[RTTN]] | -0.51 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[RPA3]] | -0.51 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[RASA1]] | -0.51 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[GPN3]] | -0.50 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[RAPGEF6]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[UBE2T]] | -0.50 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[MED14]] | -0.50 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[UBR7]] | -0.50 | -0.33 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAXC]] | B | FAXC activity raises TBKBP1's level | lines that do not express FAXC (11) vs lines expressing it (39) | 2.29× lower at baseline in the lines without FAXC | 0.050 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[TNK1]] | B | TNK1 activity lowers TBKBP1's level | lines that do not express TNK1 (13) vs lines expressing it (37) | 1.55× higher at baseline in the lines without TNK1 | 0.066 | ⚠ within organs, on part of the lines; also absent: TUBA4A, CDCP1, CHMP4C; maybe low, not absent |
| [[ZNF391]] | B | ZNF391 activity raises TBKBP1's level | lines that do not express ZNF391 (5) vs lines expressing it (45) | 2.37× lower at baseline in the lines without ZNF391 | 0.079 | ⚠ within organs, on part of the lines; also absent: LINC00159, ENSG00000283491, ASIC1; maybe low, not absent |
| [[PLEKHO1]] | B | PLEKHO1 activity raises TBKBP1's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without PLEKHO1 | 0.083 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[SLC4A3]] | B | SLC4A3 activity raises TBKBP1's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.72× lower at baseline in the lines without SLC4A3 | 0.096 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2Q2P1]] | B | TBKBP1 activity raises UBE2Q2P1's level | lines that do not express TBKBP1 (5) vs lines expressing it (45) | 3.26× lower at baseline in the lines without TBKBP1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CSRP2, PHC1, DNAJC18; its own permutation p |
| [[UBE2Q2P1-1]] | B | TBKBP1 activity raises UBE2Q2P1-1's level | lines that do not express TBKBP1 (5) vs lines expressing it (45) | 2.35× lower at baseline in the lines without TBKBP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CSRP2, PHC1, DNAJC18; its own permutation p |
| [[C7orf31]] | C | TBKBP1 activity raises C7orf31's level | lines that do not express TBKBP1 (5) vs lines expressing it (45) | 3.42× lower at baseline in the lines without TBKBP1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CSRP2, PHC1, DNAJC18; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.496). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.9, 8.4); signed map (15.2, -13.3). **Vector** length 63.0, 9.59% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.2 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.0 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +2.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.1 | -16.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.9 | -15.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.9 | -18.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -2.1 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | -2.1 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -4.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.6 | -2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | TBK1 binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:47,694,161-47,712,052 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ProSAPiP2, KIAA0775 |
| Gene groups (HGNC) | Zinc fingers UBZ1 CCHH-type |
| Matched by | ensembl_id |

**Function**, from UniProt [A7MCY6](https://www.uniprot.org/uniprotkb/A7MCY6) (TANK-binding kinase 1-binding protein 1):

> Adapter protein which constitutively binds TBK1 and IKBKE playing a role in antiviral innate immunity.

**Summary**, from NCBI Gene [9755](https://www.ncbi.nlm.nih.gov/gene/9755):

> TBKBP1 is an adaptor protein that binds to TBK1 (MIM 604834) and is part of the interaction network in the TNF (MIM 191160)/NFKB (see MIM 164011) pathway (Bouwmeester et al., 2004 [PubMed 14743216]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:30140](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30140) · Entrez [9755](https://www.ncbi.nlm.nih.gov/gene/9755) · UniProt [A7MCY6](https://www.uniprot.org/uniprotkb/A7MCY6) · Ensembl [ENSG00000198933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198933)

## Data

Gene col 12746: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12746); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12746, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12746]; `tensor/DDL_lfc|DDL_z.npy` [12746]; `embed/gene_vectors.npy` [12746]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12746 or target_col == 12746). Every well: [[TBKBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBKBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
