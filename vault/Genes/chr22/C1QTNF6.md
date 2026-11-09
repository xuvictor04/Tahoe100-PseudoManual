---
symbol: "C1QTNF6"
type: "gene"
col: 5451
ensembl_id: "ENSG00000133466"
name: "C1q and TNF related 6"
location: "22q12.3"
module: 46
arm: "+"
pooled_cpm: 10.7
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 31
n_dd_up_clean: 7
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 8
direction_downstream: 1
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# C1QTNF6

*C1q and TNF related 6* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +6.7, q 1e-08, up in 23 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.222× (z -16.9, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF362]] (+0.67, fdr 3e-05), [[CDNF]] (+0.65, fdr 5e-05), [[MIR1915HG]] (+0.65, fdr 3e-05); moves opposite to [[SH3PXD2B]] (-0.55, fdr 2e-04), [[PCTP]] (-0.53, fdr 9e-05), [[DPY30]] (-0.53, fdr 3e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC00466]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ULK-101 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5451.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.7 | 1e-08 | 23/42 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.0 | 1e-04 | 18/42 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.53×** | +4.0 | 0.012 | 8/46 (SNU-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +3.9 | 0.013 | 7/20 (HEC-1-A, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.033 | 11/47 (KATO III, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.045 | 10/44 (KATO III, NCI-H1792, …) | rises with dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.42×** | +3.3 | 0.069 | 8/45 (NCI-H460, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.070 | 11/47 (A498, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5451.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.222×** | -16.9 | 0e+00 | 45/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.431×** | -13.3 | 6e-38 | 33/44 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.344×** | -11.9 | 1e-30 | 39/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.352×** | -11.7 | 2e-29 | 33/44 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.363×** | -11.3 | 1e-27 | 38/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.379×** | -10.9 | 2e-25 | 38/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.373×** | -10.6 | 2e-24 | 30/46 (NCI-H23, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.402×** | -10.2 | 1e-22 | 31/43 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.419×** | -9.7 | 2e-20 | 31/47 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.409×** | -9.4 | 2e-19 | 36/45 (PANC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.444×** | -9.1 | 5e-18 | 35/46 (PANC-1, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.449×** | -8.9 | 2e-17 | 36/48 (NCI-H23, A-427, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.482×** | -8.2 | 2e-14 | 29/48 (A-427, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.250×** | -8.1 | 2e-14 | 33/46 (LoVo, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.312×** | -6.8 | 3e-10 | 28/43 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.608×** | -5.5 | 9e-07 | 24/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.632×** | -5.1 | 9e-06 | 23/44 (HCT15, SW48, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.632×** | -5.1 | 9e-06 | 21/46 (A-427, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5451. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 36.4 | 0 | 15 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.114× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 23.9 | 0 | 12 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0369× (z -19.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0714× (z -16.1) |
| [[PANC-1 (line)]] | alt | 13.8 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -23.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0897× (z -17.8) |
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -15.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -13.8) |
| [[SW480 (line)]] | alt | 10.8 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0652× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0864× (z -14.8) |
| [[LoVo (line)]] | wt | 15.2 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0740× (z -17.0) |
| [[MIA PaCa-2 (line)]] | alt | 18.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -14.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 5.96 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0256× (z -17.2) |
| [[BT-474 (line)]] | alt | 18.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.122× (z -10.9) |
| [[C32 (line)]] | wt | 12.5 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.104× (z -9.2) |
| [[HS-578T (line)]] | alt | 5.13 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0509× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 6.76 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0243× (z -15.5) |
| [[A549 (line)]] | wt | 8.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -10.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[COLO 205 (line)]] | alt | 9.08 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -10.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -9.3) |
| [[HOP62 (line)]] | alt | 6.39 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -8.9) |
| [[J82 (line)]] | alt | 9.63 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.184× (z -9.1) |
| [[KATO III (line)]] | alt | 6.22 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0668× (z -10.4) |
| [[SHP-77 (line)]] | alt | 7.57 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -10.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 7.29 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -9.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5451), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF362]] | +0.67 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[CDNF]] | +0.65 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[MIR1915HG]] | +0.65 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[CYB561A3]] | +0.64 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[FAM174B]] | +0.63 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[ANXA2R-AS1]] | +0.62 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[TMEM9B-AS1]] | +0.61 | +0.58 / +0.38 | both halves | 6e-05 |  |
| [[LINC02615]] | +0.61 | +0.64 / +0.27 | both halves | 3e-04 |  |
| [[DENND5B-AS1]] | +0.60 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[TAFA2]] | +0.59 | +0.55 / +0.24 | both halves | 5e-04 |  |
| [[ADCK1]] | +0.59 | +0.55 / +0.23 | both halves | 5e-04 |  |
| [[SIAH1]] | +0.58 | +0.41 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3PXD2B]] | -0.55 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[PCTP]] | -0.53 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[DPY30]] | -0.53 | -0.46 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00466]] | B | LINC00466 activity raises C1QTNF6's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 1.53× lower at baseline in the lines without LINC00466 | 0.014 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent |
| [[RASSF8-AS1]] | B | RASSF8-AS1 activity strengthens C1QTNF6's drug response | lines that do not express RASSF8-AS1 (14) vs lines expressing it (34) | the lines without RASSF8-AS1 respond 0.65× as strongly (z diff +1.63); strongest at Homoharringtonine 0.5 µM: 0.64x vs 0.33x (z diff +2.8) | 0.030 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804; target measured in part of the lines; artifact flags |
| [[LINC00466]] | B | LINC00466 activity strengthens C1QTNF6's drug response | lines that do not express LINC00466 (15) vs lines expressing it (33) | the lines without LINC00466 respond 0.68× as strongly (z diff +1.72); strongest at Digitoxin 5 µM: 0.47x vs 0.27x (z diff +3.3) | 0.047 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[FTCDNL1]] | B | FTCDNL1 activity raises C1QTNF6's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.56× lower at baseline in the lines without FTCDNL1 | 0.047 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[INHA]] | B | INHA activity strengthens C1QTNF6's drug response | lines that do not express INHA (11) vs lines expressing it (37) | the lines without INHA respond 0.56× as strongly (z diff +2.01); strongest at Homoharringtonine 0.5 µM: 0.70x vs 0.35x (z diff +3.7) | 0.050 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13; target measured in part of the lines; artifact flags |
| [[MIR1915HG]] | B | MIR1915HG activity raises C1QTNF6's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.55× lower at baseline in the lines without MIR1915HG | 0.058 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[INHA]] | B | INHA activity raises C1QTNF6's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without INHA | 0.083 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |
| [[RASSF8-AS1]] | B | RASSF8-AS1 activity raises C1QTNF6's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 1.52× lower at baseline in the lines without RASSF8-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ULK-101 (drug)]] 5 µM | C | C1QTNF6's natural level raises the cells' numbers under ULK-101 5 µM (protects the cells) | C1QTNF6's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65 | 0.361 over the table, 0.064 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (2.5, 23.7); signed map (34.0, -10.9). **Vector** length 63.2, 11.6% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +6.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +1.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.2 | +0.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -8.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -9.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.6 | -8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.4 | -9.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -9.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | C1q and TNF related 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:37,180,166-37,199,385 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CTRP6, ZACRP6 |
| Gene groups (HGNC) | C1q and TNF related |
| Matched by | ensembl_id |

UniProt [Q9BXI9](https://www.uniprot.org/uniprotkb/Q9BXI9) carries no function annotation.

**Summary**, from NCBI Gene [114904](https://www.ncbi.nlm.nih.gov/gene/114904):

> Enables identical protein binding activity. Predicted to be located in extracellular region. Predicted to be part of protein-containing complex. Predicted to be active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14343) · Entrez [114904](https://www.ncbi.nlm.nih.gov/gene/114904) · UniProt [Q9BXI9](https://www.uniprot.org/uniprotkb/Q9BXI9) · Ensembl [ENSG00000133466](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133466)

## Data

Gene col 5451: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5451); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5451, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5451]; `tensor/DDL_lfc|DDL_z.npy` [5451]; `embed/gene_vectors.npy` [5451]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5451 or target_col == 5451). Every well: [[C1QTNF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1QTNF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
