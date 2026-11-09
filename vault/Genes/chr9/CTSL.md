---
symbol: "CTSL"
type: "gene"
col: 5640
ensembl_id: "ENSG00000135047"
name: "cathepsin L"
location: "9q21.33"
module: 81
arm: "+"
pooled_cpm: 68.17
n_lines_expressing: 41
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# CTSL

*cathepsin L* — 9q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.42× (z +13.0, q 1e-35, up in 39 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.64× (z +5.2, q 3e-05, up in 27 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (C-33 A 21.9×, RKO 5.42×, NCI-H1792 8.03×, A498 3.51×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1792 9.15×, HEC-1-A 5.01×, HOP62 6.10×, A498 2.97×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 4.74×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (AsPC-1 4.33×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.310× (z -17.4, q 0e+00, down in 34 of 38 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA2-AS1]] (+0.58, fdr 2e-05), [[PNP]] (+0.54, fdr 2e-05), [[LUCAT1]] (+0.52, fdr 2e-05); moves opposite to [[CYC1]] (-0.44, fdr 2e-04), [[CKB]] (-0.43, fdr 1e-04), [[PHGR1]] (-0.43, fdr 2e-04).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ITGB1-DT]] → it (grade B ⚠); 8 go from it, the strongest it → [[FXYD5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5640.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (C-33 A 21.9×, RKO 5.42×, NCI-H1792 8.03×, A498 3.51×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1792 9.15×, HEC-1-A 5.01×, HOP62 6.10×, A498 2.97×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 4.74×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (AsPC-1 4.33×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.42×** | +13.0 | 1e-35 | 39/39 (C-33 A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.05×** | +11.3 | 3e-27 | 25/32 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +7.6 | 7e-12 | 27/33 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +5.2 | 3e-05 | 27/39 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.016 | 21/39 (A-172, RPMI-7951, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +3.5 | 0.043 | 22/38 (HS-578T, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here); position effect removed |
| [[Darinaparsin (drug)]] 5 µM |  | 1.24× | +3.2 | 0.10 | 19/39 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.37× | +3.2 | 0.11 | 19/41 (SNU-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.23× | +3.1 | 0.14 | 16/39 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5640.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.310×** | -17.4 | 0e+00 | 34/38 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.484×** | -7.6 | 6e-12 | 35/39 (A549, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.533×** | -6.6 | 7e-09 | 25/38 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.537×** | -6.5 | 8e-09 | 31/39 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.525×** | -6.5 | 8e-09 | 32/39 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.569×** | -5.9 | 3e-07 | 31/39 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.592×** | -5.5 | 3e-06 | 30/39 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.601×** | -5.4 | 6e-06 | 32/39 (J82, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.595×** | -5.3 | 9e-06 | 26/40 (A498, NCI-H2030, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.619×** | -5.1 | 2e-05 | 23/39 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.461×** | -4.3 | 0.001 | 25/38 (SK-MEL-2, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.755×** | -4.2 | 0.001 | 27/40 (CFPAC-1, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.686×** | -4.0 | 0.003 | 23/39 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.491×** | -3.9 | 0.004 | 19/40 (A-427, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.704×** | -3.7 | 0.008 | 12/38 (SNU-423, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.523×** | -3.6 | 0.012 | 20/39 (Hs 766T, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5640. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 134 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -17.9) |
| [[A549 (line)]] | wt | 156 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -20.2) |
| [[NCI-H1573 (line)]] | alt | 110 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0857× (z -19.0) |
| [[NCI-H1792 (line)]] | alt | 32.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 9.15× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -8.6) |
| [[RKO (line)]] | wt | 91.1 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 60.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 32.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.01× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 62.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 61.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -16.9) |
| [[NCI-H460 (line)]] | wt | 357 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0623× (z -31.6) |
| [[PANC-1 (line)]] | alt | 21.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 127 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0715× (z -25.1) |
| [[A-172 (line)]] | wt | 81.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -14.3) |
| [[AsPC-1 (line)]] | alt | 45.2 | 1 | 1 | [[Auranofin (drug)]] 5 µM 4.33× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -13.3) |
| [[C32 (line)]] | wt | 66.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -13.9) |
| [[H4 (line)]] | wt | 30.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.76× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.7) |
| [[HOP62 (line)]] | alt | 24.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.10× (z +10.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 75.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.0) |
| [[J82 (line)]] | alt | 105 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -14.2) |
| [[LOX-IMVI (line)]] | wt | 22.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.69× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 190 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -21.6) |
| [[NCI-H23 (line)]] | alt | 86.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -19.6) |
| [[SNU-423 (line)]] | alt | 78.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -13.9) |
| [[SW 900 (line)]] | alt | 24.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.83× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 23.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +9.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 31.3 | 0 | 1 | — | [[Roxadustat (drug)]] 5 µM 0.0625× (z -8.7) |
| [[C-33 A (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 21.9× (z +13.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 48.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 32.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 98.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -21.2) |
| [[SNU-1 (line)]] | wt | 25.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -11.4) |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.57 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.87 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 12.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5640), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA2-AS1]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[PNP]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[LUCAT1]] | +0.52 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[MMP1]] | +0.51 | +0.44 / +0.56 | both halves | 3e-05 | pathway: Collagen degradation |
| [[NIT1]] | +0.50 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[BMP6]] | +0.50 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[C9orf72]] | +0.49 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[OSMR-DT]] | +0.49 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[IL13RA2]] | +0.48 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[TMEM255B]] | +0.48 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[ITGA2]] | +0.47 | +0.44 / +0.48 | both halves | 3e-05 | pathway: Extracellular matrix organization |
| [[HCG20]] | +0.46 | +0.23 / +0.50 | both halves | 5e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYC1]] | -0.44 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[CKB]] | -0.43 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[PHGR1]] | -0.43 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[ZNF652]] | -0.43 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[YEATS4]] | -0.41 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[ALDH3A1]] | -0.41 | -0.38 / -0.27 | both halves | 3e-04 |  |
| [[AJUBA]] | -0.40 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[PUM2]] | -0.39 | -0.24 / -0.37 | both halves | 5e-04 |  |
| [[CPLX2]] | -0.39 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[IMMP1L]] | -0.39 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[RBMS3]] | -0.39 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[HADH]] | -0.38 | -0.38 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB1-DT]] | B | ITGB1-DT activity raises CTSL's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 3.03× lower at baseline in the lines without ITGB1-DT | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[IL13RA2]] | B | IL13RA2 activity raises CTSL's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 2.56× lower at baseline in the lines without IL13RA2 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3 |
| [[STC1]] | B | STC1 activity raises CTSL's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.75× lower at baseline in the lines without STC1 | 0.0996 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[ROBO3]] | C | ROBO3 activity raises CTSL's level | lines that do not express ROBO3 (8) vs lines expressing it (42) | 3.92× lower at baseline in the lines without ROBO3 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, DYRK3, SCHIP1; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FXYD5]] | B | CTSL activity raises FXYD5's level | lines that do not express CTSL (9) vs lines expressing it (41) | 1.38× lower at baseline in the lines without CTSL | 0.004 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent |
| [[UBE2D1]] | B | CTSL activity raises UBE2D1's level | lines that do not express CTSL (9) vs lines expressing it (41) | 1.41× lower at baseline in the lines without CTSL | 0.017 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent |
| [[UPP1]] | B | CTSL activity raises UPP1's level | lines that do not express CTSL (9) vs lines expressing it (41) | 2.31× lower at baseline in the lines without CTSL | 0.021 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent |
| [[EFCAB13]] | B | CTSL activity raises EFCAB13's level | lines that do not express CTSL (9) vs lines expressing it (41) | 3.62× lower at baseline in the lines without CTSL | 0.046 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent |
| [[TMEM156]] | B | CTSL activity raises TMEM156's level | lines that do not express CTSL (9) vs lines expressing it (41) | 4.25× lower at baseline in the lines without CTSL | 0.073 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent |
| [[MAP1LC3B]] | B | CTSL activity raises MAP1LC3B's level | lines that do not express CTSL (9) vs lines expressing it (41) | 1.28× lower at baseline in the lines without CTSL | 0.087 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent |
| [[BCL2A1]] | B | CTSL activity raises BCL2A1's level | lines that do not express CTSL (9) vs lines expressing it (41) | 3.19× lower at baseline in the lines without CTSL | 0.097 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent |
| [[ROBO3]] | C | CTSL activity raises ROBO3's level | lines that do not express CTSL (9) vs lines expressing it (41) | 2.55× lower at baseline in the lines without CTSL | 0.055 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.487). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.9, 3.3); signed map (4.5, 47.6). **Vector** length 95.7, 25.2% of its response variance represented; |z| ≥ 3 in 1,088 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.9 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +3.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -17.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.8 | -3.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | cathepsin L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.33 — chr9:87,724,051-87,731,469 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31037; previously CTSL1 |
| Gene groups (HGNC) | Cathepsins; Elastases; Cysteine endopeptidases |
| Hallmark sets | COMPLEMENT |
| Reactome | 40 pathways, smallest: Attachment and Entry_9678110; RUNX1 regulates transcription of genes involved in differentiation of keratinocytes; Trafficking and processing of endosomal TLR |
| Matched by | ensembl_id |

**Function**, from UniProt [P07711](https://www.uniprot.org/uniprotkb/P07711) (Procathepsin L):

> Thiol protease important for the overall degradation of proteins in lysosomes (Probable). Plays a critical for normal cellular functions such as general protein turnover, antigen processing and bone remodeling. Involved in the solubilization of cross-linked TG/thyroglobulin and in the subsequent release of thyroid hormone thyroxine (T4) by limited proteolysis of TG/thyroglobulin in the thyroid follicle lumen (By similarity). In neuroendocrine chromaffin cells secretory vesicles, catalyzes the …

**Summary**, from NCBI Gene [1514](https://www.ncbi.nlm.nih.gov/gene/1514):

> The protein encoded by this gene is a lysosomal cysteine proteinase that plays a major role in intracellular protein catabolism. Its substrates include collagen and elastin, as well as alpha-1 protease inhibitor, a major controlling element of neutrophil elastase activity. The encoded protein has been implicated in several pathologic processes, including myofibril necrosis in myopathies and in myocardial ischemia, and in the renal tubular response to proteinuria. This protein, which is a member …

**Accessions** — [HGNC:2537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2537) · Entrez [1514](https://www.ncbi.nlm.nih.gov/gene/1514) · UniProt [P07711](https://www.uniprot.org/uniprotkb/P07711) · Ensembl [ENSG00000135047](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135047)

## Data

Gene col 5640: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5640); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5640, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5640]; `tensor/DDL_lfc|DDL_z.npy` [5640]; `embed/gene_vectors.npy` [5640]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5640 or target_col == 5640). Every well: [[CTSL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTSL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
