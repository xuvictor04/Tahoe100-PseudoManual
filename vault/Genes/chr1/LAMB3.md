---
symbol: "LAMB3"
type: "gene"
col: 12299
ensembl_id: "ENSG00000196878"
name: "laminin subunit beta 3"
location: "1q32.2"
module: 101
arm: "+"
pooled_cpm: 374.69
n_lines_expressing: 28
n_dd_up: 16
n_dd_down: 25
n_dd_up_clean: 11
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 31
direction_downstream: 37
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# LAMB3

*laminin subunit beta 3* — 1q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +12.0, q 1e-30, up in 15 of 26 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.35× (z +12.0, q 2e-30, up in 17 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.353× (z -14.6, q 3e-45, down in 26 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMC2]] (+0.68, fdr 7e-06), [[IL2RG]] (+0.61, fdr 1e-05), [[GJB3]] (+0.60, fdr 1e-05); moves opposite to [[WHAMMP1]] (-0.53, fdr 3e-05), [[CIAO2A]] (-0.52, fdr 4e-05), [[PRDX3]] (-0.51, fdr 2e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 31 arrows point to it, the strongest [[WNT7B]] → it (grade B ⚠); 37 go from it, the strongest it → [[PLAUR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12299.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.89×** | +12.0 | 1e-30 | 15/26 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.35×** | +12.0 | 2e-30 | 17/26 (Panc 03.27, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.09×** | +9.9 | 7e-21 | 21/26 (HOP62, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +9.1 | 1e-17 | 23/26 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +6.6 | 5e-09 | 11/26 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +6.0 | 2e-07 | 21/26 (A498, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +5.1 | 3e-05 | 13/27 (A498, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 0.002 | 17/26 (NCI-H1792, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.003 | 18/26 (Panc 03.27, RKO, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.004 | 13/26 (LOX-IMVI, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.29×** | +3.5 | 0.021 | 9/26 (AsPC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.033 | 9/26 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +3.4 | 0.033 | 15/27 (NCI-H1573, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.045 | 14/26 (HEC-1-A, A498, …) | two highest doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.064 | 10/25 (HCT15, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12299.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.353×** | -14.6 | 3e-45 | 26/26 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.403×** | -12.7 | 2e-34 | 25/26 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.506×** | -9.5 | 3e-19 | 24/26 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.636×** | -5.9 | 7e-07 | 20/26 (RKO, AsPC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.743×** | -5.7 | 2e-06 | 19/26 (RKO, SW48, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.674×** | -5.5 | 3e-06 | 21/26 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.712×** | -4.8 | 2e-04 | 18/26 (RKO, SW 1088, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.704×** | -4.7 | 2e-04 | 21/27 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.716×** | -4.7 | 2e-04 | 15/26 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.783×** | -4.6 | 3e-04 | 13/26 (AsPC-1, RKO, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **0.713×** | -4.5 | 3e-04 | 19/25 (RKO, HT-29, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.715×** | -4.5 | 3e-04 | 14/25 (RKO, HOP62, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.482×** | -4.2 | 0.001 | 19/27 (AsPC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.742×** | -4.2 | 0.001 | 19/26 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.758×** | -3.7 | 0.007 | 18/26 (HT-29, LoVo, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.771×** | -3.7 | 0.009 | 19/27 (HOP62, A549, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **0.771×** | -3.7 | 0.009 | 13/26 (A498, NCI-H1792, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.819×** | -3.6 | 0.011 | 13/26 (RKO, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.800×** | -3.1 | 0.051 | 12/25 (RKO, AsPC-1, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12299. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 2,469 | 8 (6 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +17.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.210× (z -14.5) |
| [[RKO (line)]] | wt | 1,023 | 0 | 14 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.324× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 670 | 5 (3 ⚠) | 4 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.17× (z +16.0) | [[Panobinostat (drug)]] 5 µM 0.183× (z -16.5) |
| [[A498 (line)]] | wt | 166 | 7 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.47× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.355× (z -9.5) |
| [[HOP62 (line)]] | alt | 701 | 3 (2 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +14.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.234× (z -13.8) |
| [[KATO III (line)]] | alt | 338 | 4 | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.75× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.192× (z -17.6) |
| [[Panc 03.27 (line)]] | alt | 1,833 | 5 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.53× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.334× (z -14.2) |
| [[HT-29 (line)]] | alt | 371 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -18.7) |
| [[LoVo (line)]] | wt | 551 | 1 (1 ⚠) | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.49× (z +9.5) ⚠ cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 5 µM 0.158× (z -20.0) |
| [[SW 900 (line)]] | alt | 150 | 4 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +13.3) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.49× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.316× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 1,723 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -17.2) |
| [[HEC-1-A (line)]] | alt | 866 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -20.5) |
| [[LS 180 (line)]] | wt | 275 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -17.3) |
| [[SW48 (line)]] | wt | 1,186 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -13.8) |
| [[A549 (line)]] | wt | 199 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -17.6) |
| [[HS-578T (line)]] | alt | 157 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +16.2) ⚠ cell-cycle shift, explains ~50% of this change | [[Panobinostat (drug)]] 5 µM 0.332× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 1,312 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -11.0) |
| [[SW1417 (line)]] | alt | 237 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.1) ⚠ cell-cycle shift, explains ~50% of this change | [[Panobinostat (drug)]] 5 µM 0.388× (z -12.2) |
| [[SW480 (line)]] | alt | 169 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -12.1) |
| [[Hs 766T (line)]] | wt | 154 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.3) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.21× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 95.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +13.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.73× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 178 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.59× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 144 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -9.9) |
| [[A-172 (line)]] | wt | 49.7 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 20.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 53.5 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 38.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 28.4 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 37.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 40.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 44.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.9 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 181 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.7 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 78.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1,161 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.9 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 60.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 24.6 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 55.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 32.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 56.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12299), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMC2]] | +0.68 | +0.69 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_APICAL_JUNCTION; STRING 999 |
| [[IL2RG]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[GJB3]] | +0.60 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[TRPV3]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[EHD1]] | +0.59 | +0.63 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ARHGAP27]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[S100A2]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 | STRING 507 |
| [[PHLDA2]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[EPHA2]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[CYP3A5]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[MAST4]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[IL23A]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WHAMMP1]] | -0.53 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[CIAO2A]] | -0.52 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[PRDX3]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[DCUN1D4]] | -0.51 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[CIPC]] | -0.50 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[CMPK1]] | -0.49 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[NDC1]] | -0.48 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 12, C 19. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT7B]] | B | WNT7B activity raises LAMB3's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 3.52× lower at baseline in the lines without WNT7B | 0.007 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[PLAU]] | B | PLAU activity raises LAMB3's level | lines that do not express PLAU (26) vs lines expressing it (24) | 2.53× lower at baseline in the lines without PLAU | 0.014 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[SDCBP2]] | B | SDCBP2 activity raises LAMB3's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 4.23× lower at baseline in the lines without SDCBP2 | 0.018 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[PLAUR]] | B | PLAUR activity raises LAMB3's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 6.00× lower at baseline in the lines without PLAUR | 0.019 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[S100A2]] | B | S100A2 activity raises LAMB3's level | lines that do not express S100A2 (25) vs lines expressing it (25) | 3.07× lower at baseline in the lines without S100A2 | 0.019 | ⚠ within organs, on part of the lines; also absent: KRT81, LINC00408, FGFBP1; maybe low, not absent |
| [[PHLDA2]] | B | PHLDA2 activity raises LAMB3's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 5.52× lower at baseline in the lines without PHLDA2 | 0.037 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[PLEK2]] | B | PLEK2 activity raises LAMB3's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 3.34× lower at baseline in the lines without PLEK2 | 0.048 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[TMCC3]] | B | TMCC3 activity raises LAMB3's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.77× lower at baseline in the lines without TMCC3 | 0.051 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[PRDM1]] | B | PRDM1 activity raises LAMB3's level | lines that do not express PRDM1 (15) vs lines expressing it (35) | 2.78× lower at baseline in the lines without PRDM1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PCED1B, AMIGO2, NRP1 |
| [[KLF5]] | B | KLF5 activity raises LAMB3's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 3.25× lower at baseline in the lines without KLF5 | 0.060 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[SEMA3B]] | B | SEMA3B activity raises LAMB3's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.99× lower at baseline in the lines without SEMA3B | 0.062 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[SERPINB1]] | B | SERPINB1 activity raises LAMB3's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 4.18× lower at baseline in the lines without SERPINB1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 23, C 14. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAUR]] | B | LAMB3 activity raises PLAUR's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 3.21× lower at baseline in the lines without LAMB3 | 0.003 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[WNT7B]] | B | LAMB3 activity raises WNT7B's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 3.23× lower at baseline in the lines without LAMB3 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[KLF5]] | B | LAMB3 activity raises KLF5's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 4.51× lower at baseline in the lines without LAMB3 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[CIPC]] | B | LAMB3 activity lowers CIPC's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 1.31× higher at baseline in the lines without LAMB3 | 0.013 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[SEMA7A]] | B | LAMB3 activity raises SEMA7A's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 1.98× lower at baseline in the lines without LAMB3 | 0.017 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[EHD1]] | B | LAMB3 activity raises EHD1's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 1.66× lower at baseline in the lines without LAMB3 | 0.023 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[TMCC3]] | B | LAMB3 activity raises TMCC3's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 2.39× lower at baseline in the lines without LAMB3 | 0.031 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[BMAL2-AS1]] | B | LAMB3 activity raises BMAL2-AS1's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 1.23× lower at baseline in the lines without LAMB3 | 0.031 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[RAP1B]] | B | LAMB3 activity raises RAP1B's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 1.27× lower at baseline in the lines without LAMB3 | 0.031 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[SDC4]] | B | LAMB3 activity raises SDC4's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 2.10× lower at baseline in the lines without LAMB3 | 0.036 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[PRDM1]] | B | LAMB3 activity raises PRDM1's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 2.86× lower at baseline in the lines without LAMB3 | 0.048 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[PLEK2]] | B | LAMB3 activity raises PLEK2's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 4.00× lower at baseline in the lines without LAMB3 | 0.050 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.9, 52.7); signed map (2.7, 34.6). **Vector** length 115, 38.8% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +6.9 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +6.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +1.7 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -5.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.1 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.4 | -2.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.2 | -4.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | laminin subunit beta 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.2 — chr1:209,614,870-209,652,425 (-) |
| Ensembl biotype | protein_coding |
| Also known as | nicein-125kDa, kalinin-140kDa, BM600-125kDa; previously LAMNB1 |
| Gene groups (HGNC) | Laminin subunits; MicroRNA protein coding host genes |
| Hallmark sets | APICAL_JUNCTION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 24 pathways, smallest: Type I hemidesmosome assembly; Anchoring fibril formation; Attachment of bacteria to epithelial cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13751](https://www.uniprot.org/uniprotkb/Q13751) (Laminin subunit beta-3):

> Binding to cells via a high affinity receptor, laminin is thought to mediate the attachment, migration and organization of cells into tissues during embryonic development by interacting with other extracellular matrix components.

**Summary**, from NCBI Gene [3914](https://www.ncbi.nlm.nih.gov/gene/3914):

> The product encoded by this gene is a laminin that belongs to a family of basement membrane proteins. This protein is a beta subunit laminin, which together with an alpha and a gamma subunit, forms laminin-5. Mutations in this gene cause epidermolysis bullosa junctional Herlitz type, and generalized atrophic benign epidermolysis bullosa, diseases that are characterized by blistering of the skin. Multiple alternatively spliced transcript variants that encode the same protein have been found for …

**Accessions** — [HGNC:6490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6490) · Entrez [3914](https://www.ncbi.nlm.nih.gov/gene/3914) · UniProt [Q13751](https://www.uniprot.org/uniprotkb/Q13751) · Ensembl [ENSG00000196878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196878)

## Data

Gene col 12299: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12299); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12299, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12299]; `tensor/DDL_lfc|DDL_z.npy` [12299]; `embed/gene_vectors.npy` [12299]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12299 or target_col == 12299). Every well: [[LAMB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
