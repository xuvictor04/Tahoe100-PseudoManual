---
symbol: "ZSWIM5"
type: "gene"
col: 8514
ensembl_id: "ENSG00000162415"
name: "zinc finger SWIM-type containing 5"
location: "1p34.1"
module: 144
arm: "+"
pooled_cpm: 89.42
n_lines_expressing: 45
n_dd_up: 6
n_dd_down: 38
n_dd_up_clean: 6
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# ZSWIM5

*zinc finger SWIM-type containing 5* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.30× (z +7.4, q 6e-11, up in 21 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (17 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.406× (z -17.9, q 0e+00, down in 41 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C4orf47]] (+0.63, fdr 1e-05), [[ZBTB25]] (+0.60, fdr 1e-05), [[INHA]] (+0.59, fdr 1e-05); moves opposite to [[ADAMTSL5]] (-0.53, fdr 2e-05), [[USP14]] (-0.53, fdr 3e-05), [[ELAC2]] (-0.50, fdr 5e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPRY1]] → it (grade C ⚠); 5 go from it, the strongest it → [[DARS1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8514.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +7.4 | 6e-11 | 21/44 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +5.6 | 8e-06 | 22/44 (LoVo, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +4.7 | 6e-04 | 19/42 (H4, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +4.2 | 0.004 | 19/43 (NCI-H1573, KATO III, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +4.0 | 0.006 | 14/43 (LoVo, HS-578T, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.20×** | +3.7 | 0.018 | 15/43 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.20×** | +3.7 | 0.018 | 18/43 (hTERT-HPNE, NCI-H2030, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.091 | 9/43 (SNU-423, HT-29, …) | rises with dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.11 | 8/43 (NCI-H2030, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.11 | 6/44 (CFPAC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.12 | 8/43 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 22 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8514.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.406×** | -17.9 | 0e+00 | 41/43 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.454×** | -15.6 | 0e+00 | 39/43 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.454×** | -15.1 | 0e+00 | 38/42 (C32, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.485×** | -14.4 | 1e-44 | 38/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.512×** | -13.3 | 4e-38 | 40/43 (LS 180, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.520×** | -12.2 | 2e-32 | 40/43 (C32, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.532×** | -12.0 | 2e-31 | 30/37 (HCT15, SW480, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.540×** | -11.7 | 6e-30 | 33/43 (C32, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.528×** | -11.7 | 7e-30 | 31/38 (HepG2/C3A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.562×** | -11.4 | 2e-28 | 32/42 (C-33 A, SW480, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -9.8 | 5e-21 | 34/43 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.408×** | -9.3 | 7e-19 | 34/43 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.661×** | -8.2 | 1e-14 | 31/43 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.465×** | -7.9 | 9e-14 | 33/44 (PANC-1, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.691×** | -7.3 | 1e-11 | 26/43 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.693×** | -7.2 | 2e-11 | 29/43 (HepG2/C3A, SW480, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.697×** | -7.1 | 3e-11 | 34/43 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.709×** | -6.8 | 3e-10 | 25/43 (NCI-H23, C32, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.719×** | -6.5 | 2e-09 | 32/42 (HT-29, LS 180, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.796×** | -6.4 | 5e-09 | 28/44 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.782×** | -4.7 | 6e-05 | 23/42 (LS 180, NCI-H460, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8514. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 132 | 0 | 22 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -24.2) |
| [[C32 (line)]] | wt | 316 | 0 | 17 (11 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.114× (z -22.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.259× (z -14.3) |
| [[SW480 (line)]] | alt | 135 | 0 | 16 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -28.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.281× (z -17.0) |
| [[HepG2_C3A (line)]] | wt | 279 | 0 | 15 (8 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -21.9) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.198× (z -18.2) |
| [[HCT15 (line)]] | alt | 199 | 0 | 14 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0357× (z -30.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.174× (z -16.4) |
| [[PANC-1 (line)]] | alt | 164 | 0 | 13 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -25.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.431× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 78.2 | 1 (1 ⚠) | 11 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +16.6) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.188× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.329× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 108 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -23.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -12.7) |
| [[LoVo (line)]] | wt | 104 | 2 (1 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.318× (z -15.8) |
| [[LS 180 (line)]] | wt | 148 | 0 | 10 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.234× (z -16.2) |
| [[MIA PaCa-2 (line)]] | alt | 77.2 | 0 | 8 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.272× (z -12.3) |
| [[C-33 A (line)]] | alt | 211 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0618× (z -27.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.354× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 82.5 | 0 | 6 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.289× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 107 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.457× (z -8.8) |
| [[SHP-77 (line)]] | alt | 242 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.420× (z -11.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.438× (z -10.7) |
| [[SNU-1 (line)]] | wt | 93.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.219× (z -11.1) |
| [[HOP62 (line)]] | alt | 81.5 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.254× (z -13.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.363× (z -10.6) |
| [[HT-29 (line)]] | alt | 67.7 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.314× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 43.3 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.149× (z -12.9) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.250× (z -9.8) |
| [[A-427 (line)]] | wt | 89.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 108 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.263× (z -12.3) |
| [[COLO 205 (line)]] | alt | 146 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.171× (z -17.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.387× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 50.1 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.265× (z -9.9) |
| [[HS-578T (line)]] | alt | 44.5 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.232× (z -10.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 64.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.385× (z -9.1) |
| [[SNU-423 (line)]] | alt | 43.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.197× (z -10.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW 1271 (line)]] | alt | 51.9 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0745× (z -8.7) |
| [[SW 900 (line)]] | alt | 83.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.372× (z -9.1) |
| [[AN3 CA (line)]] | alt | 80.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 74.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 56.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 78.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.217× (z -10.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[J82 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.272× (z -9.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 56.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.423× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 37.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.239× (z -10.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 21.6 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 19.1 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 85.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8514), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C4orf47]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ZBTB25]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[INHA]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[FUT11]] | +0.58 | +0.40 / +0.61 | both halves | 4e-05 |  |
| [[NDUFC1]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[LPAR6]] | +0.57 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[DIPK2A]] | +0.55 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[SPRY1]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[KDM4C]] | +0.53 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[DHX32]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[RBPJ]] | +0.52 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[PDGFA]] | +0.51 | +0.36 / +0.57 | both halves | 9e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTSL5]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[USP14]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ELAC2]] | -0.50 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[HECTD3]] | -0.49 | -0.52 / -0.33 | both halves | 1e-04 | ⚠ same locus (5.1 kb, same strand: neighbours can correlate without regulation) |
| [[STK25]] | -0.49 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[DLST]] | -0.48 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[USP35]] | -0.48 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[TALDO1]] | -0.48 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[CDK9]] | -0.48 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ANKRD52]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[KCTD21]] | -0.47 | -0.50 / -0.29 | both halves | 3e-04 |  |
| [[EXT2]] | -0.47 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[RPUSD1]] | -0.46 | -0.52 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPRY1]] | C | SPRY1 activity raises ZSWIM5's level | lines that do not express SPRY1 (4) vs lines expressing it (46) | 2.61× lower at baseline in the lines without SPRY1 | 0.092 | ⚠ few lines (4 vs 46); across organs; also absent: ARG2, ZNF385C, ENSG00000290927; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DARS1-AS1]] | B | ZSWIM5 activity raises DARS1-AS1's level | lines that do not express ZSWIM5 (5) vs lines expressing it (45) | 2.05× lower at baseline in the lines without ZSWIM5 | 0.060 | ⚠ within organs, on part of the lines; also absent: DLGAP1, ABHD12B, TTN; maybe low, not absent; its own permutation p |
| [[CAPN1]] | B | ZSWIM5 activity lowers CAPN1's level | lines that do not express ZSWIM5 (5) vs lines expressing it (45) | 1.69× higher at baseline in the lines without ZSWIM5 | 0.060 | ⚠ within organs, on part of the lines; also absent: DLGAP1, ABHD12B, TTN; maybe low, not absent; its own permutation p |
| [[KDM2B-DT]] | B | ZSWIM5 activity raises KDM2B-DT's level | lines that do not express ZSWIM5 (5) vs lines expressing it (45) | 2.33× lower at baseline in the lines without ZSWIM5 | 0.083 | ⚠ within organs, on part of the lines; also absent: DLGAP1, ABHD12B, TTN; maybe low, not absent |
| [[MAPK9]] | B | ZSWIM5 activity lowers MAPK9's level | lines that do not express ZSWIM5 (5) vs lines expressing it (45) | 1.36× higher at baseline in the lines without ZSWIM5 | 0.089 | ⚠ within organs, on part of the lines; also absent: DLGAP1, ABHD12B, TTN; maybe low, not absent; its own permutation p |
| [[ZDHHC16]] | B | ZSWIM5 activity lowers ZDHHC16's level | lines that do not express ZSWIM5 (5) vs lines expressing it (45) | 1.26× higher at baseline in the lines without ZSWIM5 | 0.089 | ⚠ within organs, on part of the lines; also absent: DLGAP1, ABHD12B, TTN; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, -20.4); signed map (-3.8, 4.4). **Vector** length 92.3, 26.3% of its response variance represented; |z| ≥ 3 in 1,375 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Ciclopirox (drug)]] 5 µM |  | +1.6 | +1.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.9 | -12.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.1 | -15.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -5.9 | -11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.1 | -11.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.8 | -17.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -13.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.7 | -7.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -6.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger SWIM-type containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,016,399-45,306,209 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1511 |
| Gene groups (HGNC) | Zinc fingers SWIM-type |
| Matched by | ensembl_id |

UniProt [Q9P217](https://www.uniprot.org/uniprotkb/Q9P217) carries no function annotation.

**Summary**, from NCBI Gene [57643](https://www.ncbi.nlm.nih.gov/gene/57643):

> Predicted to enable zinc ion binding activity. Located in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29299) · Entrez [57643](https://www.ncbi.nlm.nih.gov/gene/57643) · UniProt [Q9P217](https://www.uniprot.org/uniprotkb/Q9P217) · Ensembl [ENSG00000162415](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162415)

## Data

Gene col 8514: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8514); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8514, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8514]; `tensor/DDL_lfc|DDL_z.npy` [8514]; `embed/gene_vectors.npy` [8514]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8514 or target_col == 8514). Every well: [[ZSWIM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSWIM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
