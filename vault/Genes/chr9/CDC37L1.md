---
symbol: "CDC37L1"
type: "gene"
col: 2819
ensembl_id: "ENSG00000106993"
name: "cell division cycle 37 like 1, HSP90 cochaperone"
location: "9p24.1"
module: 187
arm: "+"
pooled_cpm: 31.41
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# CDC37L1

*cell division cycle 37 like 1, HSP90 cochaperone* — 9p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.11× (z +18.4, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.642× (z -7.4, q 6e-11, down in 24 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Esmolol (hydrochloride) (drug)]] 5 µM: 0.803× (z -3.8, q 0.015, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (hTERT-HPNE 0.100×, LOX-IMVI 0.183×, A498 0.296×, KATO III 0.247×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A498 0.329×, Panc 03.27 0.219×, KATO III 0.235×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW1417 0.193×, A498 0.263×; ⚠ toxic; transcription drop); [[Brimonidine (drug)]] 0.5 µM in 1 line (C-33 A 0.138×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NKAP]] (+0.75, fdr 7e-06), [[TERF2IP]] (+0.74, fdr 7e-06), [[EAPP]] (+0.74, fdr 7e-06); moves opposite to [[MTHFD1]] (-0.65, fdr 1e-05), [[TFDP1]] (-0.63, fdr 1e-05), [[LMNB2]] (-0.63, fdr 1e-05).
> It is in [[Module 187]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOXA9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2819.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +18.4 | 0e+00 | 45/48 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +17.5 | 0e+00 | 43/47 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +12.5 | 1e-33 | 43/47 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +9.8 | 1e-20 | 39/48 (RKO, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +9.2 | 4e-18 | 37/48 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +9.2 | 5e-18 | 42/46 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +8.8 | 1e-16 | 35/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.64×** | +8.6 | 4e-16 | 28/48 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.56×** | +7.5 | 6e-12 | 34/48 (COLO 205, SW480, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +6.8 | 8e-10 | 28/46 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.7 | 9e-10 | 32/48 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.45×** | +6.4 | 6e-09 | 35/46 (LoVo, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +6.4 | 6e-09 | 30/47 (hTERT-HPNE, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +5.3 | 6e-06 | 24/48 (hTERT-HPNE, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +5.2 | 9e-06 | 24/48 (hTERT-HPNE, HepG2/C3A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +4.8 | 5e-05 | 23/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.022 | 13/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +2.9 | 0.075 | 7/48 (hTERT-HPNE, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +2.9 | 0.076 | 14/48 (CFPAC-1, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2819.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (hTERT-HPNE 0.100×, LOX-IMVI 0.183×, A498 0.296×, KATO III 0.247×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A498 0.329×, Panc 03.27 0.219×, KATO III 0.235×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW1417 0.193×, A498 0.263×; ⚠ toxic; transcription drop); [[Brimonidine (drug)]] 0.5 µM in 1 line (C-33 A 0.138×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.642×** | -7.4 | 6e-11 | 24/37 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.696×** | -6.3 | 8e-08 | 27/48 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.684×** | -6.1 | 2e-07 | 26/40 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.691×** | -4.4 | 0.002 | 20/44 (SW1417, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.803×** | -3.8 | 0.015 | 16/48 (NCI-H460, KATO III, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.808×** | -3.7 | 0.020 | 14/48 (SW1417, A498, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.878× | -3.2 | 0.11 | 12/48 (COLO 205, C32, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.841× | -3.0 | 0.19 | 7/48 (A498, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2819. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 40.8 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 30.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +14.1) | — |
| [[LS 180 (line)]] | wt | 38.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 92.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -13.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 28.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.1) | — |
| [[Panc 03.27 (line)]] | alt | 41.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -11.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 38.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.8) | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +13.0) | — |
| [[HT-29 (line)]] | alt | 39.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +15.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 27.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 19.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +14.4) | — |
| [[NCI-H460 (line)]] | wt | 27.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 35.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 45.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -10.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 25.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.138× (z -10.0) |
| [[C32 (line)]] | wt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 27.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +12.5) | — |
| [[HCT15 (line)]] | alt | 34.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 33.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -13.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 28.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 28.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 15.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.1) | — |
| [[RKO (line)]] | wt | 46.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 37.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 29.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.0) | — |
| [[SW48 (line)]] | wt | 45.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -9.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2819), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAP]] | +0.75 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[EAPP]] | +0.74 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[ADPRM]] | +0.72 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.68 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[TMEM258]] | +0.66 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[MED19]] | +0.66 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[ATXN3]] | +0.66 | +0.36 / +0.72 | both halves | 9e-05 |  |
| [[CCDC186]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[SCAND1]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[KLHDC2]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[WHAMM]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFD1]] | -0.65 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.63 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[LMNB2]] | -0.63 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[VMA21]] | -0.63 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[YWHAQ]] | -0.62 | -0.61 / -0.57 | both halves | 9e-06 |  |
| [[HNRNPA3]] | -0.62 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.61 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.60 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[SLC25A10]] | -0.60 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[G3BP1]] | -0.59 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[NONO]] | -0.59 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[DHX9]] | -0.59 | -0.41 / -0.60 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA9]] | B | HOXA9 activity raises CDC37L1's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 1.45× lower at baseline in the lines without HOXA9 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-29.0, -31.5); signed map (-13.7, 5.5). **Vector** length 83.7, 19.0% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +18.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +9.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +6.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.3 | +12.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.7 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.0 | -6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | +0.1 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 37 like 1, HSP90 cochaperone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:4,679,559-4,708,399 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HARC, FLJ20639, CDC37B |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L3B6](https://www.uniprot.org/uniprotkb/Q7L3B6) (Hsp90 co-chaperone Cdc37-like 1):

> Co-chaperone that binds to numerous proteins and promotes their interaction with Hsp70 and Hsp90.

**Summary**, from NCBI Gene [55664](https://www.ncbi.nlm.nih.gov/gene/55664):

> CDC37L1 is a cytoplasmic phosphoprotein that exists in complex with HSP90 (HSPCA; MIM 140571) as well as several other proteins involved in HSP90-mediated protein folding (Scholz et al., 2001 [PubMed 11413142]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:17179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17179) · Entrez [55664](https://www.ncbi.nlm.nih.gov/gene/55664) · UniProt [Q7L3B6](https://www.uniprot.org/uniprotkb/Q7L3B6) · Ensembl [ENSG00000106993](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106993)

## Data

Gene col 2819: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2819); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2819, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2819]; `tensor/DDL_lfc|DDL_z.npy` [2819]; `embed/gene_vectors.npy` [2819]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2819 or target_col == 2819). Every well: [[CDC37L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC37L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
