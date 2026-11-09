---
symbol: "PADI1"
type: "gene"
col: 6637
ensembl_id: "ENSG00000142623"
name: "peptidyl arginine deiminase 1"
location: "1p36.13"
module: 31
arm: "+"
pooled_cpm: 15.7
n_lines_expressing: 16
n_dd_up: 6
n_dd_down: 17
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 62
direction_downstream: 106
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PADI1

*peptidyl arginine deiminase 1* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.11× (z +12.0, q 3e-30, up in 3 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Docetaxel (Trihydrate) (drug)]] 0.5 µM: 1.56× (z +3.9, q 0.011, up in 0 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.05 µM: 0.644× (z -5.3, q 7e-05, down in 8 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LCK]] (+0.81, fdr 7e-06), [[B3GNT3]] (+0.80, fdr 7e-06), [[TINAGL1]] (+0.75, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 62 arrows point to it, the strongest [[PRAG1]] → it (grade B ⚠); 106 go from it, the strongest it → [[ANXA11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6637.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.11×** | +12.0 | 3e-30 | 3/10 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.43×** | +10.8 | 6e-25 | 1/11 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.63×** | +7.9 | 7e-13 | 2/10 (HEC-1-A, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.3 | 0.002 | 1/13 (HT-29) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.56×** | +3.9 | 0.011 | 0/13 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.069 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 1.45× | +3.2 | 0.13 | 9/13 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Verteporfin (drug)]] 5 µM |  | 1.44× | +3.1 | 0.15 | 0/13 | rises with dose | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | 1.41× | +3.0 | 0.16 | 3/13 (SW1417, J82, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6637.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **0.644×** | -5.3 | 7e-05 | 8/13 (SW480, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.530×** | -5.2 | 7e-05 | 9/13 (SW480, LS 180, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.547×** | -4.7 | 4e-04 | 9/13 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.589×** | -4.6 | 5e-04 | 11/13 (CFPAC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.602×** | -4.4 | 1e-03 | 10/13 (SNU-423, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.658×** | -4.4 | 0.001 | 10/13 (SW480, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.640×** | -3.9 | 0.008 | 13/13 (COLO 205, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.645×** | -3.8 | 0.009 | 12/13 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.656×** | -3.7 | 0.014 | 11/13 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.661×** | -3.6 | 0.016 | 11/13 (COLO 205, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.748×** | -3.6 | 0.016 | 8/13 (LS 180, COLO 205, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.653×** | -3.6 | 0.016 | 10/13 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.713×** | -3.5 | 0.020 | 9/13 (SW480, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.680×** | -3.4 | 0.030 | 11/13 (CFPAC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.776×** | -3.1 | 0.063 | 1/13 (SNU-423) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6637. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.0 | 0 | 12 (2 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.103× (z -12.1) |
| [[COLO 205 (line)]] | alt | 309 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0688× (z -21.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -16.5) |
| [[LS 180 (line)]] | wt | 24.8 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 202 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0837× (z -15.7) |
| [[HEC-1-A (line)]] | alt | 36.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 35.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -11.8) |
| [[SNU-423 (line)]] | alt | 17.1 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0454× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -9.9) |
| [[J82 (line)]] | alt | 4.65 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0289× (z -12.2) |
| [[SW1417 (line)]] | alt | 8.40 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0442× (z -10.6) |
| [[A-172 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6637), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCK]] | +0.81 | +0.80 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[B3GNT3]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TINAGL1]] | +0.75 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[BLACAT1]] | +0.73 | +0.73 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[LEMD1]] | +0.73 | +0.68 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ITGB4]] | +0.72 | +0.72 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[HS3ST1]] | +0.72 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[CRYBG2]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[GPR35]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[MST1R]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[EPHA2-AS1]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[KLK10]] | +0.67 | +0.71 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 3, C 59. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRAG1]] | B | PRAG1 activity raises PADI1's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 2.74× lower at baseline in the lines without PRAG1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[SDCBP2]] | B | SDCBP2 activity raises PADI1's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 2.74× lower at baseline in the lines without SDCBP2 | 0.074 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[NOSTRIN]] | B | NOSTRIN activity raises PADI1's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.26× lower at baseline in the lines without NOSTRIN | 0.087 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[CARD11]] | C | CARD11 activity raises PADI1's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 3.47× lower at baseline in the lines without CARD11 | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises PADI1's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 4.47× lower at baseline in the lines without ATP2C2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[SKAP1]] | C | SKAP1 activity raises PADI1's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 5.01× lower at baseline in the lines without SKAP1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises PADI1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.14× lower at baseline in the lines without TMPRSS4 | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[SULT2B1]] | C | SULT2B1 activity raises PADI1's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 3.68× lower at baseline in the lines without SULT2B1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent; co-absent with the target |
| [[TINAGL1]] | C | TINAGL1 activity raises PADI1's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 3.85× lower at baseline in the lines without TINAGL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19; co-absent with the target |
| [[C1orf116]] | C | C1orf116 activity raises PADI1's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 4.30× lower at baseline in the lines without C1orf116 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises PADI1's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 3.87× lower at baseline in the lines without MAL2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[HSD17B2]] | C | HSD17B2 activity raises PADI1's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 4.32× lower at baseline in the lines without HSD17B2 | 0.010 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2; co-absent with the target |

### Downstream of this gene

*106 arrows, 106 of them with an alert ⚠; grade A 0, B 35, C 71. Shown: the 12 strongest; 94 more arrows (94 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA11]] | B | PADI1 activity raises ANXA11's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 2.98× lower at baseline in the lines without PADI1 | 1e-03 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[MYRF]] | B | PADI1 activity raises MYRF's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 3.33× lower at baseline in the lines without PADI1 | 0.002 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[EPS8L1]] | B | PADI1 activity raises EPS8L1's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 3.18× lower at baseline in the lines without PADI1 | 0.003 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[JUP]] | B | PADI1 activity raises JUP's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 3.56× lower at baseline in the lines without PADI1 | 0.007 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[SDCBP2]] | B | PADI1 activity raises SDCBP2's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 3.26× lower at baseline in the lines without PADI1 | 0.007 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[RDH13]] | B | PADI1 activity raises RDH13's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 2.39× lower at baseline in the lines without PADI1 | 0.008 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[BAIAP2L2]] | B | PADI1 activity raises BAIAP2L2's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without PADI1 | 0.009 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[TJP2]] | B | PADI1 activity raises TJP2's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 3.00× lower at baseline in the lines without PADI1 | 0.011 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[ARHGEF3]] | B | PADI1 activity raises ARHGEF3's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 2.38× lower at baseline in the lines without PADI1 | 0.016 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[ARHGAP27]] | B | PADI1 activity raises ARHGAP27's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without PADI1 | 0.021 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[MET]] | B | PADI1 activity raises MET's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 2.62× lower at baseline in the lines without PADI1 | 0.021 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[CD58]] | B | PADI1 activity raises CD58's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 1.59× lower at baseline in the lines without PADI1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.750). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, 52.3); signed map (3.6, 38.7). **Vector** length 64.8, 27.2% of its response variance represented; |z| ≥ 3 in 388 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +3.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -5.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.4 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | peptidyl arginine deiminase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:17,205,128-17,246,007 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HPAD10, PDI1, PDI, PAD1 |
| Gene groups (HGNC) | Peptidyl arginine deiminases |
| Reactome | 2 pathways, smallest: Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULC6](https://www.uniprot.org/uniprotkb/Q9ULC6) (Protein-arginine deiminase type-1):

> Catalyzes the deimination of arginine residues of proteins.

**Summary**, from NCBI Gene [29943](https://www.ncbi.nlm.nih.gov/gene/29943):

> This gene encodes a member of the peptidyl arginine deiminase family of enzymes, which catalyze the post-translational deimination of proteins by converting arginine residues into citrullines in the presence of calcium ions. The family members have distinct substrate specificities and tissue-specific expression patterns. The type I enzyme is involved in the late stages of epidermal differentiation, where it deiminates filaggrin and keratin K1, which maintains hydration of the stratum corneum, …

**Accessions** — [HGNC:18367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18367) · Entrez [29943](https://www.ncbi.nlm.nih.gov/gene/29943) · UniProt [Q9ULC6](https://www.uniprot.org/uniprotkb/Q9ULC6) · Ensembl [ENSG00000142623](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142623)

## Data

Gene col 6637: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6637); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6637, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6637]; `tensor/DDL_lfc|DDL_z.npy` [6637]; `embed/gene_vectors.npy` [6637]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6637 or target_col == 6637). Every well: [[PADI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PADI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
