---
symbol: "CACNA2D1"
type: "gene"
col: 7755
ensembl_id: "ENSG00000153956"
name: "calcium voltage-gated channel auxiliary subunit alpha2delta 1"
location: "7q21.11"
module: 202
arm: "+"
pooled_cpm: 64.79
n_lines_expressing: 30
n_dd_up: 17
n_dd_down: 20
n_dd_up_clean: 13
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 12
direction_downstream: 17
tags: ["gene", "module/202"]
generated_by: "tahoemap"
---

# CACNA2D1

*calcium voltage-gated channel auxiliary subunit alpha2delta 1* — 7q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.64× (z +18.8, q 0e+00, up in 22 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.313× (z -16.0, q 0e+00, down in 28 of 28 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS35L]] (+0.73, fdr 1e-05), [[TENM3-AS1]] (+0.72, fdr 4e-05), [[ARHGAP15]] (+0.71, fdr 8e-05); moves opposite to [[SDHAP1]] (-0.70, fdr 1e-05), [[MPG]] (-0.70, fdr 2e-05), [[LCMT1]] (-0.69, fdr 2e-05).
> It is in [[Module 202]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[CLMN]] → it (grade B ⚠); 17 go from it, the strongest it → [[CFAP54]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7755.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +18.8 | 0e+00 | 22/28 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +13.9 | 1e-41 | 18/28 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.22×** | +10.5 | 2e-23 | 20/28 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +9.0 | 5e-17 | 21/28 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +8.6 | 1e-15 | 20/28 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.7 | 3e-09 | 19/28 (NCI-H2347, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +5.3 | 1e-05 | 20/28 (C32, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +5.2 | 1e-05 | 14/27 (A-427, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +5.2 | 1e-05 | 12/25 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.012 | 15/28 (NCI-H2347, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.32×** | +3.6 | 0.020 | 15/30 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.023 | 14/28 (HOP62, C32, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +3.3 | 0.042 | 12/29 (NCI-H1573, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.046 | 10/29 (C32, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.069 | 10/28 (hTERT-HPNE, NCI-H460, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.072 | 9/28 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.072 | 10/27 (A498, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7755.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.313×** | -16.0 | 0e+00 | 28/28 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.325×** | -15.4 | 0e+00 | 27/28 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.328×** | -15.3 | 0e+00 | 26/28 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.575×** | -7.6 | 4e-12 | 26/28 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.616×** | -6.7 | 3e-09 | 21/28 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.478×** | -5.3 | 1e-05 | 18/29 (LOX-IMVI, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.716×** | -4.6 | 3e-04 | 18/29 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.722×** | -4.3 | 0.001 | 14/28 (RKO, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -4.2 | 0.002 | 17/28 (SHP-77, NCI-H23, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.818×** | -3.9 | 0.005 | 18/29 (CHP-212, SHP-77, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.583×** | -3.9 | 0.005 | 19/29 (A549, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.756×** | -3.8 | 0.006 | 16/28 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.764×** | -3.7 | 0.009 | 16/28 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Mebendazole (drug)]] 5 µM |  | **0.773×** | -3.4 | 0.026 | 15/28 (A549, SHP-77, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.642×** | -3.2 | 0.054 | 11/28 (NCI-H460, CHP-212, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.743×** | -3.0 | 0.084 | 9/28 (C32, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.803×** | -3.0 | 0.084 | 14/28 (A549, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7755. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 284 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0498× (z -27.6) |
| [[HOP62 (line)]] | alt | 80.9 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -11.9) |
| [[A498 (line)]] | wt | 86.8 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +22.2) | [[Panobinostat (drug)]] 5 µM 0.352× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 230 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0870× (z -28.1) |
| [[PANC-1 (line)]] | alt | 54.0 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +22.5) | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -13.6) |
| [[A549 (line)]] | wt | 174 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.0826× (z -17.8) |
| [[NCI-H2347 (line)]] | alt | 33.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.66× (z +26.8) | — |
| [[NCI-H460 (line)]] | wt | 91.3 | 3 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.211× (z -13.9) |
| [[A-427 (line)]] | wt | 105 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.49× (z +8.8) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.309× (z -12.3) |
| [[CHP-212 (line)]] | wt | 471 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -15.0) |
| [[C32 (line)]] | wt | 89.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 177 | 1 | 3 | [[Harringtonine (drug)]] 5 µM 3.60× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.184× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 203 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -17.2) |
| [[SHP-77 (line)]] | alt | 349 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -17.2) |
| [[SK-MEL-2 (line)]] | alt | 34.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +10.9) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0723× (z -9.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 132 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.226× (z -12.2) |
| [[H4 (line)]] | wt | 223 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -13.5) |
| [[J82 (line)]] | alt | 39.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.3) | [[Belinostat (drug)]] 5 µM 0.245× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 23.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.87× (z +17.2) | — |
| [[HS-578T (line)]] | alt | 51.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 156 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.269× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 66.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +15.2) | — |
| [[Panc 03.27 (line)]] | alt | 24.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 30.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +16.4) | — |
| [[RPMI-7951 (line)]] | alt | 39.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +9.8) | — |
| [[A-172 (line)]] | wt | 5.60 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.37 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.54 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.92 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.48 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.37 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.06 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7755), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS35L]] | +0.73 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[TENM3-AS1]] | +0.72 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[ARHGAP15]] | +0.71 | +0.73 / +0.37 | both halves | 8e-05 |  |
| [[FLRT2]] | +0.71 | +0.72 / +0.45 | both halves | 3e-05 |  |
| [[MAGI2-AS3]] | +0.70 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[ANKRD18B]] | +0.70 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[FAP]] | +0.69 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[ARHGAP24]] | +0.68 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[BAZ2B]] | +0.68 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[CNTLN]] | +0.67 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[TCF12]] | +0.67 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.67 | +0.62 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1]] | -0.70 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[MPG]] | -0.70 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[LCMT1]] | -0.69 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[SDHAP2]] | -0.68 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[NBPF3]] | -0.67 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[YIF1B]] | -0.66 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[TMEM120B]] | -0.66 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[MFSD9]] | -0.65 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[MKRN2]] | -0.65 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[RNF216P1]] | -0.64 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[THOC3]] | -0.64 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[MAST3]] | -0.64 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 3, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLMN]] | B | CLMN activity lowers CACNA2D1's level | lines that do not express CLMN (7) vs lines expressing it (43) | 3.62× higher at baseline in the lines without CLMN | 0.008 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers CACNA2D1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZFPM2]] | B | ZFPM2 activity raises CACNA2D1's level | lines that do not express ZFPM2 (15) vs lines expressing it (35) | 3.75× lower at baseline in the lines without ZFPM2 | 0.099 | ⚠ within organs, on part of the lines; also absent: ZNF883, EVC, TRIM9; maybe low, not absent |
| [[LINC00882]] | C | LINC00882 activity raises CACNA2D1's level | lines that do not express LINC00882 (17) vs lines expressing it (33) | 5.08× lower at baseline in the lines without LINC00882 | 0.023 | ⚠ within organs, on part of the lines; also absent: TUSC3, B3GALT1, EVC; co-absent with the target |
| [[BNC2]] | C | BNC2 activity raises CACNA2D1's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 4.70× lower at baseline in the lines without BNC2 | 0.026 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182; co-absent with the target |
| [[LINC03041]] | C | LINC03041 activity raises CACNA2D1's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 6.76× lower at baseline in the lines without LINC03041 | 0.030 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent; co-absent with the target |
| [[CTNNA3]] | C | CTNNA3 activity lowers CACNA2D1's level | lines that do not express CTNNA3 (4) vs lines expressing it (46) | 2.03× higher at baseline in the lines without CTNNA3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL10, MYO15B; maybe low, not absent; its own permutation p |
| [[FBN2]] | C | FBN2 activity raises CACNA2D1's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 4.45× lower at baseline in the lines without FBN2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent; co-absent with the target |
| [[MAGI2-AS3]] | C | MAGI2-AS3 activity raises CACNA2D1's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 3.44× lower at baseline in the lines without MAGI2-AS3 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[MPDZ]] | C | MPDZ activity raises CACNA2D1's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 6.40× lower at baseline in the lines without MPDZ | 0.084 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1; co-absent with the target |
| [[NLGN1]] | C | NLGN1 activity raises CACNA2D1's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 4.63× lower at baseline in the lines without NLGN1 | 0.096 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[ZFHX4]] | C | ZFHX4 activity raises CACNA2D1's level | lines that do not express ZFHX4 (23) vs lines expressing it (27) | 5.00× lower at baseline in the lines without ZFHX4 | 0.097 | ⚠ within organs, on part of the lines; also absent: SNCA, UCHL1, SLITRK5; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 9, C 8. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFAP54]] | B | CACNA2D1 activity raises CFAP54's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 1.85× lower at baseline in the lines without CACNA2D1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[ZNF474]] | B | CACNA2D1 activity raises ZNF474's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 1.56× lower at baseline in the lines without CACNA2D1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[MFSD1]] | B | CACNA2D1 activity raises MFSD1's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 1.47× lower at baseline in the lines without CACNA2D1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[ATP10D]] | B | CACNA2D1 activity raises ATP10D's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without CACNA2D1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[RIPK2-DT]] | B | CACNA2D1 activity raises RIPK2-DT's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 1.54× lower at baseline in the lines without CACNA2D1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[STARD4-AS1]] | B | CACNA2D1 activity raises STARD4-AS1's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 1.55× lower at baseline in the lines without CACNA2D1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[KLHL5]] | B | CACNA2D1 activity raises KLHL5's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 2.76× lower at baseline in the lines without CACNA2D1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[TRHDE]] | B | CACNA2D1 activity raises TRHDE's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 2.04× lower at baseline in the lines without CACNA2D1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[HIVEP1]] | B | CACNA2D1 activity lowers HIVEP1's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 1.12× higher at baseline in the lines without CACNA2D1 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[MPDZ]] | C | CACNA2D1 activity raises MPDZ's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 6.31× lower at baseline in the lines without CACNA2D1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169; co-absent with the target |
| [[NLGN1]] | C | CACNA2D1 activity raises NLGN1's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 5.19× lower at baseline in the lines without CACNA2D1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169; co-absent with the target |
| [[FAT4]] | C | CACNA2D1 activity raises FAT4's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 5.36× lower at baseline in the lines without CACNA2D1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169; co-absent with the target |

## Where it sits

- **Module**: [[Module 202]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.845). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.6, 24.3); signed map (44.2, 24.7). **Vector** length 113, 37.2% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.4 | +18.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.6 | +3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.4 | +5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.9 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +8.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +2.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.9 | -16.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.4 | -15.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -15.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | -6.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel auxiliary subunit alpha2delta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.11 — chr7:81,946,444-82,443,956 (-) |
| Ensembl biotype | protein_coding |
| Also known as | lncRNA-N3, alpha2delta-1; previously CACNL2A, CACNA2, MHS3, LINC01112 |
| Gene groups (HGNC) | Calcium voltage-gated channel auxiliary alpha2delta subunits |
| Reactome | 6 pathways, smallest: Presynaptic depolarization and calcium channel opening; Mechanical load activates signaling by PIEZO1 and integrins in osteocytes; Cellular responses to mechanical stimuli |
| Matched by | ensembl_id |

**Function**, from UniProt [P54289](https://www.uniprot.org/uniprotkb/P54289) (Voltage-dependent calcium channel subunit alpha-2/delta-1):

> The alpha-2/delta subunit of voltage-dependent calcium channels regulates calcium current density and activation/inactivation kinetics of the calcium channel. Plays an important role in excitation-contraction coupling (By similarity).

**Summary**, from NCBI Gene [781](https://www.ncbi.nlm.nih.gov/gene/781):

> The preproprotein encoded by this gene is cleaved into multiple chains that comprise the alpha-2 and delta subunits of the voltage-dependent calcium channel complex. Calcium channels mediate the influx of calcium ions into the cell upon membrane polarization. Mutations in this gene can cause cardiac deficiencies, including Brugada syndrome and short QT syndrome. Alternate splicing results in multiple transcript variants, some of which may lack the delta subunit portion. [provided by RefSeq, Nov …

**Accessions** — [HGNC:1399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1399) · Entrez [781](https://www.ncbi.nlm.nih.gov/gene/781) · UniProt [P54289](https://www.uniprot.org/uniprotkb/P54289) · Ensembl [ENSG00000153956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153956)

## Data

Gene col 7755: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7755); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7755, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7755]; `tensor/DDL_lfc|DDL_z.npy` [7755]; `embed/gene_vectors.npy` [7755]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7755 or target_col == 7755). Every well: [[CACNA2D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNA2D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
