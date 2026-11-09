---
symbol: "ERBB3"
type: "gene"
col: 784
ensembl_id: "ENSG00000065361"
name: "erb-b2 receptor tyrosine kinase 3"
location: "12q13.2"
module: 8
arm: "+"
pooled_cpm: 30.98
n_lines_expressing: 23
n_dd_up: 33
n_dd_down: 26
n_dd_up_clean: 27
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 114
direction_downstream: 143
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ERBB3

*erb-b2 receptor tyrosine kinase 3* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.61× (z +14.1, q 2e-42, up in 9 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +10.5, q 1e-23, up in 2 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.463× (z -11.3, q 8e-27, down in 19 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RORC]] (+0.76, fdr 7e-06), [[BCAS1]] (+0.74, fdr 7e-06), [[TOX3]] (+0.74, fdr 7e-06); moves opposite to [[PCOLCE2]] (-0.55, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 114 arrows point to it, the strongest [[DCLK2]] → it (grade B ⚠); 143 go from it, the strongest it → [[PRRG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 784.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +14.1 | 2e-42 | 9/21 (HEC-1-A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +11.8 | 7e-30 | 9/18 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +10.5 | 1e-23 | 2/20 (HEC-1-A, BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +10.1 | 5e-22 | 5/18 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +5.9 | 5e-07 | 0/21 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.6 | 3e-06 | 0/21 | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +5.2 | 2e-05 | 1/21 (A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 2e-04 | 16/21 (AsPC-1, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **1.78×** | +4.5 | 5e-04 | 13/20 (AsPC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +4.4 | 5e-04 | 15/21 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.76×** | +4.4 | 7e-04 | 8/20 (AsPC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.003 | 2/22 (A-427, HEC-1-A) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.9 | 0.004 | 7/21 (KATO III, LoVo, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.006 | 13/21 (SW480, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +3.7 | 0.006 | 3/20 (SW480, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.006 | 12/21 (KATO III, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.006 | 2/21 (HEC-1-A, A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.008 | 2/20 (CFPAC-1, AsPC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.008 | 13/21 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.012 | 0/21 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 784.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.463×** | -11.3 | 8e-27 | 19/19 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.476×** | -10.4 | 5e-23 | 19/21 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.538×** | -9.1 | 2e-17 | 18/21 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.660×** | -8.6 | 1e-15 | 20/20 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.581×** | -8.0 | 2e-13 | 17/21 (NCI-H1573, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.591×** | -7.7 | 1e-12 | 19/21 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.633×** | -6.7 | 2e-09 | 20/21 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.654×** | -6.2 | 3e-08 | 18/21 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.678×** | -5.4 | 5e-06 | 18/20 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.698×** | -5.3 | 8e-06 | 14/21 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.721×** | -4.8 | 9e-05 | 10/21 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.737×** | -4.5 | 4e-04 | 9/21 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.767×** | -3.9 | 0.004 | 17/21 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[EX229 (drug)]] 5 µM |  | **0.623×** | -3.6 | 0.012 | 14/20 (SW1417, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.775×** | -3.5 | 0.014 | 4/21 (LoVo, HepG2/C3A, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.632×** | -3.5 | 0.014 | 15/20 (SW1417, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 784. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 194 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -32.5) |
| [[AsPC-1 (line)]] | alt | 48.1 | 0 | 12 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0822× (z -14.0) |
| [[HT-29 (line)]] | alt | 118 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -22.2) |
| [[SK-MEL-2 (line)]] | alt | 73.2 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -10.7) |
| [[LS 180 (line)]] | wt | 105 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 42.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -17.8) |
| [[NCI-H1573 (line)]] | alt | 32.1 | 0 | 6 | — | [[Digitoxin (drug)]] 0.5 µM 0.167× (z -11.9) |
| [[SW1417 (line)]] | alt | 99.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -15.2) |
| [[SW480 (line)]] | alt | 58.0 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.302× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 98.3 | 0 | 5 | — | [[Bortezomib (drug)]] 0.05 µM 0.239× (z -10.2) |
| [[LoVo (line)]] | wt | 65.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 69.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -17.6) |
| [[Panc 03.27 (line)]] | alt | 86.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -21.4) |
| [[C32 (line)]] | wt | 59.5 | 0 | 3 (2 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.295× (z -9.7) |
| [[KATO III (line)]] | alt | 50.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 24.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +13.4) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 44.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.2) |
| [[SW48 (line)]] | wt | 41.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -8.8) |
| [[A-172 (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.64 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.44 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.73 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.96 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.89 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.90 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 784), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RORC]] | +0.76 | +0.72 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[BCAS1]] | +0.74 | +0.73 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[TOX3]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A4]] | +0.73 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[TMC4]] | +0.73 | +0.72 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[TJP3]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[ST14]] | +0.69 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[ADCY4]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 | pathway: Intracellular signaling by second messengers |
| [[FAAH2]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[PROM1]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[HNF1A-AS1]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CLDN3]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCOLCE2]] | -0.55 | -0.55 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*114 arrows, 114 of them with an alert ⚠; grade A 0, B 16, C 98. Shown: the 12 strongest; 102 more arrows (102 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCLK2]] | B | DCLK2 activity lowers ERBB3's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 5.97× higher at baseline in the lines without DCLK2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises ERBB3's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 4.65× lower at baseline in the lines without SLC44A3-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[LINC03041]] | B | LINC03041 activity lowers ERBB3's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 6.28× higher at baseline in the lines without LINC03041 | 0.005 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises ERBB3's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 4.64× lower at baseline in the lines without SLC44A3 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[MTUS1]] | B | MTUS1 activity raises ERBB3's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 3.59× lower at baseline in the lines without MTUS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[MPP7]] | B | MPP7 activity raises ERBB3's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 3.07× lower at baseline in the lines without MPP7 | 0.019 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[DMTN]] | B | DMTN activity raises ERBB3's level | lines that do not express DMTN (14) vs lines expressing it (36) | 4.52× lower at baseline in the lines without DMTN | 0.031 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[PRR36]] | B | PRR36 activity raises ERBB3's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 2.82× lower at baseline in the lines without PRR36 | 0.039 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[MANSC1]] | B | MANSC1 activity raises ERBB3's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 3.99× lower at baseline in the lines without MANSC1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[PARVB]] | B | PARVB activity lowers ERBB3's level | lines that do not express PARVB (13) vs lines expressing it (37) | 4.02× higher at baseline in the lines without PARVB | 0.053 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[LRP4]] | B | LRP4 activity lowers ERBB3's level | lines that do not express LRP4 (16) vs lines expressing it (34) | 2.08× higher at baseline in the lines without LRP4 | 0.069 | ⚠ within organs, on part of the lines |
| [[TMEM51-AS1]] | B | TMEM51-AS1 activity raises ERBB3's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 3.31× lower at baseline in the lines without TMEM51-AS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |

### Downstream of this gene

*143 arrows, 143 of them with an alert ⚠; grade A 0, B 60, C 83. Shown: the 12 strongest; 131 more arrows (131 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRRG2]] | B | ERBB3 activity raises PRRG2's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 3.01× lower at baseline in the lines without ERBB3 | 9e-05 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[SLC44A3]] | B | ERBB3 activity raises SLC44A3's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 3.71× lower at baseline in the lines without ERBB3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[SLC44A3-AS1]] | B | ERBB3 activity raises SLC44A3-AS1's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 4.01× lower at baseline in the lines without ERBB3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[ST3GAL3]] | B | ERBB3 activity lowers ST3GAL3's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.38× higher at baseline in the lines without ERBB3 | 7e-04 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[DCLK2]] | B | ERBB3 activity lowers DCLK2's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 5.61× higher at baseline in the lines without ERBB3 | 0.001 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[TMEM51-AS1]] | B | ERBB3 activity raises TMEM51-AS1's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.73× lower at baseline in the lines without ERBB3 | 0.003 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[MUC20]] | B | ERBB3 activity raises MUC20's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 3.29× lower at baseline in the lines without ERBB3 | 0.003 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[ELMO3]] | B | ERBB3 activity raises ELMO3's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.23× lower at baseline in the lines without ERBB3 | 0.005 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[MPP7]] | B | ERBB3 activity raises MPP7's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 3.10× lower at baseline in the lines without ERBB3 | 0.005 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[RAB11FIP4]] | B | ERBB3 activity raises RAB11FIP4's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.71× lower at baseline in the lines without ERBB3 | 0.006 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[AP1G2]] | B | ERBB3 activity raises AP1G2's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.52× lower at baseline in the lines without ERBB3 | 0.008 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[LINC03041]] | B | ERBB3 activity lowers LINC03041's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.16× higher at baseline in the lines without ERBB3 | 0.009 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.3, 51.6); signed map (58.8, 4.8). **Vector** length 106, 40.6% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +14.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +11.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.9 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +10.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.7 | +3.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +4.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +3.2 |
|  | [[Alpelisib (drug)]] 5 µM |  | +2.1 | +4.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -9.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -5.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | erb-b2 receptor tyrosine kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:56,076,799-56,103,505 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HER3; previously LCCS2 |
| Gene groups (HGNC) | Erb-b2 receptor tyrosine kinases |
| Hallmark sets | MYOGENESIS, APOPTOSIS |
| Reactome | 25 pathways, smallest: GRB7 events in ERBB2 signaling; Downregulation of ERBB2:ERBB3 signaling; ERBB2 Activates PTK6 Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P21860](https://www.uniprot.org/uniprotkb/P21860) (Receptor tyrosine-protein kinase erbB-3):

> Tyrosine kinase receptor that, despite substitutions of key catalytic residues in the kinase domain, retains residual catalytic activity enabling autophosphorylation. Functions primarily as a heterodimer, preferentially partnering with ERBB2/HER2, which phosphorylates ERBB3 on specific tyrosine residues and provides the kinase activity required for downstream signaling. Binds neuregulins NRG1 and NRG2 through its extracellular domain, which induces conformational change from a tethered …

**Summary**, from NCBI Gene [2065](https://www.ncbi.nlm.nih.gov/gene/2065):

> This gene encodes a member of the epidermal growth factor receptor (EGFR) family of receptor tyrosine kinases. This membrane-bound protein has a neuregulin binding domain but not an active kinase domain. It therefore can bind this ligand but not convey the signal into the cell through protein phosphorylation. However, it does form heterodimers with other EGF receptor family members which do have kinase activity. Heterodimerization leads to the activation of pathways which lead to cell …

**Accessions** — [HGNC:3431](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3431) · Entrez [2065](https://www.ncbi.nlm.nih.gov/gene/2065) · UniProt [P21860](https://www.uniprot.org/uniprotkb/P21860) · Ensembl [ENSG00000065361](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065361)

## Data

Gene col 784: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 784); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 784, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 784]; `tensor/DDL_lfc|DDL_z.npy` [784]; `embed/gene_vectors.npy` [784]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 784 or target_col == 784). Every well: [[ERBB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERBB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
