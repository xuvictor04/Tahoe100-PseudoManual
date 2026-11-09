---
symbol: "TMEM30B"
type: "gene"
col: 11239
ensembl_id: "ENSG00000182107"
name: "cell division cycle 50 P4-ATPase accessory subunit B"
location: "14q23.1"
module: 73
arm: "+"
pooled_cpm: 7.38
n_lines_expressing: 15
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 90
direction_downstream: 137
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# TMEM30B

*cell division cycle 50 P4-ATPase accessory subunit B* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.49× (z +15.1, q 0e+00, up in 8 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +5.0, q 7e-05, up in 2 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.562× (z -5.8, q 3e-06, down in 13 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC17]] (+0.78, fdr 7e-06), [[LINC01559]] (+0.78, fdr 7e-06), [[NPSR1]] (+0.75, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 90 arrows point to it, the strongest [[RNF220]] → it (grade B ⚠); 137 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11239.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.49×** | +15.1 | 0e+00 | 8/10 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.53×** | +14.6 | 1e-45 | 5/7 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.25×** | +10.9 | 2e-25 | 5/10 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.46×** | +9.0 | 3e-17 | 5/13 (SW1417, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +5.0 | 6e-05 | 5/13 (SW1417, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.0 | 7e-05 | 2/13 (NCI-H1573, NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.81×** | +4.2 | 0.002 | 3/12 (LS 180, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.55×** | +4.2 | 0.002 | 0/13 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.75×** | +4.0 | 0.004 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +3.9 | 0.005 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.016 | 5/13 (HCT15, LS 180, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.017 | 0/13 | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.1 | 0.076 | 1/13 (NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.1 | 0.081 | 0/6 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11239.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.562×** | -5.8 | 3e-06 | 13/13 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.567×** | -5.7 | 3e-06 | 13/13 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | **0.647×** | -4.1 | 0.008 | 0/13 | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.670×** | -4.0 | 0.008 | 13/13 (KATO III, HT-29, …) | top dose only |  |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.674×** | -3.7 | 0.020 | 0/13 | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.706×** | -3.2 | 0.095 | 1/13 (SW48) | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 0.5 µM |  | **0.727×** | -3.2 | 0.095 | 0/13 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.727×** | -3.2 | 0.095 | 4/13 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 26.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0217× (z -20.6) |
| [[HT-29 (line)]] | alt | 26.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -10.0) |
| [[KATO III (line)]] | alt | 43.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0813× (z -18.5) |
| [[LoVo (line)]] | wt | 6.66 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0947× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.147× (z -9.2) |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0891× (z -8.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 40.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -9.8) |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.189× (z -9.9) |
| [[A-172 (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.943 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.736 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.641 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.585 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.740 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.678 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.607 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.664 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC17]] | +0.78 | +0.72 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[LINC01559]] | +0.78 | +0.77 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[NPSR1]] | +0.75 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[LINC02474]] | +0.74 | +0.79 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[HEPH]] | +0.73 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[GCNT3]] | +0.73 | +0.80 / +0.58 | both halves | 7e-06 |  |
| [[FAM3D]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[CEACAM5]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[DENND2D]] | +0.70 | +0.72 / +0.58 | both halves | 8e-06 |  |
| [[GPX2]] | +0.70 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[KRT20]] | +0.70 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[CFTR]] | +0.70 | +0.67 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*90 arrows, 90 of them with an alert ⚠; grade A 0, B 10, C 80. Shown: the 12 strongest; 78 more arrows (78 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF220]] | B | RNF220 activity lowers TMEM30B's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 3.05× higher at baseline in the lines without RNF220 | 0.055 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises TMEM30B's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without SLC44A3-AS1 | 0.056 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[LRATD2]] | B | LRATD2 activity raises TMEM30B's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 3.03× lower at baseline in the lines without LRATD2 | 0.060 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[POU5F1B]] | B | POU5F1B activity raises TMEM30B's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 2.86× lower at baseline in the lines without POU5F1B | 0.065 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[ZNF503-AS1]] | B | ZNF503-AS1 activity raises TMEM30B's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.28× lower at baseline in the lines without ZNF503-AS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[EPS8L1]] | B | EPS8L1 activity raises TMEM30B's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.74× lower at baseline in the lines without EPS8L1 | 0.067 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[HTR1D]] | B | HTR1D activity raises TMEM30B's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.86× lower at baseline in the lines without HTR1D | 0.076 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises TMEM30B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HNF4G]] | B | HNF4G activity raises TMEM30B's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 2.99× lower at baseline in the lines without HNF4G | 0.094 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[TNFRSF21]] | B | TNFRSF21 activity raises TMEM30B's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 2.96× lower at baseline in the lines without TNFRSF21 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[RAB25]] | C | RAB25 activity raises TMEM30B's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 8.48× lower at baseline in the lines without RAB25 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises TMEM30B's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 8.54× lower at baseline in the lines without TMPRSS4 | 3e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |

### Downstream of this gene

*137 arrows, 137 of them with an alert ⚠; grade A 0, B 44, C 93. Shown: the 12 strongest; 125 more arrows (125 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | TMEM30B activity raises EPS8L1's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 5.34× lower at baseline in the lines without TMEM30B | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[ABHD11]] | B | TMEM30B activity raises ABHD11's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 3.19× lower at baseline in the lines without TMEM30B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[LRATD2]] | B | TMEM30B activity raises LRATD2's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 4.06× lower at baseline in the lines without TMEM30B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[TNFRSF21]] | B | TMEM30B activity raises TNFRSF21's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 4.82× lower at baseline in the lines without TMEM30B | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[SDCBP2]] | B | TMEM30B activity raises SDCBP2's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 4.85× lower at baseline in the lines without TMEM30B | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[TMEM184A]] | B | TMEM30B activity raises TMEM184A's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 2.84× lower at baseline in the lines without TMEM30B | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[OCLN]] | B | TMEM30B activity strengthens OCLN's drug response | lines that do not express TMEM30B (16) vs lines expressing it (14) | the lines without TMEM30B respond 0.22× as strongly (z diff +4.95); strongest at Homoharringtonine 5 µM: 1.07x vs 0.39x (z diff +8.3) | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; target measured in part of the lines; artifact flags |
| [[FUT2]] | B | TMEM30B activity raises FUT2's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 2.96× lower at baseline in the lines without TMEM30B | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[MAPK13]] | B | TMEM30B activity raises MAPK13's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 3.94× lower at baseline in the lines without TMEM30B | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[KRT8]] | B | TMEM30B activity raises KRT8's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 4.75× lower at baseline in the lines without TMEM30B | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[GAREM1]] | B | TMEM30B activity raises GAREM1's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 3.44× lower at baseline in the lines without TMEM30B | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[LINC00857]] | B | TMEM30B activity raises LINC00857's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 3.05× lower at baseline in the lines without TMEM30B | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.1, 51.4); signed map (62.4, 7.2). **Vector** length 49.1, 18.7% of its response variance represented; |z| ≥ 3 in 255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +15.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +10.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +5.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +4.0 |
| fall | [[TAK-733 (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.7 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.7 | -1.3 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -0.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 50 P4-ATPase accessory subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:61,277,370-61,281,761 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TMEM30B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3MIR4](https://www.uniprot.org/uniprotkb/Q3MIR4) (Cell cycle control protein 50B):

> Accessory component of a P4-ATPase flippase complex which catalyzes the hydrolysis of ATP coupled to the transport of aminophospholipids from the outer to the inner leaflet of various membranes and ensures the maintenance of asymmetric distribution of phospholipids. Phospholipid translocation also seems to be implicated in vesicle formation and in uptake of lipid signaling molecules. The beta subunit may assist in binding of the phospholipid substrate (Probable). Can mediate the export of alpha …

**Summary**, from NCBI Gene [161291](https://www.ncbi.nlm.nih.gov/gene/161291):

> Enables aminophospholipid flippase activity. Involved in aminophospholipid transport and positive regulation of protein exit from endoplasmic reticulum. Located in endoplasmic reticulum membrane and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27254](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27254) · Entrez [161291](https://www.ncbi.nlm.nih.gov/gene/161291) · UniProt [Q3MIR4](https://www.uniprot.org/uniprotkb/Q3MIR4) · Ensembl [ENSG00000182107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182107)

## Data

Gene col 11239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11239); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11239]; `tensor/DDL_lfc|DDL_z.npy` [11239]; `embed/gene_vectors.npy` [11239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11239 or target_col == 11239). Every well: [[TMEM30B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM30B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
