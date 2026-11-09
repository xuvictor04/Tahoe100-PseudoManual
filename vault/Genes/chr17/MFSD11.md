---
symbol: "MFSD11"
type: "gene"
col: 1713
ensembl_id: "ENSG00000092931"
name: "major facilitator superfamily domain containing 11"
location: "17q25.1"
module: 18
arm: "-"
pooled_cpm: 39.25
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MFSD11

*major facilitator superfamily domain containing 11* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.06× (z +20.7, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.426× (z -9.1, q 4e-17, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPT1-AS1]] (+0.57, fdr 5e-05), [[PHKG1]] (+0.52, fdr 3e-05), [[TRNAU1AP]] (+0.51, fdr 2e-05); moves opposite to [[MRPL3]] (-0.60, fdr 1e-05), [[ZFP62]] (-0.58, fdr 1e-05), [[ALDH5A1]] (-0.58, fdr 5e-05).
> It sits in the **-** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1713.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +20.7 | 0e+00 | 45/48 (HOP62, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +12.7 | 1e-34 | 41/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +12.4 | 4e-33 | 39/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +11.9 | 2e-30 | 41/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +9.9 | 3e-21 | 29/47 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +8.8 | 1e-16 | 33/48 (A-427, HT-29, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.44×** | +7.3 | 2e-11 | 36/48 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.4 | 1e-08 | 27/47 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +6.1 | 7e-08 | 28/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +4.5 | 4e-04 | 20/47 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.3 | 9e-04 | 20/48 (Panc 03.27, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.23×** | +4.2 | 0.001 | 22/47 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.008 | 18/48 (HOP62, SW1417, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.016 | 13/48 (NCI-H460, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.029 | 16/48 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1713.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.426×** | -9.1 | 4e-17 | 37/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.500×** | -7.4 | 4e-11 | 32/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.737×** | -6.3 | 6e-08 | 28/48 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.738×** | -6.0 | 3e-07 | 24/47 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.788×** | -4.9 | 1e-04 | 22/48 (SW480, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.799×** | -4.6 | 4e-04 | 20/48 (PANC-1, NCI-H23, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.809×** | -4.4 | 0.001 | 21/46 (HCT15, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Dexamethasone (drug)]] 5 µM |  | 0.838× | -3.6 | 0.020 | 18/48 (HOP62, COLO 205, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.890× | -3.4 | 0.041 | 15/48 (NCI-H1573, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.850× | -3.3 | 0.046 | 16/48 (KATO III, PANC-1, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -3.2 | 0.066 | 17/48 (Panc 03.27, NCI-H661, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.860× | -3.1 | 0.080 | 9/48 (NCI-H2347, SW 1088, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.861× | -3.1 | 0.080 | 12/48 (H4, HOP62, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.861× | -3.1 | 0.080 | 13/48 (C-33 A, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 53.0 | 7 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +24.0) | [[TAK-901 (drug)]] 5 µM 0.296× (z -8.8) |
| [[SW480 (line)]] | alt | 84.8 | 4 | 3 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.36× (z +11.2) | [[PH-797804 (drug)]] 5 µM 0.218× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 29.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +14.7) | — |
| [[J82 (line)]] | alt | 26.4 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +12.3) | — |
| [[RKO (line)]] | wt | 20.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.51× (z +11.1) | — |
| [[A-427 (line)]] | wt | 53.2 | 2 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.69× (z +10.2) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 58.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[SNU-423 (line)]] | alt | 52.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 25.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +14.0) | — |
| [[COLO 205 (line)]] | alt | 41.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 93.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0510× (z -25.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[HOP62 (line)]] | alt | 44.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +15.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 31.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +13.2) | [[Homoharringtonine (drug)]] 0.05 µM 0.309× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 36.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +13.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.356× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 48.9 | 0 | 2 (1 ⚠) | — | [[Verapamil (drug)]] 0.5 µM 0.0578× (z -10.2) |
| [[A-172 (line)]] | wt | 37.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.4) | — |
| [[BT-474 (line)]] | alt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 24.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +11.6) | — |
| [[HCT15 (line)]] | alt | 70.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[Hs 766T (line)]] | wt | 22.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 24.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 42.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.6) | — |
| [[KATO III (line)]] | alt | 55.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[LoVo (line)]] | wt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[NCI-H1573 (line)]] | alt | 24.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.9) | — |
| [[NCI-H661 (line)]] | alt | 30.2 | 0 | 1 | — | [[5-Fluorouracil (drug)]] 0.5 µM 0.0617× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 52.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.139× (z -9.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 34.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +12.2) | — |
| [[A498 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPT1-AS1]] | +0.57 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[PHKG1]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[TRNAU1AP]] | +0.51 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[TTLL3]] | +0.51 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[HERC4]] | +0.51 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[MICU1]] | +0.51 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[MAFG]] | +0.50 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[RAB4B]] | +0.50 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[AHCYL1]] | +0.50 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[RNASEK]] | +0.50 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[TMEM91]] | +0.50 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[GLA]] | +0.50 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL3]] | -0.60 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[ZFP62]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[ALDH5A1]] | -0.58 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[PYURF]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[FAM98B]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[SAAL1]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[TRIM32]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SPATA20]] | -0.54 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[SDHAF3]] | -0.53 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[ZNF239]] | -0.53 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[SCAP]] | -0.53 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[AMER1]] | -0.53 | -0.52 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MFSD11's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **-** arm (projection on the module's main direction -0.331). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-19.6, -2.0); signed map (5.1, 7.2). **Vector** length 93.0, 21.6% of its response variance represented; |z| ≥ 3 in 1,176 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.9 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +9.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +3.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.4 | +3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +7.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.0 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.2 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | +1.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change | -4.8 | -2.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | -4.2 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -7.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | major facilitator superfamily domain containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,735,865-76,781,449 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22196, FLJ20226 |
| Gene groups (HGNC) | Unc-93 related family |
| Matched by | ensembl_id |

UniProt [O43934](https://www.uniprot.org/uniprotkb/O43934) carries no function annotation.

**Summary**, from NCBI Gene [79157](https://www.ncbi.nlm.nih.gov/gene/79157):

> Predicted to act upstream of or within response to food and response to starvation. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25458](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25458) · Entrez [79157](https://www.ncbi.nlm.nih.gov/gene/79157) · UniProt [O43934](https://www.uniprot.org/uniprotkb/O43934) · Ensembl [ENSG00000092931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092931)

## Data

Gene col 1713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1713); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1713]; `tensor/DDL_lfc|DDL_z.npy` [1713]; `embed/gene_vectors.npy` [1713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1713 or target_col == 1713). Every well: [[MFSD11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
