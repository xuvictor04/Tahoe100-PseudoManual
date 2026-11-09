---
symbol: "NECAB3"
type: "gene"
col: 4699
ensembl_id: "ENSG00000125967"
name: "N-terminal EF-hand calcium binding protein 3"
location: "20q11.22"
module: 60
arm: "+"
pooled_cpm: 6.31
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# NECAB3

*N-terminal EF-hand calcium binding protein 3* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.79× (z +6.3, q 1e-07, up in 24 of 47 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.70× (z +5.8, q 2e-06, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.421× (z -5.0, q 2e-04, down in 18 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.108×; ⚠ cell-cycle shift, would explain all of this change); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0472×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.143×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0597×); [[c-Kit-IN-1 (drug)]] 5 µM in 1 line (A498 0.0435×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP5]] (+0.72, fdr 7e-06), [[C1orf216]] (+0.70, fdr 1e-05), [[MAPK12]] (+0.68, fdr 8e-06); moves opposite to [[SUMO4]] (-0.62, fdr 3e-05), [[MED19]] (-0.61, fdr 1e-05), [[AFTPH]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4699.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.79×** | +6.3 | 1e-07 | 24/47 (RPMI-7951, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +5.8 | 2e-06 | 23/47 (SW480, BT-474, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +5.7 | 2e-06 | 11/17 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.69×** | +5.7 | 2e-06 | 24/47 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +5.5 | 4e-06 | 20/46 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.62×** | +5.3 | 1e-05 | 23/47 (KATO III, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.66×** | +5.2 | 2e-05 | 16/44 (NCI-H1792, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.41×** | +3.6 | 0.021 | 5/13 (Hs 766T, CFPAC-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~77% of this change | **1.39×** | +3.4 | 0.037 | 14/31 (J82, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.35×** | +3.2 | 0.064 | 14/47 (PANC-1, LoVo, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.064 | 2/40 (NCI-H1792, AsPC-1) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.35×** | +3.1 | 0.088 | 14/41 (HOP62, NCI-H460, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.1 | 0.096 | 1/48 (KATO III) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4699.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.108×; ⚠ cell-cycle shift, would explain all of this change); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0472×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.143×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0597×); [[c-Kit-IN-1 (drug)]] 5 µM in 1 line (A498 0.0435×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -5.0 | 2e-04 | 18/45 (A-427, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.727×** | -4.9 | 2e-04 | 19/43 (NCI-H23, SK-MEL-2, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.679×** | -4.1 | 0.009 | 15/45 (HS-578T, A-172, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.714×** | -3.7 | 0.031 | 15/41 (NCI-H23, HCT15, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.567× | -3.2 | 0.13 | 11/39 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.749× | -3.2 | 0.15 | 9/46 (H4, NCI-H23, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.745× | -3.1 | 0.15 | 8/47 (LOX-IMVI, COLO 205, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4699. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 6.70 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Docetaxel (Trihydrate) (drug)]] 0.05 µM 0.0802× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 8.10 | 0 | 2 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0472× (z -11.3) |
| [[A498 (line)]] | wt | 9.03 | 0 | 1 | — | [[c-Kit-IN-1 (drug)]] 5 µM 0.0435× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 3.65 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0931× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 5.96 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4699), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP5]] | +0.72 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[C1orf216]] | +0.70 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.68 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[ZNF731P]] | +0.68 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[RTEL1]] | +0.67 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[AHSA1]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[PLCG1]] | +0.63 | +0.68 / +0.49 | both halves | 1e-05 | same gene group |
| [[FANCG]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[MAPK9]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[NDOR1]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[B4GALNT1]] | +0.63 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[AKT1]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUMO4]] | -0.62 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[MED19]] | -0.61 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[AFTPH]] | -0.60 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[SNAPC1]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[BTG1]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[NBPF19]] | -0.57 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[KDM5B]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[ANKRD12]] | -0.56 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[EXOC1]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[NBPF10]] | -0.55 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SNRPB2]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[ACAP1]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.506). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.4, -27.2); signed map (-28.1, -31.7). **Vector** length 60.0, 8.20% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.1 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +2.7 | +3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.7 | +5.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.5 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.1 | -1.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -2.7 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.6 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | N-terminal EF-hand calcium binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:33,657,087-33,674,463 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XB51, dJ63M2.4, NIP1, dJ63M2.5, EFCBP3; previously SYTIP2, APBA2BP |
| Gene groups (HGNC) | N-terminal EF-hand calcium binding proteins; EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96P71](https://www.uniprot.org/uniprotkb/Q96P71) (N-terminal EF-hand calcium-binding protein 3):

> Inhibits the interaction of APBA2 with amyloid-beta precursor protein (APP), and hence allows formation of amyloid-beta. May enhance the activity of HIF1A and thus promote glycolysis under normoxic conditions; the function requires its ABM domain and may implicate the stabilization of the interaction between HIF1AN and APBA3.

**Summary**, from NCBI Gene [63941](https://www.ncbi.nlm.nih.gov/gene/63941):

> The protein encoded by this gene interacts with the amino-terminal domain of the neuron-specific X11-like protein (X11L), inhibits the association of X11L with amyloid precursor protein through a non-competitive mechanism, and abolishes the suppression of beta-amyloid production by X11L. This protein, together with X11L, may play an important role in the regulatory system of amyloid precursor protein metabolism and beta-amyloid generation. The protein is phosphorylated by NIMA-related expressed …

**Accessions** — [HGNC:15851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15851) · Entrez [63941](https://www.ncbi.nlm.nih.gov/gene/63941) · UniProt [Q96P71](https://www.uniprot.org/uniprotkb/Q96P71) · Ensembl [ENSG00000125967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125967)

## Data

Gene col 4699: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4699); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4699, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4699]; `tensor/DDL_lfc|DDL_z.npy` [4699]; `embed/gene_vectors.npy` [4699]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4699 or target_col == 4699). Every well: [[NECAB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NECAB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
