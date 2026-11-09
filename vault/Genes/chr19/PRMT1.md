---
symbol: "PRMT1"
type: "gene"
col: 4736
ensembl_id: "ENSG00000126457"
name: "protein arginine methyltransferase 1"
location: "19q13.33"
module: 4
arm: "+"
pooled_cpm: 34.55
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# PRMT1

*protein arginine methyltransferase 1* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.11× (z +14.4, q 4e-44, up in 43 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +6.3, q 3e-08, up in 33 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VARS1]] (+0.65, fdr 7e-06), [[IPO4]] (+0.64, fdr 7e-06), [[SLC5A6]] (+0.62, fdr 7e-06); moves opposite to [[PSMA7]] (-0.57, fdr 1e-04), [[RIOK3]] (-0.52, fdr 4e-05), [[BCAS2]] (-0.51, fdr 3e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4736.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.11×** | +14.4 | 4e-44 | 43/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.60×** | +11.6 | 8e-29 | 36/40 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.38×** | +10.1 | 7e-22 | 38/44 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.95×** | +8.1 | 5e-14 | 45/47 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.83×** | +7.6 | 3e-12 | 40/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.68×** | +6.5 | 6e-09 | 37/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.3 | 3e-08 | 33/48 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +5.9 | 2e-07 | 27/48 (PANC-1, A549, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +5.5 | 2e-06 | 37/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.54×** | +5.4 | 4e-06 | 34/45 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.56×** | +5.4 | 4e-06 | 32/48 (PANC-1, A549, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.49×** | +5.0 | 3e-05 | 28/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.44×** | +4.6 | 2e-04 | 26/48 (PANC-1, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.41×** | +4.4 | 5e-04 | 28/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.42×** | +4.3 | 8e-04 | 23/48 (MIA PaCa-2, NCI-H23, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.90×** | +4.1 | 0.002 | 33/48 (SW 900, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.81×** | +3.8 | 0.005 | 22/46 (A498, SW1417, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.005 | 20/48 (HS-578T, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.76×** | +3.6 | 0.009 | 21/48 (CFPAC-1, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.009 | 24/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.64×** | +3.1 | 0.040 | 19/47 (RPMI-7951, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.044 | 12/47 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.058 | 13/48 (NCI-H460, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.57×** | +2.9 | 0.081 | 16/46 (CFPAC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.56×** | +2.8 | 0.085 | 14/46 (C32, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4736.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.723× | -3.4 | 0.32 | 23/48 (C-33 A, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4736. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.9 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +14.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 47.0 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 22.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 17.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 34.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.2) | — |
| [[C32 (line)]] | wt | 17.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 23.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 29.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 24.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 21.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.98× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Panc 03.27 (line)]] | alt | 32.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 44.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 46.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 48.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 40.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 37.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.18× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 37.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 53.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 30.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2347 (line)]] | alt | 29.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4736), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VARS1]] | +0.65 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[IPO4]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SLC5A6]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[UBQLN4]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[PFAS]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[WDR46]] | +0.57 | +0.63 / +0.52 | both halves | 1e-05 | same gene group |
| [[ATP13A1]] | +0.56 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[KAT2A]] | +0.55 | +0.58 / +0.46 | both halves | 2e-05 | pathway: Chromatin modifying enzymes; STRING 445 |
| [[CLUH]] | +0.55 | +0.57 / +0.56 | both halves | 1e-05 | same gene group |
| [[BOP1]] | +0.54 | +0.56 / +0.61 | both halves | 1e-05 | same gene group |
| [[GTPBP6]] | +0.54 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[WIZ]] | +0.52 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA7]] | -0.57 | -0.34 / -0.56 | both halves | 1e-04 | pathway: Transcriptional regulation by RUNX1 |
| [[RIOK3]] | -0.52 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[BCAS2]] | -0.51 | -0.28 / -0.61 | both halves | 3e-04 |  |
| [[ZNF430]] | -0.48 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[KLHL20]] | -0.48 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[ZNF611]] | -0.48 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[ZCRB1]] | -0.47 | -0.37 / -0.46 | both halves | 8e-05 | same gene group; pathway: SARS-CoV-2 Infection |
| [[GLTP]] | -0.46 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[TMEM191A-1]] | -0.45 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ZER1]] | -0.45 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[CTR9]] | -0.45 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[SNAP29]] | -0.44 | -0.28 / -0.51 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.344). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-17.3, -33.0); signed map (-5.2, -44.5). **Vector** length 61.6, 13.4% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.8 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.6 | +14.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +3.3 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +3.2 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +4.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.3 | +2.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | +1.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | +1.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.1 | +0.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | protein arginine methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,675,786-49,689,029 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HCP1, ANM1; previously HRMT1L2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; 7BS protein arginine methyltranferases; Arginine methyltransferases |
| Reactome | 18 pathways, smallest: Maturation of nucleoprotein_9694631; TP53 Regulates Transcription of Genes Involved in G2 Cell Cycle Arrest; RMTs methylate histone arginines |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99873](https://www.uniprot.org/uniprotkb/Q99873) (Protein arginine N-methyltransferase 1):

> Arginine methyltransferase that methylates (mono and asymmetric dimethylation) the guanidino nitrogens of arginyl residues present in proteins such as ESR1, histone H2, H3 and H4, FMR1, ILF3, HNRNPA1, HNRNPD, NFATC2IP, SUPT5H, TAF15, EWS, HABP4, SERBP1, RBM15, FOXO1, CHTOP, MAP3K5/ASK1, MICU1 and NPRL2. Constitutes the main enzyme that mediates monomethylation and asymmetric dimethylation of histone H4 'Arg-3' (H4R3me1 and H4R3me2a, respectively), a specific tag for epigenetic transcriptional …

**Summary**, from NCBI Gene [3276](https://www.ncbi.nlm.nih.gov/gene/3276):

> This gene encodes a member of the protein arginine N-methyltransferase (PRMT) family. Post-translational modification of target proteins by PRMTs plays an important regulatory role in many biological processes, whereby PRMTs methylate arginine residues by transferring methyl groups from S-adenosyl-L-methionine to terminal guanidino nitrogen atoms. The encoded protein is a type I PRMT and is responsible for the majority of cellular arginine methylation activity. Increased expression of this gene …

**Accessions** — [HGNC:5187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5187) · Entrez [3276](https://www.ncbi.nlm.nih.gov/gene/3276) · UniProt [Q99873](https://www.uniprot.org/uniprotkb/Q99873) · Ensembl [ENSG00000126457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126457)

## Data

Gene col 4736: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4736); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4736, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4736]; `tensor/DDL_lfc|DDL_z.npy` [4736]; `embed/gene_vectors.npy` [4736]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4736 or target_col == 4736). Every well: [[PRMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
