---
symbol: "KCNH8"
type: "gene"
col: 11475
ensembl_id: "ENSG00000183960"
name: "potassium voltage-gated channel subfamily H member 8"
location: "3p24.3"
module: 55
arm: "+"
pooled_cpm: 48.08
n_lines_expressing: 18
n_dd_up: 8
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 38
direction_downstream: 48
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# KCNH8

*potassium voltage-gated channel subfamily H member 8* — 3p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.58× (z +7.1, q 1e-09, up in 8 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.554× (z -5.9, q 2e-06, down in 7 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VWA2]] (+0.75, fdr 7e-06), [[SKAP1]] (+0.74, fdr 7e-06), [[EDAR]] (+0.73, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[SLC30A10]] → it (grade B ⚠); 48 go from it, the strongest it → [[TJP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11475.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +7.1 | 1e-09 | 8/16 (C32, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.0 | 4e-07 | 1/15 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.0 | 4e-07 | 3/15 (HT-29, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +5.9 | 5e-07 | 3/11 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.0 | 5e-05 | 6/16 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +4.1 | 0.004 | 2/13 (C32, HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.8 | 0.011 | 0/16 | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.25×** | +3.5 | 0.039 | 3/16 (SK-MEL-2, NCI-H1573, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.34× | +3.1 | 0.12 | 7/16 (NCI-H1573, SK-MEL-2, …) | top dose only | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11475.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.554×** | -5.9 | 2e-06 | 7/16 (SW480, COLO 205, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.596×** | -5.6 | 5e-06 | 10/16 (SW480, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.715×** | -4.9 | 1e-04 | 6/16 (SW480, CHP-212, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.637×** | -4.9 | 1e-04 | 11/16 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.672×** | -4.5 | 7e-04 | 11/17 (NCI-H596, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.657×** | -4.3 | 0.001 | 8/16 (SW48, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.706×** | -4.3 | 0.001 | 11/16 (SW480, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.679×** | -4.2 | 0.002 | 6/16 (SW480, SW 1271, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.765×** | -4.1 | 0.003 | 14/16 (HT-29, SW1417, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.688×** | -4.1 | 0.003 | 8/16 (SK-MEL-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.690×** | -3.9 | 0.006 | 5/16 (Panc 03.27, SK-MEL-2, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.693×** | -3.8 | 0.006 | 9/16 (SW480, COLO 205, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.779×** | -3.8 | 0.006 | 10/16 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.711×** | -3.7 | 0.009 | 10/16 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.728×** | -3.4 | 0.022 | 7/16 (SW480, SW48, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.779×** | -3.4 | 0.024 | 7/16 (SW480, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 298 | 0 | 15 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -14.1) |
| [[LoVo (line)]] | wt | 195 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -11.7) |
| [[SHP-77 (line)]] | alt | 89.4 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.296× (z -10.1) |
| [[SW1417 (line)]] | alt | 522 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -11.1) |
| [[SW48 (line)]] | wt | 197 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0802× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 23.3 | 3 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 14.8× (z +14.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[C32 (line)]] | wt | 17.0 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 9.58× (z +8.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[COLO 205 (line)]] | alt | 131 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -9.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SK-MEL-2 (line)]] | alt | 56.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +14.3) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[HCT15 (line)]] | alt | 55.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 64.9 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.292× (z -9.0) |
| [[A-172 (line)]] | wt | 8.52 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.72 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.61 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.20 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.66 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.98 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.70 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.62 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VWA2]] | +0.75 | +0.74 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SKAP1]] | +0.74 | +0.72 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[EDAR]] | +0.73 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[IGFL4]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ZBTB7C]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[BMP4]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[B3GNT3]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[SLC52A3]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[INPP5D]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[AFAP1L2]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PROX1]] | +0.66 | +0.56 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 2, C 36. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC30A10]] | B | SLC30A10 activity raises KCNH8's level | lines that do not express SLC30A10 (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without SLC30A10 | 0.054 | ⚠ within organs, on part of the lines; also absent: PKHD1, LINC00698, LINC02147; maybe low, not absent |
| [[ZNF860]] | B | ZNF860 activity raises KCNH8's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.36× lower at baseline in the lines without ZNF860 | 0.055 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[INPP5D]] | C | INPP5D activity raises KCNH8's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 5.01× lower at baseline in the lines without INPP5D | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5; co-absent with the target |
| [[RBP1]] | C | RBP1 activity raises KCNH8's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 3.10× lower at baseline in the lines without RBP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5; co-absent with the target |
| [[TNNT2]] | C | TNNT2 activity raises KCNH8's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 3.38× lower at baseline in the lines without TNNT2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14; co-absent with the target |
| [[LINC02832]] | C | LINC02832 activity raises KCNH8's level | lines that do not express LINC02832 (26) vs lines expressing it (24) | 3.31× lower at baseline in the lines without LINC02832 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000235337, ENSG00000288902, ENSG00000239498; co-absent with the target |
| [[SYK]] | C | SYK activity raises KCNH8's level | lines that do not express SYK (30) vs lines expressing it (20) | 4.32× lower at baseline in the lines without SYK | 0.005 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14; co-absent with the target |
| [[VWA2]] | C | VWA2 activity raises KCNH8's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 6.12× lower at baseline in the lines without VWA2 | 0.005 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1; co-absent with the target |
| [[LAD1]] | C | LAD1 activity raises KCNH8's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 4.06× lower at baseline in the lines without LAD1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1; co-absent with the target |
| [[KIAA0040]] | C | KIAA0040 activity raises KCNH8's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 3.55× lower at baseline in the lines without KIAA0040 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1; co-absent with the target |
| [[C1orf116]] | C | C1orf116 activity raises KCNH8's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 3.58× lower at baseline in the lines without C1orf116 | 0.011 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[ZNF503-AS1]] | C | ZNF503-AS1 activity raises KCNH8's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 3.43× lower at baseline in the lines without ZNF503-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 15, C 33. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TJP2]] | B | KCNH8 activity raises TJP2's level | lines that do not express KCNH8 (32) vs lines expressing it (18) | 2.43× lower at baseline in the lines without KCNH8 | 0.004 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| [[SLC12A2]] | B | KCNH8 activity raises SLC12A2's level | lines that do not express KCNH8 (32) vs lines expressing it (18) | 2.46× lower at baseline in the lines without KCNH8 | 0.004 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| [[TMC6]] | B | KCNH8 activity raises TMC6's level | lines that do not express KCNH8 (32) vs lines expressing it (18) | 3.33× lower at baseline in the lines without KCNH8 | 0.009 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| cells under [[Mifepristone (drug)]] 0.5 µM | B | KCNH8 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express KCNH8 (32) vs lines expressing it (16) | the lines without KCNH8: 1.21× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| [[KRT18]] | B | KCNH8 activity raises KRT18's level | lines that do not express KCNH8 (32) vs lines expressing it (18) | 2.66× lower at baseline in the lines without KCNH8 | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| cells under [[Doxycycline (monohydrate) (drug)]] 5 µM | B | KCNH8 activity raises the cells' numbers under Doxycycline (monohydrate) 5 µM (protects the cells) | lines that do not express KCNH8 (32) vs lines expressing it (16) | the lines without KCNH8: 0.74× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| [[ITPKC]] | B | KCNH8 activity raises ITPKC's level | lines that do not express KCNH8 (32) vs lines expressing it (18) | 2.19× lower at baseline in the lines without KCNH8 | 0.066 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | KCNH8 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express KCNH8 (32) vs lines expressing it (16) | the lines without KCNH8: 1.16× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| cells under [[Procainamide (hydrochloride) (drug)]] 0.5 µM | B | KCNH8 activity raises the cells' numbers under Procainamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KCNH8 (32) vs lines expressing it (16) | the lines without KCNH8: 0.82× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| cells under [[Neratinib (maleate) (drug)]] 0.05 µM | B | KCNH8 activity lowers the cells' numbers under Neratinib (maleate) 0.05 µM (makes them more sensitive) | lines that do not express KCNH8 (32) vs lines expressing it (16) | the lines without KCNH8: 1.19× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| cells under [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | B | KCNH8 activity raises the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KCNH8 (32) vs lines expressing it (16) | the lines without KCNH8: 0.83× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| cells under [[Omeprazole (drug)]] 5 µM | B | KCNH8 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express KCNH8 (32) vs lines expressing it (16) | the lines without KCNH8: 1.12× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.0, 46.9); signed map (64.1, 11.7). **Vector** length 78.6, 30.1% of its response variance represented; |z| ≥ 3 in 462 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.4 | +2.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -3.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.3 | -4.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.2 | -2.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.2 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily H member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.3 — chr3:19,148,510-19,535,642 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Kv12.1, elk3 |
| Gene groups (HGNC) | Potassium voltage-gated channels; PAS domain containing |
| Reactome | 3 pathways, smallest: Voltage gated Potassium channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96L42](https://www.uniprot.org/uniprotkb/Q96L42) (Voltage-gated delayed rectifier potassium channel KCNH8):

> Pore-forming (alpha) subunit of a voltage-gated delayed rectifier potassium channel that mediates outward-rectifying potassium currents. Elicits a slowly activating, non-inactivating and slowly deactivation outwards potassium current at depolarizating voltages from -30 mV to +50mV. Shows no obvious change in the activation rate from different holding potentials. Activation is strongly dependent on the pH of the external solution (By similarity).

**Summary**, from NCBI Gene [131096](https://www.ncbi.nlm.nih.gov/gene/131096):

> Voltage-gated potassium (Kv) channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. This gene encodes a member of the potassium channel, voltage-gated, subfamily H. This member is a pore-forming (alpha) subunit. [provided by RefSeq, …

**Accessions** — [HGNC:18864](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18864) · Entrez [131096](https://www.ncbi.nlm.nih.gov/gene/131096) · UniProt [Q96L42](https://www.uniprot.org/uniprotkb/Q96L42) · Ensembl [ENSG00000183960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183960)

## Data

Gene col 11475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11475); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11475]; `tensor/DDL_lfc|DDL_z.npy` [11475]; `embed/gene_vectors.npy` [11475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11475 or target_col == 11475). Every well: [[KCNH8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNH8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
