---
symbol: "EPHA1"
type: "gene"
col: 7131
ensembl_id: "ENSG00000146904"
name: "EPH receptor A1"
location: "7q34-q35"
module: 31
arm: "+"
pooled_cpm: 3.75
n_lines_expressing: 27
n_dd_up: 24
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 66
direction_downstream: 68
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# EPHA1

*EPH receptor A1* — 7q34-q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.54× (z +9.7, q 2e-19, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 1.74× (z +6.0, q 3e-07, up in 2 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.674× (z -4.1, q 0.026, down in 9 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P2RY2]] (+0.72, fdr 1e-05), [[CBLC]] (+0.68, fdr 1e-05), [[CDH3]] (+0.67, fdr 2e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 66 arrows point to it, the strongest [[KRT19]] → it (grade B ⚠); 68 go from it, the strongest it → [[FAM83E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7131.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +9.7 | 2e-19 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +8.2 | 5e-14 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +7.6 | 4e-12 | 1/8 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.77×** | +6.1 | 1e-07 | 3/13 (HEC-1-A, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.74×** | +6.0 | 3e-07 | 2/20 (NCI-H23, A498) | all doses, flat | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +5.3 | 1e-05 | 3/13 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +5.0 | 4e-05 | 8/15 (LoVo, HCT15, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.55×** | +4.7 | 2e-04 | 1/17 (A498) | inconsistent across doses | position effect removed |
| [[Isocorydine (drug)]] 0.05 µM |  | **1.52×** | +4.5 | 3e-04 | 1/22 (NCI-H23) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.51×** | +4.5 | 4e-04 | 0/22 | all doses, flat | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.50×** | +4.4 | 6e-04 | 0/18 | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.76×** | +4.4 | 6e-04 | 1/11 (BT-474) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.002 | 4/20 (C32, HT-29, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.003 | 0/21 | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.007 | 2/19 (C32, HEC-1-A) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.015 | 0/22 | all doses, flat | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.015 | 2/14 (SW480, HT-29) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.025 | 8/22 (SW1417, KATO III, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[5-Azacytidine (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.043 | 3/19 (Panc 03.27, SW480, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **1.36×** | +3.1 | 0.050 | 0/18 | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.065 | 1/17 (A498) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7131.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.674×** | -4.1 | 0.026 | 9/18 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.707×** | -3.7 | 0.047 | 12/19 (KATO III, LS 180, …) | rises with dose | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.711×** | -3.7 | 0.047 | 4/21 (LoVo, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.721×** | -3.5 | 0.059 | 8/20 (NCI-H1573, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.724×** | -3.5 | 0.059 | 5/21 (COLO 205, HEC-1-A, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.735×** | -3.3 | 0.090 | 0/22 | two highest doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.565× | -3.2 | 0.11 | 2/20 (BT-474, LS 180) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 0.05 µM |  | 0.727× | -3.2 | 0.11 | 6/16 (SW1417, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7131. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 22.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -15.5) |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 1 | — | [[Afatinib (drug)]] 0.05 µM 0.144× (z -10.1) |
| [[KATO III (line)]] | alt | 9.15 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.969 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.983 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.915 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.779 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.896 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.911 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.897 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7131), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P2RY2]] | +0.72 | +0.72 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[CBLC]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[CDH3]] | +0.67 | +0.73 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[MUC2]] | +0.65 | +0.62 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[CEACAM5]] | +0.65 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[CEACAM6]] | +0.65 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[TMPRSS4]] | +0.64 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[IQANK1]] | +0.63 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[CAPN8]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[TMEM45B]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[TMC6]] | +0.60 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[CRYBG2]] | +0.60 | +0.53 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*66 arrows, 66 of them with an alert ⚠; grade A 0, B 7, C 59. Shown: the 12 strongest; 54 more arrows (54 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT19]] | B | KRT19 activity raises EPHA1's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.38× lower at baseline in the lines without KRT19 | 0.019 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[LMTK3]] | B | LMTK3 activity raises EPHA1's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 2.02× lower at baseline in the lines without LMTK3 | 0.041 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[LYPD3]] | B | LYPD3 activity raises EPHA1's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 2.13× lower at baseline in the lines without LYPD3 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[FLRT3]] | B | FLRT3 activity raises EPHA1's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 1.83× lower at baseline in the lines without FLRT3 | 0.065 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[FAM83E]] | B | FAM83E activity raises EPHA1's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 2.02× lower at baseline in the lines without FAM83E | 0.092 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[IGSF9]] | B | IGSF9 activity raises EPHA1's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 1.72× lower at baseline in the lines without IGSF9 | 0.093 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[TMEM92]] | B | TMEM92 activity raises EPHA1's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.73× lower at baseline in the lines without TMEM92 | 0.095 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[S100A14]] | C | S100A14 activity raises EPHA1's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 4.06× lower at baseline in the lines without S100A14 | 1e-05 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises EPHA1's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 4.24× lower at baseline in the lines without RAB25 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises EPHA1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.12× lower at baseline in the lines without TMPRSS4 | 3e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises EPHA1's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 4.22× lower at baseline in the lines without TMEM125 | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[MPZL2]] | C | MPZL2 activity raises EPHA1's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 3.35× lower at baseline in the lines without MPZL2 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14; co-absent with the target |

### Downstream of this gene

*68 arrows, 68 of them with an alert ⚠; grade A 0, B 17, C 51. Shown: the 12 strongest; 56 more arrows (56 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | EPHA1 activity raises FAM83E's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 3.31× lower at baseline in the lines without EPHA1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[ARHGEF16]] | B | EPHA1 activity raises ARHGEF16's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 2.91× lower at baseline in the lines without EPHA1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[ELMO3]] | B | EPHA1 activity raises ELMO3's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 2.17× lower at baseline in the lines without EPHA1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[LMTK3]] | B | EPHA1 activity raises LMTK3's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 2.42× lower at baseline in the lines without EPHA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[TMC6]] | B | EPHA1 activity raises TMC6's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 3.51× lower at baseline in the lines without EPHA1 | 0.009 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[ATM]] | B | EPHA1 activity lowers ATM's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 1.41× higher at baseline in the lines without EPHA1 | 0.014 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[IL22RA1]] | B | EPHA1 activity raises IL22RA1's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 2.41× lower at baseline in the lines without EPHA1 | 0.023 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[ABHD11]] | B | EPHA1 activity raises ABHD11's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 2.19× lower at baseline in the lines without EPHA1 | 0.037 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[IL1R2]] | B | EPHA1 activity raises IL1R2's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without EPHA1 | 0.042 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[ABHD17C]] | B | EPHA1 activity raises ABHD17C's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 2.01× lower at baseline in the lines without EPHA1 | 0.043 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[PKP2]] | B | EPHA1 activity raises PKP2's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 2.57× lower at baseline in the lines without EPHA1 | 0.046 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[AMN]] | B | EPHA1 activity raises AMN's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 1.84× lower at baseline in the lines without EPHA1 | 0.047 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.2, 54.0); signed map (58.9, 9.3). **Vector** length 39.7, 7.36% of its response variance represented; |z| ≥ 3 in 530 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +1.4 | +5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | +1.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.3 | +6.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +2.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +0.6 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.6 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.6 | +2.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.0 | +3.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | EPH receptor A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34-q35 — chr7:143,390,289-143,408,856 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EPH; previously EPHT, EPHT1 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; EPH receptors |
| Reactome | 7 pathways, smallest: POU5F1 (OCT4), SOX2, NANOG activate genes related to proliferation; Transcriptional regulation of pluripotent stem cells; EPHA-mediated growth cone collapse |
| Matched by | ensembl_id |

**Function**, from UniProt [P21709](https://www.uniprot.org/uniprotkb/P21709) (Ephrin type-A receptor 1):

> Receptor tyrosine kinase which binds promiscuously membrane-bound ephrin-A family ligands residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as reverse signaling. Binds with a low affinity EFNA3 and EFNA4 and with a high affinity to EFNA1 which most probably constitutes its …

**Summary**, from NCBI Gene [2041](https://www.ncbi.nlm.nih.gov/gene/2041):

> This gene belongs to the ephrin receptor subfamily of the protein-tyrosine kinase family. EPH and EPH-related receptors have been implicated in mediating developmental events, particularly in the nervous system. Receptors in the EPH subfamily typically have a single kinase domain and an extracellular region containing a Cys-rich domain and 2 fibronectin type III repeats. The ephrin receptors are divided into 2 groups based on the similarity of their extracellular domain sequences and their …

**Accessions** — [HGNC:3385](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3385) · Entrez [2041](https://www.ncbi.nlm.nih.gov/gene/2041) · UniProt [P21709](https://www.uniprot.org/uniprotkb/P21709) · Ensembl [ENSG00000146904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146904)

## Data

Gene col 7131: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7131); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7131, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7131]; `tensor/DDL_lfc|DDL_z.npy` [7131]; `embed/gene_vectors.npy` [7131]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7131 or target_col == 7131). Every well: [[EPHA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
