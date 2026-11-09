---
symbol: "HOOK2"
type: "gene"
col: 1735
ensembl_id: "ENSG00000095066"
name: "hook microtubule tethering protein 2"
location: "19p13.13"
module: 59
arm: "+"
pooled_cpm: 55.33
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# HOOK2

*hook microtubule tethering protein 2* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +17.2, q 0e+00, up in 38 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.543× (z -9.1, q 4e-17, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VASN]] (+0.63, fdr 7e-06), [[HSPA2-AS1]] (+0.62, fdr 7e-06), [[CBX4]] (+0.62, fdr 7e-06); moves opposite to [[SLC35B4]] (-0.62, fdr 1e-05), [[HERC2P9-1]] (-0.60, fdr 3e-05), [[HERC2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PRKCH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1735.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +17.2 | 0e+00 | 38/49 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +7.7 | 4e-12 | 35/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +5.9 | 5e-07 | 27/48 (SNU-423, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.7 | 2e-06 | 34/49 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +5.6 | 2e-06 | 30/48 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +5.2 | 2e-05 | 25/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +4.9 | 6e-05 | 25/44 (HS-578T, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.8 | 1e-04 | 26/46 (HS-578T, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.5 | 4e-04 | 26/46 (RKO, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +4.1 | 0.003 | 25/46 (SW480, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.004 | 21/48 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.044 | 16/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.082 | 15/48 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.1 | 0.084 | 15/47 (hTERT-HPNE, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1735.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.543×** | -9.1 | 4e-17 | 40/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.637×** | -6.8 | 4e-09 | 29/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.690×** | -5.5 | 5e-06 | 33/47 (PANC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.692×** | -5.5 | 5e-06 | 28/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.714×** | -5.0 | 6e-05 | 27/48 (COLO 205, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.574×** | -4.3 | 0.001 | 30/48 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.751×** | -4.3 | 0.001 | 23/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.756×** | -4.0 | 0.004 | 24/47 (PANC-1, SW 1271, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.764×** | -4.0 | 0.004 | 25/47 (NCI-H23, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.767×** | -4.0 | 0.004 | 23/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.765×** | -3.8 | 0.006 | 22/47 (HCT15, H4, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.836× | -3.8 | 0.007 | 13/49 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.777×** | -3.8 | 0.007 | 22/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.777×** | -3.8 | 0.007 | 24/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.791×** | -3.5 | 0.017 | 20/48 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.781×** | -3.5 | 0.017 | 23/48 (COLO 205, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.794×** | -3.4 | 0.019 | 23/48 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.795×** | -3.4 | 0.020 | 21/48 (LS 180, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.821×** | -2.9 | 0.095 | 12/47 (C32, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1735. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 42.4 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.8) | [[Digitoxin (drug)]] 0.5 µM 0.331× (z -11.1) |
| [[HCT15 (line)]] | alt | 250 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.352× (z -10.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.528× (z -9.2) |
| [[HS-578T (line)]] | alt | 30.8 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +13.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.3 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.267× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.323× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 38.1 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +12.7) | [[Digitoxin (drug)]] 5 µM 0.232× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.261× (z -9.9) |
| [[A-427 (line)]] | wt | 57.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 33.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 35.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -8.7) |
| [[SNU-423 (line)]] | alt | 49.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.5) | — |
| [[A498 (line)]] | wt | 35.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.1) | — |
| [[C32 (line)]] | wt | 36.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 31.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -9.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 34.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 24.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +12.2) | — |
| [[Hs 766T (line)]] | wt | 54.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 61.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 40.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 54.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 41.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +14.5) | — |
| [[RKO (line)]] | wt | 28.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.37× (z +8.5) ⚠ toxic | — |
| [[RPMI-7951 (line)]] | alt | 39.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 44.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +10.7) | — |
| [[SW48 (line)]] | wt | 106 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.7) | — |
| [[A-172 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 102 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 80.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 64.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1735), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VASN]] | +0.63 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CBX4]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TTC36-AS1]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[KMT2E]] | +0.61 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[CA11]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[DBP]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[IST1]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[FAM117A]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CHMP3-AS1]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[NDUFV2-AS1]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[GLIS2]] | +0.57 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35B4]] | -0.62 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[HERC2P9-1]] | -0.60 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[HERC2]] | -0.60 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[MTOR]] | -0.59 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[ELAC2]] | -0.58 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.58 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[CCT5]] | -0.57 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[MRPS27]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ICMT]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[GOT2]] | -0.56 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[WDR77]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[EXOC2]] | -0.55 | -0.59 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKCH]] | B | PRKCH activity raises HOOK2's level | lines that do not express PRKCH (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without PRKCH | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000258989, ENSG00000284686, APBA1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (11.4, 30.8); signed map (-4.7, 13.3). **Vector** length 107, 30.1% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +5.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +1.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.2 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -4.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.4 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | hook microtubule tethering protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,763,003-12,872,740 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HK2 |
| Gene groups (HGNC) | FHF complex; HOOK family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96ED9](https://www.uniprot.org/uniprotkb/Q96ED9) (Protein Hook homolog 2):

> Component of the FTS/Hook/FHIP complex (FHF complex). The FHF complex may function to promote vesicle trafficking and/or fusion via the homotypic vesicular protein sorting complex (the HOPS complex). Contributes to the establishment and maintenance of centrosome function. May function in the positioning or formation of aggresomes, which are pericentriolar accumulations of misfolded proteins, proteasomes and chaperones. FHF complex promotes the distribution of AP-4 complex to the perinuclear …

**Summary**, from NCBI Gene [29911](https://www.ncbi.nlm.nih.gov/gene/29911):

> Hook proteins are cytosolic coiled-coil proteins that contain conserved N-terminal domains, which attach to microtubules, and more divergent C-terminal domains, which mediate binding to organelles. The Drosophila Hook protein is a component of the endocytic compartment.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:19885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19885) · Entrez [29911](https://www.ncbi.nlm.nih.gov/gene/29911) · UniProt [Q96ED9](https://www.uniprot.org/uniprotkb/Q96ED9) · Ensembl [ENSG00000095066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095066)

## Data

Gene col 1735: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1735); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1735, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1735]; `tensor/DDL_lfc|DDL_z.npy` [1735]; `embed/gene_vectors.npy` [1735]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1735 or target_col == 1735). Every well: [[HOOK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOOK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
