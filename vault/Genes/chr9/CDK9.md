---
symbol: "CDK9"
type: "gene"
col: 5904
ensembl_id: "ENSG00000136807"
name: "cyclin dependent kinase 9"
location: "9q34.11"
module: 127
arm: "+"
pooled_cpm: 10.93
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# CDK9

*cyclin dependent kinase 9* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.55× (z +6.5, q 4e-08, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.717× (z -5.0, q 3e-04, down in 25 of 45 measured lines) ⚠ cell-cycle shift, explains ~89% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.700× (z -3.6, q 0.032, down in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.283×, NCI-H23 0.239×; ⚠ cell-cycle shift, explains ~89% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.0533×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.335×; ⚠ cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0745×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW 900 0.0946×); [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM in 1 line (C32 0.0587×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCNX3]] (+0.76, fdr 7e-06), [[NOP9]] (+0.69, fdr 7e-06), [[RPSA]] (+0.67, fdr 7e-06); moves opposite to [[LRCH3]] (-0.63, fdr 1e-05), [[NDUFC1]] (-0.61, fdr 1e-05), [[ZC3H6]] (-0.60, fdr 7e-06).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5904.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.55×** | +6.5 | 4e-08 | 37/47 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +5.1 | 1e-04 | 20/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.60×** | +4.9 | 1e-04 | 23/43 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +4.5 | 8e-04 | 20/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.009 | 15/47 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.35× | +3.2 | 0.14 | 11/47 (LS 180, A498, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.82× | +3.1 | 0.16 | 7/46 (A498, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5904.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.283×, NCI-H23 0.239×; ⚠ cell-cycle shift, explains ~89% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.0533×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.335×; ⚠ cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0745×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW 900 0.0946×); [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM in 1 line (C32 0.0587×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.717×** | -5.0 | 3e-04 | 25/45 (RKO, NCI-H23, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.623×** | -4.8 | 4e-04 | 23/46 (AsPC-1, A-172, …) | rises with dose | composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -3.9 | 0.018 | 12/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.698×** | -3.8 | 0.018 | 23/46 (BT-474, H4, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -3.6 | 0.032 | 20/47 (A-427, SW48, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.723×** | -3.3 | 0.090 | 15/47 (A-427, LS 180, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.664× | -3.1 | 0.15 | 15/43 (AsPC-1, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5904. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0533× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[C32 (line)]] | wt | 5.68 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM 0.0587× (z -9.3) |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.05 µM 0.114× (z -8.7) |
| [[HS-578T (line)]] | alt | 9.16 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0745× (z -10.2) |
| [[KATO III (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.8) ⚠ cell-cycle shift, explains ~89% of this change |
| [[RKO (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -10.3) ⚠ cell-cycle shift, explains ~89% of this change |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0976× (z -8.8) |
| [[SW 900 (line)]] | alt | 9.43 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0946× (z -9.7) |
| [[A-172 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5904), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX3]] | +0.76 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[NOP9]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[RPSA]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[NORAD]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[BAG5]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ABHD17A]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[IKBKG]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ZSCAN22]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[MORC2]] | +0.64 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[SNRNP200]] | +0.63 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[BAP1]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[DCTN1]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRCH3]] | -0.63 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[NDUFC1]] | -0.61 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[ZC3H6]] | -0.60 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[LRRC37A2]] | -0.59 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ANKRD26]] | -0.59 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[EIF1B]] | -0.58 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[ZNF638]] | -0.57 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[CROCCP2-1]] | -0.57 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[OFD1]] | -0.55 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[NBPF19]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[ZMYM5]] | -0.54 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[ANKRD12]] | -0.54 | -0.46 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.3, -27.1); signed map (-14.0, -31.0). **Vector** length 74.3, 13.4% of its response variance represented; |z| ≥ 3 in 772 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +1.6 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +1.5 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -5.4 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -4.7 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -3.5 | -3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.8 | -1.3 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -3.1 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:127,785,679-127,790,792 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PITALRE, C-2k, TAK; previously CDC2L4 |
| Gene groups (HGNC) | Cyclin dependent kinases; P-TEFb complex subunits |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 31 pathways, smallest: Pausing and recovery of Tat-mediated HIV elongation; Tat-mediated HIV elongation arrest and recovery; HIV elongation arrest and recovery |
| Matched by | ensembl_id |

**Function**, from UniProt [P50750](https://www.uniprot.org/uniprotkb/P50750) (Cyclin-dependent kinase 9):

> Protein kinase involved in the regulation of transcription. Member of the cyclin-dependent kinase pair (CDK9/cyclin-T) complex, also called positive transcription elongation factor b (P-TEFb), which facilitates the transition from abortive to productive elongation by phosphorylating the CTD (C-terminal domain) of the large subunit of RNA polymerase II (RNAP II) POLR2A, SUPT5H and RDBP. This complex is inactive when in the 7SK snRNP complex form. Phosphorylates EP300, MYOD1, RPB1/POLR2A and AR …

**Summary**, from NCBI Gene [1025](https://www.ncbi.nlm.nih.gov/gene/1025):

> The protein encoded by this gene is a member of the cyclin-dependent protein kinase (CDK) family. CDK family members are highly similar to the gene products of S. cerevisiae cdc28, and S. pombe cdc2, and known as important cell cycle regulators. This kinase was found to be a component of the multiprotein complex TAK/P-TEFb, which is an elongation factor for RNA polymerase II-directed transcription and functions by phosphorylating the C-terminal domain of the largest subunit of RNA polymerase …

**Accessions** — [HGNC:1780](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1780) · Entrez [1025](https://www.ncbi.nlm.nih.gov/gene/1025) · UniProt [P50750](https://www.uniprot.org/uniprotkb/P50750) · Ensembl [ENSG00000136807](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136807)

## Data

Gene col 5904: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5904); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5904, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5904]; `tensor/DDL_lfc|DDL_z.npy` [5904]; `embed/gene_vectors.npy` [5904]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5904 or target_col == 5904). Every well: [[CDK9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
