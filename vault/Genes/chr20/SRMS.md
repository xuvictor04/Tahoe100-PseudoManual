---
symbol: "SRMS"
type: "gene"
col: 4627
ensembl_id: "ENSG00000125508"
name: "src-related kinase lacking C-terminal regulatory tyrosine and N-terminal myristylation sites"
location: "20q13.33"
module: 47
arm: "+"
pooled_cpm: 2.09
n_lines_expressing: 36
n_dd_up: 9
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 28
direction_downstream: 47
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# SRMS

*src-related kinase lacking C-terminal regulatory tyrosine and N-terminal myristylation sites* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.06× (z +8.4, q 2e-14, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +4.2, q 0.003, up in 5 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.633× (z -4.1, q 0.026, down in 16 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO39]] (+0.68, fdr 7e-06), [[LGALS9]] (+0.67, fdr 7e-06), [[LSMEM2]] (+0.61, fdr 1e-05); moves opposite to [[KATNAL1]] (-0.51, fdr 4e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[MROH3P]] → it (grade B ⚠); 47 go from it, the strongest it → [[HELZ2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4627.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.06×** | +8.4 | 2e-14 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +4.6 | 1e-03 | 1/6 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.06×** | +4.5 | 1e-03 | 2/6 (LoVo, KATO III) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +4.5 | 1e-03 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.2 | 0.003 | 5/18 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +3.8 | 0.016 | 0/13 | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.024 | 3/22 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.5 | 0.033 | 0/7 | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.74×** | +3.5 | 0.033 | 1/15 (A498) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | 1.41× | +3.1 | 0.12 | 2/31 (CFPAC-1, Panc 03.27) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.66× | +3.0 | 0.12 | 2/10 (NCI-H2347, AsPC-1) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4627.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.633×** | -4.1 | 0.026 | 16/30 (KATO III, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.652×** | -3.8 | 0.040 | 15/28 (CFPAC-1, BT-474, …) | top dose only | position effect removed |
| [[Resveratrol (drug)]] 5 µM |  | **0.670×** | -3.6 | 0.067 | 6/31 (NCI-H23, Panc 03.27, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.585× | -3.4 | 0.10 | 14/31 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | 0.592× | -3.2 | 0.16 | 5/24 (BT-474, LoVo, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.607× | -3.1 | 0.16 | 14/26 (BT-474, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.514× | -3.0 | 0.21 | 3/27 (BT-474, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4627. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 12.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.174× (z -10.0) |
| [[BT-474 (line)]] | alt | 8.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -9.9) |
| [[KATO III (line)]] | alt | 16.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0956× (z -12.1) |
| [[A-172 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.268 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.687 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.565 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.872 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.608 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.780 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.691 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.785 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.208 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.576 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.882 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.233 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.755 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.626 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.718 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.324 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4627), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO39]] | +0.68 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[LGALS9]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[LSMEM2]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[NRIR]] | +0.60 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[REC8]] | +0.58 | +0.40 / +0.71 | both halves | 4e-05 |  |
| [[AMN]] | +0.58 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[FAM83E]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CATSPERB]] | +0.57 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[CEACAM5]] | +0.57 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[FSCN2]] | +0.57 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[TNNT2]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[C19orf38]] | +0.55 | +0.57 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KATNAL1]] | -0.51 | -0.54 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 23, C 5. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MROH3P]] | B | MROH3P activity raises SRMS's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 1.85× lower at baseline in the lines without MROH3P | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[C2CD4A]] | B | C2CD4A activity raises SRMS's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 2.74× lower at baseline in the lines without C2CD4A | 0.005 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L |
| [[TMEM45B]] | B | TMEM45B activity raises SRMS's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 2.32× lower at baseline in the lines without TMEM45B | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises SRMS's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.29× lower at baseline in the lines without TMPRSS4 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[P2RY2]] | B | P2RY2 activity raises SRMS's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 1.98× lower at baseline in the lines without P2RY2 | 0.013 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[IL1RN]] | B | IL1RN activity raises SRMS's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 1.94× lower at baseline in the lines without IL1RN | 0.015 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[CEACAM5]] | B | CEACAM5 activity raises SRMS's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.77× lower at baseline in the lines without CEACAM5 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[ARHGAP30]] | B | ARHGAP30 activity raises SRMS's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without ARHGAP30 | 0.017 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[CEACAM6]] | B | CEACAM6 activity raises SRMS's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 2.43× lower at baseline in the lines without CEACAM6 | 0.018 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[SMIM31]] | B | SMIM31 activity raises SRMS's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 2.14× lower at baseline in the lines without SMIM31 | 0.019 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[KATNAL1]] | B | KATNAL1 activity lowers SRMS's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 3.49× higher at baseline in the lines without KATNAL1 | 0.022 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[TNNT2]] | B | TNNT2 activity raises SRMS's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 1.93× lower at baseline in the lines without TNNT2 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 42, C 5. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HELZ2]] | B | SRMS activity raises HELZ2's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.75× lower at baseline in the lines without SRMS | 4e-05 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[OAS3]] | B | SRMS activity raises OAS3's level | lines that do not express SRMS (14) vs lines expressing it (36) | 3.69× lower at baseline in the lines without SRMS | 1e-04 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[PLSCR1]] | B | SRMS activity raises PLSCR1's level | lines that do not express SRMS (14) vs lines expressing it (36) | 3.29× lower at baseline in the lines without SRMS | 2e-04 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[CMPK2]] | B | SRMS activity raises CMPK2's level | lines that do not express SRMS (14) vs lines expressing it (36) | 3.56× lower at baseline in the lines without SRMS | 2e-04 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[TRIM25]] | B | SRMS activity raises TRIM25's level | lines that do not express SRMS (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without SRMS | 6e-04 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[REC8]] | B | SRMS activity raises REC8's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.01× lower at baseline in the lines without SRMS | 1e-03 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[PTK6]] | B | SRMS activity raises PTK6's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.38× lower at baseline in the lines without SRMS | 0.002 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[HELZ2]] | B | SRMS activity strengthens HELZ2's drug response | lines that do not express SRMS (14) vs lines expressing it (35) | the lines without SRMS respond 0.43× as strongly (z diff +2.99); strongest at Auranofin 5 µM: 0.58x vs 0.32x (z diff +4.6) | 0.004 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2; target measured in part of the lines; artifact flags |
| [[PARP10]] | B | SRMS activity raises PARP10's level | lines that do not express SRMS (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without SRMS | 0.006 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[BATF2]] | B | SRMS activity raises BATF2's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.11× lower at baseline in the lines without SRMS | 0.007 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[HSH2D]] | B | SRMS activity raises HSH2D's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.67× lower at baseline in the lines without SRMS | 0.008 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[IFI44L]] | B | SRMS activity raises IFI44L's level | lines that do not express SRMS (14) vs lines expressing it (36) | 3.73× lower at baseline in the lines without SRMS | 0.008 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.571). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.0, 57.0); signed map (68.4, 32.2). **Vector** length 44.3, 7.77% of its response variance represented; |z| ≥ 3 in 601 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +4.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.2 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.3 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.0 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | src-related kinase lacking C-terminal regulatory tyrosine and N-terminal myristylation sites |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,538,489-63,547,749 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SRM, dJ697K14.1, PTK70; previously C20orf148 |
| Gene groups (HGNC) | SH2 domain containing; PTK6 family tyrosine kinases; SH3 domain containing |
| Reactome | 3 pathways, smallest: PTK6 Down-Regulation; Signaling by Non-Receptor Tyrosine Kinases; Signaling by PTK6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3Y6](https://www.uniprot.org/uniprotkb/Q9H3Y6) (Tyrosine-protein kinase Srms):

> Non-receptor tyrosine-protein kinase which phosphorylates DOK1 on tyrosine residues. Also phosphorylates KHDRBS1/SAM68 and VIM on tyrosine residues. Phosphorylation of KHDRBS1 is EGF-dependent. Phosphorylates OTUB1, promoting deubiquitination of RPTOR.

**Summary**, from NCBI Gene [6725](https://www.ncbi.nlm.nih.gov/gene/6725):

> Enables protein tyrosine kinase activity. Involved in peptidyl-tyrosine autophosphorylation and positive regulation of TORC1 signaling. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11298) · Entrez [6725](https://www.ncbi.nlm.nih.gov/gene/6725) · UniProt [Q9H3Y6](https://www.uniprot.org/uniprotkb/Q9H3Y6) · Ensembl [ENSG00000125508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125508)

## Data

Gene col 4627: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4627); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4627, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4627]; `tensor/DDL_lfc|DDL_z.npy` [4627]; `embed/gene_vectors.npy` [4627]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4627 or target_col == 4627). Every well: [[SRMS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRMS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
