---
symbol: "ABO"
type: "gene"
col: 10571
ensembl_id: "ENSG00000175164"
name: "ABO, alpha 1-3-N-acetylgalactosaminyltransferase and alpha 1-3-galactosyltransferase"
location: "9q34.2"
module: 55
arm: "+"
pooled_cpm: 9.42
n_lines_expressing: 18
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 89
direction_downstream: 78
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# ABO

*ABO, alpha 1-3-N-acetylgalactosaminyltransferase and alpha 1-3-galactosyltransferase* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.51× (z +11.9, q 5e-30, up in 0 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.490× (z -6.5, q 5e-08, down in 15 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO7B]] (+0.82, fdr 7e-06), [[PROM1]] (+0.79, fdr 7e-06), [[IL20RA]] (+0.77, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 89 arrows point to it, the strongest [[UBE2Q2P13]] → it (grade B ⚠); 78 go from it, the strongest it → [[ASS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10571.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +11.9 | 5e-30 | 0/15 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.68×** | +8.7 | 1e-15 | 2/9 (AsPC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +7.4 | 2e-11 | 2/13 (Hs 766T, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Thymol (drug)]] 0.5 µM |  | **1.61×** | +4.4 | 0.002 | 9/15 (SW1417, KATO III, …) | two highest doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.86×** | +4.0 | 0.006 | 7/15 (KATO III, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.018 | 1/16 (SHP-77) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +3.6 | 0.026 | 1/11 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.3 | 0.079 | 2/14 (SW1417, NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10571.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.490×** | -6.5 | 5e-08 | 15/15 (LS 180, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.514×** | -6.1 | 4e-07 | 15/16 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.529×** | -5.8 | 1e-06 | 14/16 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.552×** | -5.4 | 9e-06 | 13/16 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.570×** | -5.1 | 4e-05 | 16/16 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.588×** | -4.8 | 1e-04 | 12/15 (SHP-77, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.589×** | -4.6 | 3e-04 | 15/16 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.657×** | -3.8 | 0.010 | 11/16 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.682×** | -3.5 | 0.032 | 15/16 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.689×** | -3.3 | 0.065 | 3/16 (NCI-H2347, Hs 766T, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.500×** | -3.2 | 0.066 | 8/15 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.710×** | -3.1 | 0.090 | 0/15 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.714×** | -3.1 | 0.095 | 4/16 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10571. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 64.9 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -23.7) |
| [[COLO 205 (line)]] | alt | 92.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0424× (z -32.2) |
| [[LoVo (line)]] | wt | 52.2 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -18.8) |
| [[HCT15 (line)]] | alt | 35.5 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0907× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0360× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.1000× (z -11.0) |
| [[RKO (line)]] | wt | 10.6 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0719× (z -11.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -9.7) |
| [[SW48 (line)]] | wt | 39.8 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -11.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.254× (z -10.1) |
| [[HT-29 (line)]] | alt | 8.50 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -12.9) |
| [[SW1417 (line)]] | alt | 33.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -10.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW480 (line)]] | alt | 4.70 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.124× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0642× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.110× (z -9.9) |
| [[KATO III (line)]] | alt | 58.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -14.2) |
| [[Hs 766T (line)]] | wt | 8.15 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0657× (z -14.0) |
| [[SHP-77 (line)]] | alt | 9.21 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0558× (z -11.0) |
| [[A-172 (line)]] | wt | 0.906 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.724 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.842 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.900 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.928 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.959 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.74 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10571), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO7B]] | +0.82 | +0.78 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PROM1]] | +0.79 | +0.75 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[IL20RA]] | +0.77 | +0.82 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[SYK]] | +0.77 | +0.80 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.76 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[CLIC5]] | +0.76 | +0.78 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TNFRSF14-AS1]] | +0.76 | +0.77 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.75 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.75 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[GCNT3]] | +0.75 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[USH1C]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[NPSR1]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*89 arrows, 89 of them with an alert ⚠; grade A 0, B 8, C 81. Shown: the 12 strongest; 77 more arrows (77 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2Q2P13]] | B | UBE2Q2P13 activity lowers ABO's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 3.61× higher at baseline in the lines without UBE2Q2P13 | 0.012 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1 |
| [[SYDE1]] | B | SYDE1 activity lowers ABO's level | lines that do not express SYDE1 (11) vs lines expressing it (39) | 10.63× higher at baseline in the lines without SYDE1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with APC, ACVR2A; also absent: DNAAF9, ZNF134, ENSG00000286964 |
| [[ZNF503-AS1]] | B | ZNF503-AS1 activity raises ABO's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without ZNF503-AS1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises ABO's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.31× lower at baseline in the lines without SLC44A3 | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises ABO's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.31× lower at baseline in the lines without SLC44A3-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[GNA14]] | B | GNA14 activity raises ABO's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 1.44× lower at baseline in the lines without GNA14 | 0.077 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[TRIM2]] | B | TRIM2 activity raises ABO's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 3.25× lower at baseline in the lines without TRIM2 | 0.079 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[DNAAF9]] | B | DNAAF9 activity lowers ABO's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 8.90× higher at baseline in the lines without DNAAF9 | 0.089 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; its own permutation p |
| [[TMC5]] | C | TMC5 activity raises ABO's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 5.62× lower at baseline in the lines without TMC5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4; co-absent with the target |
| [[SYNPR-AS1]] | C | SYNPR-AS1 activity raises ABO's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 4.96× lower at baseline in the lines without SYNPR-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3; co-absent with the target |
| [[PPP1R1B]] | C | PPP1R1B activity raises ABO's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 5.59× lower at baseline in the lines without PPP1R1B | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17; co-absent with the target |
| [[NPNT]] | C | NPNT activity raises ABO's level | lines that do not express NPNT (33) vs lines expressing it (17) | 5.49× lower at baseline in the lines without NPNT | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |

### Downstream of this gene

*78 arrows, 78 of them with an alert ⚠; grade A 0, B 18, C 60. Shown: the 12 strongest; 66 more arrows (66 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASS1]] | B | ABO activity raises ASS1's level | lines that do not express ABO (32) vs lines expressing it (18) | 5.14× lower at baseline in the lines without ABO | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[UBE2Q2P13]] | B | ABO activity lowers UBE2Q2P13's level | lines that do not express ABO (32) vs lines expressing it (18) | 2.65× higher at baseline in the lines without ABO | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[ZNF503-AS1]] | B | ABO activity raises ZNF503-AS1's level | lines that do not express ABO (32) vs lines expressing it (18) | 2.42× lower at baseline in the lines without ABO | 0.023 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[RAPGEF5]] | B | ABO activity raises RAPGEF5's level | lines that do not express ABO (32) vs lines expressing it (18) | 3.73× lower at baseline in the lines without ABO | 0.026 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[SYDE1]] | B | ABO activity lowers SYDE1's level | lines that do not express ABO (32) vs lines expressing it (18) | 4.74× higher at baseline in the lines without ABO | 0.030 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[SLC37A1]] | B | ABO activity raises SLC37A1's level | lines that do not express ABO (32) vs lines expressing it (18) | 3.39× lower at baseline in the lines without ABO | 0.032 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[MFSD6]] | B | ABO activity raises MFSD6's level | lines that do not express ABO (32) vs lines expressing it (18) | 2.49× lower at baseline in the lines without ABO | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[RAMP1]] | B | ABO activity raises RAMP1's level | lines that do not express ABO (32) vs lines expressing it (18) | 2.79× lower at baseline in the lines without ABO | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[FUT2]] | B | ABO activity raises FUT2's level | lines that do not express ABO (32) vs lines expressing it (18) | 2.33× lower at baseline in the lines without ABO | 0.057 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[PIK3C2B]] | B | ABO activity raises PIK3C2B's level | lines that do not express ABO (32) vs lines expressing it (18) | 2.21× lower at baseline in the lines without ABO | 0.059 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[TMEM184A]] | B | ABO activity raises TMEM184A's level | lines that do not express ABO (32) vs lines expressing it (18) | 2.07× lower at baseline in the lines without ABO | 0.060 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[SPATA6L]] | B | ABO activity raises SPATA6L's level | lines that do not express ABO (32) vs lines expressing it (18) | 3.78× lower at baseline in the lines without ABO | 0.066 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.823). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.1, 49.5); signed map (62.1, 8.0). **Vector** length 65.7, 24.4% of its response variance represented; |z| ≥ 3 in 399 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +11.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +4.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +2.9 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -5.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.7 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ABO, alpha 1-3-N-acetylgalactosaminyltransferase and alpha 1-3-galactosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:133,233,278-133,276,024 (-) |
| Ensembl biotype | protein_coding |
| Also known as | A3GALNT, A3GALT1 |
| Gene groups (HGNC) | Glycosyltransferase family 6; Blood group antigens |
| Reactome | 2 pathways, smallest: Blood group systems biosynthesis; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P16442](https://www.uniprot.org/uniprotkb/P16442) (Histo-blood group ABO system transferase):

> This protein is the basis of the ABO blood group system. The histo-blood group ABO involves three carbohydrate antigens: A, B, and H. A, B, and AB individuals express a glycosyltransferase activity that converts the H antigen to the A antigen (by addition of N-acetyl-alpha-D-galactosamine (GalNAc)) or to the B antigen (by addition of galactose (Gal)), whereas O individuals lack such activity and express the H antigen precursor unmodified.; Catalyzes the transfer of GalNAc or Gal in an alpha1,3 …

**Summary**, from NCBI Gene [28](https://www.ncbi.nlm.nih.gov/gene/28):

> This gene encodes proteins related to the first discovered blood group system, ABO. Variation in the ABO gene (chromosome 9q34.2) is the basis of the ABO blood group, thus the presence of an allele determines the blood group in an individual. The 'O' blood group is caused by a deletion of guanine-258 near the N-terminus of the protein which results in a frameshift and translation of an almost entirely different protein. Individuals with the A, B, and AB alleles express glycosyltransferase …

**Accessions** — [HGNC:79](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:79) · Entrez [28](https://www.ncbi.nlm.nih.gov/gene/28) · UniProt [P16442](https://www.uniprot.org/uniprotkb/P16442) · Ensembl [ENSG00000175164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175164)

## Data

Gene col 10571: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10571); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10571, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10571]; `tensor/DDL_lfc|DDL_z.npy` [10571]; `embed/gene_vectors.npy` [10571]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10571 or target_col == 10571). Every well: [[ABO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
