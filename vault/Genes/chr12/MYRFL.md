---
symbol: "MYRFL"
type: "gene"
col: 9274
ensembl_id: "ENSG00000166268"
name: "myelin regulatory factor like"
location: "12q15"
module: 39
arm: "+"
pooled_cpm: 12.66
n_lines_expressing: 36
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 16
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# MYRFL

*myelin regulatory factor like* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.71× (z +14.2, q 9e-43, up in 22 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.298× (z -6.4, q 1e-07, down in 20 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IMPA1P1]] (+0.76, fdr 7e-06), [[LINC01191]] (+0.73, fdr 7e-06), [[BTG3-AS1]] (+0.71, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC01277]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9274.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +14.2 | 9e-43 | 22/29 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.11×** | +10.6 | 6e-24 | 25/33 (SW480, BT-474, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +10.0 | 2e-21 | 22/30 (LOX-IMVI, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +9.2 | 8e-18 | 21/29 (LS 180, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +8.9 | 7e-17 | 18/29 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +8.2 | 3e-14 | 21/34 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.20×** | +7.9 | 2e-13 | 21/33 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +6.9 | 4e-10 | 16/33 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.93×** | +6.6 | 3e-09 | 13/33 (NCI-H23, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +5.9 | 2e-07 | 3/15 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +5.9 | 2e-07 | 1/12 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +5.5 | 2e-06 | 10/29 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +5.3 | 4e-06 | 3/20 (AsPC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +5.2 | 6e-06 | 11/33 (NCI-H23, CHP-212, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +4.1 | 0.002 | 13/34 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.002 | 7/34 (SW1417, Panc 03.27, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.005 | 9/34 (SW 900, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.054 | 7/34 (A-427, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9274.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.298×** | -6.4 | 1e-07 | 20/29 (KATO III, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.602×** | -5.1 | 8e-05 | 18/33 (NCI-H1573, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.649×** | -4.3 | 0.003 | 15/32 (SW480, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -3.7 | 0.027 | 7/34 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.690×** | -3.6 | 0.033 | 10/32 (A-427, HCT15, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.703×** | -3.6 | 0.033 | 7/34 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.706×** | -3.5 | 0.034 | 16/31 (KATO III, NCI-H1573, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.521×** | -3.4 | 0.041 | 13/31 (KATO III, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.525×** | -3.4 | 0.043 | 11/30 (LOX-IMVI, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ranolazine (drug)]] 5 µM |  | **0.728×** | -3.2 | 0.072 | 4/33 (NCI-H2030, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.730×** | -3.2 | 0.072 | 13/33 (NCI-H2030, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.733×** | -3.1 | 0.077 | 8/34 (RKO, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9274. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 146 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0794× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -11.3) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.147× (z -9.9) |
| [[KATO III (line)]] | alt | 36.9 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -13.2) ⚠ cell-cycle shift, explains ~58% of this change |
| [[LoVo (line)]] | wt | 8.84 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 30.5× (z +13.5) | — |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -9.0) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A549 (line)]] | wt | 5.53 | 0 | 1 | — | [[Pemetrexed (drug)]] 0.5 µM 0.0685× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0815× (z -16.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 13.3 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.103× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0994× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 6.16 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0457× (z -9.5) |
| [[A-172 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9274), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMPA1P1]] | +0.76 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.73 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[BTG3-AS1]] | +0.71 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.70 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[GABRR2]] | +0.69 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[SLC6A13]] | +0.67 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[C3orf20]] | +0.66 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[LINC01031]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[HSD17B3]] | +0.66 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[USP50]] | +0.65 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[CORIN]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYRFL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TTC6]] | B | TTC6 activity raises MYRFL's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 2.68× lower at baseline in the lines without TTC6 | 0.037 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[LMO7DN]] | B | LMO7DN activity raises MYRFL's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 2.04× lower at baseline in the lines without LMO7DN | 0.039 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[LINC02147]] | B | LINC02147 activity raises MYRFL's level | lines that do not express LINC02147 (26) vs lines expressing it (24) | 2.27× lower at baseline in the lines without LINC02147 | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC00992, PROX1-AS1, MOGAT3; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01277]] | B | MYRFL activity raises LINC01277's level | lines that do not express MYRFL (14) vs lines expressing it (36) | 1.83× lower at baseline in the lines without MYRFL | 0.040 | ⚠ within organs, on part of the lines; also absent: ENPP4, ATP8A1, SLC27A2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.3, -12.6); signed map (18.3, 7.1). **Vector** length 67.6, 12.5% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.1 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | +5.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +9.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +2.5 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.6 | -6.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.1 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.9 | +5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.6 | +6.9 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | myelin regulatory factor like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:69,825,227-69,959,097 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25056, bcm1377; previously C12orf15, C12orf28 |
| Matched by | ensembl_id |

UniProt [Q96LU7](https://www.uniprot.org/uniprotkb/Q96LU7) carries no function annotation.

**Summary**, from NCBI Gene [196446](https://www.ncbi.nlm.nih.gov/gene/196446):

> Predicted to enable DNA-binding transcription factor activity and sequence-specific DNA binding activity. Predicted to be involved in positive regulation of DNA-templated transcription and protein autoprocessing. Predicted to be located in membrane. Predicted to be active in endoplasmic reticulum membrane and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26316) · Entrez [196446](https://www.ncbi.nlm.nih.gov/gene/196446) · UniProt [Q96LU7](https://www.uniprot.org/uniprotkb/Q96LU7) · Ensembl [ENSG00000166268](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166268)

## Data

Gene col 9274: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9274); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9274, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9274]; `tensor/DDL_lfc|DDL_z.npy` [9274]; `embed/gene_vectors.npy` [9274]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9274 or target_col == 9274). Every well: [[MYRFL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYRFL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
