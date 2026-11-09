---
symbol: "CDC5L"
type: "gene"
col: 1766
ensembl_id: "ENSG00000096401"
name: "cell division cycle 5 like"
location: "6p21.1"
module: 12
arm: "+"
pooled_cpm: 100.66
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CDC5L

*cell division cycle 5 like* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.48× (z +9.9, q 3e-20, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.758× (z -8.3, q 6e-14, down in 37 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.296×, SW 900 0.353×, LS 180 0.511×, HEC-1-A 0.561×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (CFPAC-1 0.530×, NCI-H2347 0.600×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.541×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.554×); [[Cilostazol (drug)]] 0.05 µM in 1 line (SW 1088 0.0827×); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.530×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHAX]] (+0.67, fdr 7e-06), [[SNW1]] (+0.66, fdr 7e-06), [[TPR]] (+0.65, fdr 7e-06); moves opposite to [[MXRA7]] (-0.54, fdr 6e-05), [[NPIPB11]] (-0.51, fdr 9e-05), [[PITPNA]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1766.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +9.9 | 3e-20 | 38/48 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +9.3 | 6e-18 | 41/49 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +7.9 | 4e-13 | 38/48 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.37×** | +7.6 | 3e-12 | 35/48 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.28×** | +6.1 | 1e-07 | 30/47 (LoVo, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +5.9 | 4e-07 | 29/48 (A498, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +5.7 | 9e-07 | 29/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +5.6 | 1e-06 | 30/48 (PANC-1, HEC-1-A, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +5.5 | 2e-06 | 23/48 (A498, A549, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.23×** | +5.4 | 5e-06 | 25/48 (LoVo, HepG2/C3A, …) | inconsistent across doses | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.47×** | +5.1 | 2e-05 | 38/47 (C32, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +4.6 | 2e-04 | 24/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.3 | 0.048 | 12/48 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.073 | 15/48 (NCI-H2347, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1766.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.296×, SW 900 0.353×, LS 180 0.511×, HEC-1-A 0.561×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (CFPAC-1 0.530×, NCI-H2347 0.600×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.541×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.554×); [[Cilostazol (drug)]] 0.05 µM in 1 line (SW 1088 0.0827×); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.530×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.758×** | -8.3 | 6e-14 | 37/49 (AsPC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.868× | -3.5 | 0.11 | 17/44 (Panc 03.27, SW 900, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.4 | 0.11 | 18/48 (J82, A498, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.886× | -3.1 | 0.28 | 15/48 (BT-474, COLO 205, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.888× | -3.0 | 0.28 | 18/48 (NCI-H23, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1766. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 101 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +11.4) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.99× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 97.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.86× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.561× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 88.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.92× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.475× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.541× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 175 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.21× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 87.1 | 2 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 1.64× (z +8.6) | — |
| [[A549 (line)]] | wt | 69.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 77.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -9.6) |
| [[C32 (line)]] | wt | 75.0 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.51× (z +9.3) ⚠ toxic; cell-cycle shift, explains ~31% of this change | — |
| [[HepG2_C3A (line)]] | wt | 115 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 1.92× (z +9.0) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[LS 180 (line)]] | wt | 92.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.511× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 139 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.530× (z -8.7) |
| [[SW 1088 (line)]] | alt | 95.2 | 0 | 1 | — | [[Cilostazol (drug)]] 0.05 µM 0.0827× (z -9.1) |
| [[SW 900 (line)]] | alt | 90.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 112 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.87× (z +9.2) | — |
| [[A-172 (line)]] | wt | 85.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 153 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 123 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 94.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 128 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 109 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 96.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 97.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1766), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHAX]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[SNW1]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[TPR]] | +0.65 | +0.61 / +0.70 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 573 |
| [[ASNSD1]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[CRNKL1]] | +0.63 | +0.68 / +0.63 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[AGGF1]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ASB8]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SMC3]] | +0.62 | +0.55 / +0.66 | both halves | 1e-05 | STRING 663 |
| [[FUNDC1]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ZNF182]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[MMADHC]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PHF3]] | +0.58 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXRA7]] | -0.54 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[NPIPB11]] | -0.51 | -0.37 / -0.56 | both halves | 9e-05 |  |
| [[PITPNA]] | -0.51 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[UBE2G2]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CORO7]] | -0.50 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[CTTN]] | -0.49 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CTC-338M12.4]] | -0.49 | -0.41 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-30.7, 1.9); signed map (1.2, -17.2). **Vector** length 101, 25.8% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +7.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +9.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.0 | +5.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.0 | +1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.6 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 5 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:44,387,706-44,450,425 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PCDC5RP, hCDC5, CEF1, CDC5 |
| Gene groups (HGNC) | Myb/SANT domain containing; NineTeen complex; Spliceosomal C complex; MicroRNA protein coding host genes |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99459](https://www.uniprot.org/uniprotkb/Q99459) (Cell division cycle 5-like protein):

> DNA-binding protein involved in cell cycle control. May act as a transcription activator. Plays a role in pre-mRNA splicing as core component of precatalytic, catalytic and postcatalytic spliceosomal complexes. Component of the PRP19-CDC5L complex that forms an integral part of the spliceosome and is required for activating pre-mRNA splicing. The PRP19-CDC5L complex may also play a role in the response to DNA damage (DDR). As a component of the minor spliceosome, involved in the splicing of …

**Summary**, from NCBI Gene [988](https://www.ncbi.nlm.nih.gov/gene/988):

> The protein encoded by this gene shares a significant similarity with Schizosaccharomyces pombe cdc5 gene product, which is a cell cycle regulator important for G2/M transition. This protein has been demonstrated to act as a positive regulator of cell cycle G2/M progression. It was also found to be an essential component of a non-snRNA spliceosome, which contains at least five additional protein factors and is required for the second catalytic step of pre-mRNA splicing. [provided by RefSeq, Jul …

**Accessions** — [HGNC:1743](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1743) · Entrez [988](https://www.ncbi.nlm.nih.gov/gene/988) · UniProt [Q99459](https://www.uniprot.org/uniprotkb/Q99459) · Ensembl [ENSG00000096401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000096401)

## Data

Gene col 1766: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1766); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1766, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1766]; `tensor/DDL_lfc|DDL_z.npy` [1766]; `embed/gene_vectors.npy` [1766]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1766 or target_col == 1766). Every well: [[CDC5L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC5L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
