---
symbol: "TLE1"
type: "gene"
col: 12282
ensembl_id: "ENSG00000196781"
name: "TLE family member 1, transcriptional corepressor"
location: "9q21.32"
module: 106
arm: "+"
pooled_cpm: 65.92
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# TLE1

*TLE family member 1, transcriptional corepressor* — 9q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.47× (z +14.0, q 2e-41, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.590× (z -13.1, q 3e-36, down in 28 of 38 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (PANC-1 0.318×, A549 0.393×, SK-MEL-2 0.385×, NCI-H1573 0.432×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 0.275×, A549 0.270×, NCI-H2347 0.406×, KATO III 0.364×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 0.403×, A549 0.447×; ⚠ cell-cycle shift, explains ~10% of this change); [[Auranofin (drug)]] 5 µM in 1 line (HT-29 0.476×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGD4]] (+0.57, fdr 2e-05), [[EPS8]] (+0.57, fdr 1e-05), [[LGR4]] (+0.55, fdr 1e-05); moves opposite to [[ALG13]] (-0.58, fdr 1e-05), [[KRBOX4]] (-0.53, fdr 1e-05), [[FAM120B]] (-0.47, fdr 5e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EDN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12282.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +14.0 | 2e-41 | 39/46 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.42×** | +11.1 | 2e-26 | 32/47 (J82, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +11.1 | 2e-26 | 31/45 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +9.5 | 2e-19 | 29/46 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +8.8 | 2e-16 | 25/46 (RKO, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +6.9 | 6e-10 | 22/46 (NCI-H1792, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +6.7 | 2e-09 | 27/46 (Panc 03.27, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.28×** | +6.2 | 3e-08 | 20/46 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.27×** | +6.2 | 5e-08 | 23/47 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +5.8 | 5e-07 | 22/47 (SW1417, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.24×** | +5.4 | 3e-06 | 16/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.25×** | +5.4 | 3e-06 | 21/47 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.23×** | +5.4 | 4e-06 | 21/48 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +5.2 | 7e-06 | 13/46 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.15× | +5.1 | 1e-05 | 19/46 (RPMI-7951, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.48×** | +5.0 | 3e-05 | 18/46 (NCI-H1573, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +4.9 | 3e-05 | 16/46 (C32, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12282.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (PANC-1 0.318×, A549 0.393×, SK-MEL-2 0.385×, NCI-H1573 0.432×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 0.275×, A549 0.270×, NCI-H2347 0.406×, KATO III 0.364×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 0.403×, A549 0.447×; ⚠ cell-cycle shift, explains ~10% of this change); [[Auranofin (drug)]] 5 µM in 1 line (HT-29 0.476×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -13.1 | 3e-36 | 28/38 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.623×** | -12.2 | 1e-31 | 29/45 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Vilanterol (drug)]] 0.05 µM |  | 0.859× | -3.9 | 0.015 | 7/45 (SNU-1, PANC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -3.9 | 0.015 | 17/46 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.909× | -3.5 | 0.047 | 19/47 (NCI-H2347, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | 0.870× | -3.3 | 0.078 | 16/42 (SHP-77, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.887× | -3.1 | 0.15 | 14/46 (NCI-H2347, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12282. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 39.3 | 7 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 3.17× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 96.4 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 172 | 1 | 6 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.74× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -18.5) ⚠ cell-cycle shift, explains ~10% of this change |
| [[A549 (line)]] | wt | 144 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 61.7 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 3.35× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -10.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 106 | 2 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.54× (z +10.3) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 5.77× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -10.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 40.6 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.77× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -23.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 80.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[HS-578T (line)]] | alt | 46.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.13× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 46.3 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.03× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 49.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 32.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.11× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -9.6) ⚠ cell-cycle shift, explains ~10% of this change |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -14.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 30.4 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.88× (z +11.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 2.80× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 108 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.476× (z -9.3) |
| [[KATO III (line)]] | alt | 85.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -12.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 55.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.31× (z +12.1) | — |
| [[SW48 (line)]] | wt | 54.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 123 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 66.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -8.9) ⚠ cell-cycle shift, explains ~10% of this change |
| [[HepG2_C3A (line)]] | wt | 135 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.383× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 42.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 49.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.79× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 70.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 31.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 23.7 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.20× (z +9.6) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 141 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.12× (z +8.7) | — |
| [[RKO (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -10.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.61× (z +10.5) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 100 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 63.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12282), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGD4]] | +0.57 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[EPS8]] | +0.57 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[LGR4]] | +0.55 | +0.49 / +0.56 | both halves | 1e-05 | pathway: Signaling by WNT |
| [[PRKAR2B]] | +0.55 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[FLVCR2]] | +0.55 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[GAREM1]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[TMEM131L]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[UGCG]] | +0.53 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[PELI1]] | +0.52 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[BCL6]] | +0.51 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[GNAI1]] | +0.51 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[FNBP1L]] | +0.51 | +0.41 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG13]] | -0.58 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[KRBOX4]] | -0.53 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[FAM120B]] | -0.47 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[GPATCH2L]] | -0.47 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[BBS1]] | -0.47 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[ADGRL1-AS1]] | -0.46 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[ZCCHC4]] | -0.46 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[MYSM1]] | -0.45 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[GOLGA1]] | -0.45 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[RABGEF1P3]] | -0.45 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[KIAA0753]] | -0.44 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[ERCC6L2]] | -0.44 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDN2]] | B | EDN2 activity raises TLE1's level | lines that do not express EDN2 (30) vs lines expressing it (20) | 1.37× lower at baseline in the lines without EDN2 | 0.082 | ⚠ within organs, on part of the lines; also absent: WNT7A, FAM83A, CST6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.7, 43.2); signed map (19.5, 26.8). **Vector** length 119, 31.8% of its response variance represented; |z| ≥ 3 in 1,339 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +14.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +8.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.9 | +11.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.0 | +5.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.9 | +6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.7 | +2.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.3 | -12.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.0 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | TLE family member 1, transcriptional corepressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.32 — chr9:81,583,683-81,689,547 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ESG1, GRG1, ESG, TLE-1 |
| Gene groups (HGNC) | WD repeat domain containing; Wnt enhanceosome complex; TLE family |
| Hallmark sets | HEDGEHOG_SIGNALING |
| Reactome | 18 pathways, smallest: Repression of WNT target genes; Deactivation of the beta-catenin transactivating complex; NOTCH1 Intracellular Domain Regulates Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04724](https://www.uniprot.org/uniprotkb/Q04724) (Transducin-like enhancer protein 1):

> Transcriptional corepressor that binds to a number of transcription factors. Inhibits NF-kappa-B-regulated gene expression. Inhibits the transcriptional activation mediated by FOXA2, and by CTNNB1 and TCF family members in Wnt signaling. Enhances FOXG1/BF-1- and HES1-mediated transcriptional repression (By similarity). The effects of full-length TLE family members may be modulated by association with dominant-negative AES. Unusual function as coactivator for ESRRG.

**Summary**, from NCBI Gene [7088](https://www.ncbi.nlm.nih.gov/gene/7088):

> Enables DNA-binding transcription factor binding activity; identical protein binding activity; and transcription corepressor activity. Involved in negative regulation of anoikis; negative regulation of signal transduction; and regulation of gene expression. Located in cytosol and nucleoplasm. Part of beta-catenin-TCF complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11837](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11837) · Entrez [7088](https://www.ncbi.nlm.nih.gov/gene/7088) · UniProt [Q04724](https://www.uniprot.org/uniprotkb/Q04724) · Ensembl [ENSG00000196781](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196781)

## Data

Gene col 12282: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12282); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12282, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12282]; `tensor/DDL_lfc|DDL_z.npy` [12282]; `embed/gene_vectors.npy` [12282]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12282 or target_col == 12282). Every well: [[TLE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
