---
symbol: "CPLANE1"
type: "gene"
col: 12430
ensembl_id: "ENSG00000197603"
name: "ciliogenesis and planar polarity effector complex subunit 1"
location: "5p13.2"
module: 105
arm: "+"
pooled_cpm: 93.47
n_lines_expressing: 45
n_dd_up: 10
n_dd_down: 24
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# CPLANE1

*ciliogenesis and planar polarity effector complex subunit 1* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.35× (z +4.2, q 0.010, up in 27 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (15 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.351× (z -14.6, q 1e-45, down in 42 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.516× (z -13.0, q 2e-36, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YTHDC2]] (+0.71, fdr 7e-06), [[SENP6]] (+0.70, fdr 7e-06), [[ZNF644]] (+0.67, fdr 1e-05); moves opposite to [[INSIG2]] (-0.66, fdr 7e-06), [[WDR45B]] (-0.65, fdr 7e-06), [[SLC2A1-DT]] (-0.64, fdr 1e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[AZGP1]] → it (grade B ⚠); 3 go from it, the strongest it → [[TMEM63A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12430.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +4.2 | 0.010 | 27/43 (SW480, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.010 | 28/43 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.73×** | +4.0 | 0.010 | 34/45 (NCI-H460, SNU-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.8 | 0.018 | 25/43 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.34×** | +3.6 | 0.030 | 25/45 (NCI-H460, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.030 | 21/44 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.041 | 25/42 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +3.4 | 0.041 | 17/43 (LOX-IMVI, BT-474, …) | top dose only | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.041 | 21/42 (NCI-H460, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.072 | 21/43 (NCI-H460, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.25×** | +3.2 | 0.083 | 20/43 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.24× | +3.0 | 0.12 | 18/44 (CFPAC-1, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12430.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.351×** | -14.6 | 1e-45 | 42/43 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.516×** | -13.0 | 2e-36 | 40/44 (Hs 766T, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.401×** | -12.7 | 7e-35 | 40/43 (SW480, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.410×** | -12.4 | 2e-33 | 43/43 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.410×** | -12.4 | 2e-33 | 42/43 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.453×** | -11.0 | 2e-26 | 42/43 (LoVo, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.508×** | -9.4 | 3e-19 | 35/43 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.509×** | -9.4 | 4e-19 | 38/43 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.322×** | -8.3 | 8e-15 | 40/44 (NCI-H23, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.553×** | -8.3 | 8e-15 | 37/43 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.408×** | -6.5 | 3e-09 | 32/43 (HOP62, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.639×** | -6.0 | 1e-07 | 26/43 (NCI-H23, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.669×** | -5.6 | 9e-07 | 31/43 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.660×** | -5.6 | 1e-06 | 31/45 (NCI-H23, SW 900, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.680×** | -5.2 | 1e-05 | 27/42 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.754×** | -3.9 | 0.003 | 24/43 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.841× | -3.4 | 0.020 | 13/44 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.785×** | -3.2 | 0.031 | 21/43 (NCI-H460, hTERT-HPNE, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.800×** | -3.1 | 0.047 | 21/43 (NCI-H23, J82, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.862× | -2.9 | 0.089 | 11/44 (A-172, HCT15, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.814×** | -2.8 | 0.099 | 17/43 (NCI-H2030, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12430. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 216 | 0 | 13 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.155× (z -11.2) |
| [[HOP62 (line)]] | alt | 113 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -19.0) |
| [[LOX-IMVI (line)]] | wt | 58.8 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -14.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.301× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 110 | 0 | 11 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.406× (z -9.6) |
| [[SW480 (line)]] | alt | 73.4 | 1 (1 ⚠) | 10 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.142× (z -22.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.466× (z -8.9) |
| [[LoVo (line)]] | wt | 177 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -23.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -15.8) |
| [[HS-578T (line)]] | alt | 92.2 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -16.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -14.0) |
| [[J82 (line)]] | alt | 155 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 134 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -12.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.289× (z -12.8) |
| [[A-172 (line)]] | wt | 182 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -15.9) |
| [[Hs 766T (line)]] | wt | 117 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -19.4) |
| [[NCI-H1792 (line)]] | alt | 98.8 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -15.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 87.3 | 0 | 6 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.194× (z -15.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -14.0) |
| [[SNU-423 (line)]] | alt | 92.4 | 0 | 6 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.239× (z -12.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.3) |
| [[A549 (line)]] | wt | 112 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -13.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.1) |
| [[PANC-1 (line)]] | alt | 86.0 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -14.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -8.9) |
| [[A-427 (line)]] | wt | 180 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.419× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 59.6 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -11.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -9.8) |
| [[C-33 A (line)]] | alt | 135 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.330× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 39.3 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.184× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 139 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -10.6) |
| [[SHP-77 (line)]] | alt | 116 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.370× (z -9.9) |
| [[SW 900 (line)]] | alt | 89.9 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -13.0) |
| [[SW1417 (line)]] | alt | 67.9 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -9.8) |
| [[RKO (line)]] | wt | 75.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 66.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 87.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -10.5) |
| [[SNU-1 (line)]] | wt | 128 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.290× (z -10.4) |
| [[SW 1088 (line)]] | alt | 124 | 0 | 2 | — | [[Crizotinib (hydrochloride) (drug)]] 0.05 µM 0.0691× (z -8.6) |
| [[A498 (line)]] | wt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -8.6) |
| [[H4 (line)]] | wt | 70.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -8.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 175 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.37 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 19.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12430), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YTHDC2]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[SENP6]] | +0.70 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ZNF644]] | +0.67 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[CNTLN]] | +0.66 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[ZMYM4]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ZNF280D]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[DLG5]] | +0.62 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[VPS35L]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[EPC2]] | +0.60 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[BAZ1B]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[USP47]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INSIG2]] | -0.66 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[WDR45B]] | -0.65 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[SLC2A1-DT]] | -0.64 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[ANKRD37]] | -0.64 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[POM121]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[FAM117B]] | -0.63 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[PDXP]] | -0.62 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[QSOX1]] | -0.62 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[SPICE1]] | -0.61 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[AK2]] | -0.60 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[KIAA1958]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AZGP1]] | B | AZGP1 activity lowers CPLANE1's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 2.85× higher at baseline in the lines without AZGP1 | 0.028 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ |
| [[MAP2K1]] | B | MAP2K1 activity lowers CPLANE1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[CCDC102A]] | B | CCDC102A activity raises CPLANE1's level | lines that do not express CCDC102A (5) vs lines expressing it (45) | 4.48× lower at baseline in the lines without CCDC102A | 0.062 | ⚠ within organs, on part of the lines; also absent: CYP46A1, TMOD2, DPF1; maybe low, not absent |
| [[ULK2]] | B | ULK2 activity raises CPLANE1's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 2.31× lower at baseline in the lines without ULK2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[MAP2K2]] | B | MAP2K2 activity lowers CPLANE1's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ZNF480]] | C | ZNF480 activity raises CPLANE1's level | lines that do not express ZNF480 (3) vs lines expressing it (47) | 5.17× lower at baseline in the lines without ZNF480 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP14, CIBAR1, ZNF540; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM63A]] | B | CPLANE1 activity lowers TMEM63A's level | lines that do not express CPLANE1 (5) vs lines expressing it (45) | 1.80× higher at baseline in the lines without CPLANE1 | 0.060 | ⚠ within organs, on part of the lines; also absent: NKAIN1, SIX4, TPST1; maybe low, not absent; its own permutation p |
| [[AZGP1]] | B | CPLANE1 activity lowers AZGP1's level | lines that do not express CPLANE1 (5) vs lines expressing it (45) | 11.00× higher at baseline in the lines without CPLANE1 | 0.079 | ⚠ within organs, on part of the lines; also absent: NKAIN1, SIX4, TPST1; maybe low, not absent |
| [[NCBP3]] | B | CPLANE1 activity raises NCBP3's level | lines that do not express CPLANE1 (5) vs lines expressing it (45) | 1.26× lower at baseline in the lines without CPLANE1 | 0.089 | ⚠ within organs, on part of the lines; also absent: NKAIN1, SIX4, TPST1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction -0.702). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.2, 12.5); signed map (12.0, -33.2). **Vector** length 111, 39.5% of its response variance represented; |z| ≥ 3 in 1,305 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +8.0 | +1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.4 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.2 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.9 | +4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | -0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.0 | +4.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -13.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -9.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.4 | -11.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.3 | -12.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.1 | -12.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -6.5 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | -1.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ciliogenesis and planar polarity effector complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:37,106,228-37,249,376 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13231, JBTS17, Hug; previously C5orf42 |
| Gene groups (HGNC) | Ciliogenesis and planar polarity effector complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H799](https://www.uniprot.org/uniprotkb/Q9H799) (Ciliogenesis and planar polarity effector 1):

> Involved in ciliogenesis. Involved in the establishment of cell polarity required for directional cell migration. Proposed to act in association with the CPLANE (ciliogenesis and planar polarity effectors) complex. Involved in recruitment of peripheral IFT-A proteins to basal bodies (By similarity).

**Summary**, from NCBI Gene [65250](https://www.ncbi.nlm.nih.gov/gene/65250):

> The protein encoded by this gene has putative coiled-coil domains and may be a transmembrane protein. Defects in this gene are a cause of Joubert syndrome (JBTS). [provided by RefSeq, May 2012]

**Accessions** — [HGNC:25801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25801) · Entrez [65250](https://www.ncbi.nlm.nih.gov/gene/65250) · UniProt [Q9H799](https://www.uniprot.org/uniprotkb/Q9H799) · Ensembl [ENSG00000197603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197603)

## Data

Gene col 12430: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12430); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12430, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12430]; `tensor/DDL_lfc|DDL_z.npy` [12430]; `embed/gene_vectors.npy` [12430]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12430 or target_col == 12430). Every well: [[CPLANE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPLANE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
