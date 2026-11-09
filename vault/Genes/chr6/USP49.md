---
symbol: "USP49"
type: "gene"
col: 8983
ensembl_id: "ENSG00000164663"
name: "ubiquitin specific peptidase 49"
location: "6p21.1"
module: 37
arm: "+"
pooled_cpm: 39.42
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# USP49

*ubiquitin specific peptidase 49* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.24× (z +25.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.714× (z -6.0, q 1e-06, down in 27 of 46 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (HCT15 0.0853×, HepG2/C3A 0.117×, RPMI-7951 0.202×, COLO 205 0.338×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (AN3 CA 0.0913×, NCI-H1792 0.190×, SW480 0.344×, KATO III 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 2 lines (NCI-H1792 0.247×, CFPAC-1 0.371×; ⚠ unreliable plate only); [[Resveratrol (drug)]] 0.5 µM in 1 line (SW 1271 0.0785×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BET1]] (+0.58, fdr 2e-05), [[KLRD1]] (+0.56, fdr 1e-05), [[PMS2P4-1]] (+0.55, fdr 4e-05); moves opposite to [[SLC6A17]] (-0.54, fdr 1e-04), [[CHST10]] (-0.53, fdr 1e-04), [[MOCS1]] (-0.52, fdr 4e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8983.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.24×** | +25.6 | 0e+00 | 48/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +21.3 | 0e+00 | 45/48 (AsPC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.30×** | +21.2 | 0e+00 | 48/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.30×** | +21.2 | 0e+00 | 48/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +19.9 | 0e+00 | 45/48 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +13.1 | 4e-37 | 43/48 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +9.8 | 6e-21 | 38/48 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +8.1 | 3e-14 | 36/48 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.33×** | +7.8 | 3e-13 | 29/49 (HS-578T, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.12×** | +7.0 | 2e-10 | 39/48 (A498, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +6.8 | 5e-10 | 30/48 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +6.3 | 2e-08 | 29/48 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.27×** | +5.9 | 1e-07 | 28/48 (J82, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +5.9 | 2e-07 | 22/48 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.9 | 2e-07 | 28/48 (SW1417, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +5.6 | 1e-06 | 29/48 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8983.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (HCT15 0.0853×, HepG2/C3A 0.117×, RPMI-7951 0.202×, COLO 205 0.338×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (AN3 CA 0.0913×, NCI-H1792 0.190×, SW480 0.344×, KATO III 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 2 lines (NCI-H1792 0.247×, CFPAC-1 0.371×; ⚠ unreliable plate only); [[Resveratrol (drug)]] 0.5 µM in 1 line (SW 1271 0.0785×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.714×** | -6.0 | 1e-06 | 27/46 (HCT15, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~1% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.783×** | -4.4 | 0.003 | 23/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **0.800×** | -4.0 | 0.013 | 21/46 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.836× | -3.2 | 0.16 | 12/48 (LS 180, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -3.2 | 0.16 | 12/48 (LoVo, SW480, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.714× | -3.1 | 0.16 | 10/48 (CFPAC-1, RKO, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 0.719× | -3.1 | 0.17 | 13/47 (HepG2/C3A, C32, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8983. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 39.1 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +17.4) | — |
| [[HS-578T (line)]] | alt | 48.9 | 9 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 28.6 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.94× (z +20.0) | — |
| [[HT-29 (line)]] | alt | 30.1 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 30.4 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +16.1) | — |
| [[SW480 (line)]] | alt | 40.9 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.95× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 211 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.28× (z +20.0) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -10.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 48.4 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -14.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 30.4 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +13.1) | [[Torkinib (drug)]] 5 µM 0.105× (z -8.5) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 44.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +21.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 44.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +14.1) | — |
| [[NCI-H2347 (line)]] | alt | 35.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +13.3) | — |
| [[Panc 03.27 (line)]] | alt | 47.7 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +15.8) | — |
| [[RPMI-7951 (line)]] | alt | 37.9 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -11.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 60.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +13.9) | — |
| [[J82 (line)]] | alt | 29.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.3) | — |
| [[LoVo (line)]] | wt | 25.9 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 7.01× (z +16.9) | — |
| [[NCI-H1792 (line)]] | alt | 31.8 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.36× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 31.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 39.9 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +13.1) | — |
| [[A498 (line)]] | wt | 27.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.96× (z +11.6) | — |
| [[A549 (line)]] | wt | 23.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.30× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 18.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.40× (z +16.7) | — |
| [[CFPAC-1 (line)]] | alt | 39.0 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +12.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.371× (z -8.8) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 37.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.29× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -9.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 46.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.50× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 33.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.39× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 47.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 30.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 43.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.92× (z +13.9) | — |
| [[RKO (line)]] | wt | 35.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.280× (z -8.6) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 40.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 28.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.54× (z +11.4) | — |
| [[A-427 (line)]] | wt | 42.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.31× (z +11.6) | — |
| [[C-33 A (line)]] | alt | 43.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.27× (z +10.2) | — |
| [[C32 (line)]] | wt | 25.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.15× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 16.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 31.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +11.7) | [[Docetaxel (drug)]] 0.05 µM 0.154× (z -13.0) ⚠ transcription drop; cell-cycle shift, explains ~61% of this change |
| [[AN3 CA (line)]] | alt | 92.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0913× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 51.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0853× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 64.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 47.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 50.5 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.0785× (z -8.9) |
| [[SW48 (line)]] | wt | 15.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8983), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BET1]] | +0.58 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[KLRD1]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[PMS2P4-1]] | +0.55 | +0.40 / +0.51 | both halves | 4e-05 |  |
| [[RSL1D1-DT]] | +0.54 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[CCDC18-AS1]] | +0.54 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[PRPF18]] | +0.54 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[ADAM20]] | +0.53 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[FAM117A]] | +0.53 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[NIFK-AS1]] | +0.53 | +0.60 / +0.37 | both halves | 9e-05 |  |
| [[GALK2]] | +0.53 | +0.63 / +0.33 | both halves | 1e-04 |  |
| [[LEPR]] | +0.52 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[CDKL3]] | +0.52 | +0.59 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A17]] | -0.54 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[CHST10]] | -0.53 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[MOCS1]] | -0.52 | -0.51 / -0.25 | both halves | 4e-04 |  |
| [[AADAT]] | -0.52 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[FAM124A]] | -0.51 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[BRSK2]] | -0.50 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[ELAC2]] | -0.50 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ALKBH8]] | -0.49 | -0.49 / -0.37 | both halves | 7e-05 |  |
| [[GPR63]] | -0.49 | -0.16 / -0.30 | ⚠ not reproduced | 0.001 |  |
| [[TSPYL5]] | -0.49 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[ULBP3]] | -0.48 | -0.43 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[OSBPL6]] | -0.48 | -0.44 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[TMEM201]] | -0.48 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[BLMH]] | -0.47 | -0.36 / -0.29 | both halves | 3e-04 |  |
| [[HERC2P3]] | -0.47 | -0.50 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers USP49's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DAGLA]] | C | DAGLA activity raises USP49's level | lines that do not express DAGLA (4) vs lines expressing it (46) | 1.71× lower at baseline in the lines without DAGLA | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PLEKHF1, NBEAP2, C2orf27A; maybe low, not absent |
| [[ULBP3]] | C | ULBP3 activity lowers USP49's level | lines that do not express ULBP3 (3) vs lines expressing it (47) | 2.03× higher at baseline in the lines without ULBP3 | 0.073 | ⚠ few lines (3 vs 47); across organs; also absent: SPDL1, ARHGAP10, CDC20; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.473). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.4, 30.6); signed map (6.8, 3.2). **Vector** length 66.9, 14.2% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +13.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +9.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.5 | +0.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +1.9 | +7.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +1.9 | +5.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.5 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +5.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.2 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -3.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.5 | -1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.5 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.9 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -1.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 49 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:41,789,896-41,895,375 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC20741 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70CQ1](https://www.uniprot.org/uniprotkb/Q70CQ1) (Ubiquitin carboxyl-terminal hydrolase 49):

> Deubiquitinase that plays a role in several cellular processes including transcriptional regulation, cell cycle progression or innate immunity. Specifically deubiquitinates histone H2B at 'Lys-120' (H2BK120Ub), a specific tag for epigenetic transcriptional activation and acts as a regulator of mRNA splicing. Antagonizes DNA double-strand break-induced ubiquitination of H2AX thereby participating in the maintenance of genome integrity. Plays a role in the negative regulation of cell …

**Summary**, from NCBI Gene [25862](https://www.ncbi.nlm.nih.gov/gene/25862):

> Enables histone binding activity and peptidase activity. Involved in mRNA splicing, via spliceosome; negative regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction; and protein deubiquitination. Predicted to be located in nucleoplasm. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20078) · Entrez [25862](https://www.ncbi.nlm.nih.gov/gene/25862) · UniProt [Q70CQ1](https://www.uniprot.org/uniprotkb/Q70CQ1) · Ensembl [ENSG00000164663](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164663)

## Data

Gene col 8983: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8983); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8983, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8983]; `tensor/DDL_lfc|DDL_z.npy` [8983]; `embed/gene_vectors.npy` [8983]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8983 or target_col == 8983). Every well: [[USP49 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP49.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
