---
symbol: "AKAP12"
type: "gene"
col: 5157
ensembl_id: "ENSG00000131016"
name: "A-kinase anchoring protein 12"
location: "6q25.1"
module: 147
arm: "+"
pooled_cpm: 1025.54
n_lines_expressing: 32
n_dd_up: 35
n_dd_down: 47
n_dd_up_clean: 32
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 9
direction_downstream: 10
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# AKAP12

*A-kinase anchoring protein 12* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (3 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.54× (z +6.8, q 5e-09, up in 23 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.396× (z -14.5, q 8e-45, down in 29 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERRFI1]] (+0.70, fdr 7e-06), [[HMGA2]] (+0.67, fdr 7e-06), [[FOXL1]] (+0.66, fdr 7e-06); moves opposite to [[CD5L]] (-0.53, fdr 1e-05), [[EPB41]] (-0.51, fdr 1e-05), [[TMPRSS3]] (-0.49, fdr 2e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PDGFRA]] → it (grade B ⚠); 10 go from it, the strongest it → [[HMGA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5157.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.54×** | +6.8 | 5e-09 | 23/31 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +6.4 | 6e-08 | 24/30 (RPMI-7951, NCI-H1792, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.71×** | +5.9 | 6e-07 | 21/30 (RPMI-7951, NCI-H1792, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.09×** | +5.8 | 8e-07 | 26/30 (SW480, Panc 03.27, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.68×** | +5.8 | 8e-07 | 22/30 (RPMI-7951, SNU-423, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **1.68×** | +5.8 | 8e-07 | 22/30 (RPMI-7951, NCI-H1792, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.67×** | +5.2 | 1e-05 | 20/29 (RPMI-7951, NCI-H1792, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.60×** | +5.2 | 1e-05 | 19/29 (Panc 03.27, SW480, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.59×** | +5.1 | 2e-05 | 21/30 (RPMI-7951, NCI-H1792, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.58×** | +5.1 | 2e-05 | 20/30 (RPMI-7951, NCI-H1792, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.38×** | +5.0 | 3e-05 | 19/30 (RPMI-7951, SK-MEL-2, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.57×** | +5.0 | 3e-05 | 20/30 (RPMI-7951, SNU-423, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.56×** | +5.0 | 3e-05 | 22/30 (RPMI-7951, NCI-H1792, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.59×** | +4.9 | 3e-05 | 20/29 (HepG2/C3A, SW480, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.56×** | +4.9 | 3e-05 | 19/30 (RPMI-7951, NCI-H1792, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **2.26×** | +4.7 | 9e-05 | 25/28 (SW480, SNU-423, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5157.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.396×** | -14.5 | 8e-45 | 29/31 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.330×** | -12.2 | 5e-32 | 28/30 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.337×** | -12.0 | 6e-31 | 28/30 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.375×** | -10.8 | 3e-25 | 25/30 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.415×** | -9.3 | 1e-18 | 25/29 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.518×** | -7.3 | 4e-11 | 27/30 (H4, NCI-H23, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.526×** | -7.1 | 1e-10 | 26/30 (CFPAC-1, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.553×** | -6.9 | 3e-10 | 24/32 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.548×** | -6.4 | 1e-08 | 21/29 (HepG2/C3A, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.561×** | -6.1 | 5e-08 | 25/30 (NCI-H23, A549, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.591×** | -5.8 | 4e-07 | 24/30 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -5.5 | 2e-06 | 19/30 (LOX-IMVI, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.587×** | -5.4 | 2e-06 | 23/30 (HepG2/C3A, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.633×** | -5.4 | 3e-06 | 22/31 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.613×** | -5.4 | 3e-06 | 19/30 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.403×** | -5.2 | 8e-06 | 27/31 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.634×** | -4.8 | 4e-05 | 20/30 (HepG2/C3A, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.702×** | -4.8 | 5e-05 | 21/30 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5157. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 709 | 9 (3 ⚠) | 16 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.73× (z +14.2) | [[Binimetinib (drug)]] 0.5 µM 0.213× (z -14.6) |
| [[HepG2_C3A (line)]] | wt | 2,296 | 5 (1 ⚠) | 18 (1 ⚠) | [[Daptomycin (drug)]] 5 µM 4.17× (z +11.8) ⚠ unreliable plate only · without an alert: [[Mebendazole (drug)]] 5 µM 3.73× (z +10.4) | [[Cobimetinib (drug)]] 5 µM 0.111× (z -17.5) |
| [[NCI-H1792 (line)]] | alt | 2,090 | 7 | 12 (4 ⚠) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 2.95× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -24.2) |
| [[NCI-H23 (line)]] | alt | 4,761 | 0 | 19 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -16.4) |
| [[LOX-IMVI (line)]] | wt | 2,308 | 0 | 18 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -18.8) |
| [[RPMI-7951 (line)]] | alt | 480 | 17 | 1 | [[Clobetasol propionate (drug)]] 0.05 µM 5.67× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.3) |
| [[H4 (line)]] | wt | 782 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -16.8) |
| [[A-172 (line)]] | wt | 3,193 | 0 | 15 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0941× (z -21.3) |
| [[HOP62 (line)]] | alt | 649 | 2 | 13 (2 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.23× (z +9.1) | [[Belinostat (drug)]] 5 µM 0.166× (z -14.5) |
| [[SK-MEL-2 (line)]] | alt | 1,177 | 4 | 9 (2 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.69× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -13.1) |
| [[A549 (line)]] | wt | 3,544 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -26.6) |
| [[C32 (line)]] | wt | 955 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 1,034 | 1 | 11 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -13.8) |
| [[hTERT-HPNE (line)]] | wt | 2,414 | 0 | 12 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 388 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +17.7) | — |
| [[AsPC-1 (line)]] | alt | 2,372 | 5 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.99× (z +14.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.83× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -15.4) |
| [[J82 (line)]] | alt | 1,117 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.263× (z -12.6) |
| [[PANC-1 (line)]] | alt | 3,900 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -28.0) |
| [[SW 900 (line)]] | alt | 657 | 5 (2 ⚠) | 3 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.52× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -9.8) |
| [[CHP-212 (line)]] | wt | 2,186 | 1 | 6 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.44× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -15.0) |
| [[RKO (line)]] | wt | 445 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -12.4) |
| [[SNU-423 (line)]] | alt | 1,432 | 2 | 5 | [[Dexamethasone (drug)]] 0.5 µM 2.98× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.240× (z -11.5) |
| [[SW1417 (line)]] | alt | 275 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +19.0) | — |
| [[A-427 (line)]] | wt | 484 | 1 (1 ⚠) | 2 | [[Harringtonine (drug)]] 0.5 µM 2.19× (z +8.5) ⚠ cell-cycle shift, explains ~17% of this change | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 1,442 | 1 (1 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 3.80× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -11.1) |
| [[SW 1088 (line)]] | alt | 713 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.112× (z -9.2) |
| [[A498 (line)]] | wt | 130 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 155 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 83.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 195 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 83.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 162 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 249 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 89.4 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 181 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 105 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 75.8 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 85.1 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 99.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 109 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 667 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 84.8 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 215 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 810 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 358 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 108 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 87.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 537 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 278 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5157), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERRFI1]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[HMGA2]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[FOXL1]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[SERPINE1]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[ABLIM3]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CLMP]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[SH3RF3]] | +0.63 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[PHC2]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ELK3]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[PALM2AKAP2]] | +0.60 | +0.49 / +0.67 | both halves | 1e-05 | STRING 521 |
| [[ANGPTL4]] | +0.59 | +0.60 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[MAP4K4]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD5L]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[EPB41]] | -0.51 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[TMPRSS3]] | -0.49 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[PLBD1]] | -0.48 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[GSEC]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[TRIM2]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ZSCAN31]] | -0.47 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[P4HTM]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFRA]] | B | PDGFRA activity raises AKAP12's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 2.75× lower at baseline in the lines without PDGFRA | 0.056 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1 |
| [[PALM2AKAP2]] | B | PALM2AKAP2 activity raises AKAP12's level | lines that do not express PALM2AKAP2 (9) vs lines expressing it (41) | 5.05× lower at baseline in the lines without PALM2AKAP2 | 0.057 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MPP1, LIX1L |
| [[TUBB6]] | B | TUBB6 activity raises AKAP12's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 5.18× lower at baseline in the lines without TUBB6 | 0.060 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |
| [[NR3C1]] | B | NR3C1 activity raises AKAP12's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds |
| [[MEIS3]] | B | MEIS3 activity raises AKAP12's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 3.80× lower at baseline in the lines without MEIS3 | 0.077 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[ANGPTL4]] | B | ANGPTL4 activity raises AKAP12's level | lines that do not express ANGPTL4 (13) vs lines expressing it (37) | 3.64× lower at baseline in the lines without ANGPTL4 | 0.085 | ⚠ within organs, on part of the lines; also absent: CLDN14-AS1, LGALS1, EBI3 |
| [[ITGA5]] | B | ITGA5 activity raises AKAP12's level | lines that do not express ITGA5 (11) vs lines expressing it (39) | 2.24× lower at baseline in the lines without ITGA5 | 0.093 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1 |
| [[GAB3]] | C | GAB3 activity raises AKAP12's level | lines that do not express GAB3 (17) vs lines expressing it (33) | 4.13× lower at baseline in the lines without GAB3 | 0.070 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, SOGA3; co-absent with the target |
| [[SLC26A2]] | C | SLC26A2 activity raises AKAP12's level | lines that do not express SLC26A2 (4) vs lines expressing it (46) | 6.02× lower at baseline in the lines without SLC26A2 | 0.092 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR4435-2HG, EPB41L2, CEP85L; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGA2]] | B | AKAP12 activity raises HMGA2's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 3.22× lower at baseline in the lines without AKAP12 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B |
| [[IGF2BP2]] | B | AKAP12 activity raises IGF2BP2's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 1.80× lower at baseline in the lines without AKAP12 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B |
| [[ETS1]] | B | AKAP12 activity raises ETS1's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 3.02× lower at baseline in the lines without AKAP12 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B |
| [[SIPA1L1]] | B | AKAP12 activity raises SIPA1L1's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 1.72× lower at baseline in the lines without AKAP12 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B |
| [[MAP7D3]] | B | AKAP12 activity raises MAP7D3's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 2.18× lower at baseline in the lines without AKAP12 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B |
| [[HMGA2-AS1]] | B | AKAP12 activity raises HMGA2-AS1's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without AKAP12 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B |
| [[ELK3]] | B | AKAP12 activity raises ELK3's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 2.29× lower at baseline in the lines without AKAP12 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B |
| [[LINC02454]] | C | AKAP12 activity raises LINC02454's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 2.14× lower at baseline in the lines without AKAP12 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B; co-absent with the target |
| [[ARHGAP22]] | C | AKAP12 activity raises ARHGAP22's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 3.46× lower at baseline in the lines without AKAP12 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B; co-absent with the target |
| [[RPSAP52]] | C | AKAP12 activity raises RPSAP52's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 2.38× lower at baseline in the lines without AKAP12 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B; co-absent with the target |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.6, 12.3); signed map (11.5, 46.3). **Vector** length 133, 43.1% of its response variance represented; |z| ≥ 3 in 1,941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.8 | +1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | -4.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +5.2 | +5.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +5.1 | +5.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.0 | +5.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.9 | +5.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.7 | +4.9 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.9 | -7.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.8 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.5 | -4.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.3 | -6.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.1 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.0 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | A-kinase anchoring protein 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:151,239,967-151,358,559 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AKAP250, SSeCKS |
| Gene groups (HGNC) | A-kinase anchoring proteins |
| Hallmark sets | ANDROGEN_RESPONSE, KRAS_SIGNALING_UP, HYPOXIA |
| Reactome | 5 pathways, smallest: RHOF GTPase cycle; RHOD GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02952](https://www.uniprot.org/uniprotkb/Q02952) (A-kinase anchor protein 12):

> Anchoring protein that mediates the subcellular compartmentation of protein kinase A (PKA) and protein kinase C (PKC).

**Summary**, from NCBI Gene [9590](https://www.ncbi.nlm.nih.gov/gene/9590):

> The A-kinase anchor proteins (AKAPs) are a group of structurally diverse proteins, which have the common function of binding to the regulatory subunit of protein kinase A (PKA) and confining the holoenzyme to discrete locations within the cell. This gene encodes a member of the AKAP family. The encoded protein is expressed in endothelial cells, cultured fibroblasts, and osteosarcoma cells. It associates with protein kinases A and C and phosphatase, and serves as a scaffold protein in signal …

**Accessions** — [HGNC:370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:370) · Entrez [9590](https://www.ncbi.nlm.nih.gov/gene/9590) · UniProt [Q02952](https://www.uniprot.org/uniprotkb/Q02952) · Ensembl [ENSG00000131016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131016)

## Data

Gene col 5157: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5157); `tables/drug_effects.parquet` (83 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5157, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5157]; `tensor/DDL_lfc|DDL_z.npy` [5157]; `embed/gene_vectors.npy` [5157]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5157 or target_col == 5157). Every well: [[AKAP12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKAP12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
