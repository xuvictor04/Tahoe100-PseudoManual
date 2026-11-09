---
symbol: "SLC15A4"
type: "gene"
col: 6300
ensembl_id: "ENSG00000139370"
name: "solute carrier family 15 member 4"
location: "12q24.33"
module: 30
arm: "+"
pooled_cpm: 35.32
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# SLC15A4

*solute carrier family 15 member 4* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.23× (z +4.8, q 0.001, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.491× (z -16.1, q 0e+00, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMS19]] (+0.71, fdr 7e-06), [[HSDL1]] (+0.67, fdr 1e-05), [[LCMT1]] (+0.67, fdr 7e-06); moves opposite to [[PHF8]] (-0.66, fdr 1e-05), [[ZC3H11A]] (-0.65, fdr 1e-05), [[DCAF8]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6300.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +4.8 | 0.001 | 23/48 (CFPAC-1, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +4.3 | 0.005 | 21/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.021 | 18/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.26×** | +3.5 | 0.062 | 17/48 (HOP62, SK-MEL-2, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.062 | 15/48 (SNU-423, HS-578T, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +3.4 | 0.062 | 16/48 (COLO 205, CFPAC-1, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.2 | 0.10 | 9/48 (J82, LoVo, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.12 | 6/48 (J82, A549, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6300.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.491×** | -16.1 | 0e+00 | 37/47 (LOX-IMVI, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.464×** | -11.9 | 6e-30 | 40/48 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.526×** | -10.3 | 1e-22 | 33/43 (RPMI-7951, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.613×** | -7.8 | 7e-13 | 36/48 (AN3 CA, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.608×** | -7.7 | 2e-12 | 23/35 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.751×** | -4.2 | 0.002 | 21/37 (A-172, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.770×** | -4.2 | 0.002 | 19/48 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.835× | -4.1 | 0.003 | 16/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.840× | -3.9 | 0.005 | 22/48 (A-172, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.793×** | -3.7 | 0.012 | 17/48 (HOP62, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.811×** | -3.4 | 0.041 | 18/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.817×** | -3.2 | 0.059 | 14/48 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.825×** | -3.1 | 0.088 | 16/48 (A498, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6300. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 100 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.491× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 35.6 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.317× (z -15.0) |
| [[SNU-423 (line)]] | alt | 107 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.333× (z -14.8) |
| [[RPMI-7951 (line)]] | alt | 56.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -22.4) |
| [[MIA PaCa-2 (line)]] | alt | 39.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 73.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -25.1) |
| [[C32 (line)]] | wt | 58.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -19.1) |
| [[HEC-1-A (line)]] | alt | 27.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -12.2) |
| [[HOP62 (line)]] | alt | 42.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -18.6) |
| [[HS-578T (line)]] | alt | 33.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -17.3) |
| [[NCI-H460 (line)]] | wt | 23.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.6) |
| [[SHP-77 (line)]] | alt | 40.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 59.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.9) |
| [[A549 (line)]] | wt | 41.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -16.2) |
| [[hTERT-HPNE (line)]] | wt | 52.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -14.5) |
| [[J82 (line)]] | alt | 36.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 30.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0998× (z -25.4) |
| [[NCI-H1792 (line)]] | alt | 40.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.6) |
| [[NCI-H2030 (line)]] | alt | 29.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.458× (z -9.0) |
| [[PANC-1 (line)]] | alt | 33.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -14.7) |
| [[A-427 (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.284× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 25.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0615× (z -10.2) |
| [[H4 (line)]] | wt | 49.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0748× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.101× (z -8.7) |
| [[SW 1088 (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -9.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 42.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6300), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMS19]] | +0.71 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[HSDL1]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[SEC11A]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ANKRD27]] | +0.65 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[TMEM120B]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[DHRS1]] | +0.64 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ZNF250]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[UNC45A]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[RALA]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SVIL-AS1-1]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[NDUFAF7]] | +0.62 | +0.58 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF8]] | -0.66 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[ZC3H11A]] | -0.65 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[DCAF8]] | -0.64 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[RBM23]] | -0.61 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[BAZ2B]] | -0.61 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[SKIL]] | -0.60 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[AKT1S1]] | -0.60 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[USP16]] | -0.60 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[TIA1]] | -0.59 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[SRCAP]] | -0.58 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[C11orf58]] | -0.58 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[RAB1B]] | -0.58 | -0.39 / -0.55 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.683). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-0.2, -4.1); signed map (-37.5, -2.2). **Vector** length 115, 29.7% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.9 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.4 | +3.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.2 | -16.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.8 | -11.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -5.5 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -3.5 | -10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.2 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 15 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:128,793,194-128,823,958 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PHT1, PTR4 |
| Gene groups (HGNC) | Solute carrier family 15 |
| Reactome | 10 pathways, smallest: Proton/oligopeptide cotransporters; SLC-mediated transport of oligopeptides; SLC15A4:TASL-dependent IRF5 activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N697](https://www.uniprot.org/uniprotkb/Q8N697) (Solute carrier family 15 member 4):

> Proton-coupled amino-acid transporter that mediates the transmembrane transport of L-histidine and some di- and tripeptides from inside the lysosome to the cytosol, and plays a key role in innate immune response. Preferably binds to short peptides with a basic residue at the first position and a hydrophobic residue at the second position. Able to transport a variety of di- and tripeptides, including carnosine and some peptidoglycans. Transporter activity is pH-dependent and maximized in the …

**Summary**, from NCBI Gene [121260](https://www.ncbi.nlm.nih.gov/gene/121260):

> Enables transmembrane transporter activity. Involved in dipeptide import across plasma membrane; peptidoglycan transport; and positive regulation of pattern recognition receptor signaling pathway. Located in endolysosome membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23090) · Entrez [121260](https://www.ncbi.nlm.nih.gov/gene/121260) · UniProt [Q8N697](https://www.uniprot.org/uniprotkb/Q8N697) · Ensembl [ENSG00000139370](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139370)

## Data

Gene col 6300: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6300); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6300, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6300]; `tensor/DDL_lfc|DDL_z.npy` [6300]; `embed/gene_vectors.npy` [6300]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6300 or target_col == 6300). Every well: [[SLC15A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC15A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
