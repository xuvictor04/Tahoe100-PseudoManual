---
symbol: "HGF"
type: "gene"
col: 316
ensembl_id: "ENSG00000019991"
name: "hepatocyte growth factor"
location: "7q21.11"
module: 19
arm: "+"
pooled_cpm: 12.97
n_lines_expressing: 12
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 31
direction_downstream: 42
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# HGF

*hepatocyte growth factor* — 7q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.39× (z +10.2, q 7e-22, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +3.9, q 0.009, up in 0 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.528× (z -5.3, q 5e-05, down in 7 of 9 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCF4]] (+0.60, fdr 8e-06), [[PDE3A]] (+0.59, fdr 1e-05), [[RGS4]] (+0.59, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 31 arrows point to it, the strongest [[LINC03041]] → it (grade B ⚠); 42 go from it, the strongest it → [[CACNA1A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 316.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.39×** | +10.2 | 7e-22 | 2/7 (H4, SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.12×** | +9.2 | 1e-17 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +7.4 | 3e-11 | 2/5 (HS-578T, hTERT-HPNE) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.93×** | +4.7 | 3e-04 | 1/6 (HS-578T) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +4.4 | 0.001 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.009 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 1.46× | +3.2 | 0.11 | 2/8 (H4, HS-578T) | inconsistent across doses | low cells (technical?) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.66× | +3.1 | 0.15 | 0/9 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | 1.66× | +3.0 | 0.15 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 316.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.528×** | -5.3 | 5e-05 | 7/9 (CHP-212, RKO, …) | two highest doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.536×** | -5.2 | 5e-05 | 4/9 (CHP-212, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.584×** | -4.5 | 0.001 | 6/10 (CHP-212, RKO, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.607×** | -4.2 | 0.004 | 8/10 (CHP-212, RKO, …) | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.603×** | -4.1 | 0.005 | 6/9 (CHP-212, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.615×** | -3.8 | 0.016 | 0/10 | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.646×** | -3.7 | 0.019 | 3/9 (C-33 A, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.735×** | -3.6 | 0.019 | 9/9 (CHP-212, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.637×** | -3.5 | 0.030 | 0/10 | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.659×** | -3.2 | 0.072 | 0/9 | inconsistent across doses |  |
| [[Tadalafil (drug)]] 5 µM |  | **0.675×** | -3.2 | 0.081 | 0/9 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 316. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 1,688 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0870× (z -23.2) |
| [[RKO (line)]] | wt | 231 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0923× (z -22.8) |
| [[H4 (line)]] | wt | 15.6 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0630× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 28.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0908× (z -13.1) |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -8.5) |
| [[A-172 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.57 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 316), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF4]] | +0.60 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[PDE3A]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RGS4]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ADAMTSL1]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PDE4B]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SGIP1]] | +0.57 | +0.59 / +0.57 | both halves | 8e-06 |  |
| [[CDH10]] | +0.54 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[BAALC]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[GREM1]] | +0.51 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[LINC02197]] | +0.51 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[SYT4]] | +0.51 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[NETO1]] | +0.50 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 4, C 27. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03041]] | B | LINC03041 activity raises HGF's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 2.46× lower at baseline in the lines without LINC03041 | 0.031 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[RALYL]] | B | RALYL activity raises HGF's level | lines that do not express RALYL (17) vs lines expressing it (33) | 2.69× lower at baseline in the lines without RALYL | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[BNC2]] | B | BNC2 activity raises HGF's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 2.30× lower at baseline in the lines without BNC2 | 0.080 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[SOBP]] | B | SOBP activity raises HGF's level | lines that do not express SOBP (19) vs lines expressing it (31) | 2.24× lower at baseline in the lines without SOBP | 0.089 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[SGIP1]] | C | SGIP1 activity raises HGF's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 4.02× lower at baseline in the lines without SGIP1 | 0.004 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises HGF's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 4.00× lower at baseline in the lines without RIT2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[PDZRN3]] | C | PDZRN3 activity raises HGF's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 3.29× lower at baseline in the lines without PDZRN3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises HGF's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 9.61× lower at baseline in the lines without SYT4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises HGF's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 5.80× lower at baseline in the lines without NETO1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[FGF5]] | C | FGF5 activity raises HGF's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 2.94× lower at baseline in the lines without FGF5 | 0.014 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises HGF's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 3.08× lower at baseline in the lines without KCNE4 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[GAP43]] | C | GAP43 activity raises HGF's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 2.91× lower at baseline in the lines without GAP43 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 13, C 29. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1A]] | B | HGF activity raises CACNA1A's level | lines that do not express HGF (38) vs lines expressing it (12) | 2.88× lower at baseline in the lines without HGF | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| [[CACNA1A]] | B | HGF activity weakens CACNA1A's drug response | lines that do not express HGF (27) vs lines expressing it (8) | (z diff -3.79); strongest at Dinaciclib 5 µM: 2.89x vs 0.59x (z diff -6.6) | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; target measured in part of the lines; artifact flags |
| [[ADAMTSL1]] | B | HGF activity raises ADAMTSL1's level | lines that do not express HGF (38) vs lines expressing it (12) | 3.05× lower at baseline in the lines without HGF | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| [[LDB2]] | B | HGF activity raises LDB2's level | lines that do not express HGF (38) vs lines expressing it (12) | 3.53× lower at baseline in the lines without HGF | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| [[OFCC1]] | B | HGF activity raises OFCC1's level | lines that do not express HGF (38) vs lines expressing it (12) | 1.63× lower at baseline in the lines without HGF | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| [[RALYL]] | B | HGF activity raises RALYL's level | lines that do not express HGF (38) vs lines expressing it (12) | 3.16× lower at baseline in the lines without HGF | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| [[SOBP]] | B | HGF activity raises SOBP's level | lines that do not express HGF (38) vs lines expressing it (12) | 3.04× lower at baseline in the lines without HGF | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| [[EVC]] | B | HGF activity raises EVC's level | lines that do not express HGF (38) vs lines expressing it (12) | 2.68× lower at baseline in the lines without HGF | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| cells under [[Omeprazole (drug)]] 0.05 µM | B | HGF activity raises the cells' numbers under Omeprazole 0.05 µM (protects the cells) | lines that do not express HGF (38) vs lines expressing it (10) | the lines without HGF: 0.80× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | B | HGF activity lowers the cells' numbers under Vinblastine (sulfate) 5 µM (makes them more sensitive) | lines that do not express HGF (38) vs lines expressing it (10) | the lines without HGF: 1.19× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| [[LINC03041]] | B | HGF activity raises LINC03041's level | lines that do not express HGF (38) vs lines expressing it (12) | 1.84× lower at baseline in the lines without HGF | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| [[PEX5]] | B | HGF activity raises PEX5's level | lines that do not express HGF (38) vs lines expressing it (12) | 1.41× lower at baseline in the lines without HGF | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.278). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.7, 20.6); signed map (36.9, 43.6). **Vector** length 33.5, 10.3% of its response variance represented; |z| ≥ 3 in 249 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | -0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.7 | -0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.6 | -1.5 |
|  | [[Vitamin K4 (drug)]] 0.05 µM |  | +0.6 | +0.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.9 | -2.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | hepatocyte growth factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.11 — chr7:81,699,010-81,770,438 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SF, F-TCF, HGFB, HPTA; previously DFNB39 |
| Gene groups (HGNC) | Kringle domain containing |
| Hallmark sets | APOPTOSIS |
| Reactome | 31 pathways, smallest: MET activates STAT3; MET Receptor Activation; MET activates PTPN11 |
| Matched by | ensembl_id |

**Function**, from UniProt [P14210](https://www.uniprot.org/uniprotkb/P14210) (Hepatocyte growth factor):

> Potent mitogen for mature parenchymal hepatocyte cells, seems to be a hepatotrophic factor, and acts as a growth factor for a broad spectrum of tissues and cell types. Activating ligand for the receptor tyrosine kinase MET by binding to it and promoting its dimerization. Activates MAPK signaling following TMPRSS13 cleavage and activation.

**Summary**, from NCBI Gene [3082](https://www.ncbi.nlm.nih.gov/gene/3082):

> This gene encodes a protein that binds to the hepatocyte growth factor receptor to regulate cell growth, cell motility and morphogenesis in numerous cell and tissue types. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate alpha and beta chains, which form the mature heterodimer. This protein is secreted by mesenchymal cells and acts as a multi-functional cytokine on cells of mainly epithelial …

**Accessions** — [HGNC:4893](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4893) · Entrez [3082](https://www.ncbi.nlm.nih.gov/gene/3082) · UniProt [P14210](https://www.uniprot.org/uniprotkb/P14210) · Ensembl [ENSG00000019991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000019991)

## Data

Gene col 316: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 316); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 316, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 316]; `tensor/DDL_lfc|DDL_z.npy` [316]; `embed/gene_vectors.npy` [316]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 316 or target_col == 316). Every well: [[HGF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HGF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
