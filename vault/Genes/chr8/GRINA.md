---
symbol: "GRINA"
type: "gene"
col: 10952
ensembl_id: "ENSG00000178719"
name: "glutamate ionotropic receptor NMDA type subunit associated protein 1"
location: "8q24.3"
module: 59
arm: "+"
pooled_cpm: 34.67
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# GRINA

*glutamate ionotropic receptor NMDA type subunit associated protein 1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.66× (z +21.6, q 0e+00, up in 48 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.75× (z +6.7, q 3e-09, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.484× (z -4.7, q 0.001, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEU1]] (+0.63, fdr 7e-06), [[WASHC4]] (+0.61, fdr 7e-06), [[SLC39A1]] (+0.61, fdr 7e-06); moves opposite to [[STRAP]] (-0.58, fdr 1e-05), [[CUZD1]] (-0.51, fdr 3e-05), [[SNRPD3]] (-0.50, fdr 2e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10952.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.66×** | +21.6 | 0e+00 | 48/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +8.5 | 6e-15 | 27/34 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +7.6 | 7e-12 | 34/45 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.53×** | +7.5 | 1e-11 | 32/47 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +6.7 | 3e-09 | 35/48 (HEC-1-A, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +6.1 | 1e-07 | 36/46 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here); position effect removed |
| [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM | ⚠ unreliable plate only; position correction uncertain | **1.62×** | +6.0 | 2e-07 | 40/48 (A498, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +5.9 | 3e-07 | 37/48 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.4 | 6e-04 | 22/46 (KATO III, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.38×** | +4.0 | 0.004 | 26/47 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.008 | 23/48 (HOP62, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +3.5 | 0.019 | 21/41 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.68×** | +3.4 | 0.035 | 19/48 (A-172, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.086 | 19/48 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10952.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.484×** | -4.7 | 0.001 | 33/48 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.546×** | -3.9 | 0.023 | 26/47 (BT-474, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.743×** | -3.6 | 0.068 | 25/47 (C32, J82, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10952. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 81.8 | 3 (3 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.62× (z +17.8) ⚠ position not correctable | — |
| [[AsPC-1 (line)]] | alt | 49.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.67× (z +15.2) ⚠ position not correctable | [[Dinaciclib (drug)]] 5 µM 0.346× (z -8.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 26.2 | 3 (3 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.63× (z +12.7) ⚠ position not correctable | — |
| [[HS-578T (line)]] | alt | 51.0 | 3 (3 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.65× (z +14.1) ⚠ position not correctable | — |
| [[J82 (line)]] | alt | 54.1 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.68× (z +16.5) ⚠ position not correctable | — |
| [[Panc 03.27 (line)]] | alt | 41.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +15.5) ⚠ position not correctable | [[Dinaciclib (drug)]] 5 µM 0.188× (z -13.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 27.5 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.62× (z +14.4) ⚠ position not correctable | — |
| [[RPMI-7951 (line)]] | alt | 45.7 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.60× (z +12.1) ⚠ position not correctable | — |
| [[SW480 (line)]] | alt | 15.8 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.66× (z +13.1) ⚠ position not correctable | — |
| [[A-172 (line)]] | wt | 51.6 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.71× (z +17.1) ⚠ position not correctable | — |
| [[A-427 (line)]] | wt | 32.7 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.57× (z +11.0) ⚠ position not correctable | — |
| [[A549 (line)]] | wt | 37.9 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.61× (z +12.7) ⚠ position not correctable | — |
| [[BT-474 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.66× (z +11.6) ⚠ position not correctable | — |
| [[C-33 A (line)]] | alt | 21.6 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.79× (z +10.2) ⚠ position not correctable | — |
| [[C32 (line)]] | wt | 27.2 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.63× (z +10.1) ⚠ position not correctable | — |
| [[CFPAC-1 (line)]] | alt | 27.6 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.58× (z +11.6) ⚠ position not correctable | — |
| [[HCT15 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.66× (z +8.8) ⚠ position not correctable | — |
| [[HepG2_C3A (line)]] | wt | 27.0 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +10.8) ⚠ position not correctable | — |
| [[HOP62 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +14.6) ⚠ position not correctable | — |
| [[Hs 766T (line)]] | wt | 52.5 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.70× (z +14.3) ⚠ position not correctable | — |
| [[HT-29 (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.64× (z +12.1) ⚠ position not correctable | — |
| [[hTERT-HPNE (line)]] | wt | 39.2 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.66× (z +11.6) ⚠ position not correctable | — |
| [[KATO III (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.62× (z +13.1) ⚠ position not correctable | — |
| [[LoVo (line)]] | wt | 13.6 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.69× (z +11.3) ⚠ position not correctable | — |
| [[LOX-IMVI (line)]] | wt | 23.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.66× (z +11.6) ⚠ position not correctable | — |
| [[LS 180 (line)]] | wt | 20.2 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.66× (z +11.4) ⚠ position not correctable | — |
| [[MIA PaCa-2 (line)]] | alt | 49.6 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.92× (z +18.5) ⚠ position not correctable | — |
| [[NCI-H1573 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.66× (z +10.6) ⚠ position not correctable | — |
| [[NCI-H1792 (line)]] | alt | 21.0 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.82× (z +12.2) ⚠ position not correctable | — |
| [[NCI-H2030 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.55× (z +12.3) ⚠ position not correctable | — |
| [[NCI-H23 (line)]] | alt | 34.6 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.50× (z +10.8) ⚠ position not correctable | — |
| [[NCI-H2347 (line)]] | alt | 55.9 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.63× (z +16.3) ⚠ position not correctable | — |
| [[NCI-H460 (line)]] | wt | 19.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.70× (z +12.8) ⚠ position not correctable | — |
| [[RKO (line)]] | wt | 69.6 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.55× (z +13.1) ⚠ position not correctable | — |
| [[SHP-77 (line)]] | alt | 18.3 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.71× (z +9.8) ⚠ position not correctable | — |
| [[SK-MEL-2 (line)]] | alt | 37.8 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.67× (z +12.9) ⚠ position not correctable | — |
| [[SNU-1 (line)]] | wt | 34.1 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.70× (z +10.1) ⚠ position not correctable | — |
| [[SNU-423 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.79× (z +15.4) ⚠ position not correctable | — |
| [[SW 900 (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.71× (z +11.4) ⚠ position not correctable | — |
| [[SW1417 (line)]] | alt | 41.7 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.72× (z +14.2) ⚠ position not correctable | — |
| [[AN3 CA (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10952), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEU1]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[WASHC4]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SLC39A1]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[PRR14]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[DLX2]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[FNTA]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[UAP1L1]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TOLLIP]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[FLCN]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[IRF7]] | +0.58 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[ZNF468]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[TRAF4]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRAP]] | -0.58 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[CUZD1]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[SNRPD3]] | -0.50 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[ZNF519]] | -0.50 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[SNHG30]] | -0.50 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[C21orf58]] | -0.48 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[RBM14-RBM4]] | -0.48 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.3, -33.0); signed map (5.8, -10.6). **Vector** length 86.9, 21.3% of its response variance represented; |z| ≥ 3 in 662 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +5.9 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.1 | +4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +5.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.8 | +3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.1 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.9 | +1.6 |
| fall | [[Verteporfin (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.3 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -1.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | glutamate ionotropic receptor NMDA type subunit associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,990,056-143,993,415 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HNRGW, TMBIM3, LFG1; previously NMDARA1 |
| Gene groups (HGNC) | Transmembrane BAX inhibitor motif containing |
| Hallmark sets | UV_RESPONSE_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z429](https://www.uniprot.org/uniprotkb/Q7Z429) (Protein lifeguard 1):

> Potential apoptotic regulator.

**Summary**, from NCBI Gene [2907](https://www.ncbi.nlm.nih.gov/gene/2907):

> Predicted to enable calcium channel activity. Predicted to be involved in negative regulation of extrinsic apoptotic signaling pathway via death domain receptors and negative regulation of neuron apoptotic process. Predicted to act upstream of or within endoplasmic reticulum calcium ion homeostasis and negative regulation of endoplasmic reticulum stress-induced intrinsic apoptotic signaling pathway. Located in Golgi membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4589) · Entrez [2907](https://www.ncbi.nlm.nih.gov/gene/2907) · UniProt [Q7Z429](https://www.uniprot.org/uniprotkb/Q7Z429) · Ensembl [ENSG00000178719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178719)

## Data

Gene col 10952: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10952); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10952, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10952]; `tensor/DDL_lfc|DDL_z.npy` [10952]; `embed/gene_vectors.npy` [10952]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10952 or target_col == 10952). Every well: [[GRINA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRINA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
