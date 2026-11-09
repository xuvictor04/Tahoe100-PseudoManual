---
symbol: "CMTR2"
type: "gene"
col: 11148
ensembl_id: "ENSG00000180917"
name: "cap methyltransferase 2"
location: "16q22.2"
module: 11
arm: "+"
pooled_cpm: 22.64
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CMTR2

*cap methyltransferase 2* — 16q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.13× (z +29.7, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.770× (z -4.8, q 7e-04, down in 21 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SW480 0.0716×, LS 180 0.0918×, PANC-1 0.211×, KATO III 0.180×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.155×, MIA PaCa-2 0.230×, C32 0.128×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.187×, LS 180 0.460×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (RKO 0.367×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF518A]] (+0.71, fdr 7e-06), [[RPP25L]] (+0.70, fdr 7e-06), [[GSPT2]] (+0.69, fdr 7e-06); moves opposite to [[TM9SF2]] (-0.69, fdr 7e-06), [[SEC23A]] (-0.69, fdr 7e-06), [[KDELR1]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TSPAN13]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11148.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.13×** | +29.7 | 0e+00 | 46/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.20×** | +21.4 | 0e+00 | 46/46 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.81×** | +18.3 | 0e+00 | 45/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.45×** | +16.5 | 0e+00 | 44/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.98×** | +12.6 | 4e-34 | 41/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.95×** | +12.2 | 2e-32 | 36/45 (BT-474, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.85×** | +11.3 | 1e-27 | 36/48 (BT-474, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.68×** | +9.5 | 1e-19 | 32/47 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +8.0 | 5e-14 | 31/48 (A-172, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.55×** | +8.0 | 5e-14 | 29/47 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +6.1 | 7e-08 | 22/46 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.4 | 3e-06 | 22/44 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +5.2 | 1e-05 | 21/45 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 3e-04 | 15/47 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +4.4 | 4e-04 | 18/47 (HEC-1-A, BT-474, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.001 | 12/46 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.009 | 14/47 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.017 | 19/45 (SW480, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.20× | +3.3 | 0.032 | 7/48 (HT-29, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11148.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SW480 0.0716×, LS 180 0.0918×, PANC-1 0.211×, KATO III 0.180×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.155×, MIA PaCa-2 0.230×, C32 0.128×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.187×, LS 180 0.460×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (RKO 0.367×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.770×** | -4.8 | 7e-04 | 21/42 (RKO, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.790×** | -4.0 | 0.015 | 17/36 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.822×** | -3.5 | 0.088 | 13/32 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.889× | -3.1 | 0.27 | 21/47 (RKO, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 29.1 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +14.1) | — |
| [[NCI-H2030 (line)]] | alt | 28.5 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 13.1 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -12.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 25.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +17.8) | — |
| [[SW480 (line)]] | alt | 36.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.0716× (z -30.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 31.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +15.3) | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -12.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 84.3 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -21.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.367× (z -8.7) |
| [[A-427 (line)]] | wt | 30.8 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.17× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 12.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +14.2) | — |
| [[COLO 205 (line)]] | alt | 22.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +13.5) | — |
| [[HOP62 (line)]] | alt | 24.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +15.8) | — |
| [[J82 (line)]] | alt | 21.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +13.0) | — |
| [[KATO III (line)]] | alt | 24.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 24.7 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.80× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 47.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.0918× (z -20.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 46.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.8) | [[Adagrasib (drug)]] 0.05 µM 0.631× (z -14.1) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 11.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -12.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 13.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -13.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 15.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 18.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +13.9) | — |
| [[HEC-1-A (line)]] | alt | 20.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -9.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 36.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +9.1) | [[Simotinib (drug)]] 5 µM 0.117× (z -9.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 34.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.100× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -11.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.53× (z +14.1) | — |
| [[LoVo (line)]] | wt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 29.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +11.2) | — |
| [[A498 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF518A]] | +0.71 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.70 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[GSPT2]] | +0.69 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.68 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[CWC22]] | +0.67 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[METTL18]] | +0.67 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[MAPK1IP1L]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.66 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.66 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[RPL7L1]] | +0.66 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[SDSL]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ZNF317]] | +0.64 | +0.52 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM9SF2]] | -0.69 | -0.69 / -0.66 | both halves | 7e-06 |  |
| [[SEC23A]] | -0.69 | -0.71 / -0.66 | both halves | 7e-06 |  |
| [[KDELR1]] | -0.67 | -0.74 / -0.56 | both halves | 1e-05 |  |
| [[GSDMB]] | -0.66 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[IER3IP1]] | -0.66 | -0.72 / -0.56 | both halves | 1e-05 |  |
| [[COPA]] | -0.65 | -0.74 / -0.58 | both halves | 7e-06 |  |
| [[DDB1]] | -0.65 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[SDHAP4]] | -0.64 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[SAR1A]] | -0.64 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[STRAP]] | -0.64 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[CALU]] | -0.61 | -0.57 / -0.64 | both halves | 9e-06 |  |
| [[NAP1L4]] | -0.61 | -0.65 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN13]] | B | TSPAN13 activity lowers CMTR2's level | lines that do not express TSPAN13 (13) vs lines expressing it (37) | 1.30× higher at baseline in the lines without TSPAN13 | 0.053 | ⚠ within organs, on part of the lines; also absent: JUP, MPZL3, MYO5C |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.1, 7.1); signed map (1.1, -21.0). **Vector** length 97.7, 22.5% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.5 | +21.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.3 | +16.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.7 | +18.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.3 | +12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +29.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.0 | +6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.2 | +3.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.7 | -4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.7 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -0.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.3 | +0.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | +2.2 |

## What is on record

|  |  |
|---|---|
| Name | cap methyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.2 — chr16:71,281,389-71,289,715 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11171, AFT, MTr2; previously FTSJD1 |
| Gene groups (HGNC) | 7BS 2'O-ribose DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYT2](https://www.uniprot.org/uniprotkb/Q8IYT2) (Cap-specific mRNA):

> S-adenosyl-L-methionine-dependent methyltransferase that mediates mRNA cap2 2'-O-ribose methylation to the 5'-cap structure of mRNAs. Methylates the ribose of the second nucleotide of a m(7)GpppG-capped mRNA and small nuclear RNA (snRNA) (cap0) to produce m(7)GpppRmpNm (cap2). Recognizes a guanosine cap on RNA independently of its N(7) methylation status. Display cap2 methylation on both cap0 and cap1. Displays a preference for cap1 RNAs.

**Summary**, from NCBI Gene [55783](https://www.ncbi.nlm.nih.gov/gene/55783):

> Enables methyltransferase cap2 activity. Involved in 7-methylguanosine mRNA capping. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25635](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25635) · Entrez [55783](https://www.ncbi.nlm.nih.gov/gene/55783) · UniProt [Q8IYT2](https://www.uniprot.org/uniprotkb/Q8IYT2) · Ensembl [ENSG00000180917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180917)

## Data

Gene col 11148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11148); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11148]; `tensor/DDL_lfc|DDL_z.npy` [11148]; `embed/gene_vectors.npy` [11148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11148 or target_col == 11148). Every well: [[CMTR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMTR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
