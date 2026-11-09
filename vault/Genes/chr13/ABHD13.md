---
symbol: "ABHD13"
type: "gene"
col: 6347
ensembl_id: "ENSG00000139826"
name: "abhydrolase domain containing 13"
location: "13q33.3"
module: 1
arm: "+"
pooled_cpm: 17.13
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ABHD13

*abhydrolase domain containing 13* — 13q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.38× (z +6.7, q 1e-08, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.690× (z -3.8, q 0.068, down in 17 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 0.205×, NCI-H1573 0.214×, SHP-77 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.268×, SW480 0.431×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.109×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (AsPC-1 0.0719×); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.111×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCUN1D1]] (+0.60, fdr 1e-05), [[POMK]] (+0.59, fdr 3e-05), [[NDUFAF5]] (+0.59, fdr 1e-05); moves opposite to [[UBAP2]] (-0.59, fdr 2e-05), [[FAM53C]] (-0.58, fdr 1e-05), [[RABGEF1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6347.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +6.7 | 1e-08 | 26/48 (Panc 03.27, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.9 | 2e-04 | 23/47 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +4.7 | 4e-04 | 17/46 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.6 | 7e-04 | 20/42 (Panc 03.27, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 8e-04 | 22/47 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 0.001 | 16/47 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 0.002 | 14/47 (A-172, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.003 | 22/47 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.005 | 16/47 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.010 | 15/47 (NCI-H2030, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.010 | 11/48 (HT-29, LOX-IMVI, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.022 | 16/48 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.034 | 9/47 (A-172, RKO, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.3 | 0.044 | 8/48 (SW480, Hs 766T, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.048 | 15/46 (A-172, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.084 | 11/47 (NCI-H2347, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6347.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 0.205×, NCI-H1573 0.214×, SHP-77 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.268×, SW480 0.431×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.109×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (AsPC-1 0.0719×); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.111×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.690×** | -3.8 | 0.068 | 17/45 (COLO 205, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | 0.782× | -3.6 | 0.10 | 18/39 (NCI-H1573, SW480, …) | two highest doses | composition shift |
| [[Thymol (drug)]] 0.5 µM |  | 0.797× | -3.3 | 0.19 | 14/45 (HCT15, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6347. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 9.39 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0719× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 37.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[SW480 (line)]] | alt | 29.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[HCT15 (line)]] | alt | 21.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.111× (z -11.0) |
| [[HS-578T (line)]] | alt | 9.24 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.138× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.123× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.109× (z -11.3) |
| [[SHP-77 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[A-172 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6347), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCUN1D1]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[POMK]] | +0.59 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[NDUFAF5]] | +0.59 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[RBM45]] | +0.58 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[C5orf63]] | +0.57 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[DHFR2]] | +0.57 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[PYURF]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[PROSER1]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[VPS72]] | +0.56 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[MTPAP]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[DTWD1]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[MSL2]] | +0.55 | +0.46 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBAP2]] | -0.59 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[FAM53C]] | -0.58 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[RABGEF1]] | -0.56 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[FOSB]] | -0.54 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[DHDH]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[LRRC23]] | -0.53 | -0.43 / -0.57 | both halves | 4e-05 |  |
| [[RRP12]] | -0.53 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[TUBB3]] | -0.53 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[GTF2B]] | -0.52 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[BZW2]] | -0.51 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[DALRD3]] | -0.51 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[TINCR]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.403). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.2, 0.9); signed map (-5.1, -34.5). **Vector** length 62.1, 9.28% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.4 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.6 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.6 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -0.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.3 — chr13:108,218,392-108,234,243 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA153I24.2, FLJ14906, BEM46L1; previously C13orf6 |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Matched by | ensembl_id |

UniProt [Q7L211](https://www.uniprot.org/uniprotkb/Q7L211) carries no function annotation.

**Summary**, from NCBI Gene [84945](https://www.ncbi.nlm.nih.gov/gene/84945):

> Predicted to enable palmitoyl-(protein) hydrolase activity. Predicted to be involved in protein depalmitoylation. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20293](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20293) · Entrez [84945](https://www.ncbi.nlm.nih.gov/gene/84945) · UniProt [Q7L211](https://www.uniprot.org/uniprotkb/Q7L211) · Ensembl [ENSG00000139826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139826)

## Data

Gene col 6347: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6347); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6347, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6347]; `tensor/DDL_lfc|DDL_z.npy` [6347]; `embed/gene_vectors.npy` [6347]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6347 or target_col == 6347). Every well: [[ABHD13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
