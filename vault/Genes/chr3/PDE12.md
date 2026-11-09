---
symbol: "PDE12"
type: "gene"
col: 10532
ensembl_id: "ENSG00000174840"
name: "phosphodiesterase 12"
location: "3p14.3"
module: 1
arm: "+"
pooled_cpm: 22.09
n_lines_expressing: 50
n_dd_up: 48
n_dd_down: 2
n_dd_up_clean: 31
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PDE12

*phosphodiesterase 12* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.14× (z +26.0, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.840× (z -4.0, q 0.034, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.172×, LS 180 0.195×, NCI-H460 0.319×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.217×; ⚠ toxic; cell-cycle shift, explains ~47% of this change); [[Ponatinib (drug)]] 0.5 µM in 1 line (KATO III 0.225×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (COLO 205 0.102×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (AN3 CA 0.102×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIP7]] (+0.63, fdr 1e-05), [[TP53RK]] (+0.55, fdr 1e-05), [[CCDC86]] (+0.55, fdr 1e-05); moves opposite to [[TALAM1]] (-0.59, fdr 4e-05), [[SARAF]] (-0.54, fdr 3e-05), [[ZBTB47-AS1]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10532.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.14×** | +26.0 | 0e+00 | 46/47 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.64×** | +20.7 | 0e+00 | 46/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.58×** | +20.5 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.16×** | +18.5 | 0e+00 | 45/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.24×** | +18.2 | 0e+00 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.54×** | +15.0 | 0e+00 | 45/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +14.9 | 0e+00 | 43/47 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.47×** | +14.5 | 1e-45 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.46×** | +14.4 | 1e-45 | 45/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.45×** | +14.4 | 3e-45 | 45/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.43×** | +14.2 | 3e-44 | 45/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.38×** | +13.9 | 3e-42 | 44/47 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.90×** | +10.3 | 5e-23 | 34/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.82×** | +9.6 | 3e-20 | 40/47 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.77×** | +9.1 | 2e-18 | 39/47 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +9.1 | 5e-18 | 37/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.73×** | +8.8 | 6e-17 | 37/47 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.79×** | +8.6 | 2e-16 | 34/48 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +8.6 | 2e-16 | 37/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +6.3 | 7e-09 | 28/48 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +5.7 | 3e-07 | 29/47 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10532.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.172×, LS 180 0.195×, NCI-H460 0.319×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.217×; ⚠ toxic; cell-cycle shift, explains ~47% of this change); [[Ponatinib (drug)]] 0.5 µM in 1 line (KATO III 0.225×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (COLO 205 0.102×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (AN3 CA 0.102×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -4.0 | 0.034 | 16/48 (C32, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.716×** | -3.8 | 0.034 | 19/46 (C32, J82, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Meloxicam (drug)]] 0.5 µM |  | **0.803×** | -3.5 | 0.075 | 11/47 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[MK-3903 (drug)]] 5 µM |  | 0.678× | -3.3 | 0.15 | 12/45 (SW480, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.870× | -3.0 | 0.24 | 13/48 (SK-MEL-2, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10532. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 26.5 | 11 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.19× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.85× (z +14.7) | — |
| [[LOX-IMVI (line)]] | wt | 22.9 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +15.7) | — |
| [[NCI-H460 (line)]] | wt | 20.8 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 14.7 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +19.5) | — |
| [[LoVo (line)]] | wt | 22.8 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.10× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 22.3 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 17.9 | 5 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.23× (z +11.8) | [[Ponatinib (drug)]] 0.5 µM 0.225× (z -8.9) |
| [[RKO (line)]] | wt | 73.5 | 4 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 19.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.35× (z +18.1) | — |
| [[HOP62 (line)]] | alt | 12.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +13.3) | — |
| [[HEC-1-A (line)]] | alt | 26.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 16.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +13.3) | — |
| [[NCI-H2347 (line)]] | alt | 30.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +14.7) | — |
| [[A-427 (line)]] | wt | 22.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +9.8) | — |
| [[A549 (line)]] | wt | 14.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +14.0) | — |
| [[Hs 766T (line)]] | wt | 19.3 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.44× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.55× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 8.76 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 29.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.2) | — |
| [[SK-MEL-2 (line)]] | alt | 32.4 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.86× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 16.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 20.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.4) | — |
| [[A-172 (line)]] | wt | 13.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 14.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.3) | — |
| [[BT-474 (line)]] | alt | 19.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.72× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 9.66 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.63× (z +11.8) | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.102× (z -8.9) |
| [[HT-29 (line)]] | alt | 9.81 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +12.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 25.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +12.6) | — |
| [[Panc 03.27 (line)]] | alt | 20.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 37.1 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.102× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +11.5) | — |
| [[HCT15 (line)]] | alt | 26.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.00× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 37.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 25.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 40.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.39× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10532), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIP7]] | +0.63 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[TP53RK]] | +0.55 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CCDC86]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[INAFM2]] | +0.54 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[HGH1]] | +0.53 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[NOC3L]] | +0.53 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[VPS25]] | +0.53 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[MRPL35]] | +0.52 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ADO]] | +0.52 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[NANP]] | +0.52 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[MED27]] | +0.52 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[HSD17B10]] ⚠ | +0.51 | +0.62 / +0.52 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CIAPIN1]] | +0.51 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TALAM1]] | -0.59 | -0.42 / -0.69 | both halves | 4e-05 |  |
| [[SARAF]] | -0.54 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[ZBTB47-AS1]] | -0.54 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ECT2L]] | -0.52 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[RTN3]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[LRRC75A]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[NUCB2]] | -0.50 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[NSA2]] | -0.50 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[FBXO25]] | -0.49 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[FAM151B-DT]] | -0.49 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[EOGT-DT]] | -0.49 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[TMEM41B]] | -0.48 | -0.50 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PDE12's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.380). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-56.1, -5.2); signed map (3.7, -37.7). **Vector** length 68.2, 15.9% of its response variance represented; |z| ≥ 3 in 1,435 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +15.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +14.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +9.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +9.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.3 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -4.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.2 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:57,556,274-57,566,848 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp667B1218, 2'-PDE, 3635 |
| Reactome | 4 pathways, smallest: OAS antiviral response; Antimicrobial mechanism of IFN-stimulated genes; Interferon Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6L8Q7](https://www.uniprot.org/uniprotkb/Q6L8Q7) (2',5'-phosphodiesterase 12):

> Enzyme that cleaves 2',5'-phosphodiester bond linking adenosines of the 5'-triphosphorylated oligoadenylates, triphosphorylated oligoadenylates referred as 2-5A modulates the 2-5A system. Degrades triphosphorylated 2-5A to produce AMP and ATP. Also cleaves 3',5'-phosphodiester bond of oligoadenylates. Plays a role as a negative regulator of the 2-5A system that is one of the major pathways for antiviral and antitumor functions induced by interferons (IFNs). Suppression of this enzyme increases …

**Summary**, from NCBI Gene [201626](https://www.ncbi.nlm.nih.gov/gene/201626):

> Enables poly(A)-specific ribonuclease activity. Involved in several processes, including cellular response to interferon-alpha; innate immune response; and mRNA catabolic process. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25386) · Entrez [201626](https://www.ncbi.nlm.nih.gov/gene/201626) · UniProt [Q6L8Q7](https://www.uniprot.org/uniprotkb/Q6L8Q7) · Ensembl [ENSG00000174840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174840)

## Data

Gene col 10532: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10532); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10532, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10532]; `tensor/DDL_lfc|DDL_z.npy` [10532]; `embed/gene_vectors.npy` [10532]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10532 or target_col == 10532). Every well: [[PDE12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
