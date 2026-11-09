---
symbol: "NUP50-DT"
type: "gene"
col: 13528
ensembl_id: "ENSG00000226328"
name: "NUP50 divergent transcript"
location: "22q13.31"
module: 17
arm: "-"
pooled_cpm: 32.34
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# NUP50-DT

*NUP50 divergent transcript* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.02× (z +14.7, q 0e+00, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.272× (z -10.1, q 5e-21, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPOPL-DT]] (+0.63, fdr 1e-05), [[FBXO10]] (+0.58, fdr 1e-05), [[PTGR3]] (+0.57, fdr 3e-05); moves opposite to [[NIPSNAP1]] (-0.64, fdr 1e-05), [[ALAD]] (-0.61, fdr 5e-05), [[RAB3A]] (-0.58, fdr 1e-04).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13528.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +14.7 | 0e+00 | 38/45 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.49×** | +13.0 | 7e-36 | 39/44 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +10.1 | 8e-22 | 35/46 (SW480, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +8.0 | 2e-13 | 29/45 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.48×** | +5.8 | 6e-07 | 30/46 (KATO III, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.8 | 7e-07 | 26/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +5.5 | 4e-06 | 28/46 (CFPAC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.44×** | +5.3 | 6e-06 | 24/46 (Hs 766T, A498, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +4.7 | 1e-04 | 20/46 (A-172, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 6e-04 | 18/45 (COLO 205, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +4.3 | 8e-04 | 20/47 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.002 | 18/47 (CFPAC-1, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.009 | 20/47 (HCT15, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.28×** | +3.6 | 0.011 | 12/46 (J82, BT-474, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.18× | +3.5 | 0.017 | 12/47 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.029 | 14/47 (HOP62, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +3.3 | 0.034 | 10/47 (Hs 766T, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13528.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.272×** | -10.1 | 5e-21 | 39/47 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.414×** | -6.8 | 3e-09 | 27/44 (LS 180, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.501×** | -5.3 | 2e-05 | 27/43 (SW48, C32, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.724×** | -4.8 | 3e-04 | 23/41 (LoVo, HCT15, …) | two highest doses | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.754×** | -4.0 | 0.007 | 15/34 (SW48, C-33 A, …) | two highest doses | cell-cycle shift (explains ~16% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | 0.847× | -3.5 | 0.052 | 16/47 (LoVo, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.796×** | -3.2 | 0.087 | 18/47 (PANC-1, SW48, …) | top dose only | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -3.2 | 0.087 | 3/47 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.665× | -3.1 | 0.10 | 15/39 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.811× | -3.1 | 0.11 | 10/47 (C32, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13528. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 124 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0857× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[NG25 (drug)]] 5 µM 0.0260× (z -13.3) |
| [[LoVo (line)]] | wt | 105 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -18.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 34.5 | 4 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 3.76× (z +14.6) | [[TAK-901 (drug)]] 5 µM 0.221× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 54.9 | 1 (1 ⚠) | 3 (3 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.46× (z +9.3) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 76.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0981× (z -8.6) |
| [[PANC-1 (line)]] | alt | 38.6 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +12.8) | [[Harringtonine (drug)]] 5 µM 0.308× (z -11.2) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.166× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 31.9 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0524× (z -11.4) |
| [[A498 (line)]] | wt | 38.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -19.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 40.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -13.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 12.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +9.5) | — |
| [[J82 (line)]] | alt | 17.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 35.4 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.37× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 66.6 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.117× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 32.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.17× (z +10.9) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -8.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 35.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 24.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 13.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 27.8 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0914× (z -8.6) |
| [[C-33 A (line)]] | alt | 73.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -11.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 24.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.58× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 25.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.69× (z +12.1) | — |
| [[Hs 766T (line)]] | wt | 53.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -8.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 26.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0713× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 21.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 18.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 9.48 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0828× (z -9.4) |
| [[A-172 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.02 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13528), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOPL-DT]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 | same gene group |
| [[FBXO10]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[PTGR3]] | +0.57 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[NUTM2A-AS1]] | +0.57 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[TLNRD1]] | +0.57 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[DPH5-DT]] | +0.56 | +0.56 / +0.43 | both halves | 3e-05 | same gene group |
| [[ENOX2]] | +0.56 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[ATR]] | +0.56 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[EPM2A]] | +0.55 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[HSPBAP1]] | +0.55 | +0.58 / +0.35 | both halves | 1e-04 |  |
| [[GABPB1-AS1]] | +0.55 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[FAM86HP]] | +0.55 | +0.56 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPSNAP1]] | -0.64 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ALAD]] | -0.61 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[RAB3A]] | -0.58 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[SKIC3]] | -0.57 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[MAPRE2]] | -0.55 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[BBS5]] | -0.55 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[MDH1]] | -0.55 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[CAT]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[MTMR4]] | -0.54 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ACACB]] | -0.54 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[LRP1]] | -0.53 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[GSTM4]] | -0.53 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NUP50-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CA9]] | B | CA9 activity strengthens NUP50-DT's drug response | lines that do not express CA9 (18) vs lines expressing it (29) | the lines without CA9 respond 0.70× as strongly (z diff +1.16); strongest at Idarubicin (hydrochloride) 5 µM: 1.49x vs 2.09x (z diff +2.5) | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (7.8, -7.3); signed map (13.2, -5.3). **Vector** length 123, 33.9% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +9.0 | +13.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.3 | +10.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.7 | +4.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +6.2 | +5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.8 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +2.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.5 | -10.1 |
|  | [[NG25 (drug)]] 5 µM |  | -5.7 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -6.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.2 | +1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.5 | -1.4 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -2.4 | -2.3 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | NUP50 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q13.31 — chr22:45,133,020-45,163,811 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously NUP50-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50502](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50502) · Entrez [100506714](https://www.ncbi.nlm.nih.gov/gene/100506714) · Ensembl [ENSG00000226328](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226328)

## Data

Gene col 13528: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13528); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13528, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13528]; `tensor/DDL_lfc|DDL_z.npy` [13528]; `embed/gene_vectors.npy` [13528]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13528 or target_col == 13528). Every well: [[NUP50-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP50-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
