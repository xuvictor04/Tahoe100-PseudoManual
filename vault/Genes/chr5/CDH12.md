---
symbol: "CDH12"
type: "gene"
col: 7779
ensembl_id: "ENSG00000154162"
name: "cadherin 12"
location: "5p14.3"
module: 9
arm: "+"
pooled_cpm: 21.57
n_lines_expressing: 17
n_dd_up: 25
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 11
direction_downstream: 25
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CDH12

*cadherin 12* — 5p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.97× (z +19.3, q 0e+00, up in 4 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.708× (z -4.4, q 0.007, down in 4 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH10]] (+0.73, fdr 7e-06), [[CDH18]] (+0.72, fdr 7e-06), [[GRIA2]] (+0.71, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[LINC02197]] → it (grade C ⚠); 25 go from it, the strongest it → [[LRRIQ1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7779.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.97×** | +19.3 | 0e+00 | 4/13 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.07×** | +14.0 | 2e-42 | 2/11 (LoVo, A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +13.8 | 2e-41 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +11.5 | 1e-28 | 7/15 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +10.3 | 9e-23 | 9/15 (LoVo, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.04×** | +8.9 | 4e-17 | 4/14 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +8.8 | 1e-16 | 1/10 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +6.5 | 6e-09 | 8/14 (CHP-212, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +5.6 | 2e-06 | 10/14 (HS-578T, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.0 | 4e-05 | 2/13 (NCI-H23, SK-MEL-2) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +4.8 | 7e-05 | 10/14 (LOX-IMVI, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +4.8 | 9e-05 | 6/14 (SK-MEL-2, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.6 | 2e-04 | 4/14 (H4, HS-578T, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.44×** | +4.5 | 2e-04 | 6/14 (NCI-H23, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.44×** | +4.5 | 2e-04 | 3/14 (NCI-H23, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.002 | 9/14 (LOX-IMVI, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.025 | 4/13 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.036 | 5/14 (SHP-77, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.2 | 0.041 | 1/15 (A-172) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.053 | 0/13 | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.064 | 6/13 (A-172, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7779.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.708×** | -4.4 | 0.007 | 4/14 (A-427, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.706×** | -4.2 | 0.007 | 6/13 (SHP-77, H4, …) | rises with dose |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.735×** | -3.7 | 0.046 | 0/13 | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -3.5 | 0.071 | 2/15 (LoVo, SK-MEL-2) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.748×** | -3.4 | 0.076 | 1/14 (NCI-H23) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.767×** | -3.4 | 0.076 | 8/14 (SHP-77, H4, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.755×** | -3.3 | 0.076 | 0/14 | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.773×** | -3.3 | 0.076 | 10/14 (SHP-77, H4, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.774×** | -3.2 | 0.076 | 3/14 (SHP-77, H4, …) | top dose only | position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.763×** | -3.2 | 0.092 | 0/14 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7779. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 263 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -13.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.274× (z -10.7) |
| [[H4 (line)]] | wt | 198 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 16.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0788× (z -12.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 8.24 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +9.9) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.72 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.62 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.03 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.56 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7779), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH10]] | +0.73 | +0.62 / +0.66 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 745 |
| [[CDH18]] | +0.72 | +0.75 / +0.66 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 752 |
| [[GRIA2]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[LINC02506]] | +0.71 | +0.51 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[CSRNP3]] | +0.71 | +0.62 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[CDH8]] | +0.69 | +0.53 / +0.70 | both halves | 1e-05 | same gene group; pathway: Adherens junctions interactions; STRING 893 |
| [[LINC02197]] | +0.69 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[LINC01287]] | +0.68 | +0.58 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[MSR1]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[KCNH7]] | +0.67 | +0.63 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[PEX5L]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[KHDRBS2]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02197]] | C | LINC02197 activity raises CDH12's level | lines that do not express LINC02197 (35) vs lines expressing it (15) | 3.32× lower at baseline in the lines without LINC02197 | 0.004 | ⚠ within organs, on part of the lines; also absent: RIT2, SNTG1, CALCA; maybe low, not absent; co-absent with the target |
| [[TRIM55]] | C | TRIM55 activity raises CDH12's level | lines that do not express TRIM55 (40) vs lines expressing it (10) | 4.35× lower at baseline in the lines without TRIM55 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01425, SIM1; co-absent with the target |
| [[KC6]] | C | KC6 activity raises CDH12's level | lines that do not express KC6 (32) vs lines expressing it (18) | 3.81× lower at baseline in the lines without KC6 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises CDH12's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 5.15× lower at baseline in the lines without NETO1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[CDH18]] | C | CDH18 activity raises CDH12's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 4.32× lower at baseline in the lines without CDH18 | 0.028 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[FAM230C]] | C | FAM230C activity raises CDH12's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 3.36× lower at baseline in the lines without FAM230C | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[TRPC4]] | C | TRPC4 activity raises CDH12's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 3.53× lower at baseline in the lines without TRPC4 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[PCDH18]] | C | PCDH18 activity raises CDH12's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 4.01× lower at baseline in the lines without PCDH18 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |
| [[ZC3H12B]] | C | ZC3H12B activity raises CDH12's level | lines that do not express ZC3H12B (21) vs lines expressing it (29) | 2.42× lower at baseline in the lines without ZC3H12B | 0.047 | ⚠ within organs, on part of the lines; also absent: RUNX3, TMEM132D, LINC01876; co-absent with the target |
| [[IGSF1]] | C | IGSF1 activity raises CDH12's level | lines that do not express IGSF1 (33) vs lines expressing it (17) | 2.61× lower at baseline in the lines without IGSF1 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC01885, ZNF208, ENSG00000233358; co-absent with the target |
| [[LINC01446]] | C | LINC01446 activity raises CDH12's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 3.65× lower at baseline in the lines without LINC01446 | 0.082 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 5, C 20. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRIQ1]] | B | CDH12 activity weakens LRRIQ1's drug response | lines that do not express CDH12 (16) vs lines expressing it (11) | the lines without CDH12 respond 1.27× as strongly (z diff -0.46); strongest at Dinaciclib 0.05 µM: 1.60x vs 0.62x (z diff -4.0) | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NRXN1]] | B | CDH12 activity raises NRXN1's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 2.77× lower at baseline in the lines without CDH12 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent |
| [[MAPK10]] | B | CDH12 activity raises MAPK10's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 2.66× lower at baseline in the lines without CDH12 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent |
| [[LRRIQ1]] | B | CDH12 activity raises LRRIQ1's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 1.95× lower at baseline in the lines without CDH12 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent |
| [[BCL11A]] | B | CDH12 activity raises BCL11A's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 2.74× lower at baseline in the lines without CDH12 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent |
| [[CDH18]] | C | CDH12 activity raises CDH18's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 2.98× lower at baseline in the lines without CDH12 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[ANGPT1]] | C | CDH12 activity raises ANGPT1's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 5.56× lower at baseline in the lines without CDH12 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[MSR1]] | C | CDH12 activity raises MSR1's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 3.85× lower at baseline in the lines without CDH12 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[MAGEA3-DT]] | C | CDH12 activity raises MAGEA3-DT's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 5.51× lower at baseline in the lines without CDH12 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[TCF4]] | C | CDH12 activity raises TCF4's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 5.18× lower at baseline in the lines without CDH12 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[LINC01885]] | C | CDH12 activity raises LINC01885's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 4.67× lower at baseline in the lines without CDH12 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[ADGRL3]] | C | CDH12 activity raises ADGRL3's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 3.19× lower at baseline in the lines without CDH12 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.814). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.3, 32.3); signed map (40.8, 33.7). **Vector** length 45.4, 13.8% of its response variance represented; |z| ≥ 3 in 361 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.54 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +19.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +5.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.6 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.7 | -4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p14.3 — chr5:21,750,673-22,853,344 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Br-cadherin, CDHB |
| Gene groups (HGNC) | Type II classical cadherins |
| Reactome | 4 pathways, smallest: Adherens junctions interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P55289](https://www.uniprot.org/uniprotkb/P55289) (Cadherin-12):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types.

**Summary**, from NCBI Gene [1010](https://www.ncbi.nlm.nih.gov/gene/1010):

> This gene encodes a type II classical cadherin of the cadherin superfamily. Alternative splicing of this gene results in multiple transcript variants. At least one of these variants encodes a preproprotein that is proteolytically processed to generate the mature cadherin protein. These integral membrane proteins mediate calcium-dependent cell-cell adhesion and are composed of a large N-terminal extracellular domain, a single membrane-spanning domain, and a small, highly conserved C-terminal …

**Accessions** — [HGNC:1751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1751) · Entrez [1010](https://www.ncbi.nlm.nih.gov/gene/1010) · UniProt [P55289](https://www.uniprot.org/uniprotkb/P55289) · Ensembl [ENSG00000154162](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154162)

## Data

Gene col 7779: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7779); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7779, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7779]; `tensor/DDL_lfc|DDL_z.npy` [7779]; `embed/gene_vectors.npy` [7779]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7779 or target_col == 7779). Every well: [[CDH12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
