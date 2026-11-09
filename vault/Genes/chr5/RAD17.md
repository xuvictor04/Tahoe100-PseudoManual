---
symbol: "RAD17"
type: "gene"
col: 7671
ensembl_id: "ENSG00000152942"
name: "RAD17 checkpoint clamp loader component"
location: "5q13.2"
module: 17
arm: "+"
pooled_cpm: 45.75
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# RAD17

*RAD17 checkpoint clamp loader component* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.80× (z +14.0, q 8e-42, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.487× (z -17.1, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYM6]] (+0.74, fdr 7e-06), [[MRPS31P4]] (+0.71, fdr 1e-05), [[FRA10AC1]] (+0.70, fdr 7e-06); moves opposite to [[DDX5]] (-0.69, fdr 7e-06), [[ARSB]] (-0.63, fdr 3e-05), [[GCNT4]] (-0.58, fdr 2e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PLEKHA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7671.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +14.0 | 8e-42 | 45/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +13.7 | 3e-40 | 43/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +12.2 | 1e-31 | 44/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +8.9 | 1e-16 | 27/48 (NCI-H2347, RKO, …) | rises with dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +5.4 | 6e-06 | 26/48 (NCI-H460, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.25×** | +5.3 | 9e-06 | 27/48 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +5.2 | 1e-05 | 23/48 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +5.1 | 3e-05 | 22/48 (LS 180, J82, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.3 | 1e-03 | 18/48 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.7 | 0.015 | 16/48 (NCI-H2030, KATO III, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.032 | 7/48 (HCT15, Panc 03.27, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.10× | +3.3 | 0.052 | 5/48 (SNU-423, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7671.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.487×** | -17.1 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.493×** | -16.8 | 0e+00 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.511×** | -15.9 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.607×** | -11.8 | 4e-30 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.675×** | -9.3 | 1e-18 | 34/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.700×** | -8.1 | 4e-14 | 35/47 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.712×** | -8.0 | 7e-14 | 30/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.742×** | -6.8 | 8e-10 | 26/48 (NCI-H23, A549, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.820×** | -6.6 | 2e-09 | 28/48 (A498, CHP-212, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.800×** | -5.3 | 7e-06 | 21/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.779×** | -5.2 | 8e-06 | 22/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -5.2 | 8e-06 | 0/49 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.661×** | -5.1 | 1e-05 | 26/44 (SK-MEL-2, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.808×** | -5.0 | 2e-05 | 24/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.796×** | -5.0 | 2e-05 | 24/43 (NCI-H23, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.832×** | -4.4 | 4e-04 | 13/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.716×** | -4.1 | 0.001 | 18/48 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.809×** | -3.6 | 0.010 | 11/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.905× | -3.3 | 0.021 | 6/48 (NCI-H1792, HOP62, …) | inconsistent across doses | position effect removed |
| [[Gefitinib (drug)]] 5 µM |  | 0.887× | -2.8 | 0.099 | 2/48 (NCI-H460, SW 900) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.7 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -16.0) |
| [[PANC-1 (line)]] | alt | 72.0 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.341× (z -17.6) |
| [[SW480 (line)]] | alt | 53.4 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.183× (z -24.8) |
| [[SHP-77 (line)]] | alt | 47.8 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -12.1) |
| [[LS 180 (line)]] | wt | 35.5 | 1 | 2 | [[Panobinostat (drug)]] 0.5 µM 2.45× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.337× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 54.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 52.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 31.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.232× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.320× (z -9.5) |
| [[CHP-212 (line)]] | wt | 40.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -11.4) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.140× (z -8.9) |
| [[HS-578T (line)]] | alt | 41.6 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.386× (z -8.6) |
| [[HT-29 (line)]] | alt | 37.8 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.149× (z -9.2) ⚠ toxic |
| [[J82 (line)]] | alt | 32.3 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.331× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 36.4 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.322× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 80.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.505× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 34.4 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -10.9) ⚠ cell-cycle shift, explains ~5% of this change |
| [[SW 900 (line)]] | alt | 47.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.326× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.359× (z -9.0) |
| [[A498 (line)]] | wt | 46.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -11.6) ⚠ cell-cycle shift, explains ~5% of this change |
| [[A549 (line)]] | wt | 38.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C-33 A (line)]] | alt | 43.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 30.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -13.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 21.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.318× (z -9.0) |
| [[LoVo (line)]] | wt | 63.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.03× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 46.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.430× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.102× (z -9.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 47.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -10.4) |
| [[SW48 (line)]] | wt | 34.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7671), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM6]] | +0.74 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[MRPS31P4]] | +0.71 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[FRA10AC1]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[HEATR6]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ACTR10]] | +0.69 | +0.68 / +0.57 | both halves | 8e-06 |  |
| [[TAMM41]] | +0.69 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.68 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[HEATR5B]] | +0.67 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[INIP]] | +0.67 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[POT1]] | +0.67 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[RARS1]] | +0.66 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[ZCRB1]] | +0.65 | +0.62 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.69 | -0.59 / -0.70 | both halves | 7e-06 |  |
| [[ARSB]] | -0.63 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[GCNT4]] | -0.58 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[PLEKHA6]] | -0.58 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[HNRNPAB]] | -0.57 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[E2F3]] | -0.56 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[TMEM117]] | -0.55 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[HCFC1]] | -0.55 | -0.60 / -0.32 | both halves | 2e-04 |  |
| [[SATB2]] | -0.54 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[PSPC1]] | -0.54 | -0.46 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA6]] | B | PLEKHA6 activity lowers RAD17's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.18× higher at baseline in the lines without PLEKHA6 | 0.067 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers RAD17's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF704]] | B | ZNF704 activity lowers RAD17's level | lines that do not express ZNF704 (17) vs lines expressing it (33) | 1.28× higher at baseline in the lines without ZNF704 | 0.098 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-27.3, -2.6); signed map (-21.5, -13.8). **Vector** length 96.7, 23.6% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.0 | +5.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +12.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.9 | +8.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +14.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +13.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +5.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.5 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.3 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -8.8 | -6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -5.6 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -5.2 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -16.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | RAD17 checkpoint clamp loader component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:69,369,293-69,414,801 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Rad24, RAD17Sp, CCYC |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 21 pathways, smallest: Impaired BRCA2 binding to RAD51; Activation of ATR in response to replication stress; HDR through Single Strand Annealing (SSA) |
| Matched by | ensembl_id |

**Function**, from UniProt [O75943](https://www.uniprot.org/uniprotkb/O75943) (Cell cycle checkpoint protein RAD17):

> Essential for sustained cell growth, maintenance of chromosomal stability, and ATR-dependent checkpoint activation upon DNA damage. Has a weak ATPase activity required for binding to chromatin. Participates in the recruitment of the 9-1-1 (RAD1-RAD9-HUS1) complex and RHNO1 onto chromatin, and in CHEK1 activation. Involved in homologous recombination by mediating recruitment of the MRN complex to DNA damage sites. May also serve as a sensor of DNA replication progression.

**Summary**, from NCBI Gene [5884](https://www.ncbi.nlm.nih.gov/gene/5884):

> The protein encoded by this gene is highly similar to the gene product of Schizosaccharomyces pombe rad17, a cell cycle checkpoint gene required for cell cycle arrest and DNA damage repair in response to DNA damage. This protein shares strong similarity with DNA replication factor C (RFC), and can form a complex with RFCs. This protein binds to chromatin prior to DNA damage and is phosphorylated by the checkpoint kinase ATR following damage. This protein recruits the RAD1-RAD9-HUS1 checkpoint …

**Accessions** — [HGNC:9807](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9807) · Entrez [5884](https://www.ncbi.nlm.nih.gov/gene/5884) · UniProt [O75943](https://www.uniprot.org/uniprotkb/O75943) · Ensembl [ENSG00000152942](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152942)

## Data

Gene col 7671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7671); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7671, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7671]; `tensor/DDL_lfc|DDL_z.npy` [7671]; `embed/gene_vectors.npy` [7671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7671 or target_col == 7671). Every well: [[RAD17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
