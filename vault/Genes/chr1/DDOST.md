---
symbol: "DDOST"
type: "gene"
col: 14387
ensembl_id: "ENSG00000244038"
name: "dolichyl-diphosphooligosaccharide--protein glycosyltransferase non-catalytic subunit"
location: "1p36.12"
module: 29
arm: "+"
pooled_cpm: 63.8
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# DDOST

*dolichyl-diphosphooligosaccharide--protein glycosyltransferase non-catalytic subunit* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.84× (z +17.7, q 0e+00, up in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +9.0, q 3e-17, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.584× (z -12.9, q 3e-35, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDIA3]] (+0.83, fdr 7e-06), [[PDIA6]] (+0.80, fdr 7e-06), [[TMED10]] (+0.80, fdr 7e-06); moves opposite to [[NT5C]] (-0.66, fdr 1e-05), [[CROCCP2-1]] (-0.62, fdr 7e-06), [[LRRC8E]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MXRA8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14387.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.84×** | +17.7 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +15.5 | 0e+00 | 41/42 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +11.6 | 1e-28 | 40/44 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +9.0 | 3e-17 | 35/48 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.55×** | +8.3 | 1e-14 | 42/48 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.43×** | +7.9 | 4e-13 | 44/49 (RKO, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.6 | 2e-06 | 29/50 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.35×** | +5.0 | 3e-05 | 32/47 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.5 | 4e-04 | 24/35 (HEC-1-A, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.20× | +3.1 | 0.10 | 17/48 (PANC-1, NCI-H460, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14387.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.584×** | -12.9 | 3e-35 | 43/48 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.848× | -9.6 | 2e-19 | 21/49 (HS-578T, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.689×** | -6.1 | 3e-07 | 33/48 (KATO III, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.709×** | -5.8 | 8e-07 | 34/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.718×** | -5.6 | 2e-06 | 33/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.721×** | -5.1 | 3e-05 | 29/47 (A-172, HS-578T, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.740×** | -5.1 | 3e-05 | 26/48 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.770×** | -4.3 | 0.001 | 27/48 (HepG2/C3A, HS-578T, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.817×** | -3.4 | 0.039 | 24/48 (SW48, A-427, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.872× | -3.3 | 0.059 | 10/48 (HCT15, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14387. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 92.9 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -18.2) |
| [[A498 (line)]] | wt | 47.2 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.385× (z -9.8) |
| [[KATO III (line)]] | alt | 82.2 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -15.9) |
| [[NCI-H2347 (line)]] | alt | 78.0 | 2 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -14.2) |
| [[PANC-1 (line)]] | alt | 77.1 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +16.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -11.5) |
| [[A-172 (line)]] | wt | 48.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 42.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 58.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.2) | — |
| [[SW480 (line)]] | alt | 49.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -10.3) |
| [[C32 (line)]] | wt | 67.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.5) | — |
| [[H4 (line)]] | wt | 85.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -8.5) |
| [[HOP62 (line)]] | alt | 74.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +12.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 117 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +11.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 62.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -15.3) |
| [[J82 (line)]] | alt | 66.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -11.4) |
| [[SW 900 (line)]] | alt | 58.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.0) |
| [[A-427 (line)]] | wt | 60.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.15× (z +12.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 35.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +12.7) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 96.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -13.9) |
| [[COLO 205 (line)]] | alt | 58.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +11.6) ⚠ toxic; transcription drop | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.109× (z -8.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 56.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.13× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 54.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 54.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 50.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +13.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 40.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 66.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.40× (z +11.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 95.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 28.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +10.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 64.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 78.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 48.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 89.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 65.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +8.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 65.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 88.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.4) |
| [[SW 1088 (line)]] | alt | 111 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0955× (z -9.0) |
| [[SW1417 (line)]] | alt | 50.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -9.3) |
| [[SW48 (line)]] | wt | 70.9 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.18× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 113 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 78.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14387), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDIA3]] | +0.83 | +0.83 / +0.82 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 678 |
| [[PDIA6]] | +0.80 | +0.81 / +0.81 | both halves | 7e-06 | STRING 902 |
| [[TMED10]] | +0.80 | +0.78 / +0.82 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 646 |
| [[STT3A]] | +0.78 | +0.78 / +0.78 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 999 |
| [[RPN1]] | +0.76 | +0.76 / +0.75 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 999 |
| [[RPN2]] | +0.75 | +0.77 / +0.75 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 999 |
| [[LMAN2]] | +0.75 | +0.75 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 600 |
| [[TMEM30A]] | +0.74 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[GANAB]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | pathway: Adherens junctions interactions; STRING 692 |
| [[FKBP9]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[SDF4]] | +0.72 | +0.57 / +0.79 | both halves | 1e-05 |  |
| [[BPNT2]] | +0.71 | +0.68 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NT5C]] | -0.66 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.62 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[LRRC8E]] | -0.62 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.61 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[ATF4]] | -0.59 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[TIPRL]] | -0.59 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[NSUN5]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[ERVK3-1]] | -0.58 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[PPP1R35]] ⚠ | -0.58 | -0.46 / -0.57 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[JMJD1C]] | -0.58 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[EIF5B]] | -0.57 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[GLRX2]] | -0.57 | -0.54 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MXRA8]] | B | MXRA8 activity raises DDOST's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 1.32× lower at baseline in the lines without MXRA8 | 0.063 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.752). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.4, -22.0); signed map (-55.7, 6.3). **Vector** length 116, 33.9% of its response variance represented; |z| ≥ 3 in 857 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.4 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.7 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +15.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +1.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.2 | +0.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.1 | -5.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.9 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.3 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -12.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.3 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | dolichyl-diphosphooligosaccharide--protein glycosyltransferase non-catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:20,651,767-20,661,544 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OST, KIAA0115, OST48, WBP1 |
| Gene groups (HGNC) | Oligosaccharyltransferase complex subunits |
| Reactome | 29 pathways, smallest: Advanced glycosylation endproduct receptor signaling; PD-L1(CD274) glycosylation and translocation to plasma membrane; Regulation of CDH1 posttranslational processing and trafficking to plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [P39656](https://www.uniprot.org/uniprotkb/P39656) (Dolichyl-diphosphooligosaccharide--protein glycosyltransferase 48 kDa subunit):

> Subunit of the oligosaccharyl transferase (OST) complex that catalyzes the initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2) in eukaryotes) from the lipid carrier dolichol-pyrophosphate to an asparagine residue within an Asn-Xaa-Ser/Thr consensus motif in nascent polypeptide chains, the first step in protein N-glycosylation. N-glycosylation occurs cotranslationally and the complex associates with the Sec61 complex at the channel-forming translocon complex that mediates protein …

**Summary**, from NCBI Gene [1650](https://www.ncbi.nlm.nih.gov/gene/1650):

> This gene encodes a component of the oligosaccharyltransferase complex which catalyzes the transfer of high-mannose oligosaccharides to asparagine residues on nascent polypeptides in the lumen of the rough endoplasmic reticulum. The protein complex co-purifies with ribosomes. The product of this gene is also implicated in the processing of advanced glycation endproducts (AGEs), which form from non-enzymatic reactions between sugars and proteins or lipids and are associated with aging and …

**Accessions** — [HGNC:2728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2728) · Entrez [1650](https://www.ncbi.nlm.nih.gov/gene/1650) · UniProt [P39656](https://www.uniprot.org/uniprotkb/P39656) · Ensembl [ENSG00000244038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244038)

## Data

Gene col 14387: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14387); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14387, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14387]; `tensor/DDL_lfc|DDL_z.npy` [14387]; `embed/gene_vectors.npy` [14387]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14387 or target_col == 14387). Every well: [[DDOST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDOST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
