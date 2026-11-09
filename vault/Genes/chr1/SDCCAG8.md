---
symbol: "SDCCAG8"
type: "gene"
col: 607
ensembl_id: "ENSG00000054282"
name: "SHH signaling and ciliogenesis regulator SDCCAG8"
location: "1q43-q44"
module: 110
arm: "+"
pooled_cpm: 165.4
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 29
n_dd_up_clean: 8
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# SDCCAG8

*SHH signaling and ciliogenesis regulator SDCCAG8* — 1q43-q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.50× (z +7.5, q 3e-11, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.342× (z -19.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRY4-AS1]] (+0.52, fdr 2e-05), [[KIAA1549L]] (+0.52, fdr 4e-05), [[CEP170]] (+0.51, fdr 4e-04, ⚠ same locus), [[NLRP3]] (+0.50, fdr 5e-05); moves opposite to [[ABHD4]] (-0.49, fdr 5e-05), [[TBKBP1]] (-0.48, fdr 8e-05), [[MRAS]] (-0.47, fdr 4e-04).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[COL13A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 607.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +7.5 | 3e-11 | 32/48 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +5.6 | 7e-06 | 28/48 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.4 | 1e-05 | 27/48 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.2 | 2e-05 | 24/48 (A-427, C-33 A, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +5.0 | 6e-05 | 26/48 (A-172, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.019 | 24/48 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.026 | 25/50 (C-33 A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.061 | 9/49 (BT-474, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.3 | 0.061 | 15/48 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.061 | 19/48 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.087 | 17/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | 1.18× | +3.1 | 0.099 | 12/48 (MIA PaCa-2, AsPC-1, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.19× | +3.0 | 0.11 | 17/48 (A-172, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 607.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.342×** | -19.9 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.363×** | -18.8 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.364×** | -18.8 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.433×** | -15.5 | 0e+00 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.445×** | -14.4 | 4e-45 | 42/47 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.266×** | -12.9 | 7e-36 | 46/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.615×** | -12.8 | 2e-35 | 36/48 (A549, SNU-423, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.505×** | -12.7 | 6e-35 | 46/48 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.289×** | -12.1 | 1e-31 | 44/48 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.616×** | -8.6 | 4e-16 | 34/48 (A549, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.624×** | -8.4 | 2e-15 | 27/43 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.634×** | -8.1 | 2e-14 | 36/47 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.648×** | -8.0 | 4e-14 | 43/48 (PANC-1, HCT15, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.656×** | -7.8 | 2e-13 | 34/48 (LoVo, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.647×** | -7.6 | 1e-12 | 36/48 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.668×** | -6.4 | 4e-09 | 32/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.704×** | -5.6 | 7e-07 | 29/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.656×** | -4.1 | 0.001 | 26/48 (CFPAC-1, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.865× | -3.8 | 0.004 | 19/49 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.823×** | -3.6 | 0.007 | 20/48 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.766×** | -3.5 | 0.009 | 20/49 (SNU-423, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 607. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 187 | 0 | 19 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -30.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -28.2) |
| [[NCI-H460 (line)]] | wt | 219 | 0 | 17 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -21.0) |
| [[C32 (line)]] | wt | 271 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -20.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -13.5) |
| [[A549 (line)]] | wt | 199 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -25.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.428× (z -11.2) |
| [[SW480 (line)]] | alt | 159 | 0 | 14 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.209× (z -25.5) |
| [[H4 (line)]] | wt | 188 | 0 | 13 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -21.7) |
| [[A-172 (line)]] | wt | 303 | 3 | 9 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.43× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -16.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.220× (z -9.6) |
| [[SNU-423 (line)]] | alt | 210 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -21.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -17.4) |
| [[HOP62 (line)]] | alt | 159 | 0 | 11 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -17.8) |
| [[LoVo (line)]] | wt | 140 | 0 | 11 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.286× (z -17.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.364× (z -14.2) |
| [[HCT15 (line)]] | alt | 243 | 0 | 10 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.253× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 604 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -16.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.409× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 116 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -12.8) |
| [[J82 (line)]] | alt | 132 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -17.7) |
| [[NCI-H1792 (line)]] | alt | 138 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -12.3) |
| [[A-427 (line)]] | wt | 109 | 4 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.229× (z -10.5) |
| [[A498 (line)]] | wt | 157 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -16.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.223× (z -8.6) |
| [[COLO 205 (line)]] | alt | 134 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.353× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 151 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.272× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -14.9) |
| [[LS 180 (line)]] | wt | 104 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.243× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 145 | 1 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.410× (z -10.4) |
| [[SW 900 (line)]] | alt | 131 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.285× (z -11.9) |
| [[BT-474 (line)]] | alt | 238 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -15.2) |
| [[HT-29 (line)]] | alt | 73.3 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 388 | 0 | 5 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.653× (z -13.9) ⚠ position not correctable · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.391× (z -9.0) |
| [[CHP-212 (line)]] | wt | 215 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -10.2) |
| [[Hs 766T (line)]] | wt | 278 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.326× (z -12.4) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.450× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 100 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.449× (z -9.5) |
| [[RKO (line)]] | wt | 70.9 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -15.5) ⚠ toxic · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.309× (z -8.5) |
| [[AN3 CA (line)]] | alt | 110 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.140× (z -12.2) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.204× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 153 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -13.6) |
| [[HS-578T (line)]] | alt | 89.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.367× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 162 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.258× (z -11.2) |
| [[KATO III (line)]] | alt | 81.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -11.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.399× (z -10.6) |
| [[SHP-77 (line)]] | alt | 83.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.291× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 176 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -16.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.151× (z -9.8) |
| [[SW1417 (line)]] | alt | 75.1 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.347× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 113 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.231× (z -9.1) |
| [[SNU-1 (line)]] | wt | 64.9 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.241× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 68.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.222× (z -10.3) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.374× (z -9.4) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 242 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -11.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 607), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRY4-AS1]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[KIAA1549L]] | +0.52 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[CEP170]] | +0.51 | +0.25 / +0.59 | both halves | 4e-04 | same gene group; STRING 463; ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[NLRP3]] | +0.50 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[BCL2A1]] | +0.50 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[ARHGAP22]] | +0.49 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[UACA]] | +0.49 | +0.37 / +0.48 | both halves | 7e-05 |  |
| [[RASA2]] | +0.48 | +0.21 / +0.48 | both halves | 7e-04 |  |
| [[LRRC8C]] | +0.48 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[PHC2]] | +0.48 | +0.35 / +0.49 | both halves | 1e-04 | same gene group |
| [[ZEB1]] | +0.48 | +0.27 / +0.55 | both halves | 3e-04 |  |
| [[HMGA2]] | +0.47 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[LINC01812]] | +0.47 | +0.42 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD4]] | -0.49 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[TBKBP1]] | -0.48 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[MRAS]] | -0.47 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[RARG]] | -0.46 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[FGF2]] | -0.44 | -0.21 / -0.50 | both halves | 7e-04 |  |
| [[ZBTB7B]] | -0.43 | -0.47 / -0.43 | both halves | 4e-05 |  |
| [[EPHA5-AS1]] | -0.42 | -0.29 / -0.37 | both halves | 3e-04 |  |
| [[MSI1]] | -0.42 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[GNAI1]] | -0.42 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[ZSCAN31]] | -0.42 | -0.29 / -0.41 | both halves | 3e-04 |  |
| [[CASP7]] | -0.41 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[ARMCX6]] | -0.41 | -0.38 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL13A1]] | B | COL13A1 activity raises SDCCAG8's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 1.87× lower at baseline in the lines without COL13A1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[ANGPTL4]] | B | ANGPTL4 activity raises SDCCAG8's level | lines that do not express ANGPTL4 (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without ANGPTL4 | 0.067 | ⚠ within organs, on part of the lines; also absent: CLDN14-AS1, LGALS1, EBI3 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SDCCAG8's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SDCCAG8's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.441). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.8, 6.1); signed map (12.0, 48.3). **Vector** length 97.8, 35.1% of its response variance represented; |z| ≥ 3 in 1,646 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +5.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | +3.0 | -0.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.7 | +7.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.8 | +3.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.9 | -8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.2 | -3.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -1.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -8.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -7.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.8 | +0.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.8 | +0.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.6 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | SHH signaling and ciliogenesis regulator SDCCAG8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43-q44 — chr1:243,256,034-243,500,091 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NY-CO-8, CCCAP, SLSN7, NPHP10, BBS16 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Centriolar satellite proteins |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SQ7](https://www.uniprot.org/uniprotkb/Q86SQ7) (Serologically defined colon cancer antigen 8):

> Plays a role in the establishment of cell polarity and epithelial lumen formation (By similarity). Also plays an essential role in ciliogenesis and subsequent Hedgehog signaling pathway that requires the presence of intact primary cilia for pathway activation. Mechanistically, interacts with and mediates RABEP2 centrosomal localization which is critical for ciliogenesis.

**Summary**, from NCBI Gene [10806](https://www.ncbi.nlm.nih.gov/gene/10806):

> This gene encodes a centrosome associated protein. This protein may be involved in organizing the centrosome during interphase and mitosis. Mutations in this gene are associated with retinal-renal ciliopathy. [provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:10671](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10671) · Entrez [10806](https://www.ncbi.nlm.nih.gov/gene/10806) · UniProt [Q86SQ7](https://www.uniprot.org/uniprotkb/Q86SQ7) · Ensembl [ENSG00000054282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054282)

## Data

Gene col 607: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 607); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 607, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 607]; `tensor/DDL_lfc|DDL_z.npy` [607]; `embed/gene_vectors.npy` [607]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 607 or target_col == 607). Every well: [[SDCCAG8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDCCAG8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
