---
symbol: "ERI2"
type: "gene"
col: 12263
ensembl_id: "ENSG00000196678"
name: "ERI1 exoribonuclease family member 2"
location: "16p12.3"
module: 39
arm: "+"
pooled_cpm: 27.95
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# ERI2

*ERI1 exoribonuclease family member 2* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +15.7, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.481× (z -10.5, q 3e-23, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C21orf91-OT1]] (+0.79, fdr 7e-06), [[C3orf20]] (+0.74, fdr 1e-05), [[HCLS1]] (+0.74, fdr 7e-06); moves opposite to [[SLC23A2]] (-0.63, fdr 2e-05), [[SERAC1]] (-0.62, fdr 1e-05), [[FAM118A]] (-0.61, fdr 7e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC02284]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12263.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +15.7 | 0e+00 | 43/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +13.5 | 3e-39 | 40/47 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +8.6 | 1e-15 | 30/47 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.56×** | +6.4 | 2e-08 | 28/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.9 | 4e-07 | 26/48 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +5.8 | 7e-07 | 28/48 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.52×** | +5.8 | 7e-07 | 28/47 (A-172, A498, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.4 | 5e-06 | 26/48 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **1.32×** | +4.1 | 0.003 | 16/43 (HEC-1-A, HOP62, …) | two highest doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.013 | 17/48 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.026 | 15/48 (NCI-H2347, J82, …) | rises with dose | low cells (technical?) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.033 | 13/48 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.4 | 0.033 | 16/48 (HOP62, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.050 | 17/47 (CHP-212, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.094 | 20/48 (HCT15, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Filgotinib (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.094 | 12/48 (AsPC-1, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12263.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.481×** | -10.5 | 3e-23 | 38/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.484×** | -10.4 | 4e-23 | 34/46 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.548×** | -8.7 | 9e-16 | 39/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.581×** | -7.8 | 8e-13 | 33/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.667×** | -5.6 | 2e-06 | 29/47 (NCI-H23, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.762×** | -5.5 | 3e-06 | 29/48 (RKO, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.746×** | -4.2 | 0.002 | 21/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.749×** | -4.0 | 0.004 | 21/46 (AN3 CA, NCI-H1792, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.759×** | -4.0 | 0.005 | 20/48 (SW480, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.826×** | -3.9 | 0.006 | 19/48 (PANC-1, SW48, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.773×** | -3.6 | 0.019 | 19/48 (SW 900, J82, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.627×** | -3.5 | 0.020 | 14/46 (RPMI-7951, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.780×** | -3.4 | 0.031 | 13/47 (NCI-H1573, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.791×** | -3.4 | 0.031 | 20/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.809×** | -3.1 | 0.085 | 15/48 (SW48, HepG2/C3A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.811×** | -3.0 | 0.092 | 17/48 (C-33 A, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12263. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.3 | 3 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +14.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -9.5) |
| [[LoVo (line)]] | wt | 26.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[SW480 (line)]] | alt | 41.2 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -11.9) |
| [[C32 (line)]] | wt | 17.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 53.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -9.7) |
| [[PANC-1 (line)]] | alt | 26.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.401× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 30.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 42.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +9.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.206× (z -9.8) ⚠ toxic |
| [[HCT15 (line)]] | alt | 27.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[HOP62 (line)]] | alt | 16.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +11.9) | — |
| [[LOX-IMVI (line)]] | wt | 18.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +15.2) | — |
| [[NCI-H23 (line)]] | alt | 23.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +14.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.113× (z -13.1) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +13.4) | — |
| [[SNU-423 (line)]] | alt | 18.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +10.5) | — |
| [[SW1417 (line)]] | alt | 32.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -9.8) |
| [[A498 (line)]] | wt | 42.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +11.4) | — |
| [[A549 (line)]] | wt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 22.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0719× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 28.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[hTERT-HPNE (line)]] | wt | 34.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +9.1) | — |
| [[J82 (line)]] | alt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 34.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0898× (z -10.5) ⚠ toxic |
| [[SW 900 (line)]] | alt | 31.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.7) | — |
| [[A-427 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12263), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C21orf91-OT1]] | +0.79 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.74 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[HCLS1]] | +0.74 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.72 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[ADAMTSL4-AS2]] | +0.72 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[MPDU1]] | +0.72 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[CCT6B]] | +0.71 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[IDI2-AS1]] | +0.71 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[LINC01934]] | +0.71 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.71 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.70 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[USP50]] | +0.70 | +0.73 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC23A2]] | -0.63 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[SERAC1]] | -0.62 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[FAM118A]] | -0.61 | -0.62 / -0.38 | both halves | 7e-05 |  |
| [[FBXO3]] | -0.60 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[SLC9A6]] | -0.60 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[TMEM185A]] | -0.60 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02284]] | B | LINC02284 activity raises ERI2's level | lines that do not express LINC02284 (17) vs lines expressing it (33) | 1.34× lower at baseline in the lines without LINC02284 | 0.007 | ⚠ within organs, on part of the lines; also absent: PELI2, CFH, ADAM28; maybe low, not absent |
| [[DNAH17]] | B | DNAH17 activity raises ERI2's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without DNAH17 | 0.022 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[SLC2A9]] | B | SLC2A9 activity raises ERI2's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without SLC2A9 | 0.029 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ERI2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SEMA4A]] | B | SEMA4A activity raises ERI2's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.32× lower at baseline in the lines without SEMA4A | 0.073 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.731). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.7, -13.9); signed map (18.7, 7.9). **Vector** length 116, 29.8% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.7 | +13.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +15.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +8.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.6 | +6.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.9 | -10.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.4 | -10.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.0 | -8.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.0 | -5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.6 | -7.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.2 | -2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | -3.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.4 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ERI1 exoribonuclease family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:20,780,193-20,900,349 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1504, MGC16943, ZGRF5; previously EXOD1 |
| Gene groups (HGNC) | Zinc fingers GRF-type; Exonucleases |
| Matched by | ensembl_id |

UniProt [A8K979](https://www.uniprot.org/uniprotkb/A8K979) carries no function annotation.

**Summary**, from NCBI Gene [112479](https://www.ncbi.nlm.nih.gov/gene/112479):

> Predicted to enable 3'-5'-RNA exonuclease activity. Predicted to be involved in exonucleolytic trimming to generate mature 3'-end of 5.8S rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA) and negative regulation of regulatory ncRNA-mediated heterochromatin formation. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30541](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30541) · Entrez [112479](https://www.ncbi.nlm.nih.gov/gene/112479) · UniProt [A8K979](https://www.uniprot.org/uniprotkb/A8K979) · Ensembl [ENSG00000196678](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196678)

## Data

Gene col 12263: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12263); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12263, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12263]; `tensor/DDL_lfc|DDL_z.npy` [12263]; `embed/gene_vectors.npy` [12263]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12263 or target_col == 12263). Every well: [[ERI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
