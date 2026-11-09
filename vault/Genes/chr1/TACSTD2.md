---
symbol: "TACSTD2"
type: "gene"
col: 11515
ensembl_id: "ENSG00000184292"
name: "tumor associated calcium signal transducer 2"
location: "1p32.1"
module: 8
arm: "+"
pooled_cpm: 25.61
n_lines_expressing: 16
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 89
direction_downstream: 97
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TACSTD2

*tumor associated calcium signal transducer 2* — 1p32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.57× (z +12.2, q 3e-31, up in 8 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Docetaxel (Trihydrate) (drug)]] 0.5 µM: 1.62× (z +3.9, q 0.012, up in 0 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.536× (z -5.0, q 4e-04, down in 13 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRT23]] (+0.72, fdr 7e-06), [[SPINT1]] (+0.72, fdr 9e-06), [[ADGRF1]] (+0.69, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 89 arrows point to it, the strongest [[LRATD2]] → it (grade B ⚠); 97 go from it, the strongest it → [[MUC20]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11515.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.57×** | +12.2 | 3e-31 | 8/15 (NCI-H1792, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +8.4 | 1e-14 | 7/11 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.09×** | +8.4 | 1e-14 | 5/13 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.3 | 0.003 | 3/14 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.62×** | +3.9 | 0.012 | 0/14 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.36×** | +3.8 | 0.016 | 1/14 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.57×** | +3.6 | 0.025 | 4/14 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.025 | 8/14 (COLO 205, HT-29, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.042 | 1/15 (Hs 766T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.3 | 0.053 | 5/14 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.077 | 0/14 | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **2.11×** | +3.1 | 0.084 | 5/14 (HCT15, COLO 205, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11515.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.536×** | -5.0 | 4e-04 | 13/14 (COLO 205, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.583×** | -4.3 | 0.005 | 13/14 (KATO III, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.604×** | -4.0 | 0.011 | 12/14 (KATO III, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.628×** | -3.6 | 0.052 | 8/14 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.624×** | -3.5 | 0.057 | 1/14 (HCT15) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.442×** | -3.4 | 0.063 | 8/15 (Panc 03.27, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.642×** | -3.3 | 0.089 | 0/14 | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.887× | -3.2 | 0.099 | 1/15 (Hs 766T) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.657×** | -3.2 | 0.099 | 1/14 (Hs 766T) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 256 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 170 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -12.2) |
| [[COLO 205 (line)]] | alt | 126 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0312× (z -15.5) |
| [[KATO III (line)]] | alt | 53.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0570× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 246 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -21.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.227× (z -9.7) |
| [[HCT15 (line)]] | alt | 19.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -9.7) |
| [[SW1417 (line)]] | alt | 29.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -8.5) |
| [[A-172 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT23]] | +0.72 | +0.58 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SPINT1]] | +0.72 | +0.75 / +0.57 | both halves | 9e-06 | STRING 458 |
| [[ADGRF1]] | +0.69 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[NECTIN4]] | +0.68 | +0.71 / +0.54 | both halves | 1e-05 | STRING 600 |
| [[CLDN4]] | +0.68 | +0.70 / +0.61 | both halves | 7e-06 | STRING 555 |
| [[WFDC2]] | +0.68 | +0.72 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[CLDN7]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 | STRING 966 |
| [[ST14]] | +0.67 | +0.74 / +0.56 | both halves | 1e-05 | STRING 491 |
| [[ITGB6]] | +0.66 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[TSPAN1]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[LINC01559]] | +0.65 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[LGALS9]] | +0.65 | +0.66 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*89 arrows, 89 of them with an alert ⚠; grade A 0, B 4, C 85. Shown: the 12 strongest; 77 more arrows (77 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRATD2]] | B | LRATD2 activity raises TACSTD2's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 3.34× lower at baseline in the lines without LRATD2 | 0.037 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[JUP]] | B | JUP activity raises TACSTD2's level | lines that do not express JUP (16) vs lines expressing it (34) | 3.02× lower at baseline in the lines without JUP | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[GRHL3]] | B | GRHL3 activity raises TACSTD2's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 3.08× lower at baseline in the lines without GRHL3 | 0.094 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises TACSTD2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TMEM30B]] | C | TMEM30B activity raises TACSTD2's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 8.95× lower at baseline in the lines without TMEM30B | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises TACSTD2's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 6.07× lower at baseline in the lines without MAL2 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises TACSTD2's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 11.22× lower at baseline in the lines without STEAP4 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |
| [[FUT3]] | C | FUT3 activity raises TACSTD2's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 5.10× lower at baseline in the lines without FUT3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises TACSTD2's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 9.47× lower at baseline in the lines without WFDC2 | 7e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises TACSTD2's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 6.75× lower at baseline in the lines without RAB25 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[ST14]] | C | ST14 activity raises TACSTD2's level | lines that do not express ST14 (32) vs lines expressing it (18) | 6.88× lower at baseline in the lines without ST14 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises TACSTD2's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 6.17× lower at baseline in the lines without CDH1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |

### Downstream of this gene

*97 arrows, 97 of them with an alert ⚠; grade A 0, B 17, C 80. Shown: the 12 strongest; 85 more arrows (85 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC20]] | B | TACSTD2 activity raises MUC20's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 3.50× lower at baseline in the lines without TACSTD2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3 |
| [[JUP]] | B | TACSTD2 activity raises JUP's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 4.08× lower at baseline in the lines without TACSTD2 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3 |
| [[OCLN]] | B | TACSTD2 activity strengthens OCLN's drug response | lines that do not express TACSTD2 (17) vs lines expressing it (13) | the lines without TACSTD2 respond 0.38× as strongly (z diff +3.50); strongest at Homoharringtonine 5 µM: 0.90x vs 0.46x (z diff +5.2) | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3; target measured in part of the lines; artifact flags |
| [[BCL2L15]] | B | TACSTD2 activity raises BCL2L15's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 2.68× lower at baseline in the lines without TACSTD2 | 0.016 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3 |
| [[KPNA7]] | B | TACSTD2 activity raises KPNA7's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 2.23× lower at baseline in the lines without TACSTD2 | 0.025 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3 |
| [[TNFRSF21]] | B | TACSTD2 activity raises TNFRSF21's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 3.44× lower at baseline in the lines without TACSTD2 | 0.025 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3 |
| [[LGALS9]] | B | TACSTD2 activity raises LGALS9's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 2.80× lower at baseline in the lines without TACSTD2 | 0.027 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3 |
| [[EPS8L1]] | B | TACSTD2 activity raises EPS8L1's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 2.83× lower at baseline in the lines without TACSTD2 | 0.030 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3 |
| [[TMEM184A]] | B | TACSTD2 activity raises TMEM184A's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 2.33× lower at baseline in the lines without TACSTD2 | 0.030 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3 |
| [[FAM83E]] | B | TACSTD2 activity raises FAM83E's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 3.08× lower at baseline in the lines without TACSTD2 | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3 |
| [[LRATD2]] | B | TACSTD2 activity raises LRATD2's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 2.96× lower at baseline in the lines without TACSTD2 | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3 |
| [[STS]] | B | TACSTD2 activity raises STS's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 2.67× lower at baseline in the lines without TACSTD2 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.1, 57.3); signed map (57.7, 7.4). **Vector** length 48.0, 16.9% of its response variance represented; |z| ≥ 3 in 292 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +0.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.1 | +3.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +1.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +2.0 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.0 | +0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.0 | -2.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | tumor associated calcium signal transducer 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.1 — chr1:58,575,433-58,577,252 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TROP2, GA733-1, EGP-1; previously M1S1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P09758](https://www.uniprot.org/uniprotkb/P09758) (Tumor-associated calcium signal transducer 2):

> May function as a growth factor receptor.

**Summary**, from NCBI Gene [4070](https://www.ncbi.nlm.nih.gov/gene/4070):

> This intronless gene encodes a carcinoma-associated antigen. This antigen is a cell surface receptor that transduces calcium signals. Mutations of this gene have been associated with gelatinous drop-like corneal dystrophy.[provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:11530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11530) · Entrez [4070](https://www.ncbi.nlm.nih.gov/gene/4070) · UniProt [P09758](https://www.uniprot.org/uniprotkb/P09758) · Ensembl [ENSG00000184292](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184292)

## Data

Gene col 11515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11515); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11515]; `tensor/DDL_lfc|DDL_z.npy` [11515]; `embed/gene_vectors.npy` [11515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11515 or target_col == 11515). Every well: [[TACSTD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TACSTD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
