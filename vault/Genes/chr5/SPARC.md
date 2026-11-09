---
symbol: "SPARC"
type: "gene"
col: 3433
ensembl_id: "ENSG00000113140"
name: "secreted protein acidic and cysteine rich"
location: "5q33.1"
module: 66
arm: "+"
pooled_cpm: 307.81
n_lines_expressing: 16
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 24
direction_downstream: 30
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# SPARC

*secreted protein acidic and cysteine rich* — 5q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.17× (z +13.0, q 5e-36, up in 13 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +6.5, q 9e-09, up in 7 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.545× (z -6.6, q 2e-08, down in 14 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL1A2]] (+0.80, fdr 7e-06), [[MMP2]] (+0.78, fdr 7e-06), [[COL3A1]] (+0.77, fdr 7e-06); moves opposite to [[MRPL58]] (-0.48, fdr 3e-05), [[TATDN1]] (-0.47, fdr 1e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[CREB3L1]] → it (grade B ⚠); 30 go from it, the strongest it → [[CREB3L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3433.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.17×** | +13.0 | 5e-36 | 13/15 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.25×** | +12.3 | 2e-32 | 13/13 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.66×** | +9.3 | 3e-18 | 11/13 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +6.5 | 9e-09 | 7/15 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +5.6 | 3e-06 | 9/16 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.99×** | +5.3 | 9e-06 | 8/14 (LOX-IMVI, C32, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.79×** | +4.1 | 0.003 | 7/11 (HS-578T, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.5 | 0.034 | 4/13 (SNU-423, NCI-H661, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.54×** | +3.4 | 0.050 | 0/14 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.10×** | +3.3 | 0.059 | 1/14 (LOX-IMVI) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3433.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.545×** | -6.6 | 2e-08 | 14/14 (RPMI-7951, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.432×** | -6.5 | 3e-08 | 14/14 (RPMI-7951, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.526×** | -4.8 | 4e-04 | 9/14 (hTERT-HPNE, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.556×** | -4.2 | 0.004 | 11/14 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.604×** | -3.9 | 0.011 | 14/14 (H4, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.633× | -3.3 | 0.11 | 0/14 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3433. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 301 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.2) |
| [[HOP62 (line)]] | alt | 653 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -13.3) |
| [[C32 (line)]] | wt | 295 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.20× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -14.1) |
| [[HS-578T (line)]] | alt | 2,254 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 1,014 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -15.5) |
| [[A498 (line)]] | wt | 904 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 1,318 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -21.9) |
| [[SK-MEL-2 (line)]] | alt | 498 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -13.7) |
| [[SNU-423 (line)]] | alt | 1,262 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -12.1) |
| [[SW 1088 (line)]] | alt | 1,280 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -13.4) |
| [[A-172 (line)]] | wt | 4,101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -8.5) |
| [[A-427 (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 14.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 47.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 381 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 18.8 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 27.7 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 63.4 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 54.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 15.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 175 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 50.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 17.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 29.6 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 18.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 19.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 22.1 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 53.9 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 20.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 15.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3433), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL1A2]] | +0.80 | +0.80 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 959 |
| [[MMP2]] | +0.78 | +0.77 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION; STRING 701 |
| [[COL3A1]] | +0.77 | +0.77 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 911 |
| [[NID2]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 445 |
| [[THY1]] | +0.73 | +0.64 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 545 |
| [[COL1A1]] | +0.71 | +0.64 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 968 |
| [[ECM1]] | +0.71 | +0.73 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[DKK3]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[P3H3]] | +0.67 | +0.61 / +0.57 | both halves | 9e-06 | pathway: Extracellular matrix organization |
| [[RPN2]] | +0.65 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[PDIA3]] | +0.61 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[FKBP7]] | +0.60 | +0.63 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL58]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[TATDN1]] | -0.47 | -0.48 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 2, C 22. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREB3L1]] | B | CREB3L1 activity raises SPARC's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 2.29× lower at baseline in the lines without CREB3L1 | 0.012 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[LDOC1]] | B | LDOC1 activity raises SPARC's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 3.81× lower at baseline in the lines without LDOC1 | 0.071 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91 |
| [[ITGA4]] | C | ITGA4 activity raises SPARC's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 22.21× lower at baseline in the lines without ITGA4 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[MMP2]] | C | MMP2 activity raises SPARC's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 18.09× lower at baseline in the lines without MMP2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises SPARC's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 13.28× lower at baseline in the lines without PDGFRB | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises SPARC's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 7.74× lower at baseline in the lines without COL1A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[TIMP3]] | C | TIMP3 activity raises SPARC's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 10.56× lower at baseline in the lines without TIMP3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises SPARC's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 6.35× lower at baseline in the lines without FBN1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[SDC2]] | C | SDC2 activity raises SPARC's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 6.42× lower at baseline in the lines without SDC2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH; co-absent with the target |
| [[POSTN]] | C | POSTN activity raises SPARC's level | lines that do not express POSTN (38) vs lines expressing it (12) | 10.14× lower at baseline in the lines without POSTN | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[LAYN]] | C | LAYN activity raises SPARC's level | lines that do not express LAYN (31) vs lines expressing it (19) | 6.98× lower at baseline in the lines without LAYN | 0.013 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises SPARC's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 7.73× lower at baseline in the lines without DKK3 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 7, C 23. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREB3L1]] | B | SPARC activity raises CREB3L1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 2.17× lower at baseline in the lines without SPARC | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032 |
| [[SMPD1]] | B | SPARC activity raises SMPD1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without SPARC | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032 |
| [[FKBP7]] | B | SPARC activity raises FKBP7's level | lines that do not express SPARC (34) vs lines expressing it (16) | 2.13× lower at baseline in the lines without SPARC | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032 |
| [[P3H1]] | B | SPARC activity raises P3H1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 2.37× lower at baseline in the lines without SPARC | 0.065 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032 |
| [[PLOD1]] | B | SPARC activity raises PLOD1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 2.16× lower at baseline in the lines without SPARC | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032 |
| [[GXYLT2]] | B | SPARC activity raises GXYLT2's level | lines that do not express SPARC (34) vs lines expressing it (16) | 3.36× lower at baseline in the lines without SPARC | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032 |
| [[CALU]] | B | SPARC activity raises CALU's level | lines that do not express SPARC (34) vs lines expressing it (16) | 1.65× lower at baseline in the lines without SPARC | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032 |
| [[PDGFRB]] | C | SPARC activity raises PDGFRB's level | lines that do not express SPARC (34) vs lines expressing it (16) | 8.14× lower at baseline in the lines without SPARC | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[LAYN]] | C | SPARC activity raises LAYN's level | lines that do not express SPARC (34) vs lines expressing it (16) | 5.09× lower at baseline in the lines without SPARC | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[COL6A1]] | C | SPARC activity raises COL6A1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 6.87× lower at baseline in the lines without SPARC | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[COL1A1]] | C | SPARC activity raises COL1A1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 8.24× lower at baseline in the lines without SPARC | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[COL1A2]] | C | SPARC activity raises COL1A2's level | lines that do not express SPARC (34) vs lines expressing it (16) | 10.56× lower at baseline in the lines without SPARC | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.517). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (56.1, 22.3); signed map (25.5, 42.6). **Vector** length 60.3, 23.1% of its response variance represented; |z| ≥ 3 in 343 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Integrin cell surface interactions* (reactome, mean cos +0.56 to 10); *Assembly of collagen fibrils and other multimeric structures* (reactome, mean cos +0.56 to 8); *Fibronectin matrix formation* (reactome, mean cos +0.62 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +12.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +13.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -1.1 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -6.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | +0.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | secreted protein acidic and cysteine rich |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.1 — chr5:151,661,096-151,686,975 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ONT, BM-40; previously ON |
| Gene groups (HGNC) | SPARC family; Secretory calcium-binding phosphoprotein family |
| Hallmark sets | COAGULATION, MYOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 11 pathways, smallest: Nuclear signaling by ERBB4; Binding and Uptake of Ligands by Scavenger Receptors; Signaling by ERBB4 |
| Matched by | ensembl_id |

**Function**, from UniProt [P09486](https://www.uniprot.org/uniprotkb/P09486) (SPARC):

> Appears to regulate cell growth through interactions with the extracellular matrix and cytokines. Binds calcium and copper, several types of collagen, albumin, thrombospondin, PDGF and cell membranes. There are two calcium binding sites; an acidic domain that binds 5 to 8 Ca(2+) with a low affinity and an EF-hand loop that binds a Ca(2+) ion with a high affinity.

**Summary**, from NCBI Gene [6678](https://www.ncbi.nlm.nih.gov/gene/6678):

> This gene encodes a cysteine-rich acidic matrix-associated protein. The encoded protein is required for the collagen in bone to become calcified but is also involved in extracellular matrix synthesis and promotion of changes to cell shape. The gene product has been associated with tumor suppression but has also been correlated with metastasis based on changes to cell shape which can promote tumor cell invasion. Three transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:11219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11219) · Entrez [6678](https://www.ncbi.nlm.nih.gov/gene/6678) · UniProt [P09486](https://www.uniprot.org/uniprotkb/P09486) · Ensembl [ENSG00000113140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113140)

## Data

Gene col 3433: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3433); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3433, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3433]; `tensor/DDL_lfc|DDL_z.npy` [3433]; `embed/gene_vectors.npy` [3433]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3433 or target_col == 3433). Every well: [[SPARC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPARC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
