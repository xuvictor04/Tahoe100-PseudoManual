---
symbol: "HSPBAP1"
type: "gene"
col: 9750
ensembl_id: "ENSG00000169087"
name: "HSPB1 associated protein 1"
location: "3q21.1"
module: 124
arm: "+"
pooled_cpm: 15.26
n_lines_expressing: 50
n_dd_up: 54
n_dd_down: 9
n_dd_up_clean: 42
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# HSPBAP1

*HSPB1 associated protein 1* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 54 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.97× (z +24.0, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.628× (z -7.3, q 2e-10, down in 25 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 0.5 µM: 0.642× (z -5.0, q 2e-04, down in 16 of 48 measured lines).
> Its strongest partners by |cos| (74 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 27 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC49A4]] (+0.67, fdr 8e-06, ⚠ same locus), [[ITPA]] (+0.64, fdr 1e-04), [[HIVEP1]] (+0.63, fdr 4e-05), [[TMEM192]] (+0.63, fdr 2e-04); moves opposite to [[RAB3A]] (-0.65, fdr 1e-04), [[MPP1]] (-0.62, fdr 1e-04), [[GNAI2]] (-0.61, fdr 4e-04).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[IGFBP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 54 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9750.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.97×** | +24.0 | 0e+00 | 41/47 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.37×** | +19.1 | 0e+00 | 37/45 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +12.6 | 4e-34 | 37/47 (J82, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +11.8 | 6e-30 | 35/42 (NCI-H2347, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +9.7 | 4e-20 | 32/46 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +9.5 | 2e-19 | 31/47 (Panc 03.27, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.87×** | +9.4 | 5e-19 | 33/46 (NCI-H2347, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +9.3 | 7e-19 | 26/48 (A-427, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.73×** | +8.6 | 7e-16 | 32/47 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.68×** | +8.1 | 4e-14 | 29/47 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +7.1 | 7e-11 | 24/47 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +6.8 | 6e-10 | 27/47 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +6.7 | 8e-10 | 21/43 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.6 | 2e-09 | 25/46 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.35×** | +6.5 | 2e-09 | 20/47 (A498, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +6.4 | 5e-09 | 24/47 (LoVo, SW480, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.45×** | +5.8 | 2e-07 | 19/47 (NCI-H2030, LOX-IMVI, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +5.7 | 4e-07 | 21/47 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +5.3 | 3e-06 | 23/47 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9750.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.628×** | -7.3 | 2e-10 | 25/47 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.642×** | -5.0 | 2e-04 | 16/48 (SW480, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.550×** | -4.9 | 2e-04 | 16/46 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.555×** | -4.8 | 2e-04 | 17/42 (A549, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.589×** | -4.4 | 0.001 | 19/46 (HEC-1-A, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.779×** | -3.7 | 0.019 | 9/47 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.801×** | -3.4 | 0.055 | 14/25 (A-427, PANC-1, …) | top dose only | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.665×** | -3.4 | 0.055 | 11/45 (A498, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | **0.803×** | -3.3 | 0.055 | 7/47 (LS 180, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[EX229 (drug)]] 0.5 µM |  | 0.759× | -3.1 | 0.11 | 6/47 (MIA PaCa-2, NCI-H23, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.821× | -3.0 | 0.14 | 9/47 (COLO 205, A498, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 13.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.41× (z +17.2) | — |
| [[A-427 (line)]] | wt | 42.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[NCI-H460 (line)]] | wt | 8.45 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +14.9) | — |
| [[A-172 (line)]] | wt | 12.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 15.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +9.1) | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0924× (z -9.2) |
| [[HOP62 (line)]] | alt | 8.90 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 8.87 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.02× (z +12.4) | — |
| [[HT-29 (line)]] | alt | 21.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[J82 (line)]] | alt | 21.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +12.1) | — |
| [[KATO III (line)]] | alt | 8.43 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +11.1) | — |
| [[LoVo (line)]] | wt | 15.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.49× (z +16.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 13.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[Panc 03.27 (line)]] | alt | 19.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 6.79 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0612× (z -10.4) |
| [[BT-474 (line)]] | alt | 7.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +9.1) | — |
| [[C32 (line)]] | wt | 17.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 4.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +12.2) | — |
| [[H4 (line)]] | wt | 7.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.02× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 9.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[PANC-1 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -9.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.134× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.204× (z -9.1) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 7.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.37× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 17.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +10.0) | — |
| [[SW480 (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +8.6) | — |
| [[A498 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 23 of them with an alert (⚠; 22 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC49A4]] | +0.67 | +0.64 / +0.58 | both halves | 8e-06 | STRING 746; ⚠ same locus (1.2 kb: neighbours can correlate without regulation) |
| [[ITPA]] | +0.64 | +0.64 / +0.36 | both halves | 1e-04 |  |
| [[HIVEP1]] | +0.63 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[TMEM192]] | +0.63 | +0.74 / +0.31 | both halves | 2e-04 |  |
| [[BICRAL]] | +0.63 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[RNF146]] | +0.62 | +0.66 / +0.28 | both halves | 3e-04 |  |
| [[KIF27]] | +0.61 | +0.67 / +0.37 | both halves | 7e-05 |  |
| [[GABPB1]] | +0.61 | +0.47 / +0.36 | both halves | 9e-05 |  |
| [[CREBRF]] | +0.61 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[TBCEL]] | +0.59 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[DNAI4]] | +0.59 | +0.61 / +0.23 | both halves | 5e-04 |  |
| [[GALNT7-DT]] | +0.58 | +0.68 / +0.11 | ⚠ one half (not replicated) | 0.002 |  |
| [[RXYLT1]] | +0.58 | +0.71 / +0.21 | both halves | 7e-04 |  |
| [[PPP1R12A-AS2]] | +0.58 | +0.60 / +0.22 | both halves | 6e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | -0.65 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[MPP1]] | -0.62 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[GNAI2]] | -0.61 | -0.63 / -0.24 | both halves | 4e-04 |  |
| [[TSPAN13]] | -0.60 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[GPI]] | -0.58 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ELP1]] | -0.58 | -0.59 / -0.22 | both halves | 6e-04 |  |
| [[MATCAP1]] | -0.58 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[YIF1B]] | -0.57 | -0.58 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[ABCB9]] | -0.56 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[PAPSS1]] | -0.56 | -0.50 / -0.22 | both halves | 6e-04 |  |
| [[SEPTIN6]] | -0.56 | -0.50 / -0.24 | both halves | 5e-04 |  |
| [[GNAI3]] | -0.56 | -0.65 / -0.22 | both halves | 6e-04 |  |
| [[ANKMY2]] | -0.55 | -0.52 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGFBP3]] | B | IGFBP3 activity lowers HSPBAP1's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 1.23× higher at baseline in the lines without IGFBP3 | 0.088 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[TOP2A]] | B | TOP2A activity lowers HSPBAP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.5% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MTOR]] | B | MTOR activity lowers HSPBAP1's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 9.5% of all compounds | 0.095 | ⚠ off-target possible; 5 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.673). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (6.5, -6.7); signed map (22.9, -19.2). **Vector** length 97.9, 23.0% of its response variance represented; |z| ≥ 3 in 1,124 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +24.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +11.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +12.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +9.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.1 | +8.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +5.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.5 | +5.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +5.8 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +3.0 | +3.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.6 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.1 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -7.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -4.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -4.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.3 | -5.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.9 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | HSPB1 associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1 — chr3:122,739,999-122,793,831 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22623, PASS1 |
| Gene groups (HGNC) | Iron (II) and 2-oxoglutarate dependent oxygenases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EW2](https://www.uniprot.org/uniprotkb/Q96EW2) (HSPB1-associated protein 1):

> May play a role in cellular stress response.

**Summary**, from NCBI Gene [79663](https://www.ncbi.nlm.nih.gov/gene/79663):

> This gene encodes a protein that binds to one of the small heat shock proteins, specifically hsp27. Hsp27 is involved with cell growth and differentiation. This encoded protein was found to be abnormally expressed in patients with intractable epilepsy, although how brain function is affected remains unknown. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:16389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16389) · Entrez [79663](https://www.ncbi.nlm.nih.gov/gene/79663) · UniProt [Q96EW2](https://www.uniprot.org/uniprotkb/Q96EW2) · Ensembl [ENSG00000169087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169087)

## Data

Gene col 9750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9750); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9750]; `tensor/DDL_lfc|DDL_z.npy` [9750]; `embed/gene_vectors.npy` [9750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9750 or target_col == 9750). Every well: [[HSPBAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPBAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
