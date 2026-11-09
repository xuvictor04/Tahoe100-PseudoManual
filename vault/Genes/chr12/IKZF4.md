---
symbol: "IKZF4"
type: "gene"
col: 4430
ensembl_id: "ENSG00000123411"
name: "IKAROS family zinc finger 4"
location: "12q13.2"
module: 38
arm: "+"
pooled_cpm: 13.5
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# IKZF4

*IKAROS family zinc finger 4* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.04× (z +35.3, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.612× (z -8.8, q 7e-16, down in 21 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.676× (z -7.0, q 6e-10, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUOX]] (+0.74, fdr 7e-06, ⚠ same locus), [[CD27-AS1]] (+0.66, fdr 7e-06), [[KLC4]] (+0.66, fdr 7e-06), [[GLE1]] (+0.63, fdr 7e-06); moves opposite to [[SOAT1]] (-0.57, fdr 3e-05), [[AGPS]] (-0.55, fdr 3e-05), [[CBX6]] (-0.55, fdr 1e-04).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4430.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.04×** | +35.3 | 0e+00 | 45/46 (LoVo, A498, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +13.1 | 1e-36 | 29/46 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.81×** | +10.6 | 7e-24 | 30/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +9.1 | 2e-17 | 28/48 (HOP62, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +8.8 | 2e-16 | 26/48 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +7.0 | 2e-10 | 4/48 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +6.5 | 9e-09 | 21/41 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.2 | 4e-08 | 22/47 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.9 | 2e-07 | 20/45 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.041 | 7/47 (LS 180, H4, …) | two highest doses |  |
| [[Berbamine (drug)]] 5 µM |  | 1.13× | +3.1 | 0.10 | 2/48 (NCI-H1573, SHP-77) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.10 | 2/48 (NCI-H1573, HCT15) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.0 | 0.11 | 17/45 (SK-MEL-2, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4430.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.612×** | -8.8 | 7e-16 | 21/39 (SHP-77, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.676×** | -7.0 | 6e-10 | 23/47 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.682×** | -6.6 | 7e-09 | 15/24 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.689×** | -6.2 | 8e-08 | 19/31 (A498, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.723×** | -5.8 | 6e-07 | 19/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.737×** | -5.5 | 4e-06 | 20/47 (NCI-H23, RPMI-7951, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -5.3 | 9e-06 | 22/48 (HS-578T, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.745×** | -5.3 | 9e-06 | 19/47 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.759×** | -5.0 | 5e-05 | 17/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.760×** | -4.9 | 5e-05 | 15/47 (H4, COLO 205, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.787×** | -4.3 | 8e-04 | 20/47 (SW480, NCI-H661, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.797×** | -4.1 | 0.002 | 15/45 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.799×** | -4.0 | 0.002 | 15/48 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.824×** | -3.3 | 0.033 | 8/46 (hTERT-HPNE, C-33 A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.835× | -3.3 | 0.043 | 8/46 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Pimitespib (drug)]] 0.05 µM |  | 0.834× | -3.1 | 0.064 | 5/48 (SNU-1, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4430. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.9 | 3 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +17.2) | [[Docetaxel (drug)]] 0.05 µM 0.282× (z -10.0) ⚠ transcription drop; cell-cycle shift, explains ~51% of this change |
| [[SW480 (line)]] | alt | 22.1 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -11.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 11.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.40× (z +18.6) | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -13.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 17.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +19.1) | — |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 12.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.0832× (z -13.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.43 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +18.1) | — |
| [[BT-474 (line)]] | alt | 10.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.79× (z +13.8) | [[Harringtonine (drug)]] 0.05 µM 0.101× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 16.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +13.4) | — |
| [[HOP62 (line)]] | alt | 9.37 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 10.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.32× (z +9.8) | [[Mozavaptan (drug)]] 5 µM 0.0851× (z -8.9) |
| [[J82 (line)]] | alt | 8.63 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 12.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 14.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -10.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 20.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -11.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 16.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -12.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 16.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -9.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 12.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -10.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 8.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.63× (z +15.0) | — |
| [[AsPC-1 (line)]] | alt | 6.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.12× (z +12.2) | — |
| [[C32 (line)]] | wt | 9.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.17× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +10.9) | — |
| [[H4 (line)]] | wt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 27.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +11.7) | — |
| [[LOX-IMVI (line)]] | wt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.02× (z +14.7) | — |
| [[LS 180 (line)]] | wt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.11× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.204× (z -9.4) ⚠ cell-cycle shift, explains ~5% of this change |
| [[NCI-H23 (line)]] | alt | 23.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +8.7) | — |
| [[RKO (line)]] | wt | 21.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 9.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.09× (z +11.3) | — |
| [[SW48 (line)]] | wt | 9.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.70× (z +9.2) | — |
| [[A-427 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4430), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUOX]] | +0.74 | +0.70 / +0.76 | both halves | 7e-06 | STRING 416; ⚠ same locus (1.0 kb, same strand: neighbours can correlate without regulation) |
| [[CD27-AS1]] | +0.66 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[KLC4]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[GLE1]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[DHDH]] | +0.63 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[RECQL5]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[FAM209A]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ISY1-RAB43]] | +0.62 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[RSRP1]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[RSPH9]] | +0.61 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[TRIM39]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TXNL4B]] | +0.60 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[LINC00672]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOAT1]] | -0.57 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[AGPS]] | -0.55 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[CBX6]] | -0.55 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[MRTFB]] | -0.55 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[DFFA]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[TMEM33]] | -0.54 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[UBE2E2]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[SACS]] | -0.53 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[NAA40]] | -0.53 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[DNAH14]] | -0.52 | -0.17 / -0.60 | ⚠ one half (not replicated) | 0.001 |  |
| [[COBL]] | -0.51 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[G3BP1]] | -0.51 | -0.32 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IKZF4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[F2]] | B | F2 activity raises IKZF4's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.41× lower at baseline in the lines without F2 | 0.036 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.1, -23.1); signed map (9.3, 10.3). **Vector** length 82.5, 15.4% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +35.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +13.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.7 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +5.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +9.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +0.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.3 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | IKAROS family zinc finger 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:56,007,659-56,038,435 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Eos; previously ZNFN1A4 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2S9](https://www.uniprot.org/uniprotkb/Q9H2S9) (Zinc finger protein Eos):

> DNA-binding protein that binds to the 5'GGGAATRCC-3' Ikaros-binding sequence. Transcriptional repressor. Interacts with SPI1 and MITF to repress transcription of the CTSK and ACP5 promoters via recruitment of corepressors SIN3A and CTBP2. May be involved in the development of central and peripheral nervous systems. Essential for the inhibitory function of regulatory T-cells (Treg). Mediates FOXP3-mediated gene silencing in regulatory T-cells (Treg) via recruitment of corepressor CTBP1 (By …

**Summary**, from NCBI Gene [64375](https://www.ncbi.nlm.nih.gov/gene/64375):

> Members of the Ikaros (ZNFN1A1; MIM 603023) family of transcription factors, which includes Eos, are expressed in lymphocytes and are implicated in the control of lymphoid development.[supplied by OMIM, Jul 2002]

**Accessions** — [HGNC:13179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13179) · Entrez [64375](https://www.ncbi.nlm.nih.gov/gene/64375) · UniProt [Q9H2S9](https://www.uniprot.org/uniprotkb/Q9H2S9) · Ensembl [ENSG00000123411](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123411)

## Data

Gene col 4430: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4430); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4430, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4430]; `tensor/DDL_lfc|DDL_z.npy` [4430]; `embed/gene_vectors.npy` [4430]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4430 or target_col == 4430). Every well: [[IKZF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IKZF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
