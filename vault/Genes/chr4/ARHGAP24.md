---
symbol: "ARHGAP24"
type: "gene"
col: 6199
ensembl_id: "ENSG00000138639"
name: "Rho GTPase activating protein 24"
location: "4q21.23-q21.3"
module: 121
arm: "+"
pooled_cpm: 73.89
n_lines_expressing: 33
n_dd_up: 22
n_dd_down: 31
n_dd_up_clean: 21
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 11
direction_downstream: 7
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# ARHGAP24

*Rho GTPase activating protein 24* — 4q21.23-q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.02× (z +12.1, q 4e-31, up in 21 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.334× (z -13.3, q 2e-37, down in 29 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEX41]] (+0.73, fdr 7e-06), [[RBMS3]] (+0.71, fdr 7e-06), [[CACNA2D1]] (+0.68, fdr 3e-05); moves opposite to [[PRKCZ]] (-0.59, fdr 1e-05), [[CAPN10]] (-0.59, fdr 1e-05), [[CTNNBIP1]] (-0.57, fdr 3e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TRPS1]] → it (grade B ⚠); 7 go from it, the strongest it → [[TRPS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +12.1 | 4e-31 | 21/31 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.41×** | +10.3 | 2e-22 | 27/31 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +7.0 | 5e-10 | 19/31 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.62×** | +5.9 | 6e-07 | 20/33 (C32, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.62×** | +5.7 | 2e-06 | 22/30 (NCI-H2347, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +5.4 | 5e-06 | 19/31 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.4 | 5e-06 | 17/31 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.36×** | +5.2 | 2e-05 | 20/31 (C32, BT-474, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.31×** | +4.6 | 2e-04 | 18/31 (NCI-H1792, BT-474, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +4.6 | 3e-04 | 18/31 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.48×** | +4.4 | 5e-04 | 18/31 (C32, NCI-H2347, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.44×** | +4.3 | 1e-03 | 17/31 (C32, A549, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.92×** | +4.2 | 0.001 | 21/33 (NCI-H2347, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.38×** | +3.9 | 0.004 | 13/31 (SHP-77, A-172, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.004 | 18/31 (C32, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.006 | 15/31 (C32, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6199.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.334×** | -13.3 | 2e-37 | 29/31 (LOX-IMVI, SNU-423, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.377×** | -11.8 | 7e-30 | 30/31 (SNU-423, H4, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.400×** | -11.1 | 2e-26 | 27/31 (SW 900, H4, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.429×** | -10.3 | 2e-22 | 29/31 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.454×** | -9.2 | 3e-18 | 22/30 (A498, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.492×** | -8.6 | 7e-16 | 27/31 (SW 900, PANC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.537×** | -7.5 | 4e-12 | 24/31 (SW 900, H4, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.368×** | -7.4 | 1e-11 | 25/32 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.522×** | -7.3 | 2e-11 | 22/30 (J82, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.622×** | -5.8 | 5e-07 | 24/31 (SW 900, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.728×** | -5.4 | 3e-06 | 23/32 (SHP-77, CHP-212, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.628×** | -5.3 | 5e-06 | 21/31 (H4, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.663×** | -5.0 | 3e-05 | 20/31 (NCI-H1792, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.673×** | -4.8 | 7e-05 | 17/31 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.472×** | -4.8 | 7e-05 | 20/31 (J82, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.704×** | -4.3 | 7e-04 | 20/32 (SW 900, LOX-IMVI, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.706×** | -4.1 | 0.001 | 17/30 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.717×** | -4.0 | 0.002 | 20/31 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.728×** | -3.7 | 0.006 | 17/31 (Panc 03.27, LS 180, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.584×** | -3.4 | 0.016 | 17/31 (SNU-423, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 160 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 59.0 | 9 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +27.8) | [[Auranofin (drug)]] 5 µM 0.253× (z -11.2) |
| [[H4 (line)]] | wt | 247 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -14.6) |
| [[SW 900 (line)]] | alt | 108 | 4 (2 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +11.1) | [[Auranofin (drug)]] 5 µM 0.136× (z -15.6) |
| [[hTERT-HPNE (line)]] | wt | 342 | 1 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.0681× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.146× (z -11.1) |
| [[J82 (line)]] | alt | 164 | 2 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.247× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 199 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -17.1) |
| [[PANC-1 (line)]] | alt | 138 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.10× (z +27.6) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.372× (z -9.2) |
| [[SNU-423 (line)]] | alt | 180 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 221 | 1 | 5 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 3.50× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.397× (z -8.6) |
| [[A498 (line)]] | wt | 170 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.384× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 19.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +18.9) | — |
| [[A549 (line)]] | wt | 34.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +19.2) | — |
| [[CFPAC-1 (line)]] | alt | 27.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +23.5) | — |
| [[HOP62 (line)]] | alt | 56.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +20.2) | — |
| [[NCI-H2030 (line)]] | alt | 149 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 56.1 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +19.4) | [[Auranofin (drug)]] 5 µM 0.162× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 128 | 1 | 3 | [[Harringtonine (drug)]] 5 µM 5.28× (z +12.6) | [[Auranofin (drug)]] 5 µM 0.167× (z -14.1) |
| [[A-172 (line)]] | wt | 44.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +15.9) | — |
| [[A-427 (line)]] | wt | 85.1 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.231× (z -11.0) |
| [[CHP-212 (line)]] | wt | 171 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0541× (z -12.1) |
| [[HS-578T (line)]] | alt | 118 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +15.8) | — |
| [[Hs 766T (line)]] | wt | 66.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -9.3) |
| [[NCI-H661 (line)]] | alt | 233 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.159× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 66.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 39.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.249× (z -8.9) |
| [[C32 (line)]] | wt | 138 | 1 | 0 | [[Binimetinib (drug)]] 0.5 µM 3.24× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 46.2 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.253× (z -8.7) |
| [[AN3 CA (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.76 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.21 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.05 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.05 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.99 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.63 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 17.5 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.45 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX41]] | +0.73 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[RBMS3]] | +0.71 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[CACNA2D1]] | +0.68 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[FLRT2]] | +0.65 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[FAP]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ZEB2]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[TRPS1]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ATF7IP]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[LINC00882]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[EBF1]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ARID5B]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[HECW2]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKCZ]] | -0.59 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[CAPN10]] | -0.59 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[CTNNBIP1]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[DNAJC5]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 | same gene group |
| [[TPD52L2]] | -0.56 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[EIF4E3]] | -0.54 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[ZCCHC17]] | -0.54 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[YKT6]] | -0.53 | -0.47 / -0.39 | both halves | 6e-05 | pathway: CDC42 GTPase cycle |
| [[HMOX2]] | -0.53 | -0.48 / -0.34 | both halves | 1e-04 | pathway: RHOA GTPase cycle |
| [[RNF216P1]] | -0.53 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[C11orf80]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[LIMK1]] | -0.52 | -0.45 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPS1]] | B | TRPS1 activity raises ARHGAP24's level | lines that do not express TRPS1 (14) vs lines expressing it (36) | 4.53× lower at baseline in the lines without TRPS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, FBXO32, PRDM1 |
| [[MEF2C]] | B | MEF2C activity raises ARHGAP24's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 3.28× lower at baseline in the lines without MEF2C | 0.018 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[ANGPT1]] | B | ANGPT1 activity raises ARHGAP24's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 4.22× lower at baseline in the lines without ANGPT1 | 0.026 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[SOX5]] | B | SOX5 activity raises ARHGAP24's level | lines that do not express SOX5 (24) vs lines expressing it (26) | 4.04× lower at baseline in the lines without SOX5 | 0.038 | ⚠ within organs, on part of the lines; also absent: CTHRC1, MOXD1, AK5 |
| [[PLXDC2]] | B | PLXDC2 activity raises ARHGAP24's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 2.41× lower at baseline in the lines without PLXDC2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[LINC01687]] | B | LINC01687 activity raises ARHGAP24's level | lines that do not express LINC01687 (31) vs lines expressing it (19) | 3.80× lower at baseline in the lines without LINC01687 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC02616, TPTE |
| [[MAP2K1]] | B | MAP2K1 activity lowers ARHGAP24's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TEX41]] | B | TEX41 activity raises ARHGAP24's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 3.75× lower at baseline in the lines without TEX41 | 0.084 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[RHOBTB3]] | B | RHOBTB3 activity raises ARHGAP24's level | lines that do not express RHOBTB3 (10) vs lines expressing it (40) | 3.14× lower at baseline in the lines without RHOBTB3 | 0.095 | ⚠ within organs, on part of the lines; also absent: FYN, POGLUT3; maybe low, not absent |
| [[GPR176]] | C | GPR176 activity raises ARHGAP24's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 5.98× lower at baseline in the lines without GPR176 | 0.021 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1; co-absent with the target |
| [[DOCK10]] | C | DOCK10 activity raises ARHGAP24's level | lines that do not express DOCK10 (24) vs lines expressing it (26) | 5.58× lower at baseline in the lines without DOCK10 | 0.082 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPS1]] | B | ARHGAP24 activity raises TRPS1's level | lines that do not express ARHGAP24 (17) vs lines expressing it (33) | 3.59× lower at baseline in the lines without ARHGAP24 | 0.023 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, GPR176 |
| cells under [[Futibatinib (drug)]] 0.05 µM | B | ARHGAP24 activity lowers the cells' numbers under Futibatinib 0.05 µM (makes them more sensitive) | lines that do not express ARHGAP24 (17) vs lines expressing it (31) | the lines without ARHGAP24: 1.19× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, GPR176 |
| cells under [[c-Kit-IN-1 (drug)]] 5 µM | B | ARHGAP24 activity lowers the cells' numbers under c-Kit-IN-1 5 µM (makes them more sensitive) | lines that do not express ARHGAP24 (17) vs lines expressing it (31) | the lines without ARHGAP24: 1.45× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, GPR176 |
| cells under [[TAK-733 (drug)]] 5 µM | B | ARHGAP24 activity lowers the cells' numbers under TAK-733 5 µM (makes them more sensitive) | lines that do not express ARHGAP24 (17) vs lines expressing it (31) | the lines without ARHGAP24: 1.31× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, GPR176 |
| [[PRICKLE2]] | C | ARHGAP24 activity raises PRICKLE2's level | lines that do not express ARHGAP24 (17) vs lines expressing it (33) | 4.30× lower at baseline in the lines without ARHGAP24 | 0.032 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, GPR176; co-absent with the target |
| [[GPR176]] | C | ARHGAP24 activity raises GPR176's level | lines that do not express ARHGAP24 (17) vs lines expressing it (33) | 4.90× lower at baseline in the lines without ARHGAP24 | 0.073 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, GPR176; co-absent with the target |
| [[COL12A1]] | C | ARHGAP24 activity raises COL12A1's level | lines that do not express ARHGAP24 (17) vs lines expressing it (33) | 5.87× lower at baseline in the lines without ARHGAP24 | 0.0999 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, GPR176; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.2, 24.6); signed map (43.0, 25.6). **Vector** length 134, 42.3% of its response variance represented; |z| ≥ 3 in 1,193 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +10.6 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +12.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.8 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.0 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +3.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | -13.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -10.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.7 | -11.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.6 | -0.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.6 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -8.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.0 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.23-q21.3 — chr4:85,475,150-86,002,668 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564B1162, FLJ33877, FilGAP |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Rho GTPase activating proteins; MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: RHOA GTPase cycle; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N264](https://www.uniprot.org/uniprotkb/Q8N264) (Rho GTPase-activating protein 24):

> Rho GTPase-activating protein involved in cell polarity, cell morphology and cytoskeletal organization. Acts as a GTPase activator for the Rac-type GTPase by converting it to an inactive GDP-bound state. Controls actin remodeling by inactivating Rac downstream of Rho leading to suppress leading edge protrusion and promotes cell retraction to achieve cellular polarity. Able to suppress RAC1 and CDC42 activity in vitro. Overexpression induces cell rounding with partial or complete disruption of …

**Summary**, from NCBI Gene [83478](https://www.ncbi.nlm.nih.gov/gene/83478):

> This gene encodes a Rho-GTPase activating protein, which is specific for the small GTPase family member Rac. Binding of the encoded protein by filamin A targets it to sites of membrane protrusion, where it antognizes Rac. This results in suppression of lamellae formation and promotion of retraction to regulate cell polarity. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:25361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25361) · Entrez [83478](https://www.ncbi.nlm.nih.gov/gene/83478) · UniProt [Q8N264](https://www.uniprot.org/uniprotkb/Q8N264) · Ensembl [ENSG00000138639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138639)

## Data

Gene col 6199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6199); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6199]; `tensor/DDL_lfc|DDL_z.npy` [6199]; `embed/gene_vectors.npy` [6199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6199 or target_col == 6199). Every well: [[ARHGAP24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
