---
symbol: "AP1B1"
type: "gene"
col: 1909
ensembl_id: "ENSG00000100280"
name: "adaptor related protein complex 1 subunit beta 1"
location: "22q12.2"
module: 111
arm: "+"
pooled_cpm: 30.64
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# AP1B1

*adaptor related protein complex 1 subunit beta 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.63× (z +29.1, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Bimiralisib (drug)]] 5 µM: 0.642× (z -3.8, q 0.097, down in 12 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 0.274×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.308×; ⚠ cell-cycle shift, explains ~38% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THOP1]] (+0.65, fdr 7e-06), [[DBNL]] (+0.64, fdr 1e-05), [[WDR1]] (+0.63, fdr 1e-05); moves opposite to [[CAMLG]] (-0.60, fdr 7e-06), [[NACA]] (-0.58, fdr 1e-05, ⚠ NACA in the vector space only through flagged drug-doses), [[SNHG7]] (-0.58, fdr 1e-05), [[TAF1D]] (-0.57, fdr 3e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 19 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1909.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.63×** | +29.1 | 0e+00 | 45/47 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **3.87×** | +21.6 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.62×** | +20.5 | 0e+00 | 48/48 (SW480, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **3.47×** | +19.9 | 0e+00 | 48/48 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **3.18×** | +18.4 | 0e+00 | 38/42 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.05×** | +17.1 | 0e+00 | 45/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.87×** | +16.2 | 0e+00 | 35/36 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.27×** | +13.0 | 5e-37 | 40/47 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.54×** | +12.9 | 3e-36 | 35/38 (LoVo, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.51×** | +9.2 | 1e-18 | 34/48 (NCI-H2347, A549, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.76×** | +9.0 | 1e-17 | 40/48 (SW480, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.80×** | +8.6 | 5e-16 | 39/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.68×** | +8.3 | 6e-15 | 37/46 (LoVo, HEC-1-A, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.67×** | +8.1 | 2e-14 | 33/48 (LoVo, SW480, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.70×** | +8.1 | 3e-14 | 40/48 (SNU-423, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +7.1 | 6e-11 | 35/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.4 | 2e-06 | 28/48 (SNU-423, HCT15, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.84×** | +5.1 | 1e-05 | 28/48 (A549, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.5 | 2e-04 | 24/48 (SNU-1, NCI-H2030, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 8e-04 | 22/47 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.004 | 16/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.009 | 14/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.51×** | +3.4 | 0.012 | 12/46 (NCI-H460, HT-29, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.026 | 7/45 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.037 | 5/48 (SW1417, HT-29, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.049 | 13/48 (NCI-H2347, SNU-423, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1909.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 0.274×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.308×; ⚠ cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | **0.642×** | -3.8 | 0.097 | 12/47 (AsPC-1, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.783× | -3.4 | 0.20 | 11/48 (AsPC-1, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.875× | -3.1 | 0.20 | 9/48 (AsPC-1, AN3 CA, …) | rises with dose | position effect removed |
| [[AZD-8055 (drug)]] 0.5 µM |  | 0.769× | -3.1 | 0.20 | 9/48 (HCT15, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 0.824× | -3.1 | 0.20 | 13/47 (RKO, SW 900, …) | rises with dose | position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | 0.700× | -3.0 | 0.20 | 10/48 (C32, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | 0.701× | -3.0 | 0.20 | 10/48 (C32, AsPC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.70 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1909. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 37.9 | 10 (7 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.55× (z +19.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.86× (z +16.9) | — |
| [[LoVo (line)]] | wt | 28.8 | 9 (7 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.27× (z +13.9) | — |
| [[NCI-H460 (line)]] | wt | 21.6 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +20.8) | — |
| [[A498 (line)]] | wt | 40.5 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +21.8) | — |
| [[A549 (line)]] | wt | 19.6 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +17.8) | — |
| [[HOP62 (line)]] | alt | 17.5 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +14.3) | — |
| [[HS-578T (line)]] | alt | 34.6 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +15.7) | — |
| [[PANC-1 (line)]] | alt | 22.6 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +16.6) | — |
| [[HT-29 (line)]] | alt | 57.5 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +16.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.7 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +15.1) | — |
| [[NCI-H2347 (line)]] | alt | 30.7 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +16.8) | — |
| [[HEC-1-A (line)]] | alt | 41.9 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +16.4) | — |
| [[KATO III (line)]] | alt | 33.4 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.65× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +13.4) | — |
| [[Panc 03.27 (line)]] | alt | 21.6 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +14.4) | — |
| [[SNU-423 (line)]] | alt | 22.3 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.47× (z +17.2) | — |
| [[A-172 (line)]] | wt | 19.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +16.1) | — |
| [[CFPAC-1 (line)]] | alt | 27.0 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +15.9) | — |
| [[LS 180 (line)]] | wt | 34.2 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.57× (z +13.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 27.1 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.46× (z +10.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.29× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 36.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 30.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 35.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +14.2) | — |
| [[SW1417 (line)]] | alt | 53.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.4) | — |
| [[A-427 (line)]] | wt | 16.6 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.52× (z +9.3) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 32.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +13.6) | — |
| [[NCI-H2030 (line)]] | alt | 36.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.2) | — |
| [[SHP-77 (line)]] | alt | 52.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +10.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[AsPC-1 (line)]] | alt | 80.1 | 0 | 2 (1 ⚠) | — | [[Radotinib (drug)]] 5 µM 0.274× (z -10.5) |
| [[C32 (line)]] | wt | 24.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[J82 (line)]] | alt | 25.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 19.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.11× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[RKO (line)]] | wt | 47.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +16.4) | — |
| [[RPMI-7951 (line)]] | alt | 28.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +10.9) | — |
| [[SNU-1 (line)]] | wt | 24.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 39.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.11× (z +9.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SW48 (line)]] | wt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +10.7) | — |
| [[AN3 CA (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1909), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOP1]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[DBNL]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 | same gene group |
| [[WDR1]] | +0.63 | +0.51 / +0.58 | both halves | 1e-05 | same gene group |
| [[NF2]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 | STRING 657 |
| [[AXL]] | +0.60 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[ARPC4]] | +0.59 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[NUP188]] | +0.58 | +0.51 / +0.61 | both halves | 1e-05 | pathway: HIV Infection |
| [[CSRP1]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[CAPNS1]] | +0.56 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[ARHGDIA]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[NCBP1]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 | pathway: HIV Infection |
| [[ZKSCAN2]] | +0.55 | +0.66 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMLG]] | -0.60 | -0.71 / -0.62 | both halves | 7e-06 |  |
| [[NACA]] ⚠ | -0.58 | -0.49 / -0.61 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG7]] | -0.58 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[TAF1D]] | -0.57 | -0.47 / -0.45 | both halves | 3e-05 | same gene group |
| [[NACA4P]] ⚠ | -0.55 | -0.45 / -0.54 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | -0.55 | -0.55 / -0.57 | both halves | 1e-05 | same gene group |
| [[ZFAS1]] | -0.55 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[RPL34]] | -0.54 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[GAS5]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[NDUFAF7]] | -0.54 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | -0.53 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[FTL]] | -0.53 | -0.49 / -0.58 | both halves | 1e-05 | pathway: Golgi Associated Vesicle Biogenesis; STRING 528 |
| [[RPL7]] | -0.53 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[SOS1]] | -0.53 | -0.54 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AP1B1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.6, -19.6); signed map (-7.2, 33.9). **Vector** length 78.0, 19.6% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.4 | +17.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +4.8 | +18.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +4.7 | +16.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +29.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.7 | +1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +1.1 |
| fall | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | +0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.9 | +9.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | +0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.0 | -0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | +2.2 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 1 subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:29,327,680-29,388,583 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BAM22, AP105A; previously ADTB1, CLAPB2 |
| Gene groups (HGNC) | Clathrin/coatomer adaptor, adaptin-like, N-terminal domain containing; Adaptor related protein complex 1; MicroRNA protein coding host genes; Small nucleolar RNA protein coding host genes |
| Reactome | 13 pathways, smallest: Nef mediated downregulation of MHC class I complex cell surface expression; Nef-mediates down modulation of cell surface receptors by recruiting them to clathrin adapters; The role of Nef in HIV-1 replication and disease pathogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q10567](https://www.uniprot.org/uniprotkb/Q10567) (AP-1 complex subunit beta-1):

> Subunit of clathrin-associated adaptor protein complex 1 that plays a role in protein sorting in the late-Golgi/trans-Golgi network (TGN) and/or endosomes. The AP complexes mediate both the recruitment of clathrin to membranes and the recognition of sorting signals within the cytosolic tails of transmembrane cargo molecules.

**Summary**, from NCBI Gene [162](https://www.ncbi.nlm.nih.gov/gene/162):

> Adaptor protein complex 1 is found at the cytoplasmic face of coated vesicles located at the Golgi complex, where it mediates both the recruitment of clathrin to the membrane and the recognition of sorting signals within the cytosolic tails of transmembrane receptors. This complex is a heterotetramer composed of two large, one medium, and one small adaptin subunit. The protein encoded by this gene serves as one of the large subunits of this complex and is a member of the adaptin protein family. …

**Accessions** — [HGNC:554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:554) · Entrez [162](https://www.ncbi.nlm.nih.gov/gene/162) · UniProt [Q10567](https://www.uniprot.org/uniprotkb/Q10567) · Ensembl [ENSG00000100280](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100280)

## Data

Gene col 1909: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1909); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1909, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1909]; `tensor/DDL_lfc|DDL_z.npy` [1909]; `embed/gene_vectors.npy` [1909]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1909 or target_col == 1909). Every well: [[AP1B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP1B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
