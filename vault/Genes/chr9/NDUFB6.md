---
symbol: "NDUFB6"
type: "gene"
col: 9096
ensembl_id: "ENSG00000165264"
name: "NADH:ubiquinone oxidoreductase subunit B6"
location: "9p21.1"
module: 220
arm: "+"
pooled_cpm: 29.27
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/220"]
generated_by: "tahoemap"
---

# NDUFB6

*NADH:ubiquinone oxidoreductase subunit B6* — 9p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.69× (z +9.6, q 5e-19, up in 40 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.24× (z +3.4, q 0.031, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 4 lines (LS 180 5.09×, LoVo 3.75×, SW480 3.18×, NCI-H460 3.54×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW 900 5.70×, PANC-1 3.12×, A-172 4.10×, A549 4.17×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 3.47×, KATO III 3.65×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFB7]] (+0.71, fdr 7e-06), [[HMGN3]] (+0.64, fdr 1e-05), [[SDHB]] (+0.63, fdr 1e-05); moves opposite to [[EIF5]] (-0.63, fdr 1e-05), [[PPIEL-1]] (-0.58, fdr 5e-05), [[DDX5]] (-0.57, fdr 4e-05).
> It is in [[Module 220]], a single-armed module (Respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 18 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9096.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 4 lines (LS 180 5.09×, LoVo 3.75×, SW480 3.18×, NCI-H460 3.54×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW 900 5.70×, PANC-1 3.12×, A-172 4.10×, A549 4.17×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 3.47×, KATO III 3.65×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.69×** | +9.6 | 5e-19 | 40/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.39×** | +9.2 | 1e-17 | 32/36 (SW 900, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.04×** | +7.8 | 1e-12 | 39/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.94×** | +6.7 | 3e-09 | 33/40 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +6.2 | 7e-08 | 36/45 (NCI-H2030, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.73×** | +6.0 | 2e-07 | 39/48 (J82, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.66×** | +5.6 | 2e-06 | 38/48 (PANC-1, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.62×** | +5.3 | 1e-05 | 38/48 (A549, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **1.53×** | +4.5 | 5e-04 | 32/47 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.43×** | +3.9 | 0.005 | 26/48 (BT-474, J82, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.95×** | +3.8 | 0.006 | 27/48 (KATO III, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~73% of this change | **1.41×** | +3.8 | 0.006 | 24/46 (NCI-H2347, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +3.5 | 0.019 | 22/48 (LS 180, LoVo, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.031 | 22/48 (SNU-423, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.37×** | +3.3 | 0.032 | 23/48 (LS 180, NCI-H460, …) | rises with dose | composition shift |
| [[Arbutin (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.043 | 20/48 (HCT15, PANC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9096.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.742× | -3.0 | 0.65 | 18/48 (RPMI-7951, CFPAC-1, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.586× | -3.0 | 0.65 | 19/48 (AsPC-1, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9096. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 41.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[LS 180 (line)]] | wt | 35.9 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.09× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[PANC-1 (line)]] | alt | 44.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A-172 (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.10× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A549 (line)]] | wt | 27.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[LoVo (line)]] | wt | 31.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.75× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H460 (line)]] | wt | 21.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.54× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[SW 900 (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SW480 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.18× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[A-427 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9096), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFB7]] | +0.71 | +0.61 / +0.67 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[HMGN3]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SDHB]] | +0.63 | +0.50 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 859 |
| [[PEX2]] | +0.63 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[AP2S1]] | +0.62 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PXMP4]] | +0.61 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[MALSU1]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ANAPC11]] | +0.61 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[MED9]] | +0.61 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[TMEM14A]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[UQCR11]] | +0.60 | +0.58 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 963 |
| [[NDUFC2]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF5]] | -0.63 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[PPIEL-1]] | -0.58 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[DDX5]] | -0.57 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[C6orf62]] | -0.56 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[FLII]] | -0.56 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[PARD6G-AS1]] | -0.55 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[CSRNP2]] | -0.55 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[PLAC8L1]] | -0.55 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[SLC2A9]] | -0.54 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[MPP4]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SLC22A1]] | -0.53 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[HCLS1]] | -0.53 | -0.55 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 220]] — Respiratory electron transport; 11 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.0, -11.5); signed map (-32.6, -11.1). **Vector** length 64.3, 14.7% of its response variance represented; |z| ≥ 3 in 661 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.3 | +3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +3.9 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +2.7 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | +2.8 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit B6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.1 — chr9:32,553,001-32,573,184 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B17, CI |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Complex I biogenesis; Mitochondrial protein degradation; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O95139](https://www.uniprot.org/uniprotkb/O95139) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4712](https://www.ncbi.nlm.nih.gov/gene/4712):

> The protein encoded by this gene is a subunit of the multisubunit NADH:ubiquinone oxidoreductase (complex I). Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Alternative splicing occurs at this locus and three transcript variants …

**Accessions** — [HGNC:7701](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7701) · Entrez [4712](https://www.ncbi.nlm.nih.gov/gene/4712) · UniProt [O95139](https://www.uniprot.org/uniprotkb/O95139) · Ensembl [ENSG00000165264](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165264)

## Data

Gene col 9096: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9096); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9096, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9096]; `tensor/DDL_lfc|DDL_z.npy` [9096]; `embed/gene_vectors.npy` [9096]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9096 or target_col == 9096). Every well: [[NDUFB6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFB6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
