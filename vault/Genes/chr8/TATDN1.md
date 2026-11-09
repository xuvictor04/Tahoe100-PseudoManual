---
symbol: "TATDN1"
type: "gene"
col: 7217
ensembl_id: "ENSG00000147687"
name: "TatD DNase domain containing 1"
location: "8q24.13"
module: 1
arm: "+"
pooled_cpm: 56.12
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TATDN1

*TatD DNase domain containing 1* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.30× (z +17.9, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.809× (z -4.6, q 0.002, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.315×, SHP-77 0.376×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.573×, A549 0.580×; ⚠ cell-cycle shift, explains ~1% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.567×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC4]] (+0.73, fdr 7e-06), [[MRPL45]] (+0.66, fdr 7e-06), [[NOL8]] (+0.66, fdr 7e-06); moves opposite to [[TWSG1]] (-0.63, fdr 1e-05), [[CALM3]] (-0.63, fdr 7e-06), [[GGH]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7217.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.30×** | +17.9 | 0e+00 | 45/47 (HT-29, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.93×** | +14.1 | 9e-43 | 46/48 (NCI-H1573, COLO 205, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.82×** | +12.2 | 8e-32 | 45/48 (NCI-H1573, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +11.8 | 4e-30 | 41/48 (HT-29, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +9.5 | 3e-19 | 39/48 (NCI-H1573, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +9.4 | 4e-19 | 37/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +8.8 | 2e-16 | 33/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +8.5 | 2e-15 | 28/47 (AsPC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +8.4 | 2e-15 | 35/48 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +8.1 | 3e-14 | 35/48 (NCI-H460, LoVo, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.6 | 2e-09 | 26/43 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.7 | 5e-07 | 24/47 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +4.9 | 3e-05 | 23/45 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.4 | 5e-04 | 23/48 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.002 | 19/47 (RPMI-7951, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.003 | 18/48 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.003 | 17/46 (LOX-IMVI, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.13× | +3.8 | 0.005 | 8/49 (SNU-423, AsPC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.7 | 0.006 | 15/48 (A498, NCI-H460, …) | top dose only |  |
| [[AZD1390 (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.006 | 16/47 (HCT15, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7217.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.315×, SHP-77 0.376×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.573×, A549 0.580×; ⚠ cell-cycle shift, explains ~1% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.567×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.809×** | -4.6 | 0.002 | 18/48 (SW480, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.884× | -3.8 | 0.039 | 17/48 (RKO, A549, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.861× | -3.2 | 0.22 | 13/47 (MIA PaCa-2, CFPAC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7217. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 119 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.72× (z +15.9) | — |
| [[NCI-H1573 (line)]] | alt | 68.7 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.25× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -9.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 45.4 | 6 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.85× (z +11.9) | — |
| [[KATO III (line)]] | alt | 54.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.4) | — |
| [[LoVo (line)]] | wt | 40.9 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.19× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 44.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.14× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 92.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.80× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.567× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 89.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 33.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 41.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.84× (z +15.2) | — |
| [[H4 (line)]] | wt | 41.1 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.14× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 64.0 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 60.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.43× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 56.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 62.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 53.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +8.9) | — |
| [[A-427 (line)]] | wt | 45.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.45× (z +8.9) | — |
| [[A498 (line)]] | wt | 48.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +9.2) | — |
| [[A549 (line)]] | wt | 69.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -8.7) ⚠ cell-cycle shift, explains ~1% of this change |
| [[CFPAC-1 (line)]] | alt | 29.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.97× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 45.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.04× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 79.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 72.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.75× (z +13.6) | — |
| [[LS 180 (line)]] | wt | 48.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +9.6) | — |
| [[RKO (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -9.1) ⚠ cell-cycle shift, explains ~1% of this change |
| [[RPMI-7951 (line)]] | alt | 62.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 64.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +9.1) | — |
| [[SW480 (line)]] | alt | 55.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7217), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC4]] | +0.73 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[MRPL45]] | +0.66 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[NOL8]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[DNAJC2]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[DNAJA3]] | +0.64 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[DPH5]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[NSRP1]] | +0.63 | +0.68 / +0.55 | both halves | 1e-05 | same gene group |
| [[JPX]] | +0.63 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[MLH3]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[FCF1]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[ZC3H8]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[DNAJC11]] | +0.61 | +0.67 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TWSG1]] | -0.63 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[CALM3]] | -0.63 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[GGH]] | -0.63 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[G3BP2]] | -0.62 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[BSG]] | -0.61 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[APLP1]] | -0.60 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[NPTN]] | -0.59 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[LAPTM4A]] | -0.58 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[PRKACA]] | -0.58 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[CLSTN1]] | -0.58 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[ABHD12]] | -0.58 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[MLEC]] | -0.57 | -0.65 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-40.4, -0.8); signed map (3.7, -24.1). **Vector** length 118, 32.7% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.7 | +17.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.6 | +12.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.0 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.9 | +9.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.9 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +14.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +11.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.8 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +3.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -6.4 | -3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.8 | +0.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | TatD DNase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:124,488,485-124,539,458 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDA11 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1N9](https://www.uniprot.org/uniprotkb/Q6P1N9) (Deoxyribonuclease TATDN1):

> Exhibits 3'-5' exonuclease and apurinic/apyrimidinic (AP) endonuclease activities (in vitro). Shows preferential AP endonuclease activity on dsDNA substrates and 3'-5' exonuclease activity on ssDNA. Catalyzes decatenation of catenated kinetoplast DNA to produce separated linear DNA in vitro (By similarity). Plays an important role in chromosomal segregation and cell cycle progression during eye development probably via its DNA decatenation activity (By similarity).

**Summary**, from NCBI Gene [83940](https://www.ncbi.nlm.nih.gov/gene/83940):

> Enables 3'-5'-DNA exonuclease activity and DNA endonuclease activity. Predicted to be involved in DNA metabolic process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24220](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24220) · Entrez [83940](https://www.ncbi.nlm.nih.gov/gene/83940) · UniProt [Q6P1N9](https://www.uniprot.org/uniprotkb/Q6P1N9) · Ensembl [ENSG00000147687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147687)

## Data

Gene col 7217: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7217); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7217, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7217]; `tensor/DDL_lfc|DDL_z.npy` [7217]; `embed/gene_vectors.npy` [7217]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7217 or target_col == 7217). Every well: [[TATDN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TATDN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
