---
symbol: "SATB2"
type: "gene"
col: 4038
ensembl_id: "ENSG00000119042"
name: "SATB homeobox 2"
location: "2q33.1"
module: 57
arm: "-"
pooled_cpm: 117.99
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# SATB2

*SATB homeobox 2* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +17.9, q 0e+00, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.511× (z -11.9, q 7e-30, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGF2BP3]] (+0.73, fdr 7e-06), [[ZBED5]] (+0.64, fdr 2e-05), [[TSC22D1]] (+0.64, fdr 1e-05); moves opposite to [[USP30]] (-0.62, fdr 1e-05), [[SKIC3]] (-0.62, fdr 1e-04), [[SLC35A3]] (-0.61, fdr 3e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[HIVEP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4038.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +17.9 | 0e+00 | 38/46 (SW1417, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +9.5 | 5e-19 | 33/45 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +8.1 | 1e-13 | 32/45 (SW1417, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.2 | 7e-08 | 26/47 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.8 | 9e-07 | 27/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +5.7 | 1e-06 | 25/45 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 9e-06 | 30/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +5.2 | 1e-05 | 27/45 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.4 | 8e-04 | 23/45 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.5 | 0.029 | 20/45 (COLO 205, PANC-1, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | **1.21×** | +3.3 | 0.042 | 17/46 (NCI-H1573, CFPAC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4038.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.511×** | -11.9 | 7e-30 | 39/45 (LOX-IMVI, LS 180, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.543×** | -10.8 | 8e-25 | 41/45 (LS 180, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.563×** | -9.4 | 6e-19 | 32/46 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.572×** | -9.1 | 2e-17 | 32/40 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.626×** | -8.3 | 1e-14 | 31/45 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.670×** | -7.1 | 1e-10 | 32/45 (LOX-IMVI, SHP-77, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.694×** | -6.0 | 2e-07 | 26/42 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.732×** | -5.5 | 2e-06 | 31/45 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.761×** | -4.8 | 9e-05 | 28/45 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.756×** | -4.7 | 2e-04 | 26/45 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.776×** | -4.5 | 4e-04 | 23/45 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.618×** | -4.5 | 4e-04 | 17/34 (SK-MEL-2, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.847× | -4.1 | 0.002 | 18/45 (RKO, AsPC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.657×** | -3.9 | 0.004 | 23/44 (C32, J82, …) | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.820×** | -3.2 | 0.052 | 22/44 (NCI-H2030, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.779×** | -3.2 | 0.053 | 18/46 (NCI-H460, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.866× | -3.2 | 0.053 | 18/45 (NCI-H460, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4038. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 96.5 | 8 (1 ⚠) | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +17.4) | [[Panobinostat (drug)]] 5 µM 0.320× (z -16.4) |
| [[LoVo (line)]] | wt | 204 | 6 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +17.8) | [[Panobinostat (drug)]] 5 µM 0.384× (z -13.5) |
| [[LS 180 (line)]] | wt | 245 | 6 (2 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +18.2) | [[Panobinostat (drug)]] 5 µM 0.169× (z -22.7) |
| [[NCI-H460 (line)]] | wt | 165 | 7 (2 ⚠) | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.40× (z +14.6) | [[Auranofin (drug)]] 5 µM 0.442× (z -10.7) |
| [[SW 900 (line)]] | alt | 171 | 3 | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.23× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.416× (z -10.8) |
| [[A-427 (line)]] | wt | 134 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.436× (z -10.8) |
| [[COLO 205 (line)]] | alt | 114 | 7 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +20.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +16.6) | [[Panobinostat (drug)]] 0.5 µM 0.397× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 381 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -23.8) |
| [[PANC-1 (line)]] | alt | 249 | 2 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.61× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.293× (z -15.6) |
| [[C32 (line)]] | wt | 126 | 2 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[NG25 (drug)]] 5 µM 0.153× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 84.3 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +15.3) | — |
| [[NCI-H2030 (line)]] | alt | 169 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.412× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 115 | 3 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.99× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.443× (z -9.0) |
| [[RKO (line)]] | wt | 177 | 2 | 3 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.49× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.335× (z -10.4) ⚠ toxic · without an alert: [[Radotinib (drug)]] 5 µM 0.554× (z -8.7) |
| [[HCT15 (line)]] | alt | 168 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -9.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 94.0 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +15.0) | [[Dinaciclib (drug)]] 0.05 µM 0.478× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 76.5 | 4 (1 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.01× (z +10.2) | — |
| [[J82 (line)]] | alt | 124 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.394× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 57.1 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.122× (z -18.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 193 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.290× (z -14.4) |
| [[SW1417 (line)]] | alt | 48.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.66× (z +20.9) | — |
| [[A498 (line)]] | wt | 90.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -11.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 64.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +17.2) | — |
| [[NCI-H2347 (line)]] | alt | 31.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 85.7 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +11.4) | [[Lonafarnib (drug)]] 5 µM 0.0850× (z -13.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.411× (z -9.0) |
| [[SNU-423 (line)]] | alt | 66.2 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 34.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +18.2) | — |
| [[CHP-212 (line)]] | wt | 54.2 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0603× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 227 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.334× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 249 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.254× (z -8.5) |
| [[A-172 (line)]] | wt | 132 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 80.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -16.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 35.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 51.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +13.9) | — |
| [[KATO III (line)]] | alt | 35.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 83.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +12.6) | — |
| [[RPMI-7951 (line)]] | alt | 134 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 124 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.7) | — |
| [[SW48 (line)]] | wt | 81.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +11.8) | — |
| [[AN3 CA (line)]] | alt | 116 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 127 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4038), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGF2BP3]] | +0.73 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ZBED5]] | +0.64 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[TSC22D1]] | +0.64 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[HIVEP1]] | +0.61 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[PSPC1]] | +0.60 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[SCHIP1]] | +0.59 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[MSANTD2]] | +0.59 | +0.56 / +0.36 | both halves | 1e-04 |  |
| [[DENND5B-AS1]] | +0.59 | +0.46 / +0.36 | both halves | 1e-04 |  |
| [[TCF12]] | +0.59 | +0.57 / +0.37 | both halves | 8e-05 |  |
| [[ERCC6L2]] | +0.58 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[E2F3]] | +0.58 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[CDK6-AS1]] | +0.57 | +0.44 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP30]] | -0.62 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[SKIC3]] | -0.62 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[SLC35A3]] | -0.61 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[STX7]] | -0.61 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[LONP2]] | -0.60 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[RNF20]] | -0.60 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[MRPS31P4]] | -0.60 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[VAMP7]] | -0.60 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[CALCOCO2]] | -0.59 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[COMMD9]] | -0.59 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[MAPK3]] | -0.58 | -0.56 / -0.44 | both halves | 3e-05 | pathway: RUNX2 regulates bone development |
| [[TMEM9]] | -0.58 | -0.49 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SATB2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MSRB3]] | B | MSRB3 activity raises SATB2's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without MSRB3 | 0.065 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HIVEP1]] | C | SATB2 activity lowers HIVEP1's level | lines that do not express SATB2 (3) vs lines expressing it (47) | 2.14× higher at baseline in the lines without SATB2 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PARP3, MCF2, LCA5; maybe low, not absent; its own permutation p |
| [[MAMLD1]] | C | SATB2 activity raises MAMLD1's level | lines that do not express SATB2 (3) vs lines expressing it (47) | 4.72× lower at baseline in the lines without SATB2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PARP3, MCF2, LCA5; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.3, -5.2); signed map (15.7, -9.3). **Vector** length 134, 41.0% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.7 | +17.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +11.4 | +9.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +9.6 | +8.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +2.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.5 | +2.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -9.0 | -11.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.7 | -10.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.5 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.0 | -5.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.4 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -8.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.9 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | SATB homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:199,269,505-199,471,266 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1034, FLJ21474 |
| Gene groups (HGNC) | CUT class homeoboxes and pseudogenes |
| Reactome | 6 pathways, smallest: RUNX2 regulates osteoblast differentiation; RUNX2 regulates bone development; SUMOylation of chromatin organization proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPW6](https://www.uniprot.org/uniprotkb/Q9UPW6) (DNA-binding protein SATB2):

> Binds to DNA, at nuclear matrix- or scaffold-associated regions. Thought to recognize the sugar-phosphate structure of double-stranded DNA. Transcription factor controlling nuclear gene expression, by binding to matrix attachment regions (MARs) of DNA and inducing a local chromatin-loop remodeling. Acts as a docking site for several chromatin remodeling enzymes and also by recruiting corepressors (HDACs) or coactivators (HATs) directly to promoters and enhancers. Required for the initiation of …

**Summary**, from NCBI Gene [23314](https://www.ncbi.nlm.nih.gov/gene/23314):

> This gene encodes a DNA binding protein that specifically binds nuclear matrix attachment regions. The encoded protein is involved in transcription regulation and chromatin remodeling. Defects in this gene are associated with isolated cleft palate and cognitive disability. Alternate splicing results in multiple transcript variants that encode the same protein. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:21637](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21637) · Entrez [23314](https://www.ncbi.nlm.nih.gov/gene/23314) · UniProt [Q9UPW6](https://www.uniprot.org/uniprotkb/Q9UPW6) · Ensembl [ENSG00000119042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119042)

## Data

Gene col 4038: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4038); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4038, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4038]; `tensor/DDL_lfc|DDL_z.npy` [4038]; `embed/gene_vectors.npy` [4038]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4038 or target_col == 4038). Every well: [[SATB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SATB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
