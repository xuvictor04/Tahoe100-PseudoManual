---
symbol: "TTC23"
type: "gene"
col: 2397
ensembl_id: "ENSG00000103852"
name: "tetratricopeptide repeat domain 23"
location: "15q26.3"
module: 17
arm: "+"
pooled_cpm: 27.53
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TTC23

*tetratricopeptide repeat domain 23* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.63× (z +9.9, q 3e-20, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.630× (z -13.1, q 2e-36, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POT1]] (+0.62, fdr 1e-04), [[NPHP1]] (+0.59, fdr 4e-05), [[INTU]] (+0.59, fdr 1e-05); moves opposite to [[C2orf88]] (-0.51, fdr 9e-04, ⚠ not reproduced), [[KLHL21]] (-0.50, fdr 6e-05), [[WNT9A]] (-0.50, fdr 6e-05), [[CCNT2-AS1]] (-0.49, fdr 7e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2397.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +9.9 | 3e-20 | 35/46 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +8.6 | 3e-15 | 32/46 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +8.0 | 2e-13 | 28/46 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +5.9 | 6e-07 | 24/46 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +5.8 | 8e-07 | 25/46 (A-172, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +5.7 | 1e-06 | 24/46 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.9 | 7e-05 | 20/44 (A549, C-33 A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +4.5 | 4e-04 | 16/44 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.21×** | +3.8 | 0.007 | 9/45 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.038 | 13/45 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.18× | +3.3 | 0.047 | 7/46 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.1 | 0.100 | 8/46 (HOP62, LS 180, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.17× | +3.0 | 0.11 | 7/46 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2397.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -13.1 | 2e-36 | 35/46 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.557×** | -11.7 | 3e-29 | 33/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -11.0 | 6e-26 | 35/44 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.629×** | -9.3 | 2e-18 | 31/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.641×** | -8.9 | 7e-17 | 33/46 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.707×** | -6.9 | 4e-10 | 27/43 (SW1417, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.698×** | -6.9 | 4e-10 | 25/44 (AN3 CA, COLO 205, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.729×** | -6.3 | 2e-08 | 26/45 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.742×** | -5.5 | 2e-06 | 23/38 (C32, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.770×** | -5.2 | 1e-05 | 21/46 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.850× | -4.6 | 2e-04 | 21/46 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.795×** | -4.6 | 2e-04 | 18/45 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.797×** | -4.5 | 3e-04 | 16/45 (MIA PaCa-2, CFPAC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.800×** | -4.4 | 4e-04 | 21/46 (A549, NCI-H23, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.807×** | -4.3 | 7e-04 | 16/46 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.684×** | -4.0 | 0.002 | 16/45 (SW480, C32, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.823×** | -3.9 | 0.003 | 16/44 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.812×** | -3.8 | 0.003 | 13/44 (MIA PaCa-2, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.878× | -3.7 | 0.006 | 14/46 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.833×** | -3.6 | 0.007 | 19/46 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.793×** | -3.3 | 0.020 | 12/45 (H4, SNU-423, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.845× | -3.2 | 0.027 | 9/45 (NCI-H460, H4, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 45.8 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 28.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -12.5) |
| [[PANC-1 (line)]] | alt | 35.6 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.278× (z -14.8) |
| [[SW480 (line)]] | alt | 30.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.242× (z -15.7) |
| [[A-172 (line)]] | wt | 24.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -8.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 40.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 38.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -9.0) |
| [[SNU-423 (line)]] | alt | 28.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0343× (z -26.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change |
| [[SW 900 (line)]] | alt | 26.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.195× (z -11.4) |
| [[LoVo (line)]] | wt | 28.7 | 1 | 1 | [[Belinostat (drug)]] 5 µM 2.66× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 0 | 2 | — | [[Harringtonine (drug)]] 0.05 µM 0.188× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 24.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -10.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 52.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0966× (z -11.1) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 42.7 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.115× (z -9.0) |
| [[COLO 205 (line)]] | alt | 43.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.273× (z -8.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.119× (z -9.4) ⚠ toxic |
| [[J82 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 26.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 24.0 | 0 | 1 | — | [[Pralsetinib (drug)]] 5 µM 0.0777× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 20.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -12.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 48.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0745× (z -14.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 19.0 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0870× (z -9.2) |
| [[A498 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.79 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POT1]] | +0.62 | +0.33 / +0.71 | both halves | 1e-04 |  |
| [[NPHP1]] | +0.59 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[INTU]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[LCLAT1]] | +0.56 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[RFC1]] | +0.56 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[TRAPPC11]] | +0.55 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[NUDT12]] | +0.55 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[GPATCH11]] | +0.55 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[SLX4IP]] | +0.55 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[ZNF45]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[THYN1]] | +0.54 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[INIP]] | +0.54 | +0.46 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2orf88]] | -0.51 | -0.18 / -0.41 | ⚠ not reproduced | 9e-04 |  |
| [[KLHL21]] | -0.50 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[WNT9A]] | -0.50 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[UPP2]] | -0.49 | -0.14 / -0.44 | ⚠ not reproduced | 0.002 |  |
| [[CCNT2-AS1]] | -0.49 | -0.20 / -0.45 | both halves | 7e-04 |  |
| [[ACVR1C]] | -0.49 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[CCDC168]] | -0.49 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[SPON1-AS1]] | -0.48 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[CDR2]] | -0.48 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[NINL]] | -0.48 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[LINC01579]] | -0.47 | -0.17 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[RBPMS2]] | -0.47 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[LARGE1]] | -0.47 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[SWT1]] | -0.47 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[TPTE2]] | -0.46 | -0.35 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TTC23's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.1, 0.2); signed map (-20.8, -19.1). **Vector** length 73.8, 13.8% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.7 | +8.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +1.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -0.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.3 | +0.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.1 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +5.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -13.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -3.8 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:99,136,323-99,251,223 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12572, HCC-8 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5W5X9](https://www.uniprot.org/uniprotkb/Q5W5X9) (Tetratricopeptide repeat protein 23):

> Participates positively in the ciliary Hedgehog (Hh) signaling.

**Summary**, from NCBI Gene [64927](https://www.ncbi.nlm.nih.gov/gene/64927):

> Predicted to be involved in positive regulation of smoothened signaling pathway. Predicted to be located in cilium. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25730](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25730) · Entrez [64927](https://www.ncbi.nlm.nih.gov/gene/64927) · UniProt [Q5W5X9](https://www.uniprot.org/uniprotkb/Q5W5X9) · Ensembl [ENSG00000103852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103852)

## Data

Gene col 2397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2397); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2397]; `tensor/DDL_lfc|DDL_z.npy` [2397]; `embed/gene_vectors.npy` [2397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2397 or target_col == 2397). Every well: [[TTC23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
