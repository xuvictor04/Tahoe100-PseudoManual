---
symbol: "ZSCAN32"
type: "gene"
col: 6472
ensembl_id: "ENSG00000140987"
name: "zinc finger and SCAN domain containing 32"
location: "16p13.3"
module: 114
arm: "+"
pooled_cpm: 11.9
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# ZSCAN32

*zinc finger and SCAN domain containing 32* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.96× (z +12.0, q 3e-30, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.682× (z -6.5, q 5e-08, down in 18 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.732× (z -5.5, q 6e-06, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (HT-29 0.131×, SNU-423 0.106×, KATO III 0.210×, LOX-IMVI 0.195×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.0681×, SW480 0.250×, PANC-1 0.302×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HT-29 0.105×, KATO III 0.174×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 0.302×, PANC-1 0.319×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (AsPC-1 0.178×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF7]] (+0.71, fdr 7e-06), [[RPP14]] (+0.65, fdr 7e-06), [[CBLL1]] (+0.64, fdr 1e-05).
> It is in [[Module 114]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6472.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +12.0 | 3e-30 | 40/47 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +11.1 | 4e-26 | 38/47 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +8.3 | 2e-14 | 26/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +8.3 | 2e-14 | 28/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +7.8 | 5e-13 | 26/40 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +6.9 | 4e-10 | 23/46 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.22×** | +5.0 | 4e-05 | 17/46 (A498, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +5.0 | 4e-05 | 15/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.21×** | +4.9 | 6e-05 | 14/48 (NCI-H1573, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +4.9 | 7e-05 | 7/47 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.29×** | +4.5 | 3e-04 | 12/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 0.001 | 13/45 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 0.001 | 11/46 (A-172, AsPC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.2 | 0.001 | 0/48 | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 0.001 | 5/44 (SW480, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 0.001 | 8/47 (LOX-IMVI, RKO, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.027 | 10/46 (LoVo, SW48, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.046 | 2/48 (A-172, J82) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ciclopirox (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.062 | 3/47 (LS 180, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6472.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (HT-29 0.131×, SNU-423 0.106×, KATO III 0.210×, LOX-IMVI 0.195×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.0681×, SW480 0.250×, PANC-1 0.302×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HT-29 0.105×, KATO III 0.174×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 0.302×, PANC-1 0.319×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (AsPC-1 0.178×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.682×** | -6.5 | 5e-08 | 18/37 (MIA PaCa-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.701×** | -5.8 | 2e-06 | 14/28 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.732×** | -5.5 | 6e-06 | 23/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.787×** | -4.1 | 0.006 | 21/39 (Panc 03.27, LS 180, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.811×** | -3.7 | 0.020 | 12/47 (PANC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.805×** | -3.7 | 0.020 | 13/24 (HT-29, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Silodosin (drug)]] 5 µM |  | **0.812×** | -3.6 | 0.031 | 10/45 (SHP-77, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.823×** | -3.4 | 0.040 | 19/46 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.838× | -3.1 | 0.11 | 4/48 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6472. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -10.4) |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -12.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 18.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 11.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.6) | — |
| [[SW480 (line)]] | alt | 15.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -11.0) |
| [[A-427 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -10.3) ⚠ cell-cycle shift, explains ~14% of this change |
| [[AsPC-1 (line)]] | alt | 18.3 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.178× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0681× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 9.51 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6472), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF7]] | +0.71 | +0.71 / +0.62 | both halves | 7e-06 | same gene group |
| [[RPP14]] | +0.65 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CBLL1]] | +0.64 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[ZNF557]] | +0.64 | +0.68 / +0.60 | both halves | 7e-06 | same gene group |
| [[ZNF197]] | +0.63 | +0.70 / +0.57 | both halves | 1e-05 | same gene group; STRING 807 |
| [[ZNF28]] | +0.63 | +0.57 / +0.68 | both halves | 1e-05 | same gene group |
| [[ZBTB39]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 | same gene group |
| [[ZNF2]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 | same gene group |
| [[MTHFS]] | +0.61 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[ZNF746]] | +0.61 | +0.49 / +0.60 | both halves | 1e-05 | same gene group |
| [[ZSCAN25]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 | same gene group |
| [[ZNF696]] | +0.60 | +0.65 / +0.58 | both halves | 7e-06 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.3, 4.5); signed map (-5.3, -14.8). **Vector** length 60.6, 8.56% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +7.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.7 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +5.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.2 | +4.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.8 | -6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.6 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.3 | -5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | +1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,382,081-3,401,065 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20417; previously ZNF434 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX65](https://www.uniprot.org/uniprotkb/Q9NX65) (Zinc finger and SCAN domain-containing protein 32):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [54925](https://www.ncbi.nlm.nih.gov/gene/54925):

> Enables identical protein binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20812) · Entrez [54925](https://www.ncbi.nlm.nih.gov/gene/54925) · UniProt [Q9NX65](https://www.uniprot.org/uniprotkb/Q9NX65) · Ensembl [ENSG00000140987](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140987)

## Data

Gene col 6472: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6472); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6472, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6472]; `tensor/DDL_lfc|DDL_z.npy` [6472]; `embed/gene_vectors.npy` [6472]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6472 or target_col == 6472). Every well: [[ZSCAN32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
