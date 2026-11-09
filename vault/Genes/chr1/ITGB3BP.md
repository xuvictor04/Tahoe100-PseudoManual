---
symbol: "ITGB3BP"
type: "gene"
col: 6658
ensembl_id: "ENSG00000142856"
name: "integrin subunit beta 3 binding protein"
location: "1p31.3"
module: 71
arm: "+"
pooled_cpm: 77.46
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 25
n_dd_up_clean: 5
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# ITGB3BP

*integrin subunit beta 3 binding protein* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.25× (z +5.6, q 1e-05, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.521× (z -16.3, q 0e+00, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFC3]] (+0.58, fdr 1e-05), [[PRIMPOL]] (+0.58, fdr 1e-05), [[ZRANB3]] (+0.57, fdr 1e-05); moves opposite to [[JUP]] (-0.48, fdr 7e-05), [[TPPP]] (-0.48, fdr 2e-04), [[ARHGEF3]] (-0.48, fdr 4e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[JUP]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TOPBP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6658.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.6 | 1e-05 | 24/48 (CFPAC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +5.0 | 2e-04 | 26/47 (NCI-H1792, KATO III, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.003 | 21/46 (A-172, HepG2/C3A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.003 | 26/47 (MIA PaCa-2, A-172, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.029 | 13/47 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.029 | 18/47 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.11 | 10/48 (C-33 A, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.20× | +3.2 | 0.11 | 16/47 (Hs 766T, NCI-H2030, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.13× | +3.1 | 0.12 | 8/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.15 | 6/48 (Panc 03.27, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6658.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.521×** | -16.3 | 0e+00 | 37/47 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.532×** | -10.7 | 2e-24 | 40/46 (H4, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.558×** | -10.3 | 1e-22 | 36/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.574×** | -9.8 | 2e-20 | 38/47 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.563×** | -9.8 | 2e-20 | 34/47 (C32, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.602×** | -9.0 | 3e-17 | 36/47 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.632×** | -8.1 | 4e-14 | 32/47 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.778×** | -6.2 | 4e-08 | 31/48 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.712×** | -6.0 | 1e-07 | 27/47 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.554×** | -5.5 | 3e-06 | 27/47 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.740×** | -5.3 | 6e-06 | 27/47 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.742×** | -5.3 | 7e-06 | 32/47 (Panc 03.27, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.743×** | -5.2 | 7e-06 | 30/47 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.761×** | -4.8 | 6e-05 | 24/47 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.767×** | -4.4 | 4e-04 | 25/47 (H4, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.633×** | -4.2 | 7e-04 | 24/48 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.804×** | -3.8 | 0.004 | 22/47 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6658. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 187 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0976× (z -26.1) |
| [[H4 (line)]] | wt | 263 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -18.7) |
| [[HOP62 (line)]] | alt | 149 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -25.0) |
| [[HEC-1-A (line)]] | alt | 144 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -21.4) |
| [[PANC-1 (line)]] | alt | 92.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -17.7) |
| [[SW480 (line)]] | alt | 91.0 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.406× (z -12.9) |
| [[A498 (line)]] | wt | 53.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -16.6) |
| [[J82 (line)]] | alt | 99.9 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.250× (z -16.0) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 48.6 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 58.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -18.3) |
| [[RPMI-7951 (line)]] | alt | 145 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -24.3) |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -22.1) |
| [[A-427 (line)]] | wt | 77.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0533× (z -32.0) |
| [[BT-474 (line)]] | alt | 42.8 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.191× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 90.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -23.7) |
| [[AN3 CA (line)]] | alt | 89.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -12.4) |
| [[HS-578T (line)]] | alt | 123 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.239× (z -10.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.436× (z -8.5) |
| [[LoVo (line)]] | wt | 39.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.374× (z -9.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 110 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H2347 (line)]] | alt | 25.5 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.09× (z +9.1) ⚠ toxic; cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +8.6) | — |
| [[SW 1088 (line)]] | alt | 194 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -9.4) |
| [[A-172 (line)]] | wt | 78.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.337× (z -8.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 56.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +12.0) | — |
| [[COLO 205 (line)]] | alt | 65.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -8.5) |
| [[HCT15 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change |
| [[hTERT-HPNE (line)]] | wt | 93.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -18.8) |
| [[LOX-IMVI (line)]] | wt | 68.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 83.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -22.0) |
| [[NCI-H2030 (line)]] | alt | 41.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 77.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -12.9) |
| [[A549 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 81.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6658), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFC3]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[PRIMPOL]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[ZRANB3]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[BRCA1]] | +0.55 | +0.57 / +0.46 | both halves | 2e-05 | pathway: Cell Cycle Checkpoints |
| [[FANCM]] | +0.55 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TTC28-AS1]] | +0.54 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[RMI1]] | +0.53 | +0.52 / +0.44 | both halves | 3e-05 | pathway: Cell Cycle Checkpoints |
| [[LIN9]] | +0.53 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[ANKRD17-DT]] | +0.52 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[TNNI3K]] | +0.52 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[MTBP]] | +0.51 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[ZGRF1]] | +0.51 | +0.52 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUP]] | -0.48 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[TPPP]] | -0.48 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[ARHGEF3]] | -0.48 | -0.40 / -0.45 | both halves | 4e-05 | pathway: Cell death signalling via NRAGE, NRIF and NADE |
| [[ASS1]] | -0.46 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[ACBD4]] | -0.45 | -0.34 / -0.29 | both halves | 2e-04 |  |
| [[CEP295NL]] | -0.44 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[RMC1]] | -0.43 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[MMP15]] | -0.43 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[PSEN2]] | -0.42 | -0.33 / -0.36 | both halves | 1e-04 | pathway: Cell death signalling via NRAGE, NRIF and NADE; STRING 400 |
| [[PDP1]] | -0.42 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[EML6]] | -0.42 | -0.40 / -0.18 | ⚠ not reproduced | 1e-03 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JUP]] | B | JUP activity lowers ITGB3BP's level | lines that do not express JUP (16) vs lines expressing it (34) | 1.71× higher at baseline in the lines without JUP | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[LINC02641]] | B | LINC02641 activity raises ITGB3BP's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 1.45× lower at baseline in the lines without LINC02641 | 0.055 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[TMEM45A]] | B | TMEM45A activity raises ITGB3BP's level | lines that do not express TMEM45A (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without TMEM45A | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, TTC28, ARHGEF25 |
| [[LINC00159]] | C | LINC00159 activity raises ITGB3BP's level | lines that do not express LINC00159 (4) vs lines expressing it (46) | 2.04× lower at baseline in the lines without LINC00159 | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF391, LINC01341, HHAT; maybe low, not absent |
| [[UBA6-DT]] | C | UBA6-DT activity raises ITGB3BP's level | lines that do not express UBA6-DT (3) vs lines expressing it (47) | 2.29× lower at baseline in the lines without UBA6-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF419, C2orf27A, CLEC2D; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOPBP1]] | C | ITGB3BP's natural level strengthens TOPBP1's drug response | ITGB3BP's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.13; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.2, -44.7); signed map (-41.7, -49.3). **Vector** length 98.0, 28.3% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.0 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | -4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | +3.3 | +1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +4.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +0.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | -1.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.4 | -4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -5.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | -5.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit beta 3 binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:63,440,770-63,593,721 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NRIF3, HSU37139, TAP20, CENPR |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Reactome | 24 pathways, smallest: NRIF signals cell death from the nucleus; Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13352](https://www.uniprot.org/uniprotkb/Q13352) (Centromere protein R):

> Transcription coregulator that can have both coactivator and corepressor functions. Isoform 1, but not other isoforms, is involved in the coactivation of nuclear receptors for retinoid X (RXRs) and thyroid hormone (TRs) in a ligand-dependent fashion. In contrast, it does not coactivate nuclear receptors for retinoic acid, vitamin D, progesterone receptor, nor glucocorticoid. Acts as a coactivator for estrogen receptor alpha. Acts as a transcriptional corepressor via its interaction with the …

**Summary**, from NCBI Gene [23421](https://www.ncbi.nlm.nih.gov/gene/23421):

> This gene encodes a transcriptional coregulator that binds to and enhances the activity of members of the nuclear receptor families, thyroid hormone receptors and retinoid X receptors. This protein also acts as a corepressor of NF-kappaB-dependent signaling. This protein induces apoptosis in breast cancer cells through a caspase 2-mediated signaling pathway. This protein is also a component of the centromere-specific histone H3 variant nucleosome associated complex (CENP-NAC) and may be …

**Accessions** — [HGNC:6157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6157) · Entrez [23421](https://www.ncbi.nlm.nih.gov/gene/23421) · UniProt [Q13352](https://www.uniprot.org/uniprotkb/Q13352) · Ensembl [ENSG00000142856](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142856)

## Data

Gene col 6658: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6658); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6658, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6658]; `tensor/DDL_lfc|DDL_z.npy` [6658]; `embed/gene_vectors.npy` [6658]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6658 or target_col == 6658). Every well: [[ITGB3BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGB3BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
