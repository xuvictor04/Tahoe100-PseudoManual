---
symbol: "PRPF3"
type: "gene"
col: 3897
ensembl_id: "ENSG00000117360"
name: "pre-mRNA processing factor 3"
location: "1q21.2"
module: 49
arm: "+"
pooled_cpm: 96.84
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# PRPF3

*pre-mRNA processing factor 3* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 9.97× (z +18.7, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.670× (z -8.5, q 1e-14, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP6]] (+0.69, fdr 7e-06), [[NUP160]] (+0.67, fdr 7e-06), [[PRPF6]] (+0.66, fdr 1e-05); moves opposite to [[GRIP1]] (-0.58, fdr 1e-05), [[FBXO30]] (-0.57, fdr 3e-05), [[B3GALNT2]] (-0.55, fdr 2e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3897.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **9.97×** | +18.7 | 0e+00 | 48/49 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **7.63×** | +16.5 | 0e+00 | 48/48 (SW480, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +9.5 | 4e-19 | 38/48 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +6.8 | 2e-09 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.55×** | +6.4 | 1e-08 | 31/47 (BT-474, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +5.6 | 2e-06 | 28/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.96×** | +5.5 | 3e-06 | 42/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.3 | 9e-06 | 0/50 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.8 | 8e-05 | 28/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.70×** | +4.3 | 8e-04 | 29/49 (A-172, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.001 | 29/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.002 | 26/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.069 | 20/48 (COLO 205, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3897.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -8.5 | 1e-14 | 42/49 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.583×** | -8.4 | 1e-14 | 41/49 (SW 900, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.580×** | -8.2 | 5e-14 | 33/44 (CHP-212, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.654×** | -6.1 | 1e-07 | 29/45 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -4.8 | 1e-04 | 29/48 (H4, SW48, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.734×** | -4.8 | 1e-04 | 30/48 (HOP62, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.814×** | -4.4 | 8e-04 | 32/48 (SNU-1, SW 900, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -3.8 | 0.012 | 28/50 (A-427, LoVo, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.784×** | -3.7 | 0.016 | 24/48 (NCI-H2347, SHP-77, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.798×** | -3.5 | 0.023 | 28/48 (Panc 03.27, NCI-H2030, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.709×** | -3.2 | 0.073 | 26/47 (SW480, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3897. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 128 | 6 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 15.3× (z +15.9) | — |
| [[NCI-H460 (line)]] | wt | 110 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -10.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 96.1 | 3 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.75× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.0) |
| [[A-172 (line)]] | wt | 94.4 | 4 | 1 | [[PH-797804 (drug)]] 5 µM 8.43× (z +13.0) | [[Auranofin (drug)]] 5 µM 0.464× (z -8.9) |
| [[BT-474 (line)]] | alt | 120 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 5.83× (z +17.0) | — |
| [[LoVo (line)]] | wt | 83.8 | 3 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.7× (z +15.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 69.1 | 4 | 1 | [[TAK-901 (drug)]] 5 µM 14.6× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -11.8) |
| [[SW480 (line)]] | alt | 77.5 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 15.5× (z +18.2) | — |
| [[A549 (line)]] | wt | 112 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.41× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -13.3) |
| [[CHP-212 (line)]] | wt | 239 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0415× (z -24.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 89.7 | 3 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 9.18× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.446× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 103 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 13.3× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -15.5) |
| [[NCI-H2347 (line)]] | alt | 104 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.21× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.502× (z -8.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 120 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 10.4× (z +12.4) | — |
| [[SK-MEL-2 (line)]] | alt | 75.5 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.12× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0612× (z -26.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 96.3 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.7× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -10.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 85.1 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 14.5× (z +11.7) | — |
| [[Hs 766T (line)]] | wt | 87.2 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 19.1× (z +12.9) | — |
| [[KATO III (line)]] | alt | 82.9 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 11.7× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -10.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 99.3 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.61× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 95.9 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 17.5× (z +15.3) | — |
| [[RPMI-7951 (line)]] | alt | 96.8 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.2× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -12.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 194 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.96× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -11.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 81.2 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.31× (z +11.7) | — |
| [[A-427 (line)]] | wt | 92.4 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 9.07× (z +12.5) | — |
| [[A498 (line)]] | wt | 103 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.40× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -15.2) |
| [[CFPAC-1 (line)]] | alt | 83.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.5× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 110 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 34.6× (z +14.5) | — |
| [[HS-578T (line)]] | alt | 68.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.9× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 69.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 14.0× (z +13.1) | — |
| [[hTERT-HPNE (line)]] | wt | 81.5 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 10.2× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 68.1 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 26.0× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 86.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.5× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 131 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.01× (z +9.9) | — |
| [[RKO (line)]] | wt | 73.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 20.4× (z +16.1) | — |
| [[SHP-77 (line)]] | alt | 201 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.50× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -9.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 80.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -9.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 107 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.63× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 90.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 16.1× (z +11.4) | — |
| [[J82 (line)]] | alt | 82.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.04× (z +11.7) | — |
| [[SNU-1 (line)]] | wt | 77.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 14.6× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 70.6 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 7.24× (z +9.6) | — |
| [[SW48 (line)]] | wt | 76.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -10.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3897), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP6]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[NUP160]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[PRPF6]] | +0.66 | +0.66 / +0.49 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 999 |
| [[SMN1]] | +0.65 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[RAD17]] | +0.64 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[AQR]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[IFT172]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[RARS1]] | +0.58 | +0.65 / +0.39 | both halves | 5e-05 |  |
| [[NCK1]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ZMYM6]] | +0.58 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[DRG1]] | +0.58 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[POT1]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRIP1]] | -0.58 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[FBXO30]] | -0.57 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[B3GALNT2]] | -0.55 | -0.60 / -0.32 | both halves | 2e-04 |  |
| [[LARGE1]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[MARK1]] | -0.52 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[TMEM117]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[GCNT4]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[ARHGAP21]] | -0.49 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[PARD3]] | -0.49 | -0.39 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PRPF3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.6, -8.0); signed map (-34.7, -24.2). **Vector** length 92.5, 28.1% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +18.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +16.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | -0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | -1.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.3 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +0.7 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.1 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | pre-mRNA processing factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:150,321,479-150,353,233 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Prp3, hPrp3, SNRNP90; previously RP18 |
| Gene groups (HGNC) | U4/U6 small nuclear ribonucleoprotein particle |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O43395](https://www.uniprot.org/uniprotkb/O43395) (U4/U6 small nuclear ribonucleoprotein Prp3):

> Plays a role in pre-mRNA splicing as component of the U4/U6-U5 tri-snRNP complex that is involved in spliceosome assembly, and as component of the precatalytic spliceosome (spliceosome B complex).

**Summary**, from NCBI Gene [9129](https://www.ncbi.nlm.nih.gov/gene/9129):

> The removal of introns from nuclear pre-mRNAs occurs on complexes called spliceosomes, which are made up of 4 small nuclear ribonucleoprotein (snRNP) particles and an undefined number of transiently associated splicing factors. This gene product is one of several proteins that associate with U4 and U6 snRNPs. Mutations in this gene are associated with retinitis pigmentosa-18. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17348) · Entrez [9129](https://www.ncbi.nlm.nih.gov/gene/9129) · UniProt [O43395](https://www.uniprot.org/uniprotkb/O43395) · Ensembl [ENSG00000117360](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117360)

## Data

Gene col 3897: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3897); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3897, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3897]; `tensor/DDL_lfc|DDL_z.npy` [3897]; `embed/gene_vectors.npy` [3897]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3897 or target_col == 3897). Every well: [[PRPF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
