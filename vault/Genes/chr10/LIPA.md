---
symbol: "LIPA"
type: "gene"
col: 2881
ensembl_id: "ENSG00000107798"
name: "lipase A, lysosomal acid type"
location: "10q23.31"
module: 32
arm: "+"
pooled_cpm: 42.1
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 24
n_dd_up_clean: 24
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# LIPA

*lipase A, lysosomal acid type* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +14.5, q 1e-44, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.648× (z -9.5, q 8e-19, down in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.637× (z -7.0, q 3e-10, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCARB2]] (+0.71, fdr 7e-06), [[LGALS3BP]] (+0.70, fdr 9e-06), [[IFIT1]] (+0.67, fdr 7e-06, ⚠ same locus), [[HLA-C]] (+0.64, fdr 1e-05); moves opposite to [[CROCCP2-1]] (-0.57, fdr 5e-05), [[RNF166]] (-0.52, fdr 1e-04), [[RBMX2]] (-0.48, fdr 3e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TRIM22]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2881.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +14.5 | 1e-44 | 42/48 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +12.2 | 7e-32 | 29/36 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +11.4 | 9e-28 | 37/45 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +8.5 | 2e-15 | 32/41 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +7.0 | 3e-10 | 38/47 (KATO III, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +6.6 | 4e-09 | 32/48 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +6.5 | 5e-09 | 31/48 (MIA PaCa-2, J82, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +6.0 | 2e-07 | 29/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.44×** | +5.7 | 8e-07 | 28/48 (CFPAC-1, J82, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +5.7 | 8e-07 | 29/47 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.7 | 8e-07 | 25/48 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.6 | 9e-07 | 28/48 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +5.0 | 2e-05 | 26/47 (A549, HOP62, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.25×** | +4.8 | 5e-05 | 21/48 (PANC-1, BT-474, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 5e-05 | 25/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.30×** | +4.2 | 7e-04 | 21/48 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 9e-04 | 19/48 (CFPAC-1, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 1e-03 | 22/48 (CFPAC-1, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.001 | 23/47 (KATO III, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2881.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.648×** | -9.5 | 8e-19 | 30/48 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.590×** | -7.9 | 7e-13 | 31/48 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -7.3 | 5e-11 | 30/46 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.637×** | -7.0 | 3e-10 | 29/48 (SW1417, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.639×** | -7.0 | 3e-10 | 31/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.764×** | -5.9 | 3e-07 | 27/48 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.685×** | -5.9 | 3e-07 | 28/47 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.767×** | -5.8 | 4e-07 | 26/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.747×** | -4.6 | 3e-04 | 24/47 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.823×** | -4.3 | 9e-04 | 22/48 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.771×** | -3.9 | 0.005 | 20/47 (H4, RKO, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.781×** | -3.8 | 0.006 | 20/47 (RKO, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **0.788×** | -3.6 | 0.015 | 21/47 (RPMI-7951, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.796×** | -3.6 | 0.015 | 19/48 (PANC-1, A549, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.022 | 14/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.799×** | -3.3 | 0.029 | 18/47 (NCI-H23, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.809×** | -3.3 | 0.029 | 19/47 (PANC-1, LoVo, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.822×** | -3.1 | 0.060 | 15/47 (LOX-IMVI, J82, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.824×** | -3.0 | 0.067 | 19/48 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.874× | -3.0 | 0.072 | 12/49 (SNU-423, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2881. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +17.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.5) | — |
| [[A549 (line)]] | wt | 43.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -19.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HEC-1-A (line)]] | alt | 36.0 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +15.1) | — |
| [[HT-29 (line)]] | alt | 15.8 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.14× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +8.6) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.239× (z -8.9) ⚠ toxic |
| [[LS 180 (line)]] | wt | 17.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 123 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +10.0) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.250× (z -11.1) |
| [[PANC-1 (line)]] | alt | 42.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -19.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SW1417 (line)]] | alt | 40.8 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -11.4) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.362× (z -9.0) |
| [[A498 (line)]] | wt | 50.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -12.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[BT-474 (line)]] | alt | 26.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -9.3) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.222× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 30.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.20× (z +9.1) ⚠ toxic; transcription drop | [[Pentoxifylline (drug)]] 0.5 µM 0.222× (z -8.7) |
| [[Hs 766T (line)]] | wt | 99.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +11.2) | [[Harringtonine (drug)]] 5 µM 0.375× (z -8.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[J82 (line)]] | alt | 27.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +10.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 37.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +13.9) | [[Tofacitinib (drug)]] 5 µM 0.452× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 51.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -18.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H23 (line)]] | alt | 36.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -10.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[Panc 03.27 (line)]] | alt | 62.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.96× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -12.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[RKO (line)]] | wt | 38.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.149× (z -11.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 71.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -11.4) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0709× (z -8.9) |
| [[A-427 (line)]] | wt | 27.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -14.4) ⚠ cell-cycle shift, explains ~50% of this change |
| [[C-33 A (line)]] | alt | 30.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -9.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 50.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -16.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SHP-77 (line)]] | alt | 18.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -12.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SW480 (line)]] | alt | 24.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.7) | — |
| [[A-172 (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2881), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCARB2]] | +0.71 | +0.59 / +0.73 | both halves | 7e-06 | STRING 522 |
| [[LGALS3BP]] | +0.70 | +0.57 / +0.75 | both halves | 9e-06 | **novel candidate** |
| [[IFIT1]] | +0.67 | +0.79 / +0.60 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HLA-C]] | +0.64 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[RNF213]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[OAS3]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[SAMHD1]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PNPT1]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[LAP3]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[ADAR]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[TRANK1]] | +0.62 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[LY6E]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TRIM14]] | +0.60 | +0.65 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.57 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[RNF166]] | -0.52 | -0.32 / -0.49 | both halves | 1e-04 |  |
| [[RBMX2]] | -0.48 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[NKAP]] | -0.48 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[EIF5B]] | -0.48 | -0.27 / -0.49 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM22]] | B | TRIM22 activity raises LIPA's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.41× lower at baseline in the lines without TRIM22 | 0.070 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[MDK]] | B | MDK activity lowers LIPA's level | lines that do not express MDK (14) vs lines expressing it (36) | 1.55× higher at baseline in the lines without MDK | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.601). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.5, 51.2); signed map (67.5, 28.0). **Vector** length 108, 30.1% of its response variance represented; |z| ≥ 3 in 1,156 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.50 to 56); *interferon gamma response* (hallmark, mean cos +0.51 to 60); *interferon* (control, mean cos +0.55 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.9 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.6 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +8.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.5 | +3.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.3 | +5.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.2 | +4.1 |
| fall | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.6 | -4.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.5 | -5.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.0 | -2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | -1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.7 | -7.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | lipase A, lysosomal acid type |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:89,213,569-89,414,557 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LAL, CESD |
| Gene groups (HGNC) | Lipases |
| Hallmark sets | COMPLEMENT |
| Reactome | 4 pathways, smallest: LDL clearance; Plasma lipoprotein clearance; Plasma lipoprotein assembly, remodeling, and clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [P38571](https://www.uniprot.org/uniprotkb/P38571) (Lysosomal acid lipase/cholesteryl ester hydrolase):

> Catalyzes the deacylation of cholesteryl ester core lipids of endocytosed low density lipoproteins to generate free fatty acids and cholesterol. Hydrolyzes triglycerides (1,2,3-triacylglycerol) and diglycerides (such as 1,2-diacylglycerol and 1,3-diacylglycerol) with preference for the acyl moieties at the sn-1 or sn-3 positions.

**Summary**, from NCBI Gene [3988](https://www.ncbi.nlm.nih.gov/gene/3988):

> This gene encodes lipase A, the lysosomal acid lipase (also known as cholesterol ester hydrolase). This enzyme functions in the lysosome to catalyze the hydrolysis of cholesteryl esters and triglycerides. Mutations in this gene can result in Wolman disease and cholesteryl ester storage disease. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:6617](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6617) · Entrez [3988](https://www.ncbi.nlm.nih.gov/gene/3988) · UniProt [P38571](https://www.uniprot.org/uniprotkb/P38571) · Ensembl [ENSG00000107798](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107798)

## Data

Gene col 2881: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2881); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2881, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2881]; `tensor/DDL_lfc|DDL_z.npy` [2881]; `embed/gene_vectors.npy` [2881]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2881 or target_col == 2881). Every well: [[LIPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
