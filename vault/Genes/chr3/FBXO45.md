---
symbol: "FBXO45"
type: "gene"
col: 10454
ensembl_id: "ENSG00000174013"
name: "F-box protein 45"
location: "3q29"
module: 119
arm: "+"
pooled_cpm: 37.8
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# FBXO45

*F-box protein 45* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (18 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.44× (z +10.4, q 2e-22, up in 45 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.26× (z +9.8, q 2e-20, up in 42 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.114×, HEC-1-A 0.262×, C32 0.196×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (KATO III 0.0761×, C32 0.0822×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.150×, SK-MEL-2 0.278×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIFK]] (+0.68, fdr 7e-06), [[CCDC137]] (+0.67, fdr 7e-06), [[LEO1]] (+0.65, fdr 2e-05); moves opposite to [[MORF4L1]] (-0.69, fdr 3e-05), [[LAMP2]] (-0.63, fdr 1e-05), [[PAPOLA]] (-0.60, fdr 5e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PAQR7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10454.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.44×** | +10.4 | 2e-22 | 45/47 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +9.8 | 2e-20 | 42/47 (CFPAC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.99×** | +8.3 | 2e-14 | 43/48 (LOX-IMVI, PANC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.13×** | +7.6 | 5e-12 | 38/48 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.80×** | +7.1 | 2e-10 | 43/48 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.79×** | +7.0 | 2e-10 | 43/48 (LoVo, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.77×** | +6.9 | 4e-10 | 41/48 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.50×** | +6.9 | 4e-10 | 31/47 (CFPAC-1, KATO III, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.52×** | +5.8 | 4e-07 | 34/48 (COLO 205, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.40×** | +5.7 | 8e-07 | 31/48 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +5.4 | 4e-06 | 34/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.55×** | +5.1 | 2e-05 | 28/47 (NCI-H23, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.51×** | +5.0 | 3e-05 | 31/47 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.54×** | +5.0 | 3e-05 | 33/48 (SW480, COLO 205, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.56×** | +4.9 | 3e-05 | 33/47 (MIA PaCa-2, LOX-IMVI, …) | all doses, flat | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.77×** | +3.6 | 0.010 | 20/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.013 | 23/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.65×** | +3.1 | 0.040 | 18/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.040 | 20/47 (A498, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.57×** | +2.8 | 0.096 | 13/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +2.8 | 0.096 | 12/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10454.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.114×, HEC-1-A 0.262×, C32 0.196×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (KATO III 0.0761×, C32 0.0822×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.150×, SK-MEL-2 0.278×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.726× | -3.6 | 0.11 | 24/48 (A-427, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.570× | -3.6 | 0.11 | 22/48 (A-427, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.745× | -3.4 | 0.11 | 23/47 (SW 1271, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.827× | -3.2 | 0.19 | 22/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.835× | -3.1 | 0.19 | 13/48 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Folic acid (drug)]] 5 µM |  | 0.836× | -3.1 | 0.19 | 15/48 (HS-578T, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.764× | -3.0 | 0.19 | 21/43 (KATO III, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 0.773× | -3.0 | 0.19 | 15/47 (HOP62, hTERT-HPNE, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 43.8 | 3 (2 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.59× (z +9.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.04× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0761× (z -18.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 52.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 33.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0822× (z -15.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 34.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.93× (z +11.7) | — |
| [[HT-29 (line)]] | alt | 31.2 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.12× (z +11.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.50× (z +8.7) | — |
| [[SW480 (line)]] | alt | 50.7 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.64× (z +10.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.40× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 35.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.31× (z +9.2) | — |
| [[J82 (line)]] | alt | 61.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.70× (z +8.7) ⚠ toxic | — |
| [[LOX-IMVI (line)]] | wt | 43.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 3.46× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 60.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.71× (z +11.4) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 29.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.04× (z +10.0) | — |
| [[RKO (line)]] | wt | 50.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.44× (z +8.9) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 6 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIFK]] | +0.68 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[CCDC137]] | +0.67 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[LEO1]] | +0.65 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[C16orf91]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[IMP3]] | +0.65 | +0.38 / +0.73 | both halves | 6e-05 |  |
| [[ZNF593]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[NUDT22]] | +0.65 | +0.37 / +0.69 | both halves | 7e-05 |  |
| [[MRPS26]] | +0.64 | +0.42 / +0.73 | both halves | 4e-05 |  |
| [[C1orf35]] | +0.64 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[MRPL36]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[GADD45GIP1]] | +0.63 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[ADPRS]] | +0.62 | +0.48 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MORF4L1]] | -0.69 | -0.44 / -0.80 | both halves | 3e-05 |  |
| [[LAMP2]] | -0.63 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[PAPOLA]] | -0.60 | -0.39 / -0.70 | both halves | 5e-05 |  |
| [[GALC]] | -0.59 | -0.31 / -0.65 | both halves | 2e-04 |  |
| [[ACADVL]] | -0.57 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[TPP1]] | -0.57 | -0.33 / -0.63 | both halves | 1e-04 |  |
| [[GNS]] | -0.56 | -0.36 / -0.63 | both halves | 9e-05 |  |
| [[IGF2R]] | -0.56 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[CTSD]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[LAMP1]] | -0.55 | -0.35 / -0.63 | both halves | 1e-04 |  |
| [[NUCB1]] | -0.55 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[DHFR]] | -0.54 | -0.27 / -0.59 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAQR7]] | B | PAQR7 activity raises FBXO45's level | lines that do not express PAQR7 (5) vs lines expressing it (45) | 1.11× lower at baseline in the lines without PAQR7 | 0.069 | ⚠ within organs, on part of the lines; also absent: DBN1, VASN, LTBP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.5, -9.6); signed map (-13.2, -7.7). **Vector** length 93.1, 26.4% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +10.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +2.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -9.5 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -9.4 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.9 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | +2.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.6 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +0.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 45 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,568,611-196,589,059 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Fbx45 |
| Gene groups (HGNC) | F-boxes other |
| Matched by | ensembl_id |

**Function**, from UniProt [P0C2W1](https://www.uniprot.org/uniprotkb/P0C2W1) (F-box/SPRY domain-containing protein 1):

> Component of E3 ubiquitin ligase complex consisting of FBXO45, MYCBP2 and SKP1. Functions in substrate recognition but also plays an important role in assembly of the complex. Required for normal neuromuscular synaptogenesis, axon pathfinding and neuronal migration (By similarity). Regulates neuron migration during brain development through interaction with N-cadherin/CDH2 after secretion via a non-classical mechanism (By similarity). Plays a role in the regulation of neurotransmission at …

**Summary**, from NCBI Gene [200933](https://www.ncbi.nlm.nih.gov/gene/200933):

> Members of the F-box protein family, such as FBXO45, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (summary by Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Jan 2011]

**Accessions** — [HGNC:29148](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29148) · Entrez [200933](https://www.ncbi.nlm.nih.gov/gene/200933) · UniProt [P0C2W1](https://www.uniprot.org/uniprotkb/P0C2W1) · Ensembl [ENSG00000174013](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174013)

## Data

Gene col 10454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10454); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10454]; `tensor/DDL_lfc|DDL_z.npy` [10454]; `embed/gene_vectors.npy` [10454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10454 or target_col == 10454). Every well: [[FBXO45 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO45.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
