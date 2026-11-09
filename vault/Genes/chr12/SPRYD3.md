---
symbol: "SPRYD3"
type: "gene"
col: 9540
ensembl_id: "ENSG00000167778"
name: "SPRY domain containing 3"
location: "12q13.13"
module: 2
arm: "+"
pooled_cpm: 16.52
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SPRYD3

*SPRY domain containing 3* — 12q13.13

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.328× (z -25.2, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PREB]] (+0.66, fdr 1e-05), [[ARFGAP1]] (+0.64, fdr 1e-05), [[TPD52L2]] (+0.63, fdr 5e-05); moves opposite to [[RHOBTB3]] (-0.56, fdr 3e-05), [[CDKN2B-AS1]] (-0.56, fdr 7e-05), [[TGIF2]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9540.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.17 | 11/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.23× | +3.3 | 0.17 | 14/48 (SW480, A498, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.23× | +3.3 | 0.17 | 13/44 (RPMI-7951, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | 1.33× | +3.2 | 0.17 | 9/45 (HS-578T, LoVo, …) | rises with dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.22× | +3.1 | 0.20 | 9/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.24× | +3.0 | 0.24 | 11/47 (A498, NCI-H1792, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9540.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.328×** | -25.2 | 0e+00 | 44/47 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.562×** | -8.9 | 2e-16 | 29/47 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.602×** | -8.1 | 8e-14 | 30/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.614×** | -7.8 | 1e-12 | 26/46 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.633×** | -6.4 | 1e-08 | 22/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.486×** | -6.0 | 1e-07 | 24/48 (KATO III, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.739×** | -4.8 | 1e-04 | 19/47 (SNU-1, H4, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.783×** | -3.9 | 0.007 | 21/47 (HOP62, A-172, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.778×** | -3.8 | 0.009 | 16/47 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.792×** | -3.6 | 0.018 | 16/42 (SNU-1, A-172, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.804×** | -3.5 | 0.025 | 15/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.814×** | -3.3 | 0.047 | 22/47 (SW 900, LS 180, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -3.2 | 0.053 | 17/46 (SW48, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.817×** | -3.1 | 0.074 | 13/42 (NCI-H2347, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9540. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -19.9) |
| [[A-172 (line)]] | wt | 22.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -15.1) |
| [[LoVo (line)]] | wt | 19.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -11.2) |
| [[A549 (line)]] | wt | 18.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 34.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -13.6) |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -16.0) |
| [[J82 (line)]] | alt | 20.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -21.0) |
| [[NCI-H1573 (line)]] | alt | 14.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -14.0) |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -21.6) |
| [[PANC-1 (line)]] | alt | 14.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -18.5) |
| [[RKO (line)]] | wt | 36.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -16.0) |
| [[SW 900 (line)]] | alt | 15.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -8.7) |
| [[H4 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 29.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -16.7) |
| [[HS-578T (line)]] | alt | 29.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -15.4) |
| [[HT-29 (line)]] | alt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.1) |
| [[KATO III (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -12.2) |
| [[LS 180 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -9.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 9.96 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -12.5) |
| [[SW48 (line)]] | wt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -11.1) |
| [[A-427 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9540), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PREB]] | +0.66 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ARFGAP1]] | +0.64 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[TPD52L2]] | +0.63 | +0.74 / +0.39 | both halves | 5e-05 |  |
| [[YKT6]] | +0.63 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[ZNF598]] | +0.62 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.62 | +0.66 / +0.36 | both halves | 9e-05 |  |
| [[RNF216P1]] | +0.61 | +0.69 / +0.31 | both halves | 2e-04 |  |
| [[SLC39A13]] | +0.61 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ABCC10]] | +0.61 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[ELOVL1]] | +0.60 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[LDLRAP1]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[SEMA4F]] | +0.59 | +0.48 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOBTB3]] | -0.56 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CDKN2B-AS1]] | -0.56 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[TGIF2]] | -0.54 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[CAMK2D]] | -0.53 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[KANSL1L]] | -0.52 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[ANGPT2]] | -0.52 | -0.54 / -0.28 | both halves | 3e-04 |  |
| [[DRAIC]] | -0.52 | -0.56 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[LINC00869-1]] | -0.52 | -0.56 / -0.25 | both halves | 4e-04 |  |
| [[BAZ2B]] | -0.52 | -0.56 / -0.24 | both halves | 5e-04 |  |
| [[ZBTB2]] | -0.52 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[GTF2H1]] | -0.52 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[ATF7IP]] | -0.51 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[CLEC2D]] | -0.50 | -0.52 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (8.4, -29.5); signed map (-49.2, 2.8). **Vector** length 85.6, 16.6% of its response variance represented; |z| ≥ 3 in 816 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +2.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +3.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.4 | +3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.0 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.9 | -25.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -8.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -6.0 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.9 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SPRY domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,064,316-53,079,404 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14800 |
| Matched by | ensembl_id |

UniProt [Q8NCJ5](https://www.uniprot.org/uniprotkb/Q8NCJ5) carries no function annotation.

**Summary**, from NCBI Gene [84926](https://www.ncbi.nlm.nih.gov/gene/84926):

> Predicted to enable protein-macromolecule adaptor activity. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25920) · Entrez [84926](https://www.ncbi.nlm.nih.gov/gene/84926) · UniProt [Q8NCJ5](https://www.uniprot.org/uniprotkb/Q8NCJ5) · Ensembl [ENSG00000167778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167778)

## Data

Gene col 9540: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9540); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9540, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9540]; `tensor/DDL_lfc|DDL_z.npy` [9540]; `embed/gene_vectors.npy` [9540]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9540 or target_col == 9540). Every well: [[SPRYD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPRYD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
