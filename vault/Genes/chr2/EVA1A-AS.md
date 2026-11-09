---
symbol: "EVA1A-AS"
type: "gene"
col: 13784
ensembl_id: "ENSG00000231172"
name: "EVA1A antisense RNA"
location: "2p12"
module: 34
arm: "+"
pooled_cpm: 5.0
n_lines_expressing: 28
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 13
direction_downstream: 25
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# EVA1A-AS

*EVA1A antisense RNA* — 2p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 4.26× (z +9.0, q 1e-16, up in 19 of 24 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 6.07× (z +6.3, q 5e-08, up in 13 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.398× (z -6.2, q 4e-07, down in 13 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MANCR]] (+0.64, fdr 1e-05), [[LINC02813]] (+0.58, fdr 8e-06), [[ADAM19]] (+0.57, fdr 1e-05); moves opposite to [[JMY]] (-0.48, fdr 5e-05), [[ATG2B]] (-0.45, fdr 9e-05), [[ZBTB10]] (-0.44, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[CARD11]] → it (grade B ⚠); 25 go from it, the strongest it → [[RAC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13784.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **4.26×** | +9.0 | 1e-16 | 19/24 (HOP62, A549, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.06×** | +7.2 | 2e-10 | 0/6 | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **6.07×** | +6.3 | 5e-08 | 13/16 (HOP62, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **6.02×** | +6.3 | 5e-08 | 8/14 (SW480, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **3.86×** | +4.7 | 3e-04 | 5/13 (HOP62, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.01×** | +4.6 | 3e-04 | 7/24 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **3.48×** | +4.3 | 0.001 | 7/21 (HOP62, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.96×** | +4.2 | 0.002 | 0/7 | all doses, stronger at high dose | composition shift |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.85×** | +4.1 | 0.003 | 10/25 (HOP62, SW 900, …) | inconsistent across doses | position effect removed |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.84×** | +4.1 | 0.003 | 12/25 (LS 180, SW1417, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.006 | 7/25 (HOP62, SW 1088, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **2.99×** | +3.8 | 0.006 | 4/13 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.94×** | +3.8 | 0.007 | 3/13 (HOP62, SW480, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **2.16×** | +3.7 | 0.010 | 4/23 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.67×** | +3.4 | 0.025 | 4/24 (CFPAC-1, LS 180, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **2.03×** | +3.4 | 0.026 | 6/25 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.96×** | +3.2 | 0.043 | 4/21 (LOX-IMVI, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.59×** | +3.1 | 0.061 | 6/23 (HOP62, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13784.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.398×** | -6.2 | 4e-07 | 13/18 (HOP62, SNU-423, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.808×** | -5.1 | 1e-04 | 9/26 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.516×** | -4.4 | 0.002 | 13/24 (COLO 205, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 5 µM |  | **0.649×** | -4.1 | 0.006 | 8/23 (HS-578T, LOX-IMVI, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM |  | **0.662×** | -3.9 | 0.011 | 9/25 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.674×** | -3.7 | 0.017 | 6/25 (A-172, HOP62, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.599×** | -3.4 | 0.049 | 10/25 (AsPC-1, HCT15, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.602× | -3.1 | 0.11 | 6/24 (SK-MEL-2, AsPC-1, …) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.603× | -3.1 | 0.11 | 3/24 (AsPC-1, A-172, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13784. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 38.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0311× (z -13.2) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SNU-423 (line)]] | alt | 46.1 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0718× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 8.63 | 0 | 2 (1 ⚠) | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0326× (z -8.8) |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0921× (z -9.5) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.0399× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 6.44 | 0 | 2 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0110× (z -11.0) |
| [[LS 180 (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0390× (z -14.8) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SW1417 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0837× (z -12.4) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A-172 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.869 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.929 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.815 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.941 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.845 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.701 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13784), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MANCR]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[LINC02813]] | +0.58 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[ADAM19]] | +0.57 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[LINC01705]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[EPHB6]] | +0.54 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[OTUB2]] | +0.53 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[TGFA]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ADAMTS14]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[EDNRA]] | +0.52 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[MILR1]] | +0.51 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[ADORA2B]] | +0.50 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[RABGEF1P3]] | +0.50 | +0.41 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JMY]] | -0.48 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[ATG2B]] | -0.45 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[ZBTB10]] | -0.44 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[MTURN]] | -0.44 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[DUSP22]] | -0.44 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[KRT7]] | -0.44 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[PIK3CA]] | -0.43 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[STAT5B]] | -0.43 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[CCBE1]] | -0.43 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[CHPT1]] | -0.42 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[MEAF6]] | -0.42 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[GNG10]] | -0.42 | -0.36 / -0.45 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 7, C 6. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD11]] | B | CARD11 activity raises EVA1A-AS's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.23× lower at baseline in the lines without CARD11 | 0.006 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[SHC3]] | B | SHC3 activity raises EVA1A-AS's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 1.88× lower at baseline in the lines without SHC3 | 0.044 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[EPHB6]] | B | EPHB6 activity raises EVA1A-AS's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without EPHB6 | 0.051 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38 |
| [[ARL4C]] | B | ARL4C activity raises EVA1A-AS's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 2.19× lower at baseline in the lines without ARL4C | 0.072 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |
| [[NLRP1]] | B | NLRP1 activity raises EVA1A-AS's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 1.64× lower at baseline in the lines without NLRP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[MALL]] | B | MALL activity raises EVA1A-AS's level | lines that do not express MALL (21) vs lines expressing it (29) | 1.61× lower at baseline in the lines without MALL | 0.094 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[KRT7]] | B | KRT7 activity raises EVA1A-AS's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 1.25× lower at baseline in the lines without KRT7 | 0.099 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[LINC01705]] | C | LINC01705 activity raises EVA1A-AS's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 1.62× lower at baseline in the lines without LINC01705 | 0.032 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137; co-absent with the target |
| [[EDNRA]] | C | EDNRA activity raises EVA1A-AS's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 1.67× lower at baseline in the lines without EDNRA | 0.033 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |
| [[EVA1A]] | C | EVA1A activity raises EVA1A-AS's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.05× lower at baseline in the lines without EVA1A | 0.051 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2; co-absent with the target |
| [[STRA6]] | C | STRA6 activity raises EVA1A-AS's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 1.60× lower at baseline in the lines without STRA6 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3; co-absent with the target |
| [[CEMIP]] | C | CEMIP activity raises EVA1A-AS's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.33× lower at baseline in the lines without CEMIP | 0.080 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 19, C 6. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAC2]] | B | EVA1A-AS activity raises RAC2's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 3.37× lower at baseline in the lines without EVA1A-AS | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[ARL4C]] | B | EVA1A-AS activity raises ARL4C's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 2.29× lower at baseline in the lines without EVA1A-AS | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[SHB]] | B | EVA1A-AS activity raises SHB's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 1.75× lower at baseline in the lines without EVA1A-AS | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[PLAUR]] | B | EVA1A-AS activity raises PLAUR's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 2.79× lower at baseline in the lines without EVA1A-AS | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[SHC3]] | B | EVA1A-AS activity raises SHC3's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 2.37× lower at baseline in the lines without EVA1A-AS | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[GALNT5]] | B | EVA1A-AS activity raises GALNT5's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 2.18× lower at baseline in the lines without EVA1A-AS | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[GPR68]] | B | EVA1A-AS activity raises GPR68's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 1.81× lower at baseline in the lines without EVA1A-AS | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[CCBE1]] | B | EVA1A-AS activity raises CCBE1's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 1.78× lower at baseline in the lines without EVA1A-AS | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[DUSP22]] | B | EVA1A-AS activity lowers DUSP22's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 1.36× higher at baseline in the lines without EVA1A-AS | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[SLC25A51]] | B | EVA1A-AS activity raises SLC25A51's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 1.32× lower at baseline in the lines without EVA1A-AS | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[ADAM19]] | B | EVA1A-AS activity raises ADAM19's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 2.87× lower at baseline in the lines without EVA1A-AS | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[LASTR]] | B | EVA1A-AS activity raises LASTR's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 1.53× lower at baseline in the lines without EVA1A-AS | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.416). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.4, 8.4); signed map (11.2, 51.8). **Vector** length 61.3, 14.9% of its response variance represented; |z| ≥ 3 in 671 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +9.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.2 | +1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +6.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +4.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | EVA1A antisense RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p12 — chr2:75,524,068-75,542,706 (+) |
| Ensembl biotype | lncRNA |
| Also known as | EVA1A-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55283](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55283) · Entrez [101927884](https://www.ncbi.nlm.nih.gov/gene/101927884) · Ensembl [ENSG00000231172](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231172)

## Data

Gene col 13784: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13784); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13784, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13784]; `tensor/DDL_lfc|DDL_z.npy` [13784]; `embed/gene_vectors.npy` [13784]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13784 or target_col == 13784). Every well: [[EVA1A-AS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EVA1A-AS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
