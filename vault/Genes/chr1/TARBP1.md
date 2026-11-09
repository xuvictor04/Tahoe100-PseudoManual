---
symbol: "TARBP1"
type: "gene"
col: 675
ensembl_id: "ENSG00000059588"
name: "tRNA guanosine 2 -O-methyltransferase TARBP1"
location: "1q42.2"
module: 18
arm: "+"
pooled_cpm: 48.44
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 22
n_dd_up_clean: 13
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TARBP1

*tRNA guanosine 2 -O-methyltransferase TARBP1* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.33× (z +7.7, q 6e-12, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.397× (z -17.8, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC88C]] (+0.65, fdr 7e-06), [[HEATR3]] (+0.64, fdr 7e-06), [[LRRC8D]] (+0.64, fdr 1e-05); moves opposite to [[TOX4]] (-0.54, fdr 1e-05), [[ZFYVE1]] (-0.54, fdr 1e-05), [[ZBTB43]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ADAMTS9-AS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 675.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +7.7 | 6e-12 | 29/48 (A-172, HOP62, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +5.8 | 1e-06 | 26/48 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +5.8 | 1e-06 | 23/48 (A-172, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +4.8 | 2e-04 | 23/48 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +4.3 | 0.002 | 20/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.2 | 0.003 | 0/48 | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.004 | 11/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.005 | 21/48 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Regorafenib (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.006 | 14/48 (SHP-77, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.007 | 14/48 (A-172, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.8 | 0.007 | 18/48 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.018 | 12/47 (NCI-H1573, COLO 205, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.018 | 6/48 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.018 | 9/47 (PANC-1, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 675.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.397×** | -17.8 | 0e+00 | 44/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.487×** | -13.9 | 2e-41 | 36/47 (PANC-1, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -13.5 | 4e-39 | 34/47 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.615×** | -13.3 | 4e-38 | 30/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.527×** | -12.4 | 4e-33 | 33/48 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.543×** | -11.8 | 4e-30 | 32/48 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.561×** | -11.2 | 5e-27 | 34/47 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.578×** | -10.6 | 3e-24 | 38/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -10.3 | 3e-23 | 29/48 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.590×** | -9.8 | 6e-21 | 31/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -9.2 | 2e-18 | 29/48 (A498, SNU-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.617×** | -8.8 | 7e-17 | 29/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.545×** | -6.1 | 4e-08 | 25/42 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.766×** | -5.1 | 1e-05 | 21/46 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.780×** | -4.8 | 7e-05 | 22/47 (PANC-1, SW48, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.764×** | -4.5 | 3e-04 | 17/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.805×** | -4.0 | 0.002 | 16/47 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.818×** | -3.9 | 0.003 | 17/47 (SW 1271, J82, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 144 | 0 | 22 (10 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -29.6) |
| [[NCI-H23 (line)]] | alt | 69.0 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -21.7) |
| [[NCI-H460 (line)]] | wt | 99.8 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -16.8) |
| [[A-427 (line)]] | wt | 65.0 | 0 | 11 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -14.6) |
| [[SNU-1 (line)]] | wt | 90.7 | 0 | 11 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0161× (z -29.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0343× (z -23.8) |
| [[MIA PaCa-2 (line)]] | alt | 97.5 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -33.2) |
| [[C-33 A (line)]] | alt | 81.3 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -19.2) |
| [[A498 (line)]] | wt | 58.5 | 0 | 7 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.266× (z -15.5) |
| [[HT-29 (line)]] | alt | 38.2 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.281× (z -15.0) |
| [[SW1417 (line)]] | alt | 63.1 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -12.3) |
| [[SW48 (line)]] | wt | 100 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0793× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -10.3) |
| [[LoVo (line)]] | wt | 41.3 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -13.1) |
| [[RKO (line)]] | wt | 38.2 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0913× (z -16.4) |
| [[HEC-1-A (line)]] | alt | 61.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -20.8) |
| [[J82 (line)]] | alt | 51.4 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -12.6) |
| [[A-172 (line)]] | wt | 24.8 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.65× (z +11.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.83× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 35.3 | 0 | 4 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.112× (z -9.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -8.8) |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 32.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -11.9) |
| [[A549 (line)]] | wt | 45.8 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.266× (z -11.9) |
| [[C32 (line)]] | wt | 27.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 28.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.274× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 22.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -16.0) |
| [[SW480 (line)]] | alt | 52.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.2) |
| [[AN3 CA (line)]] | alt | 63.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.109× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 24.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.0) |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.358× (z -8.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 33.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.311× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 675), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC88C]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[HEATR3]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 | same gene group |
| [[LRRC8D]] | +0.64 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[TSEN2]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[FXN]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CLYBL]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[STX18-AS1]] | +0.61 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[UCK2]] | +0.59 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[ASIC1]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PMS1]] | +0.59 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[TMTC4]] | +0.59 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[ASB13]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOX4]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ZFYVE1]] | -0.54 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ZBTB43]] | -0.52 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[RP2]] | -0.50 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[ADAMTS9-AS2]] | -0.50 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ATP6V1G1]] | -0.50 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[PRR13]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[SYNRG]] | -0.48 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[C9orf24]] | -0.48 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[RAB5B]] | -0.48 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS9-AS2]] | B | ADAMTS9-AS2 activity lowers TARBP1's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 1.52× higher at baseline in the lines without ADAMTS9-AS2 | 0.065 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[FTCDNL1]] | B | FTCDNL1 activity raises TARBP1's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.60× lower at baseline in the lines without FTCDNL1 | 0.095 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[ADAM22]] | B | ADAM22 activity raises TARBP1's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 1.87× lower at baseline in the lines without ADAM22 | 0.096 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[MCOLN2]] | B | MCOLN2 activity raises TARBP1's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.31× lower at baseline in the lines without MCOLN2 | 0.097 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[UBE2D4]] | C | UBE2D4's natural level strengthens TARBP1's drug response | UBE2D4's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.34; direction not clear | 0.094 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.2, -40.1); signed map (-7.4, -53.6). **Vector** length 109, 31.0% of its response variance represented; |z| ≥ 3 in 1,240 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +3.8 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +7.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.5 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -4.6 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.5 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -13.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -10.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.2 | -3.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -3.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.2 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | tRNA guanosine 2 -O-methyltransferase TARBP1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:234,391,313-234,479,179 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRP-185, TRM3, TRMT3 |
| Gene groups (HGNC) | SPOUT methyltransferase domain containing; Armadillo like helical domain containing; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13395](https://www.uniprot.org/uniprotkb/Q13395) (tRNA):

> S-adenosyl-L-methionine-dependent 2'-O-ribose methyltransferase that catalyzes the formation of 2'-O-methylguanosine at position 18 (Gm18) in a subset of tRNA. Selectively mediates Gm18 methylation of tRNAGln-TTG/CTG and tRNASer-TGA/GCT. Gm18 modification can enhance the stability of modified tRNAs.; (Microbial infection) In case of infection by HIV-1, it binds to the loop region of TAR RNA, a region also bound by RNA polymerase II. Binding of TARBP1 and RNA polymerase II to HIV-1 TAR RNA is …

**Summary**, from NCBI Gene [6894](https://www.ncbi.nlm.nih.gov/gene/6894):

> HIV-1, the causative agent of acquired immunodeficiency syndrome (AIDS), contains an RNA genome that produces a chromosomally integrated DNA during the replicative cycle. Activation of HIV-1 gene expression by the transactivator Tat is dependent on an RNA regulatory element (TAR) located downstream of the transcription initiation site. This element forms a stable stem-loop structure and can be bound by either the protein encoded by this gene or by RNA polymerase II. This protein may act to …

**Accessions** — [HGNC:11568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11568) · Entrez [6894](https://www.ncbi.nlm.nih.gov/gene/6894) · UniProt [Q13395](https://www.uniprot.org/uniprotkb/Q13395) · Ensembl [ENSG00000059588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000059588)

## Data

Gene col 675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 675); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 675, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 675]; `tensor/DDL_lfc|DDL_z.npy` [675]; `embed/gene_vectors.npy` [675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 675 or target_col == 675). Every well: [[TARBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TARBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
