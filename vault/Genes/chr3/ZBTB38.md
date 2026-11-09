---
symbol: "ZBTB38"
type: "gene"
col: 10811
ensembl_id: "ENSG00000177311"
name: "zinc finger and BTB domain containing 38"
location: "3q23"
module: 219
arm: "+"
pooled_cpm: 206.18
n_lines_expressing: 47
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/219"]
generated_by: "tahoemap"
---

# ZBTB38

*zinc finger and BTB domain containing 38* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.56× (z +12.1, q 4e-31, up in 34 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.256× (z -26.3, q 0e+00, down in 45 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H12C]] (+0.72, fdr 7e-06), [[ERCC6L2]] (+0.65, fdr 9e-06), [[ST7L]] (+0.64, fdr 1e-05); moves opposite to [[SRP54-AS1]] (-0.69, fdr 7e-06), [[SEC11A]] (-0.66, fdr 7e-06), [[SEC61A2]] (-0.65, fdr 7e-06).
> It is in [[Module 219]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FJX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10811.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +12.1 | 4e-31 | 34/45 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +7.8 | 1e-12 | 31/45 (A-172, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +7.8 | 2e-12 | 32/45 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +6.4 | 2e-08 | 32/45 (hTERT-HPNE, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +6.2 | 9e-08 | 30/45 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.3 | 9e-06 | 32/44 (hTERT-HPNE, SNU-1, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.24×** | +4.2 | 0.003 | 23/45 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.004 | 23/45 (Hs 766T, H4, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **1.21×** | +3.6 | 0.015 | 22/45 (SNU-1, HepG2/C3A, …) | two highest doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.015 | 17/45 (Hs 766T, H4, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.14× | +3.6 | 0.015 | 7/45 (CFPAC-1, NCI-H2030, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.015 | 20/45 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | **1.20×** | +3.5 | 0.017 | 22/45 (SNU-1, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.030 | 15/45 (SW1417, J82, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.035 | 18/45 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.059 | 16/46 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.091 | 11/45 (SW1417, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10811.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.256×** | -26.3 | 0e+00 | 45/45 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.273×** | -25.0 | 0e+00 | 45/45 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.286×** | -24.1 | 0e+00 | 45/45 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.564×** | -15.6 | 0e+00 | 40/46 (RPMI-7951, SNU-423, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.544×** | -11.6 | 5e-29 | 38/45 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.609×** | -9.5 | 2e-19 | 33/45 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -8.6 | 1e-15 | 36/45 (SNU-423, RKO, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.672×** | -7.6 | 2e-12 | 34/45 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.486×** | -7.3 | 2e-11 | 37/46 (SW1417, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.681×** | -7.1 | 7e-11 | 33/47 (hTERT-HPNE, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.703×** | -6.5 | 4e-09 | 30/44 (HepG2/C3A, SW1417, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.736×** | -5.7 | 7e-07 | 30/44 (RKO, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.570×** | -5.7 | 7e-07 | 31/42 (J82, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.579×** | -5.5 | 2e-06 | 30/45 (hTERT-HPNE, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.748×** | -5.3 | 5e-06 | 27/45 (J82, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.769×** | -5.0 | 2e-05 | 27/45 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.839× | -4.7 | 7e-05 | 21/45 (RKO, COLO 205, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -4.4 | 4e-04 | 21/45 (NCI-H460, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 263 | 2 | 12 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -19.7) |
| [[PANC-1 (line)]] | alt | 110 | 0 | 13 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -18.1) |
| [[SNU-1 (line)]] | wt | 258 | 8 (4 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +22.2) | [[Panobinostat (drug)]] 5 µM 0.295× (z -13.9) |
| [[C32 (line)]] | wt | 189 | 6 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +23.3) | [[Belinostat (drug)]] 5 µM 0.291× (z -15.4) |
| [[NCI-H460 (line)]] | wt | 373 | 1 | 11 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.05× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.131× (z -25.1) |
| [[HepG2_C3A (line)]] | wt | 228 | 3 (2 ⚠) | 7 (3 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.91× (z +10.9) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.119× (z -20.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 450 | 2 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 3.28× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.111× (z -23.2) |
| [[SK-MEL-2 (line)]] | alt | 288 | 2 | 8 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +17.0) | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -19.0) |
| [[Hs 766T (line)]] | wt | 116 | 6 | 3 | [[Budesonide (drug)]] 5 µM 2.62× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.236× (z -15.5) |
| [[HS-578T (line)]] | alt | 478 | 3 | 6 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +17.4) | [[Panobinostat (drug)]] 5 µM 0.123× (z -21.1) |
| [[A-172 (line)]] | wt | 155 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +28.0) | [[Panobinostat (drug)]] 5 µM 0.237× (z -16.8) |
| [[HOP62 (line)]] | alt | 423 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -18.2) |
| [[J82 (line)]] | alt | 236 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -19.3) |
| [[LOX-IMVI (line)]] | wt | 193 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +15.6) | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -22.4) |
| [[MIA PaCa-2 (line)]] | alt | 348 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.155× (z -16.0) |
| [[SNU-423 (line)]] | alt | 579 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -21.9) |
| [[SW480 (line)]] | alt | 320 | 1 | 6 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 127 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -21.3) |
| [[LS 180 (line)]] | wt | 145 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.310× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 223 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -17.5) |
| [[RPMI-7951 (line)]] | alt | 603 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -23.6) |
| [[SW1417 (line)]] | alt | 328 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -18.4) |
| [[A549 (line)]] | wt | 232 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -16.3) |
| [[KATO III (line)]] | alt | 166 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +16.4) | [[Panobinostat (drug)]] 5 µM 0.329× (z -15.6) |
| [[NCI-H1792 (line)]] | alt | 198 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0924× (z -21.1) |
| [[Panc 03.27 (line)]] | alt | 266 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -18.9) |
| [[A-427 (line)]] | wt | 60.3 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.315× (z -11.6) |
| [[A498 (line)]] | wt | 120 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -12.3) |
| [[H4 (line)]] | wt | 182 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -15.7) |
| [[HT-29 (line)]] | alt | 97.9 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +17.7) | [[Belinostat (drug)]] 5 µM 0.305× (z -12.4) |
| [[SHP-77 (line)]] | alt | 65.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.263× (z -13.0) |
| [[SW 1271 (line)]] | alt | 254 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -9.8) |
| [[COLO 205 (line)]] | alt | 197 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.192× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 146 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -12.8) |
| [[SW 900 (line)]] | alt | 83.9 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.203× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 55.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 110 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.420× (z -9.1) |
| [[HCT15 (line)]] | alt | 84.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.354× (z -8.9) |
| [[SW48 (line)]] | wt | 55.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.6) | [[Belinostat (drug)]] 5 µM 0.253× (z -9.1) |
| [[AN3 CA (line)]] | alt | 138 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -9.6) |
| [[BT-474 (line)]] | alt | 72.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.381× (z -9.1) |
| [[C-33 A (line)]] | alt | 50.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 82.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 44.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 49.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 182 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H12C]] | +0.72 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ERCC6L2]] | +0.65 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[ST7L]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[MED1]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[TANK]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[SKIL]] | +0.62 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[RP1]] | +0.62 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[SVIL]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ZNF518A]] | +0.62 | +0.60 / +0.52 | both halves | 1e-05 | same gene group |
| [[SLC35A4]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[PPP1R10]] | +0.61 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[MIS12]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54-AS1]] | -0.69 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[SEC11A]] | -0.66 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[SEC61A2]] | -0.65 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[C20orf96]] | -0.65 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[SDHAP1]] | -0.64 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[MAX]] | -0.64 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[IER3IP1]] | -0.63 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[NDUFAF7]] | -0.63 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[RAB6A]] | -0.62 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[PMS2P3-1]] | -0.62 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[TM9SF2]] | -0.62 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[NAPB]] | -0.62 | -0.63 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FJX1]] | B | FJX1 activity raises ZBTB38's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 1.76× lower at baseline in the lines without FJX1 | 0.023 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[ETS1]] | B | ETS1 activity raises ZBTB38's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 2.07× lower at baseline in the lines without ETS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[CASZ1]] | B | CASZ1 activity lowers ZBTB38's level | lines that do not express CASZ1 (10) vs lines expressing it (40) | 2.40× higher at baseline in the lines without CASZ1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SBK1, CPLX1, LLGL2; maybe low, not absent |
| [[PLPP4]] | B | PLPP4 activity raises ZBTB38's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 1.75× lower at baseline in the lines without PLPP4 | 0.089 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 219]]; 11 genes; every member is in the + arm (projection on the module's main direction 0.790). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.44; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.4, -18.2); signed map (17.5, -26.1). **Vector** length 134, 43.6% of its response variance represented; |z| ≥ 3 in 1,619 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.6 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.5 | +12.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.0 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.0 | +6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.7 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +0.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.4 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.3 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +2.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.7 | -9.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.9 | -4.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.3 | -24.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.9 | -5.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.9 | -7.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.1 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:141,324,213-141,449,792 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35036, CIBZ, ZNF921, PPP1R171 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NAP3](https://www.uniprot.org/uniprotkb/Q8NAP3) (Zinc finger and BTB domain-containing protein 38):

> Transcriptional regulator with bimodal DNA-binding specificity. Binds with a higher affinity to methylated CpG dinucleotides in the consensus sequence 5'-CGCG-3' but can also bind to E-box elements (5'-CACGTG-3'). Can also bind specifically to a single methyl-CpG pair. Represses transcription in a methyl-CpG-dependent manner. Plays an important role in regulating DNA replication and common fragile sites (CFS) stability in a RBBP6- and MCM10-dependent manner; represses expression of MCM10 which …

**Summary**, from NCBI Gene [253461](https://www.ncbi.nlm.nih.gov/gene/253461):

> The protein encoded by this gene is a zinc finger transcriptional activator that binds methylated DNA. The encoded protein can form homodimers or heterodimers through the zinc finger domains. In mouse, inhibition of this protein has been associated with apoptosis in some cell types. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:26636](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26636) · Entrez [253461](https://www.ncbi.nlm.nih.gov/gene/253461) · UniProt [Q8NAP3](https://www.uniprot.org/uniprotkb/Q8NAP3) · Ensembl [ENSG00000177311](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177311)

## Data

Gene col 10811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10811); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10811]; `tensor/DDL_lfc|DDL_z.npy` [10811]; `embed/gene_vectors.npy` [10811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10811 or target_col == 10811). Every well: [[ZBTB38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
