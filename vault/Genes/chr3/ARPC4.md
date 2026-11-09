---
symbol: "ARPC4"
type: "gene"
col: 14280
ensembl_id: "ENSG00000241553"
name: "actin related protein 2/3 complex subunit 4"
location: "3p25.3"
module: 111
arm: "+"
pooled_cpm: 37.48
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# ARPC4

*actin related protein 2/3 complex subunit 4* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.05× (z +23.9, q 0e+00, up in 44 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.79× (z +6.5, q 1e-08, up in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A498 4.10×, SW480 3.31×, KATO III 4.27×, NCI-H460 3.66×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 4.17×, A498 3.82×, KATO III 3.71×, HOP62 4.09×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 3.32×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.817× (z -6.1, q 5e-07, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR1]] (+0.76, fdr 7e-06), [[ACTR3]] (+0.69, fdr 1e-05), [[DBNL]] (+0.67, fdr 1e-05); moves opposite to [[C15orf61]] (-0.67, fdr 3e-05, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[TENT4B]] (-0.63, fdr 1e-05), [[ATP5MC2]] (-0.61, fdr 2e-05), [[TAF1D]] (-0.60, fdr 1e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14280.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A498 4.10×, SW480 3.31×, KATO III 4.27×, NCI-H460 3.66×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 4.17×, A498 3.82×, KATO III 3.71×, HOP62 4.09×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 3.32×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.05×** | +23.9 | 0e+00 | 44/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +19.3 | 0e+00 | 35/38 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +15.6 | 0e+00 | 36/41 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.79×** | +6.5 | 1e-08 | 28/48 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~7% of this change | **1.20×** | +4.0 | 0.008 | 19/46 (SW1417, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.9 | 0.008 | 11/48 (A-427, SW1417, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.6 | 0.024 | 17/48 (SW480, HCT15, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.6 | 0.027 | 5/48 (A498, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14280.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.817×** | -6.1 | 5e-07 | 23/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -5.6 | 5e-06 | 5/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -4.9 | 2e-04 | 21/47 (RKO, NCI-H2347, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.805×** | -4.7 | 5e-04 | 21/48 (A-172, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.801×** | -4.6 | 6e-04 | 18/47 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.713×** | -3.8 | 0.015 | 9/48 (RKO, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.864× | -3.5 | 0.036 | 13/48 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.845× | -3.3 | 0.064 | 11/48 (C32, SW480, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.858× | -3.1 | 0.10 | 19/46 (BT-474, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.868× | -3.0 | 0.13 | 12/48 (SW 1271, HOP62, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.864× | -3.0 | 0.13 | 16/47 (SNU-423, HS-578T, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14280. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 29.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +15.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 47.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 44.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 25.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +10.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 57.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +10.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 30.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 33.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +11.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 30.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +11.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 46.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 45.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +10.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 36.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +13.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 21.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +11.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 41.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +12.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 41.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +12.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 49.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.564× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 26.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +13.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 35.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +16.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 46.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +8.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.312× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +9.4) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 36.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.100× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 25.4 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0913× (z -12.8) |
| [[Hs 766T (line)]] | wt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 36.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 50.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +10.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +9.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 35.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +10.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 41.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 57.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 41.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 59.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0617× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14280), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR1]] | +0.76 | +0.66 / +0.78 | both halves | 7e-06 | STRING 582 |
| [[ACTR3]] | +0.69 | +0.53 / +0.75 | both halves | 1e-05 | same gene group; pathway: Clathrin-mediated endocytosis; STRING 999 |
| [[DBNL]] | +0.67 | +0.50 / +0.67 | both halves | 1e-05 | STRING 449 |
| [[CDC42]] | +0.66 | +0.59 / +0.71 | both halves | 7e-06 | pathway: EPH-Ephrin signaling; STRING 745 |
| [[MTRF1L]] | +0.64 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[CAPNS1]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SSU72]] | +0.63 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[KPNA4]] | +0.62 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[EIF2S1]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TADA3]] | +0.61 | +0.67 / +0.55 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ARF3]] | +0.61 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[NCBP1]] | +0.61 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[SMU1]] | +0.60 | +0.45 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 9 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf61]] ⚠ | -0.67 | -0.45 / -0.74 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TENT4B]] | -0.63 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[ATP5MC2]] | -0.61 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[TAF1D]] | -0.60 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[SNHG7]] | -0.59 | -0.42 / -0.69 | both halves | 4e-05 |  |
| [[CAMLG]] | -0.59 | -0.41 / -0.68 | both halves | 4e-05 |  |
| [[SMIM26]] ⚠ | -0.59 | -0.36 / -0.59 | both halves | 9e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NACA4P]] ⚠ | -0.59 | -0.45 / -0.58 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[C16orf87]] | -0.58 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[FAM182B]] | -0.58 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[RPL36AL]] ⚠ | -0.56 | -0.30 / -0.59 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[THAP3]] | -0.56 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[LSM2]] | -0.56 | -0.33 / -0.64 | both halves | 1e-04 |  |
| [[MRPL34]] | -0.55 | -0.30 / -0.65 | both halves | 2e-04 |  |
| [[LAMTOR5]] | -0.55 | -0.23 / -0.58 | both halves | 5e-04 |  |
| [[TMEM170A]] | -0.54 | -0.30 / -0.63 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ARPC4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.4, -18.8); signed map (-8.3, 34.4). **Vector** length 96.6, 21.5% of its response variance represented; |z| ≥ 3 in 780 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G-protein beta:gamma signalling* (reactome, mean cos +0.51 to 4); *G beta:gamma signalling through CDC42* (reactome, mean cos +0.56 to 3); *High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +23.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +19.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.1 | +2.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +1.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.1 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -6.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -2.6 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 2/3 complex subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,792,495-9,807,101 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p20-Arc, ARC20 |
| Gene groups (HGNC) | Actin related protein 2/3 complex subunits |
| Reactome | 19 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; EPHB-mediated forward signaling; FCGR3A-mediated phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P59998](https://www.uniprot.org/uniprotkb/P59998) (Actin-related protein 2/3 complex subunit 4):

> Actin-binding component of the Arp2/3 complex, a multiprotein complex that mediates actin polymerization upon stimulation by nucleation-promoting factor (NPF). The Arp2/3 complex mediates the formation of branched actin networks in the cytoplasm, providing the force for cell motility. In addition to its role in the cytoplasmic cytoskeleton, the Arp2/3 complex also promotes actin polymerization in the nucleus, thereby regulating gene transcription and repair of damaged DNA. The Arp2/3 complex …

**Summary**, from NCBI Gene [10093](https://www.ncbi.nlm.nih.gov/gene/10093):

> This gene encodes one of seven subunits of the human Arp2/3 protein complex. This complex controls actin polymerization in cells and has been conserved throughout eukaryotic evolution. This gene encodes the p20 subunit, which is necessary for actin nucleation and high-affinity binding to F-actin. Alternative splicing results in multiple transcript variants. Naturally occurring read-through transcription exists between this gene and the downstream tubulin tyrosine ligase-like family, member 3 …

**Accessions** — [HGNC:707](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:707) · Entrez [10093](https://www.ncbi.nlm.nih.gov/gene/10093) · UniProt [P59998](https://www.uniprot.org/uniprotkb/P59998) · Ensembl [ENSG00000241553](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241553)

## Data

Gene col 14280: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14280); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14280, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14280]; `tensor/DDL_lfc|DDL_z.npy` [14280]; `embed/gene_vectors.npy` [14280]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14280 or target_col == 14280). Every well: [[ARPC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARPC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
