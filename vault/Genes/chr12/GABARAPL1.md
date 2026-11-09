---
symbol: "GABARAPL1"
type: "gene"
col: 6258
ensembl_id: "ENSG00000139112"
name: "GABA type A receptor associated protein like 1"
location: "12p13.2"
module: 187
arm: "+"
pooled_cpm: 47.64
n_lines_expressing: 47
n_dd_up: 44
n_dd_down: 17
n_dd_up_clean: 35
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# GABARAPL1

*GABA type A receptor associated protein like 1* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.73× (z +15.0, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.373× (z -14.7, q 0e+00, down in 43 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.293× (z -9.4, q 2e-18, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YPEL5]] (+0.74, fdr 7e-06), [[RB1CC1]] (+0.70, fdr 7e-06), [[WBP2]] (+0.67, fdr 8e-06); moves opposite to [[PDSS1]] (-0.65, fdr 1e-05), [[RNGTT]] (-0.60, fdr 1e-05), [[NSUN2]] (-0.59, fdr 1e-05).
> It is in [[Module 187]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[JMY]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6258.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.73×** | +15.0 | 0e+00 | 43/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.84×** | +14.7 | 0e+00 | 44/45 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.65×** | +14.5 | 1e-45 | 42/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +8.1 | 5e-14 | 31/45 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +8.0 | 1e-13 | 36/45 (C32, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +8.0 | 1e-13 | 31/45 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +7.5 | 7e-12 | 24/42 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +7.2 | 3e-11 | 25/45 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.61×** | +7.1 | 6e-11 | 28/45 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.99×** | +7.0 | 1e-10 | 32/45 (PANC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +6.8 | 6e-10 | 31/45 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +6.1 | 4e-08 | 27/44 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.40×** | +5.7 | 6e-07 | 30/45 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.41×** | +5.5 | 2e-06 | 28/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +5.4 | 3e-06 | 18/36 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 4e-06 | 25/45 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 4e-06 | 25/45 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +5.1 | 9e-06 | 24/46 (A-172, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 4e-04 | 18/46 (NCI-H460, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6258.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.373×** | -14.7 | 0e+00 | 43/45 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.293×** | -9.4 | 2e-18 | 38/44 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.316×** | -8.8 | 2e-16 | 39/43 (NCI-H460, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.358×** | -7.9 | 5e-13 | 38/44 (NCI-H1792, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.364×** | -7.7 | 1e-12 | 35/45 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.610×** | -7.4 | 1e-11 | 30/45 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.388×** | -7.2 | 3e-11 | 33/43 (NCI-H2030, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.634×** | -6.8 | 6e-10 | 29/45 (NCI-H1792, NCI-H2030, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.552×** | -6.1 | 8e-08 | 33/45 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.697×** | -5.1 | 2e-05 | 22/45 (NCI-H23, RKO, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.559×** | -4.5 | 4e-04 | 24/42 (NCI-H2030, NCI-H23, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **0.653×** | -4.3 | 6e-04 | 21/45 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.755×** | -4.2 | 0.001 | 21/45 (NCI-H1573, HepG2/C3A, …) | top dose only |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.794×** | -3.3 | 0.044 | 14/45 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[Everolimus (drug)]] 5 µM |  | **0.742×** | -3.2 | 0.046 | 11/45 (NCI-H23, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.736×** | -3.1 | 0.062 | 8/45 (NCI-H23, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | **0.679×** | -3.0 | 0.099 | 8/45 (NCI-H1573, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6258. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 65.0 | 14 (3 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +18.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.142× (z -17.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0945× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 86.3 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[EX229 (drug)]] 5 µM 0.128× (z -10.4) |
| [[A498 (line)]] | wt | 65.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +17.5) | — |
| [[NCI-H1573 (line)]] | alt | 121 | 1 (1 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.7) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.219× (z -13.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.127× (z -9.7) |
| [[SW480 (line)]] | alt | 25.4 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.04× (z +12.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.270× (z -11.2) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 25.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +15.0) | — |
| [[HOP62 (line)]] | alt | 44.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 42.5 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.12× (z +11.0) | — |
| [[LoVo (line)]] | wt | 22.8 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.07× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 145 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.268× (z -13.6) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 26.3 | 3 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.66× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.272× (z -12.6) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 26.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +12.1) | — |
| [[C32 (line)]] | wt | 29.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.60× (z +10.1) | — |
| [[H4 (line)]] | wt | 66.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.82× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 42.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.15× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 40.9 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.66× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.312× (z -9.1) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 144 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.283× (z -12.6) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 46.0 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.14× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 18.4 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 5.40× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 20.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.83× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 22.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.1) | — |
| [[A-427 (line)]] | wt | 217 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.20× (z +9.1) | — |
| [[A549 (line)]] | wt | 44.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.217× (z -12.8) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 30.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.287× (z -8.6) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 44.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.149× (z -8.6) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 58.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 28.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.209× (z -9.5) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 62.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.337× (z -9.6) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 83.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.325× (z -10.1) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.64 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.49 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6258), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL5]] | +0.74 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[RB1CC1]] | +0.70 | +0.62 / +0.75 | both halves | 7e-06 | same gene group; pathway: Autophagy; STRING 967 |
| [[WBP2]] | +0.67 | +0.57 / +0.74 | both halves | 8e-06 |  |
| [[HSPB1]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[KLHL24]] | +0.61 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[TBC1D15]] | +0.60 | +0.44 / +0.64 | both halves | 3e-05 | STRING 984 |
| [[TAX1BP1]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 | STRING 987 |
| [[OTUD1]] | +0.60 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[IKZF5]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ABHD4]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[BSDC1]] | +0.59 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[JMY]] | +0.57 | +0.42 / +0.63 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDSS1]] | -0.65 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[RNGTT]] | -0.60 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[NSUN2]] | -0.59 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[LYAR]] | -0.58 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[SCFD2]] | -0.54 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[POLR1B]] | -0.52 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[CDCA4]] | -0.51 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[SNRPD1]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[TERT]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[NME1]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[URB1]] | -0.51 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[LCLAT1]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JMY]] | C | GABARAPL1 activity raises JMY's level | lines that do not express GABARAPL1 (3) vs lines expressing it (47) | 2.68× lower at baseline in the lines without GABARAPL1 | 0.021 | ⚠ few lines (3 vs 47); across organs; also absent: GPR137B, ERO1B, TEX14; maybe low, not absent |

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-0.4, -46.1); signed map (-12.7, 11.2). **Vector** length 137, 42.6% of its response variance represented; |z| ≥ 3 in 1,336 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.6 | +14.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.0 | +14.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.7 | +15.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.6 | +5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.3 | +5.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.7 | +4.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +5.1 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.9 | +4.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.3 | -14.7 |
|  | [[EX229 (drug)]] 5 µM |  | -8.7 | -9.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.3 | -8.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.2 | -7.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.8 | -7.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -6.8 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | GABA type A receptor associated protein like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:10,212,458-10,223,128 (+) |
| Ensembl biotype | protein_coding |
| Also known as | gec1, APG8L, ATG8L, ATG8B |
| Gene groups (HGNC) | Autophagy related; GABA type A receptor-associated protein family |
| Hallmark sets | FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM, IL2_STAT5_SIGNALING |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0R8](https://www.uniprot.org/uniprotkb/Q9H0R8) (Gamma-aminobutyric acid receptor-associated protein-like 1):

> Ubiquitin-like modifier that increases cell-surface expression of kappa-type opioid receptor through facilitating anterograde intracellular trafficking of the receptor. Involved in formation of autophagosomal vacuoles. While LC3s are involved in elongation of the phagophore membrane, the GABARAP/GATE-16 subfamily is essential for a later stage in autophagosome maturation. Through its interaction with the reticulophagy receptor TEX264, participates in the remodeling of subdomains of the …

**Summary**, from NCBI Gene [23710](https://www.ncbi.nlm.nih.gov/gene/23710):

> Enables several functions, including Tat protein binding activity; cargo adaptor activity; and ubiquitin protein ligase binding activity. Acts upstream of or within glycophagy. Located in autophagosome and mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4068) · Entrez [23710](https://www.ncbi.nlm.nih.gov/gene/23710) · UniProt [Q9H0R8](https://www.uniprot.org/uniprotkb/Q9H0R8) · Ensembl [ENSG00000139112](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139112)

## Data

Gene col 6258: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6258); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6258, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6258]; `tensor/DDL_lfc|DDL_z.npy` [6258]; `embed/gene_vectors.npy` [6258]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6258 or target_col == 6258). Every well: [[GABARAPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABARAPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
