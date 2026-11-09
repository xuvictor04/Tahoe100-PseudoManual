---
symbol: "HOXB8"
type: "gene"
col: 4155
ensembl_id: "ENSG00000120068"
name: "homeobox B8"
location: "17q21.32"
module: 201
arm: "+"
pooled_cpm: 4.03
n_lines_expressing: 31
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# HOXB8

*homeobox B8* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.51× (z +10.7, q 3e-24, up in 10 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.330× (z -9.2, q 1e-17, down in 25 of 28 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOTAIR]] (+0.69, fdr 1e-05), [[HOXB6]] (+0.69, fdr 7e-06, ⚠ same locus), [[HOXB5]] (+0.64, fdr 1e-05, ⚠ same locus), [[TSPOAP1]] (+0.56, fdr 4e-05), [[TSPOAP1-AS1]] (+0.55, fdr 8e-05); moves opposite to [[PTPRG-AS1]] (-0.49, fdr 1e-04), [[MTG1]] (-0.46, fdr 6e-04), [[ASCC2]] (-0.46, fdr 3e-04).
> It is in [[Module 201]], a single-armed module (Kidney development).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HOXB4]] → it (grade B ⚠); 5 go from it, the strongest it → [[HOXB3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4155.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +10.7 | 3e-24 | 10/21 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.27×** | +9.4 | 1e-18 | 3/5 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +9.1 | 2e-17 | 6/13 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +7.8 | 1e-12 | 3/7 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +4.6 | 3e-04 | 3/12 (LoVo, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +4.6 | 3e-04 | 3/28 (HCT15, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.29×** | +4.2 | 0.002 | 2/17 (SW480, A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.1 | 0.003 | 3/16 (A498, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.007 | 9/25 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.6 | 0.018 | 1/21 (A498) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.95×** | +3.4 | 0.033 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.049 | 5/20 (A-172, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.064 | 5/22 (HCT15, RKO, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4155.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.330×** | -9.2 | 1e-17 | 25/28 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.564×** | -6.8 | 3e-09 | 17/21 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.457×** | -6.5 | 1e-08 | 19/27 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.498×** | -5.8 | 8e-07 | 16/19 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.527×** | -5.4 | 1e-05 | 16/27 (SW480, SW1417, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.638×** | -3.6 | 0.026 | 13/26 (SNU-423, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.657×** | -3.5 | 0.033 | 5/28 (NCI-H1573, RPMI-7951, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.692× | -3.1 | 0.14 | 11/27 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4155. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.0 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0953× (z -16.6) |
| [[PANC-1 (line)]] | alt | 8.14 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -11.9) |
| [[LoVo (line)]] | wt | 8.27 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0665× (z -12.2) |
| [[SW1417 (line)]] | alt | 25.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0662× (z -17.1) |
| [[A-172 (line)]] | wt | 4.86 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 2.40 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0268× (z -10.3) |
| [[A549 (line)]] | wt | 3.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.66× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 2.73 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0887× (z -9.4) |
| [[HCT15 (line)]] | alt | 7.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -10.5) |
| [[SHP-77 (line)]] | alt | 4.55 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -10.1) |
| [[A-427 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.733 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.765 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.775 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4155), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 16 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOTAIR]] | +0.69 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[HOXB6]] | +0.69 | +0.58 / +0.59 | both halves | 7e-06 | same gene group; STRING 887; ⚠ same locus (6.4 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB5]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 | same gene group; STRING 911; ⚠ same locus (17.6 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB3]] | +0.64 | +0.52 / +0.53 | both halves | 1e-05 | same gene group; STRING 714; ⚠ same locus (6.5 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB7]] | +0.61 | +0.43 / +0.61 | both halves | 3e-05 | same gene group; STRING 755; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB-AS3]] | +0.61 | +0.47 / +0.49 | both halves | 2e-05 | ⚠ same locus (5.0 kb: neighbours can correlate without regulation) |
| [[TSPOAP1]] | +0.56 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[HOXB4]] | +0.56 | +0.51 / +0.40 | both halves | 5e-05 | same gene group; STRING 561; ⚠ same locus (33.0 kb, same strand: neighbours can correlate without regulation) |
| [[TSPOAP1-AS1]] | +0.55 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[BMP7]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[USP6NL]] | +0.53 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[GPRC5C]] | +0.52 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[P4HTM]] | +0.52 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[SATB2-AS1]] | +0.51 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[BCAR3-AS1]] | +0.51 | +0.26 / +0.45 | both halves | 3e-04 |  |
| [[OVOL2]] | +0.51 | +0.40 / +0.33 | both halves | 1e-04 |  |
| [[AXIN2]] | +0.51 | +0.43 / +0.33 | both halves | 1e-04 |  |
| [[PTCH1]] | +0.51 | +0.44 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRG-AS1]] | -0.49 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[MTG1]] | -0.46 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[ASCC2]] | -0.46 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[AP1M1]] | -0.45 | -0.27 / -0.30 | both halves | 3e-04 |  |
| [[BCAP29]] | -0.45 | -0.14 / -0.51 | ⚠ one half (not replicated) | 0.002 |  |
| [[HUS1]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ZNF674]] | -0.44 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[IPO9]] | -0.43 | -0.21 / -0.57 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB4]] | B | HOXB4 activity raises HOXB8's level | lines that do not express HOXB4 (12) vs lines expressing it (38) | 2.15× lower at baseline in the lines without HOXB4 | 0.055 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises HOXB8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HOXB5]], [[HOXB6]] | C | HOXB5, HOXB6 activity raises HOXB8's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 2.35× lower at baseline in the lines without HOXB5, HOXB6 | 0.021 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent with the target; co-absent genes |
| [[LINC02086]] | C | LINC02086 activity raises HOXB8's level | lines that do not express LINC02086 (24) vs lines expressing it (26) | 2.34× lower at baseline in the lines without LINC02086 | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MIR4713HG, SERPINB9, PRSS3; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB3]] | B | HOXB8 activity raises HOXB3's level | lines that do not express HOXB8 (19) vs lines expressing it (31) | 3.26× lower at baseline in the lines without HOXB8 | 0.011 | ⚠ within organs, on part of the lines; also absent: FAM83F, LINC02086, ZBTB7C |
| [[HOXB-AS3]] | B | HOXB8 activity raises HOXB-AS3's level | lines that do not express HOXB8 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without HOXB8 | 0.022 | ⚠ within organs, on part of the lines; also absent: FAM83F, LINC02086, ZBTB7C |
| [[HOXB7]] | B | HOXB8 activity raises HOXB7's level | lines that do not express HOXB8 (19) vs lines expressing it (31) | 2.38× lower at baseline in the lines without HOXB8 | 0.029 | ⚠ within organs, on part of the lines; also absent: FAM83F, LINC02086, ZBTB7C |
| [[HOXB6]] | C | HOXB8 activity raises HOXB6's level | lines that do not express HOXB8 (19) vs lines expressing it (31) | 3.51× lower at baseline in the lines without HOXB8 | 0.012 | ⚠ within organs, on part of the lines; also absent: FAM83F, LINC02086, ZBTB7C; co-absent with the target |
| [[HOXB5]] | C | HOXB8 activity raises HOXB5's level | lines that do not express HOXB8 (19) vs lines expressing it (31) | 2.42× lower at baseline in the lines without HOXB8 | 0.056 | ⚠ within organs, on part of the lines; also absent: FAM83F, LINC02086, ZBTB7C; co-absent with the target |

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-0.8, 26.8); signed map (39.3, -4.2). **Vector** length 39.5, 6.05% of its response variance represented; |z| ≥ 3 in 613 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +10.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.9 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.4 | -6.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.4 | -9.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.4 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -3.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | homeobox B8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,611,377-48,615,292 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX2, HOX2D |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P17481](https://www.uniprot.org/uniprotkb/P17481) (Homeobox protein Hox-B8):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3218](https://www.ncbi.nlm.nih.gov/gene/3218):

> This gene is a member of the Antp homeobox family and encodes a nuclear protein with a homeobox DNA-binding domain. It is included in a cluster of homeobox B genes located on chromosome 17. The encoded protein functions as a sequence-specific transcription factor that is involved in development. Increased expression of this gene is associated with colorectal cancer. Mice that have had the murine ortholog of this gene knocked out exhibit an excessive pathologic grooming behavior. This behavior …

**Accessions** — [HGNC:5119](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5119) · Entrez [3218](https://www.ncbi.nlm.nih.gov/gene/3218) · UniProt [P17481](https://www.uniprot.org/uniprotkb/P17481) · Ensembl [ENSG00000120068](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120068)

## Data

Gene col 4155: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4155); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4155, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4155]; `tensor/DDL_lfc|DDL_z.npy` [4155]; `embed/gene_vectors.npy` [4155]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4155 or target_col == 4155). Every well: [[HOXB8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXB8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
