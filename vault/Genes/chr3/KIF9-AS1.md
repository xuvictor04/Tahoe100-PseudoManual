---
symbol: "KIF9-AS1"
type: "gene"
col: 13590
ensembl_id: "ENSG00000227398"
name: "KIF9 antisense RNA 1"
location: "3p21.31"
module: 89
arm: "+"
pooled_cpm: 41.18
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# KIF9-AS1

*KIF9 antisense RNA 1* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.33× (z +19.5, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.489× (z -12.2, q 2e-31, down in 28 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.761× (z -4.7, q 2e-04, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZCCHC10]] (+0.67, fdr 1e-05), [[HOXC8]] (+0.66, fdr 1e-05), [[ZBTB8A]] (+0.65, fdr 1e-05); moves opposite to [[APEH]] (-0.61, fdr 3e-05), [[ECHS1]] (-0.60, fdr 4e-05), [[SNRNP200]] (-0.57, fdr 1e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PODXL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13590.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +19.5 | 0e+00 | 43/48 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +4.5 | 0.002 | 20/47 (NCI-H460, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +4.3 | 0.003 | 18/48 (SW480, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 0.003 | 21/47 (hTERT-HPNE, Hs 766T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 0.003 | 21/47 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.29×** | +4.0 | 0.006 | 16/48 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.9 | 0.007 | 20/47 (RKO, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.011 | 23/48 (NCI-H2347, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.011 | 20/48 (LS 180, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.22×** | +3.6 | 0.019 | 19/48 (NCI-H2347, A-172, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.022 | 20/48 (HEC-1-A, RPMI-7951, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.023 | 13/48 (LS 180, SW1417, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.028 | 14/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.037 | 13/48 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.037 | 11/48 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.041 | 13/47 (LS 180, CHP-212, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13590.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.489×** | -12.2 | 2e-31 | 28/41 (Panc 03.27, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.542×** | -10.9 | 5e-25 | 34/44 (A-172, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.664×** | -7.3 | 8e-11 | 35/46 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.676×** | -6.9 | 5e-10 | 29/48 (SW480, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.658×** | -6.8 | 9e-10 | 30/44 (C-33 A, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.684×** | -6.7 | 2e-09 | 28/48 (SW480, A498, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.603×** | -4.7 | 2e-04 | 17/34 (HEC-1-A, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.761×** | -4.7 | 2e-04 | 24/48 (PANC-1, LoVo, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.768×** | -4.5 | 5e-04 | 23/47 (A498, C32, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.632×** | -4.3 | 0.001 | 23/48 (C32, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.677×** | -3.6 | 0.015 | 21/49 (A-172, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.690×** | -3.4 | 0.027 | 15/48 (C32, A-172, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13590. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 39.0 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 55.4 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[PANC-1 (line)]] | alt | 54.2 | 1 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 40.6 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.345× (z -8.5) |
| [[SW480 (line)]] | alt | 49.3 | 2 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 77.9 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +14.6) | [[Lonafarnib (drug)]] 5 µM 0.0590× (z -18.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 29.1 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +18.7) | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 61.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HS-578T (line)]] | alt | 45.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 44.8 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +9.7) | [[Harringtonine (drug)]] 0.05 µM 0.134× (z -11.5) |
| [[A549 (line)]] | wt | 40.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 62.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C-33 A (line)]] | alt | 91.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0957× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 32.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HCT15 (line)]] | alt | 41.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 22.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.44× (z +15.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 46.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 45.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 46.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[RPMI-7951 (line)]] | alt | 39.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 54.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 45.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +12.4) | [[Docetaxel (drug)]] 0.05 µM 0.406× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HOP62 (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[Hs 766T (line)]] | wt | 29.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 28.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 29.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +8.7) | — |
| [[J82 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 33.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +13.1) | — |
| [[LoVo (line)]] | wt | 35.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +17.8) | — |
| [[NCI-H23 (line)]] | alt | 52.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +8.9) | — |
| [[RKO (line)]] | wt | 34.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 53.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13590), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC10]] | +0.67 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[HOXC8]] | +0.66 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ZBTB8A]] | +0.65 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ZNF785]] | +0.61 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[PIP5K1A]] | +0.60 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[ELMOD3]] | +0.59 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[NAA60]] | +0.59 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ZBTB8OS]] | +0.59 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[UBXN2A]] | +0.58 | +0.63 / +0.34 | both halves | 1e-04 |  |
| [[COA6]] | +0.58 | +0.52 / +0.33 | both halves | 1e-04 |  |
| [[MAFG]] | +0.58 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[SHOX2]] | +0.58 | +0.39 / +0.45 | both halves | 6e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APEH]] | -0.61 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ECHS1]] | -0.60 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[SNRNP200]] | -0.57 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[CORO1C]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[MATCAP1]] | -0.54 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[CSRP1]] | -0.53 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[BCKDK]] | -0.53 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[TTLL12]] | -0.52 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[MYH9]] | -0.51 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[FAM91A1]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ACTB]] | -0.51 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PHF6]] | -0.50 | -0.28 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | PODXL2 activity raises KIF9-AS1's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.34× lower at baseline in the lines without PODXL2 | 0.022 | ⚠ within organs, on part of the lines |
| [[SHOX2]] | B | SHOX2 activity raises KIF9-AS1's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 1.36× lower at baseline in the lines without SHOX2 | 0.040 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B |
| [[SYT13]] | B | SYT13 activity lowers KIF9-AS1's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 1.36× higher at baseline in the lines without SYT13 | 0.043 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[FAM171A1]] | B | FAM171A1 activity raises KIF9-AS1's level | lines that do not express FAM171A1 (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without FAM171A1 | 0.064 | ⚠ within organs, on part of the lines; also absent: PORCN, CMTM7, ANXA6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.382). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.7, 15.6); signed map (4.8, -3.9). **Vector** length 104, 26.4% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +19.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +0.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +4.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.8 | +3.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.2 | +1.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | +4.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.2 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +2.7 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -8.7 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -7.8 | -6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -6.2 | -10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -5.8 | -12.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[Folic acid (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | +0.1 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | KIF9 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p21.31 — chr3:47,164,186-47,246,601 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ39534 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26822) · Entrez [285352](https://www.ncbi.nlm.nih.gov/gene/285352) · Ensembl [ENSG00000227398](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227398)

## Data

Gene col 13590: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13590); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13590, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13590]; `tensor/DDL_lfc|DDL_z.npy` [13590]; `embed/gene_vectors.npy` [13590]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13590 or target_col == 13590). Every well: [[KIF9-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF9-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
