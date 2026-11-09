---
symbol: "CRYBG2"
type: "gene"
col: 10679
ensembl_id: "ENSG00000176092"
name: "crystallin beta-gamma domain containing 2"
location: "1p36.11"
module: 31
arm: "+"
pooled_cpm: 9.06
n_lines_expressing: 27
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 115
direction_downstream: 150
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# CRYBG2

*crystallin beta-gamma domain containing 2* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.76× (z +8.5, q 1e-14, up in 11 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.644× (z -4.6, q 0.003, down in 14 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA3B]] (+0.77, fdr 7e-06), [[B3GNT3]] (+0.77, fdr 7e-06), [[C1orf116]] (+0.76, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 115 arrows point to it, the strongest [[PCDH1]] → it (grade B ⚠); 150 go from it, the strongest it → [[PARD6B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10679.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +8.5 | 1e-14 | 11/24 (KATO III, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.13×** | +8.0 | 3e-13 | 10/25 (NCI-H2030, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +6.0 | 4e-07 | 12/24 (LS 180, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.45×** | +5.5 | 5e-06 | 9/24 (LS 180, COLO 205, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.59×** | +4.9 | 1e-04 | 10/23 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +4.8 | 1e-04 | 4/25 (NCI-H2030, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +4.3 | 0.001 | 4/24 (NCI-H2030, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.68×** | +3.9 | 0.006 | 6/22 (LS 180, COLO 205, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.96×** | +3.7 | 0.011 | 10/21 (SW480, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +3.6 | 0.015 | 0/12 | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.063 | 2/25 (HCT15, NCI-H23) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.2 | 0.063 | 1/11 (AsPC-1) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.063 | 5/23 (SW480, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.1 | 0.077 | 1/17 (HCT15) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.083 | 9/24 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.100 | 7/25 (COLO 205, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10679.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.644×** | -4.6 | 0.003 | 14/25 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.481×** | -4.1 | 0.011 | 9/24 (HCT15, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.694×** | -4.0 | 0.014 | 15/23 (LoVo, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -3.5 | 0.056 | 15/22 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | 0.763× | -3.1 | 0.19 | 10/26 (CFPAC-1, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM |  | 0.821× | -3.1 | 0.19 | 2/25 (NCI-H661, C-33 A) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.756× | -3.0 | 0.19 | 13/25 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10679. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 25.9 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -16.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0816× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 22.5 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0950× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.0731× (z -11.3) |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0998× (z -10.9) |
| [[SW480 (line)]] | alt | 18.4 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -15.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 41.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0401× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.226× (z -9.6) |
| [[COLO 205 (line)]] | alt | 46.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0344× (z -26.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[LoVo (line)]] | wt | 16.7 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -11.5) |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -15.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0759× (z -13.8) |
| [[KATO III (line)]] | alt | 24.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -13.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H2347 (line)]] | alt | 14.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -17.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 9.72 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0373× (z -10.5) |
| [[A-172 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.957 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.766 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.977 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.911 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.795 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.886 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.23 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10679), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA3B]] | +0.77 | +0.75 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[B3GNT3]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[C1orf116]] | +0.76 | +0.70 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS4]] | +0.74 | +0.72 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[FA2H]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[HS3ST1]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[CDH1]] | +0.71 | +0.60 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[PRSS3]] | +0.71 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L1]] | +0.71 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[DSG3]] | +0.71 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[PADI1]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[TTC9]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*115 arrows, 115 of them with an alert ⚠; grade A 0, B 29, C 86. Shown: the 12 strongest; 103 more arrows (103 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH1]] | B | PCDH1 activity raises CRYBG2's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 3.09× lower at baseline in the lines without PCDH1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[JUP]] | B | JUP activity raises CRYBG2's level | lines that do not express JUP (16) vs lines expressing it (34) | 3.21× lower at baseline in the lines without JUP | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[MYO7B]] | B | MYO7B activity raises CRYBG2's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.52× lower at baseline in the lines without MYO7B | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[LPAR5]] | B | LPAR5 activity raises CRYBG2's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 3.08× lower at baseline in the lines without LPAR5 | 0.014 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[KRT16]] | B | KRT16 activity raises CRYBG2's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 2.69× lower at baseline in the lines without KRT16 | 0.016 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[EPS8L1]] | B | EPS8L1 activity raises CRYBG2's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.78× lower at baseline in the lines without EPS8L1 | 0.017 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[STYK1]] | B | STYK1 activity raises CRYBG2's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 2.91× lower at baseline in the lines without STYK1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[MYO1D]] | B | MYO1D activity raises CRYBG2's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 2.79× lower at baseline in the lines without MYO1D | 0.018 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[CCDC120]] | B | CCDC120 activity raises CRYBG2's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 3.40× lower at baseline in the lines without CCDC120 | 0.024 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[SEMA3B]] | B | SEMA3B activity raises CRYBG2's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.33× lower at baseline in the lines without SEMA3B | 0.026 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[TMEM92]] | B | TMEM92 activity raises CRYBG2's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 2.55× lower at baseline in the lines without TMEM92 | 0.030 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[CDA]] | B | CDA activity raises CRYBG2's level | lines that do not express CDA (16) vs lines expressing it (34) | 2.85× lower at baseline in the lines without CDA | 0.037 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |

### Downstream of this gene

*150 arrows, 150 of them with an alert ⚠; grade A 0, B 69, C 81. Shown: the 12 strongest; 138 more arrows (138 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARD6B]] | B | CRYBG2 activity raises PARD6B's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 3.48× lower at baseline in the lines without CRYBG2 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[CCDC120]] | B | CRYBG2 activity raises CCDC120's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.86× lower at baseline in the lines without CRYBG2 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[JUP]] | B | CRYBG2 activity raises JUP's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 4.33× lower at baseline in the lines without CRYBG2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[EPS8L1]] | B | CRYBG2 activity raises EPS8L1's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 3.26× lower at baseline in the lines without CRYBG2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[TMC6]] | B | CRYBG2 activity raises TMC6's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 3.51× lower at baseline in the lines without CRYBG2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[ARHGAP27]] | B | CRYBG2 activity raises ARHGAP27's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.40× lower at baseline in the lines without CRYBG2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[PTK2B]] | B | CRYBG2 activity raises PTK2B's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.38× lower at baseline in the lines without CRYBG2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[ACOT11]] | B | CRYBG2 activity raises ACOT11's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.38× lower at baseline in the lines without CRYBG2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[FAM83E]] | B | CRYBG2 activity raises FAM83E's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 3.21× lower at baseline in the lines without CRYBG2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[MYO1D]] | B | CRYBG2 activity raises MYO1D's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 3.32× lower at baseline in the lines without CRYBG2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[UBXN11]] | B | CRYBG2 activity raises UBXN11's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 1.67× lower at baseline in the lines without CRYBG2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[KIAA1522]] | B | CRYBG2 activity raises KIAA1522's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.58× lower at baseline in the lines without CRYBG2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.888). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, 55.3); signed map (-1.0, 38.5). **Vector** length 80.2, 23.6% of its response variance represented; |z| ≥ 3 in 655 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.0 | +8.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +5.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | crystallin beta-gamma domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,321,698-26,360,080 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38020; previously AIM1L |
| Gene groups (HGNC) | Beta-gamma crystallin domain containing |
| Matched by | ensembl_id |

UniProt [Q8N1P7](https://www.uniprot.org/uniprotkb/Q8N1P7) carries no function annotation.

**Summary**, from NCBI Gene [55057](https://www.ncbi.nlm.nih.gov/gene/55057):

> Predicted to enable carbohydrate binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17295) · Entrez [55057](https://www.ncbi.nlm.nih.gov/gene/55057) · UniProt [Q8N1P7](https://www.uniprot.org/uniprotkb/Q8N1P7) · Ensembl [ENSG00000176092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176092)

## Data

Gene col 10679: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10679); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10679, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10679]; `tensor/DDL_lfc|DDL_z.npy` [10679]; `embed/gene_vectors.npy` [10679]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10679 or target_col == 10679). Every well: [[CRYBG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRYBG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
