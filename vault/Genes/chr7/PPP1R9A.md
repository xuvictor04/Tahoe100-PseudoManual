---
symbol: "PPP1R9A"
type: "gene"
col: 8170
ensembl_id: "ENSG00000158528"
name: "protein phosphatase 1 regulatory subunit 9A"
location: "7q21.3"
module: 16
arm: "+"
pooled_cpm: 90.15
n_lines_expressing: 34
n_dd_up: 13
n_dd_down: 24
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 16
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# PPP1R9A

*protein phosphatase 1 regulatory subunit 9A* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.44× (z +5.2, q 1e-04, up in 23 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.356× (z -14.5, q 1e-44, down in 29 of 32 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.540× (z -12.2, q 3e-32, down in 27 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARD3B]] (+0.80, fdr 7e-06), [[IQCH-AS1]] (+0.65, fdr 7e-06), [[AASDHPPT]] (+0.65, fdr 8e-06); moves opposite to [[SDHAP4-1]] (-0.58, fdr 1e-05), [[MYO9B]] (-0.57, fdr 1e-05), [[SDHAP1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC16A9]] → it (grade B ⚠); 16 go from it, the strongest it → [[MTPAP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8170.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +5.2 | 1e-04 | 23/32 (NCI-H2347, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +4.9 | 3e-04 | 24/32 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.035 | 17/32 (SW480, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.6 | 0.035 | 16/32 (NCI-H2347, SW480, …) | all doses, flat | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.035 | 18/32 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.036 | 18/32 (J82, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.036 | 17/32 (A-427, NCI-H2347, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.036 | 18/34 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.31×** | +3.4 | 0.036 | 18/34 (SW480, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.049 | 15/32 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.073 | 13/33 (SW480, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.095 | 9/33 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.24×** | +3.1 | 0.095 | 14/33 (NCI-H2347, LOX-IMVI, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.096 | 19/31 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.096 | 14/32 (SW480, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8170.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.356×** | -14.5 | 1e-44 | 29/32 (HEC-1-A, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.382×** | -13.5 | 5e-39 | 26/31 (LoVo, SNU-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.392×** | -13.1 | 5e-37 | 29/32 (HEC-1-A, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.402×** | -12.8 | 3e-35 | 30/32 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.404×** | -12.7 | 5e-35 | 26/32 (SNU-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.540×** | -12.2 | 3e-32 | 27/33 (HepG2/C3A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.438×** | -11.6 | 5e-29 | 26/32 (LoVo, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.444×** | -11.4 | 4e-28 | 26/32 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.447×** | -11.3 | 1e-27 | 26/32 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.545×** | -8.5 | 1e-15 | 26/32 (SW48, HCT15, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.553×** | -8.0 | 9e-14 | 27/31 (RKO, SW480, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.608×** | -6.7 | 1e-09 | 21/34 (NCI-H23, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.631×** | -6.4 | 5e-09 | 24/32 (SW48, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.418×** | -6.4 | 7e-09 | 27/33 (NCI-H23, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.631×** | -6.2 | 2e-08 | 21/31 (SK-MEL-2, RKO, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.448×** | -5.9 | 1e-07 | 27/31 (HEC-1-A, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.648×** | -5.7 | 3e-07 | 24/32 (HepG2/C3A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.807×** | -2.9 | 0.097 | 16/32 (RKO, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.63 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8170. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 288 | 0 | 15 (11 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -20.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.210× (z -16.3) |
| [[NCI-H23 (line)]] | alt | 157 | 0 | 14 (9 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.238× (z -15.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -14.6) |
| [[SW480 (line)]] | alt | 135 | 1 (1 ⚠) | 13 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.236× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -14.4) |
| [[RKO (line)]] | wt | 277 | 0 | 11 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.166× (z -17.0) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.279× (z -12.6) |
| [[HT-29 (line)]] | alt | 122 | 1 (1 ⚠) | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -14.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.345× (z -10.4) |
| [[LoVo (line)]] | wt | 194 | 0 | 10 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.258× (z -16.6) |
| [[SW48 (line)]] | wt | 203 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -16.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.154× (z -13.7) |
| [[LS 180 (line)]] | wt | 206 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -18.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.367× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 192 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -21.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.445× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 105 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -11.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.250× (z -11.9) |
| [[A-427 (line)]] | wt | 200 | 0 | 5 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.312× (z -14.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.398× (z -11.8) |
| [[A498 (line)]] | wt | 96.7 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.369× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.398× (z -10.0) |
| [[HCT15 (line)]] | alt | 168 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.267× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.346× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 130 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -14.3) |
| [[NCI-H2030 (line)]] | alt | 148 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 137 | 0 | 5 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -13.5) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -10.9) |
| [[A549 (line)]] | wt | 200 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.214× (z -13.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -13.3) |
| [[C-33 A (line)]] | alt | 204 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -17.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 223 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 86.4 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -12.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.9) |
| [[SW 900 (line)]] | alt | 82.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.278× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -9.0) |
| [[AN3 CA (line)]] | alt | 345 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 62.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.15× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -8.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW1417 (line)]] | alt | 81.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -11.2) |
| [[J82 (line)]] | alt | 37.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -10.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.296× (z -9.3) |
| [[BT-474 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.290× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[CHP-212 (line)]] | wt | 64.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -10.2) |
| [[A-172 (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.98 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.01 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.55 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.85 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.99 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8170), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARD3B]] | +0.80 | +0.76 / +0.78 | both halves | 7e-06 | same gene group |
| [[IQCH-AS1]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.65 | +0.63 / +0.57 | both halves | 8e-06 |  |
| [[THOC7]] | +0.64 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[DIS3L]] | +0.64 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[REPIN1]] | +0.63 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[ZNF280D]] | +0.63 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[ZMYM4]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[PHACTR2]] | +0.62 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[FOXP1]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[GCFC2]] | +0.61 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[STK33]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP4-1]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.57 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ASB16-AS1]] | -0.57 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[MAP2K1]] | -0.56 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[WDR37]] | -0.56 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[DRD4]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[BET1L]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[DPM1]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[VRK3]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SDF2]] | -0.55 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SWI5]] | -0.55 | -0.49 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A9]] | B | SLC16A9 activity raises PPP1R9A's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 2.97× lower at baseline in the lines without SLC16A9 | 0.032 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |
| [[DENND2D]] | B | DENND2D activity raises PPP1R9A's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.38× lower at baseline in the lines without DENND2D | 0.050 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTPAP]] | B | PPP1R9A activity raises MTPAP's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 1.72× lower at baseline in the lines without PPP1R9A | 0.007 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[ADGRA3]] | B | PPP1R9A activity raises ADGRA3's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without PPP1R9A | 0.013 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[DCDC2]] | B | PPP1R9A activity raises DCDC2's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 2.72× lower at baseline in the lines without PPP1R9A | 0.017 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[BET1L]] | B | PPP1R9A activity lowers BET1L's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 1.60× higher at baseline in the lines without PPP1R9A | 0.020 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[DNAAF2]] | B | PPP1R9A activity raises DNAAF2's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 1.55× lower at baseline in the lines without PPP1R9A | 0.048 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[DENND2D]] | B | PPP1R9A activity raises DENND2D's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 1.94× lower at baseline in the lines without PPP1R9A | 0.068 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| cells under [[Carbamazepine (drug)]] 0.5 µM | B | PPP1R9A activity raises the cells' numbers under Carbamazepine 0.5 µM (protects the cells) | lines that do not express PPP1R9A (16) vs lines expressing it (32) | the lines without PPP1R9A: 0.81× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| cells under [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM | B | PPP1R9A activity lowers the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (makes them more sensitive) | lines that do not express PPP1R9A (16) vs lines expressing it (32) | the lines without PPP1R9A: 1.19× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[BMI1]] | B | PPP1R9A activity raises BMI1's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 1.57× lower at baseline in the lines without PPP1R9A | 0.087 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| cells under [[Cabozantinib (S-malate) (drug)]] 5 µM | B | PPP1R9A activity raises the cells' numbers under Cabozantinib (S-malate) 5 µM (protects the cells) | lines that do not express PPP1R9A (16) vs lines expressing it (32) | the lines without PPP1R9A: 0.83× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[PPP1R32]] | B | PPP1R9A activity lowers PPP1R32's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 1.21× higher at baseline in the lines without PPP1R9A | 0.091 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| cells under [[Clopidogrel (drug)]] 0.05 µM | B | PPP1R9A activity lowers the cells' numbers under Clopidogrel 0.05 µM (makes them more sensitive) | lines that do not express PPP1R9A (16) vs lines expressing it (32) | the lines without PPP1R9A: 1.30× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.504). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-19.9, 5.8); signed map (14.4, -31.6). **Vector** length 122, 39.8% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +8.5 | +2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.5 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.6 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.9 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +4.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.4 | +0.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.1 | -14.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.8 | -13.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.7 | -12.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -12.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 9A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:94,907,202-95,296,415 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Neurabin-I, KIAA1222, FLJ20068 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Sterile alpha motif domain containing; PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULJ8](https://www.uniprot.org/uniprotkb/Q9ULJ8) (Neurabin-1):

> Binds to actin filaments (F-actin) and shows cross-linking activity. Binds along the sides of the F-actin. May be involved in neurite formation. Inhibits protein phosphatase 1-alpha activity (By similarity).

**Summary**, from NCBI Gene [55607](https://www.ncbi.nlm.nih.gov/gene/55607):

> This gene is imprinted, and located in a cluster of imprinted genes on chromosome 7q12. This gene is transcribed in both neuronal and multiple embryonic tissues, and it is maternally expressed mainly in embryonic skeletal muscle tissues and biallelically expressed in other embryonic tissues. The protein encoded by this gene includes a PDZ domain and a sterile alpha motif (SAM). It is a regulatory subunit of protein phosphatase I, and controls actin cytoskeleton reorganization. Alternatively …

**Accessions** — [HGNC:14946](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14946) · Entrez [55607](https://www.ncbi.nlm.nih.gov/gene/55607) · UniProt [Q9ULJ8](https://www.uniprot.org/uniprotkb/Q9ULJ8) · Ensembl [ENSG00000158528](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158528)

## Data

Gene col 8170: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8170); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8170, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8170]; `tensor/DDL_lfc|DDL_z.npy` [8170]; `embed/gene_vectors.npy` [8170]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8170 or target_col == 8170). Every well: [[PPP1R9A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R9A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
