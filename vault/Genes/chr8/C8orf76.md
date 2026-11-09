---
symbol: "C8orf76"
type: "gene"
col: 12122
ensembl_id: "ENSG00000189376"
name: "chromosome 8 open reading frame 76"
location: "8q24.13"
module: 15
arm: "+"
pooled_cpm: 28.91
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# C8orf76

*chromosome 8 open reading frame 76* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.71× (z +10.8, q 2e-24, up in 32 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +9.6, q 2e-19, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.505× (z -14.2, q 4e-43, down in 37 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (LOX-IMVI 0.0477×, SHP-77 0.131×, NCI-H2030 0.158×, A-172 0.139×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HT-29 0.133×, SNU-423 0.148×, Panc 03.27 0.255×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.237×, LOX-IMVI 0.203×; ⚠ toxic; transcription drop); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (H4 0.161×); [[Gemfibrozil (drug)]] 0.05 µM in 1 line (CHP-212 0.0857×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAHD2A]] (+0.72, fdr 1e-05), [[GPR89A]] (+0.68, fdr 7e-06), [[NDUFAF7]] (+0.68, fdr 7e-06); moves opposite to [[JUNB]] (-0.63, fdr 1e-05), [[FOS]] (-0.62, fdr 1e-05), [[IER2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12122.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +10.8 | 2e-24 | 32/44 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +9.6 | 2e-19 | 30/47 (PANC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +6.5 | 2e-08 | 27/47 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +6.2 | 7e-08 | 25/48 (HEC-1-A, Hs 766T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +5.2 | 2e-05 | 19/46 (HOP62, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.29×** | +5.0 | 5e-05 | 22/48 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.25×** | +4.8 | 2e-04 | 21/47 (KATO III, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.25×** | +4.7 | 2e-04 | 21/48 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +4.4 | 8e-04 | 16/47 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.16× | +4.3 | 9e-04 | 17/48 (NCI-H1573, HT-29, …) | top dose only | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.003 | 16/47 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.021 | 18/48 (SW480, PANC-1, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12122.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (LOX-IMVI 0.0477×, SHP-77 0.131×, NCI-H2030 0.158×, A-172 0.139×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HT-29 0.133×, SNU-423 0.148×, Panc 03.27 0.255×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.237×, LOX-IMVI 0.203×; ⚠ toxic; transcription drop); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (H4 0.161×); [[Gemfibrozil (drug)]] 0.05 µM in 1 line (CHP-212 0.0857×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.505×** | -14.2 | 4e-43 | 37/43 (HT-29, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.614×** | -9.4 | 2e-18 | 25/39 (NCI-H2347, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.628×** | -9.3 | 2e-18 | 27/37 (LOX-IMVI, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | 0.836× | -5.2 | 2e-05 | 24/47 (AsPC-1, HOP62, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.774×** | -5.1 | 4e-05 | 23/48 (Panc 03.27, HS-578T, …) | rises with dose | composition shift |
| [[Methotrexate (drug)]] 0.5 µM |  | 0.859× | -3.1 | 0.17 | 10/48 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.863× | -3.0 | 0.19 | 5/48 (NCI-H1573, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12122. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 75.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -22.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 38.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0477× (z -25.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 37.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.413× (z -9.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 34.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -10.9) ⚠ cell-cycle shift, explains ~88% of this change |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -13.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 29.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -10.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 64.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -19.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -15.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -10.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.05 µM 0.0857× (z -8.6) |
| [[H4 (line)]] | wt | 22.7 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.161× (z -9.2) |
| [[HOP62 (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -8.8) ⚠ cell-cycle shift, explains ~88% of this change |
| [[Hs 766T (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -9.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0902× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[J82 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0977× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -14.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -11.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0969× (z -14.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -12.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -10.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.26× (z +8.7) ⚠ toxic | — |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12122), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAHD2A]] | +0.72 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[GPR89A]] | +0.68 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[TAF11]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[CCNY-AS1]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[MIR762HG]] | +0.66 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[TRAPPC13]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[PGS1]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CAPN10-DT]] | +0.64 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ZNF250]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 | STRING 407 |
| [[ELMOD3]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[CCT6P3-1]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUNB]] | -0.63 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[FOS]] | -0.62 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[IER2]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[JUN]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[SFR1]] | -0.59 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[EGR1]] | -0.58 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.58 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[NAB1]] | -0.58 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[HES1]] | -0.58 | -0.70 / -0.45 | both halves | 3e-05 |  |
| [[ATP7A]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[FOSB]] | -0.57 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[HNRNPC]] | -0.57 | -0.33 / -0.65 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.3, 21.7); signed map (-44.1, 0.9). **Vector** length 80.4, 14.7% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.7 | +10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +3.2 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.1 | +4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +3.0 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -5.9 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -5.6 | -5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | -14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -0.5 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.8 | -2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Esmolol (hydrochloride) (drug)]] 5 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 8 open reading frame 76 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:123,219,967-123,241,377 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14825 |
| Matched by | ensembl_id |

UniProt [Q96K31](https://www.uniprot.org/uniprotkb/Q96K31) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25924](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25924) · Entrez [84933](https://www.ncbi.nlm.nih.gov/gene/84933) · UniProt [Q96K31](https://www.uniprot.org/uniprotkb/Q96K31) · Ensembl [ENSG00000189376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189376)

## Data

Gene col 12122: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12122); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12122, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12122]; `tensor/DDL_lfc|DDL_z.npy` [12122]; `embed/gene_vectors.npy` [12122]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12122 or target_col == 12122). Every well: [[C8orf76 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C8orf76.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
