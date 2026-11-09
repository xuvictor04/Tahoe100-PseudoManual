---
symbol: "SSBP4"
type: "gene"
col: 5072
ensembl_id: "ENSG00000130511"
name: "single stranded DNA binding protein 4"
location: "19p13.11"
module: 77
arm: "+"
pooled_cpm: 15.42
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 25
n_dd_up_clean: 7
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# SSBP4

*single stranded DNA binding protein 4* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.43× (z +5.7, q 8e-06, up in 15 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.52× (z +5.0, q 1e-04, up in 16 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.312× (z -27.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GFOD2]] (+0.68, fdr 8e-06), [[BRAT1]] (+0.66, fdr 1e-05), [[ANKRD13B]] (+0.66, fdr 7e-06); moves opposite to [[C11orf58]] (-0.66, fdr 1e-05), [[TRIP11]] (-0.63, fdr 2e-05), [[UBQLN2]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ARHGAP44]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5072.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +5.7 | 8e-06 | 15/30 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +5.1 | 1e-04 | 18/38 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +5.0 | 1e-04 | 16/45 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +4.8 | 2e-04 | 18/47 (SW480, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +4.4 | 0.001 | 18/48 (NCI-H2347, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **1.30×** | +4.2 | 0.002 | 12/44 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.9 | 0.008 | 14/48 (HS-578T, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.013 | 14/47 (CHP-212, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.041 | 4/48 (BT-474, J82, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.069 | 12/46 (SHP-77, SW48, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.069 | 4/48 (A498, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5072.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.312×** | -27.3 | 0e+00 | 46/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.327×** | -18.6 | 0e+00 | 47/47 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.369×** | -15.9 | 0e+00 | 41/48 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.566×** | -9.4 | 5e-19 | 32/48 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.623×** | -7.9 | 5e-13 | 29/48 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.639×** | -7.4 | 1e-11 | 28/47 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.646×** | -7.2 | 4e-11 | 28/47 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.419×** | -6.7 | 1e-09 | 27/48 (COLO 205, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.656×** | -6.6 | 3e-09 | 25/48 (LoVo, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.684×** | -6.3 | 2e-08 | 25/47 (C32, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.688×** | -6.2 | 3e-08 | 20/46 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.700×** | -5.9 | 2e-07 | 25/47 (LS 180, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.750×** | -4.8 | 9e-05 | 21/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.754×** | -4.7 | 1e-04 | 20/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.782×** | -4.1 | 0.002 | 11/48 (HS-578T, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.782×** | -3.9 | 0.003 | 16/46 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.620×** | -3.7 | 0.007 | 9/48 (C-33 A, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5072. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 48.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -16.8) |
| [[LOX-IMVI (line)]] | wt | 20.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -17.8) |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -19.3) |
| [[NCI-H460 (line)]] | wt | 11.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -16.9) |
| [[A549 (line)]] | wt | 12.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0739× (z -21.2) |
| [[PANC-1 (line)]] | alt | 18.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -22.8) |
| [[A-172 (line)]] | wt | 35.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -13.8) |
| [[BT-474 (line)]] | alt | 9.44 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -11.0) |
| [[HOP62 (line)]] | alt | 7.68 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -16.2) |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -15.0) |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -9.4) |
| [[LoVo (line)]] | wt | 14.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 17.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -18.4) |
| [[NCI-H23 (line)]] | alt | 23.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 15.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.2) |
| [[RKO (line)]] | wt | 13.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0686× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 2 | — | [[XRK3F2 (drug)]] 0.5 µM 0.111× (z -8.8) |
| [[SNU-423 (line)]] | alt | 13.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -15.4) |
| [[SW48 (line)]] | wt | 19.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0561× (z -13.0) |
| [[SW480 (line)]] | alt | 9.50 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.290× (z -12.8) |
| [[A-427 (line)]] | wt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -10.5) |
| [[COLO 205 (line)]] | alt | 8.15 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -8.9) |
| [[H4 (line)]] | wt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0744× (z -11.7) |
| [[HT-29 (line)]] | alt | 8.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -9.6) |
| [[J82 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 6.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -8.8) |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -9.2) |
| [[SW 900 (line)]] | alt | 13.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -9.2) |
| [[SW1417 (line)]] | alt | 9.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.2) |
| [[A498 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5072), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GFOD2]] | +0.68 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[BRAT1]] | +0.66 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ANKRD13B]] | +0.66 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[CORO7]] | +0.65 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[TSEN54]] | +0.65 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[TMEM120B]] | +0.65 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[GRAMD4]] | +0.65 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[STK32C]] | +0.65 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[PDXP]] | +0.64 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[ANKRD13D]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[SMARCD3]] | +0.63 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[NPDC1]] | +0.63 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf58]] | -0.66 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.63 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[UBQLN2]] | -0.63 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[RNF6]] | -0.62 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[ARCN1]] | -0.61 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[MCTS1]] | -0.60 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[ZC3H11A]] | -0.60 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[LIG4]] | -0.59 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[PCNX4-DT]] | -0.59 | -0.65 / -0.30 | both halves | 2e-04 |  |
| [[RIPK2-DT]] | -0.59 | -0.64 / -0.37 | both halves | 7e-05 |  |
| [[ZXDB]] | -0.58 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[THAP5]] | -0.58 | -0.66 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP44]] | B | ARHGAP44 activity raises SSBP4's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.33× lower at baseline in the lines without ARHGAP44 | 0.021 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[STARD9]] | B | STARD9 activity raises SSBP4's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without STARD9 | 0.027 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[CHD5]] | B | CHD5 activity raises SSBP4's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.24× lower at baseline in the lines without CHD5 | 0.030 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[SLC29A4]] | B | SLC29A4 activity raises SSBP4's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.82× lower at baseline in the lines without SLC29A4 | 0.046 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[CTXN1]] | B | CTXN1 activity raises SSBP4's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without CTXN1 | 0.082 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[GNAZ]] | B | GNAZ activity raises SSBP4's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.52× lower at baseline in the lines without GNAZ | 0.082 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[SMARCD3]] | C | SMARCD3 activity raises SSBP4's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 2.05× lower at baseline in the lines without SMARCD3 | 0.061 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.699). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-1.8, -1.0); signed map (-42.4, -3.7). **Vector** length 85.2, 17.2% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.4 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +5.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -18.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.7 | -27.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -15.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | single stranded DNA binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,418,864-18,434,562 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Wnt enhanceosome complex |
| Matched by | ensembl_id |

UniProt [Q9BWG4](https://www.uniprot.org/uniprotkb/Q9BWG4) carries no function annotation.

**Summary**, from NCBI Gene [170463](https://www.ncbi.nlm.nih.gov/gene/170463):

> Predicted to enable transcription coactivator activity. Predicted to be involved in positive regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15676](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15676) · Entrez [170463](https://www.ncbi.nlm.nih.gov/gene/170463) · UniProt [Q9BWG4](https://www.uniprot.org/uniprotkb/Q9BWG4) · Ensembl [ENSG00000130511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130511)

## Data

Gene col 5072: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5072); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5072, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5072]; `tensor/DDL_lfc|DDL_z.npy` [5072]; `embed/gene_vectors.npy` [5072]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5072 or target_col == 5072). Every well: [[SSBP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSBP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
