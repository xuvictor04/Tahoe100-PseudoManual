---
symbol: "TDP2"
type: "gene"
col: 3285
ensembl_id: "ENSG00000111802"
name: "tyrosyl-DNA phosphodiesterase 2"
location: "6p22.3"
module: 135
arm: "+"
pooled_cpm: 41.51
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# TDP2

*tyrosyl-DNA phosphodiesterase 2* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.19× (z +25.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.716× (z -7.8, q 3e-12, down in 26 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.717× (z -7.7, q 3e-12, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF6]] (+0.72, fdr 2e-05), [[RIMOC1]] (+0.67, fdr 1e-05), [[METTL6]] (+0.65, fdr 2e-05); moves opposite to [[FAM118A]] (-0.62, fdr 2e-04), [[CTXN1]] (-0.62, fdr 5e-04), [[PI4KA]] (-0.60, fdr 5e-05).
> It sits in the **+** arm of [[Module 135]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3285.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +25.7 | 0e+00 | 46/48 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +19.0 | 0e+00 | 34/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +9.3 | 3e-18 | 36/48 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +8.6 | 9e-16 | 26/48 (J82, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.6 | 3e-12 | 32/48 (NCI-H1573, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +7.2 | 8e-11 | 25/47 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +6.4 | 1e-08 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +6.1 | 8e-08 | 24/48 (COLO 205, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +5.5 | 2e-06 | 21/48 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.2 | 9e-06 | 20/49 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.23×** | +4.8 | 7e-05 | 14/48 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.23×** | +4.8 | 7e-05 | 19/48 (J82, CHP-212, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.8 | 7e-05 | 21/48 (COLO 205, HT-29, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.46×** | +4.6 | 2e-04 | 16/47 (NCI-H460, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +4.6 | 2e-04 | 19/48 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +4.2 | 9e-04 | 16/48 (HOP62, A-172, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.4 | 0.017 | 13/47 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.11× | +3.3 | 0.024 | 8/49 (NCI-H460, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3285.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.716×** | -7.8 | 3e-12 | 26/47 (Hs 766T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.717×** | -7.7 | 3e-12 | 29/48 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.747×** | -6.8 | 2e-09 | 23/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.785×** | -5.6 | 3e-06 | 20/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.851× | -3.8 | 0.016 | 19/48 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.892× | -3.8 | 0.016 | 11/48 (NCI-H2030, NCI-H460, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.862× | -3.4 | 0.041 | 17/48 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.813×** | -3.4 | 0.041 | 17/47 (RPMI-7951, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Gallic acid (drug)]] 5 µM |  | 0.912× | -3.0 | 0.12 | 4/48 (SNU-1, HEC-1-A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | 0.779× | -3.0 | 0.12 | 6/48 (A-427, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lucanthone (drug)]] 5 µM |  | 0.874× | -3.0 | 0.12 | 7/48 (NCI-H2347, HEC-1-A, …) | top dose only | position effect removed |
| [[Bergenin (drug)]] 0.5 µM |  | 0.878× | -3.0 | 0.12 | 8/48 (hTERT-HPNE, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 25.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.74× (z +20.6) | — |
| [[HOP62 (line)]] | alt | 40.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +23.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.444× (z -8.6) |
| [[Hs 766T (line)]] | wt | 28.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.286× (z -9.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 38.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +17.5) | — |
| [[NCI-H1573 (line)]] | alt | 43.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 3.40× (z +8.6) | [[Lonafarnib (drug)]] 5 µM 0.0358× (z -12.8) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 42.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +16.5) | — |
| [[AsPC-1 (line)]] | alt | 25.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +14.4) | — |
| [[C32 (line)]] | wt | 22.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +17.3) | — |
| [[HCT15 (line)]] | alt | 49.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 35.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +8.7) | [[Lonafarnib (drug)]] 5 µM 0.141× (z -8.5) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 32.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +15.4) | — |
| [[J82 (line)]] | alt | 55.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +13.0) | — |
| [[KATO III (line)]] | alt | 42.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 45.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +22.0) | — |
| [[NCI-H1792 (line)]] | alt | 33.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +18.7) | — |
| [[PANC-1 (line)]] | alt | 34.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 61.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.378× (z -9.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 52.6 | 0 | 2 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0861× (z -9.0) |
| [[A-172 (line)]] | wt | 31.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +11.2) | — |
| [[A-427 (line)]] | wt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 24.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 44.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +18.9) | — |
| [[HEC-1-A (line)]] | alt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 45.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +14.5) | — |
| [[LS 180 (line)]] | wt | 79.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.332× (z -9.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[MIA PaCa-2 (line)]] | alt | 46.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +15.7) | — |
| [[NCI-H2347 (line)]] | alt | 28.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 42.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.1) | — |
| [[NCI-H661 (line)]] | alt | 33.3 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0632× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 52.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +11.4) | — |
| [[RKO (line)]] | wt | 35.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +18.8) | — |
| [[SW 900 (line)]] | alt | 35.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.4) | — |
| [[SW48 (line)]] | wt | 26.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.203× (z -8.6) |
| [[SW480 (line)]] | alt | 35.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +12.0) | — |
| [[A498 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF6]] | +0.72 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[RIMOC1]] | +0.67 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[METTL6]] | +0.65 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[CCDC117]] | +0.65 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[ZFR]] | +0.62 | +0.63 / +0.38 | both halves | 7e-05 |  |
| [[C17orf75]] | +0.62 | +0.63 / +0.33 | both halves | 1e-04 |  |
| [[BROX]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[TTC33]] | +0.61 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[ZXDA]] | +0.60 | +0.55 / +0.38 | both halves | 7e-05 |  |
| [[DNAJB4]] | +0.60 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[THAP2]] | +0.59 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[OSGIN2]] | +0.59 | +0.55 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.62 | -0.60 / -0.29 | both halves | 2e-04 |  |
| [[CTXN1]] | -0.62 | -0.58 / -0.23 | both halves | 5e-04 |  |
| [[PI4KA]] | -0.60 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[TXNL4A]] | -0.59 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[MAPK8]] | -0.56 | -0.58 / -0.33 | both halves | 1e-04 | pathway: DNA Double-Strand Break Repair |
| [[RHPN1]] | -0.56 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[MSH5]] | -0.54 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[NDUFA3]] | -0.53 | -0.52 / -0.21 | both halves | 6e-04 |  |
| [[CHTF18]] | -0.53 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[EML4]] | -0.53 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[GGA1]] | -0.53 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[ANTKMT]] | -0.53 | -0.38 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.734). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-19.1, 8.4); signed map (8.2, -29.0). **Vector** length 98.6, 21.1% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +25.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +19.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.5 | +8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | +2.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.5 | -3.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.5 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.1 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.1 | -7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -3.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.4 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | tyrosyl-DNA phosphodiesterase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:24,649,979-24,666,930 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TTRAP |
| Reactome | 3 pathways, smallest: Nonhomologous End-Joining (NHEJ); DNA Double-Strand Break Repair; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [O95551](https://www.uniprot.org/uniprotkb/O95551) (Tyrosyl-DNA phosphodiesterase 2):

> DNA repair enzyme that can remove a variety of covalent adducts from DNA through hydrolysis of a 5'-phosphodiester bond, giving rise to DNA with a free 5' phosphate. Catalyzes the hydrolysis of dead-end complexes between DNA and the topoisomerase 2 (TOP2) active site tyrosine residue. The 5'-tyrosyl DNA phosphodiesterase activity can enable the repair of TOP2-induced DNA double-strand breaks/DSBs without the need for nuclease activity, creating a 'clean' DSB with 5'-phosphate termini that are …

**Summary**, from NCBI Gene [51567](https://www.ncbi.nlm.nih.gov/gene/51567):

> This gene encodes a member of a superfamily of divalent cation-dependent phosphodiesterases. The encoded protein associates with CD40, tumor necrosis factor (TNF) receptor-75 and TNF receptor associated factors (TRAFs), and inhibits nuclear factor-kappa-B activation. This protein has sequence and structural similarities with APE1 endonuclease, which is involved in both DNA repair and the activation of transcription factors. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17768) · Entrez [51567](https://www.ncbi.nlm.nih.gov/gene/51567) · UniProt [O95551](https://www.uniprot.org/uniprotkb/O95551) · Ensembl [ENSG00000111802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111802)

## Data

Gene col 3285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3285); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3285]; `tensor/DDL_lfc|DDL_z.npy` [3285]; `embed/gene_vectors.npy` [3285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3285 or target_col == 3285). Every well: [[TDP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TDP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
