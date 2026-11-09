---
symbol: "TMEM219"
type: "gene"
col: 7420
ensembl_id: "ENSG00000149932"
name: "transmembrane protein 219"
location: "16p11.2"
module: 30
arm: "+"
pooled_cpm: 21.47
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# TMEM219

*transmembrane protein 219* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.60× (z +15.2, q 0e+00, up in 39 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 1.87× (z +4.1, q 0.004, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.398× (z -13.0, q 1e-35, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A23]] (+0.68, fdr 8e-06), [[SNX1]] (+0.67, fdr 7e-06), [[SEC11A]] (+0.66, fdr 1e-05); moves opposite to [[NIP7]] (-0.60, fdr 1e-05), [[DNAJC11]] (-0.60, fdr 2e-05), [[EIF4G1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[F11R]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7420.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.60×** | +15.2 | 0e+00 | 39/40 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.73×** | +14.8 | 0e+00 | 31/32 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.96×** | +9.3 | 4e-18 | 35/37 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.3 | 0.002 | 5/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.87×** | +4.1 | 0.004 | 31/47 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.83×** | +4.0 | 0.006 | 31/45 (A498, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.74×** | +3.7 | 0.020 | 27/45 (Hs 766T, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.70×** | +3.5 | 0.031 | 21/47 (A498, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 1.61× | +3.2 | 0.10 | 13/47 (LOX-IMVI, PANC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7420.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.398×** | -13.0 | 1e-35 | 45/47 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.367×** | -9.9 | 7e-21 | 43/47 (A549, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.522×** | -6.5 | 2e-08 | 36/48 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.529×** | -6.1 | 2e-07 | 33/47 (NCI-H1792, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.548×** | -6.0 | 3e-07 | 38/48 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.610×** | -4.9 | 8e-05 | 32/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.672×** | -4.0 | 0.005 | 26/48 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.672×** | -4.0 | 0.005 | 27/47 (NCI-H1573, H4, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.663×** | -3.9 | 0.007 | 24/47 (A-172, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.687×** | -3.7 | 0.011 | 27/47 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.675×** | -3.7 | 0.011 | 27/48 (MIA PaCa-2, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.691×** | -3.7 | 0.011 | 20/47 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.734×** | -3.1 | 0.090 | 20/47 (H4, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.487×** | -3.1 | 0.090 | 19/48 (LOX-IMVI, SW 1271, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7420. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 19.7 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 9.60× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.5) |
| [[HT-29 (line)]] | alt | 24.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.53× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.5) |
| [[NCI-H2030 (line)]] | alt | 31.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.63× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 16.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.03× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.4) |
| [[A-172 (line)]] | wt | 35.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.07× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 19.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.18× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 22.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +15.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 22.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -13.2) |
| [[LoVo (line)]] | wt | 16.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 23.1× (z +19.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 15.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.28× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -11.7) |
| [[SW480 (line)]] | alt | 14.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.46× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 29.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -10.5) |
| [[BT-474 (line)]] | alt | 21.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.64× (z +8.9) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 17.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.06× (z +11.7) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -13.0) |
| [[HOP62 (line)]] | alt | 14.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.35× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 16.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.36× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -15.4) |
| [[LS 180 (line)]] | wt | 22.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 27.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 13.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.25× (z +8.6) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.105× (z -10.5) |
| [[PANC-1 (line)]] | alt | 32.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.01× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 19.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.02× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 21.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +11.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -10.9) |
| [[KATO III (line)]] | alt | 24.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -11.5) |
| [[SHP-77 (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 22.9 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.159× (z -8.5) |
| [[SNU-423 (line)]] | alt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -11.9) |
| [[A-427 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7420), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A23]] | +0.68 | +0.64 / +0.57 | both halves | 8e-06 |  |
| [[SNX1]] | +0.67 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SEC11A]] | +0.66 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[FLYWCH2]] | +0.66 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[DHPS]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[CD99]] | +0.65 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[ABHD8]] | +0.64 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[SEZ6L2]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 | STRING 587; ⚠ same locus (41.3 kb: neighbours can correlate without regulation) |
| [[ATP6AP2]] | +0.63 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[GET1]] | +0.63 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[PTOV1]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[UNC45A]] | +0.63 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[COPS4]] | +0.63 | +0.64 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIP7]] | -0.60 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.60 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[EIF4G1]] | -0.60 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[GRWD1]] | -0.59 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[CYREN]] | -0.59 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[TRMT5]] | -0.59 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[GPATCH4]] | -0.59 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[MLH3]] | -0.58 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[MRM3]] | -0.58 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[MGA]] | -0.57 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[RPL7L1]] | -0.57 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[CCT5]] | -0.57 | -0.56 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F11R]] | B | F11R activity raises TMEM219's level | lines that do not express F11R (10) vs lines expressing it (40) | 1.29× lower at baseline in the lines without F11R | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (2.7, -12.4); signed map (-30.6, -2.9). **Vector** length 77.5, 18.9% of its response variance represented; |z| ≥ 3 in 734 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +15.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.1 | +1.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.3 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -9.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 219 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,940,885-29,973,050 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IGFBP-3R |
| Reactome | 3 pathways, smallest: TP53 Regulates Transcription of Death Receptors and Ligands; TP53 Regulates Transcription of Cell Death Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XT9](https://www.uniprot.org/uniprotkb/Q86XT9) (Insulin-like growth factor-binding protein 3 receptor):

> Cell death receptor specific for IGFBP3, may mediate caspase-8-dependent apoptosis upon ligand binding.

**Summary**, from NCBI Gene [124446](https://www.ncbi.nlm.nih.gov/gene/124446):

> Predicted to be involved in several processes, including ERK1 and ERK2 cascade; positive regulation of ERK1 and ERK2 cascade; and transforming growth factor beta1 production. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25201](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25201) · Entrez [124446](https://www.ncbi.nlm.nih.gov/gene/124446) · UniProt [Q86XT9](https://www.uniprot.org/uniprotkb/Q86XT9) · Ensembl [ENSG00000149932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149932)

## Data

Gene col 7420: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7420); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7420, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7420]; `tensor/DDL_lfc|DDL_z.npy` [7420]; `embed/gene_vectors.npy` [7420]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7420 or target_col == 7420). Every well: [[TMEM219 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM219.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
