---
symbol: "NXF1"
type: "gene"
col: 8492
ensembl_id: "ENSG00000162231"
name: "nuclear RNA export factor 1"
location: "11q12.3"
module: 93
arm: "+"
pooled_cpm: 33.07
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# NXF1

*nuclear RNA export factor 1* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.94× (z +18.4, q 0e+00, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HCT15 0.114×, KATO III 0.184×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2A]] (+0.70, fdr 7e-06), [[LINC02936]] (+0.64, fdr 1e-05), [[EMC1-AS1]] (+0.64, fdr 1e-05); moves opposite to [[ZNF45]] (-0.55, fdr 4e-05), [[ESD]] (-0.54, fdr 3e-05), [[VTA1]] (-0.53, fdr 3e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8492.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.94×** | +18.4 | 0e+00 | 47/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.71×** | +17.9 | 0e+00 | 46/47 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **4.05×** | +11.4 | 6e-28 | 48/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.53×** | +10.3 | 1e-22 | 45/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.52×** | +10.3 | 1e-22 | 48/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.59×** | +10.0 | 1e-21 | 44/47 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.93×** | +8.4 | 3e-15 | 44/48 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.74×** | +7.9 | 2e-13 | 44/48 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.36×** | +7.0 | 2e-10 | 45/48 (SW480, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.79×** | +6.7 | 9e-10 | 39/48 (HOP62, A-172, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.24×** | +6.6 | 2e-09 | 38/48 (LoVo, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +6.2 | 2e-08 | 39/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.45×** | +6.0 | 1e-07 | 45/48 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +5.8 | 3e-07 | 35/46 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.00×** | +5.7 | 5e-07 | 42/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.24×** | +5.0 | 2e-05 | 41/49 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.09×** | +4.9 | 3e-05 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.00×** | +4.7 | 9e-05 | 32/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.97×** | +4.5 | 2e-04 | 35/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8492.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HCT15 0.114×, KATO III 0.184×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 0.05 µM |  | 0.669× | -3.3 | 0.53 | 27/48 (NCI-H2030, CFPAC-1, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.687× | -3.1 | 0.53 | 24/48 (AN3 CA, NCI-H2347, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8492. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.7 | 13 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.89× (z +17.2) | — |
| [[SW480 (line)]] | alt | 31.5 | 11 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +16.3) | — |
| [[KATO III (line)]] | alt | 25.1 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 13.0× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 34.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +16.1) | — |
| [[HOP62 (line)]] | alt | 26.3 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +15.9) | — |
| [[HS-578T (line)]] | alt | 29.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.74× (z +15.6) | — |
| [[LS 180 (line)]] | wt | 19.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 22.1 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.61× (z +17.7) | — |
| [[A498 (line)]] | wt | 21.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +18.0) | — |
| [[AsPC-1 (line)]] | alt | 34.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +19.7) | — |
| [[hTERT-HPNE (line)]] | wt | 32.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +13.0) | — |
| [[LOX-IMVI (line)]] | wt | 38.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +15.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.67× (z +16.4) | — |
| [[NCI-H1792 (line)]] | alt | 26.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +19.1) | — |
| [[SNU-423 (line)]] | alt | 33.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +15.2) | — |
| [[A-172 (line)]] | wt | 18.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +12.8) | — |
| [[A549 (line)]] | wt | 23.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 27.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.12× (z +14.9) | — |
| [[C32 (line)]] | wt | 39.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +15.4) | — |
| [[COLO 205 (line)]] | alt | 23.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 22.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.20× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 34.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.94× (z +14.5) | — |
| [[RKO (line)]] | wt | 41.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 36.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +12.7) | — |
| [[SW 900 (line)]] | alt | 37.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +13.2) | — |
| [[SW1417 (line)]] | alt | 61.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +13.1) | — |
| [[SW48 (line)]] | wt | 28.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.36× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 35.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 54.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +12.1) | — |
| [[H4 (line)]] | wt | 25.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +10.7) | — |
| [[HCT15 (line)]] | alt | 53.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 25.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +14.9) | — |
| [[HT-29 (line)]] | alt | 41.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.50× (z +13.5) | — |
| [[J82 (line)]] | alt | 38.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.26× (z +13.4) | — |
| [[NCI-H2030 (line)]] | alt | 67.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.73× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 24.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 55.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +15.8) | — |
| [[Panc 03.27 (line)]] | alt | 44.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.40× (z +14.4) | — |
| [[RPMI-7951 (line)]] | alt | 41.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 19.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +13.2) | — |
| [[A-427 (line)]] | wt | 40.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.06× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 31.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8492), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2A]] | +0.70 | +0.64 / +0.60 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[LINC02936]] | +0.64 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[EMC1-AS1]] | +0.64 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CSRNP2]] | +0.63 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[ATXN1L]] | +0.63 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[CCDC17]] | +0.61 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[CD27-AS1]] | +0.61 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[PIPOX]] | +0.60 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[LINC00910]] | +0.60 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[TRPV1]] | +0.60 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[LINC00880]] | +0.59 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[LSMEM1]] | +0.59 | +0.61 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF45]] | -0.55 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[ESD]] | -0.54 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[VTA1]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[NDUFB6]] | -0.52 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[SNRPD1]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[COA1]] | -0.51 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[METTL5]] | -0.51 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[MICU2]] | -0.50 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[COG2]] | -0.50 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[ZNF567]] | -0.50 | -0.44 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NXF1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.4, -25.1); signed map (3.4, 14.8). **Vector** length 85.5, 28.7% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +18.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +8.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.9 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +6.6 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[Uridine (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.1 | +2.3 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.1 | +7.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.9 | +0.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.7 | +5.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.5 | -3.3 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -2.3 | -2.6 |
|  | [[Riluzole hydrochloride (drug)]] 0.05 µM |  | -2.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | nuclear RNA export factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,792,123-62,806,302 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAP, Mex67, DKFZp667O0311 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 8 pathways, smallest: Transport of the SLBP independent Mature mRNA; Transport of the SLBP Dependant Mature mRNA; Transport of Mature mRNA Derived from an Intronless Transcript |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBU9](https://www.uniprot.org/uniprotkb/Q9UBU9) (Nuclear RNA export factor 1):

> Involved in the nuclear export of mRNA species bearing retroviral constitutive transport elements (CTE) and in the export of mRNA from the nucleus to the cytoplasm (TAP/NFX1 pathway). The NXF1-NXT1 heterodimer is involved in the export of HSP70 mRNA in conjunction with ALYREF/THOC4 and THOC5 components of the TREX complex. ALYREF/THOC4-bound mRNA is thought to be transferred to the NXF1-NXT1 heterodimer for export. Also involved in nuclear export of m6A-containing mRNAs: interaction between …

**Summary**, from NCBI Gene [10482](https://www.ncbi.nlm.nih.gov/gene/10482):

> This gene is one member of a family of nuclear RNA export factor genes. Common domain features of this family are a noncanonical RNP-type RNA-binding domain (RBD), 4 leucine-rich repeats (LRRs), a nuclear transport factor 2 (NTF2)-like domain that allows heterodimerization with NTF2-related export protein-1 (NXT1), and a ubiquitin-associated domain that mediates interactions with nucleoporins. The LRRs and NTF2-like domains are required for export activity. Alternative splicing seems to be a …

**Accessions** — [HGNC:8071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8071) · Entrez [10482](https://www.ncbi.nlm.nih.gov/gene/10482) · UniProt [Q9UBU9](https://www.uniprot.org/uniprotkb/Q9UBU9) · Ensembl [ENSG00000162231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162231)

## Data

Gene col 8492: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8492); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8492, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8492]; `tensor/DDL_lfc|DDL_z.npy` [8492]; `embed/gene_vectors.npy` [8492]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8492 or target_col == 8492). Every well: [[NXF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NXF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
