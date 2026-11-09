---
symbol: "ANKS1B"
type: "gene"
col: 11615
ensembl_id: "ENSG00000185046"
name: "ankyrin repeat and sterile alpha motif domain containing 1B"
location: "12q23.1"
module: 10
arm: "+"
pooled_cpm: 63.53
n_lines_expressing: 32
n_dd_up: 25
n_dd_down: 18
n_dd_up_clean: 23
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 18
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ANKS1B

*ankyrin repeat and sterile alpha motif domain containing 1B* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +10.3, q 4e-22, up in 12 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.574× (z -7.7, q 1e-11, down in 25 of 30 measured lines) ⚠ toxic. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.603× (z -7.3, q 1e-10, down in 23 of 30 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KATNAL2]] (+0.71, fdr 7e-06), [[FRG1-DT]] (+0.68, fdr 2e-05), [[FTCDNL1]] (+0.65, fdr 3e-05); moves opposite to [[LCMT1]] (-0.53, fdr 1e-04), [[MPG]] (-0.48, fdr 4e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CACNA1B]] → it (grade B ⚠); 18 go from it, the strongest it → [[ATP6V1E2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11615.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +10.3 | 4e-22 | 12/30 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +9.4 | 2e-18 | 18/30 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +9.3 | 3e-18 | 16/30 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +7.7 | 2e-12 | 21/30 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.71×** | +7.4 | 2e-11 | 26/30 (C-33 A, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +7.0 | 2e-10 | 9/30 (NCI-H460, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.45×** | +5.3 | 8e-06 | 21/30 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.4 | 7e-04 | 9/30 (HS-578T, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.002 | 9/30 (NCI-H460, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +4.1 | 0.002 | 14/30 (SNU-1, C-33 A, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 15/30 (BT-474, A-172, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.006 | 11/31 (BT-474, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.006 | 15/30 (BT-474, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.007 | 16/30 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.008 | 15/30 (NCI-H1573, C-33 A, …) | two highest doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.010 | 14/30 (A549, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11615.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -7.7 | 1e-11 | 25/30 (SNU-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.603×** | -7.3 | 1e-10 | 23/30 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.670×** | -5.7 | 2e-06 | 19/30 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.690×** | -5.3 | 1e-05 | 18/30 (NCI-H23, A-427, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.694×** | -5.2 | 2e-05 | 24/30 (PANC-1, J82, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.699×** | -5.1 | 2e-05 | 21/30 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.713×** | -4.9 | 1e-04 | 20/30 (PANC-1, J82, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.720×** | -4.7 | 2e-04 | 21/30 (A-427, SNU-423, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.740×** | -4.3 | 9e-04 | 21/30 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.743×** | -4.3 | 0.001 | 16/30 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.750×** | -4.1 | 0.002 | 20/30 (PANC-1, NCI-H23, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.766×** | -3.8 | 0.006 | 19/30 (A-427, SNU-423, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.781×** | -3.6 | 0.016 | 20/30 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.775×** | -3.4 | 0.028 | 9/30 (A-427, SNU-423, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.654×** | -3.2 | 0.055 | 12/24 (HEC-1-A, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.656×** | -3.2 | 0.056 | 13/30 (HEC-1-A, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.799×** | -3.1 | 0.065 | 8/30 (A549, J82, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.810×** | -3.0 | 0.077 | 16/30 (NCI-H2030, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 471 | 0 | 11 (8 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -16.4) |
| [[SNU-423 (line)]] | alt | 306 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 152 | 0 | 8 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.268× (z -10.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.285× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 211 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0820× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.224× (z -12.5) |
| [[PANC-1 (line)]] | alt | 88.6 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.205× (z -13.7) |
| [[J82 (line)]] | alt | 75.5 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.217× (z -11.0) |
| [[C-33 A (line)]] | alt | 303 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.278× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 18.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +15.5) | — |
| [[AN3 CA (line)]] | alt | 206 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.193× (z -9.5) |
| [[LoVo (line)]] | wt | 67.4 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.255× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 73.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.198× (z -10.4) |
| [[C32 (line)]] | wt | 16.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +11.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0952× (z -10.7) ⚠ toxic |
| [[HS-578T (line)]] | alt | 60.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +13.4) | — |
| [[LOX-IMVI (line)]] | wt | 45.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.8) | [[Digitoxin (drug)]] 0.05 µM 0.272× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +12.0) | — |
| [[A-172 (line)]] | wt | 41.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +13.1) | — |
| [[BT-474 (line)]] | alt | 31.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.90× (z +8.8) | — |
| [[H4 (line)]] | wt | 28.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 92.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0421× (z -17.1) ⚠ toxic |
| [[A498 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.32 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.16 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 250 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.47 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.94 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.89 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.47 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.63 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.14 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KATNAL2]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[FRG1-DT]] | +0.68 | +0.77 / +0.46 | both halves | 2e-05 |  |
| [[FTCDNL1]] | +0.65 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[MMRN1]] | +0.63 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[LINC00882]] | +0.60 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[CCDC144CP]] | +0.59 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ZMAT1]] | +0.58 | +0.59 / +0.36 | both halves | 9e-05 |  |
| [[AGA-DT]] | +0.58 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[L3MBTL4]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 | same gene group |
| [[SPAG17]] | +0.58 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[AGBL4]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TENM3]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | -0.53 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[MPG]] | -0.48 | -0.60 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1B]] | B | CACNA1B activity raises ANKS1B's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 2.50× lower at baseline in the lines without CACNA1B | 0.035 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ANKS1B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KATNAL2]] | B | KATNAL2 activity raises ANKS1B's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 4.47× lower at baseline in the lines without KATNAL2 | 0.045 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[DOCK3]] | B | DOCK3 activity raises ANKS1B's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 2.89× lower at baseline in the lines without DOCK3 | 0.072 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[CTNNA2]] | B | CTNNA2 activity raises ANKS1B's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.20× lower at baseline in the lines without CTNNA2 | 0.074 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |
| [[RFPL1S]] | B | RFPL1S activity raises ANKS1B's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.28× lower at baseline in the lines without RFPL1S | 0.085 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[FAM184A]] | B | FAM184A activity raises ANKS1B's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.99× lower at baseline in the lines without FAM184A | 0.089 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[SAMD11]] | C | SAMD11 activity raises ANKS1B's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 3.79× lower at baseline in the lines without SAMD11 | 0.021 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1; co-absent with the target |
| [[LNC-LBCS]] | C | LNC-LBCS activity raises ANKS1B's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 3.57× lower at baseline in the lines without LNC-LBCS | 0.021 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent; co-absent with the target |
| [[ATRNL1]] | C | ATRNL1 activity raises ANKS1B's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 3.00× lower at baseline in the lines without ATRNL1 | 0.040 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 14, C 4. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP6V1E2]] | B | ANKS1B activity raises ATP6V1E2's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 2.08× lower at baseline in the lines without ANKS1B | 0.003 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[LINC03036]] | B | ANKS1B activity raises LINC03036's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 1.46× lower at baseline in the lines without ANKS1B | 0.005 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[FTCDNL1]] | B | ANKS1B activity raises FTCDNL1's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 2.23× lower at baseline in the lines without ANKS1B | 0.009 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[FAM184A]] | B | ANKS1B activity raises FAM184A's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 2.86× lower at baseline in the lines without ANKS1B | 0.013 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[SYT9-AS1]] | B | ANKS1B activity raises SYT9-AS1's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without ANKS1B | 0.013 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[ANOS2P]] | B | ANKS1B activity raises ANOS2P's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without ANKS1B | 0.026 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[RETREG1]] | B | ANKS1B activity raises RETREG1's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 2.28× lower at baseline in the lines without ANKS1B | 0.042 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[CCDC171]] | B | ANKS1B activity raises CCDC171's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 1.44× lower at baseline in the lines without ANKS1B | 0.065 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| cells under [[Lonafarnib (drug)]] 5 µM | B | ANKS1B activity raises the cells' numbers under Lonafarnib 5 µM (protects the cells) | lines that do not express ANKS1B (18) vs lines expressing it (30) | the lines without ANKS1B: 0.25× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[FBXO15]] | B | ANKS1B activity raises FBXO15's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without ANKS1B | 0.075 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| cells under [[Riluzole hydrochloride (drug)]] 5 µM | B | ANKS1B activity lowers the cells' numbers under Riluzole hydrochloride 5 µM (makes them more sensitive) | lines that do not express ANKS1B (18) vs lines expressing it (30) | the lines without ANKS1B: 1.13× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[FRG1-DT]] | B | ANKS1B activity raises FRG1-DT's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 2.25× lower at baseline in the lines without ANKS1B | 0.086 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.6, 32.5); signed map (34.6, -10.2). **Vector** length 105, 31.7% of its response variance represented; |z| ≥ 3 in 993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.9 | +5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +4.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.3 | -7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.4 | -4.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.8 | -5.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -2.6 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.5 | -5.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -0.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -3.0 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and sterile alpha motif domain containing 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:98,726,457-99,984,936 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EB-1, AIDA-1, cajalin-2, ANKS2 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Sterile alpha motif domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6G8](https://www.uniprot.org/uniprotkb/Q7Z6G8) (Ankyrin repeat and sterile alpha motif domain-containing protein 1B):

> Isoform 2 may participate in the regulation of nucleoplasmic coilin protein interactions in neuronal and transformed cells.; Isoform 3 can regulate global protein synthesis by altering nucleolar numbers.; Isoform 4 may play a role as a modulator of APP processing. Overexpression can down-regulate APP processing.

**Summary**, from NCBI Gene [56899](https://www.ncbi.nlm.nih.gov/gene/56899):

> This gene encodes a multi-domain protein that is predominantly expressed in brain and testis. This protein interacts with amyloid beta protein precursor (AbetaPP) and may have a role in normal brain development, and in the pathogenesis of Alzheimer's disease. Expression of this gene has been shown to be elevated in patients with pre-B cell acute lymphocytic leukemia associated with t(1;19) translocation. Alternatively spliced transcript variants encoding different isoforms (some with different …

**Accessions** — [HGNC:24600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24600) · Entrez [56899](https://www.ncbi.nlm.nih.gov/gene/56899) · UniProt [Q7Z6G8](https://www.uniprot.org/uniprotkb/Q7Z6G8) · Ensembl [ENSG00000185046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185046)

## Data

Gene col 11615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11615); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11615]; `tensor/DDL_lfc|DDL_z.npy` [11615]; `embed/gene_vectors.npy` [11615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11615 or target_col == 11615). Every well: [[ANKS1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKS1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
