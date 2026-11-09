---
symbol: "MICALL1"
type: "gene"
col: 1876
ensembl_id: "ENSG00000100139"
name: "MICAL like 1"
location: "22q13.1"
module: 65
arm: "-"
pooled_cpm: 26.5
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 21
n_dd_up_clean: 14
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# MICALL1

*MICAL like 1* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[5-Azacytidine (drug)]] 5 µM: 1.67× (z +8.1, q 2e-13, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.396× (z -14.6, q 1e-45, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPNE2]] (+0.65, fdr 7e-06), [[ADCY7]] (+0.64, fdr 9e-06), [[ZNF767P-1]] (+0.63, fdr 7e-06); moves opposite to [[ARHGAP12]] (-0.67, fdr 7e-06), [[RHOXF1]] (-0.66, fdr 7e-06), [[ORC4]] (-0.57, fdr 3e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PDK4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1876.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **1.67×** | +8.1 | 2e-13 | 37/47 (KATO III, A498, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.43×** | +8.0 | 2e-13 | 38/48 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.70×** | +8.0 | 2e-13 | 37/47 (COLO 205, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.63×** | +7.7 | 2e-12 | 35/48 (COLO 205, HT-29, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.64×** | +7.5 | 6e-12 | 31/47 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.56×** | +7.0 | 3e-10 | 34/47 (COLO 205, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.54×** | +6.8 | 7e-10 | 33/47 (COLO 205, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.48×** | +6.2 | 4e-08 | 32/47 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +5.9 | 3e-07 | 28/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +5.3 | 8e-06 | 25/48 (AsPC-1, NCI-H1573, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 9e-05 | 23/47 (H4, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Neratinib (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.002 | 21/47 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.002 | 18/47 (COLO 205, SK-MEL-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.30×** | +4.1 | 0.002 | 22/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.31×** | +4.0 | 0.003 | 19/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.005 | 12/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.57×** | +3.7 | 0.006 | 12/45 (CFPAC-1, PANC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.032 | 14/45 (A498, H4, …) | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +3.2 | 0.038 | 8/48 (Panc 03.27, C-33 A, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.054 | 11/48 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1876.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.396×** | -14.6 | 1e-45 | 44/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.467×** | -12.1 | 5e-31 | 38/48 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.498×** | -11.1 | 4e-26 | 39/48 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -7.2 | 1e-10 | 26/46 (RKO, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.459×** | -6.4 | 1e-08 | 30/46 (H4, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.672×** | -6.3 | 3e-08 | 32/48 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.693×** | -5.8 | 4e-07 | 24/48 (NCI-H1573, J82, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.693×** | -5.8 | 4e-07 | 27/46 (SW48, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.790×** | -5.3 | 7e-06 | 23/48 (KATO III, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.729×** | -4.8 | 8e-05 | 24/48 (A-427, LoVo, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.815×** | -4.6 | 2e-04 | 22/47 (A-427, RKO, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.753×** | -4.5 | 3e-04 | 22/47 (A-427, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.818×** | -4.5 | 3e-04 | 19/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.786×** | -3.8 | 0.005 | 19/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.658×** | -3.5 | 0.019 | 13/48 (A498, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.038 | 8/48 (NCI-H2030, A-172, …) | top dose only | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.826×** | -3.0 | 0.069 | 13/48 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.700×** | -3.0 | 0.083 | 17/47 (RKO, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1876. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 66.3 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -15.4) |
| [[J82 (line)]] | alt | 41.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -10.9) |
| [[LoVo (line)]] | wt | 35.3 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.238× (z -11.9) |
| [[A-172 (line)]] | wt | 45.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.174× (z -15.5) |
| [[A498 (line)]] | wt | 47.2 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.393× (z -10.1) |
| [[A-427 (line)]] | wt | 23.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -12.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 26.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.269× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 38.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.211× (z -9.2) |
| [[HS-578T (line)]] | alt | 49.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -14.5) |
| [[SNU-423 (line)]] | alt | 34.7 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -9.4) |
| [[AN3 CA (line)]] | alt | 34.6 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0637× (z -10.4) |
| [[BT-474 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0840× (z -11.8) ⚠ cell-cycle shift, explains ~18% of this change |
| [[C-33 A (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.192× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~16% of this change |
| [[COLO 205 (line)]] | alt | 18.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 18.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.261× (z -8.5) |
| [[Hs 766T (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.237× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 19.5 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.59× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 36.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.355× (z -9.3) |
| [[LS 180 (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.279× (z -8.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.264× (z -8.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 35.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0768× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1876), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPNE2]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ADCY7]] | +0.64 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[ZNF767P-1]] | +0.63 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[GTPBP2]] | +0.60 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[KLC1]] | +0.58 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[LTO1]] | +0.57 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[RBPMS2]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CLIP1]] | +0.57 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[TYRO3]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PVR]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TLNRD1]] | +0.56 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[NUTM2A-AS1]] | +0.56 | +0.42 / +0.66 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP12]] | -0.67 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[RHOXF1]] | -0.66 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[ORC4]] | -0.57 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[FAM13A]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[CTDSPL2]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[IFT172]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[HMGN3]] | -0.53 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[PTCD3]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[CNOT2]] | -0.52 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PRDX2]] | -0.51 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[SLC25A40]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ZNF292]] | -0.50 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDK4]] | B | PDK4 activity lowers MICALL1's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 1.56× higher at baseline in the lines without PDK4 | 0.011 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[NUP62CL]] | B | NUP62CL activity lowers MICALL1's level | lines that do not express NUP62CL (19) vs lines expressing it (31) | 1.35× higher at baseline in the lines without NUP62CL | 0.053 | ⚠ within organs, on part of the lines; also absent: LINC01589, ABCC3, GOLT1A |
| [[ADM2]] | B | ADM2 activity lowers MICALL1's level | lines that do not express ADM2 (9) vs lines expressing it (41) | 1.63× higher at baseline in the lines without ADM2 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with PTEN; also absent: CXADR, ARHGAP26, CFL1P1-1; its own permutation p |
| [[LINC01564]] | B | LINC01564 activity lowers MICALL1's level | lines that do not express LINC01564 (24) vs lines expressing it (26) | 1.19× higher at baseline in the lines without LINC01564 | 0.096 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent |
| [[SPRY1]] | C | SPRY1 activity lowers MICALL1's level | lines that do not express SPRY1 (4) vs lines expressing it (46) | 1.83× higher at baseline in the lines without SPRY1 | 0.037 | ⚠ few lines (4 vs 46); across organs; also absent: ARG2, ZNF385C, ENSG00000290927; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.380). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (17.9, -11.2); signed map (-7.4, 25.2). **Vector** length 118, 32.0% of its response variance represented; |z| ≥ 3 in 1,287 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +5.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +7.7 | +8.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.4 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | +7.3 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +5.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.6 | +8.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +6.3 | +6.2 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.2 | -6.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -2.5 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -2.4 | -5.8 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -2.4 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | MICAL like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,905,657-37,942,822 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MIRAB13, KIAA1668, MICAL-L1 |
| Gene groups (HGNC) | LIM domain containing; Bivalent Mical/EHBP Rab binding domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3F8](https://www.uniprot.org/uniprotkb/Q8N3F8) (MICAL-like protein 1):

> Lipid-binding protein with higher affinity for phosphatidic acid, a lipid enriched in recycling endosome membranes. On endosome membranes, acts as a downstream effector of Rab proteins recruiting cytosolic proteins to regulate membrane tubulation. Involved in a late step of receptor-mediated endocytosis regulating for instance endocytosed-EGF receptor trafficking. Alternatively, regulates slow endocytic recycling of endocytosed proteins back to the plasma membrane. Also involved in cargo …

**Summary**, from NCBI Gene [85377](https://www.ncbi.nlm.nih.gov/gene/85377):

> Enables several functions, including identical protein binding activity; phosphatidic acid binding activity; and small GTPase binding activity. Involved in several processes, including plasma membrane tubulation; protein localization to endosome; and slow endocytic recycling. Located in several cellular components, including cilium; endosome; and microtubule organizing center. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29804](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29804) · Entrez [85377](https://www.ncbi.nlm.nih.gov/gene/85377) · UniProt [Q8N3F8](https://www.uniprot.org/uniprotkb/Q8N3F8) · Ensembl [ENSG00000100139](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100139)

## Data

Gene col 1876: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1876); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1876, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1876]; `tensor/DDL_lfc|DDL_z.npy` [1876]; `embed/gene_vectors.npy` [1876]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1876 or target_col == 1876). Every well: [[MICALL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MICALL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
