---
symbol: "PLBD1"
type: "gene"
col: 4267
ensembl_id: "ENSG00000121316"
name: "phospholipase B domain containing 1"
location: "12p13.1"
module: 29
arm: "+"
pooled_cpm: 14.76
n_lines_expressing: 26
n_dd_up: 21
n_dd_down: 21
n_dd_up_clean: 12
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PLBD1

*phospholipase B domain containing 1* — 12p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.87× (z +16.4, q 0e+00, up in 13 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +9.6, q 1e-19, up in 8 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.442× (z -12.7, q 3e-34, down in 20 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCARB2]] (+0.65, fdr 7e-06), [[TSPAN6]] (+0.64, fdr 1e-05), [[FUCA2]] (+0.64, fdr 1e-05); moves opposite to [[PLIN3]] (-0.55, fdr 6e-05), [[PRKG2-AS1]] (-0.54, fdr 2e-05), [[ZNF274]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CTSH]] → it (grade B ⚠); 4 go from it, the strongest it → [[CELSR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4267.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +16.4 | 0e+00 | 13/16 (LoVo, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +14.7 | 0e+00 | 14/16 (Panc 03.27, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +14.2 | 1e-43 | 14/15 (AsPC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +9.6 | 1e-19 | 8/23 (CFPAC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.6 | 4e-09 | 6/23 (MIA PaCa-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.5 | 6e-04 | 9/23 (SK-MEL-2, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +4.4 | 7e-04 | 9/24 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.22×** | +4.4 | 7e-04 | 10/24 (RKO, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.4 | 7e-04 | 4/14 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.002 | 14/24 (LoVo, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.45×** | +4.1 | 0.002 | 4/20 (AN3 CA, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.002 | 11/24 (LoVo, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.003 | 10/24 (LoVo, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.8 | 0.006 | 4/18 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.006 | 7/24 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.015 | 7/24 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.030 | 7/24 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.075 | 2/23 (C-33 A, PANC-1) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.21×** | +2.9 | 0.088 | 4/24 (LoVo, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 1 with an alert ⚠; shown: the 15 strongest. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4267.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.442×** | -12.7 | 3e-34 | 20/22 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.580×** | -12.0 | 1e-30 | 21/22 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.477×** | -11.5 | 2e-28 | 20/24 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.540×** | -9.2 | 4e-18 | 19/24 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.558×** | -9.1 | 1e-17 | 20/24 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.584×** | -8.4 | 5e-15 | 19/24 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.634×** | -7.1 | 1e-10 | 18/24 (LoVo, SNU-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.683×** | -5.9 | 2e-07 | 20/24 (LoVo, SW48, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.702×** | -5.5 | 2e-06 | 12/24 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.730×** | -4.9 | 5e-05 | 13/24 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.747×** | -4.5 | 3e-04 | 11/24 (KATO III, MIA PaCa-2, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.749×** | -4.5 | 3e-04 | 14/24 (MIA PaCa-2, Panc 03.27, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.764×** | -4.2 | 0.001 | 13/24 (SNU-1, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.598×** | -4.2 | 0.001 | 7/23 (SNU-1, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.771×** | -4.0 | 0.002 | 11/24 (AN3 CA, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 104 | 1 (1 ⚠) | 7 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -21.3) |
| [[MIA PaCa-2 (line)]] | alt | 54.7 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -19.7) |
| [[AsPC-1 (line)]] | alt | 33.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -18.5) |
| [[LS 180 (line)]] | wt | 16.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 47.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -14.7) |
| [[SNU-1 (line)]] | wt | 50.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -18.7) |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 3 | — | [[Verteporfin (drug)]] 5 µM 0.0749× (z -10.8) |
| [[KATO III (line)]] | alt | 36.7 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.183× (z -10.6) |
| [[PANC-1 (line)]] | alt | 27.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -16.2) |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0919× (z -10.0) |
| [[Hs 766T (line)]] | wt | 36.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -15.0) |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0932× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 31.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 8.76 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.232× (z -8.9) |
| [[RKO (line)]] | wt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -9.0) |
| [[A-172 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCARB2]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[TSPAN6]] | +0.64 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[FUCA2]] | +0.64 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[RAVER2]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TMEM123]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[SCP2]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[GSTK1]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ITM2B]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SUMO3]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[CNOT1]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CRTAP]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PPT1]] | +0.59 | +0.51 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLIN3]] | -0.55 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[PRKG2-AS1]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ZNF274]] | -0.54 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[ZNF699]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PPP1R13L]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[RGP1]] | -0.53 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[MIDN]] | -0.53 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[ZNF611]] | -0.53 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ZNF674]] | -0.52 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TUBB6]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[METTL23]] | -0.52 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[SLC12A4]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSH]] | B | CTSH activity raises PLBD1's level | lines that do not express CTSH (8) vs lines expressing it (42) | 3.47× lower at baseline in the lines without CTSH | 0.042 | ⚠ within organs, on part of the lines; also absent: BCL2L1, ENSG00000234139, DAPK2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers PLBD1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELSR2]] | B | PLBD1 activity raises CELSR2's level | lines that do not express PLBD1 (24) vs lines expressing it (26) | 1.60× lower at baseline in the lines without PLBD1 | 0.057 | ⚠ within organs, on part of the lines; also absent: PLBD1-AS1, LINC01357, IKZF3 |
| [[CXCL16]] | B | PLBD1 activity raises CXCL16's level | lines that do not express PLBD1 (24) vs lines expressing it (26) | 1.90× lower at baseline in the lines without PLBD1 | 0.058 | ⚠ within organs, on part of the lines; also absent: PLBD1-AS1, LINC01357, IKZF3 |
| cells under [[Adagrasib (drug)]] 5 µM | B | PLBD1 activity lowers the cells' numbers under Adagrasib 5 µM (makes them more sensitive) | lines that do not express PLBD1 (24) vs lines expressing it (24) | the lines without PLBD1: 1.21× the cells of the other lines | 0.059 | ⚠ within organs, on part of the lines; also absent: PLBD1-AS1, LINC01357, IKZF3 |
| cells under [[Cabozantinib (S-malate) (drug)]] 5 µM | B | PLBD1 activity raises the cells' numbers under Cabozantinib (S-malate) 5 µM (protects the cells) | lines that do not express PLBD1 (24) vs lines expressing it (24) | the lines without PLBD1: 0.84× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: PLBD1-AS1, LINC01357, IKZF3 |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.8, -19.8); signed map (-21.1, -40.0). **Vector** length 68.5, 17.3% of its response variance represented; |z| ≥ 3 in 600 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +14.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +3.1 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +14.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +9.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.9 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.7 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +4.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.5 | +4.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -12.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase B domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.1 — chr12:14,503,661-14,567,883 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PLBL1, FLJ22662 |
| Reactome | 7 pathways, smallest: Hydrolysis of LPC; Acyl chain remodelling of PI; Acyl chain remodelling of PC |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P4A8](https://www.uniprot.org/uniprotkb/Q6P4A8) (Lysosomal leucine aminopeptidase):

> Lysosomal processive monoaminopeptidase that preferentially cleaves hydrophobic amino acids, with strong preference for leucine residues. Plays a key role in the degradation of hydrophobic transmembrane domains within the lysosome.

**Summary**, from NCBI Gene [79887](https://www.ncbi.nlm.nih.gov/gene/79887):

> Enables aminopeptidase activity. Involved in lysosomal protein catabolic process. Located in lysosome and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26215) · Entrez [79887](https://www.ncbi.nlm.nih.gov/gene/79887) · UniProt [Q6P4A8](https://www.uniprot.org/uniprotkb/Q6P4A8) · Ensembl [ENSG00000121316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121316)

## Data

Gene col 4267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4267); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4267]; `tensor/DDL_lfc|DDL_z.npy` [4267]; `embed/gene_vectors.npy` [4267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4267 or target_col == 4267). Every well: [[PLBD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLBD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
