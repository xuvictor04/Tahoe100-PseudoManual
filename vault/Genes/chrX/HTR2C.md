---
symbol: "HTR2C"
type: "gene"
col: 7166
ensembl_id: "ENSG00000147246"
name: "5-hydroxytryptamine receptor 2C"
location: "Xq23"
module: 90
arm: "+"
pooled_cpm: 2.31
n_lines_expressing: 28
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# HTR2C

*5-hydroxytryptamine receptor 2C* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.28× (z +19.0, q 0e+00, up in 5 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Irinotecan (hydrochloride) (drug)]] 5 µM: 0.601× (z -3.8, q 0.094, down in 0 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (SW480 0.111×, LOX-IMVI 0.166×; ⚠ cell-cycle shift, explains ~61% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.272×, A-172 0.340×); [[Auranofin (drug)]] 5 µM in 1 line (A-172 0.0757×); [[Panobinostat (drug)]] 5 µM in 1 line (LOX-IMVI 0.115×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLCO6A1]] (+0.66, fdr 5e-05), [[KIF6]] (+0.63, fdr 1e-05), [[ZFPM2]] (+0.61, fdr 3e-05).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC25A24P1]] → it (grade B ⚠); 9 go from it, the strongest it → [[KIF6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7166.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.28×** | +19.0 | 0e+00 | 5/12 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.86×** | +13.0 | 2e-36 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.71×** | +12.5 | 1e-33 | 1/6 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.14×** | +10.6 | 3e-24 | 1/4 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +9.1 | 1e-17 | 8/18 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.34×** | +6.9 | 7e-10 | 7/17 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.71×** | +6.1 | 7e-08 | 4/22 (LOX-IMVI, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.47×** | +5.2 | 1e-05 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +4.8 | 9e-05 | 7/21 (KATO III, CHP-212, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.15×** | +4.4 | 6e-04 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.03×** | +4.1 | 0.002 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.1 | 0.002 | 1/8 (NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +4.0 | 0.002 | 1/9 (NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +3.9 | 0.004 | 6/12 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.8 | 0.005 | 1/5 (A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.58×** | +3.7 | 0.008 | 2/17 (KATO III, A-172) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +3.7 | 0.008 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.048 | 0/9 | top dose only |  |
| [[Valdecoxib (drug)]] 0.05 µM |  | **1.46×** | +3.1 | 0.060 | 1/10 (SK-MEL-2) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.68×** | +3.0 | 0.069 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7166.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (SW480 0.111×, LOX-IMVI 0.166×; ⚠ cell-cycle shift, explains ~61% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.272×, A-172 0.340×); [[Auranofin (drug)]] 5 µM in 1 line (A-172 0.0757×); [[Panobinostat (drug)]] 5 µM in 1 line (LOX-IMVI 0.115×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.601×** | -3.8 | 0.094 | 0/18 | rises with dose | plate-row cell shift |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.652× | -3.2 | 0.28 | 0/23 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.679× | -3.1 | 0.28 | 7/20 (LOX-IMVI, KATO III, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.769× | -3.0 | 0.28 | 5/21 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.690× | -3.0 | 0.28 | 1/18 (NCI-H460) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7166. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 19.4 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0814× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.115× (z -10.4) |
| [[A-172 (line)]] | wt | 21.2 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0757× (z -14.6) |
| [[SW480 (line)]] | alt | 4.85 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0948× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 0.901 | 0 | 1 | — | [[Radotinib (drug)]] 5 µM 0.0800× (z -8.8) |
| [[A-427 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.838 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.585 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.631 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.601 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.599 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.818 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.616 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.582 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.706 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.835 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.743 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.728 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.581 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.565 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7166), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLCO6A1]] | +0.66 | +0.77 / +0.40 | both halves | 5e-05 |  |
| [[KIF6]] | +0.63 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[ZFPM2]] | +0.61 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[LINC01414]] | +0.61 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[GRM7]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 | pathway: GPCR ligand binding |
| [[FBXO38-DT]] | +0.58 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[ELAPOR2]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[GABRG2]] | +0.57 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[LINC00491]] | +0.57 | +0.75 / +0.21 | both halves | 6e-04 |  |
| [[LINC01807]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[LINC01905]] | +0.57 | +0.62 / +0.34 | both halves | 1e-04 |  |
| [[LINC01605]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A24P1]] | B | SLC25A24P1 activity raises HTR2C's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 1.80× lower at baseline in the lines without SLC25A24P1 | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2 |
| [[LINC01605]] | B | LINC01605 activity raises HTR2C's level | lines that do not express LINC01605 (27) vs lines expressing it (23) | 1.67× lower at baseline in the lines without LINC01605 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC00460, LINC01133, PTPRR |
| [[MIR4500HG]] | B | MIR4500HG activity raises HTR2C's level | lines that do not express MIR4500HG (29) vs lines expressing it (21) | 1.48× lower at baseline in the lines without MIR4500HG | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000272046, BMP5, SNCA |
| [[NETO1]] | B | NETO1 activity raises HTR2C's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 2.16× lower at baseline in the lines without NETO1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4 |
| [[LINC01611]] | C | LINC01611 activity raises HTR2C's level | lines that do not express LINC01611 (34) vs lines expressing it (16) | 2.36× lower at baseline in the lines without LINC01611 | 0.078 | ⚠ within organs, on part of the lines; also absent: CDH13, ENSG00000248973, LINC02377; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF6]] | B | HTR2C activity raises KIF6's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 1.65× lower at baseline in the lines without HTR2C | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent |
| [[NPAS3]] | B | HTR2C activity raises NPAS3's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 3.10× lower at baseline in the lines without HTR2C | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent |
| [[FAM13C]] | B | HTR2C activity raises FAM13C's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 1.83× lower at baseline in the lines without HTR2C | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent |
| [[CACNA1E]] | B | HTR2C activity raises CACNA1E's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 1.20× lower at baseline in the lines without HTR2C | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent |
| [[GALNTL6]] | B | HTR2C activity raises GALNTL6's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 1.58× lower at baseline in the lines without HTR2C | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent |
| [[MIR325HG]] | B | HTR2C activity raises MIR325HG's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 1.54× lower at baseline in the lines without HTR2C | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent |
| [[CNTNAP2]] | B | HTR2C activity raises CNTNAP2's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 1.99× lower at baseline in the lines without HTR2C | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent |
| [[MIR2052HG]] | C | HTR2C activity raises MIR2052HG's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 2.28× lower at baseline in the lines without HTR2C | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent; co-absent with the target |
| [[GABRG2]] | C | HTR2C activity raises GABRG2's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 2.04× lower at baseline in the lines without HTR2C | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.525). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.7, 26.9); signed map (35.7, 14.0). **Vector** length 31.1, 5.53% of its response variance represented; |z| ≥ 3 in 483 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +13.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +19.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.9 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.8 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.9 | -3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -0.8 | -2.9 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -0.6 | -0.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.6 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.6 | -0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -3.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -1.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | 5-hydroxytryptamine receptor 2C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq23 — chrX:114,584,078-114,910,061 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 5-HT2C, 5HTR2C; previously HTR1C |
| Gene groups (HGNC) | 5-hydroxytryptamine receptors, G protein-coupled; MicroRNA protein coding host genes; Small nucleolar RNA protein coding host genes |
| Reactome | 7 pathways, smallest: Serotonin receptors; Amine ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P28335](https://www.uniprot.org/uniprotkb/P28335) (5-hydroxytryptamine receptor 2C):

> G protein-coupled receptor for 5-hydroxytryptamine (serotonin). Also functions as a receptor for various drugs and psychoactive substances, including ergot alkaloid derivatives, 1-2,5,-dimethoxy-4-iodophenyl-2-aminopropane (DOI) and lysergic acid diethylamide (LSD). Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors. HTR2C is coupled to G(q)/G(11) G alpha proteins and …

**Summary**, from NCBI Gene [3358](https://www.ncbi.nlm.nih.gov/gene/3358):

> This gene encodes a seven-transmembrane G-protein-coupled receptor. The encoded protein responds to signaling through the neurotransmitter serotonin. The mRNA of this gene is subject to multiple RNA editing events, where adenosine residues encoded by the genome are converted to inosines. RNA editing is predicted to alter the structure of the second intracellular loop, thereby generating alternate protein forms with decreased ability to interact with G proteins. Abnormalities in RNA editing of …

**Accessions** — [HGNC:5295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5295) · Entrez [3358](https://www.ncbi.nlm.nih.gov/gene/3358) · UniProt [P28335](https://www.uniprot.org/uniprotkb/P28335) · Ensembl [ENSG00000147246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147246)

## Data

Gene col 7166: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7166); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7166, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7166]; `tensor/DDL_lfc|DDL_z.npy` [7166]; `embed/gene_vectors.npy` [7166]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7166 or target_col == 7166). Every well: [[HTR2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HTR2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
