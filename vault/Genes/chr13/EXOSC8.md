---
symbol: "EXOSC8"
type: "gene"
col: 4210
ensembl_id: "ENSG00000120699"
name: "exosome component 8"
location: "13q13.3"
module: 28
arm: "+"
pooled_cpm: 28.68
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# EXOSC8

*exosome component 8* — 13q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.44× (z +17.6, q 0e+00, up in 38 of 38 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (SHP-77 10.6×, HEC-1-A 7.75×, NCI-H460 8.12×, LoVo 7.30×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LoVo 8.60×, NCI-H460 7.50×, J82 5.95×, HOP62 9.18×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 3.63×; ⚠ cell-cycle shift, explains ~60% of this change).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.778× (z -4.3, q 0.010, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGOHB]] (+0.70, fdr 7e-06), [[CCDC25]] (+0.63, fdr 3e-05), [[ZC3H7A]] (+0.61, fdr 1e-05); moves opposite to [[UBL5]] (-0.54, fdr 8e-05), [[PRDX1]] (-0.53, fdr 3e-05), [[TSPAN17]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4210.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (SHP-77 10.6×, HEC-1-A 7.75×, NCI-H460 8.12×, LoVo 7.30×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LoVo 8.60×, NCI-H460 7.50×, J82 5.95×, HOP62 9.18×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 3.63×; ⚠ cell-cycle shift, explains ~60% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.44×** | +17.6 | 0e+00 | 38/38 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.08×** | +15.5 | 0e+00 | 42/43 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.63×** | +11.0 | 1e-25 | 37/40 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.66×** | +8.8 | 1e-16 | 39/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.77×** | +6.7 | 2e-09 | 39/48 (NCI-H460, RKO, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.3 | 0.001 | 24/46 (SW1417, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.42×** | +3.9 | 0.008 | 25/48 (NCI-H460, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.33×** | +3.5 | 0.031 | 24/47 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **1.33×** | +3.4 | 0.042 | 22/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.63×** | +3.2 | 0.092 | 16/48 (SW 900, NCI-H460, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.28× | +3.0 | 0.12 | 19/47 (LoVo, SW48, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4210.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.778×** | -4.3 | 0.010 | 24/48 (HOP62, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -3.9 | 0.019 | 21/47 (SW48, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.726×** | -3.9 | 0.019 | 28/48 (SW1417, SW 1088, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.733×** | -3.8 | 0.023 | 23/48 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.747×** | -3.5 | 0.044 | 19/48 (C-33 A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.761×** | -3.3 | 0.083 | 20/48 (HT-29, SW 1088, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.754×** | -3.2 | 0.097 | 15/48 (RKO, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4210. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.6 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.12× (z +15.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 25.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.60× (z +15.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 35.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.75× (z +16.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 17.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.20× (z +14.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 33.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.38× (z +13.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 43.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.15× (z +15.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 24.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.83× (z +13.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 50.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.56× (z +14.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 41.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.10× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 16.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.9× (z +14.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 18.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.6× (z +13.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 20.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.80× (z +11.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 50.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.18× (z +11.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 22.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.58× (z +11.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 23.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.44× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.37× (z +9.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 32.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +9.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 27.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 40.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.6× (z +17.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 28.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 22.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.45× (z +10.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 20.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.14× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 21.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.48× (z +10.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 41.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +12.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 37.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +12.8) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[RPMI-7951 (line)]] | alt | 28.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.84× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 36.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.66× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.57× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4210), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGOHB]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[CCDC25]] | +0.63 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[ZC3H7A]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ICE2]] | +0.58 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[DDX1]] | +0.57 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[MKS1]] | +0.57 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[SMARCE1]] | +0.57 | +0.61 / +0.45 | both halves | 3e-05 | pathway: Affinity selection of immunoglobulins |
| [[DXO]] | +0.56 | +0.64 / +0.37 | both halves | 8e-05 | pathway: Nuclear RNA decay |
| [[COPS5]] | +0.56 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[C2CD5]] | +0.56 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[NDUFA5]] | +0.56 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[ZNF678]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBL5]] | -0.54 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[PRDX1]] | -0.53 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[TSPAN17]] | -0.53 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[HSBP1]] | -0.51 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[ORMDL2]] | -0.51 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[FRMD8]] | -0.50 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[APRT]] | -0.49 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[TBC1D2]] | -0.49 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[CAP1]] | -0.48 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[LUZP1]] | -0.48 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[CD9]] | -0.47 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[HTRA2]] | -0.47 | -0.39 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises EXOSC8's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.2, 4.1); signed map (7.5, -25.9). **Vector** length 81.0, 19.6% of its response variance represented; |z| ≥ 3 in 698 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +7.1 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +15.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +17.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.4 | +6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.8 | +0.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.7 | -0.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.7 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.6 | -1.4 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | exosome component 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.3 — chr13:36,998,816-37,025,881 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OIP2, RRP43, bA421P11.3, Rrp43p, EAP2, p9, CIP3 |
| Gene groups (HGNC) | Exosome complex |
| Hallmark sets | E2F_TARGETS |
| Reactome | 20 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; KSRP (KHSRP) binds and destabilizes mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96B26](https://www.uniprot.org/uniprotkb/Q96B26) (Exosome complex component RRP43):

> Non-catalytic component of the RNA exosome complex which has 3'->5' exoribonuclease activity and participates in a multitude of cellular RNA processing and degradation events. In the nucleus, the RNA exosome complex is involved in proper maturation of stable RNA species such as rRNA, snRNA and snoRNA, in the elimination of RNA processing by-products and non-coding 'pervasive' transcripts, such as antisense RNA species and promoter-upstream transcripts (PROMPTs), and of mRNAs with processing …

**Summary**, from NCBI Gene [11340](https://www.ncbi.nlm.nih.gov/gene/11340):

> This gene encodes a 3'-5' exoribonuclease that specifically interacts with mRNAs containing AU-rich elements. The encoded protein is part of the exosome complex that is important for the degradation of numerous RNA species. A pseudogene of this gene is found on chromosome 6. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:17035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17035) · Entrez [11340](https://www.ncbi.nlm.nih.gov/gene/11340) · UniProt [Q96B26](https://www.uniprot.org/uniprotkb/Q96B26) · Ensembl [ENSG00000120699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120699)

## Data

Gene col 4210: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4210); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4210, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4210]; `tensor/DDL_lfc|DDL_z.npy` [4210]; `embed/gene_vectors.npy` [4210]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4210 or target_col == 4210). Every well: [[EXOSC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOSC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
