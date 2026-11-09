---
symbol: "SLC6A14"
type: "gene"
col: 15589
ensembl_id: "ENSG00000268104"
name: "solute carrier family 6 member 14"
location: "Xq23"
module: 55
arm: "+"
pooled_cpm: 17.97
n_lines_expressing: 11
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 86
direction_downstream: 108
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# SLC6A14

*solute carrier family 6 member 14* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.99× (z +11.9, q 5e-30, up in 1 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.48× (z +4.8, q 2e-04, up in 6 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.410× (z -7.7, q 8e-12, down in 9 of 9 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST6GALNAC1]] (+0.74, fdr 7e-06), [[MUC5B]] (+0.74, fdr 7e-06), [[CATSPERB]] (+0.72, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 86 arrows point to it, the strongest [[RAPGEF5]] → it (grade B ⚠); 108 go from it, the strongest it → [[FAM83E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15589.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.99×** | +11.9 | 5e-30 | 1/9 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.88×** | +11.2 | 7e-27 | 1/7 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +8.5 | 2e-15 | 1/8 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +5.1 | 4e-05 | 1/9 (BT-474) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +4.8 | 2e-04 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +4.8 | 2e-04 | 6/9 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.5 | 5e-04 | 2/9 (BT-474, HT-29) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.00×** | +3.9 | 0.006 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.016 | 2/9 (KATO III, NCI-H2347) | top dose only |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.017 | 0/10 | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.51×** | +3.6 | 0.020 | 0/10 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.5 | 0.020 | 1/9 (NCI-H2347) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.49×** | +3.4 | 0.025 | 1/9 (Panc 03.27) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.82×** | +3.4 | 0.029 | 1/9 (NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15589.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.410×** | -7.7 | 8e-12 | 9/9 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.484×** | -6.3 | 1e-07 | 8/9 (HepG2/C3A, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.631×** | -4.0 | 0.010 | 2/9 (HT-29, KATO III) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.599×** | -4.0 | 0.010 | 1/9 (LS 180) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.635×** | -3.9 | 0.010 | 8/9 (KATO III, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.646×** | -3.8 | 0.015 | 6/9 (HepG2/C3A, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.668×** | -3.5 | 0.040 | 8/9 (HepG2/C3A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.671×** | -3.4 | 0.040 | 7/9 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | 0.467× | -3.1 | 0.10 | 5/10 (KATO III, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.779× | -3.1 | 0.13 | 7/9 (LS 180, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 112 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0386× (z -21.1) |
| [[HepG2_C3A (line)]] | wt | 181 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0720× (z -19.9) |
| [[LS 180 (line)]] | wt | 92.6 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0865× (z -19.2) |
| [[CFPAC-1 (line)]] | alt | 213 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -12.6) |
| [[BT-474 (line)]] | alt | 37.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.117× (z -9.8) |
| [[A-172 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.979 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.23 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC1]] | +0.74 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[MUC5B]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[CATSPERB]] | +0.72 | +0.69 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[GPX2]] | +0.71 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[TMEM45B]] | +0.70 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[TC2N]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[MPZL2]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[SIDT1]] | +0.67 | +0.60 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[HSD17B2]] | +0.67 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[C9orf152]] | +0.67 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R1B]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[NPSR1]] | +0.65 | +0.70 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*86 arrows, 86 of them with an alert ⚠; grade A 0, B 4, C 82. Shown: the 12 strongest; 74 more arrows (74 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF5]] | B | RAPGEF5 activity raises SLC6A14's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.63× lower at baseline in the lines without RAPGEF5 | 0.052 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[ARHGEF34P]] | B | ARHGEF34P activity raises SLC6A14's level | lines that do not express ARHGEF34P (19) vs lines expressing it (31) | 2.80× lower at baseline in the lines without ARHGEF34P | 0.081 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000284644, ESRP2, GOLT1A |
| [[HDAC6]] | B | HDAC6 activity raises SLC6A14's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ABCC3]] | B | ABCC3 activity raises SLC6A14's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.60× lower at baseline in the lines without ABCC3 | 0.089 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[RAB25]] | C | RAB25 activity raises SLC6A14's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 6.75× lower at baseline in the lines without RAB25 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises SLC6A14's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 5.75× lower at baseline in the lines without TMEM30B | 8e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises SLC6A14's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 8.92× lower at baseline in the lines without ST6GALNAC1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises SLC6A14's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 7.68× lower at baseline in the lines without SLC44A4 | 0.002 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[GSDMC]] | C | GSDMC activity raises SLC6A14's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 7.87× lower at baseline in the lines without GSDMC | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises SLC6A14's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 6.57× lower at baseline in the lines without MUC5B | 0.003 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises SLC6A14's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 5.71× lower at baseline in the lines without TMPRSS2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[ITGB6]] | C | ITGB6 activity raises SLC6A14's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 4.11× lower at baseline in the lines without ITGB6 | 0.003 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4; co-absent with the target |

### Downstream of this gene

*108 arrows, 108 of them with an alert ⚠; grade A 0, B 29, C 79. Shown: the 12 strongest; 96 more arrows (96 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | SLC6A14 activity raises FAM83E's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 4.45× lower at baseline in the lines without SLC6A14 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[IQANK1]] | B | SLC6A14 activity raises IQANK1's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 3.62× lower at baseline in the lines without SLC6A14 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[USP6NL]] | B | SLC6A14 activity raises USP6NL's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 2.09× lower at baseline in the lines without SLC6A14 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[ARHGEF34P]] | B | SLC6A14 activity raises ARHGEF34P's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 3.46× lower at baseline in the lines without SLC6A14 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[ELMO3]] | B | SLC6A14 activity raises ELMO3's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 2.31× lower at baseline in the lines without SLC6A14 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[SLC12A2]] | B | SLC6A14 activity raises SLC12A2's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 2.22× lower at baseline in the lines without SLC6A14 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[TNFRSF21]] | B | SLC6A14 activity raises TNFRSF21's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 4.52× lower at baseline in the lines without SLC6A14 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[KRT8]] | B | SLC6A14 activity raises KRT8's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 3.94× lower at baseline in the lines without SLC6A14 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[TCP11L1]] | B | SLC6A14 activity lowers TCP11L1's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 1.97× higher at baseline in the lines without SLC6A14 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[MANSC1]] | B | SLC6A14 activity raises MANSC1's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 2.54× lower at baseline in the lines without SLC6A14 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[SHROOM3]] | B | SLC6A14 activity raises SHROOM3's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 3.21× lower at baseline in the lines without SLC6A14 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[GAREM1]] | B | SLC6A14 activity raises GAREM1's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 3.12× lower at baseline in the lines without SLC6A14 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.7, 55.3); signed map (60.8, 8.0). **Vector** length 49.6, 19.5% of its response variance represented; |z| ≥ 3 in 336 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.0 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.0 | -0.6 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.9 | +1.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.8 | +0.7 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 6 member 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq23 — chrX:116,436,606-116,461,458 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Solute carrier family 6 |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 7 pathways, smallest: SLC-mediated transport of neurotransmitters; Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UN76](https://www.uniprot.org/uniprotkb/Q9UN76) (Sodium- and chloride-dependent neutral and basic amino acid transporter B(0+)):

> Amino acid transporter that plays an important role in the absorption of amino acids in the intestinal tract. Mediates the uptake of a broad range of neutral and cationic amino acids (with the exception of proline) in a Na(+)/Cl(-)-dependent manner. Transports non-alpha-amino acids such as beta-alanine with low affinity, and has a higher affinity for dipolar and cationic amino acids such as leucine and lysine. Can also transport carnitine, butirylcarnitine and propionylcarnitine coupled to the …

**Summary**, from NCBI Gene [11254](https://www.ncbi.nlm.nih.gov/gene/11254):

> This gene encodes a member of the solute carrier family 6. Members of this family are sodium and chloride dependent neurotransmitter transporters. The encoded protein transports both neutral and cationic amino acids. This protein may also function as a beta-alanine carrier. Mutations in this gene may be associated with X-linked obesity. A pseudogene of this gene is found on chromosome X.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:11047](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11047) · Entrez [11254](https://www.ncbi.nlm.nih.gov/gene/11254) · UniProt [Q9UN76](https://www.uniprot.org/uniprotkb/Q9UN76) · Ensembl [ENSG00000268104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000268104)

## Data

Gene col 15589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15589); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15589]; `tensor/DDL_lfc|DDL_z.npy` [15589]; `embed/gene_vectors.npy` [15589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15589 or target_col == 15589). Every well: [[SLC6A14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC6A14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
