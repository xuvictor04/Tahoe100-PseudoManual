---
symbol: "LAPTM4A"
type: "gene"
col: 897
ensembl_id: "ENSG00000068697"
name: "lysosomal protein transmembrane 4 alpha"
location: "2p24.1"
module: 11
arm: "-"
pooled_cpm: 81.41
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# LAPTM4A

*lysosomal protein transmembrane 4 alpha* — 2p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.25× (z +11.2, q 2e-26, up in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +6.5, q 1e-08, up in 34 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A-172 3.99×, NCI-H1573 4.30×, NCI-H460 3.57×, PANC-1 3.33×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 2.97×, SW480 2.98×, SK-MEL-2 4.55×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 2.12×, SW1417 1.95×).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.580× (z -10.7, q 9e-24, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TM9SF2]] (+0.77, fdr 7e-06), [[IER3IP1]] (+0.71, fdr 7e-06), [[TMED4]] (+0.69, fdr 7e-06); moves opposite to [[RPL7L1]] (-0.71, fdr 7e-06), [[GPATCH4]] (-0.70, fdr 7e-06), [[CCDC137]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 897.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A-172 3.99×, NCI-H1573 4.30×, NCI-H460 3.57×, PANC-1 3.33×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 2.97×, SW480 2.98×, SK-MEL-2 4.55×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 2.12×, SW1417 1.95×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +11.2 | 2e-26 | 44/49 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +10.4 | 4e-23 | 39/44 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.67×** | +7.1 | 3e-10 | 44/48 (NCI-H460, NCI-H23, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.5 | 1e-08 | 34/49 (A-172, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +6.3 | 3e-08 | 42/49 (RPMI-7951, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +6.3 | 4e-08 | 37/45 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.54×** | +5.9 | 2e-07 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.5 | 3e-06 | 36/47 (NCI-H1573, A-172, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.1 | 2e-05 | 3/50 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.42×** | +4.8 | 9e-05 | 37/48 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.34×** | +4.1 | 0.002 | 30/48 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.29×** | +3.5 | 0.021 | 27/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.27×** | +3.3 | 0.046 | 22/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 897.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.580×** | -10.7 | 9e-24 | 41/48 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.552×** | -8.2 | 5e-14 | 41/48 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.692×** | -5.1 | 6e-05 | 35/48 (NCI-H2347, SW 900, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.718×** | -4.6 | 6e-04 | 33/48 (KATO III, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.739×** | -4.0 | 0.006 | 28/48 (HCT15, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.782× | -3.1 | 0.21 | 26/47 (AsPC-1, LoVo, …) | all doses, flat | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 897. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 51.1 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +12.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 123 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 58.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -10.9) |
| [[PANC-1 (line)]] | alt | 62.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 45.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -9.8) |
| [[HOP62 (line)]] | alt | 84.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 116 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -13.0) |
| [[C32 (line)]] | wt | 80.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +10.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 74.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -10.6) |
| [[HCT15 (line)]] | alt | 62.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 44.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 124 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -10.8) |
| [[KATO III (line)]] | alt | 106 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -12.8) |
| [[LS 180 (line)]] | wt | 63.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 158 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 93.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -15.2) |
| [[SNU-1 (line)]] | wt | 79.2 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.105× (z -9.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.463× (z -8.5) |
| [[SW 900 (line)]] | alt | 91.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -13.9) |
| [[SW1417 (line)]] | alt | 90.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -9.2) |
| [[A498 (line)]] | wt | 212 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.391× (z -10.3) |
| [[A549 (line)]] | wt | 77.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +9.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 68.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -9.6) |
| [[BT-474 (line)]] | alt | 63.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.8) |
| [[C-33 A (line)]] | alt | 53.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +10.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 93.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -10.8) |
| [[J82 (line)]] | alt | 62.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +10.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 49.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 76.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.56× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 53.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -15.9) |
| [[SHP-77 (line)]] | alt | 35.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 47.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.55× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 84.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 157 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 897), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM9SF2]] | +0.77 | +0.81 / +0.73 | both halves | 7e-06 | STRING 685 |
| [[IER3IP1]] | +0.71 | +0.81 / +0.61 | both halves | 7e-06 |  |
| [[TMED4]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[ATP6AP2]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[RCN2]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ASAH1]] | +0.67 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[ADIPOR1]] | +0.66 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[GTF2IP4]] | +0.66 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[GRN]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[PPT2]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[TMEM59]] | +0.65 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[KLHDC3]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL7L1]] | -0.71 | -0.76 / -0.65 | both halves | 7e-06 |  |
| [[GPATCH4]] | -0.70 | -0.71 / -0.69 | both halves | 7e-06 |  |
| [[CCDC137]] | -0.69 | -0.77 / -0.63 | both halves | 7e-06 |  |
| [[THG1L]] | -0.68 | -0.72 / -0.57 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.66 | -0.71 / -0.54 | both halves | 1e-05 |  |
| [[UTP14A]] | -0.66 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[NEPRO-AS1]] | -0.66 | -0.75 / -0.46 | both halves | 3e-05 |  |
| [[ESF1]] | -0.65 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[EIF3J]] | -0.65 | -0.71 / -0.58 | both halves | 7e-06 |  |
| [[NOP14]] | -0.64 | -0.69 / -0.57 | both halves | 9e-06 |  |
| [[MPHOSPH6]] | -0.64 | -0.63 / -0.70 | both halves | 7e-06 |  |
| [[NOP56]] | -0.63 | -0.67 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.8, -18.5); signed map (-50.4, -7.0). **Vector** length 116, 36.6% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +6.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.5 | +2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.0 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.5 | -10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.7 | -8.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.2 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.8 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.1 | -5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.3 | -3.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.2 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | lysosomal protein transmembrane 4 alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.1 — chr2:20,032,650-20,051,628 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HUMORF13, KIAA0108, Mtrp, LAPTM4; previously MBNT |
| Gene groups (HGNC) | Lysosomal protein transmembrane family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15012](https://www.uniprot.org/uniprotkb/Q15012) (Lysosomal-associated transmembrane protein 4A):

> May function in the transport of nucleosides and/or nucleoside derivatives between the cytosol and the lumen of an intracellular membrane-bound compartment.

**Summary**, from NCBI Gene [9741](https://www.ncbi.nlm.nih.gov/gene/9741):

> This gene encodes a protein that has four predicted transmembrane domains. The function of this gene has not yet been determined; however, studies in the mouse homolog suggest a role in the transport of small molecules across endosomal and lysosomal membranes. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6924](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6924) · Entrez [9741](https://www.ncbi.nlm.nih.gov/gene/9741) · UniProt [Q15012](https://www.uniprot.org/uniprotkb/Q15012) · Ensembl [ENSG00000068697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068697)

## Data

Gene col 897: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 897); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 897, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 897]; `tensor/DDL_lfc|DDL_z.npy` [897]; `embed/gene_vectors.npy` [897]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 897 or target_col == 897). Every well: [[LAPTM4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAPTM4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
