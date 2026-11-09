---
symbol: "FTCDNL1"
type: "gene"
col: 13512
ensembl_id: "ENSG00000226124"
name: "formiminotransferase cyclodeaminase N-terminal like"
location: "2q33.1"
module: 10
arm: "+"
pooled_cpm: 8.25
n_lines_expressing: 39
n_dd_up: 13
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 8
direction_downstream: 19
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FTCDNL1

*formiminotransferase cyclodeaminase N-terminal like* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.73× (z +12.4, q 2e-32, up in 6 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +8.3, q 2e-14, up in 17 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.376× (z -9.6, q 4e-19, down in 28 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V1E2]] (+0.70, fdr 1e-05), [[LINC01088]] (+0.69, fdr 7e-06), [[FRG1-DT]] (+0.67, fdr 1e-05); moves opposite to [[VRK3]] (-0.60, fdr 1e-05), [[ZCCHC17]] (-0.58, fdr 6e-05), [[TULP3]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MIR1915HG]] → it (grade B ⚠); 19 go from it, the strongest it → [[METAP1D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13512.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.73×** | +12.4 | 2e-32 | 6/9 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +8.8 | 3e-16 | 14/22 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +8.3 | 2e-14 | 17/32 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +8.2 | 3e-14 | 12/15 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +7.3 | 3e-11 | 22/36 (A498, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +5.9 | 3e-07 | 18/34 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.51×** | +5.7 | 1e-06 | 13/36 (SK-MEL-2, A-172, …) | top dose only | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.63×** | +4.8 | 1e-04 | 16/34 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.65×** | +4.7 | 1e-04 | 17/33 (SW480, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +4.6 | 2e-04 | 12/34 (A-427, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.003 | 13/34 (A-172, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.005 | 13/36 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.010 | 14/34 (SK-MEL-2, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13512.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.376×** | -9.6 | 4e-19 | 28/35 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.392×** | -9.2 | 1e-17 | 22/36 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.437×** | -8.1 | 9e-14 | 27/36 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.468×** | -7.4 | 1e-11 | 23/32 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.482×** | -7.2 | 9e-11 | 24/36 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.494×** | -6.9 | 4e-10 | 23/35 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.498×** | -6.5 | 8e-09 | 22/34 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.548×** | -5.9 | 3e-07 | 19/35 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.555×** | -5.8 | 5e-07 | 17/36 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.598×** | -5.0 | 3e-05 | 18/34 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.491×** | -3.6 | 0.014 | 13/18 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.596×** | -3.6 | 0.014 | 11/35 (SNU-1, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.700×** | -3.5 | 0.020 | 12/36 (A498, SK-MEL-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.507×** | -3.5 | 0.020 | 13/30 (NCI-H23, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.542×** | -3.1 | 0.064 | 14/35 (HEC-1-A, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 50.7 | 0 | 12 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0723× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0831× (z -18.7) |
| [[A-427 (line)]] | wt | 22.8 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.138× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -12.3) |
| [[PANC-1 (line)]] | alt | 10.5 | 0 | 6 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.114× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 23.1 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.62× (z +8.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.183× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.204× (z -11.6) |
| [[LoVo (line)]] | wt | 9.04 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0570× (z -13.4) |
| [[J82 (line)]] | alt | 13.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +12.0) | [[Belinostat (drug)]] 0.5 µM 0.0345× (z -16.2) |
| [[A-172 (line)]] | wt | 4.70 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.3× (z +14.2) | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0457× (z -9.9) |
| [[A549 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0421× (z -15.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 5.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.9× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.50× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1E2]] | +0.70 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[LINC01088]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[FRG1-DT]] | +0.67 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[ZMAT1]] | +0.66 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[MIR1915HG]] | +0.66 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[ANKS1B]] | +0.65 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[TMCC1-DT]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[KATNAL2]] | +0.62 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[TMEM9B-AS1]] | +0.62 | +0.73 / +0.39 | both halves | 5e-05 |  |
| [[LINC02026]] | +0.62 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[RAP2C-AS1]] | +0.61 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[TXNRD3]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VRK3]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.58 | -0.65 / -0.38 | both halves | 6e-05 |  |
| [[TULP3]] | -0.54 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[KRBOX4]] | -0.53 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[ZNHIT1]] | -0.53 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[SWI5]] | -0.51 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[WIPI1]] | -0.51 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[CCDC32]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PMM1]] | -0.51 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[MED31]] | -0.51 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[TMED9]] | -0.50 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[OSBPL2]] | -0.50 | -0.55 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR1915HG]] | B | MIR1915HG activity raises FTCDNL1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.77× lower at baseline in the lines without MIR1915HG | 0.001 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[ANKS1B]] | B | ANKS1B activity raises FTCDNL1's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 2.23× lower at baseline in the lines without ANKS1B | 0.009 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[SYT9-AS1]] | B | SYT9-AS1 activity raises FTCDNL1's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 2.17× lower at baseline in the lines without SYT9-AS1 | 0.019 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KATNAL2]] | B | KATNAL2 activity raises FTCDNL1's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 2.36× lower at baseline in the lines without KATNAL2 | 0.048 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[ZMAT1]] | B | ZMAT1 activity raises FTCDNL1's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 2.16× lower at baseline in the lines without ZMAT1 | 0.056 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[LINC00466]] | B | LINC00466 activity raises FTCDNL1's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 2.30× lower at baseline in the lines without LINC00466 | 0.081 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent |
| [[LINC01088]] | B | LINC01088 activity raises FTCDNL1's level | lines that do not express LINC01088 (9) vs lines expressing it (41) | 1.99× lower at baseline in the lines without LINC01088 | 0.086 | ⚠ within organs, on part of the lines; also absent: PPP4R4, GPR155, PKIG; maybe low, not absent |
| [[KLHL14]] | B | KLHL14 activity raises FTCDNL1's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 1.76× lower at baseline in the lines without KLHL14 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55 |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[METAP1D]] | B | FTCDNL1 activity raises METAP1D's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.55× lower at baseline in the lines without FTCDNL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[GABPB1-AS1]] | B | FTCDNL1 activity raises GABPB1-AS1's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.80× lower at baseline in the lines without FTCDNL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[CHN1]] | B | FTCDNL1 activity raises CHN1's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 3.02× lower at baseline in the lines without FTCDNL1 | 0.012 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[SF3B3]] | B | FTCDNL1 activity raises SF3B3's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without FTCDNL1 | 0.027 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[C5]] | B | FTCDNL1 activity raises C5's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 2.06× lower at baseline in the lines without FTCDNL1 | 0.044 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[C1QTNF6]] | B | FTCDNL1 activity raises C1QTNF6's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.56× lower at baseline in the lines without FTCDNL1 | 0.047 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[GNAL]] | B | FTCDNL1 activity raises GNAL's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 2.40× lower at baseline in the lines without FTCDNL1 | 0.049 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[KICS2]] | B | FTCDNL1 activity raises KICS2's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.45× lower at baseline in the lines without FTCDNL1 | 0.052 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[ATP6V1E2]] | B | FTCDNL1 activity raises ATP6V1E2's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 2.06× lower at baseline in the lines without FTCDNL1 | 0.052 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[KLHL23]] | B | FTCDNL1 activity raises KLHL23's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.64× lower at baseline in the lines without FTCDNL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[TMEM147-AS1]] | B | FTCDNL1 activity raises TMEM147-AS1's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.31× lower at baseline in the lines without FTCDNL1 | 0.056 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[GCFC2]] | B | FTCDNL1 activity raises GCFC2's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without FTCDNL1 | 0.058 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.8, 31.4); signed map (35.2, -10.1). **Vector** length 79.0, 17.5% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +4.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -9.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.6 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -7.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -6.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -3.6 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | formiminotransferase cyclodeaminase N-terminal like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:199,760,544-199,851,192 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FONG |
| Matched by | ensembl_id |

UniProt [E5RQL4](https://www.uniprot.org/uniprotkb/E5RQL4) carries no function annotation.

**Summary**, from NCBI Gene [348751](https://www.ncbi.nlm.nih.gov/gene/348751):

> Predicted to enable transferase activity. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:48661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48661) · Entrez [348751](https://www.ncbi.nlm.nih.gov/gene/348751) · UniProt [E5RQL4](https://www.uniprot.org/uniprotkb/E5RQL4) · Ensembl [ENSG00000226124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226124)

## Data

Gene col 13512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13512); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13512]; `tensor/DDL_lfc|DDL_z.npy` [13512]; `embed/gene_vectors.npy` [13512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13512 or target_col == 13512). Every well: [[FTCDNL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FTCDNL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
