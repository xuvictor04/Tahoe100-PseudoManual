---
symbol: "TMEM131L"
type: "gene"
col: 4258
ensembl_id: "ENSG00000121210"
name: "transmembrane 131 like"
location: "4q31.3"
module: 214
arm: "+"
pooled_cpm: 45.23
n_lines_expressing: 47
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 21
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/214"]
generated_by: "tahoemap"
---

# TMEM131L

*transmembrane 131 like* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.45× (z +23.4, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.414× (z -16.7, q 0e+00, down in 38 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.628× (z -8.8, q 2e-16, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYBU]] (+0.63, fdr 1e-05), [[METAP1]] (+0.63, fdr 1e-05), [[MRPL34]] (+0.62, fdr 2e-05); moves opposite to [[UBXN4]] (-0.56, fdr 3e-05), [[ZNF655]] (-0.56, fdr 3e-05), [[YIPF6]] (-0.55, fdr 2e-05).
> It is in [[Module 214]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SCML2]] → it (grade B ⚠); 7 go from it, the strongest it → [[ARHGEF26]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4258.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.45×** | +23.4 | 0e+00 | 44/45 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.04×** | +21.0 | 0e+00 | 43/45 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.97×** | +20.5 | 0e+00 | 42/45 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.44×** | +16.8 | 0e+00 | 42/45 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +12.7 | 1e-34 | 40/45 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +11.9 | 2e-30 | 34/45 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.13×** | +11.2 | 2e-27 | 39/45 (A-427, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +10.3 | 3e-23 | 30/44 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +9.5 | 1e-19 | 30/44 (J82, NCI-H23, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +8.6 | 5e-16 | 32/45 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +8.1 | 4e-14 | 27/45 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +6.4 | 9e-09 | 25/45 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +6.2 | 2e-08 | 23/45 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.39×** | +6.0 | 1e-07 | 22/45 (C32, HOP62, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.34×** | +5.2 | 6e-06 | 24/45 (A498, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +5.2 | 6e-06 | 21/45 (CFPAC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +5.0 | 2e-05 | 18/45 (NCI-H2030, A549, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.65×** | +4.9 | 3e-05 | 17/45 (LoVo, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +4.9 | 3e-05 | 19/45 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4258.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.414×** | -16.7 | 0e+00 | 38/43 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.426×** | -15.5 | 0e+00 | 35/38 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.540×** | -10.8 | 8e-25 | 28/41 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.628×** | -8.8 | 2e-16 | 27/45 (SW480, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.761×** | -4.8 | 2e-04 | 17/44 (SNU-1, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.626×** | -4.6 | 3e-04 | 19/46 (RKO, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.799×** | -4.3 | 0.002 | 15/45 (RKO, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.827×** | -3.6 | 0.022 | 16/45 (A549, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4258. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 20.2 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +23.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 7.05× (z +12.1) | — |
| [[A-172 (line)]] | wt | 38.3 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.37× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.0681× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.279× (z -10.7) |
| [[A-427 (line)]] | wt | 40.1 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.11× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.485× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 59.7 | 3 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.96× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -11.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 47.6 | 4 (1 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 3.33× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -12.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 34.7 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.19× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -9.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 89.3 | 2 (1 ⚠) | 4 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.44× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.378× (z -11.0) |
| [[C32 (line)]] | wt | 32.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.86× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 28.4 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.56× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 21.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 7.17× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 148 | 2 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0977× (z -19.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 32.4 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -8.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 70.5 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.248× (z -12.3) |
| [[SW1417 (line)]] | alt | 36.5 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.82× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -15.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 49.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.52× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 12.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 12.0× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 65.8 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.03× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -14.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 29.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.67× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 32.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.84× (z +15.5) | — |
| [[SK-MEL-2 (line)]] | alt | 48.7 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.06× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -11.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 46.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.353× (z -8.5) |
| [[A498 (line)]] | wt | 73.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0703× (z -16.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 23.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.90× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 133 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0796× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.186× (z -10.7) |
| [[H4 (line)]] | wt | 39.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0992× (z -14.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.78× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 43.4 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.46× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -14.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 47.4 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.89× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 41.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.92× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 19.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.31× (z +10.8) | — |
| [[SW48 (line)]] | wt | 74.3 | 1 | 2 (2 ⚠) | [[Ponatinib (drug)]] 5 µM 3.28× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0911× (z -16.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 72.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -14.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 70.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0710× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.248× (z -10.2) |
| [[HS-578T (line)]] | alt | 28.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.17× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -9.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 37.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -9.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -13.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 8.77 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.62 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4258), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYBU]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[METAP1]] | +0.63 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[MRPL34]] | +0.62 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[PPARGC1B]] | +0.61 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[ARHGEF26]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[RAC3]] | +0.60 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[FLVCR2]] | +0.59 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[FDX1]] | +0.59 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[FNBP1L]] | +0.59 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[LRRC1]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[TADA1]] | +0.58 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[TGFBR3]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN4]] | -0.56 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ZNF655]] | -0.56 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[YIPF6]] | -0.55 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[GPATCH2L]] | -0.55 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[UBE2D3-AS1]] | -0.54 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[SP2]] | -0.54 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[SUPT6H]] | -0.54 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ZNF546]] | -0.54 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[MAP3K7]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[DPP8]] | -0.53 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[SLC30A9]] | -0.53 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[MIS12]] | -0.53 | -0.42 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCML2]] | B | SCML2 activity raises TMEM131L's level | lines that do not express SCML2 (7) vs lines expressing it (43) | 2.19× lower at baseline in the lines without SCML2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ASAP3, ENSG00000267131, LAG3 |
| [[RNF220]] | B | RNF220 activity raises TMEM131L's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 2.05× lower at baseline in the lines without RNF220 | 0.095 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[ARHGEF26]] | C | ARHGEF26 activity raises TMEM131L's level | lines that do not express ARHGEF26 (4) vs lines expressing it (46) | 3.50× lower at baseline in the lines without ARHGEF26 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ERO1B, RHOQ, DPF1; co-absent with the target; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF26]] | C | TMEM131L activity raises ARHGEF26's level | lines that do not express TMEM131L (3) vs lines expressing it (47) | 5.17× lower at baseline in the lines without TMEM131L | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: DPF1, TBC1D19, ARHGEF26; maybe low, not absent; co-absent with the target; its own permutation p |
| [[HMGN3]] | C | TMEM131L activity raises HMGN3's level | lines that do not express TMEM131L (3) vs lines expressing it (47) | 3.58× lower at baseline in the lines without TMEM131L | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: DPF1, TBC1D19, ARHGEF26; maybe low, not absent; co-absent with the target; its own permutation p |
| [[TFEB]] | C | TMEM131L activity lowers TFEB's level | lines that do not express TMEM131L (3) vs lines expressing it (47) | 2.29× higher at baseline in the lines without TMEM131L | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: DPF1, TBC1D19, ARHGEF26; maybe low, not absent; its own permutation p |
| [[MACIR]] | C | TMEM131L activity raises MACIR's level | lines that do not express TMEM131L (3) vs lines expressing it (47) | 2.26× lower at baseline in the lines without TMEM131L | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: DPF1, TBC1D19, ARHGEF26; maybe low, not absent; its own permutation p |
| [[PPAT]] | C | TMEM131L activity raises PPAT's level | lines that do not express TMEM131L (3) vs lines expressing it (47) | 1.95× lower at baseline in the lines without TMEM131L | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: DPF1, TBC1D19, ARHGEF26; maybe low, not absent; its own permutation p |
| [[ZNF621]] | C | TMEM131L activity raises ZNF621's level | lines that do not express TMEM131L (3) vs lines expressing it (47) | 1.84× lower at baseline in the lines without TMEM131L | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: DPF1, TBC1D19, ARHGEF26; maybe low, not absent; its own permutation p |
| [[CHPT1]] | C | TMEM131L activity raises CHPT1's level | lines that do not express TMEM131L (3) vs lines expressing it (47) | 1.62× lower at baseline in the lines without TMEM131L | 0.083 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: DPF1, TBC1D19, ARHGEF26; maybe low, not absent |

## Where it sits

- **Module**: [[Module 214]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.1, -5.7); signed map (-20.1, 19.3). **Vector** length 109, 30.9% of its response variance represented; |z| ≥ 3 in 1,342 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +12.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.5 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +16.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.5 | +5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +11.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.2 | +2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +3.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.3 | -8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.4 | -15.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.0 | -10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.9 | -16.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane 131 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:153,466,346-153,636,711 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586H1322; previously KIAA0922 |
| Matched by | ensembl_id |

**Function**, from UniProt [A2VDJ0](https://www.uniprot.org/uniprotkb/A2VDJ0) (Transmembrane protein 131-like):

> [Isoform 1]: Membrane-associated form that antagonizes canonical Wnt signaling by triggering lysosome-dependent degradation of Wnt-activated LRP6. Regulates thymocyte proliferation.

**Summary**, from NCBI Gene [23240](https://www.ncbi.nlm.nih.gov/gene/23240):

> Involved in negative regulation of canonical Wnt signaling pathway and negative regulation of immature T cell proliferation in thymus. Located in cytoplasm and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29146](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29146) · Entrez [23240](https://www.ncbi.nlm.nih.gov/gene/23240) · UniProt [A2VDJ0](https://www.uniprot.org/uniprotkb/A2VDJ0) · Ensembl [ENSG00000121210](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121210)

## Data

Gene col 4258: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4258); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4258, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4258]; `tensor/DDL_lfc|DDL_z.npy` [4258]; `embed/gene_vectors.npy` [4258]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4258 or target_col == 4258). Every well: [[TMEM131L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM131L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
