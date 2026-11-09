---
symbol: "SNX10"
type: "gene"
col: 1459
ensembl_id: "ENSG00000086300"
name: "sorting nexin 10"
location: "7p15.2"
module: 132
arm: "+"
pooled_cpm: 37.39
n_lines_expressing: 39
n_dd_up: 7
n_dd_down: 22
n_dd_up_clean: 5
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 11
direction_downstream: 6
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# SNX10

*sorting nexin 10* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.41× (z +9.5, q 2e-18, up in 25 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.370× (z -27.0, q 0e+00, down in 34 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB6B]] (+0.59, fdr 1e-05), [[ZNF483]] (+0.58, fdr 3e-05), [[GLO1]] (+0.56, fdr 3e-05); moves opposite to [[KIAA2026]] (-0.55, fdr 6e-05), [[UBAP1L]] (-0.52, fdr 4e-05), [[EFCAB6]] (-0.51, fdr 1e-04).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[STOX2]] → it (grade B ⚠); 6 go from it, the strongest it → [[RASGEF1C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1459.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +9.5 | 2e-18 | 25/37 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +9.1 | 2e-17 | 26/36 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +8.4 | 6e-15 | 20/35 (SW480, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +6.2 | 9e-08 | 16/29 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +5.4 | 6e-06 | 17/37 (HOP62, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.004 | 14/37 (NCI-H2347, BT-474, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.040 | 9/36 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.17 | 13/36 (HOP62, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1459.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.370×** | -27.0 | 0e+00 | 34/37 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.398×** | -17.7 | 0e+00 | 29/35 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.414×** | -16.9 | 0e+00 | 31/36 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.559×** | -15.8 | 0e+00 | 31/37 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.491×** | -13.7 | 2e-40 | 31/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.497×** | -13.4 | 5e-39 | 29/36 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -12.6 | 2e-34 | 29/36 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.307×** | -11.9 | 1e-30 | 29/37 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.536×** | -11.5 | 9e-29 | 29/36 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.369×** | -10.0 | 8e-22 | 24/35 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.703×** | -9.6 | 7e-20 | 30/37 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.622×** | -8.8 | 8e-17 | 23/36 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -8.3 | 4e-15 | 24/36 (RKO, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.661×** | -7.9 | 9e-14 | 20/36 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.750×** | -5.5 | 1e-06 | 20/36 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -5.3 | 5e-06 | 20/36 (C32, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.762×** | -5.2 | 7e-06 | 19/36 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1459. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 142 | 0 | 21 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -18.7) |
| [[PANC-1 (line)]] | alt | 46.6 | 1 (1 ⚠) | 15 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.21× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -31.7) |
| [[SW480 (line)]] | alt | 67.3 | 2 (2 ⚠) | 13 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.61× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -21.8) |
| [[MIA PaCa-2 (line)]] | alt | 42.7 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0543× (z -26.8) |
| [[HepG2_C3A (line)]] | wt | 94.9 | 0 | 9 (4 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0354× (z -17.1) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.409× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 22.7 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -22.2) |
| [[SNU-1 (line)]] | wt | 44.8 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -15.7) |
| [[HEC-1-A (line)]] | alt | 65.4 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -30.0) |
| [[NCI-H2030 (line)]] | alt | 78.0 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -22.7) |
| [[RKO (line)]] | wt | 80.3 | 0 | 8 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -16.1) |
| [[A549 (line)]] | wt | 41.9 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -24.2) |
| [[NCI-H23 (line)]] | alt | 44.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -19.0) |
| [[SW1417 (line)]] | alt | 38.1 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.458× (z -10.1) |
| [[SW48 (line)]] | wt | 50.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -15.2) |
| [[H4 (line)]] | wt | 51.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -15.3) |
| [[A-172 (line)]] | wt | 23.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.1) |
| [[A-427 (line)]] | wt | 78.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -11.6) |
| [[BT-474 (line)]] | alt | 42.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -10.0) |
| [[HCT15 (line)]] | alt | 60.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -15.0) |
| [[HOP62 (line)]] | alt | 15.9 | 1 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.73× (z +9.0) ⚠ cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -8.6) |
| [[LoVo (line)]] | wt | 30.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -18.7) |
| [[SK-MEL-2 (line)]] | alt | 87.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -27.1) |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.438× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 27.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -11.5) |
| [[SW 900 (line)]] | alt | 21.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.211× (z -8.9) |
| [[A498 (line)]] | wt | 80.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.24 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.49 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1459), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB6B]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ZNF483]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[GLO1]] | +0.56 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[GNPDA2]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[ULBP3]] | +0.54 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[MOCS2]] | +0.54 | +0.39 / +0.53 | both halves | 5e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[RPAP3]] | +0.54 | +0.29 / +0.51 | both halves | 3e-04 |  |
| [[DTNB]] | +0.53 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[TMEM161A]] | +0.52 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[RIMKLA]] | +0.51 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[TOM1L1]] | +0.51 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[RBM11]] | +0.51 | +0.26 / +0.62 | both halves | 4e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA2026]] | -0.55 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[UBAP1L]] | -0.52 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[EFCAB6]] | -0.51 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[SETD1B]] | -0.50 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[MIB2]] | -0.50 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ZNF846]] | -0.49 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[ZZEF1]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TMEM187]] | -0.47 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[BBOF1]] | -0.47 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[CAPN3]] | -0.47 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[ZFTRAF1]] | -0.46 | -0.37 / -0.42 | both halves | 7e-05 |  |
| [[ALOX12-AS1]] | -0.46 | -0.38 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STOX2]] | B | STOX2 activity raises SNX10's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.12× lower at baseline in the lines without STOX2 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27 |
| [[RASGEF1C]] | B | RASGEF1C activity raises SNX10's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 2.96× lower at baseline in the lines without RASGEF1C | 0.012 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[GNAZ]] | B | GNAZ activity strengthens SNX10's drug response | lines that do not express GNAZ (6) vs lines expressing it (31) | the lines without GNAZ respond 0.57× as strongly (z diff +2.76); strongest at Niclosamide (olamine) 5 µM: 0.87x vs 0.49x (z diff +4.9) | 0.014 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ST6GAL1]] | B | ST6GAL1 activity raises SNX10's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 2.85× lower at baseline in the lines without ST6GAL1 | 0.015 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| [[RAB6B]] | B | RAB6B activity raises SNX10's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 2.63× lower at baseline in the lines without RAB6B | 0.015 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS |
| [[RBM11]] | B | RBM11 activity raises SNX10's level | lines that do not express RBM11 (25) vs lines expressing it (25) | 1.84× lower at baseline in the lines without RBM11 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000268119, ANKRD20A11P, VWDE |
| [[TOP2A]] | B | TOP2A activity raises SNX10's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MCOLN2]] | B | MCOLN2 activity raises SNX10's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.74× lower at baseline in the lines without MCOLN2 | 0.041 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[TFR2]] | B | TFR2 activity raises SNX10's level | lines that do not express TFR2 (10) vs lines expressing it (40) | 2.87× lower at baseline in the lines without TFR2 | 0.050 | ⚠ within organs, on part of the lines; also absent: KRTAP5-AS1, EFNA2, AP1G2; maybe low, not absent |
| [[LHX6]] | B | LHX6 activity raises SNX10's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without LHX6 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[ARHGAP44]] | B | ARHGAP44 activity raises SNX10's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without ARHGAP44 | 0.075 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1C]] | B | SNX10 activity raises RASGEF1C's level | lines that do not express SNX10 (11) vs lines expressing it (39) | 2.43× lower at baseline in the lines without SNX10 | 0.020 | ⚠ within organs, on part of the lines; also absent: AP3B2, LRRC4B, CCDC144CP |
| [[STOX2]] | B | SNX10 activity raises STOX2's level | lines that do not express SNX10 (11) vs lines expressing it (39) | 3.31× lower at baseline in the lines without SNX10 | 0.032 | ⚠ within organs, on part of the lines; also absent: AP3B2, LRRC4B, CCDC144CP |
| [[RBM11]] | B | SNX10 activity raises RBM11's level | lines that do not express SNX10 (11) vs lines expressing it (39) | 2.15× lower at baseline in the lines without SNX10 | 0.053 | ⚠ within organs, on part of the lines; also absent: AP3B2, LRRC4B, CCDC144CP |
| [[TFR2]] | B | SNX10 activity raises TFR2's level | lines that do not express SNX10 (11) vs lines expressing it (39) | 1.78× lower at baseline in the lines without SNX10 | 0.070 | ⚠ within organs, on part of the lines; also absent: AP3B2, LRRC4B, CCDC144CP |
| [[ST6GAL1]] | B | SNX10 activity raises ST6GAL1's level | lines that do not express SNX10 (11) vs lines expressing it (39) | 2.79× lower at baseline in the lines without SNX10 | 0.073 | ⚠ within organs, on part of the lines; also absent: AP3B2, LRRC4B, CCDC144CP |
| [[RAB6B]] | B | SNX10 activity raises RAB6B's level | lines that do not express SNX10 (11) vs lines expressing it (39) | 2.47× lower at baseline in the lines without SNX10 | 0.095 | ⚠ within organs, on part of the lines; also absent: AP3B2, LRRC4B, CCDC144CP |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.4, 42.1); signed map (-28.7, -21.0). **Vector** length 97.1, 23.6% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +6.0 | +3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.8 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -15.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -8.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.4 | -11.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | -13.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -9.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:26,291,862-26,374,383 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sorting nexins |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5X0](https://www.uniprot.org/uniprotkb/Q9Y5X0) (Sorting nexin-10):

> Probable phosphoinositide-binding protein involved in protein sorting and membrane trafficking in endosomes. Plays a role in cilium biogenesis through regulation of the transport and the localization of proteins to the cilium. Required for the localization to the cilium of V-ATPase subunit ATP6V1D and ATP6V0D1, and RAB8A. Involved in osteoclast differentiation and therefore bone resorption.

**Summary**, from NCBI Gene [29887](https://www.ncbi.nlm.nih.gov/gene/29887):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This protein does not contain a coiled coil region, like some family members. This gene may play a role in regulating endosome homeostasis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:14974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14974) · Entrez [29887](https://www.ncbi.nlm.nih.gov/gene/29887) · UniProt [Q9Y5X0](https://www.uniprot.org/uniprotkb/Q9Y5X0) · Ensembl [ENSG00000086300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086300)

## Data

Gene col 1459: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1459); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1459, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1459]; `tensor/DDL_lfc|DDL_z.npy` [1459]; `embed/gene_vectors.npy` [1459]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1459 or target_col == 1459). Every well: [[SNX10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
