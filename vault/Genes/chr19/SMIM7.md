---
symbol: "SMIM7"
type: "gene"
col: 13166
ensembl_id: "ENSG00000214046"
name: "small integral membrane protein 7"
location: "19p13.11"
module: 36
arm: "+"
pooled_cpm: 39.92
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# SMIM7

*small integral membrane protein 7* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.20× (z +10.3, q 4e-22, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.472× (z -26.5, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCTN4]] (+0.76, fdr 7e-06), [[TAF6L]] (+0.64, fdr 7e-06), [[ZNF875]] (+0.64, fdr 1e-05); moves opposite to [[SLC41A1]] (-0.65, fdr 1e-05), [[TRIM36]] (-0.55, fdr 1e-05), [[CSRNP2]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13166.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.20×** | +10.3 | 4e-22 | 39/49 (HS-578T, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +7.6 | 8e-12 | 35/48 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +7.5 | 2e-11 | 30/48 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +6.6 | 8e-09 | 28/48 (KATO III, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +5.8 | 7e-07 | 26/48 (HS-578T, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +5.7 | 9e-07 | 26/48 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +5.5 | 2e-06 | 22/48 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +5.5 | 4e-06 | 19/41 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +5.3 | 8e-06 | 22/47 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +4.8 | 7e-05 | 15/48 (HS-578T, A-172, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.16× | +3.6 | 0.018 | 19/47 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.018 | 16/47 (HEC-1-A, A-172, …) | rises with dose | composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.14× | +3.3 | 0.039 | 3/48 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.3 | 0.044 | 10/48 (NCI-H2030, SHP-77, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.045 | 9/48 (LOX-IMVI, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.092 | 4/48 (HOP62, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13166.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.472×** | -26.5 | 0e+00 | 47/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.484×** | -17.4 | 0e+00 | 40/48 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.503×** | -16.5 | 0e+00 | 39/48 (NCI-H23, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.687×** | -9.4 | 9e-19 | 35/48 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.696×** | -9.0 | 2e-17 | 33/48 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.697×** | -9.0 | 2e-17 | 35/48 (SW1417, H4, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.792×** | -8.2 | 2e-14 | 25/47 (SNU-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.721×** | -8.2 | 2e-14 | 34/48 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.725×** | -8.0 | 7e-14 | 30/48 (H4, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.813×** | -7.3 | 2e-11 | 28/48 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.816×** | -5.1 | 2e-05 | 22/48 (HCT15, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.815×** | -4.9 | 5e-05 | 24/47 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.833×** | -4.4 | 5e-04 | 18/48 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -4.2 | 0.001 | 12/48 (Hs 766T, LS 180, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.851× | -4.0 | 0.002 | 12/48 (A-427, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.864× | -3.6 | 0.009 | 14/48 (HOP62, H4, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.762×** | -3.5 | 0.012 | 12/48 (Panc 03.27, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.785×** | -3.2 | 0.043 | 12/48 (HOP62, SW 1271, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.885× | -3.1 | 0.056 | 10/48 (SW 1088, LOX-IMVI, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.885× | -3.1 | 0.056 | 12/48 (C-33 A, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13166. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.3 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -14.2) |
| [[COLO 205 (line)]] | alt | 43.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -9.3) |
| [[HOP62 (line)]] | alt | 30.8 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -13.9) |
| [[HS-578T (line)]] | alt | 57.9 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -14.4) |
| [[LS 180 (line)]] | wt | 47.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 32.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -18.2) |
| [[Panc 03.27 (line)]] | alt | 68.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -10.9) |
| [[SHP-77 (line)]] | alt | 87.8 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -14.9) |
| [[SW480 (line)]] | alt | 57.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -14.2) |
| [[A498 (line)]] | wt | 33.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -11.4) |
| [[C32 (line)]] | wt | 38.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -11.4) |
| [[HT-29 (line)]] | alt | 32.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 44.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -15.3) |
| [[NCI-H2030 (line)]] | alt | 43.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 47.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -18.1) |
| [[RKO (line)]] | wt | 35.6 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -9.8) |
| [[SNU-1 (line)]] | wt | 65.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -12.0) |
| [[SNU-423 (line)]] | alt | 49.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -14.2) |
| [[A-172 (line)]] | wt | 36.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -9.8) |
| [[A-427 (line)]] | wt | 46.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.459× (z -11.9) |
| [[A549 (line)]] | wt | 28.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -9.9) |
| [[AN3 CA (line)]] | alt | 41.4 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0608× (z -12.6) |
| [[C-33 A (line)]] | alt | 56.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 33.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -8.9) |
| [[H4 (line)]] | wt | 63.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.266× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 59.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 39.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 28.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.170× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 32.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -8.9) |
| [[LoVo (line)]] | wt | 35.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 29.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 29.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -9.3) |
| [[NCI-H661 (line)]] | alt | 39.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 40.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 34.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.8) |
| [[SW 900 (line)]] | alt | 33.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13166), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN4]] | +0.76 | +0.72 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TAF6L]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ZNF875]] | +0.64 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[ZNF790-AS1]] | +0.62 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[PPP6C]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[MED9]] | +0.61 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[SARS2]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[GTF3C2]] | +0.60 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[CSTPP1]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[UBE2L3]] | +0.58 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[NRDE2]] | +0.57 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SNRPD3]] | +0.57 | +0.70 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC41A1]] | -0.65 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[TRIM36]] | -0.55 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[CSRNP2]] | -0.52 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[LHFPL6]] | -0.48 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[LINC02362]] | -0.48 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[KATNA1]] | -0.48 | -0.47 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SMIM7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.431). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-31.3, -6.6); signed map (-16.9, -20.1). **Vector** length 94.5, 21.2% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.0 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +6.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | -9.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +5.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.1 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -26.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -17.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -16.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.5 | -3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.4 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:16,630,751-16,660,442 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2747; previously C19orf42 |
| Matched by | ensembl_id |

UniProt [Q9BQ49](https://www.uniprot.org/uniprotkb/Q9BQ49) carries no function annotation.

**Summary**, from NCBI Gene [79086](https://www.ncbi.nlm.nih.gov/gene/79086):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28419](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28419) · Entrez [79086](https://www.ncbi.nlm.nih.gov/gene/79086) · UniProt [Q9BQ49](https://www.uniprot.org/uniprotkb/Q9BQ49) · Ensembl [ENSG00000214046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214046)

## Data

Gene col 13166: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13166); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13166, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13166]; `tensor/DDL_lfc|DDL_z.npy` [13166]; `embed/gene_vectors.npy` [13166]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13166 or target_col == 13166). Every well: [[SMIM7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
