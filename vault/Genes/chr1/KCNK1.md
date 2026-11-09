---
symbol: "KCNK1"
type: "gene"
col: 5752
ensembl_id: "ENSG00000135750"
name: "potassium two pore domain channel subfamily K member 1"
location: "1q42.2"
module: 31
arm: "+"
pooled_cpm: 133.97
n_lines_expressing: 27
n_dd_up: 8
n_dd_down: 26
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 61
direction_downstream: 82
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# KCNK1

*potassium two pore domain channel subfamily K member 1* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.26× (z +6.7, q 1e-08, up in 10 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.395× (z -26.9, q 0e+00, down in 25 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRSS3]] (+0.70, fdr 7e-06), [[FA2H]] (+0.67, fdr 7e-06), [[TMPRSS4]] (+0.64, fdr 7e-06); moves opposite to [[USP24]] (-0.52, fdr 4e-05), [[ERMARD]] (-0.48, fdr 3e-05), [[YAP1]] (-0.45, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 61 arrows point to it, the strongest [[FUT2]] → it (grade B ⚠); 82 go from it, the strongest it → [[RALGPS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5752.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.7 | 1e-08 | 10/25 (RKO, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +5.2 | 4e-05 | 16/25 (SW48, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +5.2 | 4e-05 | 12/24 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +4.9 | 2e-04 | 11/25 (KATO III, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.7 | 2e-04 | 10/26 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.26×** | +4.7 | 2e-04 | 8/26 (RKO, HOP62, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +4.5 | 6e-04 | 14/25 (SW48, LS 180, …) | rises with dose | low cells (technical?) |
| [[vincristine (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.020 | 10/25 (CFPAC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.023 | 5/26 (RKO, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.11 | 6/25 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | 1.11× | +3.1 | 0.12 | 2/25 (COLO 205, CHP-212) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5752.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.395×** | -26.9 | 0e+00 | 25/25 (NCI-H2347, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.352×** | -21.4 | 0e+00 | 25/25 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.374×** | -20.1 | 0e+00 | 25/25 (LS 180, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.373×** | -19.5 | 0e+00 | 25/25 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.440×** | -16.9 | 0e+00 | 25/25 (LoVo, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.630×** | -13.4 | 7e-39 | 24/26 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.540×** | -12.6 | 1e-34 | 22/25 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.544×** | -12.5 | 7e-34 | 21/25 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.591×** | -10.4 | 2e-23 | 25/25 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.611×** | -10.1 | 3e-22 | 24/25 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.634×** | -9.3 | 5e-19 | 24/25 (LoVo, SW 900, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.694×** | -7.2 | 3e-11 | 22/27 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **0.709×** | -7.1 | 8e-11 | 22/26 (LS 180, NCI-H2347, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.709×** | -6.8 | 5e-10 | 21/25 (COLO 205, NCI-H2347, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.792×** | -6.7 | 6e-10 | 18/25 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.814×** | -6.0 | 9e-08 | 15/25 (NCI-H2347, COLO 205, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.774×** | -5.0 | 2e-05 | 20/25 (NCI-H1792, A498, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.811×** | -4.3 | 5e-04 | 9/25 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.806×** | -4.1 | 0.001 | 7/25 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.846× | -3.4 | 0.015 | 4/26 (HOP62, RKO, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.893× | -3.3 | 0.021 | 7/25 (LS 180, LoVo, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.852× | -3.3 | 0.021 | 12/25 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 0.842× | -3.3 | 0.022 | 10/25 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | 0.845× | -3.1 | 0.038 | 9/26 (LoVo, KATO III, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 207 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -33.9) |
| [[CFPAC-1 (line)]] | alt | 267 | 1 | 15 (9 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.60× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -26.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.396× (z -16.6) |
| [[HT-29 (line)]] | alt | 216 | 0 | 16 (12 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0748× (z -27.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.189× (z -25.1) |
| [[NCI-H1573 (line)]] | alt | 175 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -27.1) |
| [[A498 (line)]] | wt | 171 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -30.0) |
| [[AsPC-1 (line)]] | alt | 899 | 0 | 14 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0752× (z -31.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.240× (z -16.6) |
| [[Hs 766T (line)]] | wt | 485 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -31.2) |
| [[LoVo (line)]] | wt | 695 | 0 | 14 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0640× (z -34.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.269× (z -23.4) |
| [[SW 900 (line)]] | alt | 278 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -28.1) |
| [[HOP62 (line)]] | alt | 85.6 | 0 | 13 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.123× (z -19.1) |
| [[Panc 03.27 (line)]] | alt | 204 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -17.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.407× (z -15.7) |
| [[COLO 205 (line)]] | alt | 190 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -30.2) |
| [[LS 180 (line)]] | wt | 399 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0814× (z -33.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.290× (z -23.2) |
| [[HEC-1-A (line)]] | alt | 82.4 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -28.6) |
| [[RKO (line)]] | wt | 116 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -26.2) |
| [[KATO III (line)]] | alt | 126 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.109× (z -26.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.250× (z -23.3) |
| [[A549 (line)]] | wt | 105 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -24.4) |
| [[NCI-H1792 (line)]] | alt | 122 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -16.0) |
| [[SW48 (line)]] | wt | 242 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -18.1) |
| [[CHP-212 (line)]] | wt | 129 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -14.9) |
| [[BT-474 (line)]] | alt | 125 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -13.3) |
| [[SW1417 (line)]] | alt | 38.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.283× (z -10.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -9.9) |
| [[HCT15 (line)]] | alt | 129 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -12.8) |
| [[J82 (line)]] | alt | 43.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -12.2) |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.196× (z -9.2) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 29.2 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 23.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 28.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.09 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 22.5 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.40 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.96 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.40 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 30.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 21.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRSS3]] | +0.70 | +0.65 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[FA2H]] | +0.67 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[DSG3]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[CLDN4]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[JUP]] | +0.63 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TTC9]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[HS3ST1]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ARHGAP30]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ADGRF1]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[DENND2C]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[NECTIN4]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP24]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ERMARD]] | -0.48 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[YAP1]] | -0.45 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[TRAF3IP2-AS1]] | -0.45 | -0.54 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 18, C 43. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT2]] | B | FUT2 activity raises KCNK1's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 4.45× lower at baseline in the lines without FUT2 | 0.006 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[CD55]] | B | CD55 activity raises KCNK1's level | lines that do not express CD55 (16) vs lines expressing it (34) | 3.62× lower at baseline in the lines without CD55 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL32, IL2RG, ENSG00000271933; maybe low, not absent |
| [[BMP2]] | B | BMP2 activity raises KCNK1's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 3.04× lower at baseline in the lines without BMP2 | 0.019 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[GRHL3]] | B | GRHL3 activity raises KCNK1's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 3.28× lower at baseline in the lines without GRHL3 | 0.030 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[IKZF2]] | B | IKZF2 activity raises KCNK1's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 2.66× lower at baseline in the lines without IKZF2 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[RALGPS2]] | B | RALGPS2 activity raises KCNK1's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 5.69× lower at baseline in the lines without RALGPS2 | 0.035 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[KCNK6]] | B | KCNK6 activity raises KCNK1's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 4.49× lower at baseline in the lines without KCNK6 | 0.037 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[GPRC5A]] | B | GPRC5A activity raises KCNK1's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 4.15× lower at baseline in the lines without GPRC5A | 0.039 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[TOP2A]] | B | TOP2A activity raises KCNK1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IFNLR1]] | B | IFNLR1 activity raises KCNK1's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 2.99× lower at baseline in the lines without IFNLR1 | 0.044 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[ABHD17C]] | B | ABHD17C activity raises KCNK1's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 3.98× lower at baseline in the lines without ABHD17C | 0.049 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[LYPD3]] | B | LYPD3 activity raises KCNK1's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 3.21× lower at baseline in the lines without LYPD3 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |

### Downstream of this gene

*82 arrows, 82 of them with an alert ⚠; grade A 0, B 38, C 44. Shown: the 12 strongest; 70 more arrows (70 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALGPS2]] | B | KCNK1 activity raises RALGPS2's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.94× lower at baseline in the lines without KCNK1 | 0.001 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[PLAUR]] | B | KCNK1 activity raises PLAUR's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.32× lower at baseline in the lines without KCNK1 | 0.005 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[IFNLR1]] | B | KCNK1 activity raises IFNLR1's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.48× lower at baseline in the lines without KCNK1 | 0.006 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[MCU]] | B | KCNK1 activity raises MCU's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 1.59× lower at baseline in the lines without KCNK1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[TRAF3IP2-AS1]] | B | KCNK1 activity lowers TRAF3IP2-AS1's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 1.82× higher at baseline in the lines without KCNK1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[ABHD17C]] | B | KCNK1 activity raises ABHD17C's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.54× lower at baseline in the lines without KCNK1 | 0.010 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[RHPN2]] | B | KCNK1 activity raises RHPN2's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.63× lower at baseline in the lines without KCNK1 | 0.011 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[FUT2]] | B | KCNK1 activity raises FUT2's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without KCNK1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[CD55]] | B | KCNK1 activity raises CD55's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.87× lower at baseline in the lines without KCNK1 | 0.017 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[GPRC5A]] | B | KCNK1 activity raises GPRC5A's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 3.52× lower at baseline in the lines without KCNK1 | 0.019 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[FBXO34]] | B | KCNK1 activity strengthens FBXO34's drug response | lines that do not express KCNK1 (23) vs lines expressing it (26) | the lines without KCNK1 respond 0.73× as strongly (z diff +1.49); strongest at Homoharringtonine 5 µM: 0.77x vs 0.61x (z diff +3.2) | 0.020 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132; target measured in part of the lines; artifact flags |
| [[GCKR]] | B | KCNK1 activity raises GCKR's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 1.50× lower at baseline in the lines without KCNK1 | 0.020 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.3, 56.6); signed map (56.1, 8.2). **Vector** length 116, 39.3% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.3 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.8 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +4.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.7 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -19.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -10.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -12.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.9 | -2.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.8 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -5.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | potassium two pore domain channel subfamily K member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:233,614,106-233,672,514 (+) |
| Ensembl biotype | protein_coding |
| Also known as | K2p1.1, DPK, TWIK-1 |
| Gene groups (HGNC) | Potassium two pore domain channel subfamily K; MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: Tandem pore domain potassium channels; Phase 4 - resting membrane potential; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [O00180](https://www.uniprot.org/uniprotkb/O00180) (Potassium channel subfamily K member 1):

> Ion channel that contributes to passive transmembrane potassium transport and to the regulation of the resting membrane potential in brain astrocytes, but also in kidney and in other tissues. Forms dimeric channels through which potassium ions pass in accordance with their electrochemical gradient. The channel is selective for K(+) ions at physiological potassium concentrations and at neutral pH, but becomes permeable to Na(+) at subphysiological K(+) levels and upon acidification of the …

**Summary**, from NCBI Gene [3775](https://www.ncbi.nlm.nih.gov/gene/3775):

> This gene encodes one of the members of the superfamily of potassium channel proteins containing two pore-forming P domains. The product of this gene has not been shown to be a functional channel, however, it may require other non-pore-forming proteins for activity. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6272) · Entrez [3775](https://www.ncbi.nlm.nih.gov/gene/3775) · UniProt [O00180](https://www.uniprot.org/uniprotkb/O00180) · Ensembl [ENSG00000135750](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135750)

## Data

Gene col 5752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5752); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5752]; `tensor/DDL_lfc|DDL_z.npy` [5752]; `embed/gene_vectors.npy` [5752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5752 or target_col == 5752). Every well: [[KCNK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
