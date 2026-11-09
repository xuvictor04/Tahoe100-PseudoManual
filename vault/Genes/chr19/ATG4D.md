---
symbol: "ATG4D"
type: "gene"
col: 5112
ensembl_id: "ENSG00000130734"
name: "autophagy related 4D cysteine peptidase"
location: "19p13.2"
module: 12
arm: "+"
pooled_cpm: 6.82
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ATG4D

*autophagy related 4D cysteine peptidase* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.97× (z +14.4, q 4e-44, up in 32 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.736× (z -4.4, q 0.006, down in 9 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HS-578T 0.0622×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[IQ 1 (drug)]] 0.05 µM in 1 line (SHP-77 0.0629×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (NCI-H1573 0.0860×); [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (Hs 766T 0.0950×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFT22]] (+0.60, fdr 1e-05), [[GFER]] (+0.60, fdr 1e-05), [[CIDECP1]] (+0.60, fdr 1e-05); moves opposite to [[GART]] (-0.59, fdr 1e-05), [[TBC1D4]] (-0.58, fdr 1e-05), [[IPO7]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5112.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +14.4 | 4e-44 | 32/43 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +8.7 | 6e-16 | 24/45 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +7.7 | 2e-12 | 7/13 (BT-474, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +7.4 | 2e-11 | 20/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +6.9 | 8e-10 | 18/43 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +6.7 | 2e-09 | 24/41 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +5.9 | 4e-07 | 19/47 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 7e-06 | 10/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +5.1 | 2e-05 | 15/46 (A498, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.39×** | +5.0 | 3e-05 | 14/31 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +5.0 | 3e-05 | 11/47 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.36×** | +4.6 | 2e-04 | 11/40 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 1e-03 | 12/46 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **1.33×** | +4.1 | 0.002 | 12/37 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.002 | 12/47 (A-427, NCI-H2030, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.004 | 7/41 (A-427, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +3.7 | 0.008 | 10/45 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.010 | 3/38 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.013 | 2/43 (PANC-1, RPMI-7951) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.033 | 1/47 (NCI-H2347) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5112.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HS-578T 0.0622×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[IQ 1 (drug)]] 0.05 µM in 1 line (SHP-77 0.0629×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (NCI-H1573 0.0860×); [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (Hs 766T 0.0950×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.736×** | -4.4 | 0.006 | 9/44 (SNU-423, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.782×** | -3.7 | 0.068 | 9/45 (RPMI-7951, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Erlotinib (drug)]] 5 µM |  | 0.786× | -3.4 | 0.11 | 9/46 (RKO, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.854× | -3.3 | 0.12 | 8/48 (SHP-77, BT-474, …) | rises with dose |  |
| [[MK-3903 (drug)]] 0.05 µM |  | 0.796× | -3.2 | 0.15 | 12/47 (HCT15, HepG2/C3A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.802× | -3.2 | 0.15 | 6/45 (LOX-IMVI, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5112. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 6.49 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0950× (z -9.0) |
| [[HS-578T (line)]] | alt | 8.11 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0622× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 4.46 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0860× (z -9.3) |
| [[PANC-1 (line)]] | alt | 4.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 10.0 | 0 | 1 | — | [[IQ 1 (drug)]] 0.05 µM 0.0629× (z -12.2) |
| [[A-172 (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5112), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT22]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[GFER]] | +0.60 | +0.64 / +0.51 | both halves | 1e-05 | STRING 456 |
| [[CIDECP1]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[DNAL4]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[SAT2]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ALG12]] | +0.59 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[APBA3]] | +0.59 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[RFNG]] | +0.59 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[PI4KB]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[FBXW5]] | +0.58 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[PRR14]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[DPF2]] | +0.58 | +0.67 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GART]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[TBC1D4]] | -0.58 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[IPO7]] | -0.58 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[NOLC1]] | -0.56 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[UGGT2]] | -0.54 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[TXN]] | -0.54 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[EIF5A]] | -0.51 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[PRKDC]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[PAICS]] | -0.50 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[LDHB]] | -0.50 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[GLS]] | -0.50 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[RAN]] | -0.50 | -0.38 / -0.49 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.6, -0.8); signed map (-11.5, -1.1). **Vector** length 41.6, 4.29% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +3.3 | +5.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | +2.5 | +4.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.3 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | -0.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -1.5 | -3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.4 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -0.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -0.5 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 4D cysteine peptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,543,895-10,553,418 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APG4-D; previously AUTL4, APG4D |
| Gene groups (HGNC) | Autophagy related; MicroRNA protein coding host genes; Autophagy related 4 family cysteine peptidases |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TL0](https://www.uniprot.org/uniprotkb/Q86TL0) (Cysteine protease ATG4D):

> [Cysteine protease ATG4D]: Cysteine protease that plays a key role in autophagy by mediating both proteolytic activation and delipidation of ATG8 family proteins. The protease activity is required for proteolytic activation of ATG8 family proteins: cleaves the C-terminal amino acid of ATG8 proteins MAP1LC3 and GABARAPL2, to reveal a C-terminal glycine. Exposure of the glycine at the C-terminus is essential for ATG8 proteins conjugation to phosphatidylethanolamine (PE) and insertion to …

**Summary**, from NCBI Gene [84971](https://www.ncbi.nlm.nih.gov/gene/84971):

> Autophagy is the process by which endogenous proteins and damaged organelles are destroyed intracellularly. Autophagy is postulated to be essential for cell homeostasis and cell remodeling during differentiation, metamorphosis, non-apoptotic cell death, and aging. Reduced levels of autophagy have been described in some malignant tumors, and a role for autophagy in controlling the unregulated cell growth linked to cancer has been proposed. This gene belongs to the autophagy-related protein 4 …

**Accessions** — [HGNC:20789](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20789) · Entrez [84971](https://www.ncbi.nlm.nih.gov/gene/84971) · UniProt [Q86TL0](https://www.uniprot.org/uniprotkb/Q86TL0) · Ensembl [ENSG00000130734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130734)

## Data

Gene col 5112: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5112); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5112, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5112]; `tensor/DDL_lfc|DDL_z.npy` [5112]; `embed/gene_vectors.npy` [5112]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5112 or target_col == 5112). Every well: [[ATG4D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG4D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
