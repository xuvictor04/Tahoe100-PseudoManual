---
symbol: "STX2"
type: "gene"
col: 3234
ensembl_id: "ENSG00000111450"
name: "syntaxin 2"
location: "12q24.33"
module: 2
arm: "+"
pooled_cpm: 38.59
n_lines_expressing: 47
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# STX2

*syntaxin 2* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.68× (z +12.9, q 2e-35, up in 33 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 1.28× (z +8.6, q 2e-15, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.349× (z -37.1, q 0e+00, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PACS2]] (+0.71, fdr 7e-06), [[DGKZ]] (+0.70, fdr 7e-06), [[ANKRD27]] (+0.68, fdr 2e-05); moves opposite to [[FAM200A]] (-0.63, fdr 3e-05), [[HMG20A]] (-0.60, fdr 2e-05), [[NSUN3]] (-0.58, fdr 6e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[STARD9]] → it (grade B ⚠); 3 go from it, the strongest it → [[GAS2L1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3234.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +12.9 | 2e-35 | 33/44 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.28×** | +8.6 | 2e-15 | 29/45 (NCI-H1792, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +7.6 | 5e-12 | 24/45 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +7.4 | 2e-11 | 21/36 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +7.1 | 1e-10 | 24/45 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +7.0 | 3e-10 | 21/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.34×** | +7.0 | 3e-10 | 24/44 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.29×** | +6.4 | 1e-08 | 21/45 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.29×** | +6.3 | 1e-08 | 25/45 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +6.1 | 7e-08 | 19/41 (HOP62, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +6.0 | 1e-07 | 21/44 (H4, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +5.4 | 3e-06 | 18/44 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +4.3 | 9e-04 | 14/45 (MIA PaCa-2, LOX-IMVI, …) | two highest doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.19× | +4.2 | 0.001 | 14/44 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.17× | +3.8 | 0.004 | 10/45 (SNU-1, LoVo, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.010 | 10/45 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.5 | 0.017 | 15/45 (CFPAC-1, RKO, …) | two highest doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.034 | 6/45 (RKO, SW48, …) | rises with dose |  |
| [[Neratinib (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.039 | 8/45 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.050 | 12/45 (SW480, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.13× | +3.0 | 0.069 | 13/45 (SW48, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3234.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.349×** | -37.1 | 0e+00 | 37/45 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.455×** | -19.7 | 0e+00 | 36/45 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -16.5 | 0e+00 | 34/45 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.516×** | -15.9 | 0e+00 | 32/45 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.472×** | -9.8 | 1e-20 | 32/45 (LOX-IMVI, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.763×** | -9.6 | 8e-20 | 28/45 (SW1417, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.772×** | -6.5 | 7e-09 | 24/45 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -6.2 | 5e-08 | 2/45 (AN3 CA, SW 1271) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.809×** | -5.3 | 7e-06 | 18/45 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.813×** | -5.2 | 1e-05 | 19/45 (HEC-1-A, SNU-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.832×** | -4.4 | 5e-04 | 17/45 (HS-578T, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.750×** | -3.8 | 0.008 | 14/44 (HCT15, A-172, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.908× | -3.4 | 0.026 | 8/45 (J82, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.2 | 0.050 | 11/45 (hTERT-HPNE, SK-MEL-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.914× | -3.2 | 0.050 | 10/45 (HOP62, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3234. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 38.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -19.4) |
| [[A549 (line)]] | wt | 66.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -18.4) |
| [[HS-578T (line)]] | alt | 51.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -22.0) |
| [[J82 (line)]] | alt | 76.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -22.2) |
| [[MIA PaCa-2 (line)]] | alt | 58.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -22.4) |
| [[NCI-H460 (line)]] | wt | 61.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -25.3) |
| [[PANC-1 (line)]] | alt | 42.4 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -17.8) |
| [[SW480 (line)]] | alt | 28.2 | 4 (1 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 2.75× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -12.4) |
| [[A-172 (line)]] | wt | 65.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -24.5) |
| [[HOP62 (line)]] | alt | 50.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -32.3) |
| [[KATO III (line)]] | alt | 13.5 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.04× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 73.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0851× (z -39.3) |
| [[LoVo (line)]] | wt | 22.5 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.03× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -10.1) |
| [[LS 180 (line)]] | wt | 11.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.70× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -13.9) |
| [[A-427 (line)]] | wt | 60.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -14.0) |
| [[H4 (line)]] | wt | 34.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -9.4) |
| [[Hs 766T (line)]] | wt | 41.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -20.4) |
| [[NCI-H1792 (line)]] | alt | 32.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -18.9) |
| [[NCI-H2030 (line)]] | alt | 31.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 55.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -18.1) |
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -17.3) |
| [[RPMI-7951 (line)]] | alt | 33.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0734× (z -27.4) |
| [[SK-MEL-2 (line)]] | alt | 44.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.5) |
| [[SNU-1 (line)]] | wt | 72.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -14.7) |
| [[SNU-423 (line)]] | alt | 52.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -22.5) |
| [[SW 1271 (line)]] | alt | 65.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -8.7) |
| [[SW1417 (line)]] | alt | 42.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -12.7) |
| [[A498 (line)]] | wt | 36.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -14.1) |
| [[C32 (line)]] | wt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -13.0) |
| [[CHP-212 (line)]] | wt | 29.7 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.5 µM 0.0884× (z -8.9) |
| [[HCT15 (line)]] | alt | 42.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 40.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 45.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.6) |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.214× (z -12.2) |
| [[SHP-77 (line)]] | alt | 44.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.2) |
| [[SW 900 (line)]] | alt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -8.7) |
| [[AN3 CA (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.41 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.26 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3234), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACS2]] | +0.71 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[DGKZ]] | +0.70 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[ANKRD27]] | +0.68 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[EPS15]] | +0.67 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[GET1]] | +0.66 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[TCF3]] | +0.65 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ATP13A2]] | +0.65 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.64 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[CORO7]] | +0.63 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[CAMSAP1]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[RSU1]] | +0.63 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[CROCCP3]] | +0.63 | +0.60 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM200A]] | -0.63 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[HMG20A]] | -0.60 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[NSUN3]] | -0.58 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[METTL18]] | -0.58 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[CREB3L4]] | -0.58 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[RBBP6]] | -0.58 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[SMG8]] | -0.58 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[C11orf71]] | -0.58 | -0.60 / -0.32 | both halves | 2e-04 |  |
| [[AP5S1]] | -0.58 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[ZNF830]] | -0.57 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[RBM23]] | -0.57 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[PATL2]] | -0.57 | -0.59 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises STX2's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 3.37× lower at baseline in the lines without STARD9 | 0.003 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[GNAZ]] | B | GNAZ activity raises STX2's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.16× lower at baseline in the lines without GNAZ | 0.004 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[SNTA1]] | B | SNTA1 activity raises STX2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 2.68× lower at baseline in the lines without SNTA1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[MYO5A]] | B | MYO5A activity raises STX2's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 2.85× lower at baseline in the lines without MYO5A | 0.036 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[FOXA1]] | B | FOXA1 activity lowers STX2's level | lines that do not express FOXA1 (22) vs lines expressing it (28) | 1.55× higher at baseline in the lines without FOXA1 | 0.066 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL |
| [[KATNAL1]] | B | KATNAL1 activity raises STX2's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.60× lower at baseline in the lines without KATNAL1 | 0.097 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[FSD1L]] | C | FSD1L activity raises STX2's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 3.93× lower at baseline in the lines without FSD1L | 0.004 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAS2L1]] | C | STX2 activity raises GAS2L1's level | lines that do not express STX2 (3) vs lines expressing it (47) | 1.82× lower at baseline in the lines without STX2 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NPW, PALS2, CAPRIN2; maybe low, not absent; its own permutation p |
| [[DVL1]] | C | STX2 activity raises DVL1's level | lines that do not express STX2 (3) vs lines expressing it (47) | 1.40× lower at baseline in the lines without STX2 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NPW, PALS2, CAPRIN2; maybe low, not absent |
| [[RSU1]] | C | STX2 activity raises RSU1's level | lines that do not express STX2 (3) vs lines expressing it (47) | 2.03× lower at baseline in the lines without STX2 | 0.099 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NPW, PALS2, CAPRIN2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (0.8, 0.8); signed map (-43.4, -7.2). **Vector** length 120, 31.6% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +12.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.6 | +7.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.0 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.8 | +7.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.9 | +3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.6 | +8.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.5 | +3.5 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.8 | +6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.4 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.6 | -37.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.4 | -15.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -19.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.2 | -9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -16.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Docetaxel (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:130,789,600-130,839,254 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EPM; previously STX2B, STX2C, STX2A, EPIM |
| Gene groups (HGNC) | Syntaxins |
| Matched by | ensembl_id |

**Function**, from UniProt [P32856](https://www.uniprot.org/uniprotkb/P32856) (Syntaxin-2):

> Essential for epithelial morphogenesis. May mediate Ca(2+)-regulation of exocytosis acrosomal reaction in sperm.

**Summary**, from NCBI Gene [2054](https://www.ncbi.nlm.nih.gov/gene/2054):

> The product of this gene belongs to the syntaxin/epimorphin family of proteins. The syntaxins are a large protein family implicated in the targeting and fusion of intracellular transport vesicles. The product of this gene regulates epithelial-mesenchymal interactions and epithelial cell morphogenesis and activation. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3403](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3403) · Entrez [2054](https://www.ncbi.nlm.nih.gov/gene/2054) · UniProt [P32856](https://www.uniprot.org/uniprotkb/P32856) · Ensembl [ENSG00000111450](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111450)

## Data

Gene col 3234: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3234); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3234, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3234]; `tensor/DDL_lfc|DDL_z.npy` [3234]; `embed/gene_vectors.npy` [3234]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3234 or target_col == 3234). Every well: [[STX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
