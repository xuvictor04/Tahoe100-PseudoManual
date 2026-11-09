---
symbol: "FBXO27"
type: "gene"
col: 8423
ensembl_id: "ENSG00000161243"
name: "F-box protein 27"
location: "19q13.2"
module: 128
arm: "+"
pooled_cpm: 16.45
n_lines_expressing: 22
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 16
direction_downstream: 11
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# FBXO27

*F-box protein 27* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.04× (z +12.2, q 2e-31, up in 7 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.03× (z +6.4, q 2e-08, up in 6 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.664× (z -5.2, q 1e-04, down in 17 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC36]] (+0.62, fdr 1e-05), [[CACNA1B]] (+0.56, fdr 2e-05), [[JPH3]] (+0.56, fdr 4e-05); moves opposite to [[DECR1]] (-0.47, fdr 9e-05), [[RRP8]] (-0.46, fdr 1e-04), [[CREBZF]] (-0.44, fdr 9e-05).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[KIF26A]] → it (grade B ⚠); 11 go from it, the strongest it → [[RUNDC3A-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8423.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.04×** | +12.2 | 2e-31 | 7/10 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.81×** | +12.1 | 2e-31 | 10/15 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +8.0 | 2e-13 | 6/13 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +6.4 | 2e-08 | 6/20 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.2 | 5e-08 | 5/20 (A549, A498, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +6.2 | 5e-08 | 6/20 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +5.1 | 3e-05 | 2/20 (MIA PaCa-2, HEC-1-A) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +4.9 | 8e-05 | 5/20 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.79×** | +3.8 | 0.010 | 8/19 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.010 | 8/20 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.019 | 3/18 (HEC-1-A, C-33 A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.4 | 0.035 | 2/17 (J82, HOP62) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.039 | 5/18 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +3.2 | 0.051 | 4/20 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.083 | 5/20 (PANC-1, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8423.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.664×** | -5.2 | 1e-04 | 17/19 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.620×** | -4.2 | 0.009 | 14/19 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.647×** | -3.9 | 0.016 | 12/19 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.663×** | -3.7 | 0.029 | 10/20 (PANC-1, NCI-H661, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.693× | -3.3 | 0.10 | 10/19 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.697× | -3.3 | 0.10 | 9/20 (NCI-H23, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.509× | -3.2 | 0.11 | 11/18 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8423. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 35.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0913× (z -22.1) |
| [[PANC-1 (line)]] | alt | 117 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -20.3) |
| [[NCI-H2030 (line)]] | alt | 109 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0620× (z -23.7) |
| [[A-427 (line)]] | wt | 73.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -17.0) |
| [[MIA PaCa-2 (line)]] | alt | 9.66 | 0 | 2 | — | [[Bimiralisib (drug)]] 0.5 µM 0.0649× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 4.59 | 0 | 2 (1 ⚠) | — | [[Erlotinib (drug)]] 5 µM 0.0565× (z -9.6) |
| [[SW480 (line)]] | alt | 15.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -12.4) |
| [[A498 (line)]] | wt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 5.96 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0891× (z -9.0) |
| [[A-172 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.950 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8423), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC36]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CACNA1B]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[JPH3]] | +0.56 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[KCTD20]] | +0.54 | +0.53 / +0.36 | both halves | 9e-05 |  |
| [[MYOM1]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[UPK1A-AS1]] | +0.54 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[BMERB1]] | +0.53 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[PDZD4]] | +0.52 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[KNDC1]] | +0.51 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[RFPL1S]] | +0.51 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[PNMA2]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[TMEM41B]] | +0.50 | +0.39 / +0.52 | both halves | 5e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | -0.47 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[RRP8]] | -0.46 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[CREBZF]] | -0.44 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[RNF146]] | -0.42 | -0.31 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 9, C 7. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF26A]] | B | KIF26A activity raises FBXO27's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.26× lower at baseline in the lines without KIF26A | 0.054 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[STC1]] | B | STC1 activity lowers FBXO27's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.24× higher at baseline in the lines without STC1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[GNAO1]] | B | GNAO1 activity raises FBXO27's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.47× lower at baseline in the lines without GNAO1 | 0.056 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[GBX1]] | B | GBX1 activity raises FBXO27's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 2.60× lower at baseline in the lines without GBX1 | 0.059 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[LHX6]] | B | LHX6 activity raises FBXO27's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 2.14× lower at baseline in the lines without LHX6 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[FSD1]] | B | FSD1 activity raises FBXO27's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 2.41× lower at baseline in the lines without FSD1 | 0.079 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[MMP17]] | B | MMP17 activity raises FBXO27's level | lines that do not express MMP17 (17) vs lines expressing it (33) | 2.35× lower at baseline in the lines without MMP17 | 0.084 | ⚠ within organs, on part of the lines; also absent: NOVA2, TUB, RIMKLB |
| [[UPK1A-AS1]] | B | UPK1A-AS1 activity raises FBXO27's level | lines that do not express UPK1A-AS1 (18) vs lines expressing it (32) | 2.51× lower at baseline in the lines without UPK1A-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: CERS4, SUSD5, WIPF1 |
| [[ADGRB1]] | B | ADGRB1 activity raises FBXO27's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 2.47× lower at baseline in the lines without ADGRB1 | 0.098 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[PDZD4]] | C | PDZD4 activity raises FBXO27's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 3.18× lower at baseline in the lines without PDZD4 | 0.004 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12; co-absent with the target |
| [[LMX1B]] | C | LMX1B activity raises FBXO27's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 3.14× lower at baseline in the lines without LMX1B | 0.019 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2; co-absent with the target |
| [[JPH3]] | C | JPH3 activity raises FBXO27's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 2.86× lower at baseline in the lines without JPH3 | 0.026 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RUNDC3A-AS1]] | B | FBXO27 activity raises RUNDC3A-AS1's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 2.07× lower at baseline in the lines without FBXO27 | 0.016 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2 |
| [[FBXO17]] | B | FBXO27 activity raises FBXO17's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 3.72× lower at baseline in the lines without FBXO27 | 0.054 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2 |
| [[GBX1]] | B | FBXO27 activity raises GBX1's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 1.82× lower at baseline in the lines without FBXO27 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2 |
| [[STC1]] | B | FBXO27 activity lowers STC1's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 1.92× higher at baseline in the lines without FBXO27 | 0.080 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2 |
| [[MCF2L2]] | B | FBXO27 activity raises MCF2L2's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 2.04× lower at baseline in the lines without FBXO27 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2 |
| [[TNNT1]] | B | FBXO27 activity raises TNNT1's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 1.82× lower at baseline in the lines without FBXO27 | 0.092 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2 |
| [[CYS1]] | B | FBXO27 activity raises CYS1's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 1.63× lower at baseline in the lines without FBXO27 | 0.096 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2 |
| [[LMX1B]] | C | FBXO27 activity raises LMX1B's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 3.07× lower at baseline in the lines without FBXO27 | 0.032 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2; co-absent with the target |
| [[PDZD4]] | C | FBXO27 activity raises PDZD4's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 2.48× lower at baseline in the lines without FBXO27 | 0.037 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2; co-absent with the target |
| [[RAB6B]] | C | FBXO27 activity raises RAB6B's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 2.98× lower at baseline in the lines without FBXO27 | 0.040 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2; co-absent with the target |
| [[JPH3]] | C | FBXO27 activity raises JPH3's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 2.41× lower at baseline in the lines without FBXO27 | 0.058 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.1, 37.4); signed map (24.6, 25.5). **Vector** length 44.9, 10.8% of its response variance represented; |z| ≥ 3 in 400 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +3.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -3.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -3.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -3.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.9 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,990,714-39,032,785 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Fbg5, Fbx27 |
| Gene groups (HGNC) | F-boxes other |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NI29](https://www.uniprot.org/uniprotkb/Q8NI29) (F-box only protein 27):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex. Able to recognize and bind denatured glycoproteins, which are modified with complex-type oligosaccharides.

**Summary**, from NCBI Gene [126433](https://www.ncbi.nlm.nih.gov/gene/126433):

> Members of the F-box protein family, such as FBXO27, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18753](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18753) · Entrez [126433](https://www.ncbi.nlm.nih.gov/gene/126433) · UniProt [Q8NI29](https://www.uniprot.org/uniprotkb/Q8NI29) · Ensembl [ENSG00000161243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161243)

## Data

Gene col 8423: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8423); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8423, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8423]; `tensor/DDL_lfc|DDL_z.npy` [8423]; `embed/gene_vectors.npy` [8423]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8423 or target_col == 8423). Every well: [[FBXO27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
