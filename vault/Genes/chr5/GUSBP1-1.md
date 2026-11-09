---
symbol: "GUSBP1-1"
type: "gene"
col: 16583
ensembl_id: "ENSG00000291102"
name: ""
location: ""
module: 54
arm: "+"
pooled_cpm: 59.72
n_lines_expressing: 47
n_dd_up: 7
n_dd_down: 28
n_dd_up_clean: 7
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# GUSBP1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.16× (z +11.1, q 1e-25, up in 37 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.383× (z -13.7, q 5e-40, down in 39 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.417× (z -12.5, q 2e-33, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GUSBP1]] (+0.50, fdr 7e-05, ⚠ same locus), [[BBS9]] (+0.49, fdr 4e-05), [[WDR70]] (+0.49, fdr 5e-05), [[ACAD10]] (+0.47, fdr 4e-05); moves opposite to [[ELF4]] (-0.48, fdr 4e-05), [[ACSS1]] (-0.47, fdr 3e-04), [[SEPTIN11]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16583.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.16×** | +11.1 | 1e-25 | 37/45 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +10.0 | 4e-21 | 37/45 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +6.5 | 1e-08 | 26/45 (AsPC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +5.0 | 7e-05 | 28/45 (J82, CFPAC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.007 | 20/44 (SW480, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.022 | 22/45 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.022 | 23/44 (SW480, NCI-H23, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.25× | +3.2 | 0.10 | 10/45 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16583.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.383×** | -13.7 | 5e-40 | 39/45 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.417×** | -12.5 | 2e-33 | 37/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.268×** | -9.9 | 1e-20 | 43/46 (NCI-H460, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.519×** | -9.4 | 1e-18 | 35/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.664×** | -8.3 | 2e-14 | 25/44 (CFPAC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.553×** | -8.2 | 3e-14 | 31/45 (NCI-H1792, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.566×** | -8.1 | 4e-14 | 30/46 (NCI-H1792, NCI-H23, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.567×** | -8.1 | 4e-14 | 35/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.579×** | -7.5 | 4e-12 | 31/44 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.607×** | -6.9 | 4e-10 | 29/44 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.401×** | -6.8 | 4e-10 | 27/45 (RPMI-7951, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.642×** | -6.3 | 1e-08 | 25/44 (NCI-H460, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.626×** | -6.2 | 3e-08 | 26/42 (A-427, HCT15, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.673×** | -5.7 | 6e-07 | 27/45 (CFPAC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.676×** | -5.6 | 9e-07 | 28/45 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.677×** | -5.6 | 1e-06 | 26/45 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.819×** | -4.0 | 0.002 | 18/46 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.821×** | -4.0 | 0.002 | 22/45 (NCI-H2347, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.765×** | -3.8 | 0.004 | 22/45 (BT-474, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.773×** | -3.7 | 0.006 | 21/45 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.797×** | -3.1 | 0.044 | 18/45 (HT-29, PANC-1, …) | top dose only | plate-row cell shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.809×** | -3.0 | 0.057 | 16/44 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | 0.865× | -2.9 | 0.080 | 13/46 (NCI-H1792, SHP-77, …) | top dose only |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -2.9 | 0.084 | 15/45 (HOP62, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 83.4 | 0 | 16 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -18.2) |
| [[NCI-H23 (line)]] | alt | 157 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.371× (z -10.6) |
| [[SW480 (line)]] | alt | 70.8 | 2 | 9 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.63× (z +11.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -16.8) |
| [[HOP62 (line)]] | alt | 64.6 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 126 | 0 | 7 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.123× (z -18.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.366× (z -9.1) |
| [[PANC-1 (line)]] | alt | 28.0 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -14.9) |
| [[SW 900 (line)]] | alt | 136 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -16.7) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -12.5) |
| [[A549 (line)]] | wt | 34.3 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -13.1) ⚠ cell-cycle shift, explains ~73% of this change |
| [[C32 (line)]] | wt | 77.1 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.172× (z -11.7) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 59.6 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.217× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.254× (z -12.1) |
| [[A498 (line)]] | wt | 35.5 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.13× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.4) ⚠ cell-cycle shift, explains ~73% of this change |
| [[J82 (line)]] | alt | 83.7 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.274× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.379× (z -8.5) |
| [[A-172 (line)]] | wt | 27.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.65× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.0) ⚠ cell-cycle shift, explains ~73% of this change |
| [[CFPAC-1 (line)]] | alt | 117 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -17.9) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.372× (z -8.6) |
| [[HT-29 (line)]] | alt | 48.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.306× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.118× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 46.0 | 0 | 3 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0161× (z -13.9) |
| [[SNU-423 (line)]] | alt | 62.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -14.9) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -10.2) |
| [[A-427 (line)]] | wt | 87.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 17.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.03× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 71.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[H4 (line)]] | wt | 44.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -13.3) ⚠ toxic |
| [[HCT15 (line)]] | alt | 60.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0795× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 73.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.56× (z +9.2) | [[Lonafarnib (drug)]] 5 µM 0.167× (z -9.3) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 43.9 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.313× (z -8.7) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 64.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.320× (z -8.7) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SHP-77 (line)]] | alt | 158 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[AN3 CA (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.123× (z -8.8) ⚠ transcription drop |
| [[BT-474 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[LOX-IMVI (line)]] | wt | 42.4 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0811× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 41.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 107 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -13.5) |
| [[SNU-1 (line)]] | wt | 63.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.260× (z -9.9) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 83.9 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0668× (z -11.1) ⚠ cell-cycle shift, explains ~21% of this change |
| [[CHP-212 (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 59.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 17 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUSBP1]] | +0.50 | +0.43 / +0.38 | both halves | 7e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[BBS9]] | +0.49 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[WDR70]] | +0.49 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[ACAD10]] | +0.47 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[DNAAF11]] | +0.46 | +0.47 / +0.36 | both halves | 9e-05 |  |
| [[NBEA]] | +0.46 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[C1QTNF3-AMACR]] | +0.46 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[CWF19L2]] | +0.45 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[ADAMTS9-AS2]] | +0.44 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[POU5F2]] | +0.44 | +0.34 / +0.35 | both halves | 1e-04 |  |
| [[CDRT4]] | +0.44 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[PRH1]] | +0.44 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ZNF559-ZNF177]] | +0.44 | +0.41 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELF4]] | -0.48 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ACSS1]] | -0.47 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[SEPTIN11]] | -0.45 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[SEPTIN8]] | -0.44 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[PRSS12]] | -0.44 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[GFRA1]] | -0.43 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[NECTIN1]] | -0.43 | -0.51 / -0.37 | both halves | 9e-05 |  |
| [[PTP4A3]] | -0.42 | -0.29 / -0.36 | both halves | 3e-04 |  |
| [[AMZ2P1]] | -0.42 | -0.22 / -0.44 | both halves | 6e-04 |  |
| [[OXCT1]] | -0.41 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[OGFRL1]] | -0.41 | -0.10 / -0.45 | ⚠ not reproduced | 0.003 |  |
| [[PANX1]] | -0.41 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[STK26]] | -0.41 | -0.27 / -0.34 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers GUSBP1-1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.320). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-22.3, 30.4); signed map (-20.4, 3.1). **Vector** length 80.1, 21.3% of its response variance represented; |z| ≥ 3 in 1,157 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.8 | +1.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +11.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +10.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.4 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.8 | -6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -2.8 | -8.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.2 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.7 | -0.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -6.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +2.0 |

## What is on record

> [!warning] No registry record
> GUSBP1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16583); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16583]; `tensor/DDL_lfc|DDL_z.npy` [16583]; `embed/gene_vectors.npy` [16583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16583 or target_col == 16583). Every well: [[GUSBP1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUSBP1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
