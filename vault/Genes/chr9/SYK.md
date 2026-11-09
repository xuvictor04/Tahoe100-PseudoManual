---
symbol: "SYK"
type: "gene"
col: 9054
ensembl_id: "ENSG00000165025"
name: "spleen associated tyrosine kinase"
location: "9q22.2"
module: 55
arm: "+"
pooled_cpm: 34.76
n_lines_expressing: 20
n_dd_up: 12
n_dd_down: 25
n_dd_up_clean: 6
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 105
direction_downstream: 116
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# SYK

*spleen associated tyrosine kinase* — 9q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.27× (z +16.2, q 0e+00, up in 7 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +4.8, q 3e-04, up in 0 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.404× (z -12.4, q 2e-32, down in 18 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABO]] (+0.77, fdr 7e-06), [[KCNE3]] (+0.76, fdr 7e-06), [[ZNF503-AS1]] (+0.75, fdr 7e-06); moves opposite to [[EPOR]] (-0.56, fdr 3e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 105 arrows point to it, the strongest [[SPATA6L]] → it (grade B ⚠); 116 go from it, the strongest it → [[TMEM184A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9054.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.27×** | +16.2 | 0e+00 | 7/18 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +13.9 | 2e-41 | 6/15 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +7.7 | 2e-12 | 3/17 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.8 | 3e-04 | 0/18 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.38×** | +4.5 | 1e-03 | 0/18 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +4.4 | 0.001 | 1/18 (BT-474) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.007 | 12/18 (KATO III, SW1417, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.6 | 0.021 | 3/18 (A498, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.027 | 6/18 (SW480, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +3.5 | 0.027 | 1/18 (NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.034 | 10/18 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.2 | 0.067 | 2/18 (NCI-H1573, BT-474) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9054.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.404×** | -12.4 | 2e-32 | 18/18 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.482×** | -10.0 | 7e-21 | 18/18 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.599×** | -9.9 | 1e-20 | 17/18 (RKO, COLO 205, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.502×** | -9.4 | 7e-19 | 18/18 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.593×** | -7.1 | 1e-10 | 16/18 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.597×** | -7.0 | 2e-10 | 17/18 (SW48, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.608×** | -6.8 | 1e-09 | 16/18 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.666×** | -5.5 | 2e-06 | 14/18 (SHP-77, RKO, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.714×** | -4.6 | 3e-04 | 16/18 (LoVo, HT-29, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.715×** | -4.6 | 3e-04 | 14/18 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.543×** | -4.4 | 7e-04 | 17/19 (RKO, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.545×** | -4.3 | 7e-04 | 13/18 (HEC-1-A, COLO 205, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.719×** | -4.3 | 7e-04 | 13/18 (COLO 205, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.733×** | -4.2 | 9e-04 | 7/18 (RKO, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.733×** | -4.2 | 9e-04 | 2/18 (SHP-77, RKO) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9054. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 71.7 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0565× (z -34.1) |
| [[COLO 205 (line)]] | alt | 103 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0440× (z -26.7) |
| [[LoVo (line)]] | wt | 93.6 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -22.5) |
| [[SW480 (line)]] | alt | 196 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0507× (z -25.0) |
| [[HEC-1-A (line)]] | alt | 74.4 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -17.9) |
| [[KATO III (line)]] | alt | 76.8 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0400× (z -26.3) |
| [[LS 180 (line)]] | wt | 80.1 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0984× (z -21.3) |
| [[SHP-77 (line)]] | alt | 70.0 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -18.4) |
| [[SW1417 (line)]] | alt | 158 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -16.2) |
| [[HT-29 (line)]] | alt | 55.7 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -18.2) |
| [[NCI-H1573 (line)]] | alt | 20.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -16.0) |
| [[Panc 03.27 (line)]] | alt | 27.0 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 24.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -12.0) |
| [[SW48 (line)]] | wt | 46.8 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -13.6) |
| [[A498 (line)]] | wt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -11.3) |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 31.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.331× (z -9.8) |
| [[A-172 (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.95 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.53 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9054), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABO]] | +0.77 | +0.80 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.76 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[ZNF503-AS1]] | +0.75 | +0.69 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[PROM1]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[LINC02253]] | +0.72 | +0.63 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A3]] | +0.71 | +0.71 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[C9orf152]] | +0.71 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[GPX2]] | +0.70 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[IL20RA]] | +0.70 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[SPINT1-AS1]] | +0.70 | +0.77 / +0.51 | both halves | 1e-05 |  |
| [[DENND2D]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPOR]] | -0.56 | -0.58 / -0.43 | both halves | 3e-05 | STRING 526 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*105 arrows, 105 of them with an alert ⚠; grade A 0, B 11, C 94. Shown: the 12 strongest; 93 more arrows (93 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPATA6L]] | B | SPATA6L activity raises SYK's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.67× lower at baseline in the lines without SPATA6L | 0.034 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[DCLK2]] | B | DCLK2 activity lowers SYK's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 4.75× higher at baseline in the lines without DCLK2 | 0.044 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[FAM20C]] | B | FAM20C activity lowers SYK's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 3.88× higher at baseline in the lines without FAM20C | 0.045 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[UBE2Q2P13]] | B | UBE2Q2P13 activity lowers SYK's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 4.05× higher at baseline in the lines without UBE2Q2P13 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1 |
| [[PCAT1]] | B | PCAT1 activity raises SYK's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 3.85× lower at baseline in the lines without PCAT1 | 0.051 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[ZNF860]] | B | ZNF860 activity raises SYK's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 3.50× lower at baseline in the lines without ZNF860 | 0.054 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[POU5F1B]] | B | POU5F1B activity raises SYK's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 3.99× lower at baseline in the lines without POU5F1B | 0.055 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[MAPK13]] | B | MAPK13 activity raises SYK's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 3.83× lower at baseline in the lines without MAPK13 | 0.060 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[ZNF404]] | B | ZNF404 activity lowers SYK's level | lines that do not express ZNF404 (14) vs lines expressing it (36) | 7.74× higher at baseline in the lines without ZNF404 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MIR130AHG, RAB34, PYGO1 |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises SYK's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.86× lower at baseline in the lines without SLC44A3-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[BRSK1]] | B | BRSK1 activity lowers SYK's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 4.52× higher at baseline in the lines without BRSK1 | 0.095 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[LINC03040]] | C | LINC03040 activity raises SYK's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 6.24× lower at baseline in the lines without LINC03040 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2; co-absent with the target |

### Downstream of this gene

*116 arrows, 116 of them with an alert ⚠; grade A 0, B 31, C 85. Shown: the 12 strongest; 104 more arrows (104 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM184A]] | B | SYK activity raises TMEM184A's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.81× lower at baseline in the lines without SYK | 0.005 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[MAPK13]] | B | SYK activity raises MAPK13's level | lines that do not express SYK (30) vs lines expressing it (20) | 3.61× lower at baseline in the lines without SYK | 0.006 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[SLC37A1]] | B | SYK activity raises SLC37A1's level | lines that do not express SYK (30) vs lines expressing it (20) | 3.96× lower at baseline in the lines without SYK | 0.007 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[SLC44A3]] | B | SYK activity raises SLC44A3's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.95× lower at baseline in the lines without SYK | 0.014 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[TJP2]] | B | SYK activity raises TJP2's level | lines that do not express SYK (30) vs lines expressing it (20) | 3.15× lower at baseline in the lines without SYK | 0.015 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[PCAT1]] | B | SYK activity raises PCAT1's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.94× lower at baseline in the lines without SYK | 0.015 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[STS]] | B | SYK activity raises STS's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.33× lower at baseline in the lines without SYK | 0.018 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[UBE2Q2P13]] | B | SYK activity lowers UBE2Q2P13's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.56× higher at baseline in the lines without SYK | 0.020 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[USP6NL]] | B | SYK activity raises USP6NL's level | lines that do not express SYK (30) vs lines expressing it (20) | 1.99× lower at baseline in the lines without SYK | 0.021 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[RAMP1]] | B | SYK activity raises RAMP1's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.11× lower at baseline in the lines without SYK | 0.025 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[MFSD6]] | B | SYK activity raises MFSD6's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without SYK | 0.027 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[ZNF404]] | B | SYK activity lowers ZNF404's level | lines that do not express SYK (30) vs lines expressing it (20) | 3.75× higher at baseline in the lines without SYK | 0.027 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.6, 48.7); signed map (62.4, 8.2). **Vector** length 82.1, 31.8% of its response variance represented; |z| ≥ 3 in 506 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +16.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +4.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.1 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -4.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | spleen associated tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.2 — chr9:90,801,787-90,898,549 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SH2 domain containing; Syk family tyrosine kinases |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 44 pathways, smallest: FLT3 signaling through SRC family kinases; FCGR activation; Interleukin-2 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P43405](https://www.uniprot.org/uniprotkb/P43405) (Tyrosine-protein kinase SYK):

> Non-receptor tyrosine kinase which mediates signal transduction downstream of a variety of transmembrane receptors including classical immunoreceptors like the B-cell receptor (BCR). Regulates several biological processes including innate and adaptive immunity, cell adhesion, osteoclast maturation, platelet activation and vascular development. Assembles into signaling complexes with activated receptors at the plasma membrane via interaction between its SH2 domains and the receptor …

**Summary**, from NCBI Gene [6850](https://www.ncbi.nlm.nih.gov/gene/6850):

> This gene encodes a member of the family of non-receptor type Tyr protein kinases. This protein is widely expressed in hematopoietic cells and is involved in coupling activated immunoreceptors to downstream signaling events that mediate diverse cellular responses, including proliferation, differentiation, and phagocytosis. It is thought to be a modulator of epithelial cell growth and a potential tumour suppressor in human breast carcinomas. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:11491](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11491) · Entrez [6850](https://www.ncbi.nlm.nih.gov/gene/6850) · UniProt [P43405](https://www.uniprot.org/uniprotkb/P43405) · Ensembl [ENSG00000165025](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165025)

## Data

Gene col 9054: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9054); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9054, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9054]; `tensor/DDL_lfc|DDL_z.npy` [9054]; `embed/gene_vectors.npy` [9054]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9054 or target_col == 9054). Every well: [[SYK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
