---
symbol: "KCNJ6"
type: "gene"
col: 8082
ensembl_id: "ENSG00000157542"
name: "potassium inwardly rectifying channel subfamily J member 6"
location: "21q22.13"
module: 19
arm: "+"
pooled_cpm: 9.36
n_lines_expressing: 27
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 16
direction_downstream: 11
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# KCNJ6

*potassium inwardly rectifying channel subfamily J member 6* — 21q22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.95× (z +17.7, q 0e+00, up in 13 of 23 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.324×, H4 0.101×, A549 0.217×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.189×, SK-MEL-2 0.232×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.0961×; ⚠ toxic; transcription drop); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (AN3 CA 0.0854×); [[Thymol (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0801×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCDH15]] (+0.73, fdr 7e-06), [[MARCHF1]] (+0.71, fdr 7e-06), [[KCNMB2]] (+0.70, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 11 go from it, the strongest it → [[PDE4D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8082.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.95×** | +17.7 | 0e+00 | 13/23 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.51×** | +13.9 | 1e-41 | 3/11 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +12.8 | 3e-35 | 6/19 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +11.7 | 2e-29 | 18/24 (C32, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +7.6 | 4e-12 | 3/12 (CFPAC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +7.4 | 1e-11 | 7/21 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.84×** | +7.0 | 2e-10 | 15/23 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.80×** | +6.8 | 8e-10 | 9/24 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.7 | 6e-07 | 5/21 (SK-MEL-2, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +4.6 | 3e-04 | 6/23 (A-172, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.3 | 8e-04 | 6/21 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +4.2 | 0.001 | 2/7 (A-172, NCI-H460) | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.55×** | +3.6 | 0.014 | 0/14 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +3.6 | 0.015 | 11/24 (NCI-H2030, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +3.5 | 0.015 | 15/24 (SK-MEL-2, NCI-H1573, …) | all doses, flat |  |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.031 | 2/23 (NCI-H2030, NCI-H661) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.050 | 3/24 (NCI-H661, AN3 CA, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8082.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.324×, H4 0.101×, A549 0.217×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.189×, SK-MEL-2 0.232×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.0961×; ⚠ toxic; transcription drop); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (AN3 CA 0.0854×); [[Thymol (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0801×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Phenytoin (sodium) (drug)]] 0.5 µM |  | 0.748× | -3.4 | 0.30 | 3/24 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.737× | -3.3 | 0.30 | 3/24 (RPMI-7951, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8082. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 242 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0961× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 60.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -9.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -9.6) |
| [[AN3 CA (line)]] | alt | 39.5 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0854× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 3.33 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0801× (z -8.5) |
| [[H4 (line)]] | wt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.102× (z -8.8) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 6.83 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0799× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.117× (z -11.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8082), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCDH15]] | +0.73 | +0.62 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[MARCHF1]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[KCNMB2]] | +0.70 | +0.55 / +0.76 | both halves | 1e-05 | pathway: Neuronal System |
| [[ASXL3]] | +0.70 | +0.53 / +0.75 | both halves | 1e-05 | **novel candidate** |
| [[RIMS1]] | +0.69 | +0.58 / +0.71 | both halves | 8e-06 | pathway: Neuronal System |
| [[NKAIN2]] | +0.68 | +0.59 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[RAB3C]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[LSAMP]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[ADGRL3]] | +0.65 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[LINC01035]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[IQCM]] | +0.64 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[COL4A6]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 1, C 15. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KCNJ6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02506]] | C | LINC02506 activity raises KCNJ6's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 3.84× lower at baseline in the lines without LINC02506 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises KCNJ6's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 6.33× lower at baseline in the lines without SRRM4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[ENPP2]] | C | ENPP2 activity raises KCNJ6's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.61× lower at baseline in the lines without ENPP2 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |
| [[CCDC144NL-AS1]] | C | CCDC144NL-AS1 activity raises KCNJ6's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.68× lower at baseline in the lines without CCDC144NL-AS1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[LRP2]] | C | LRP2 activity raises KCNJ6's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 2.75× lower at baseline in the lines without LRP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent; co-absent with the target |
| [[GAP43]] | C | GAP43 activity raises KCNJ6's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 2.57× lower at baseline in the lines without GAP43 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent; co-absent with the target |
| [[FSTL5]] | C | FSTL5 activity raises KCNJ6's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 2.56× lower at baseline in the lines without FSTL5 | 0.063 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[LAMB4]] | C | LAMB4 activity raises KCNJ6's level | lines that do not express LAMB4 (26) vs lines expressing it (24) | 2.67× lower at baseline in the lines without LAMB4 | 0.064 | ⚠ within organs, on part of the lines; also absent: NRCAM, MEIOB, SOX2; maybe low, not absent; co-absent with the target |
| [[MARCHF1]] | C | MARCHF1 activity raises KCNJ6's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 2.78× lower at baseline in the lines without MARCHF1 | 0.070 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[CALCA]] | C | CALCA activity raises KCNJ6's level | lines that do not express CALCA (45) vs lines expressing it (5) | 6.43× lower at baseline in the lines without CALCA | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises KCNJ6's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.46× lower at baseline in the lines without DPP10 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE4D]] | B | KCNJ6 activity raises PDE4D's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without KCNJ6 | 0.091 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent |
| [[SORCS3]] | B | KCNJ6 activity raises SORCS3's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 1.38× lower at baseline in the lines without KCNJ6 | 0.097 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent |
| [[PCBP3]] | C | KCNJ6 activity raises PCBP3's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 4.15× lower at baseline in the lines without KCNJ6 | 0.016 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |
| [[LRP2]] | C | KCNJ6 activity raises LRP2's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 2.11× lower at baseline in the lines without KCNJ6 | 0.016 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |
| [[AUTS2]] | C | KCNJ6 activity raises AUTS2's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 3.70× lower at baseline in the lines without KCNJ6 | 0.018 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |
| [[SNAP25]] | C | KCNJ6 activity raises SNAP25's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 5.01× lower at baseline in the lines without KCNJ6 | 0.021 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |
| [[PALMD]] | C | KCNJ6 activity raises PALMD's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 1.96× lower at baseline in the lines without KCNJ6 | 0.043 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |
| [[NOVA1]] | C | KCNJ6 activity raises NOVA1's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 4.41× lower at baseline in the lines without KCNJ6 | 0.049 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |
| [[SCUBE1]] | C | KCNJ6 activity raises SCUBE1's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 2.60× lower at baseline in the lines without KCNJ6 | 0.079 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |
| [[COL4A5]] | C | KCNJ6 activity raises COL4A5's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 3.72× lower at baseline in the lines without KCNJ6 | 0.092 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |
| [[PDE7B]] | C | KCNJ6 activity raises PDE7B's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 2.31× lower at baseline in the lines without KCNJ6 | 0.092 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.9, 34.4); signed map (42.0, 38.4). **Vector** length 42.8, 7.53% of its response variance represented; |z| ≥ 3 in 554 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +13.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +17.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +11.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.1 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -1.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.8 | -1.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.6 | -1.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | potassium inwardly rectifying channel subfamily J member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.13 — chr21:37,607,373-38,121,345 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Kir3.2, GIRK2, KATP2, BIR1, hiGIRK2; previously KCNJ7 |
| Gene groups (HGNC) | Potassium inwardly rectifying channel subfamily J |
| Reactome | 11 pathways, smallest: Activation of G protein gated Potassium channels; G protein gated Potassium channels; Inhibition  of voltage gated Ca2+ channels via Gbeta/gamma subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [P48051](https://www.uniprot.org/uniprotkb/P48051) (G protein-activated inward rectifier potassium channel 2):

> Inward rectifier potassium channels are characterized by a greater tendency to allow potassium to flow into the cell rather than out of it. Their voltage dependence is regulated by the concentration of extracellular potassium; as external potassium is raised, the voltage range of the channel opening shifts to more positive voltages. The inward rectification is mainly due to the blockage of outward current by internal magnesium. This potassium channel may be involved in the regulation of insulin …

**Summary**, from NCBI Gene [3763](https://www.ncbi.nlm.nih.gov/gene/3763):

> This gene encodes a member of the G protein-coupled inwardly-rectifying potassium channel family of inward rectifier potassium channels. This type of potassium channel allows a greater flow of potassium into the cell than out of it. These proteins modulate many physiological processes, including heart rate in cardiac cells and circuit activity in neuronal cells, through G-protein coupled receptor stimulation. Mutations in this gene are associated with Keppen-Lubinsky Syndrome, a rare condition …

**Accessions** — [HGNC:6267](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6267) · Entrez [3763](https://www.ncbi.nlm.nih.gov/gene/3763) · UniProt [P48051](https://www.uniprot.org/uniprotkb/P48051) · Ensembl [ENSG00000157542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157542)

## Data

Gene col 8082: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8082); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8082, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8082]; `tensor/DDL_lfc|DDL_z.npy` [8082]; `embed/gene_vectors.npy` [8082]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8082 or target_col == 8082). Every well: [[KCNJ6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNJ6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
