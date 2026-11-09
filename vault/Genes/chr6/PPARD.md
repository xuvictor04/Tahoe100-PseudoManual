---
symbol: "PPARD"
type: "gene"
col: 3314
ensembl_id: "ENSG00000112033"
name: "peroxisome proliferator activated receptor delta"
location: "6p21.31"
module: 34
arm: "+"
pooled_cpm: 160.5
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 34
n_dd_up_clean: 9
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 25
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PPARD

*peroxisome proliferator activated receptor delta* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.59× (z +7.5, q 3e-11, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.395× (z -14.4, q 3e-44, down in 35 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.680× (z -8.8, q 3e-16, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLAUR]] (+0.72, fdr 7e-06), [[PLEK2]] (+0.71, fdr 7e-06), [[RDH13]] (+0.71, fdr 1e-05); moves opposite to [[USP24]] (-0.57, fdr 5e-05), [[PAIP1]] (-0.56, fdr 3e-05), [[TGFBRAP1]] (-0.55, fdr 4e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[SEMA3B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +7.5 | 3e-11 | 27/46 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +7.4 | 4e-11 | 31/46 (PANC-1, C32, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +7.3 | 6e-11 | 26/46 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +6.2 | 1e-07 | 25/46 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +6.1 | 1e-07 | 23/46 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.73×** | +4.6 | 4e-04 | 28/46 (KATO III, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.32×** | +4.5 | 6e-04 | 25/46 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.002 | 23/45 (COLO 205, Panc 03.27, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.018 | 23/45 (H4, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.083 | 20/46 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.085 | 20/45 (H4, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.11 | 15/46 (J82, A498, …) | all doses, flat |  |
| [[Dabrafenib (drug)]] 5 µM |  | 1.43× | +3.0 | 0.11 | 18/47 (SW480, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3314.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.395×** | -14.4 | 3e-44 | 35/41 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.442×** | -13.2 | 4e-37 | 42/47 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.515×** | -9.9 | 9e-21 | 34/43 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.680×** | -8.8 | 3e-16 | 34/46 (HOP62, SNU-423, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.603×** | -8.1 | 4e-14 | 34/46 (AsPC-1, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.722×** | -7.4 | 1e-11 | 25/46 (NCI-H2347, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.658×** | -6.5 | 8e-09 | 33/45 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -5.6 | 2e-06 | 25/47 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.525×** | -5.4 | 4e-06 | 33/45 (Panc 03.27, HT-29, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.741×** | -5.3 | 6e-06 | 32/46 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.724×** | -5.0 | 3e-05 | 33/46 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.736×** | -4.7 | 1e-04 | 27/45 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.817×** | -4.6 | 2e-04 | 23/46 (AsPC-1, LoVo, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.767×** | -4.6 | 2e-04 | 24/46 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.752×** | -4.6 | 2e-04 | 23/46 (AsPC-1, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.755×** | -4.5 | 2e-04 | 26/47 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.780×** | -4.5 | 2e-04 | 22/48 (AsPC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.756×** | -4.5 | 2e-04 | 23/46 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.751×** | -4.4 | 4e-04 | 26/46 (AsPC-1, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 390 | 0 | 20 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0832× (z -22.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 427 | 0 | 17 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -19.8) |
| [[SNU-423 (line)]] | alt | 521 | 0 | 15 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -20.2) |
| [[CFPAC-1 (line)]] | alt | 544 | 0 | 13 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -24.8) |
| [[SW480 (line)]] | alt | 152 | 0 | 13 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.424× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 476 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -18.7) |
| [[PANC-1 (line)]] | alt | 66.7 | 8 (4 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.93× (z +11.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -10.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 307 | 1 (1 ⚠) | 7 (4 ⚠) | [[Daptomycin (drug)]] 5 µM 2.31× (z +8.5) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -19.5) |
| [[SW1417 (line)]] | alt | 287 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -16.8) |
| [[A549 (line)]] | wt | 99.6 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0389× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 272 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.5) |
| [[A-172 (line)]] | wt | 167 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.405× (z -10.9) |
| [[J82 (line)]] | alt | 138 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.479× (z -10.3) |
| [[LoVo (line)]] | wt | 141 | 1 (1 ⚠) | 3 (2 ⚠) | [[Daptomycin (drug)]] 5 µM 2.60× (z +9.7) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.177× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 73.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +11.4) | — |
| [[C32 (line)]] | wt | 69.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +18.9) | — |
| [[H4 (line)]] | wt | 94.6 | 2 | 1 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.61× (z +9.2) | [[Cobimetinib (drug)]] 5 µM 0.266× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 51.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +13.4) | — |
| [[HS-578T (line)]] | alt | 180 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -13.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 70.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 80.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +20.0) | — |
| [[SK-MEL-2 (line)]] | alt | 60.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -11.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 58.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +12.8) | — |
| [[BT-474 (line)]] | alt | 74.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 311 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -15.7) |
| [[KATO III (line)]] | alt | 135 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.62× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 57.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -12.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 44.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 85.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 93.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 96.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -10.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 69.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.1) | — |
| [[SW48 (line)]] | wt | 172 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0526× (z -20.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 97.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 116 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 34.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 83.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAUR]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[PLEK2]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[RDH13]] | +0.71 | +0.67 / +0.57 | both halves | 1e-05 | pathway: Signaling by Nuclear Receptors |
| [[PDE2A]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ABTB3]] | +0.69 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[TMCC3]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PLEKHM1P1]] | +0.68 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[SERPINB1]] | +0.67 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[SEMA7A]] | +0.67 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[KRT15]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[KIF21B]] | +0.65 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[LRRC8A]] | +0.65 | +0.71 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP24]] | -0.57 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[PAIP1]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[TGFBRAP1]] | -0.55 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[SUCLG2-DT]] | -0.55 | -0.55 / -0.22 | both halves | 6e-04 |  |
| [[GTF2I]] | -0.54 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[AKAP7]] | -0.54 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[MGST1]] | -0.54 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[RAB11FIP2]] | -0.54 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[GAS2]] | -0.54 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[CABLES1]] | -0.54 | -0.55 / -0.22 | both halves | 6e-04 |  |
| [[TLK1]] | -0.54 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[CFAP418]] | -0.53 | -0.53 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 25, C 0. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA3B]] | B | SEMA3B activity raises PPARD's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.24× lower at baseline in the lines without SEMA3B | 0.001 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[ANO1]] | B | ANO1 activity raises PPARD's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 1.88× lower at baseline in the lines without ANO1 | 0.003 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[TINAGL1]] | B | TINAGL1 activity raises PPARD's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.31× lower at baseline in the lines without TINAGL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[CARD11]] | B | CARD11 activity raises PPARD's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.94× lower at baseline in the lines without CARD11 | 0.015 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[CDH1]] | B | CDH1 activity raises PPARD's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.01× lower at baseline in the lines without CDH1 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| KDR | B | KDR activity raises PPARD's level | compounds that target KDR: 5 of 8 lower it (Cabozantinib, Ponatinib, Regorafenib, Sulfatinib, Sunitinib) | 62% of the class's compounds vs 6.2% of all compounds | 0.036 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[SEMA7A]] | B | SEMA7A activity raises PPARD's level | lines that do not express SEMA7A (13) vs lines expressing it (37) | 1.95× lower at baseline in the lines without SEMA7A | 0.036 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PADI1]] | B | PADI1 activity raises PPARD's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 2.07× lower at baseline in the lines without PADI1 | 0.045 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[WNT7B]] | B | WNT7B activity raises PPARD's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.97× lower at baseline in the lines without WNT7B | 0.051 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[SULT2B1]] | B | SULT2B1 activity raises PPARD's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 1.65× lower at baseline in the lines without SULT2B1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[EVA1A-AS]] | B | EVA1A-AS activity raises PPARD's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 1.88× lower at baseline in the lines without EVA1A-AS | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[KCNK1]] | B | KCNK1 activity raises PPARD's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 1.66× lower at baseline in the lines without KCNK1 | 0.058 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.8, 0.7); signed map (-0.1, 46.0). **Vector** length 135, 45.5% of its response variance represented; |z| ≥ 3 in 1,744 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +8.1 | +7.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.5 | +7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.5 | +6.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.7 | +4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.0 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +3.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.2 | +1.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.8 | -7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.4 | -8.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.5 | -3.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.9 | -4.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -5.6 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.5 | -4.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.4 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | peroxisome proliferator activated receptor delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:35,342,558-35,428,191 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NUC1, NUCII, FAAR, NR1C2, PPARB |
| Gene groups (HGNC) | Peroxisome proliferator activated receptors |
| Hallmark sets | NOTCH_SIGNALING, WNT_BETA_CATENIN_SIGNALING, XENOBIOTIC_METABOLISM |
| Reactome | 6 pathways, smallest: Carnitine shuttle; Signaling by Retinoic Acid; Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03181](https://www.uniprot.org/uniprotkb/Q03181) (Peroxisome proliferator-activated receptor delta):

> Ligand-activated transcription factor key mediator of energy metabolism in adipose tissues. Receptor that binds peroxisome proliferators such as hypolipidemic drugs and fatty acids. Has a preference for poly-unsaturated fatty acids, such as gamma-linoleic acid and eicosapentanoic acid. Once activated by a ligand, the receptor binds to promoter elements of target genes. Regulates the peroxisomal beta-oxidation pathway of fatty acids. Functions as transcription activator for the acyl-CoA oxidase …

**Summary**, from NCBI Gene [5467](https://www.ncbi.nlm.nih.gov/gene/5467):

> This gene encodes a member of the peroxisome proliferator-activated receptor (PPAR) family. The encoded protein is thought to function as an integrator of transcriptional repression and nuclear receptor signaling. It may inhibit the ligand-induced transcriptional activity of peroxisome proliferator activated receptors alpha and gamma, though evidence for this effect is inconsistent. Expression of this gene in colorectal cancer cells may be variable but is typically relatively low. Knockout …

**Accessions** — [HGNC:9235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9235) · Entrez [5467](https://www.ncbi.nlm.nih.gov/gene/5467) · UniProt [Q03181](https://www.uniprot.org/uniprotkb/Q03181) · Ensembl [ENSG00000112033](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112033)

## Data

Gene col 3314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3314); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3314]; `tensor/DDL_lfc|DDL_z.npy` [3314]; `embed/gene_vectors.npy` [3314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3314 or target_col == 3314). Every well: [[PPARD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPARD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
