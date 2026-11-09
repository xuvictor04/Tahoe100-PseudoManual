---
symbol: "PIP5K1B"
type: "gene"
col: 2836
ensembl_id: "ENSG00000107242"
name: "phosphatidylinositol-4-phosphate 5-kinase type 1 beta"
location: "9q21.11"
module: 8
arm: "+"
pooled_cpm: 32.81
n_lines_expressing: 17
n_dd_up: 31
n_dd_down: 4
n_dd_up_clean: 27
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 75
direction_downstream: 50
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PIP5K1B

*phosphatidylinositol-4-phosphate 5-kinase type 1 beta* — 9q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +12.1, q 3e-31, up in 3 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[vincristine (drug)]] 0.05 µM: 0.710× (z -4.5, q 0.004, down in 3 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POF1B]] (+0.77, fdr 7e-06), [[MGAM2]] (+0.75, fdr 7e-06), [[GCNT3]] (+0.75, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 75 arrows point to it, the strongest [[LDLRAD4]] → it (grade B ⚠); 50 go from it, the strongest it → [[ZNF703]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2836.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +12.1 | 3e-31 | 3/15 (HCT15, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +11.8 | 9e-30 | 1/13 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +11.5 | 2e-28 | 3/10 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +9.7 | 5e-20 | 8/15 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.97×** | +9.3 | 2e-18 | 6/15 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +8.1 | 7e-14 | 2/11 (AsPC-1, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +8.0 | 1e-13 | 9/15 (SHP-77, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +7.1 | 8e-11 | 5/15 (AsPC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +5.5 | 3e-06 | 6/15 (SHP-77, SW48, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.4 | 3e-06 | 1/15 (SNU-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +5.0 | 4e-05 | 1/15 (HCT15) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 4e-05 | 7/15 (AsPC-1, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +4.9 | 4e-05 | 3/15 (SW48, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.8 | 5e-05 | 5/15 (AsPC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 2e-04 | 5/15 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.003 | 0/15 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.014 | 0/15 | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.014 | 3/15 (COLO 205, HCT15, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.014 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2836.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[vincristine (drug)]] 0.05 µM |  | **0.710×** | -4.5 | 0.004 | 3/15 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.751×** | -4.0 | 0.021 | 5/15 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.758×** | -3.5 | 0.071 | 1/15 (SW48) | inconsistent across doses |  |
| [[Methyl aminolevulinate (hydrochloride) (drug)]] 0.5 µM |  | **0.778×** | -3.5 | 0.071 | 0/15 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.791× | -3.2 | 0.13 | 10/15 (HT-29, SW480, …) | two highest doses | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2836. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 188 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.234× (z -12.3) |
| [[KATO III (line)]] | alt | 246 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.175× (z -13.7) |
| [[LoVo (line)]] | wt | 238 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.216× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 16.2 | 5 (1 ⚠) | 0 | [[Trametinib (drug)]] 0.5 µM 4.56× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 267 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.222× (z -12.0) |
| [[COLO 205 (line)]] | alt | 138 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.369× (z -9.4) |
| [[SHP-77 (line)]] | alt | 8.88 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0986× (z -9.3) |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.102× (z -9.1) |
| [[A-172 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.71 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.31 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.57 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.89 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.38 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.95 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.56 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2836), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POF1B]] | +0.77 | +0.78 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[MGAM2]] | +0.75 | +0.75 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.75 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[TOX3]] | +0.74 | +0.76 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A6]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A9]] | +0.74 | +0.70 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS2]] | +0.72 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[PROM1]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[UGT1A8]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[MUC13]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[PRR15L]] | +0.70 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[CLIC5]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*75 arrows, 75 of them with an alert ⚠; grade A 0, B 3, C 72. Shown: the 12 strongest; 63 more arrows (63 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDLRAD4]] | B | LDLRAD4 activity raises PIP5K1B's level | lines that do not express LDLRAD4 (23) vs lines expressing it (27) | 1.70× lower at baseline in the lines without LDLRAD4 | 0.047 | ⚠ within organs, on part of the lines; also absent: TTTY14, NLGN4X, ENSG00000260958 |
| [[HGD]] | B | HGD activity raises PIP5K1B's level | lines that do not express HGD (15) vs lines expressing it (35) | 3.14× lower at baseline in the lines without HGD | 0.074 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises PIP5K1B's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.41× lower at baseline in the lines without SLC44A3 | 0.086 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[NPSR1]] | C | NPSR1 activity raises PIP5K1B's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 14.00× lower at baseline in the lines without NPSR1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[SYNPR-AS1]] | C | SYNPR-AS1 activity raises PIP5K1B's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 4.85× lower at baseline in the lines without SYNPR-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises PIP5K1B's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 5.86× lower at baseline in the lines without SLC44A4 | 0.002 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[AGR2]] | C | AGR2 activity raises PIP5K1B's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 4.46× lower at baseline in the lines without AGR2 | 0.002 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises PIP5K1B's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 8.01× lower at baseline in the lines without CDH17 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[PRR15]] | C | PRR15 activity raises PIP5K1B's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 4.75× lower at baseline in the lines without PRR15 | 0.003 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C; co-absent with the target |
| [[TMEM45B]] | C | TMEM45B activity raises PIP5K1B's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 5.60× lower at baseline in the lines without TMEM45B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; co-absent with the target |
| [[NPSR1-AS1]] | C | NPSR1-AS1 activity raises PIP5K1B's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 5.24× lower at baseline in the lines without NPSR1-AS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises PIP5K1B's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 9.30× lower at baseline in the lines without FAM3D | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 13, C 37. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF703]] | B | PIP5K1B activity raises ZNF703's level | lines that do not express PIP5K1B (33) vs lines expressing it (17) | 2.88× lower at baseline in the lines without PIP5K1B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| [[ASS1]] | B | PIP5K1B activity raises ASS1's level | lines that do not express PIP5K1B (33) vs lines expressing it (17) | 3.13× lower at baseline in the lines without PIP5K1B | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| [[LDLRAD4]] | B | PIP5K1B activity raises LDLRAD4's level | lines that do not express PIP5K1B (33) vs lines expressing it (17) | 2.13× lower at baseline in the lines without PIP5K1B | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| [[SPATA6L]] | B | PIP5K1B activity raises SPATA6L's level | lines that do not express PIP5K1B (33) vs lines expressing it (17) | 3.12× lower at baseline in the lines without PIP5K1B | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| [[GAREM1]] | B | PIP5K1B activity raises GAREM1's level | lines that do not express PIP5K1B (33) vs lines expressing it (17) | 2.79× lower at baseline in the lines without PIP5K1B | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| cells under [[Tranilast (drug)]] 0.5 µM | B | PIP5K1B activity lowers the cells' numbers under Tranilast 0.5 µM (makes them more sensitive) | lines that do not express PIP5K1B (33) vs lines expressing it (15) | the lines without PIP5K1B: 1.19× the cells of the other lines | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| cells under [[Pimozide (drug)]] 0.05 µM | B | PIP5K1B activity raises the cells' numbers under Pimozide 0.05 µM (protects the cells) | lines that do not express PIP5K1B (33) vs lines expressing it (15) | the lines without PIP5K1B: 0.83× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| [[MTUS1]] | B | PIP5K1B activity raises MTUS1's level | lines that do not express PIP5K1B (33) vs lines expressing it (17) | 3.82× lower at baseline in the lines without PIP5K1B | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| [[SLC37A1]] | B | PIP5K1B activity raises SLC37A1's level | lines that do not express PIP5K1B (33) vs lines expressing it (17) | 2.59× lower at baseline in the lines without PIP5K1B | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | B | PIP5K1B activity raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | lines that do not express PIP5K1B (33) vs lines expressing it (15) | the lines without PIP5K1B: 0.83× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| cells under [[Erlotinib (drug)]] 0.05 µM | B | PIP5K1B activity raises the cells' numbers under Erlotinib 0.05 µM (protects the cells) | lines that do not express PIP5K1B (33) vs lines expressing it (15) | the lines without PIP5K1B: 0.79× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| [[BAG1]] | B | PIP5K1B activity raises BAG1's level | lines that do not express PIP5K1B (33) vs lines expressing it (17) | 1.70× lower at baseline in the lines without PIP5K1B | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.6, 51.5); signed map (61.8, 3.6). **Vector** length 68.8, 27.0% of its response variance represented; |z| ≥ 3 in 440 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.1 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +9.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +4.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.5 |
| fall | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-4-phosphate 5-kinase type 1 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.11 — chr9:68,705,240-69,009,176 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STM7, MSS4 |
| Gene groups (HGNC) | Phosphatidylinositol-4-phosphate 5-kinase type 1 family |
| Reactome | 11 pathways, smallest: WNT mediated activation of DVL; Synthesis of PIPs at the plasma membrane; PI Metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O14986](https://www.uniprot.org/uniprotkb/O14986) (Phosphatidylinositol 4-phosphate 5-kinase type-1 beta):

> Catalyzes the phosphorylation of phosphatidylinositol 4-phosphate (PtdIns(4)P/PI4P) to form phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2/PIP2), a lipid second messenger that regulates several cellular processes such as signal transduction, vesicle trafficking, actin cytoskeleton dynamics, cell adhesion, and cell motility (By similarity). PtdIns(4,5)P2 can directly act as a second messenger or can be utilized as a precursor to generate other second messengers: inositol …

**Summary**, from NCBI Gene [8395](https://www.ncbi.nlm.nih.gov/gene/8395):

> Predicted to enable 1-phosphatidylinositol-4-phosphate 5-kinase activity. Predicted to be involved in phosphatidylinositol phosphate biosynthetic process. Predicted to act upstream of or within phosphatidylinositol biosynthetic process. Located in uropod. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:8995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8995) · Entrez [8395](https://www.ncbi.nlm.nih.gov/gene/8395) · UniProt [O14986](https://www.uniprot.org/uniprotkb/O14986) · Ensembl [ENSG00000107242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107242)

## Data

Gene col 2836: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2836); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2836, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2836]; `tensor/DDL_lfc|DDL_z.npy` [2836]; `embed/gene_vectors.npy` [2836]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2836 or target_col == 2836). Every well: [[PIP5K1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIP5K1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
