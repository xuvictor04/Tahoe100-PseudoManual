---
symbol: "LUM"
type: "gene"
col: 6293
ensembl_id: "ENSG00000139329"
name: "lumican"
location: "12q21.33"
module: 66
arm: "+"
pooled_cpm: 2.88
n_lines_expressing: 16
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 15
direction_downstream: 16
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# LUM

*lumican* — 12q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.12× (z +12.0, q 2e-30, up in 4 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 2.06× (z +6.1, q 1e-07, up in 5 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.0707×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.136×; ⚠ cell-cycle shift, explains ~36% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (H4 0.111×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFH]] (+0.69, fdr 7e-06), [[AKR1B1]] (+0.68, fdr 1e-05), [[TNFAIP6]] (+0.64, fdr 7e-06); moves opposite to [[ABTB3]] (-0.48, fdr 5e-05), [[TRIM27]] (-0.47, fdr 4e-05), [[NLRP3]] (-0.47, fdr 3e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[THBS1]] → it (grade B ⚠); 16 go from it, the strongest it → [[THBS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6293.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.12×** | +12.0 | 2e-30 | 4/6 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.25×** | +10.9 | 3e-25 | 8/10 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.93×** | +8.8 | 3e-16 | 4/7 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.16×** | +6.5 | 2e-08 | 4/12 (hTERT-HPNE, J82, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.06×** | +6.1 | 1e-07 | 5/13 (AsPC-1, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +5.9 | 3e-07 | 8/11 (AsPC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +5.9 | 4e-07 | 9/13 (SNU-423, AsPC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.48×** | +5.4 | 5e-06 | 2/8 (AsPC-1, SNU-423) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +5.0 | 3e-05 | 2/9 (CHP-212, hTERT-HPNE) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.27×** | +5.0 | 3e-05 | 1/7 (RPMI-7951) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +4.6 | 2e-04 | 5/11 (H4, J82, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +4.5 | 4e-04 | 1/10 (J82) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.49×** | +3.9 | 0.005 | 3/9 (HS-578T, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +3.7 | 0.010 | 8/10 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.03×** | +3.5 | 0.021 | 1/5 (HS-578T) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.71×** | +3.2 | 0.045 | 6/12 (HS-578T, AsPC-1, …) | two highest doses | position effect removed |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.71×** | +3.2 | 0.046 | 0/11 | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +3.2 | 0.046 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.62×** | +3.1 | 0.049 | 6/13 (HS-578T, H4, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +3.0 | 0.064 | 2/12 (HS-578T, H4) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +2.9 | 0.082 | 6/13 (HS-578T, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6293.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.0707×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.136×; ⚠ cell-cycle shift, explains ~36% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (H4 0.111×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.555× | -3.5 | 0.22 | 1/12 (RPMI-7951) | inconsistent across doses | position effect removed |
| [[Dabrafenib (drug)]] 5 µM |  | 0.383× | -3.0 | 0.72 | 4/13 (J82, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6293. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 80.5 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0707× (z -11.8) |
| [[H4 (line)]] | wt | 27.6 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.111× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.08× (z +8.9) ⚠ position not correctable | — |
| [[RPMI-7951 (line)]] | alt | 8.84 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -9.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.176 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.220 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.187 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.237 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.233 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.196 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.806 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.183 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.234 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.708 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6293), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFH]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[AKR1B1]] | +0.68 | +0.52 / +0.66 | both halves | 1e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[TNFAIP6]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ROS1]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[POSTN]] | +0.63 | +0.43 / +0.68 | both halves | 3e-05 | pathway: HALLMARK_ANGIOGENESIS; STRING 913 |
| [[VCAM1]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 421 |
| [[MXRA8]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[OLR1]] | +0.58 | +0.46 / +0.55 | both halves | 2e-05 | pathway: HALLMARK_ANGIOGENESIS |
| [[GBP2]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.57 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[CCDC80]] | +0.57 | +0.48 / +0.65 | both halves | 2e-05 | STRING 443 |
| [[TGFB2]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS; STRING 808 |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABTB3]] | -0.48 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[TRIM27]] | -0.47 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[NLRP3]] | -0.47 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PRKAG1]] | -0.47 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[MPP3]] | -0.46 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[CORO2B]] | -0.46 | -0.54 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 1, C 14. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS1]] | B | THBS1 activity raises LUM's level | lines that do not express THBS1 (14) vs lines expressing it (36) | 2.30× lower at baseline in the lines without THBS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ETNK2, SLC35G2, ENSG00000176593 |
| [[MAN1A1]] | C | MAN1A1 activity raises LUM's level | lines that do not express MAN1A1 (20) vs lines expressing it (30) | 2.44× lower at baseline in the lines without MAN1A1 | 0.018 | ⚠ within organs, on part of the lines; also absent: BDKRB2, TMEM200A, EVA1A; co-absent with the target |
| [[C1QTNF1-AS1]] | C | C1QTNF1-AS1 activity raises LUM's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 2.64× lower at baseline in the lines without C1QTNF1-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent; co-absent with the target |
| [[THY1]] | C | THY1 activity raises LUM's level | lines that do not express THY1 (38) vs lines expressing it (12) | 4.45× lower at baseline in the lines without THY1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[ANGPT1]] | C | ANGPT1 activity raises LUM's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.62× lower at baseline in the lines without ANGPT1 | 0.040 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5; co-absent with the target |
| [[TMEM47]] | C | TMEM47 activity raises LUM's level | lines that do not express TMEM47 (27) vs lines expressing it (23) | 2.75× lower at baseline in the lines without TMEM47 | 0.042 | ⚠ within organs, on part of the lines; also absent: KCNE4, ENSG00000280241, ENSG00000225649; co-absent with the target |
| [[ROS1]] | C | ROS1 activity raises LUM's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 2.46× lower at baseline in the lines without ROS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent; co-absent with the target |
| [[MGP]] | C | MGP activity raises LUM's level | lines that do not express MGP (35) vs lines expressing it (15) | 3.62× lower at baseline in the lines without MGP | 0.050 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1; co-absent with the target |
| [[FBLN2]] | C | FBLN2 activity raises LUM's level | lines that do not express FBLN2 (25) vs lines expressing it (25) | 2.53× lower at baseline in the lines without FBLN2 | 0.060 | ⚠ within organs, on part of the lines; also absent: MME, LINC01411, TLL1; co-absent with the target |
| [[IGFBP7]] | C | IGFBP7 activity raises LUM's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 2.11× lower at baseline in the lines without IGFBP7 | 0.071 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[TNFRSF11B]] | C | TNFRSF11B activity raises LUM's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 2.81× lower at baseline in the lines without TNFRSF11B | 0.076 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |
| [[NLRP3]] | C | NLRP3 activity raises LUM's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 2.46× lower at baseline in the lines without NLRP3 | 0.077 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 4, C 12. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS1]] | B | LUM activity raises THBS1's level | lines that do not express LUM (34) vs lines expressing it (16) | 5.62× lower at baseline in the lines without LUM | 0.008 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2 |
| [[B2M]] | B | LUM activity raises B2M's level | lines that do not express LUM (34) vs lines expressing it (16) | 1.79× lower at baseline in the lines without LUM | 0.032 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2 |
| [[SLC39A1]] | B | LUM activity lowers SLC39A1's level | lines that do not express LUM (34) vs lines expressing it (16) | 1.15× higher at baseline in the lines without LUM | 0.036 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2 |
| [[TMEM123]] | B | LUM activity weakens TMEM123's drug response | lines that do not express LUM (34) vs lines expressing it (15) | the lines without LUM respond 1.59× as strongly (z diff -1.86); strongest at Homoharringtonine 5 µM: 0.43x vs 0.76x (z diff -5.6) | 0.066 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; target measured in part of the lines; artifact flags |
| [[ANGPT1]] | C | LUM activity raises ANGPT1's level | lines that do not express LUM (34) vs lines expressing it (16) | 3.89× lower at baseline in the lines without LUM | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |
| [[COL12A1]] | C | LUM activity raises COL12A1's level | lines that do not express LUM (34) vs lines expressing it (16) | 6.68× lower at baseline in the lines without LUM | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |
| [[COL1A1]] | C | LUM activity raises COL1A1's level | lines that do not express LUM (34) vs lines expressing it (16) | 8.44× lower at baseline in the lines without LUM | 0.019 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |
| [[TNFAIP6]] | C | LUM activity raises TNFAIP6's level | lines that do not express LUM (34) vs lines expressing it (16) | 2.84× lower at baseline in the lines without LUM | 0.025 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |
| [[VCAM1]] | C | LUM activity raises VCAM1's level | lines that do not express LUM (34) vs lines expressing it (16) | 2.56× lower at baseline in the lines without LUM | 0.043 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |
| [[IGFBP7]] | C | LUM activity raises IGFBP7's level | lines that do not express LUM (34) vs lines expressing it (16) | 5.58× lower at baseline in the lines without LUM | 0.059 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |
| [[PTN]] | C | LUM activity raises PTN's level | lines that do not express LUM (34) vs lines expressing it (16) | 3.45× lower at baseline in the lines without LUM | 0.061 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |
| [[THY1]] | C | LUM activity raises THY1's level | lines that do not express LUM (34) vs lines expressing it (16) | 4.29× lower at baseline in the lines without LUM | 0.076 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.7, 22.4); signed map (45.5, 21.4). **Vector** length 32.0, 8.52% of its response variance represented; |z| ≥ 3 in 266 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +10.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +5.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +1.9 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -0.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | lumican |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.33 — chr12:91,102,629-91,111,494 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLRR2D; previously LDC |
| Gene groups (HGNC) | Small leucine rich repeat proteoglycans |
| Hallmark sets | ANGIOGENESIS, APOPTOSIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 11 pathways, smallest: Keratan sulfate degradation; Keratan sulfate biosynthesis; Keratan sulfate/keratin metabolism |
| Matched by | ensembl_id |

UniProt [P51884](https://www.uniprot.org/uniprotkb/P51884) carries no function annotation.

**Summary**, from NCBI Gene [4060](https://www.ncbi.nlm.nih.gov/gene/4060):

> This gene encodes a member of the small leucine-rich proteoglycan (SLRP) family that includes decorin, biglycan, fibromodulin, keratocan, epiphycan, and osteoglycin. In these bifunctional molecules, the protein moiety binds collagen fibrils and the highly charged hydrophilic glycosaminoglycans regulate interfibrillar spacings. Lumican is the major keratan sulfate proteoglycan of the cornea but is also distributed in interstitial collagenous matrices throughout the body. Lumican may regulate …

**Accessions** — [HGNC:6724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6724) · Entrez [4060](https://www.ncbi.nlm.nih.gov/gene/4060) · UniProt [P51884](https://www.uniprot.org/uniprotkb/P51884) · Ensembl [ENSG00000139329](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139329)

## Data

Gene col 6293: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6293); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6293, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6293]; `tensor/DDL_lfc|DDL_z.npy` [6293]; `embed/gene_vectors.npy` [6293]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6293 or target_col == 6293). Every well: [[LUM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LUM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
