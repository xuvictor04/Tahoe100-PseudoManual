---
symbol: "TNIK"
type: "gene"
col: 7798
ensembl_id: "ENSG00000154310"
name: "TRAF2 and NCK interacting kinase"
location: "3q26.2-q26.31"
module: 46
arm: "-"
pooled_cpm: 159.75
n_lines_expressing: 39
n_dd_up: 6
n_dd_down: 33
n_dd_up_clean: 6
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 9
direction_downstream: 13
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# TNIK

*TRAF2 and NCK interacting kinase* — 3q26.2-q26.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.54× (z +12.5, q 6e-33, up in 29 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.466× (z -15.5, q 0e+00, down in 27 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.517× (z -13.4, q 8e-39, down in 32 of 37 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLNB]] (+0.59, fdr 1e-05), [[ST3GAL1]] (+0.58, fdr 1e-05), [[PKP2]] (+0.57, fdr 3e-05); moves opposite to [[FBXW4]] (-0.66, fdr 1e-05), [[DDX59]] (-0.60, fdr 3e-05), [[ZDHHC1]] (-0.59, fdr 3e-05).
> It sits in the **-** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TINAGL1]] → it (grade B ⚠); 13 go from it, the strongest it → [[TNS4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7798.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +12.5 | 6e-33 | 29/37 (HS-578T, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +9.5 | 4e-19 | 24/38 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +8.8 | 2e-16 | 24/37 (NCI-H1573, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +5.6 | 2e-06 | 20/37 (SK-MEL-2, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.004 | 21/38 (NCI-H1573, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.049 | 13/37 (C32, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.049 | 16/37 (NCI-H1573, NCI-H2030, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.3 | 0.079 | 12/37 (HOP62, HS-578T, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.079 | 9/37 (HEC-1-A, C32, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7798.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.466×** | -15.5 | 0e+00 | 27/38 (C32, LS 180, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.450×** | -15.0 | 0e+00 | 26/34 (C32, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -14.4 | 7e-45 | 24/33 (RPMI-7951, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.492×** | -13.8 | 2e-41 | 30/36 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.517×** | -13.4 | 8e-39 | 32/37 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.544×** | -11.9 | 2e-30 | 27/37 (RKO, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.557×** | -11.8 | 2e-30 | 32/37 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.639×** | -9.1 | 8e-18 | 29/37 (RKO, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.655×** | -8.6 | 7e-16 | 26/37 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.660×** | -8.4 | 2e-15 | 26/37 (C-33 A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.745×** | -8.4 | 2e-15 | 23/38 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.674×** | -8.0 | 7e-14 | 26/37 (LoVo, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.681×** | -7.8 | 3e-13 | 27/37 (C32, LoVo, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -7.4 | 8e-12 | 29/37 (C32, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.778×** | -7.2 | 3e-11 | 21/37 (RKO, C32, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.717×** | -6.7 | 6e-10 | 24/37 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.754×** | -5.7 | 3e-07 | 21/37 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.769×** | -5.3 | 3e-06 | 20/37 (HT-29, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.776×** | -5.1 | 8e-06 | 22/37 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -4.9 | 3e-05 | 20/39 (C32, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7798. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 226 | 0 | 43 (9 ⚠) | — | [[Afatinib (drug)]] 0.5 µM 0.112× (z -17.2) |
| [[C32 (line)]] | wt | 609 | 0 | 18 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -27.4) |
| [[J82 (line)]] | alt | 375 | 1 (1 ⚠) | 14 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.32× (z +8.9) ⚠ cell-cycle shift, explains ~74% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -25.0) |
| [[NCI-H1792 (line)]] | alt | 266 | 0 | 14 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.245× (z -16.5) |
| [[RKO (line)]] | wt | 143 | 0 | 11 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0467× (z -30.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.237× (z -21.4) |
| [[KATO III (line)]] | alt | 615 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -18.7) |
| [[SNU-423 (line)]] | alt | 228 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -14.4) |
| [[SW480 (line)]] | alt | 399 | 0 | 10 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.280× (z -18.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -15.0) |
| [[CFPAC-1 (line)]] | alt | 160 | 1 | 8 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.79× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.291× (z -13.1) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.368× (z -11.1) |
| [[LoVo (line)]] | wt | 145 | 0 | 9 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -17.9) |
| [[A498 (line)]] | wt | 113 | 0 | 8 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.285× (z -15.8) |
| [[Hs 766T (line)]] | wt | 146 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -14.7) |
| [[HT-29 (line)]] | alt | 166 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.328× (z -13.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.466× (z -9.7) |
| [[LS 180 (line)]] | wt | 299 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.635× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 225 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 178 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0902× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.339× (z -11.0) |
| [[SW 900 (line)]] | alt | 169 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.336× (z -13.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -9.2) |
| [[COLO 205 (line)]] | alt | 300 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.412× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.455× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 348 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -14.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 150 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.11× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 50.0 | 2 | 2 | [[Panobinostat (drug)]] 0.05 µM 3.06× (z +10.3) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.356× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 46.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 244 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -14.4) |
| [[A-172 (line)]] | wt | 98.4 | 1 (1 ⚠) | 2 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.36× (z +9.3) ⚠ unreliable plate only | [[Harringtonine (drug)]] 0.5 µM 0.406× (z -9.7) |
| [[A549 (line)]] | wt | 43.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.8) |
| [[H4 (line)]] | wt | 58.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.178× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 279 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.370× (z -10.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.6) |
| [[HS-578T (line)]] | alt | 59.7 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.67× (z +13.9) | — |
| [[SW48 (line)]] | wt | 157 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -14.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 49.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.188× (z -11.4) |
| [[CHP-212 (line)]] | wt | 72.9 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.161× (z -9.6) |
| [[HCT15 (line)]] | alt | 73.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.280× (z -8.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 34.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.6 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 31.6 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 34.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 214 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7798), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLNB]] | +0.59 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[ST3GAL1]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[PKP2]] | +0.57 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[KRT18]] | +0.56 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[ZFYVE28]] | +0.55 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[LAMA3]] | +0.55 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[LANCL3]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[TRIB2]] | +0.54 | +0.59 / +0.45 | both halves | 3e-05 | same gene group |
| [[FCHO1]] | +0.53 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[HK1]] | +0.53 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[SHB]] | +0.53 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[GALNT18]] | +0.53 | +0.48 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW4]] | -0.66 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[DDX59]] | -0.60 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[ZDHHC1]] | -0.59 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[STRIP1]] | -0.58 | -0.50 / -0.49 | both halves | 1e-05 | STRING 486 |
| [[BICRAL]] | -0.56 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ENTPD3-AS1]] | -0.56 | -0.60 / -0.28 | both halves | 3e-04 |  |
| [[TBC1D22B]] | -0.55 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[FAIM]] | -0.54 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[RC3H2]] | -0.53 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[IDNK]] | -0.53 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[DHRS12]] | -0.52 | -0.55 / -0.32 | both halves | 1e-04 |  |
| [[RNF146]] | -0.52 | -0.52 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TINAGL1]] | B | TINAGL1 activity raises TNIK's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 3.27× lower at baseline in the lines without TINAGL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[TNS4]] | B | TNS4 activity raises TNIK's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 2.50× lower at baseline in the lines without TNS4 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[KRT19]] | B | KRT19 activity raises TNIK's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.36× lower at baseline in the lines without KRT19 | 0.034 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[LAMA3]] | B | LAMA3 activity raises TNIK's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.71× lower at baseline in the lines without LAMA3 | 0.057 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TNIK's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TNIK's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PPARG]] | B | PPARG activity raises TNIK's level | lines that do not express PPARG (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without PPARG | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[ST3GAL1]] | B | ST3GAL1 activity raises TNIK's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.58× lower at baseline in the lines without ST3GAL1 | 0.0995 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[FLNB]] | C | FLNB activity raises TNIK's level | lines that do not express FLNB (3) vs lines expressing it (47) | 7.10× lower at baseline in the lines without FLNB | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNS4]] | B | TNIK activity raises TNS4's level | lines that do not express TNIK (11) vs lines expressing it (39) | 3.42× lower at baseline in the lines without TNIK | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |
| [[PPP3CA]] | B | TNIK activity weakens PPP3CA's drug response | lines that do not express TNIK (11) vs lines expressing it (38) | the lines without TNIK respond 1.10× as strongly (z diff -0.08); strongest at Panobinostat 5 µM: 1.63x vs 1.22x (z diff -3.7) | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE; target measured in part of the lines; both ways; artifact flags |
| [[ST3GAL1]] | B | TNIK activity raises ST3GAL1's level | lines that do not express TNIK (11) vs lines expressing it (39) | 2.46× lower at baseline in the lines without TNIK | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |
| [[SLC1A1]] | B | TNIK activity raises SLC1A1's level | lines that do not express TNIK (11) vs lines expressing it (39) | 2.72× lower at baseline in the lines without TNIK | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |
| [[LAMA3]] | B | TNIK activity raises LAMA3's level | lines that do not express TNIK (11) vs lines expressing it (39) | 2.86× lower at baseline in the lines without TNIK | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |
| [[TGFA]] | B | TNIK activity raises TGFA's level | lines that do not express TNIK (11) vs lines expressing it (39) | 3.01× lower at baseline in the lines without TNIK | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |
| [[TINAGL1]] | B | TNIK activity raises TINAGL1's level | lines that do not express TNIK (11) vs lines expressing it (39) | 3.46× lower at baseline in the lines without TNIK | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |
| [[FLNB]] | B | TNIK activity raises FLNB's level | lines that do not express TNIK (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without TNIK | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |
| [[ETHE1]] | B | TNIK activity raises ETHE1's level | lines that do not express TNIK (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without TNIK | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |
| [[SH3GL3]] | B | TNIK activity raises SH3GL3's level | lines that do not express TNIK (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without TNIK | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |
| [[PKP2]] | B | TNIK activity raises PKP2's level | lines that do not express TNIK (11) vs lines expressing it (39) | 2.10× lower at baseline in the lines without TNIK | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |
| [[TRAF3IP2-AS1]] | B | TNIK activity weakens TRAF3IP2-AS1's drug response | lines that do not express TNIK (11) vs lines expressing it (37) | the lines without TNIK respond 1.37× as strongly (z diff -1.65); rises at some drug-doses, falls at others (25% from rises): Belinostat 5 µM: 0.28x vs 0.44x (z diff -2.8); Panobinostat 0.5 µM: 0.28x vs 0.40x (z diff -2.3); Ouabain (Octahydrate) 5 µM: 2.46x vs 1.94x (z diff -1.9) | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **-** arm (projection on the module's main direction -0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.4, 16.0); signed map (3.6, 52.1). **Vector** length 117, 34.1% of its response variance represented; |z| ≥ 3 in 1,464 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +12.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.3 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +9.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.0 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +4.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +0.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.1 | -13.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.6 | -5.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -7.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.2 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | TRAF2 and NCK interacting kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.2-q26.31 — chr3:171,058,414-171,460,408 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAP4K7, KIAA0551 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; MAP4K family (GCK-IV subfamily) |
| Reactome | 4 pathways, smallest: Oxidative Stress Induced Senescence; Cellular Senescence; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKE5](https://www.uniprot.org/uniprotkb/Q9UKE5) (TRAF2 and NCK-interacting protein kinase):

> Serine/threonine kinase that acts as an essential activator of the Wnt signaling pathway. Recruited to promoters of Wnt target genes and required to activate their expression. May act by phosphorylating TCF4/TCF7L2. Appears to act upstream of the JUN N-terminal pathway. May play a role in the response to environmental stress. Part of a signaling complex composed of NEDD4, RAP2A and TNIK which regulates neuronal dendrite extension and arborization during development. More generally, it may play …

**Summary**, from NCBI Gene [23043](https://www.ncbi.nlm.nih.gov/gene/23043):

> Wnt signaling plays important roles in carcinogenesis and embryonic development. The protein encoded by this gene is a serine/threonine kinase that functions as an activator of the Wnt signaling pathway. Mutations in this gene are associated with an autosomal recessive form of cognitive disability. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:30765](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30765) · Entrez [23043](https://www.ncbi.nlm.nih.gov/gene/23043) · UniProt [Q9UKE5](https://www.uniprot.org/uniprotkb/Q9UKE5) · Ensembl [ENSG00000154310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154310)

## Data

Gene col 7798: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7798); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7798, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7798]; `tensor/DDL_lfc|DDL_z.npy` [7798]; `embed/gene_vectors.npy` [7798]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7798 or target_col == 7798). Every well: [[TNIK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNIK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
