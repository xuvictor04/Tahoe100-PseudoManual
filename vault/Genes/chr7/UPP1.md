---
symbol: "UPP1"
type: "gene"
col: 11439
ensembl_id: "ENSG00000183696"
name: "uridine phosphorylase 1"
location: "7p12.3"
module: 125
arm: "+"
pooled_cpm: 123.85
n_lines_expressing: 41
n_dd_up: 42
n_dd_down: 27
n_dd_up_clean: 36
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 10
direction_downstream: 8
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# UPP1

*uridine phosphorylase 1* — 7p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.45× (z +13.1, q 3e-36, up in 35 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.496× (z -7.0, q 2e-09, down in 31 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCP1]] (+0.62, fdr 1e-05), [[SMIM29]] (+0.61, fdr 1e-05), [[PHLDA2]] (+0.61, fdr 8e-06); moves opposite to [[SORT1]] (-0.52, fdr 2e-05), [[TNS3]] (-0.51, fdr 7e-05), [[TMEM245]] (-0.49, fdr 2e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CTSL]] → it (grade B ⚠); 8 go from it, the strongest it → [[CDCP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11439.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.45×** | +13.1 | 3e-36 | 35/39 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.35×** | +8.5 | 8e-15 | 32/39 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.25×** | +8.1 | 1e-13 | 35/39 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.01×** | +7.2 | 8e-11 | 31/39 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.91×** | +6.4 | 2e-08 | 29/39 (NCI-H1573, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.99×** | +6.3 | 3e-08 | 37/40 (NCI-H2347, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +6.0 | 2e-07 | 26/39 (SW480, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.72×** | +5.6 | 2e-06 | 33/40 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +5.2 | 1e-05 | 29/39 (LoVo, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +5.1 | 2e-05 | 25/39 (H4, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.63×** | +5.1 | 2e-05 | 33/39 (LoVo, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.0 | 2e-05 | 21/40 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.39×** | +4.8 | 7e-05 | 23/40 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.8 | 7e-05 | 24/38 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.7 | 1e-04 | 27/39 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.87×** | +4.6 | 1e-04 | 33/39 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +4.5 | 2e-04 | 20/39 (H4, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.53×** | +4.4 | 4e-04 | 23/39 (SW480, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 1 with an alert ⚠; shown: the 15 strongest. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11439.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.496×** | -7.0 | 2e-09 | 31/38 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.515×** | -6.6 | 9e-09 | 32/39 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.633×** | -6.6 | 9e-09 | 31/39 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.488×** | -6.5 | 9e-09 | 33/41 (MIA PaCa-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.613×** | -6.2 | 7e-08 | 33/39 (NCI-H1573, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.578×** | -5.7 | 1e-06 | 28/39 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.653×** | -5.5 | 3e-06 | 29/39 (MIA PaCa-2, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.604×** | -5.2 | 1e-05 | 32/38 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.586×** | -5.2 | 1e-05 | 26/40 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.621×** | -4.9 | 5e-05 | 27/39 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.634×** | -4.7 | 1e-04 | 29/40 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.723×** | -4.6 | 2e-04 | 24/40 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.603×** | -4.1 | 0.002 | 25/39 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.658×** | -4.1 | 0.002 | 26/39 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.685×** | -3.9 | 0.004 | 26/39 (PANC-1, NCI-H2030, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11439. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 227 | 0 | 16 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.298× (z -25.2) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.132× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 139 | 7 (1 ⚠) | 9 | [[Selinexor (drug)]] 0.5 µM 6.80× (z +13.8) | [[Trametinib (drug)]] 0.5 µM 0.290× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 406 | 7 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +16.0) | [[Trametinib (drug)]] 0.5 µM 0.441× (z -8.8) |
| [[LoVo (line)]] | wt | 63.3 | 7 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +16.5) | [[Trametinib (drug)]] 0.5 µM 0.465× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 76.8 | 9 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.15× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.76× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 192 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +15.3) | — |
| [[NCI-H23 (line)]] | alt | 85.1 | 0 | 7 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.464× (z -19.2) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.215× (z -11.1) |
| [[H4 (line)]] | wt | 156 | 4 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 5.77× (z +10.7) | — |
| [[A498 (line)]] | wt | 73.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +14.3) | — |
| [[BT-474 (line)]] | alt | 46.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +12.8) | [[Simotinib (drug)]] 5 µM 0.199× (z -8.7) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 72.4 | 3 | 0 | [[Selinexor (drug)]] 5 µM 2.82× (z +11.7) | — |
| [[RKO (line)]] | wt | 517 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -12.4) |
| [[SW1417 (line)]] | alt | 101 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +17.1) | — |
| [[J82 (line)]] | alt | 110 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.9) | — |
| [[KATO III (line)]] | alt | 43.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 140 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.6) | — |
| [[SW480 (line)]] | alt | 68.5 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.15× (z +9.5) | — |
| [[A-172 (line)]] | wt | 76.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 81.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 299 | 1 | 0 | [[Artesunate (drug)]] 5 µM 2.28× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 44.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 206 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.84× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 418 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.192× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -11.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 74.1 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.102× (z -8.5) |
| [[A-427 (line)]] | wt | 30.5 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 78.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.3 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 30.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 26.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 383 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 26.3 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11439), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCP1]] | +0.62 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[SMIM29]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[PHLDA2]] | +0.61 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[SPHK1]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[FOSL1]] | +0.60 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[LIF]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[ACVR1]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SNX9]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ARHGEF2]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[FAM83G]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[NIT1]] | +0.58 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[TRPV3]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORT1]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TNS3]] | -0.51 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[TMEM245]] | -0.49 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[PDLIM1]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ATP5F1A]] | -0.48 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[HOPX]] | -0.48 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[NUMA1]] | -0.48 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[GTF2I]] | -0.48 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[ADAM15]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSL]] | B | CTSL activity raises UPP1's level | lines that do not express CTSL (9) vs lines expressing it (41) | 2.31× lower at baseline in the lines without CTSL | 0.021 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent |
| [[TNFRSF10A]] | B | TNFRSF10A activity raises UPP1's level | lines that do not express TNFRSF10A (10) vs lines expressing it (40) | 1.76× lower at baseline in the lines without TNFRSF10A | 0.036 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, SLC16A5, CDCP1 |
| [[SUN3]] | B | SUN3 activity raises UPP1's level | lines that do not express SUN3 (31) vs lines expressing it (19) | 2.09× lower at baseline in the lines without SUN3 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000250038, SFTA1P, PKD1L1-AS1; maybe low, not absent |
| [[SPHK1]] | B | SPHK1 activity raises UPP1's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 2.72× lower at baseline in the lines without SPHK1 | 0.046 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[TMEM158]] | B | TMEM158 activity raises UPP1's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without TMEM158 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[PLAUR]] | B | PLAUR activity raises UPP1's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 2.54× lower at baseline in the lines without PLAUR | 0.065 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[TNFRSF10A-DT]] | B | TNFRSF10A-DT activity raises UPP1's level | lines that do not express TNFRSF10A-DT (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without TNFRSF10A-DT | 0.076 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, SLC16A5, ARHGEF16 |
| [[CDCP1]] | B | CDCP1 activity raises UPP1's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without CDCP1 | 0.077 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[IL23A]] | B | IL23A activity strengthens UPP1's drug response | lines that do not express IL23A (5) vs lines expressing it (36) | the lines without IL23A respond 0.89× as strongly (z diff +1.35); strongest at Trametinib 5 µM: 0.63x vs 0.45x (z diff +3.8) | 0.081 | ⚠ within organs, on part of the lines; also absent: MYRF; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises UPP1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCP1]] | B | UPP1 activity raises CDCP1's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 2.94× lower at baseline in the lines without UPP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |
| [[TNFRSF10A]] | B | UPP1 activity raises TNFRSF10A's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 1.96× lower at baseline in the lines without UPP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |
| [[FOSL1]] | B | UPP1 activity raises FOSL1's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 2.34× lower at baseline in the lines without UPP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |
| [[SNX9]] | B | UPP1 activity raises SNX9's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without UPP1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |
| [[GTF2I]] | B | UPP1 activity raises GTF2I's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 1.17× lower at baseline in the lines without UPP1 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |
| [[TNFRSF10A-DT]] | B | UPP1 activity raises TNFRSF10A-DT's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without UPP1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |
| [[HMGA1]] | B | UPP1 activity raises HMGA1's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 1.44× lower at baseline in the lines without UPP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |
| [[MEAK7]] | B | UPP1 activity raises MEAK7's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 1.79× lower at baseline in the lines without UPP1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.488). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.7, -3.0); signed map (1.9, 33.5). **Vector** length 123, 42.1% of its response variance represented; |z| ≥ 3 in 1,543 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.8 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +13.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.6 | +8.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.3 | +6.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.1 | +3.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.1 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.5 | +4.8 |
| fall | [[NG25 (drug)]] 5 µM |  | -7.3 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.9 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.6 | +3.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.9 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.9 | -4.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.7 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.6 | -6.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.6 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | uridine phosphorylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p12.3 — chr7:48,088,628-48,108,736 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UPASE, UPP, UDRPASE; previously UP |
| Hallmark sets | XENOBIOTIC_METABOLISM, INTERFERON_GAMMA_RESPONSE, P53_PATHWAY |
| Reactome | 5 pathways, smallest: Pyrimidine catabolism; Pyrimidine salvage; Nucleotide salvage |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16831](https://www.uniprot.org/uniprotkb/Q16831) (Uridine phosphorylase 1):

> Catalyzes the reversible phosphorylytic cleavage of uridine to uracil and ribose-1-phosphate which can then be utilized as carbon and energy sources or in the rescue of pyrimidine bases for nucleotide synthesis. Shows broad substrate specificity and can also accept deoxyuridine and other analogous compounds (Probable).

**Summary**, from NCBI Gene [7378](https://www.ncbi.nlm.nih.gov/gene/7378):

> This gene encodes a uridine phosphorylase, an enzyme that catalyzes the reversible phosphorylation of uridine (or 2'- deoxyuridine) to uracil and ribose-1-phosphate (or deoxyribose-1-phosphate). The encoded enzyme functions in the degradation and salvage of pyrimidine ribonucleosides. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:12576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12576) · Entrez [7378](https://www.ncbi.nlm.nih.gov/gene/7378) · UniProt [Q16831](https://www.uniprot.org/uniprotkb/Q16831) · Ensembl [ENSG00000183696](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183696)

## Data

Gene col 11439: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11439); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11439, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11439]; `tensor/DDL_lfc|DDL_z.npy` [11439]; `embed/gene_vectors.npy` [11439]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11439 or target_col == 11439). Every well: [[UPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
