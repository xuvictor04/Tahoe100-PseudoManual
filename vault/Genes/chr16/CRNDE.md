---
symbol: "CRNDE"
type: "gene"
col: 14441
ensembl_id: "ENSG00000245694"
name: "colorectal neoplasia differentially expressed"
location: "16q12.2"
module: 12
arm: "-"
pooled_cpm: 26.85
n_lines_expressing: 47
n_dd_up: 23
n_dd_down: 11
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CRNDE

*colorectal neoplasia differentially expressed* — 16q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.79× (z +25.3, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.612× (z -8.6, q 4e-15, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMTOR5-AS1]] (+0.54, fdr 2e-05), [[SNHG10]] (+0.53, fdr 1e-05), [[SLC16A4-AS1]] (+0.53, fdr 6e-05); moves opposite to [[ALAS1]] (-0.58, fdr 6e-05), [[MRPS18A]] (-0.57, fdr 1e-05), [[POP4]] (-0.56, fdr 4e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MRPS18A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +25.3 | 0e+00 | 43/45 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +11.9 | 6e-30 | 34/40 (NCI-H460, C32, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +8.4 | 9e-15 | 28/43 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +8.4 | 9e-15 | 28/37 (PANC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +8.1 | 6e-14 | 33/44 (C-33 A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +7.7 | 1e-12 | 28/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +7.5 | 4e-12 | 33/45 (C-33 A, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.4 | 1e-08 | 23/44 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +6.0 | 1e-07 | 25/45 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +5.5 | 2e-06 | 19/42 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.1 | 1e-05 | 23/45 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +5.0 | 2e-05 | 20/34 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.0 | 3e-05 | 20/45 (HEC-1-A, SHP-77, …) | top dose only | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +5.0 | 3e-05 | 20/45 (HOP62, BT-474, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +4.5 | 2e-04 | 20/45 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +4.4 | 5e-04 | 15/45 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.002 | 17/44 (HCT15, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.007 | 11/45 (HOP62, PANC-1, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.008 | 12/45 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.009 | 18/45 (LOX-IMVI, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | 1.19× | +3.1 | 0.049 | 10/45 (C-33 A, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14441.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.612×** | -8.6 | 4e-15 | 29/45 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.643×** | -7.7 | 3e-12 | 28/45 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.680×** | -6.8 | 3e-09 | 30/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.814×** | -5.1 | 4e-05 | 23/45 (A-172, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.737×** | -5.1 | 5e-05 | 23/45 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.745×** | -5.0 | 7e-05 | 20/45 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.739×** | -4.9 | 7e-05 | 22/44 (LoVo, A-427, …) | all doses, flat | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.765×** | -4.7 | 2e-04 | 19/45 (HT-29, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.630×** | -4.2 | 0.001 | 19/45 (SW480, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.806×** | -3.8 | 0.008 | 16/45 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.671×** | -3.7 | 0.013 | 10/44 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.834× | -3.0 | 0.12 | 11/44 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 29.3 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +18.7) | [[Harringtonine (drug)]] 0.5 µM 0.356× (z -11.0) |
| [[C32 (line)]] | wt | 22.1 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.20× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 22.8 | 4 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +19.6) | [[Selinexor (drug)]] 0.5 µM 0.380× (z -8.7) |
| [[A549 (line)]] | wt | 32.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +13.5) | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.95× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +9.3) | — |
| [[KATO III (line)]] | alt | 27.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.0) | [[Bortezomib (drug)]] 0.05 µM 0.265× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 37.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +13.4) | — |
| [[PANC-1 (line)]] | alt | 43.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 41.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.582× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 41.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +13.5) | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 33.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 41.9 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.220× (z -9.8) |
| [[HOP62 (line)]] | alt | 32.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +14.5) | — |
| [[HS-578T (line)]] | alt | 33.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.348× (z -8.7) ⚠ cell-cycle shift, explains ~24% of this change |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +8.7) | — |
| [[J82 (line)]] | alt | 25.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.8) | — |
| [[LoVo (line)]] | wt | 24.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +16.4) | — |
| [[NCI-H1573 (line)]] | alt | 31.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 14.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 6.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +8.9) | — |
| [[RKO (line)]] | wt | 25.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 31.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +10.5) | — |
| [[SNU-1 (line)]] | wt | 40.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.104× (z -9.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 24.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 31.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +12.0) | — |
| [[A-427 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*32 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMTOR5-AS1]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[SNHG10]] | +0.53 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[SLC16A4-AS1]] | +0.53 | +0.56 / +0.38 | both halves | 6e-05 |  |
| [[ZNF460-AS1]] | +0.52 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[GARS1-DT]] | +0.51 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[DLEU2]] | +0.50 | +0.52 / +0.41 | both halves | 4e-05 | same gene group |
| [[NRSN2-AS1]] | +0.49 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[CKS1B]] | +0.49 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[PCK2]] | +0.49 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[TMEM91]] | +0.48 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[MXD3]] | +0.48 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[NR2C2]] | +0.48 | +0.41 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*68 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAS1]] | -0.58 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[MRPS18A]] | -0.57 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[POP4]] | -0.56 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[BCKDK]] | -0.55 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[ZKSCAN2]] | -0.55 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ZNF414]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[BMS1]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[MRPL10]] | -0.53 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[ZNF845]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[KIF3B]] | -0.53 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[REXO4]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[DNAJC18]] | -0.52 | -0.54 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises CRNDE's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRPS18A]] | C | CRNDE activity lowers MRPS18A's level | lines that do not express CRNDE (3) vs lines expressing it (47) | 1.52× higher at baseline in the lines without CRNDE | 0.096 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: HSD17B14, DMXL2, CRB1 |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.366). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-35.0, 10.1); signed map (32.4, -18.0). **Vector** length 112, 27.7% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +25.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.7 | +8.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.6 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.4 | +7.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +8.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | +5.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.6 | +3.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.1 | -8.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.9 | -5.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.4 | -6.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -7.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.2 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | colorectal neoplasia differentially expressed |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16q12.2 — chr16:54,845,189-54,929,189 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LOC643911, LINC00180, CRNDEP |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [643911](https://www.ncbi.nlm.nih.gov/gene/643911):

> This gene is transcribed into multiple transcript variants, some of which may function as non-coding RNAs. One of the transcript variants encodes a putative short protein that is localized to the nucleus (PMID:25978564). Expression of this locus is increased in proliferating tissues, including certain tumors such as colorectal adenomas and adenocarcinomas. Transcription from this gene is negatively regulated by insulin and insulin-like growth factors, and may regulate the expression of genes …

**Accessions** — [HGNC:37078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37078) · Entrez [643911](https://www.ncbi.nlm.nih.gov/gene/643911) · Ensembl [ENSG00000245694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245694)

## Data

Gene col 14441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14441); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14441]; `tensor/DDL_lfc|DDL_z.npy` [14441]; `embed/gene_vectors.npy` [14441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14441 or target_col == 14441). Every well: [[CRNDE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRNDE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
