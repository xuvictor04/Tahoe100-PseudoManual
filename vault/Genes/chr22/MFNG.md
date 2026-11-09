---
symbol: "MFNG"
type: "gene"
col: 1856
ensembl_id: "ENSG00000100060"
name: "MFNG O-fucosylpeptide 3-beta-N-acetylglucosaminyltransferase"
location: "22q13.1"
module: 34
arm: "+"
pooled_cpm: 3.97
n_lines_expressing: 38
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 15
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# MFNG

*MFNG O-fucosylpeptide 3-beta-N-acetylglucosaminyltransferase* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.34× (z +10.1, q 4e-21, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.38× (z +4.0, q 0.011, up in 5 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.491× (z -6.2, q 3e-07, down in 18 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CARD10]] (+0.65, fdr 7e-06, ⚠ same locus), [[GAL3ST2]] (+0.60, fdr 1e-05), [[TTLL13]] (+0.60, fdr 1e-05), [[SPATA32]] (+0.57, fdr 4e-05); moves opposite to [[C3orf14]] (-0.52, fdr 2e-05), [[STX17]] (-0.46, fdr 4e-05), [[AZI2]] (-0.46, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PLCH2]] → it (grade B ⚠); 15 go from it, the strongest it → [[CDC42BPG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1856.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.34×** | +10.1 | 4e-21 | 2/7 (NCI-H2347, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +6.0 | 8e-07 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +5.8 | 9e-07 | 4/14 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.011 | 5/32 (LS 180, KATO III, …) | top dose only |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.3 | 0.094 | 3/18 (Panc 03.27, NCI-H2347, …) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | 1.47× | +3.1 | 0.17 | 2/18 (HOP62, Panc 03.27) | inconsistent across doses | position effect removed |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 1.42× | +3.1 | 0.17 | 3/25 (A-172, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1856.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.491×** | -6.2 | 3e-07 | 18/31 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.515×** | -5.8 | 2e-06 | 12/31 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.565×** | -4.8 | 3e-04 | 15/29 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.606×** | -4.4 | 0.002 | 14/32 (HCT15, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.637×** | -3.9 | 0.009 | 12/34 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.729×** | -3.9 | 0.009 | 20/28 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.649×** | -3.8 | 0.014 | 7/32 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.654×** | -3.7 | 0.015 | 14/30 (PANC-1, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.660×** | -3.6 | 0.019 | 15/30 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.456×** | -3.6 | 0.020 | 11/26 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.660×** | -3.3 | 0.042 | 9/32 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.693×** | -3.2 | 0.065 | 5/28 (HEC-1-A, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.700×** | -3.1 | 0.082 | 4/33 (HEC-1-A, J82, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1856. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 4 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0878× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.195× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 6.55 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0331× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 2.61 | 0 | 1 | — | [[Dimethyl fumarate (drug)]] 5 µM 0.0541× (z -8.7) |
| [[A-172 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.593 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.789 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1856), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARD10]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 | ⚠ same locus (4.0 kb, same strand: neighbours can correlate without regulation) |
| [[GAL3ST2]] | +0.60 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[TTLL13]] | +0.60 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[SPATA32]] | +0.57 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[RAPGEF3]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[SLC27A5]] | +0.57 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[SH3BP1]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[GDPGP1]] | +0.54 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[PDE2A]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[VSIG1]] | +0.54 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[LHX4]] | +0.54 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[ST6GALNAC6-1]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[SMIM41]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C3orf14]] | -0.52 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[STX17]] | -0.46 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[AZI2]] | -0.46 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[PHC3]] | -0.44 | -0.42 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCH2]] | B | PLCH2 activity raises MFNG's level | lines that do not express PLCH2 (26) vs lines expressing it (24) | 2.00× lower at baseline in the lines without PLCH2 | 0.012 | ⚠ within organs, on part of the lines; also absent: SERPINA5, LINC01814, ACOXL; maybe low, not absent |
| [[ZNF860]] | B | ZNF860 activity raises MFNG's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 1.98× lower at baseline in the lines without ZNF860 | 0.017 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[ATAD3C]] | B | ATAD3C activity raises MFNG's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 1.93× lower at baseline in the lines without ATAD3C | 0.026 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[FAM3C2P]] | B | FAM3C2P activity lowers MFNG's level | lines that do not express FAM3C2P (6) vs lines expressing it (44) | 1.85× higher at baseline in the lines without FAM3C2P | 0.074 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent |
| [[SPNS2]] | B | SPNS2 activity raises MFNG's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 1.78× lower at baseline in the lines without SPNS2 | 0.082 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[TNNT2]] | B | TNNT2 activity raises MFNG's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 1.85× lower at baseline in the lines without TNNT2 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[PRAG1]] | C | PRAG1 activity raises MFNG's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 2.12× lower at baseline in the lines without PRAG1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 12, C 3. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC42BPG]] | B | MFNG activity raises CDC42BPG's level | lines that do not express MFNG (12) vs lines expressing it (38) | 2.64× lower at baseline in the lines without MFNG | 0.012 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| [[SPNS2]] | B | MFNG activity raises SPNS2's level | lines that do not express MFNG (12) vs lines expressing it (38) | 3.40× lower at baseline in the lines without MFNG | 0.046 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| [[FSCN2]] | B | MFNG activity raises FSCN2's level | lines that do not express MFNG (12) vs lines expressing it (38) | 1.52× lower at baseline in the lines without MFNG | 0.052 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| [[TNNT2]] | B | MFNG activity raises TNNT2's level | lines that do not express MFNG (12) vs lines expressing it (38) | 2.28× lower at baseline in the lines without MFNG | 0.054 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| [[WNT2B]] | B | MFNG activity lowers WNT2B's level | lines that do not express MFNG (12) vs lines expressing it (38) | 1.53× higher at baseline in the lines without MFNG | 0.062 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| [[LAMA3]] | B | MFNG activity raises LAMA3's level | lines that do not express MFNG (12) vs lines expressing it (38) | 3.49× lower at baseline in the lines without MFNG | 0.063 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| [[SLC22A20P]] | B | MFNG activity raises SLC22A20P's level | lines that do not express MFNG (12) vs lines expressing it (38) | 1.96× lower at baseline in the lines without MFNG | 0.070 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| [[LSMEM2]] | B | MFNG activity raises LSMEM2's level | lines that do not express MFNG (12) vs lines expressing it (38) | 1.74× lower at baseline in the lines without MFNG | 0.083 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| cells under [[Peretinoin (drug)]] 5 µM | B | MFNG activity raises the cells' numbers under Peretinoin 5 µM (protects the cells) | lines that do not express MFNG (12) vs lines expressing it (36) | the lines without MFNG: 0.91× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| [[WNT7B]] | B | MFNG activity raises WNT7B's level | lines that do not express MFNG (12) vs lines expressing it (38) | 3.23× lower at baseline in the lines without MFNG | 0.094 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| cells under [[Omeprazole (drug)]] 5 µM | B | MFNG activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express MFNG (12) vs lines expressing it (36) | the lines without MFNG: 1.10× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| cells under [[Docetaxel (Trihydrate) (drug)]] 5 µM | B | MFNG activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express MFNG (12) vs lines expressing it (36) | the lines without MFNG: 0.85× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.9, -18.4); signed map (18.7, 14.9). **Vector** length 54.7, 9.40% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +1.2 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -3.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -4.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | MFNG O-fucosylpeptide 3-beta-N-acetylglucosaminyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,469,063-37,486,393 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Beta 3-glycosyltransferases |
| Reactome | 3 pathways, smallest: Pre-NOTCH Processing in Golgi; Pre-NOTCH Expression and Processing; Signaling by NOTCH |
| Matched by | ensembl_id |

**Function**, from UniProt [O00587](https://www.uniprot.org/uniprotkb/O00587) (Beta-1,3-N-acetylglucosaminyltransferase manic fringe):

> Glycosyltransferase that initiates the elongation of O-linked fucose residues attached to EGF-like repeats in the extracellular domain of Notch molecules (By similarity). Modulates NOTCH1 activity by modifying O-fucose residues at specific EGF-like domains resulting in inhibition of NOTCH1 activation by JAG1 and enhancement of NOTCH1 activation by DLL1 via an increase in its binding to DLL1 (By similarity).

**Summary**, from NCBI Gene [4242](https://www.ncbi.nlm.nih.gov/gene/4242):

> This gene is a member of the glycosyltransferase 31 gene family. Members of this gene family, which also includes the LFNG (GeneID: 3955) and RFNG (GeneID: 5986) genes, encode evolutionarily conserved glycosyltransferases that act in the Notch signaling pathway to define boundaries during embryonic development. While their genomic structure is distinct from other glycosyltransferases, these proteins have a fucose-specific beta-1,3-N-acetylglucosaminyltransferase activity that leads to …

**Accessions** — [HGNC:7038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7038) · Entrez [4242](https://www.ncbi.nlm.nih.gov/gene/4242) · UniProt [O00587](https://www.uniprot.org/uniprotkb/O00587) · Ensembl [ENSG00000100060](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100060)

## Data

Gene col 1856: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1856); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1856, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1856]; `tensor/DDL_lfc|DDL_z.npy` [1856]; `embed/gene_vectors.npy` [1856]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1856 or target_col == 1856). Every well: [[MFNG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFNG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
