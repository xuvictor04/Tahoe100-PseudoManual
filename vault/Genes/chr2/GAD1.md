---
symbol: "GAD1"
type: "gene"
col: 4912
ensembl_id: "ENSG00000128683"
name: "glutamate decarboxylase 1"
location: "2q31.1"
module: 4
arm: "-"
pooled_cpm: 21.38
n_lines_expressing: 37
n_dd_up: 19
n_dd_down: 21
n_dd_up_clean: 17
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# GAD1

*glutamate decarboxylase 1* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +15.2, q 0e+00, up in 27 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.502× (z -9.9, q 2e-20, down in 20 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.638× (z -6.5, q 1e-08, down in 18 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP23]] (+0.63, fdr 7e-06), [[ZBTB25]] (+0.61, fdr 1e-05), [[INTS6L]] (+0.60, fdr 1e-05); moves opposite to [[PSMD1]] (-0.61, fdr 1e-05), [[USP14]] (-0.58, fdr 3e-05), [[RSU1]] (-0.57, fdr 5e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOXB-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4912.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +15.2 | 0e+00 | 27/35 (NCI-H2030, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +13.6 | 8e-40 | 19/33 (CFPAC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +9.5 | 6e-19 | 20/34 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +7.2 | 1e-10 | 22/34 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +6.8 | 1e-09 | 19/34 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +6.6 | 3e-09 | 16/34 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.6 | 3e-04 | 13/34 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +4.5 | 5e-04 | 13/33 (SW1417, H4, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.3 | 0.001 | 12/34 (SW 900, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.004 | 7/34 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.006 | 13/34 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.008 | 8/33 (SW1417, C32, …) | top dose only | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.009 | 5/34 (A498, C-33 A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.015 | 13/32 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.023 | 9/35 (A498, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Terfenadine (drug)]] 5 µM |  | 1.18× | +3.3 | 0.029 | 8/34 (A498, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4912.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.502×** | -9.9 | 2e-20 | 20/27 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -8.2 | 9e-14 | 16/18 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.603×** | -6.7 | 3e-09 | 16/23 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.638×** | -6.5 | 1e-08 | 18/34 (A498, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.666×** | -5.8 | 6e-07 | 20/34 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.688×** | -5.2 | 2e-05 | 18/34 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.812×** | -4.2 | 0.002 | 13/35 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.733×** | -4.1 | 0.003 | 12/34 (A498, J82, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.742×** | -3.9 | 0.006 | 13/35 (A498, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.743×** | -3.9 | 0.006 | 9/35 (A-172, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.783×** | -3.5 | 0.022 | 8/34 (A-172, PANC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **0.778×** | -3.5 | 0.024 | 12/30 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.774×** | -3.3 | 0.033 | 9/34 (PANC-1, SNU-423, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.793×** | -3.3 | 0.033 | 16/34 (SW480, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.794×** | -3.3 | 0.033 | 11/34 (A498, SW48, …) | two highest doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.776×** | -3.3 | 0.033 | 5/34 (A-172, A498, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.779×** | -3.3 | 0.037 | 7/34 (A-172, A498, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.783×** | -3.2 | 0.041 | 11/34 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | 0.856× | -3.1 | 0.046 | 6/34 (A498, J82, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.857× | -3.1 | 0.047 | 13/35 (SNU-423, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4912. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 110 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.244× (z -12.6) |
| [[SW480 (line)]] | alt | 62.0 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.297× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 35.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.114× (z -15.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 35.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.0843× (z -16.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 24.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -8.5) ⚠ cell-cycle shift, explains ~11% of this change |
| [[NCI-H1573 (line)]] | alt | 13.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 13.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.147× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 23.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +9.5) | — |
| [[A549 (line)]] | wt | 6.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.67× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 14.3 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0650× (z -10.3) |
| [[C32 (line)]] | wt | 44.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.8) | — |
| [[H4 (line)]] | wt | 9.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 38.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.8) | — |
| [[A-427 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.92 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4912), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP23]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ZBTB25]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[INTS6L]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ZNF821]] | +0.60 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[HMGCL]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ABCA5]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[POLR1H]] | +0.57 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[NEURL3]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[STAP2]] | +0.56 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[MITD1]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SLC11A2]] | +0.54 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[GLIS2]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD1]] | -0.61 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[USP14]] | -0.58 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[RSU1]] | -0.57 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[LAS1L]] | -0.55 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[RPRD1A]] | -0.55 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[HERC2]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SNX19]] | -0.53 | -0.34 / -0.61 | both halves | 1e-04 |  |
| [[CAPZB]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[GNB1]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 | pathway: Neuronal System |
| [[LINC00205]] | -0.52 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[KPNA4]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[MICAL2]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB-AS1]] | B | HOXB-AS1 activity raises GAD1's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 1.83× lower at baseline in the lines without HOXB-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.506). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (3.2, -30.2); signed map (-3.9, 4.4). **Vector** length 84.4, 20.0% of its response variance represented; |z| ≥ 3 in 757 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +15.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +13.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +6.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +3.8 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -3.2 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.1 | -5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -5.2 |
|  | [[Megestrol (drug)]] 0.05 µM |  | -2.5 | -3.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.3 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | glutamate decarboxylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:170,813,213-170,861,151 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GAD |
| Gene groups (HGNC) | Decarboxylases |
| Hallmark sets | SPERMATOGENESIS, XENOBIOTIC_METABOLISM |
| Reactome | 5 pathways, smallest: GABA synthesis, release, reuptake and degradation; Neurotransmitter release cycle; Transcriptional Regulation by MECP2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99259](https://www.uniprot.org/uniprotkb/Q99259) (Glutamate decarboxylase 1):

> Catalyzes the synthesis of the inhibitory neurotransmitter gamma-aminobutyric acid (GABA) with pyridoxal 5'-phosphate as cofactor.; [Isoform 3]: Enzymatically inactive as glutamate decarboxylase.

**Summary**, from NCBI Gene [2571](https://www.ncbi.nlm.nih.gov/gene/2571):

> This gene encodes one of several forms of glutamic acid decarboxylase, identified as a major autoantigen in insulin-dependent diabetes. The enzyme encoded is responsible for catalyzing the production of gamma-aminobutyric acid from L-glutamic acid. A pathogenic role for this enzyme has been identified in the human pancreas since it has been identified as an autoantigen and an autoreactive T cell target in insulin-dependent diabetes. This gene may also play a role in the stiff man syndrome. …

**Accessions** — [HGNC:4092](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4092) · Entrez [2571](https://www.ncbi.nlm.nih.gov/gene/2571) · UniProt [Q99259](https://www.uniprot.org/uniprotkb/Q99259) · Ensembl [ENSG00000128683](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128683)

## Data

Gene col 4912: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4912); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4912, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4912]; `tensor/DDL_lfc|DDL_z.npy` [4912]; `embed/gene_vectors.npy` [4912]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4912 or target_col == 4912). Every well: [[GAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
