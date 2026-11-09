---
symbol: "NUMA1"
type: "gene"
col: 6024
ensembl_id: "ENSG00000137497"
name: "nuclear mitotic apparatus protein 1"
location: "11q13.4"
module: 22
arm: "+"
pooled_cpm: 115.44
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# NUMA1

*nuclear mitotic apparatus protein 1* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.76× (z +10.6, q 2e-23, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.589× (z -9.9, q 3e-20, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INCENP]] (+0.70, fdr 7e-06), [[SPAG5]] (+0.67, fdr 7e-06), [[KIF22]] (+0.67, fdr 7e-06); moves opposite to [[CDKL1]] (-0.51, fdr 4e-05), [[ZC3H8]] (-0.50, fdr 6e-05), [[PRKAG1]] (-0.50, fdr 1e-04).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.76×** | +10.6 | 2e-23 | 43/48 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +9.2 | 1e-17 | 40/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +7.0 | 5e-10 | 34/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +6.9 | 5e-10 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.5 | 5e-06 | 1/50 (MIA PaCa-2) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.006 | 25/49 (SW1417, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.006 | 26/48 (NCI-H23, KATO III, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.8 | 0.012 | 24/47 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.042 | 20/48 (C32, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.053 | 24/47 (MIA PaCa-2, SW48, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6024.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.589×** | -9.9 | 3e-20 | 40/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.664×** | -7.6 | 6e-12 | 37/48 (SW 900, HEC-1-A, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -7.0 | 6e-10 | 37/47 (C32, LS 180, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.787×** | -6.3 | 3e-08 | 28/49 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.808×** | -5.6 | 2e-06 | 28/48 (LS 180, Panc 03.27, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.777×** | -4.5 | 5e-04 | 22/44 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -4.5 | 5e-04 | 24/48 (C32, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.797×** | -4.0 | 0.004 | 25/48 (Hs 766T, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.781×** | -4.0 | 0.004 | 34/49 (NCI-H2030, SW1417, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | **0.808×** | -4.0 | 0.004 | 22/49 (HCT15, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.791×** | -3.8 | 0.007 | 30/49 (AN3 CA, HT-29, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.684×** | -3.7 | 0.010 | 24/48 (NCI-H1792, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.825×** | -3.6 | 0.013 | 23/49 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.701×** | -3.5 | 0.020 | 22/48 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.811×** | -3.4 | 0.025 | 20/48 (NCI-H2347, SHP-77, …) | inconsistent across doses |  |
| [[Fumaric acid (drug)]] 0.5 µM |  | 0.840× | -3.3 | 0.037 | 16/48 (A549, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.740×** | -2.9 | 0.092 | 18/48 (HCT15, Panc 03.27, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 0.895× | -2.9 | 0.092 | 8/48 (A549, NCI-H2347, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 129 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.353× (z -10.7) |
| [[PANC-1 (line)]] | alt | 115 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +12.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.502× (z -9.0) |
| [[LoVo (line)]] | wt | 71.7 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +14.1) | — |
| [[NCI-H23 (line)]] | alt | 149 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.341× (z -12.2) |
| [[SW480 (line)]] | alt | 154 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.49× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +12.6) | — |
| [[AsPC-1 (line)]] | alt | 123 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.428× (z -10.0) |
| [[HT-29 (line)]] | alt | 163 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +9.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.434× (z -10.0) |
| [[LS 180 (line)]] | wt | 154 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +11.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.468× (z -9.2) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 126 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +11.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.492× (z -8.5) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 75.1 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.97× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -9.8) |
| [[SW 900 (line)]] | alt | 124 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.374× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 125 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.426× (z -10.3) |
| [[CHP-212 (line)]] | wt | 134 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -9.7) |
| [[COLO 205 (line)]] | alt | 85.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -11.2) |
| [[HOP62 (line)]] | alt | 80.8 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.12× (z +8.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +8.5) | — |
| [[J82 (line)]] | alt | 143 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +13.1) | — |
| [[KATO III (line)]] | alt | 150 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.56× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 104 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -14.6) |
| [[RKO (line)]] | wt | 102 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 148 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +12.3) | — |
| [[A-427 (line)]] | wt | 160 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.510× (z -9.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 89.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[AN3 CA (line)]] | alt | 168 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -10.5) |
| [[H4 (line)]] | wt | 108 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -9.7) |
| [[HCT15 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[HEC-1-A (line)]] | alt | 131 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.527× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 87.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -12.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 165 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -12.0) |
| [[SHP-77 (line)]] | alt | 203 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.428× (z -8.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 59.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -10.5) |
| [[A-172 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 117 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 134 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 86.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 86.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 99.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INCENP]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 432 |
| [[SPAG5]] | +0.67 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[KIF22]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 453 |
| [[FOXM1]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[NCAPD2]] | +0.65 | +0.57 / +0.62 | both halves | 1e-05 | pathway: Mitotic Prometaphase |
| [[KIFC1]] | +0.62 | +0.66 / +0.53 | both halves | 1e-05 | STRING 749 |
| [[RACGAP1]] | +0.61 | +0.56 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[HMG20B]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PSRC1]] | +0.61 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[H2AZ2]] | +0.60 | +0.54 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[CDCA3]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[STMN1]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL1]] | -0.51 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[ZC3H8]] | -0.50 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[PRKAG1]] | -0.50 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[TATDN1]] | -0.50 | -0.61 / -0.33 | both halves | 1e-04 | same gene group |
| [[NDUFB9]] | -0.49 | -0.61 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.5, -54.0); signed map (-47.4, -41.4). **Vector** length 127, 38.1% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.50 to 8); *Polo-like kinase mediated events* (reactome, mean cos +0.50 to 7); *Kinesins* (reactome, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +8.6 | +10.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +9.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.4 | +6.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.3 | +7.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +6.1 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +1.7 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +3.0 | +3.0 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +2.7 | +0.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.6 | +1.8 |
|  | [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | +2.5 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.1 | -9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.0 | -7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | -4.3 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -4.0 | -3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.9 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | nuclear mitotic apparatus protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:72,002,864-72,080,693 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NUMA |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 6 pathways, smallest: Recruitment of NuMA to mitotic centrosomes; Mitotic Prophase; Mitotic Prometaphase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14980](https://www.uniprot.org/uniprotkb/Q14980) (Nuclear mitotic apparatus protein 1):

> Microtubule (MT)-binding protein that plays a role in the formation and maintenance of the spindle poles and the alignement and the segregation of chromosomes during mitotic cell division. Functions to tether the minus ends of MTs at the spindle poles, which is critical for the establishment and maintenance of the spindle poles. Plays a role in the establishment of the mitotic spindle orientation during metaphase and elongation during anaphase in a dynein-dynactin-dependent manner. In …

**Summary**, from NCBI Gene [4926](https://www.ncbi.nlm.nih.gov/gene/4926):

> This gene encodes a large protein that forms a structural component of the nuclear matrix. The encoded protein interacts with microtubules and plays a role in the formation and organization of the mitotic spindle during cell division. Chromosomal translocation of this gene with the RARA (retinoic acid receptor, alpha) gene on chromosome 17 have been detected in patients with acute promyelocytic leukemia. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:8059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8059) · Entrez [4926](https://www.ncbi.nlm.nih.gov/gene/4926) · UniProt [Q14980](https://www.uniprot.org/uniprotkb/Q14980) · Ensembl [ENSG00000137497](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137497)

## Data

Gene col 6024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6024); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6024]; `tensor/DDL_lfc|DDL_z.npy` [6024]; `embed/gene_vectors.npy` [6024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6024 or target_col == 6024). Every well: [[NUMA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUMA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
