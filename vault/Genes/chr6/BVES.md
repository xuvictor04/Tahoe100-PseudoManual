---
symbol: "BVES"
type: "gene"
col: 3345
ensembl_id: "ENSG00000112276"
name: "popeye domain cAMP effector 1"
location: "6q21"
module: 82
arm: "+"
pooled_cpm: 5.3
n_lines_expressing: 31
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 10
direction_downstream: 14
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# BVES

*popeye domain cAMP effector 1* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.45× (z +6.3, q 2e-07, up in 12 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.395× (z -15.8, q 0e+00, down in 19 of 26 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.407× (z -5.6, q 3e-06, down in 11 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SVIL-AS1-1]] (+0.58, fdr 1e-05), [[RAB23]] (+0.56, fdr 1e-05), [[BVES-AS1]] (+0.56, fdr 2e-05, ⚠ same locus), [[UBE2Q2P1]] (+0.55, fdr 1e-05); moves opposite to [[ASXL1]] (-0.48, fdr 4e-05), [[FAAH2]] (-0.47, fdr 4e-05), [[RAD51B]] (-0.45, fdr 1e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LOXL1]] → it (grade B ⚠); 14 go from it, the strongest it → [[SMIM13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3345.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +6.3 | 2e-07 | 12/28 (NCI-H2347, NCI-H2030, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.39×** | +5.6 | 5e-06 | 6/27 (J82, LOX-IMVI, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +5.3 | 2e-05 | 10/25 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.6 | 6e-04 | 3/14 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.47×** | +4.5 | 1e-03 | 9/25 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.013 | 8/29 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.014 | 2/27 (RPMI-7951, SK-MEL-2) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.5 | 0.035 | 8/20 (hTERT-HPNE, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.037 | 7/27 (HS-578T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.042 | 6/28 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.042 | 9/26 (HOP62, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.056 | 5/29 (A549, SW 900, …) | rises with dose |  |
| [[Erlotinib (drug)]] 5 µM |  | 1.30× | +3.0 | 0.12 | 2/26 (NCI-H1792, SK-MEL-2) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3345.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.395×** | -15.8 | 0e+00 | 19/26 (NCI-H460, A549, …) | top dose only | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.493×** | -8.2 | 9e-14 | 14/25 (NCI-H460, A549, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.407×** | -5.6 | 3e-06 | 11/24 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.476×** | -4.7 | 5e-04 | 14/25 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.712×** | -4.1 | 0.005 | 10/28 (NCI-H2030, J82, …) | rises with dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.730×** | -3.8 | 0.015 | 9/28 (RPMI-7951, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.742×** | -3.6 | 0.026 | 6/26 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.751×** | -3.4 | 0.041 | 11/24 (NCI-H2030, NCI-H1792, …) | rises with dose |  |
| [[Trimetrexate (drug)]] 5 µM |  | **0.824×** | -3.3 | 0.059 | 7/26 (H4, SHP-77, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.772× | -3.1 | 0.10 | 8/25 (H4, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3345. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.54 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -11.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 12.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -11.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -11.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 9.53 | 0 | 2 (1 ⚠) | — | [[Omeprazole (drug)]] 0.5 µM 0.0938× (z -11.6) |
| [[SNU-423 (line)]] | alt | 3.84 | 0 | 2 | — | [[Rifaximin (drug)]] 5 µM 0.0652× (z -9.1) |
| [[A-172 (line)]] | wt | 4.55 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 19.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0654× (z -12.5) |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0906× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 4.69 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -8.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 6.19 | 0 | 1 | — | [[Norepinephrine (hydrochloride) (drug)]] 5 µM 0.132× (z -10.2) |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.393 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.571 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.511 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3345), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SVIL-AS1-1]] | +0.58 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[RAB23]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[BVES-AS1]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[UBE2Q2P1]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SGPP1]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[FAM124A]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[NIPA1]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[LOXL1-AS1]] | +0.53 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[CDYL2]] | +0.52 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[C1orf198]] | +0.51 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[PCBP4]] | +0.51 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[RHOC]] | +0.51 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[RASSF2]] | +0.51 | +0.41 / +0.59 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASXL1]] | -0.48 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[FAAH2]] | -0.47 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[RAD51B]] | -0.45 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[NIHCOLE]] | -0.44 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[DLEU1]] | -0.44 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[ATXN7L1]] | -0.44 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[PILRB]] | -0.44 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ANKHD1]] | -0.44 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[BPTF]] | -0.44 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[HES1]] | -0.44 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[ZNF608]] | -0.44 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[C1QTNF3-AMACR]] | -0.43 | -0.30 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOXL1]] | B | LOXL1 activity raises BVES's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 2.30× lower at baseline in the lines without LOXL1 | 0.020 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[FAAH2]] | B | FAAH2 activity lowers BVES's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 3.40× higher at baseline in the lines without FAAH2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[LINC01091]] | B | LINC01091 activity lowers BVES's level | lines that do not express LINC01091 (16) vs lines expressing it (34) | 1.74× higher at baseline in the lines without LINC01091 | 0.063 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent |
| [[KATNAL1]] | B | KATNAL1 activity raises BVES's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 3.39× lower at baseline in the lines without KATNAL1 | 0.098 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[GNB4]] | C | GNB4 activity raises BVES's level | lines that do not express GNB4 (18) vs lines expressing it (32) | 4.88× lower at baseline in the lines without GNB4 | 0.008 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES, BVES-AS1; co-absent with the target |
| [[TSHZ3-AS1]] | C | TSHZ3-AS1 activity raises BVES's level | lines that do not express TSHZ3-AS1 (25) vs lines expressing it (25) | 2.95× lower at baseline in the lines without TSHZ3-AS1 | 0.041 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |
| [[RECK]] | C | RECK activity raises BVES's level | lines that do not express RECK (12) vs lines expressing it (38) | 3.59× lower at baseline in the lines without RECK | 0.046 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9; co-absent with the target |
| [[WIPF1]] | C | WIPF1 activity raises BVES's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 4.42× lower at baseline in the lines without WIPF1 | 0.049 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3; co-absent with the target |
| [[BVES-AS1]] | C | BVES-AS1 activity raises BVES's level | lines that do not express BVES-AS1 (17) vs lines expressing it (33) | 4.96× lower at baseline in the lines without BVES-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: BVES, MPDZ, MAP9; maybe low, not absent; co-absent with the target; its own permutation p |
| [[TWIST2]] | C | TWIST2 activity raises BVES's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 2.89× lower at baseline in the lines without TWIST2 | 0.090 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 9, C 5. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMIM13]] | B | BVES activity raises SMIM13's level | lines that do not express BVES (19) vs lines expressing it (31) | 1.46× lower at baseline in the lines without BVES | 0.014 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[LOXL1]] | B | BVES activity raises LOXL1's level | lines that do not express BVES (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without BVES | 0.060 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[LOXL1-AS1]] | B | BVES activity raises LOXL1-AS1's level | lines that do not express BVES (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without BVES | 0.065 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[MXRA7]] | B | BVES activity raises MXRA7's level | lines that do not express BVES (19) vs lines expressing it (31) | 2.69× lower at baseline in the lines without BVES | 0.066 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[NIHCOLE]] | B | BVES activity lowers NIHCOLE's level | lines that do not express BVES (19) vs lines expressing it (31) | 2.09× higher at baseline in the lines without BVES | 0.068 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[KATNAL1]] | B | BVES activity raises KATNAL1's level | lines that do not express BVES (19) vs lines expressing it (31) | 2.81× lower at baseline in the lines without BVES | 0.073 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[ZNF608]] | B | BVES activity raises ZNF608's level | lines that do not express BVES (19) vs lines expressing it (31) | 1.16× lower at baseline in the lines without BVES | 0.074 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[SEMA4F]] | B | BVES activity raises SEMA4F's level | lines that do not express BVES (19) vs lines expressing it (31) | 1.49× lower at baseline in the lines without BVES | 0.079 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[MYO5A]] | B | BVES activity raises MYO5A's level | lines that do not express BVES (19) vs lines expressing it (31) | 2.17× lower at baseline in the lines without BVES | 0.083 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[GNB4]] | C | BVES activity raises GNB4's level | lines that do not express BVES (19) vs lines expressing it (31) | 11.50× lower at baseline in the lines without BVES | 5e-04 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2; co-absent with the target |
| [[WIPF1]] | C | BVES activity raises WIPF1's level | lines that do not express BVES (19) vs lines expressing it (31) | 8.59× lower at baseline in the lines without BVES | 0.002 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2; co-absent with the target |
| [[BVES-AS1]] | C | BVES activity raises BVES-AS1's level | lines that do not express BVES (19) vs lines expressing it (31) | 2.40× lower at baseline in the lines without BVES | 0.040 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.370). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.9, 46.7); signed map (-8.8, 21.8). **Vector** length 49.5, 9.42% of its response variance represented; |z| ≥ 3 in 582 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.4 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.4 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.5 | -15.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.7 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.2 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.1 | -4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -3.8 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.8 | -5.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -0.4 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -0.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | popeye domain cAMP effector 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:105,096,822-105,137,157 (-) |
| Ensembl biotype | protein_coding |
| Also known as | POP1, HBVES; previously BVES |
| Gene groups (HGNC) | Popeye domain cAMP effector family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NE79](https://www.uniprot.org/uniprotkb/Q8NE79) (Popeye domain-containing protein 1):

> Cell adhesion molecule involved in the establishment and/or maintenance of cell integrity. Involved in the formation and regulation of the tight junction (TJ) paracellular permeability barrier in epithelial cells. Plays a role in VAMP3-mediated vesicular transport and recycling of different receptor molecules through its interaction with VAMP3. Plays a role in the regulation of cell shape and movement by modulating the Rho-family GTPase activity through its interaction with ARHGEF25/GEFT. …

**Summary**, from NCBI Gene [11149](https://www.ncbi.nlm.nih.gov/gene/11149):

> This gene encodes a member of the POP family of proteins containing three putative transmembrane domains. This gene is expressed in cardiac and skeletal muscle and may play an important role in development of these tissues. The mouse ortholog may be involved in the regeneration of adult skeletal muscle and may act as a cell adhesion molecule in coronary vasculogenesis. Three transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:1152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1152) · Entrez [11149](https://www.ncbi.nlm.nih.gov/gene/11149) · UniProt [Q8NE79](https://www.uniprot.org/uniprotkb/Q8NE79) · Ensembl [ENSG00000112276](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112276)

## Data

Gene col 3345: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3345); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3345, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3345]; `tensor/DDL_lfc|DDL_z.npy` [3345]; `embed/gene_vectors.npy` [3345]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3345 or target_col == 3345). Every well: [[BVES — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BVES.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
