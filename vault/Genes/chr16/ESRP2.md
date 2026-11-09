---
symbol: "ESRP2"
type: "gene"
col: 2317
ensembl_id: "ENSG00000103067"
name: "epithelial splicing regulatory protein 2"
location: "16q22.1"
module: 31
arm: "+"
pooled_cpm: 5.86
n_lines_expressing: 24
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 14
direction_downstream: 31
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ESRP2

*epithelial splicing regulatory protein 2* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.66× (z +13.7, q 3e-40, up in 4 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +9.0, q 9e-17, up in 12 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.686× (z -4.1, q 0.012, down in 10 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND2D]] (+0.62, fdr 1e-05), [[PTPN18]] (+0.56, fdr 2e-05), [[SPTBN2]] (+0.55, fdr 4e-05); moves opposite to [[ZNF235]] (-0.52, fdr 3e-05), [[ZNF565]] (-0.49, fdr 4e-05), [[ZNF559-ZNF177]] (-0.49, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[SH2D4A]] → it (grade B ⚠); 31 go from it, the strongest it → [[SSH3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2317.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.66×** | +13.7 | 3e-40 | 4/10 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +9.0 | 9e-17 | 12/20 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +6.6 | 6e-09 | 2/15 (NCI-H2347, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +6.0 | 3e-07 | 2/17 (NCI-H2030, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +4.7 | 3e-04 | 3/19 (SW480, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.52×** | +4.6 | 3e-04 | 1/21 (LS 180) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.6 | 3e-04 | 8/21 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.5 | 4e-04 | 7/22 (NCI-H2030, SW48, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.77×** | +4.5 | 5e-04 | 0/20 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.1 | 0.002 | 1/18 (LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.67×** | +4.0 | 0.003 | 3/19 (NCI-H1573, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (maleate) (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.015 | 0/22 | inconsistent across doses | low cells (technical?); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.6 | 0.015 | 0/14 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.22×** | +3.1 | 0.067 | 4/22 (NCI-H2030, HEC-1-A, …) | top dose only | low cells (technical?) |
| [[Folic acid (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.082 | 3/22 (SW480, KATO III, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2317.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.686×** | -4.1 | 0.012 | 10/22 (RKO, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.491×** | -4.1 | 0.012 | 13/21 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -3.8 | 0.032 | 1/22 (HEC-1-A) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.721×** | -3.6 | 0.045 | 12/21 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.725×** | -3.5 | 0.046 | 12/22 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.731×** | -3.5 | 0.052 | 9/22 (COLO 205, SW480, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.736×** | -3.4 | 0.061 | 11/22 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.744×** | -3.3 | 0.081 | 10/22 (NCI-H1573, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.755× | -3.1 | 0.12 | 10/22 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.758× | -3.1 | 0.13 | 12/22 (A-427, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2317. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 10.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0444× (z -15.8) |
| [[NCI-H2030 (line)]] | alt | 6.42 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 8.22 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0684× (z -15.4) |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.147× (z -8.9) |
| [[HT-29 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.154× (z -8.6) ⚠ toxic |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -12.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 10.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0856× (z -8.6) |
| [[A-172 (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.829 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.474 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2317), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND2D]] | +0.62 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[PTPN18]] | +0.56 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[SPTBN2]] | +0.55 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[TMEM30B]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[IQANK1]] | +0.53 | +0.59 / +0.38 | both halves | 6e-05 |  |
| [[HGH1]] | +0.52 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[SAMD10]] | +0.51 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[SIGMAR1]] | +0.50 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[MST1R]] | +0.50 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[SSH3]] | +0.50 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[PRXL2B]] | +0.50 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[SYK]] | +0.49 | +0.49 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF235]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ZNF565]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[ZNF559-ZNF177]] | -0.49 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[SNHG6]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[RPL36]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[NDUFB4]] | -0.47 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[RPS28]] ⚠ | -0.47 | -0.42 / -0.41 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TOMM7]] | -0.46 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[DCTN6-DT]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[CWC15]] | -0.46 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[SEC22A]] | -0.46 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[UQCRB]] ⚠ | -0.45 | -0.42 / -0.40 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MC2]] | -0.45 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[NSA2]] | -0.45 | -0.44 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 2, C 12. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH2D4A]] | B | SH2D4A activity raises ESRP2's level | lines that do not express SH2D4A (11) vs lines expressing it (39) | 3.15× lower at baseline in the lines without SH2D4A | 0.066 | ⚠ within organs, on part of the lines; also absent: IL22RA1, ABCC3, CDA |
| [[HDAC6]] | B | HDAC6 activity raises ESRP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LAD1]] | C | LAD1 activity raises ESRP2's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 4.58× lower at baseline in the lines without LAD1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1; co-absent with the target |
| [[SPINT1-AS1]] | C | SPINT1-AS1 activity raises ESRP2's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 4.63× lower at baseline in the lines without SPINT1-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3; co-absent with the target |
| [[MST1R]] | C | MST1R activity raises ESRP2's level | lines that do not express MST1R (24) vs lines expressing it (26) | 4.51× lower at baseline in the lines without MST1R | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises ESRP2's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 4.56× lower at baseline in the lines without TMEM30B | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |
| [[IQANK1]] | C | IQANK1 activity raises ESRP2's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 3.70× lower at baseline in the lines without IQANK1 | 0.009 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent; co-absent with the target |
| [[YBX2]] | C | YBX2 activity raises ESRP2's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 3.39× lower at baseline in the lines without YBX2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9; co-absent with the target |
| [[DENND2D]] | C | DENND2D activity raises ESRP2's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.91× lower at baseline in the lines without DENND2D | 0.030 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG; co-absent with the target |
| [[CHDH]] | C | CHDH activity raises ESRP2's level | lines that do not express CHDH (22) vs lines expressing it (28) | 3.76× lower at baseline in the lines without CHDH | 0.035 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |
| [[TNFSF15]] | C | TNFSF15 activity raises ESRP2's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 4.29× lower at baseline in the lines without TNFSF15 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14; co-absent with the target |
| [[SYK]] | C | SYK activity raises ESRP2's level | lines that do not express SYK (30) vs lines expressing it (20) | 4.25× lower at baseline in the lines without SYK | 0.039 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 16, C 15. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSH3]] | B | ESRP2 activity raises SSH3's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.82× lower at baseline in the lines without ESRP2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[LRP5]] | B | ESRP2 activity raises LRP5's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 2.90× lower at baseline in the lines without ESRP2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[FSCN2]] | B | ESRP2 activity raises FSCN2's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.76× lower at baseline in the lines without ESRP2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[PSD4]] | B | ESRP2 activity raises PSD4's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 3.08× lower at baseline in the lines without ESRP2 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[ABHD11]] | B | ESRP2 activity raises ABHD11's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 2.45× lower at baseline in the lines without ESRP2 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[LRATD2]] | B | ESRP2 activity raises LRATD2's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 2.94× lower at baseline in the lines without ESRP2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[XK]] | B | ESRP2 activity raises XK's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.89× lower at baseline in the lines without ESRP2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[TRMT112]] | B | ESRP2 activity raises TRMT112's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.38× lower at baseline in the lines without ESRP2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[POLK]] | B | ESRP2 activity lowers POLK's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.47× higher at baseline in the lines without ESRP2 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[NDUFB4]] | B | ESRP2 activity raises NDUFB4's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.16× lower at baseline in the lines without ESRP2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[RPS29]] | B | ESRP2 activity raises RPS29's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.44× lower at baseline in the lines without ESRP2 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[SH2D4A]] | B | ESRP2 activity raises SH2D4A's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 2.77× lower at baseline in the lines without ESRP2 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.322). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.9, 54.9); signed map (31.6, -34.6). **Vector** length 52.0, 12.3% of its response variance represented; |z| ≥ 3 in 480 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +9.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.0 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +13.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.0 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +4.5 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | epithelial splicing regulatory protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:68,229,033-68,238,102 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21918; previously RBM35B |
| Gene groups (HGNC) | RNA binding motif containing; MicroRNA protein coding host genes; Epithelial splicing regulatory protein family |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: FGFR2 alternative splicing; Signaling by FGFR2; Signaling by FGFR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6T0](https://www.uniprot.org/uniprotkb/Q9H6T0) (Epithelial splicing regulatory protein 2):

> mRNA splicing factor that regulates the formation of epithelial cell-specific isoforms. Specifically regulates the expression of FGFR2-IIIb, an epithelial cell-specific isoform of FGFR2. Also regulates the splicing of CD44, CTNND1, ENAH, 3 transcripts that undergo changes in splicing during the epithelial-to-mesenchymal transition (EMT). Acts by directly binding specific sequences in mRNAs. Binds the GU-rich sequence motifs in the ISE/ISS-3, a cis-element regulatory region present in the mRNA …

**Summary**, from NCBI Gene [80004](https://www.ncbi.nlm.nih.gov/gene/80004):

> ESPR2 is an epithelial cell-type-specific splicing regulator (Warzecha et al., 2009 [PubMed 19285943]).[supplied by OMIM, Aug 2009]

**Accessions** — [HGNC:26152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26152) · Entrez [80004](https://www.ncbi.nlm.nih.gov/gene/80004) · UniProt [Q9H6T0](https://www.uniprot.org/uniprotkb/Q9H6T0) · Ensembl [ENSG00000103067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103067)

## Data

Gene col 2317: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2317); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2317, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2317]; `tensor/DDL_lfc|DDL_z.npy` [2317]; `embed/gene_vectors.npy` [2317]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2317 or target_col == 2317). Every well: [[ESRP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESRP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
