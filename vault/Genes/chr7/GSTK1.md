---
symbol: "GSTK1"
type: "gene"
col: 12399
ensembl_id: "ENSG00000197448"
name: "glutathione S-transferase kappa 1"
location: "7q34"
module: 29
arm: "+"
pooled_cpm: 20.84
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# GSTK1

*glutathione S-transferase kappa 1* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.48× (z +14.7, q 0e+00, up in 38 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.48× (z +6.6, q 7e-09, up in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (HEC-1-A 5.40×, A498 3.78×, CFPAC-1 5.17×, PANC-1 3.98×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.27×, LS 180 3.64×, LoVo 3.55×, NCI-H460 4.33×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.480× (z -12.2, q 1e-31, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPAN6]] (+0.69, fdr 7e-06), [[PLBD1]] (+0.62, fdr 1e-05), [[CTSH]] (+0.59, fdr 1e-05); moves opposite to [[FBXL18]] (-0.57, fdr 3e-05), [[UCKL1-AS1]] (-0.54, fdr 3e-05), [[LINC02804]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12399.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (HEC-1-A 5.40×, A498 3.78×, CFPAC-1 5.17×, PANC-1 3.98×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.27×, LS 180 3.64×, LoVo 3.55×, NCI-H460 4.33×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.48×** | +14.7 | 0e+00 | 38/39 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.22×** | +13.3 | 6e-38 | 28/30 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +8.4 | 8e-15 | 31/34 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +6.6 | 7e-09 | 32/48 (A-427, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.7 | 0.027 | 23/43 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.029 | 16/45 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12399.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.480×** | -12.2 | 1e-31 | 40/47 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.554×** | -7.0 | 9e-10 | 32/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.635×** | -5.3 | 2e-05 | 26/47 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.652×** | -5.0 | 7e-05 | 26/46 (NCI-H2030, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.689×** | -4.4 | 0.001 | 24/48 (SW480, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.484×** | -4.0 | 0.006 | 20/44 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.712×** | -3.8 | 0.013 | 21/47 (SK-MEL-2, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.758× | -3.1 | 0.15 | 16/47 (C32, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 39.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -9.6) |
| [[LoVo (line)]] | wt | 31.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.6) |
| [[PANC-1 (line)]] | alt | 16.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.27× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.4) |
| [[LS 180 (line)]] | wt | 49.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 16.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -8.6) |
| [[A-427 (line)]] | wt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -9.7) |
| [[A549 (line)]] | wt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +8.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 42.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 16.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +11.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 22.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -8.5) |
| [[HT-29 (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +8.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 11.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +9.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 43.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -16.9) |
| [[RKO (line)]] | wt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -19.7) |
| [[RPMI-7951 (line)]] | alt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -13.5) |
| [[SNU-1 (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0969× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 32.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -9.9) |
| [[A-172 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN6]] | +0.69 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[PLBD1]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CTSH]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SH3BGRL]] | +0.58 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[FAM210B]] | +0.58 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[ATRAID]] | +0.58 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[CIAO2A]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[PON2]] | +0.55 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[ITM2B]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[PYURF]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[SCARB2]] | +0.54 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[SPATA20]] | +0.54 | +0.46 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL18]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[UCKL1-AS1]] | -0.54 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[LINC02804]] | -0.53 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[CHRNA10]] | -0.51 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[CFAP251]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[CRK]] | -0.50 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[PRKAG1]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[FAM131A]] | -0.49 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[SPATA32]] | -0.48 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[SETX]] | -0.48 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ZKSCAN5]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TRIOBP]] | -0.47 | -0.54 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.5, -19.7); signed map (-21.2, -40.1). **Vector** length 60.9, 11.7% of its response variance represented; |z| ≥ 3 in 711 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.5 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +14.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +8.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | glutathione S-transferase kappa 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:143,244,093-143,270,854 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GST13 |
| Gene groups (HGNC) | Soluble glutathione S-transferases |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME |
| Reactome | 5 pathways, smallest: Glutathione conjugation; Peroxisomal protein import; Phase II - Conjugation of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2Q3](https://www.uniprot.org/uniprotkb/Q9Y2Q3) (Glutathione S-transferase kappa 1):

> Glutathione S-transferase that catalyzes the conjugation of glutathione to exogenous and endogenous compounds. Significant glutathione conjugating activity is found only with the model substrate, 1-chloro-2,4-dinitrobenzene (CDNB).

**Summary**, from NCBI Gene [373156](https://www.ncbi.nlm.nih.gov/gene/373156):

> This gene encodes a member of the kappa class of the glutathione transferase superfamily of enzymes that function in cellular detoxification. The encoded protein is localized to the peroxisome and catalyzes the conjugation of glutathione to a wide range of hydrophobic substates facilitating the removal of these compounds from cells. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:16906](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16906) · Entrez [373156](https://www.ncbi.nlm.nih.gov/gene/373156) · UniProt [Q9Y2Q3](https://www.uniprot.org/uniprotkb/Q9Y2Q3) · Ensembl [ENSG00000197448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197448)

## Data

Gene col 12399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12399); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12399]; `tensor/DDL_lfc|DDL_z.npy` [12399]; `embed/gene_vectors.npy` [12399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12399 or target_col == 12399). Every well: [[GSTK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSTK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
