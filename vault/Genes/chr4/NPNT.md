---
symbol: "NPNT"
type: "gene"
col: 9690
ensembl_id: "ENSG00000168743"
name: "nephronectin"
location: "4q24"
module: 44
arm: "+"
pooled_cpm: 16.96
n_lines_expressing: 17
n_dd_up: 36
n_dd_down: 1
n_dd_up_clean: 28
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 77
direction_downstream: 84
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# NPNT

*nephronectin* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.36× (z +21.7, q 0e+00, up in 4 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.695× (z -4.3, q 0.010, down in 0 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 4 lines (LS 180 0.192×, LoVo 0.211×, HT-29 0.179×, AsPC-1 0.254×); [[Panobinostat (drug)]] 5 µM in 3 lines (LoVo 0.162×, LS 180 0.178×, HT-29 0.178×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 3 lines (LoVo 0.246×, HT-29 0.304×, LS 180 0.379×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LS 180 0.479×, HCT15 0.362×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TM4SF4]] (+0.78, fdr 7e-06), [[SH3BGRL2]] (+0.77, fdr 7e-06), [[CDH17]] (+0.76, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 77 arrows point to it, the strongest [[CMTM3]] → it (grade B ⚠); 84 go from it, the strongest it → [[CMTM3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9690.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.36×** | +21.7 | 0e+00 | 4/15 (HEC-1-A, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.51×** | +15.9 | 0e+00 | 5/13 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +14.9 | 0e+00 | 7/15 (HepG2/C3A, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.25×** | +14.4 | 1e-44 | 4/11 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.85×** | +12.3 | 1e-32 | 6/11 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +10.7 | 8e-25 | 3/15 (HEC-1-A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +8.5 | 1e-15 | 4/15 (NCI-H2347, SHP-77, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.46×** | +5.8 | 4e-07 | 10/15 (HepG2/C3A, AsPC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.7 | 7e-07 | 2/15 (HEC-1-A, BT-474) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.7 | 8e-07 | 2/15 (HEC-1-A, LS 180) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +5.3 | 6e-06 | 6/14 (COLO 205, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +5.3 | 7e-06 | 6/15 (LoVo, BT-474, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +5.2 | 1e-05 | 5/15 (AsPC-1, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +4.4 | 5e-04 | 5/15 (COLO 205, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.39×** | +4.3 | 8e-04 | 9/15 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 0.002 | 11/15 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.002 | 10/15 (HepG2/C3A, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.006 | 7/15 (HepG2/C3A, AsPC-1, …) | rises with dose |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.007 | 1/15 (COLO 205) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9690.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 4 lines (LS 180 0.192×, LoVo 0.211×, HT-29 0.179×, AsPC-1 0.254×); [[Panobinostat (drug)]] 5 µM in 3 lines (LoVo 0.162×, LS 180 0.178×, HT-29 0.178×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 3 lines (LoVo 0.246×, HT-29 0.304×, LS 180 0.379×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LS 180 0.479×, HCT15 0.362×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.695×** | -4.3 | 0.010 | 0/15 | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.602× | -3.4 | 0.21 | 3/15 (HepG2/C3A, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.1 | 0.31 | 2/15 (KATO III, LS 180) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 96.1 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.179× (z -14.9) |
| [[LS 180 (line)]] | wt | 96.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -16.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.192× (z -15.5) |
| [[LoVo (line)]] | wt | 130 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -17.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.211× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 48.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 104 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -9.4) |
| [[BT-474 (line)]] | alt | 6.26 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0697× (z -8.8) |
| [[HCT15 (line)]] | alt | 61.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 61.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +9.2) | — |
| [[A-172 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.62 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM4SF4]] | +0.78 | +0.73 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[SH3BGRL2]] | +0.77 | +0.73 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[CDH17]] | +0.76 | +0.72 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[MUC13]] | +0.75 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[MGAM2]] | +0.75 | +0.70 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[BCL2L15]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[TSPAN8]] | +0.73 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[PLCH1]] | +0.72 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[TRIM31]] | +0.71 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[UGT1A6]] | +0.70 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[POF1B]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[UGT1A9]] | +0.68 | +0.65 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 7, C 70. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMTM3]] | B | CMTM3 activity lowers NPNT's level | lines that do not express CMTM3 (11) vs lines expressing it (39) | 7.07× higher at baseline in the lines without CMTM3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ZNF605, C2orf74, MAP1B |
| [[HGD]] | B | HGD activity raises NPNT's level | lines that do not express HGD (15) vs lines expressing it (35) | 3.44× lower at baseline in the lines without HGD | 0.045 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[C4orf19]] | B | C4orf19 activity raises NPNT's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.56× lower at baseline in the lines without C4orf19 | 0.054 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers NPNT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC44A3]] | B | SLC44A3 activity raises NPNT's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.80× lower at baseline in the lines without SLC44A3 | 0.070 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises NPNT's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.84× lower at baseline in the lines without SLC44A3-AS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[GNA14]] | B | GNA14 activity raises NPNT's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 2.48× lower at baseline in the lines without GNA14 | 0.084 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[PRR15L]] | C | PRR15L activity raises NPNT's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 8.62× lower at baseline in the lines without PRR15L | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881; co-absent with the target |
| [[VIL1]] | C | VIL1 activity raises NPNT's level | lines that do not express VIL1 (34) vs lines expressing it (16) | 7.43× lower at baseline in the lines without VIL1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises NPNT's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 9.80× lower at baseline in the lines without CDH17 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[ST14]] | C | ST14 activity raises NPNT's level | lines that do not express ST14 (32) vs lines expressing it (18) | 6.48× lower at baseline in the lines without ST14 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |
| [[GPA33]] | C | GPA33 activity raises NPNT's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 10.89× lower at baseline in the lines without GPA33 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |

### Downstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 18, C 66. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMTM3]] | B | NPNT activity lowers CMTM3's level | lines that do not express NPNT (33) vs lines expressing it (17) | 3.47× higher at baseline in the lines without NPNT | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[SLC44A3]] | B | NPNT activity raises SLC44A3's level | lines that do not express NPNT (33) vs lines expressing it (17) | 3.20× lower at baseline in the lines without NPNT | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[SLC44A3-AS1]] | B | NPNT activity raises SLC44A3-AS1's level | lines that do not express NPNT (33) vs lines expressing it (17) | 3.02× lower at baseline in the lines without NPNT | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[SLC37A1]] | B | NPNT activity raises SLC37A1's level | lines that do not express NPNT (33) vs lines expressing it (17) | 3.05× lower at baseline in the lines without NPNT | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | NPNT activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express NPNT (33) vs lines expressing it (15) | the lines without NPNT: 1.17× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[FUT2]] | B | NPNT activity raises FUT2's level | lines that do not express NPNT (33) vs lines expressing it (17) | 2.31× lower at baseline in the lines without NPNT | 0.029 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[PLEKHA7]] | B | NPNT activity raises PLEKHA7's level | lines that do not express NPNT (33) vs lines expressing it (17) | 3.03× lower at baseline in the lines without NPNT | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[SH3BGRL2]] | B | NPNT activity raises SH3BGRL2's level | lines that do not express NPNT (33) vs lines expressing it (17) | 3.80× lower at baseline in the lines without NPNT | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | NPNT activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express NPNT (33) vs lines expressing it (15) | the lines without NPNT: 1.18× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[C4orf19]] | B | NPNT activity raises C4orf19's level | lines that do not express NPNT (33) vs lines expressing it (17) | 2.74× lower at baseline in the lines without NPNT | 0.055 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[HGD]] | B | NPNT activity raises HGD's level | lines that do not express NPNT (33) vs lines expressing it (17) | 3.07× lower at baseline in the lines without NPNT | 0.057 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[FMO5]] | B | NPNT activity raises FMO5's level | lines that do not express NPNT (33) vs lines expressing it (17) | 1.67× lower at baseline in the lines without NPNT | 0.062 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.2, 52.0); signed map (61.2, 2.9). **Vector** length 56.0, 17.9% of its response variance represented; |z| ≥ 3 in 409 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.52 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.52 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +15.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +12.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +14.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +21.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +8.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +5.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +3.5 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | nephronectin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:105,894,775-106,004,027 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EGFL6L, POEM |
| Reactome | 3 pathways, smallest: Formation of the nephric duct; Formation of the ureteric bud; Kidney development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXI9](https://www.uniprot.org/uniprotkb/Q6UXI9) (Nephronectin):

> Functional ligand of integrin alpha-8/beta-1 in kidney development. Regulates the expression of GDNF with integrin alpha-8/beta-1 which is essential for kidney development. May also play a role in the development and function of various tissues, regulating cell adhesion, spreading and survival through the binding of several integrins (By similarity).

**Summary**, from NCBI Gene [255743](https://www.ncbi.nlm.nih.gov/gene/255743):

> Predicted to enable integrin binding activity. Predicted to be involved in several processes, including cell-cell adhesion mediated by integrin; positive regulation of ERK1 and ERK2 cascade; and positive regulation of osteoblast differentiation. Predicted to act upstream of or within positive regulation of transforming growth factor beta receptor signaling pathway. Located in extracellular exosome and extracellular matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27405) · Entrez [255743](https://www.ncbi.nlm.nih.gov/gene/255743) · UniProt [Q6UXI9](https://www.uniprot.org/uniprotkb/Q6UXI9) · Ensembl [ENSG00000168743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168743)

## Data

Gene col 9690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9690); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9690]; `tensor/DDL_lfc|DDL_z.npy` [9690]; `embed/gene_vectors.npy` [9690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9690 or target_col == 9690). Every well: [[NPNT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPNT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
