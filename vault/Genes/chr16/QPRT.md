---
symbol: "QPRT"
type: "gene"
col: 2370
ensembl_id: "ENSG00000103485"
name: "quinolinate phosphoribosyltransferase"
location: "16p11.2"
module: 45
arm: "+"
pooled_cpm: 14.07
n_lines_expressing: 29
n_dd_up: 25
n_dd_down: 9
n_dd_up_clean: 20
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 10
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# QPRT

*quinolinate phosphoribosyltransferase* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.56× (z +12.5, q 4e-33, up in 19 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cepharanthine (drug)]] 5 µM: 1.50× (z +5.7, q 2e-06, up in 16 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.598× (z -5.0, q 2e-04, down in 18 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRXL2A]] (+0.68, fdr 7e-06), [[TMEM135]] (+0.61, fdr 1e-05), [[GSTM4]] (+0.61, fdr 1e-05); moves opposite to [[TBCCD1]] (-0.54, fdr 4e-05), [[AGO2]] (-0.49, fdr 2e-05), [[LRWD1]] (-0.49, fdr 8e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AP1M2]] → it (grade B ⚠); 10 go from it, the strongest it → [[ATP6V1A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2370.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.56×** | +12.5 | 4e-33 | 19/22 (A-172, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +11.0 | 7e-26 | 13/18 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.20×** | +11.0 | 7e-26 | 13/18 (J82, A498, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.50×** | +5.7 | 2e-06 | 16/27 (A498, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +5.5 | 3e-06 | 16/27 (A-172, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +5.2 | 1e-05 | 15/27 (A-172, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 5 µM |  | **1.42×** | +4.9 | 7e-05 | 11/27 (HEC-1-A, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.8 | 9e-05 | 14/27 (A498, A-172, …) | two highest doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.62×** | +4.8 | 1e-04 | 16/26 (A498, RPMI-7951, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.37×** | +4.4 | 5e-04 | 18/27 (RPMI-7951, HepG2/C3A, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.52×** | +4.1 | 0.002 | 13/26 (HEC-1-A, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +4.1 | 0.002 | 15/27 (A-172, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.006 | 10/26 (SW480, A498, …) | rises with dose |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.8 | 0.006 | 10/26 (RPMI-7951, A498, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **2.06×** | +3.7 | 0.007 | 9/27 (A-172, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.018 | 10/27 (A-172, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.96×** | +3.5 | 0.018 | 10/25 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.025 | 7/26 (HCT15, SW480, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.049 | 7/27 (HepG2/C3A, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2370.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.598×** | -5.0 | 2e-04 | 18/26 (A498, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.602×** | -5.0 | 2e-04 | 19/27 (A498, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.600×** | -4.8 | 3e-04 | 14/26 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.681×** | -3.8 | 0.023 | 12/27 (SW1417, A498, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.685×** | -3.7 | 0.024 | 12/26 (NCI-H2030, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM |  | **0.773×** | -3.6 | 0.035 | 9/27 (BT-474, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.704×** | -3.4 | 0.047 | 15/26 (BT-474, HCT15, …) | rises with dose | position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | **0.515×** | -3.4 | 0.047 | 12/27 (BT-474, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.720×** | -3.2 | 0.080 | 14/25 (COLO 205, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.727× | -3.1 | 0.10 | 13/27 (COLO 205, CHP-212, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.729× | -3.1 | 0.10 | 11/26 (A498, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.553× | -3.0 | 0.11 | 6/27 (BT-474, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 0.736× | -3.0 | 0.12 | 6/26 (hTERT-HPNE, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 33.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 2.56× (z +9.9) | — |
| [[A498 (line)]] | wt | 81.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +10.9) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.325× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 21.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +10.8) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 33.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 59.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[ULK-101 (drug)]] 5 µM 0.0512× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 57.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 60.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 7.87 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 55.9 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0814× (z -9.7) |
| [[PANC-1 (line)]] | alt | 5.61 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.23× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.970 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.25 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRXL2A]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[TMEM135]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[GSTM4]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[ATP6V1A]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[CMBL]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[MAP2K6]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[SNX2]] | +0.55 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CLN3]] | +0.55 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[DENND4C]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[TRIM2]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PALS1]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[SCPEP1]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCCD1]] | -0.54 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[AGO2]] | -0.49 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[LRWD1]] | -0.49 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[WDR27]] | -0.48 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PLGRKT]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[EEFSEC]] | -0.48 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[ZBED4]] | -0.47 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[CRYGS]] | -0.47 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[TEX30]] | -0.47 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[SMIM12]] | -0.47 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[CCM2]] | -0.47 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[CPSF3]] | -0.45 | -0.33 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AP1M2]] | B | AP1M2 activity raises QPRT's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 2.15× lower at baseline in the lines without AP1M2 | 0.062 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |
| [[SERPINF1]] | C | SERPINF1 activity raises QPRT's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 3.95× lower at baseline in the lines without SERPINF1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP6V1A]] | B | QPRT activity raises ATP6V1A's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.41× lower at baseline in the lines without QPRT | 0.013 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[FGD3]] | B | QPRT activity raises FGD3's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.50× lower at baseline in the lines without QPRT | 0.013 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[SLC7A8]] | B | QPRT activity raises SLC7A8's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.65× lower at baseline in the lines without QPRT | 0.031 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[ARMH1]] | B | QPRT activity raises ARMH1's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.49× lower at baseline in the lines without QPRT | 0.031 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[ERG28]] | B | QPRT activity raises ERG28's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.23× lower at baseline in the lines without QPRT | 0.049 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[PECR]] | B | QPRT activity raises PECR's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.48× lower at baseline in the lines without QPRT | 0.060 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[DHCR7]] | B | QPRT activity raises DHCR7's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.33× lower at baseline in the lines without QPRT | 0.084 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[PREPL]] | B | QPRT activity raises PREPL's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.10× lower at baseline in the lines without QPRT | 0.090 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[AMOT]] | B | QPRT activity raises AMOT's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.93× lower at baseline in the lines without QPRT | 0.095 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[TEX30]] | B | QPRT activity raises TEX30's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without QPRT | 0.0998 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.8, -7.8); signed map (-26.2, -4.1). **Vector** length 59.6, 14.3% of its response variance represented; |z| ≥ 3 in 572 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +11.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.5 | +4.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.5 | +5.7 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.2 | -5.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | quinolinate phosphoribosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,663,279-29,698,699 (+) |
| Ensembl biotype | protein_coding |
| Also known as | QPRTase |
| Gene groups (HGNC) | Phosphoribosyltransferases |
| Reactome | 3 pathways, smallest: Nicotinate metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15274](https://www.uniprot.org/uniprotkb/Q15274) (Nicotinate-nucleotide pyrophosphorylase):

> Involved in the catabolism of quinolinic acid (QA).

**Summary**, from NCBI Gene [23475](https://www.ncbi.nlm.nih.gov/gene/23475):

> This gene encodes a key enzyme in catabolism of quinolinate, an intermediate in the tryptophan-nicotinamide adenine dinucleotide pathway. Quinolinate acts as a most potent endogenous exitotoxin to neurons. Elevation of quinolinate levels in the brain has been linked to the pathogenesis of neurodegenerative disorders such as epilepsy, Alzheimer's disease, and Huntington's disease. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:9755](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9755) · Entrez [23475](https://www.ncbi.nlm.nih.gov/gene/23475) · UniProt [Q15274](https://www.uniprot.org/uniprotkb/Q15274) · Ensembl [ENSG00000103485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103485)

## Data

Gene col 2370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2370); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2370]; `tensor/DDL_lfc|DDL_z.npy` [2370]; `embed/gene_vectors.npy` [2370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2370 or target_col == 2370). Every well: [[QPRT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/QPRT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
