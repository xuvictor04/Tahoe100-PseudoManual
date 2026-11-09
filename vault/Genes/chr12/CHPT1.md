---
symbol: "CHPT1"
type: "gene"
col: 3254
ensembl_id: "ENSG00000111666"
name: "choline phosphotransferase 1"
location: "12q23.2"
module: 214
arm: "+"
pooled_cpm: 26.68
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/214"]
generated_by: "tahoemap"
---

# CHPT1

*choline phosphotransferase 1* — 12q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.50× (z +7.8, q 5e-12, up in 22 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.40× (z +6.7, q 5e-09, up in 24 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.436× (z -23.5, q 0e+00, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCB10]] (+0.67, fdr 7e-06), [[ACVR1B]] (+0.65, fdr 1e-05), [[SLC35D1]] (+0.64, fdr 9e-06); moves opposite to [[SYNJ2]] (-0.61, fdr 1e-05), [[BACH1]] (-0.60, fdr 8e-06), [[EHD1]] (-0.59, fdr 1e-05).
> It is in [[Module 214]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3254.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +7.8 | 5e-12 | 22/34 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +6.7 | 5e-09 | 24/46 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +6.5 | 2e-08 | 22/40 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.3 | 5e-08 | 22/41 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.33×** | +5.7 | 1e-06 | 21/45 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.27×** | +4.7 | 3e-04 | 20/45 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.6 | 3e-04 | 14/42 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.27×** | +4.4 | 6e-04 | 19/45 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +4.4 | 6e-04 | 13/46 (LoVo, RKO, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +4.4 | 7e-04 | 8/46 (BT-474, CFPAC-1, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.24×** | +4.3 | 9e-04 | 13/45 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.16× | +4.2 | 0.001 | 17/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +4.1 | 0.002 | 17/45 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.002 | 14/43 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.22×** | +3.9 | 0.003 | 14/46 (LoVo, NCI-H1573, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.004 | 16/45 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.20× | +3.5 | 0.014 | 10/45 (KATO III, LoVo, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.20× | +3.4 | 0.021 | 14/45 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.026 | 16/46 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | 1.18× | +3.3 | 0.026 | 15/45 (HOP62, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3254.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.436×** | -23.5 | 0e+00 | 40/46 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.537×** | -12.0 | 1e-30 | 32/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.591×** | -10.5 | 1e-23 | 30/46 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.600×** | -10.2 | 2e-22 | 31/45 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.611×** | -9.9 | 7e-21 | 32/46 (NCI-H460, KATO III, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.779×** | -5.0 | 5e-05 | 21/45 (NCI-H460, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.792×** | -4.7 | 2e-04 | 20/46 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.658×** | -4.4 | 8e-04 | 15/46 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.839× | -3.5 | 0.025 | 20/45 (A-172, KATO III, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.719×** | -3.5 | 0.030 | 12/44 (LS 180, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3254. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 43.2 | 18 | 7 | [[Triamcinolone (drug)]] 0.5 µM 2.79× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -29.5) |
| [[HOP62 (line)]] | alt | 10.3 | 13 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 6.75× (z +10.8) | — |
| [[A-172 (line)]] | wt | 29.5 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.247× (z -11.3) |
| [[LoVo (line)]] | wt | 24.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -16.0) |
| [[NCI-H1573 (line)]] | alt | 16.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.1) |
| [[PANC-1 (line)]] | alt | 27.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -12.6) |
| [[A-427 (line)]] | wt | 36.7 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -12.8) |
| [[A498 (line)]] | wt | 32.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.261× (z -13.7) |
| [[A549 (line)]] | wt | 45.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -16.6) |
| [[C32 (line)]] | wt | 51.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -17.5) |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0942× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 40.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -16.4) |
| [[KATO III (line)]] | alt | 40.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.336× (z -10.0) |
| [[SNU-1 (line)]] | wt | 45.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -9.5) |
| [[SW480 (line)]] | alt | 31.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -10.6) |
| [[AN3 CA (line)]] | alt | 45.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.147× (z -8.7) |
| [[HS-578T (line)]] | alt | 7.52 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0543× (z -12.7) |
| [[J82 (line)]] | alt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 27.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -21.2) |
| [[LS 180 (line)]] | wt | 26.3 | 0 | 1 | — | [[PF-06260933 (drug)]] 5 µM 0.0918× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 37.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -14.1) |
| [[RKO (line)]] | wt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.150× (z -10.3) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.4) |
| [[SW 900 (line)]] | alt | 29.1 | 1 | 0 | [[Triamcinolone (drug)]] 5 µM 2.53× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 30.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -9.2) |
| [[SW48 (line)]] | wt | 31.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3254), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB10]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ACVR1B]] | +0.65 | +0.78 / +0.57 | both halves | 1e-05 |  |
| [[SLC35D1]] | +0.64 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[AK3]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[AMFR]] | +0.62 | +0.65 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[USP46]] | +0.61 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[DRAM2]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[FDX1]] | +0.61 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[RAVER2]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PHKA1]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[EPB41L4B]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[FLVCR2]] | +0.58 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNJ2]] | -0.61 | -0.56 / -0.61 | both halves | 1e-05 | pathway: Phospholipid metabolism |
| [[BACH1]] | -0.60 | -0.57 / -0.62 | both halves | 8e-06 |  |
| [[EHD1]] | -0.59 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[LUCAT1]] | -0.59 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[SSUH2]] | -0.59 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[SPTBN5]] | -0.59 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[HRH1]] | -0.58 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[PDE2A]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[GPATCH2L]] | -0.57 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[PPP1R10]] | -0.57 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[CFAP251]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[POU2F2]] | -0.56 | -0.63 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises CHPT1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[NFIA]] | B | NFIA activity raises CHPT1's level | lines that do not express NFIA (11) vs lines expressing it (39) | 1.86× lower at baseline in the lines without NFIA | 0.027 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[ADAM8]] | B | ADAM8 activity lowers CHPT1's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.65× higher at baseline in the lines without ADAM8 | 0.030 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[NEK10]] | B | NEK10 activity raises CHPT1's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without NEK10 | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises CHPT1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[BIVM]] | C | BIVM activity raises CHPT1's level | lines that do not express BIVM (3) vs lines expressing it (47) | 3.43× lower at baseline in the lines without BIVM | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, RAPGEF4, SYCP2L; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ZDHHC11]] | C | ZDHHC11 activity raises CHPT1's level | lines that do not express ZDHHC11 (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without ZDHHC11 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[TMEM131L]] | C | TMEM131L activity raises CHPT1's level | lines that do not express TMEM131L (3) vs lines expressing it (47) | 1.62× lower at baseline in the lines without TMEM131L | 0.083 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: DPF1, TBC1D19, ARHGEF26; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 214]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-12.5, 14.8); signed map (-28.5, -18.2). **Vector** length 110, 26.9% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.2 | +6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.3 | +4.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.0 | +3.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.0 | +5.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.0 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.0 | -23.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -10.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -12.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -4.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | choline phosphotransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.2 — chr12:101,696,947-101,744,140 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CPT1 |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Synthesis of PC; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUD6](https://www.uniprot.org/uniprotkb/Q8WUD6) (Cholinephosphotransferase 1):

> Catalyzes the final step of de novo phosphatidylcholine (PC) synthesis, i.e. the transfer of choline phosphate from CDP-choline to the free hydroxyl of a diacylglycerol (DAG), producing a PC. It thereby plays a central role in the formation and maintenance of vesicular membranes.

**Summary**, from NCBI Gene [56994](https://www.ncbi.nlm.nih.gov/gene/56994):

> Enables diacylglycerol cholinephosphotransferase activity. Involved in phosphatidylcholine biosynthetic process and platelet activating factor biosynthetic process. Is active in Golgi membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17852) · Entrez [56994](https://www.ncbi.nlm.nih.gov/gene/56994) · UniProt [Q8WUD6](https://www.uniprot.org/uniprotkb/Q8WUD6) · Ensembl [ENSG00000111666](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111666)

## Data

Gene col 3254: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3254); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3254, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3254]; `tensor/DDL_lfc|DDL_z.npy` [3254]; `embed/gene_vectors.npy` [3254]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3254 or target_col == 3254). Every well: [[CHPT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHPT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
