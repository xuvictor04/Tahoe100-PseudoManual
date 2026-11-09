---
symbol: "MIR3681HG"
type: "gene"
col: 13384
ensembl_id: "ENSG00000224184"
name: "MIR3681 host gene"
location: "2p24.3"
module: 87
arm: "+"
pooled_cpm: 28.7
n_lines_expressing: 23
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 37
direction_downstream: 25
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# MIR3681HG

*MIR3681 host gene* — 2p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.06× (z +19.6, q 0e+00, up in 8 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.752× (z -4.9, q 5e-04, down in 11 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL19A1]] (+0.76, fdr 7e-06), [[SAMMSON]] (+0.75, fdr 7e-06), [[C10orf90]] (+0.73, fdr 7e-06).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[LEF1]] → it (grade B ⚠); 25 go from it, the strongest it → [[TRIB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13384.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.06×** | +19.6 | 0e+00 | 8/19 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.38×** | +15.1 | 0e+00 | 9/21 (HOP62, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.21×** | +13.9 | 1e-41 | 16/21 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +12.2 | 6e-32 | 10/16 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +11.6 | 3e-29 | 10/18 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.96×** | +8.3 | 7e-15 | 5/20 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +7.2 | 5e-11 | 15/20 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +7.1 | 8e-11 | 4/21 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +5.3 | 6e-06 | 9/19 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.3 | 9e-04 | 3/11 (HOP62, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.003 | 1/20 (HOP62) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.020 | 0/19 | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.077 | 2/20 (HOP62, HS-578T) | top dose only | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13384.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.752×** | -4.9 | 5e-04 | 11/21 (AN3 CA, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.690×** | -4.2 | 0.007 | 5/21 (C32, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.719×** | -4.0 | 0.015 | 10/22 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.762× | -3.3 | 0.12 | 11/19 (C32, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.829× | -3.2 | 0.12 | 9/21 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.798× | -3.2 | 0.12 | 7/21 (MIA PaCa-2, C32, …) | two highest doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.771× | -3.2 | 0.12 | 9/21 (C32, AN3 CA, …) | rises with dose |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.781× | -3.0 | 0.16 | 4/21 (HOP62, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13384. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 576 | 0 | 29 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0423× (z -32.2) |
| [[MIA PaCa-2 (line)]] | alt | 24.6 | 0 | 6 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.323× (z -17.3) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.148× (z -9.6) |
| [[AN3 CA (line)]] | alt | 298 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0316× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0773× (z -11.5) |
| [[HS-578T (line)]] | alt | 20.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.82× (z +12.8) | — |
| [[A-172 (line)]] | wt | 14.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.97× (z +10.4) | — |
| [[H4 (line)]] | wt | 21.4 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0541× (z -10.3) |
| [[HOP62 (line)]] | alt | 13.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.61× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Artesunate (drug)]] 5 µM 0.229× (z -9.4) ⚠ cell-cycle shift, explains ~17% of this change |
| [[SK-MEL-2 (line)]] | alt | 204 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 199 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0266× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.64 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.77 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.68 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.55 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1,371 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.45 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.78 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.68 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.00 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.37 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.61 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.89 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13384), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL19A1]] | +0.76 | +0.70 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SAMMSON]] | +0.75 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[C10orf90]] | +0.73 | +0.66 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[LEF1-AS1]] | +0.72 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[CD96]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[A2M]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SOX10]] | +0.66 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[EFR3B]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TRPM8]] | +0.64 | +0.48 / +0.67 | both halves | 2e-05 | **novel candidate** |
| [[DIRC3]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[LOXL3]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[FCRLA]] | +0.64 | +0.61 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 7, C 30. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LEF1]] | B | LEF1 activity raises MIR3681HG's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 2.72× lower at baseline in the lines without LEF1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |
| [[CTTNBP2]] | B | CTTNBP2 activity raises MIR3681HG's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 2.33× lower at baseline in the lines without CTTNBP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR |
| [[NYAP2]] | B | NYAP2 activity raises MIR3681HG's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 3.23× lower at baseline in the lines without NYAP2 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[LOXL3]] | B | LOXL3 activity raises MIR3681HG's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.97× lower at baseline in the lines without LOXL3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MIR3681HG's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SYTL5]] | B | SYTL5 activity raises MIR3681HG's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 2.40× lower at baseline in the lines without SYTL5 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[TRIB2]] | B | TRIB2 activity raises MIR3681HG's level | lines that do not express TRIB2 (10) vs lines expressing it (40) | 3.05× lower at baseline in the lines without TRIB2 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[AEBP1]] | C | AEBP1 activity raises MIR3681HG's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 12.64× lower at baseline in the lines without AEBP1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[A2M]] | C | A2M activity raises MIR3681HG's level | lines that do not express A2M (42) vs lines expressing it (8) | 10.22× lower at baseline in the lines without A2M | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[TYR]] | C | TYR activity raises MIR3681HG's level | lines that do not express TYR (43) vs lines expressing it (7) | 15.32× lower at baseline in the lines without TYR | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises MIR3681HG's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 5.64× lower at baseline in the lines without EDNRB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises MIR3681HG's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 15.88× lower at baseline in the lines without LHFPL3-AS1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 10, C 15. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIB2]] | B | MIR3681HG activity raises TRIB2's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 4.04× lower at baseline in the lines without MIR3681HG | 3e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[CNIH3]] | B | MIR3681HG activity raises CNIH3's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 3.11× lower at baseline in the lines without MIR3681HG | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[GRIA4]] | B | MIR3681HG activity raises GRIA4's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 1.89× lower at baseline in the lines without MIR3681HG | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[CNIH3]] | B | MIR3681HG activity weakens CNIH3's drug response | lines that do not express MIR3681HG (17) vs lines expressing it (19) | the lines without MIR3681HG respond 1.39× as strongly (z diff -0.63); strongest at Idarubicin (hydrochloride) 5 µM: 4.45x vs 1.84x (z diff -5.1) | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[MILR1]] | B | MIR3681HG activity raises MILR1's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without MIR3681HG | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[PARVG]] | B | MIR3681HG activity raises PARVG's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 1.65× lower at baseline in the lines without MIR3681HG | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[SORCS1]] | B | MIR3681HG activity raises SORCS1's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 2.24× lower at baseline in the lines without MIR3681HG | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[TNC]] | B | MIR3681HG activity raises TNC's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 2.95× lower at baseline in the lines without MIR3681HG | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[SETBP1]] | B | MIR3681HG activity raises SETBP1's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 4.16× lower at baseline in the lines without MIR3681HG | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[FZD1]] | B | MIR3681HG activity raises FZD1's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 1.67× lower at baseline in the lines without MIR3681HG | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[DOCK2]] | C | MIR3681HG activity raises DOCK2's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 2.18× lower at baseline in the lines without MIR3681HG | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent; co-absent with the target |
| [[TIMP3]] | C | MIR3681HG activity raises TIMP3's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 6.48× lower at baseline in the lines without MIR3681HG | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.840). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.8, 28.6); signed map (29.0, 39.1). **Vector** length 67.9, 19.1% of its response variance represented; |z| ≥ 3 in 527 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +19.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +13.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.5 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -4.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | MIR3681 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p24.3 — chr2:11,833,926-12,702,913 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52001) · Entrez [100506457](https://www.ncbi.nlm.nih.gov/gene/100506457) · Ensembl [ENSG00000224184](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224184)

## Data

Gene col 13384: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13384); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13384, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13384]; `tensor/DDL_lfc|DDL_z.npy` [13384]; `embed/gene_vectors.npy` [13384]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13384 or target_col == 13384). Every well: [[MIR3681HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR3681HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
