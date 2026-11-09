---
symbol: "DCXR"
type: "gene"
col: 9846
ensembl_id: "ENSG00000169738"
name: "dicarbonyl and L-xylulose reductase"
location: "17q25.3"
module: 24
arm: "+"
pooled_cpm: 13.51
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# DCXR

*dicarbonyl and L-xylulose reductase* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.70× (z +8.4, q 2e-14, up in 34 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +6.9, q 8e-10, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.302× (z -3.7, q 0.074, down in 24 of 43 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C17orf49]] (+0.71, fdr 7e-06, ⚠ C17orf49 in the vector space only through flagged drug-doses), [[FBXL15]] (+0.70, fdr 7e-06), [[TIMM17B]] (+0.66, fdr 7e-06, ⚠ TIMM17B in the vector space only through flagged drug-doses), [[PITPNA-AS1]] (+0.66, fdr 1e-05), [[POLR2H]] (+0.66, fdr 2e-04); moves opposite to [[NAA50]] (-0.58, fdr 1e-05), [[MACROH2A1]] (-0.58, fdr 2e-05), [[XRCC5]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9846.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.70×** | +8.4 | 2e-14 | 34/35 (LoVo, HEC-1-A, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.30×** | +7.7 | 5e-12 | 46/47 (HEC-1-A, KATO III, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **3.05×** | +7.1 | 2e-10 | 44/47 (SW480, HEC-1-A, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +6.9 | 8e-10 | 42/46 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.77×** | +6.3 | 4e-08 | 19/21 (NCI-H460, Hs 766T, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.70×** | +6.1 | 8e-08 | 39/46 (AsPC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **2.38×** | +5.5 | 2e-06 | 39/47 (HT-29, KATO III, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.46×** | +5.3 | 7e-06 | 22/28 (KATO III, HEC-1-A, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +5.2 | 1e-05 | 30/39 (HOP62, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.73×** | +4.9 | 5e-05 | 32/46 (AsPC-1, COLO 205, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +4.2 | 0.002 | 26/46 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.86×** | +4.0 | 0.003 | 32/42 (Hs 766T, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.86×** | +4.0 | 0.003 | 32/47 (SW480, A549, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.78×** | +3.6 | 0.015 | 27/45 (LS 180, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +3.5 | 0.015 | 21/45 (RKO, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **3.08×** | +3.5 | 0.018 | 26/43 (KATO III, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.018 | 22/48 (NCI-H2347, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.64×** | +3.1 | 0.049 | 23/47 (NCI-H23, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9846.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.302×** | -3.7 | 0.074 | 24/43 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.571×** | -3.7 | 0.074 | 28/47 (RKO, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.569×** | -3.5 | 0.098 | 24/47 (BT-474, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.630× | -3.0 | 0.36 | 20/46 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9846. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 8.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.35× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 5.47 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +8.9) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[COLO 205 (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +8.5) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[LoVo (line)]] | wt | 11.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.20× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9846), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 9 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C17orf49]] ⚠ | +0.71 | +0.60 / +0.71 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[FBXL15]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[TIMM17B]] ⚠ | +0.66 | +0.67 / +0.61 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PITPNA-AS1]] | +0.66 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[POLR2H]] | +0.66 | +0.32 / +0.77 | both halves | 2e-04 |  |
| [[MED19]] | +0.65 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[TMEM42]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[FKBP2]] ⚠ | +0.64 | +0.47 / +0.59 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PQBP1]] | +0.64 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[LAGE3]] | +0.63 | +0.28 / +0.76 | both halves | 3e-04 |  |
| [[TRAPPC5]] | +0.63 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[NDUFA7]] | +0.63 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[TMEM205]] | +0.62 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[RNF7]] | +0.62 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[DNAL4]] | +0.62 | +0.71 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA50]] | -0.58 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[MACROH2A1]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[XRCC5]] | -0.57 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[MAPK9]] | -0.57 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[TMX3]] | -0.56 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[TARDBP]] | -0.56 | -0.32 / -0.61 | both halves | 2e-04 |  |
| [[NUDT5]] | -0.56 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[HCFC1]] | -0.55 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[TMEM33]] | -0.55 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[CCT5]] | -0.54 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[EIF5A]] | -0.54 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[HNRNPA3]] | -0.54 | -0.46 / -0.59 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.652). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.2, -20.0); signed map (-12.6, -0.0). **Vector** length 66.6, 16.5% of its response variance represented; |z| ≥ 3 in 730 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.5 | +6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +4.2 | +4.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.4 | +4.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -3.0 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -2.6 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | dicarbonyl and L-xylulose reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,035,136-82,037,709 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIDCR, DCR, SDR20C1, HCR2, P34H |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | XENOBIOTIC_METABOLISM, ESTROGEN_RESPONSE_LATE, P53_PATHWAY |
| Reactome | 4 pathways, smallest: Formation of xylulose-5-phosphate; Diseases of carbohydrate metabolism; Diseases of metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4W1](https://www.uniprot.org/uniprotkb/Q7Z4W1) (L-xylulose reductase):

> Catalyzes the NADPH-dependent reduction of several pentoses, tetroses, trioses, alpha-dicarbonyl compounds and L-xylulose. Can use both NAD and NADP as cosubstrate but shows higher activity with NADP. Participates in the uronate cycle of glucose metabolism. May play a role in the water absorption and cellular osmoregulation in the proximal renal tubules by producing xylitol, an osmolyte, thereby preventing osmolytic stress from occurring in the renal tubules.

**Summary**, from NCBI Gene [51181](https://www.ncbi.nlm.nih.gov/gene/51181):

> The protein encoded by this gene acts as a homotetramer to catalyze diacetyl reductase and L-xylulose reductase reactions. The encoded protein may play a role in the uronate cycle of glucose metabolism and in the cellular osmoregulation in the proximal renal tubules. Defects in this gene are a cause of pentosuria. Two transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:18985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18985) · Entrez [51181](https://www.ncbi.nlm.nih.gov/gene/51181) · UniProt [Q7Z4W1](https://www.uniprot.org/uniprotkb/Q7Z4W1) · Ensembl [ENSG00000169738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169738)

## Data

Gene col 9846: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9846); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9846, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9846]; `tensor/DDL_lfc|DDL_z.npy` [9846]; `embed/gene_vectors.npy` [9846]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9846 or target_col == 9846). Every well: [[DCXR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCXR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
