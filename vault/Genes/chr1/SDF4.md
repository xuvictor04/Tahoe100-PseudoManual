---
symbol: "SDF4"
type: "gene"
col: 1234
ensembl_id: "ENSG00000078808"
name: "stromal cell derived factor 4"
location: "1p36.33"
module: 50
arm: "+"
pooled_cpm: 44.28
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# SDF4

*stromal cell derived factor 4* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.09× (z +16.5, q 0e+00, up in 45 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +11.3, q 3e-27, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Verteporfin (drug)]] 5 µM: 0.644× (z -6.2, q 4e-07, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDOST]] (+0.72, fdr 1e-05), [[NCSTN]] (+0.67, fdr 1e-05), [[NUCB1]] (+0.65, fdr 7e-06); moves opposite to [[KRI1]] (-0.55, fdr 1e-04), [[NT5C]] (-0.54, fdr 2e-04), [[GTF2H2]] (-0.53, fdr 1e-04).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1234.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.09×** | +16.5 | 0e+00 | 45/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +13.4 | 1e-38 | 36/39 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +11.6 | 6e-29 | 40/42 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +11.3 | 3e-27 | 43/47 (AsPC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +5.6 | 3e-06 | 32/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +5.5 | 4e-06 | 38/49 (COLO 205, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.3 | 9e-06 | 31/45 (HepG2/C3A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.2 | 1e-05 | 28/48 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +4.9 | 5e-05 | 33/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.39×** | +4.8 | 1e-04 | 29/47 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.006 | 23/48 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.3 | 0.053 | 17/34 (A-172, HOP62, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1234.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.644×** | -6.2 | 4e-07 | 37/48 (HepG2/C3A, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.663×** | -6.0 | 5e-07 | 33/48 (RKO, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.712×** | -5.0 | 1e-04 | 29/48 (hTERT-HPNE, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.731×** | -4.6 | 6e-04 | 26/48 (hTERT-HPNE, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.736×** | -4.5 | 8e-04 | 32/48 (KATO III, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.740×** | -4.4 | 0.001 | 24/48 (A-427, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.743×** | -4.3 | 0.001 | 31/48 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.762×** | -4.0 | 0.005 | 28/48 (LoVo, SW 1088, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.758×** | -3.9 | 0.006 | 25/48 (HT-29, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.780×** | -3.6 | 0.016 | 24/48 (H4, SW 900, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.783×** | -3.6 | 0.017 | 21/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.842× | -3.6 | 0.017 | 20/48 (A-427, SW1417, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -3.5 | 0.017 | 2/48 (AN3 CA, SW 1271) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.804×** | -3.2 | 0.060 | 21/48 (LS 180, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1234. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 90.4 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.5) | [[Verteporfin (drug)]] 5 µM 0.341× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 45.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 32.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +13.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 45.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +13.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 50.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +14.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 37.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 38.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 38.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 42.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 46.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.3) | — |
| [[A-172 (line)]] | wt | 46.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 48.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +10.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 35.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.0) | — |
| [[C32 (line)]] | wt | 57.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 83.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 76.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.0) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.136× (z -15.8) |
| [[HT-29 (line)]] | alt | 45.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 36.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 65.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +13.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 39.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -10.0) |
| [[SW 1088 (line)]] | alt | 85.1 | 0 | 2 | — | [[Sunitinib (drug)]] 0.05 µM 0.0701× (z -10.2) |
| [[SW480 (line)]] | alt | 38.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +14.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 25.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +8.8) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 39.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +9.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 51.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +9.8) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 65.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.291× (z -9.1) |
| [[J82 (line)]] | alt | 56.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 36.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 48.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +12.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 27.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 47.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1234), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDOST]] | +0.72 | +0.57 / +0.79 | both halves | 1e-05 |  |
| [[NCSTN]] | +0.67 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[NUCB1]] | +0.65 | +0.60 / +0.74 | both halves | 7e-06 | STRING 526 |
| [[PDIA3]] | +0.64 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[RNF167]] | +0.64 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PIGT]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[LAMP1]] | +0.63 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[RPN1]] | +0.62 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[CANX]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[FKBP9]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[GANAB]] | +0.61 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[TLN1]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRI1]] | -0.55 | -0.32 / -0.58 | both halves | 1e-04 |  |
| [[NT5C]] | -0.54 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[GTF2H2]] | -0.53 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[MRPL12]] | -0.53 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[METTL5]] | -0.53 | -0.26 / -0.59 | both halves | 4e-04 |  |
| [[PPP1R35]] ⚠ | -0.52 | -0.31 / -0.52 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PHF20]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[CELF1]] | -0.51 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[ORAI1]] | -0.51 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[CIAO1]] | -0.51 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[GGT7]] | -0.50 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[EXOC6]] | -0.49 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[POLM]] | -0.49 | -0.29 / -0.55 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SDF4's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.3, -22.1); signed map (-18.5, -33.1). **Vector** length 92.1, 23.0% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +11.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.4 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +5.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.4 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +1.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.9 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -3.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | stromal cell derived factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,216,931-1,232,031 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cab45 |
| Gene groups (HGNC) | CREC family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRK5](https://www.uniprot.org/uniprotkb/Q9BRK5) (45 kDa calcium-binding protein):

> May regulate calcium-dependent activities in the endoplasmic reticulum lumen or post-ER compartment.; Isoform 5 may be involved in the exocytosis of zymogens by pancreatic acini.

**Summary**, from NCBI Gene [51150](https://www.ncbi.nlm.nih.gov/gene/51150):

> This gene encodes a stromal cell derived factor that is a member of the CREC protein family. The encoded protein contains six EF-hand motifs and calcium-binding motifs. This protein localizes to the Golgi lumen and may be involved in regulating calcium dependent cellular activities. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:24188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24188) · Entrez [51150](https://www.ncbi.nlm.nih.gov/gene/51150) · UniProt [Q9BRK5](https://www.uniprot.org/uniprotkb/Q9BRK5) · Ensembl [ENSG00000078808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078808)

## Data

Gene col 1234: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1234); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1234, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1234]; `tensor/DDL_lfc|DDL_z.npy` [1234]; `embed/gene_vectors.npy` [1234]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1234 or target_col == 1234). Every well: [[SDF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
