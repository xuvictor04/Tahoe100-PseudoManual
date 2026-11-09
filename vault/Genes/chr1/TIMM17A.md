---
symbol: "TIMM17A"
type: "gene"
col: 5557
ensembl_id: "ENSG00000134375"
name: "translocase of inner mitochondrial membrane 17A"
location: "1q32.1"
module: 49
arm: "+"
pooled_cpm: 47.91
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# TIMM17A

*translocase of inner mitochondrial membrane 17A* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.17× (z +13.7, q 5e-40, up in 48 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.303×, SW1417 0.385×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 0.530×, SNU-1 0.371×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.194×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GORASP2]] (+0.71, fdr 7e-06), [[PREB]] (+0.65, fdr 1e-05), [[RARS1]] (+0.65, fdr 1e-05); moves opposite to [[NAP1L1]] (-0.51, fdr 3e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5557.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.17×** | +13.7 | 5e-40 | 48/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.56×** | +12.2 | 1e-31 | 39/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.93×** | +12.1 | 3e-31 | 45/48 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.84×** | +11.2 | 7e-27 | 44/48 (SW480, HOP62, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.80×** | +10.8 | 3e-25 | 45/48 (SW480, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +9.6 | 6e-20 | 41/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +9.0 | 2e-17 | 37/48 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.9 | 4e-10 | 32/46 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +6.7 | 1e-09 | 31/48 (NCI-H460, C32, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +6.3 | 2e-08 | 37/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.37×** | +5.8 | 4e-07 | 26/46 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +5.6 | 1e-06 | 27/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +5.2 | 1e-05 | 24/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +5.0 | 3e-05 | 19/35 (LOX-IMVI, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.64×** | +4.7 | 9e-05 | 28/48 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.63×** | +4.7 | 1e-04 | 25/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.58×** | +4.4 | 3e-04 | 18/48 (NCI-H460, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 7e-04 | 21/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.002 | 25/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.004 | 19/47 (NCI-H460, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.005 | 19/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5557.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.303×, SW1417 0.385×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 0.530×, SNU-1 0.371×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.194×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | 0.886× | -3.2 | 0.56 | 10/48 (SNU-1, AsPC-1, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.847× | -3.1 | 0.56 | 16/48 (NCI-H2347, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5557. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 40.4 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.62× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 36.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.83× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 69.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 46.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.1) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.89× (z +9.9) | — |
| [[A549 (line)]] | wt | 35.5 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.77× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 44.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 66.2 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 8.21× (z +8.7) | — |
| [[LoVo (line)]] | wt | 53.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 44.6 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.43× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 55.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.31× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 49.5 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.57× (z +9.5) | — |
| [[A-172 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 80.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5557), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GORASP2]] | +0.71 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PREB]] | +0.65 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[RARS1]] | +0.65 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[YRDC]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[POLR3A]] | +0.63 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[NUS1]] | +0.63 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[SRPRB]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 | pathway: Protein localization |
| [[TIMM23]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 | same gene group; pathway: Mitochondrial protein import; STRING 999 |
| [[SSR2]] | +0.61 | +0.59 / +0.46 | both halves | 3e-05 | pathway: Protein localization |
| [[DERL2]] | +0.60 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[TMEM161B]] | +0.60 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SEC13]] | +0.60 | +0.51 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAP1L1]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.0, -30.4); signed map (-55.4, 11.3). **Vector** length 90.9, 23.2% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +9.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +12.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.5 | +11.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +12.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +4.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +4.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -3.5 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -2.9 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -1.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Tofacitinib (drug)]] 0.05 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane 17A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:201,955,503-201,970,664 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIM17, TIM17A |
| Gene groups (HGNC) | TIM23 complex; Tim17 family |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Mitochondrial protein import; Mitochondrial protein degradation; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99595](https://www.uniprot.org/uniprotkb/Q99595) (Mitochondrial import inner membrane translocase subunit Tim17-A):

> Essential component of the TIM23 complex, a complex that mediates the translocation of transit peptide-containing proteins across the mitochondrial inner membrane.

**Summary**, from NCBI Gene [10440](https://www.ncbi.nlm.nih.gov/gene/10440):

> Predicted to contribute to transmembrane protein transporter activity. Predicted to be involved in protein import into mitochondrial matrix. Located in mitochondrial inner membrane. Part of TIM23 mitochondrial import inner membrane translocase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17315](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17315) · Entrez [10440](https://www.ncbi.nlm.nih.gov/gene/10440) · UniProt [Q99595](https://www.uniprot.org/uniprotkb/Q99595) · Ensembl [ENSG00000134375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134375)

## Data

Gene col 5557: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5557); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5557, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5557]; `tensor/DDL_lfc|DDL_z.npy` [5557]; `embed/gene_vectors.npy` [5557]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5557 or target_col == 5557). Every well: [[TIMM17A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM17A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
