---
symbol: "SPATA2"
type: "gene"
col: 8167
ensembl_id: "ENSG00000158480"
name: "spermatogenesis associated 2"
location: "20q13.13"
module: 7
arm: "+"
pooled_cpm: 8.04
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SPATA2

*spermatogenesis associated 2* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.17× (z +12.0, q 3e-30, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.709× (z -4.0, q 0.031, down in 18 of 32 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW1417 0.126×, NCI-H2030 0.105×, SW 900 0.118×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.0972×; ⚠ toxic; transcription drop); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM in 1 line (C32 0.0520×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (COLO 205 0.110×); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0897×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF384]] (+0.60, fdr 1e-05), [[MAPK7]] (+0.59, fdr 1e-05), [[WDR24]] (+0.58, fdr 1e-05); moves opposite to [[ROCK1]] (-0.54, fdr 4e-05), [[KTN1]] (-0.50, fdr 1e-04), [[SEPTIN7]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8167.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.17×** | +12.0 | 3e-30 | 40/44 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +11.5 | 3e-28 | 32/41 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.20×** | +8.7 | 6e-16 | 31/40 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +7.8 | 9e-13 | 31/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.86×** | +7.2 | 9e-11 | 34/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +6.8 | 1e-09 | 27/45 (BT-474, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.4 | 2e-08 | 25/42 (MIA PaCa-2, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +6.2 | 4e-08 | 27/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +5.8 | 4e-07 | 20/38 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.57×** | +5.2 | 1e-05 | 18/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +5.1 | 2e-05 | 22/43 (Hs 766T, LS 180, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.54×** | +5.0 | 3e-05 | 20/47 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.56×** | +4.9 | 4e-05 | 16/35 (NCI-H2030, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +4.5 | 3e-04 | 19/46 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +4.3 | 8e-04 | 16/47 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +4.1 | 0.002 | 18/46 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.086 | 3/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8167.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW1417 0.126×, NCI-H2030 0.105×, SW 900 0.118×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.0972×; ⚠ toxic; transcription drop); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM in 1 line (C32 0.0520×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (COLO 205 0.110×); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0897×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.709×** | -4.0 | 0.031 | 18/32 (SW1417, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.760× | -3.1 | 0.50 | 11/15 (SW1417, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Lapatinib ditosylate (drug)]] 0.05 µM |  | 0.763× | -3.0 | 0.50 | 8/45 (SW48, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8167. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 19.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0972× (z -14.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.148× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 5.45 | 0 | 1 | — | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM 0.0520× (z -10.4) |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.110× (z -9.4) |
| [[Hs 766T (line)]] | wt | 12.1 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.168× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 5.07 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0897× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 7.79 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -10.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 5.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.287× (z -8.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW 900 (line)]] | alt | 8.46 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8167), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF384]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[MAPK7]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[WDR24]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ZNF256]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ZNF408]] | +0.57 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[ZNF17]] | +0.56 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[C19orf47]] | +0.56 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[ANAPC2]] | +0.56 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[MBD1]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[SLC25A44]] | +0.55 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[OTUB1]] | +0.55 | +0.69 / +0.35 | both halves | 1e-04 |  |
| [[XAB2]] | +0.55 | +0.57 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROCK1]] | -0.54 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[KTN1]] | -0.50 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[SEPTIN7]] | -0.49 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[SSB]] | -0.48 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[SMC3]] | -0.47 | -0.25 / -0.50 | both halves | 4e-04 |  |
| [[TUT4]] | -0.46 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[CHD1]] | -0.46 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ITSN1]] | -0.45 | -0.37 / -0.44 | both halves | 8e-05 | pathway: Death Receptor Signaling |
| [[SMC6]] | -0.45 | -0.35 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.382). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-35.2, -3.6); signed map (-11.3, -24.8). **Vector** length 51.3, 6.68% of its response variance represented; |z| ≥ 3 in 945 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +12.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +3.0 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +6.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.5 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +8.7 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.1 | +0.2 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.1 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -2.9 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | +0.5 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.1 | -2.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.0 | +0.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:49,903,391-49,915,529 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0757, PD1, tamo, PPP1R145 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Reactome | 5 pathways, smallest: TNFR1-induced proapoptotic signaling; TNFR1-induced NF-kappa-B signaling pathway; Regulation of TNFR1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UM82](https://www.uniprot.org/uniprotkb/Q9UM82) (Spermatogenesis-associated protein 2):

> Bridging factor that mediates the recruitment of CYLD to the LUBAC complex, thereby regulating TNF-induced necroptosis. Acts as a direct binding intermediate that bridges RNF31/HOIP, the catalytic subunit of the LUBAC complex, and the deubiquitinase (CYLD), thereby recruiting CYLD to the TNF-R1 signaling complex (TNF-RSC). Required to activate the 'Met-1'- (linear) and 'Lys-63'-linked deubiquitinase activities of CYLD. Controls the kinase activity of RIPK1 and TNF-induced necroptosis by …

**Summary**, from NCBI Gene [9825](https://www.ncbi.nlm.nih.gov/gene/9825):

> Enables signaling receptor complex adaptor activity and ubiquitin-specific protease binding activity. Involved in several processes, including protein deubiquitination; regulation of necroptotic process; and regulation of tumor necrosis factor-mediated signaling pathway. Located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14681](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14681) · Entrez [9825](https://www.ncbi.nlm.nih.gov/gene/9825) · UniProt [Q9UM82](https://www.uniprot.org/uniprotkb/Q9UM82) · Ensembl [ENSG00000158480](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158480)

## Data

Gene col 8167: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8167); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8167, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8167]; `tensor/DDL_lfc|DDL_z.npy` [8167]; `embed/gene_vectors.npy` [8167]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8167 or target_col == 8167). Every well: [[SPATA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
