---
symbol: "FKBP9P1"
type: "gene"
col: 10753
ensembl_id: "ENSG00000176826"
name: "FKBP prolyl isomerase 9 pseudogene 1"
location: "7p11.2"
module: 27
arm: "+"
pooled_cpm: 2.95
n_lines_expressing: 40
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 22
direction_downstream: 3
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# FKBP9P1

*FKBP prolyl isomerase 9 pseudogene 1* — 7p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[AZD2858 (drug)]] 0.5 µM: 2.26× (z +5.2, q 1e-04, up in 0 of 7 measured lines) ⚠ toxic. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.306× (z -10.0, q 5e-21, down in 22 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FKBP9P1-1]] (+0.81, fdr 7e-06, ⚠ same locus), [[OPRD1]] (+0.58, fdr 3e-05), [[FAM83F]] (+0.58, fdr 2e-05), [[RIMBP2]] (+0.56, fdr 3e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[FKBP9P1-1]] → it (grade B ⚠); 3 go from it, the strongest it → [[FKBP9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10753.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.26×** | +5.2 | 1e-04 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +4.5 | 0.002 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.25×** | +3.8 | 0.028 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.45× | +3.4 | 0.11 | 1/9 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.28× | +3.2 | 0.15 | 4/35 (SHP-77, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10753.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.306×** | -10.0 | 5e-21 | 22/28 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.377×** | -8.6 | 2e-15 | 23/35 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.382×** | -8.5 | 4e-15 | 18/33 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.410×** | -7.9 | 6e-13 | 19/28 (SHP-77, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.412×** | -7.8 | 6e-13 | 17/33 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.554×** | -7.3 | 2e-11 | 23/25 (SW480, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.436×** | -7.3 | 2e-11 | 19/30 (SW480, SHP-77, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.546×** | -5.3 | 7e-06 | 16/24 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.552×** | -5.2 | 1e-05 | 13/29 (SW480, H4, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.572×** | -4.9 | 5e-05 | 12/24 (H4, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.691×** | -3.2 | 0.066 | 7/33 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.686×** | -3.2 | 0.073 | 3/32 (HT-29, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10753. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.8 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0636× (z -19.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0731× (z -12.5) |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0521× (z -15.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0356× (z -12.0) |
| [[KATO III (line)]] | alt | 4.55 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -10.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0437× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 12.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0407× (z -13.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0163× (z -11.9) |
| [[H4 (line)]] | wt | 19.8 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0377× (z -10.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0876× (z -10.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 7.36 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0650× (z -13.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LoVo (line)]] | wt | 2.85 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0689× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 5.20 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0549× (z -8.6) |
| [[A-172 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.948 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.885 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.808 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.566 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.872 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.864 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.796 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.992 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.844 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.770 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.885 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.819 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10753), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP9P1-1]] | +0.81 | +0.84 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[OPRD1]] | +0.58 | +0.46 / +0.53 | both halves | 3e-05 | **novel candidate** |
| [[FAM83F]] | +0.58 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[RIMBP2]] | +0.56 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[VWA2]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[INPP5D]] | +0.54 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[GJB1]] | +0.53 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[ST18]] | +0.53 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[LINC03040]] | +0.52 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[CACNA2D4]] | +0.51 | +0.45 / +0.38 | both halves | 6e-05 |  |
| [[MIR3667HG]] | +0.51 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[PCSK1]] | +0.51 | +0.56 / +0.31 | both halves | 2e-04 |  |
| [[PSG1]] | +0.51 | +0.31 / +0.35 | both halves | 2e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP9P1-1]] | B | FKBP9P1-1 activity raises FKBP9P1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.78× lower at baseline in the lines without FKBP9P1-1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[LINC03040]] | B | LINC03040 activity raises FKBP9P1's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 1.86× lower at baseline in the lines without LINC03040 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[CFI]] | B | CFI activity raises FKBP9P1's level | lines that do not express CFI (31) vs lines expressing it (19) | 1.59× lower at baseline in the lines without CFI | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[PKHD1]] | B | PKHD1 activity raises FKBP9P1's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 2.04× lower at baseline in the lines without PKHD1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[FAM83F]] | B | FAM83F activity raises FKBP9P1's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 1.84× lower at baseline in the lines without FAM83F | 0.016 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B |
| [[LINC02050]] | B | LINC02050 activity raises FKBP9P1's level | lines that do not express LINC02050 (37) vs lines expressing it (13) | 1.76× lower at baseline in the lines without LINC02050 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000286329, ENSG00000242828, PASD1 |
| [[BLACAT1]] | B | BLACAT1 activity raises FKBP9P1's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without BLACAT1 | 0.043 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[RNF128]] | B | RNF128 activity raises FKBP9P1's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 1.50× lower at baseline in the lines without RNF128 | 0.049 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |
| [[GPX2]] | B | GPX2 activity raises FKBP9P1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 1.55× lower at baseline in the lines without GPX2 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[INPP5D]] | B | INPP5D activity raises FKBP9P1's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 1.56× lower at baseline in the lines without INPP5D | 0.055 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |
| [[TPRXL]] | B | TPRXL activity raises FKBP9P1's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 1.94× lower at baseline in the lines without TPRXL | 0.061 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent |
| [[MIR3667HG]] | B | MIR3667HG activity raises FKBP9P1's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 1.93× lower at baseline in the lines without MIR3667HG | 0.061 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP9]] | B | FKBP9P1 activity raises FKBP9's level | lines that do not express FKBP9P1 (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without FKBP9P1 | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC01814]] | B | FKBP9P1 activity raises LINC01814's level | lines that do not express FKBP9P1 (10) vs lines expressing it (40) | 3.06× lower at baseline in the lines without FKBP9P1 | 0.087 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMPRSS3]] | B | FKBP9P1 activity raises TMPRSS3's level | lines that do not express FKBP9P1 (10) vs lines expressing it (40) | 2.44× lower at baseline in the lines without FKBP9P1 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.496). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.8, 42.0); signed map (64.9, 16.7). **Vector** length 50.3, 8.89% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +4.3 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | -0.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.5 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -10.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -0.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -0.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | FKBP prolyl isomerase 9 pseudogene 1 |
| Locus type | pseudogene |
| Location | 7p11.2 — chr7:55,682,652-55,713,252 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | MGC20531; previously FKBP9L |
| Matched by | ensembl_id |

UniProt [Q75LS8](https://www.uniprot.org/uniprotkb/Q75LS8) carries no function annotation.

**Summary**, from NCBI Gene [360132](https://www.ncbi.nlm.nih.gov/gene/360132):

> Predicted to enable calcium ion binding activity and peptidyl-prolyl cis-trans isomerase activity. Predicted to be located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23568) · Entrez [360132](https://www.ncbi.nlm.nih.gov/gene/360132) · UniProt [Q75LS8](https://www.uniprot.org/uniprotkb/Q75LS8) · Ensembl [ENSG00000176826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176826)

## Data

Gene col 10753: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10753); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10753, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10753]; `tensor/DDL_lfc|DDL_z.npy` [10753]; `embed/gene_vectors.npy` [10753]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10753 or target_col == 10753). Every well: [[FKBP9P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP9P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
