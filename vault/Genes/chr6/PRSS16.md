---
symbol: "PRSS16"
type: "gene"
col: 3409
ensembl_id: "ENSG00000112812"
name: "serine protease 16"
location: "6p22.1"
module: 8
arm: "+"
pooled_cpm: 2.82
n_lines_expressing: 37
n_dd_up: 8
n_dd_down: 26
n_dd_up_clean: 3
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 12
direction_downstream: 4
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PRSS16

*serine protease 16* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.10× (z +7.4, q 1e-10, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.76× (z +4.2, q 0.004, up in 2 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.285× (z -12.9, q 4e-35, down in 27 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDT7]] (+0.59, fdr 3e-05), [[VWA5A]] (+0.58, fdr 2e-05), [[EPHX2]] (+0.58, fdr 1e-05); moves opposite to [[PRDM15]] (-0.53, fdr 5e-05), [[WNT5B]] (-0.49, fdr 4e-05), [[EHMT1]] (-0.48, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[CLDN3]] → it (grade B ⚠); 4 go from it, the strongest it → [[NOXA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +7.4 | 1e-10 | 1/5 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +5.7 | 4e-06 | 8/16 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.8 | 3e-04 | 4/13 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +4.2 | 0.004 | 2/14 (LoVo, A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.32×** | +4.1 | 0.006 | 5/33 (LoVo, RKO, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +3.6 | 0.035 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.040 | 6/34 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.046 | 3/27 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.35× | +3.2 | 0.10 | 4/31 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.11 | 1/33 (RKO) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3409.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.285×** | -12.9 | 4e-35 | 27/33 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.292×** | -12.6 | 4e-34 | 25/28 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.300×** | -12.3 | 9e-33 | 24/31 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.416×** | -9.0 | 4e-17 | 19/21 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.218×** | -8.2 | 4e-14 | 24/31 (LoVo, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.475×** | -7.6 | 2e-12 | 15/33 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.546×** | -6.2 | 5e-08 | 16/33 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.551×** | -6.1 | 8e-08 | 16/26 (HCT15, HOP62, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -5.9 | 2e-07 | 15/25 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.583×** | -5.5 | 2e-06 | 13/32 (KATO III, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.684×** | -5.5 | 2e-06 | 15/26 (KATO III, NCI-H2030, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.601×** | -5.2 | 1e-05 | 11/28 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.384×** | -5.1 | 1e-05 | 12/22 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.881× | -4.3 | 7e-04 | 14/34 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.745×** | -4.2 | 9e-04 | 14/32 (NCI-H2030, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.694×** | -3.7 | 0.007 | 9/32 (NCI-H460, A-172, …) | two highest doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.508×** | -3.6 | 0.010 | 7/25 (PANC-1, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.713×** | -3.4 | 0.017 | 8/23 (HT-29, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 8.58 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -13.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.116× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 7.40 | 0 | 4 (2 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0720× (z -12.8) ⚠ toxic · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.203× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 5.94 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0322× (z -12.4) |
| [[PANC-1 (line)]] | alt | 2.37 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0250× (z -12.5) |
| [[SW480 (line)]] | alt | 3.69 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0623× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.134× (z -9.3) |
| [[LoVo (line)]] | wt | 5.10 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -10.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 3.02 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0161× (z -12.1) |
| [[A498 (line)]] | wt | 2.73 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0823× (z -9.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 5.66 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.129× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 5.73 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0543× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 3.87 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0796× (z -8.8) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 4.63 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.151× (z -9.0) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.739 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.221 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.295 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.195 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.216 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT7]] | +0.59 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[VWA5A]] | +0.58 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[EPHX2]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ENPP4]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ACBD4]] | +0.57 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[KCNK15-AS1]] | +0.57 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ESRP1]] | +0.56 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[GSTM4]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[AP1G2]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[GALM]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[CAPN5]] | +0.54 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[PREPL]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM15]] | -0.53 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[WNT5B]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[EHMT1]] | -0.48 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[CCM2]] | -0.48 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ARPC5L]] | -0.48 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[IQCJ-SCHIP1]] | -0.48 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[IGF2BP3]] | -0.48 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[C1orf159]] | -0.47 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[ST3GAL3]] | -0.47 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[MSANTD2]] | -0.47 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[TIMM23B-AGAP6]] | -0.47 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[HIRA]] | -0.47 | -0.46 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN3]] | B | CLDN3 activity raises PRSS16's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.24× lower at baseline in the lines without CLDN3 | 0.016 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[EPHA10]] | B | EPHA10 activity raises PRSS16's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 2.18× lower at baseline in the lines without EPHA10 | 0.022 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[RDM1P5]] | B | RDM1P5 activity raises PRSS16's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.83× lower at baseline in the lines without RDM1P5 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[TMEM125]] | B | TMEM125 activity raises PRSS16's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 2.02× lower at baseline in the lines without TMEM125 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[TJP3]] | B | TJP3 activity raises PRSS16's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.00× lower at baseline in the lines without TJP3 | 0.034 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[KIAA1522]] | B | KIAA1522 activity raises PRSS16's level | lines that do not express KIAA1522 (5) vs lines expressing it (45) | 2.47× lower at baseline in the lines without KIAA1522 | 0.043 | ⚠ across organs; also absent: ENSG00000257489, TRIB3, PBX4 |
| [[SMPDL3B]] | B | SMPDL3B activity raises PRSS16's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without SMPDL3B | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[ESRP1]] | B | ESRP1 activity raises PRSS16's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 2.01× lower at baseline in the lines without ESRP1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[TMC4]] | B | TMC4 activity raises PRSS16's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 1.99× lower at baseline in the lines without TMC4 | 0.062 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[ENPP5]] | B | ENPP5 activity raises PRSS16's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.46× lower at baseline in the lines without ENPP5 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[PLXNA2]] | B | PLXNA2 activity lowers PRSS16's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.46× higher at baseline in the lines without PLXNA2 | 0.084 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[TESMIN]] | B | TESMIN activity raises PRSS16's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 2.18× lower at baseline in the lines without TESMIN | 0.085 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOXA1]] | B | PRSS16 activity raises NOXA1's level | lines that do not express PRSS16 (13) vs lines expressing it (37) | 2.13× lower at baseline in the lines without PRSS16 | 0.060 | ⚠ within organs, on part of the lines; also absent: STXBP2, MAP3K21, LINC00857 |
| [[TESMIN]] | B | PRSS16 activity raises TESMIN's level | lines that do not express PRSS16 (13) vs lines expressing it (37) | 2.33× lower at baseline in the lines without PRSS16 | 0.060 | ⚠ within organs, on part of the lines; also absent: STXBP2, MAP3K21, LINC00857 |
| [[EPHA10]] | B | PRSS16 activity raises EPHA10's level | lines that do not express PRSS16 (13) vs lines expressing it (37) | 2.30× lower at baseline in the lines without PRSS16 | 0.088 | ⚠ within organs, on part of the lines; also absent: STXBP2, MAP3K21, LINC00857 |
| [[PLXNA2]] | B | PRSS16 activity lowers PLXNA2's level | lines that do not express PRSS16 (13) vs lines expressing it (37) | 1.68× higher at baseline in the lines without PRSS16 | 0.095 | ⚠ within organs, on part of the lines; also absent: STXBP2, MAP3K21, LINC00857 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.455). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.6, 32.7); signed map (-4.6, 17.1). **Vector** length 48.4, 7.67% of its response variance represented; |z| ≥ 3 in 866 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +7.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +2.1 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +2.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -12.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -12.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -12.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | serine protease 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:27,247,701-27,256,624 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSSP |
| Gene groups (HGNC) | Serine proteases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQE7](https://www.uniprot.org/uniprotkb/Q9NQE7) (Thymus-specific serine protease):

> Protease that may play a role in T-cell development.

**Summary**, from NCBI Gene [10279](https://www.ncbi.nlm.nih.gov/gene/10279):

> This gene encodes a serine protease expressed exclusively in the thymus. It is thought to play a role in the alternative antigen presenting pathway used by cortical thymic epithelial cells during the positive selection of T cells. The gene is found in the large histone gene cluster on chromosome 6, near the major histocompatibility complex (MHC) class I region. A second transcript variant has been described, but its full length nature has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9480) · Entrez [10279](https://www.ncbi.nlm.nih.gov/gene/10279) · UniProt [Q9NQE7](https://www.uniprot.org/uniprotkb/Q9NQE7) · Ensembl [ENSG00000112812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112812)

## Data

Gene col 3409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3409); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3409]; `tensor/DDL_lfc|DDL_z.npy` [3409]; `embed/gene_vectors.npy` [3409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3409 or target_col == 3409). Every well: [[PRSS16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRSS16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
