---
symbol: "TOB1"
type: "gene"
col: 6495
ensembl_id: "ENSG00000141232"
name: "transducer of ERBB2, 1"
location: "17q21.33"
module: 59
arm: "+"
pooled_cpm: 62.45
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 19
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# TOB1

*transducer of ERBB2, 1* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.72× (z +12.2, q 3e-31, up in 34 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.52× (z +9.4, q 8e-19, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.893× (z -6.1, q 5e-07, down in 6 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.500× (z -5.7, q 3e-06, down in 28 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYLIP]] (+0.59, fdr 1e-05), [[ATP1B1]] (+0.58, fdr 1e-05), [[KLF4]] (+0.57, fdr 1e-05); moves opposite to [[TIMM23B]] (-0.58, fdr 1e-05), [[PGS1]] (-0.53, fdr 1e-05), [[TIMM23B-AGAP6]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[POF1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6495.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.72×** | +12.2 | 3e-31 | 34/47 (C32, HOP62, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +10.4 | 8e-23 | 40/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +9.4 | 8e-19 | 38/48 (A-427, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +7.8 | 7e-13 | 31/48 (NCI-H1792, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +7.2 | 9e-11 | 37/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.43×** | +5.6 | 2e-06 | 28/46 (HOP62, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 3e-04 | 23/48 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.002 | 19/48 (J82, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.002 | 23/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Capmatinib (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.007 | 18/48 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.27×** | +3.8 | 0.008 | 23/48 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +3.5 | 0.018 | 20/48 (NCI-H460, SNU-423, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.25×** | +3.5 | 0.020 | 21/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.026 | 19/48 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.3 | 0.031 | 15/48 (SW480, SNU-1, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.032 | 15/48 (SW480, SW1417, …) | inconsistent across doses | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.032 | 19/47 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.15× | +3.1 | 0.061 | 12/49 (LOX-IMVI, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6495.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -6.1 | 5e-07 | 6/49 (LOX-IMVI, RKO, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.500×** | -5.7 | 3e-06 | 28/49 (NCI-H460, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.736×** | -4.8 | 2e-04 | 27/46 (COLO 205, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -4.7 | 3e-04 | 25/47 (COLO 205, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.812×** | -4.6 | 4e-04 | 25/49 (HT-29, COLO 205, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.741×** | -4.6 | 5e-04 | 25/40 (A-427, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.771×** | -3.8 | 0.012 | 23/42 (A-172, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.673×** | -3.3 | 0.067 | 16/48 (SW480, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.674×** | -3.3 | 0.067 | 15/47 (BT-474, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.814×** | -3.2 | 0.067 | 23/47 (SW 1271, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.819×** | -3.2 | 0.077 | 16/47 (SNU-1, NCI-H1573, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.683×** | -3.1 | 0.077 | 15/46 (HepG2/C3A, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.822×** | -3.1 | 0.087 | 19/48 (SNU-1, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6495. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 144 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0926× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.309× (z -9.0) |
| [[COLO 205 (line)]] | alt | 157 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 117 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 102 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +16.7) ⚠ cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 34.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +12.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Selinexor (drug)]] 5 µM 2.77× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 98.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -15.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 61.4 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.19× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.125× (z -18.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 90.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 25.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.90× (z +17.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[CHP-212 (line)]] | wt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0464× (z -15.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 38.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HOP62 (line)]] | alt | 27.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +16.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HT-29 (line)]] | alt | 110 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 26.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +13.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 37.9 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.69× (z +13.4) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 33.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +13.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.43× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 45.4 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.75× (z +9.1) ⚠ toxic | — |
| [[SK-MEL-2 (line)]] | alt | 41.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +16.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.40× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 129 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.50× (z +10.4) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 45.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -11.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 110 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +13.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HepG2_C3A (line)]] | wt | 75.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.07× (z +9.9) ⚠ toxic | — |
| [[Hs 766T (line)]] | wt | 66.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 22.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +9.0) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 40.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +12.6) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[KATO III (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 69.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 28.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.51× (z +9.6) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 78.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 32.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +15.9) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[RKO (line)]] | wt | 31.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.25× (z +9.7) ⚠ toxic | — |
| [[SNU-423 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.4) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW 900 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 54.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -10.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6495), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLIP]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ATP1B1]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[KLF4]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[ZFP36L2]] | +0.54 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[FZD5]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[BCL2L11]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CLDN3]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[CXXC5]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[GPRC5C]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TRAF4]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[NEDD9]] | +0.52 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[ZNF703]] | +0.52 | +0.52 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B]] | -0.58 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[PGS1]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | -0.53 | -0.50 / -0.49 | both halves | 2e-05 |  |
| [[TIMM23]] | -0.48 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[MAPKAP1]] | -0.48 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[PARGP1]] | -0.46 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[UIMC1]] | -0.46 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[FUBP3]] | -0.45 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[NSUN2]] | -0.45 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[GHRLOS]] | -0.45 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[ARIH2]] | -0.45 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[THOC5]] | -0.45 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POF1B]] | B | POF1B activity raises TOB1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 2.06× lower at baseline in the lines without POF1B | 0.002 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[PRR15]] | B | PRR15 activity raises TOB1's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.03× lower at baseline in the lines without PRR15 | 0.003 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[GCNT3]] | B | GCNT3 activity raises TOB1's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 1.98× lower at baseline in the lines without GCNT3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises TOB1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 1.98× lower at baseline in the lines without TMPRSS2 | 0.013 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[TC2N]] | B | TC2N activity raises TOB1's level | lines that do not express TC2N (28) vs lines expressing it (22) | 1.78× lower at baseline in the lines without TC2N | 0.015 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[TJP3]] | B | TJP3 activity raises TOB1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.75× lower at baseline in the lines without TJP3 | 0.019 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[TRIM31]] | B | TRIM31 activity raises TOB1's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 1.98× lower at baseline in the lines without TRIM31 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[JUP]] | B | JUP activity raises TOB1's level | lines that do not express JUP (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without JUP | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[BMP4]] | B | BMP4 activity raises TOB1's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 1.81× lower at baseline in the lines without BMP4 | 0.037 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[MUC13]] | B | MUC13 activity raises TOB1's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 1.92× lower at baseline in the lines without MUC13 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[CYP3A5]] | B | CYP3A5 activity raises TOB1's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 1.88× lower at baseline in the lines without CYP3A5 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[PLEKHG6]] | B | PLEKHG6 activity raises TOB1's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 1.61× lower at baseline in the lines without PLEKHG6 | 0.054 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (24.7, 58.2); signed map (50.7, 5.7). **Vector** length 134, 39.3% of its response variance represented; |z| ≥ 3 in 1,187 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.5 | +10.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.0 | +9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +3.9 | +3.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.8 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.9 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +2.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.2 | -5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.1 | -4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.9 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.7 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | transducer of ERBB2, 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,862,223-50,867,978 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TOB, TROB, APRO5; previously TROB1 |
| Gene groups (HGNC) | BTG/Tob family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ADIPOGENESIS, ESTROGEN_RESPONSE_EARLY, P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [P50616](https://www.uniprot.org/uniprotkb/P50616) (Protein Tob1):

> Anti-proliferative protein; the function is mediated by association with deadenylase subunits of the CCR4-NOT complex. Mediates CPEB3-accelerated mRNA deadenylation by binding to CPEB3 and recruiting CNOT7 which leads to target mRNA deadenylation and decay.

**Summary**, from NCBI Gene [10140](https://www.ncbi.nlm.nih.gov/gene/10140):

> This gene encodes a member of the transducer of erbB-2 /B-cell translocation gene protein family. Members of this family are anti-proliferative factors that have the potential to regulate cell growth. The encoded protein may function as a tumor suppressor. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:11979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11979) · Entrez [10140](https://www.ncbi.nlm.nih.gov/gene/10140) · UniProt [P50616](https://www.uniprot.org/uniprotkb/P50616) · Ensembl [ENSG00000141232](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141232)

## Data

Gene col 6495: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6495); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6495, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6495]; `tensor/DDL_lfc|DDL_z.npy` [6495]; `embed/gene_vectors.npy` [6495]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6495 or target_col == 6495). Every well: [[TOB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
