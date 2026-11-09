---
symbol: "DAD1"
type: "gene"
col: 4988
ensembl_id: "ENSG00000129562"
name: "defender against cell death 1"
location: "14q11.2"
module: 41
arm: "+"
pooled_cpm: 34.68
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# DAD1

*defender against cell death 1* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.98× (z +8.7, q 1e-15, up in 36 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.60× (z +6.5, q 1e-08, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.743× (z -4.1, q 0.021, down in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 0.307×, SK-MEL-2 0.276×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.216×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPE]] (+0.66, fdr 1e-05), [[PPIB]] (+0.65, fdr 7e-06), [[TMED9]] (+0.61, fdr 2e-05); moves opposite to [[ZNF362]] (-0.56, fdr 3e-05), [[HNRNPU]] (-0.55, fdr 9e-05), [[TMCO4]] (-0.55, fdr 5e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4988.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.98×** | +8.7 | 1e-15 | 36/45 (A549, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.63×** | +6.5 | 1e-08 | 30/37 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +6.5 | 1e-08 | 42/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +6.0 | 3e-07 | 34/48 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +5.6 | 2e-06 | 34/48 (SW480, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.45×** | +5.1 | 3e-05 | 24/47 (LS 180, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.40×** | +4.7 | 2e-04 | 27/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.43×** | +4.6 | 3e-04 | 23/39 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.5 | 5e-04 | 1/48 (AsPC-1) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.38×** | +4.4 | 5e-04 | 24/47 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.28×** | +3.4 | 0.028 | 20/48 (NCI-H1573, A-427, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.28×** | +3.4 | 0.028 | 21/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.30×** | +3.3 | 0.040 | 17/48 (NCI-H2030, NCI-H1573, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.066 | 17/48 (HT-29, NCI-H23, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.17× | +3.0 | 0.096 | 13/48 (NCI-H460, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4988.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 0.307×, SK-MEL-2 0.276×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.216×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.743×** | -4.1 | 0.021 | 24/48 (CFPAC-1, H4, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.841× | -3.4 | 0.17 | 18/48 (hTERT-HPNE, Panc 03.27, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.3 | 0.17 | 25/48 (SNU-1, LoVo, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.775× | -3.2 | 0.17 | 17/48 (NCI-H23, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4988. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 46.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A549 (line)]] | wt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4988), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPE]] | +0.66 | +0.56 / +0.59 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[PPIB]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[TMED9]] | +0.61 | +0.61 / +0.47 | both halves | 2e-05 | pathway: Asparagine N-linked glycosylation |
| [[PIBF1]] | +0.60 | +0.67 / +0.33 | both halves | 1e-04 |  |
| [[INIP]] | +0.59 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[KLHL28]] | +0.59 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[MAP3K13]] | +0.58 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SEC22A]] | +0.58 | +0.57 / +0.45 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[ZMYM6]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[COG3]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[RRAS]] | +0.57 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[RARS1]] | +0.57 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF362]] | -0.56 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[HNRNPU]] | -0.55 | -0.58 / -0.36 | both halves | 9e-05 |  |
| [[TMCO4]] | -0.55 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[SRC]] | -0.53 | -0.48 / -0.36 | both halves | 9e-05 | pathway: Adherens junctions interactions |
| [[UBTF]] | -0.53 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[ILF3]] | -0.52 | -0.52 / -0.40 | both halves | 5e-05 | pathway: Adherens junctions interactions |
| [[SMG1-DT]] | -0.51 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[POU6F1]] | -0.50 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[SFMBT1]] | -0.50 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[ECPAS]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[LRRK1]] | -0.50 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[PRRC2B]] | -0.50 | -0.53 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (7.3, -34.8); signed map (-54.2, 9.3). **Vector** length 87.3, 20.6% of its response variance represented; |z| ≥ 3 in 678 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +6.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +5.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +6.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.3 | +4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +1.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.7 | -4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -2.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | -2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | -2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.9 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | defender against cell death 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:22,564,907-22,589,224 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OST2 |
| Gene groups (HGNC) | Oligosaccharyltransferase complex subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 26 pathways, smallest: PD-L1(CD274) glycosylation and translocation to plasma membrane; Regulation of CDH1 posttranslational processing and trafficking to plasma membrane; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [P61803](https://www.uniprot.org/uniprotkb/P61803) (Dolichyl-diphosphooligosaccharide--protein glycosyltransferase subunit DAD1):

> Subunit of the oligosaccharyl transferase (OST) complex that catalyzes the initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2) in eukaryotes) from the lipid carrier dolichol-pyrophosphate to an asparagine residue within an Asn-Xaa-Ser/Thr consensus motif in nascent polypeptide chains, the first step in protein N-glycosylation. N-glycosylation occurs cotranslationally and the complex associates with the Sec61 complex at the channel-forming translocon complex that mediates protein …

**Summary**, from NCBI Gene [1603](https://www.ncbi.nlm.nih.gov/gene/1603):

> DAD1, the defender against apoptotic cell death, was initially identified as a negative regulator of programmed cell death in the temperature sensitive tsBN7 cell line. The DAD1 protein disappeared in temperature-sensitive cells following a shift to the nonpermissive temperature, suggesting that loss of the DAD1 protein triggered apoptosis. DAD1 is believed to be a tightly associated subunit of oligosaccharyltransferase both in the intact membrane and in the purified enzyme, thus reflecting the …

**Accessions** — [HGNC:2664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2664) · Entrez [1603](https://www.ncbi.nlm.nih.gov/gene/1603) · UniProt [P61803](https://www.uniprot.org/uniprotkb/P61803) · Ensembl [ENSG00000129562](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129562)

## Data

Gene col 4988: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4988); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4988, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4988]; `tensor/DDL_lfc|DDL_z.npy` [4988]; `embed/gene_vectors.npy` [4988]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4988 or target_col == 4988). Every well: [[DAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
