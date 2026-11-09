---
symbol: "PROM1"
type: "gene"
col: 136
ensembl_id: "ENSG00000007062"
name: "prominin 1"
location: "4p15.32"
module: 8
arm: "+"
pooled_cpm: 12.68
n_lines_expressing: 13
n_dd_up: 22
n_dd_down: 13
n_dd_up_clean: 17
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 113
direction_downstream: 137
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PROM1

*prominin 1* — 4p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.42× (z +21.1, q 0e+00, up in 0 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.618× (z -5.9, q 3e-06, down in 2 of 11 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNE3]] (+0.81, fdr 7e-06), [[ABO]] (+0.79, fdr 7e-06), [[LINC01814]] (+0.78, fdr 7e-06); moves opposite to [[DNAAF9]] (-0.61, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 113 arrows point to it, the strongest [[MAP2K6]] → it (grade B ⚠); 137 go from it, the strongest it → [[ACTR3C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 136.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.42×** | +21.1 | 0e+00 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.25×** | +13.7 | 2e-40 | 2/9 (CFPAC-1, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.98×** | +13.2 | 1e-37 | 1/9 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +9.1 | 1e-17 | 1/9 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +8.0 | 1e-13 | 1/11 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +5.8 | 5e-07 | 5/11 (HT-29, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +5.5 | 4e-06 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.3 | 6e-06 | 0/10 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +4.6 | 3e-04 | 7/11 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 0.001 | 7/11 (HT-29, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +4.2 | 0.001 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +4.2 | 0.001 | 5/11 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.013 | 2/11 (HT-29, CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **1.88×** | +3.6 | 0.014 | 4/10 (CFPAC-1, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.035 | 0/11 | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.037 | 0/11 | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.048 | 1/11 (CFPAC-1) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.067 | 1/11 (HT-29) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **1.71×** | +3.0 | 0.068 | 2/11 (SW480, CFPAC-1) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 136.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.618×** | -5.9 | 3e-06 | 2/11 (COLO 205, SW480) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.637×** | -5.5 | 1e-05 | 9/11 (LoVo, KATO III, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.701×** | -4.3 | 0.003 | 10/11 (LoVo, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.784×** | -4.2 | 0.004 | 5/11 (HT-29, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.714×** | -3.8 | 0.016 | 0/11 | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.05 µM |  | **0.718×** | -3.7 | 0.017 | 0/11 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.752×** | -3.3 | 0.066 | 10/11 (SW1417, COLO 205, …) | two highest doses | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.766×** | -3.3 | 0.072 | 9/11 (LoVo, SW1417, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **0.767×** | -3.2 | 0.072 | 5/11 (SW1417, CFPAC-1, …) | top dose only |  |
| [[Ranolazine (drug)]] 0.5 µM |  | **0.768×** | -3.2 | 0.072 | 1/11 (SW1417) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.775×** | -3.1 | 0.094 | 6/11 (SW1417, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.761×** | -3.1 | 0.094 | 0/11 | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.766×** | -3.1 | 0.094 | 0/11 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 136. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 43.5 | 0 | 9 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -13.3) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.259× (z -11.3) |
| [[COLO 205 (line)]] | alt | 23.8 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0159× (z -14.4) |
| [[KATO III (line)]] | alt | 55.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -12.6) |
| [[SW1417 (line)]] | alt | 58.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0410× (z -24.4) |
| [[HT-29 (line)]] | alt | 76.4 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.310× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 58.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -14.0) |
| [[SW48 (line)]] | wt | 53.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -16.4) |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -14.6) |
| [[HepG2_C3A (line)]] | wt | 32.2 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.149× (z -8.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.933 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.964 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.885 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.869 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.962 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.838 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.998 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 136), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNE3]] | +0.81 | +0.83 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ABO]] | +0.79 | +0.75 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[LINC01814]] | +0.78 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[BCL2L15]] | +0.78 | +0.80 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[LINC02331]] | +0.76 | +0.75 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC00299]] | +0.76 | +0.69 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CLIC5]] | +0.75 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[SYK]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[GPX2]] | +0.75 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[MGAM2]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.74 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[TOX3]] | +0.73 | +0.73 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.61 | -0.56 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*113 arrows, 113 of them with an alert ⚠; grade A 0, B 7, C 106. Shown: the 12 strongest; 101 more arrows (101 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K6]] | B | MAP2K6 activity raises PROM1's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 2.15× lower at baseline in the lines without MAP2K6 | 0.023 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[MTUS1]] | B | MTUS1 activity raises PROM1's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.96× lower at baseline in the lines without MTUS1 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[CCSER1]] | B | CCSER1 activity raises PROM1's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 2.33× lower at baseline in the lines without CCSER1 | 0.066 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[RAPGEF5]] | B | RAPGEF5 activity raises PROM1's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.81× lower at baseline in the lines without RAPGEF5 | 0.067 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises PROM1's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.61× lower at baseline in the lines without SLC44A3-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises PROM1's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.57× lower at baseline in the lines without SLC44A3 | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[PLEKHS1]] | B | PLEKHS1 activity raises PROM1's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 2.41× lower at baseline in the lines without PLEKHS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[LINC01814]] | C | LINC01814 activity raises PROM1's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 5.57× lower at baseline in the lines without LINC01814 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises PROM1's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 6.26× lower at baseline in the lines without RAB25 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises PROM1's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 6.89× lower at baseline in the lines without STEAP4 | 0.001 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises PROM1's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 5.76× lower at baseline in the lines without MAL2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[TMEM45B]] | C | TMEM45B activity raises PROM1's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 6.47× lower at baseline in the lines without TMEM45B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; co-absent with the target |

### Downstream of this gene

*137 arrows, 137 of them with an alert ⚠; grade A 0, B 32, C 105. Shown: the 12 strongest; 125 more arrows (125 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTR3C]] | B | PROM1 activity raises ACTR3C's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 3.59× lower at baseline in the lines without PROM1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[PLEKHA7]] | B | PROM1 activity raises PLEKHA7's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 3.32× lower at baseline in the lines without PROM1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[ARHGEF34P]] | B | PROM1 activity raises ARHGEF34P's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 3.56× lower at baseline in the lines without PROM1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[MTUS1]] | B | PROM1 activity raises MTUS1's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 4.48× lower at baseline in the lines without PROM1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[LINC00511]] | B | PROM1 activity raises LINC00511's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 4.11× lower at baseline in the lines without PROM1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[TMEM51-AS1]] | B | PROM1 activity raises TMEM51-AS1's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 2.94× lower at baseline in the lines without PROM1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[VILL]] | B | PROM1 activity raises VILL's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 2.68× lower at baseline in the lines without PROM1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[SLC25A25-AS1]] | B | PROM1 activity raises SLC25A25-AS1's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 2.15× lower at baseline in the lines without PROM1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[SLC44A3-AS1]] | B | PROM1 activity raises SLC44A3-AS1's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 3.10× lower at baseline in the lines without PROM1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[USP6NL]] | B | PROM1 activity raises USP6NL's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 2.25× lower at baseline in the lines without PROM1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[TNFRSF21]] | B | PROM1 activity raises TNFRSF21's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 4.36× lower at baseline in the lines without PROM1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[PCAT1]] | B | PROM1 activity raises PCAT1's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 2.61× lower at baseline in the lines without PROM1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.796). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.5, 49.0); signed map (61.9, 8.1). **Vector** length 66.2, 30.0% of its response variance represented; |z| ≥ 3 in 394 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.51 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +21.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.6 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +5.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.3 | +2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.3 | +2.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.3 | -5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -5.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.2 | -4.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -3.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | prominin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.32 — chr4:15,963,076-16,084,378 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AC133, CD133, RP41, CORD12; previously PROML1, MCDR2, STGD4 |
| Gene groups (HGNC) | CD molecules; Prominin family |
| Matched by | ensembl_id |

**Function**, from UniProt [O43490](https://www.uniprot.org/uniprotkb/O43490) (Prominin-1):

> May play a role in cell differentiation, proliferation and apoptosis. Binds cholesterol in cholesterol-containing plasma membrane microdomains and may play a role in the organization of the apical plasma membrane in epithelial cells. During early retinal development acts as a key regulator of disk morphogenesis. Involved in regulation of MAPK and Akt signaling pathways. In neuroblastoma cells suppresses cell differentiation such as neurite outgrowth in a RET-dependent manner.

**Summary**, from NCBI Gene [8842](https://www.ncbi.nlm.nih.gov/gene/8842):

> This gene encodes a pentaspan transmembrane glycoprotein. The protein localizes to membrane protrusions and is often expressed on adult stem cells, where it is thought to function in maintaining stem cell properties by suppressing differentiation. Mutations in this gene have been shown to result in retinitis pigmentosa and Stargardt disease. Expression of this gene is also associated with several types of cancer. This gene is expressed from at least five alternative promoters that are expressed …

**Accessions** — [HGNC:9454](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9454) · Entrez [8842](https://www.ncbi.nlm.nih.gov/gene/8842) · UniProt [O43490](https://www.uniprot.org/uniprotkb/O43490) · Ensembl [ENSG00000007062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007062)

## Data

Gene col 136: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 136); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 136, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 136]; `tensor/DDL_lfc|DDL_z.npy` [136]; `embed/gene_vectors.npy` [136]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 136 or target_col == 136). Every well: [[PROM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PROM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
