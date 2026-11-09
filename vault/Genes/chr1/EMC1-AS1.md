---
symbol: "EMC1-AS1"
type: "gene"
col: 13746
ensembl_id: "ENSG00000230424"
name: "EMC1 antisense RNA 1"
location: "1p36.13"
module: 15
arm: "+"
pooled_cpm: 23.37
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# EMC1-AS1

*EMC1 antisense RNA 1* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.90× (z +19.2, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.673× (z -4.7, q 0.001, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.138×, HCT15 0.177×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.0998×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.180×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H661 0.0969×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM4]] (+0.75, fdr 7e-06), [[POLR2A]] (+0.74, fdr 7e-06), [[KMT2E-AS1]] (+0.68, fdr 1e-05); moves opposite to [[RABGAP1L]] (-0.55, fdr 5e-05), [[COG2]] (-0.53, fdr 5e-05), [[BRD7]] (-0.53, fdr 8e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MIA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13746.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.90×** | +19.2 | 0e+00 | 46/47 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.42×** | +11.2 | 8e-27 | 43/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +9.3 | 3e-18 | 40/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +8.5 | 2e-15 | 36/48 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +8.4 | 3e-15 | 32/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +7.8 | 8e-13 | 37/44 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +5.7 | 1e-06 | 28/46 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +4.9 | 7e-05 | 31/48 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +4.8 | 1e-04 | 22/48 (J82, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +4.7 | 1e-04 | 29/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +4.7 | 2e-04 | 29/47 (A549, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +4.5 | 3e-04 | 23/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.4 | 6e-04 | 22/48 (LoVo, A-427, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +3.7 | 0.008 | 16/48 (A498, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +3.7 | 0.008 | 15/39 (C-33 A, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +3.3 | 0.031 | 15/46 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.032 | 15/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.067 | 10/48 (SK-MEL-2, NCI-H1573, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13746.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.138×, HCT15 0.177×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.0998×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.180×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H661 0.0969×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.673×** | -4.7 | 0.001 | 25/48 (PANC-1, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -4.6 | 0.001 | 19/34 (KATO III, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **0.660×** | -3.8 | 0.029 | 18/47 (SK-MEL-2, SW48, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Flutamide (drug)]] 5 µM |  | 0.770× | -3.3 | 0.12 | 17/48 (A549, SW1417, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.787× | -3.1 | 0.17 | 12/48 (A-172, SW480, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.787× | -3.1 | 0.17 | 11/48 (LoVo, SW48, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.789× | -3.0 | 0.17 | 12/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.789× | -3.0 | 0.17 | 14/48 (NCI-H1573, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13746. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.1 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 15.0 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.63× (z +11.3) | — |
| [[KATO III (line)]] | alt | 22.8 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.84× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -12.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 27.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +12.2) | — |
| [[BT-474 (line)]] | alt | 16.8 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.09× (z +9.9) | [[AZD2858 (drug)]] 0.5 µM 0.0886× (z -8.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 28.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.18× (z +16.4) | — |
| [[PANC-1 (line)]] | alt | 21.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +11.3) | — |
| [[SW480 (line)]] | alt | 23.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +12.6) | — |
| [[A-172 (line)]] | wt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +9.8) | — |
| [[A-427 (line)]] | wt | 28.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -10.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +9.0) | — |
| [[A549 (line)]] | wt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -9.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 28.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +11.5) | — |
| [[HepG2_C3A (line)]] | wt | 41.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.60× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 28.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 30.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 30.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 29.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +10.2) | — |
| [[J82 (line)]] | alt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +11.3) | — |
| [[LoVo (line)]] | wt | 26.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +14.0) | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 48.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 18.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 22.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 17.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 24.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0969× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 14.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +10.4) | — |
| [[RKO (line)]] | wt | 22.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +12.5) | — |
| [[SHP-77 (line)]] | alt | 23.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.38× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 19.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 26.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0998× (z -11.5) |
| [[SW1417 (line)]] | alt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +9.0) | — |
| [[SW48 (line)]] | wt | 29.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13746), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM4]] | +0.75 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[POLR2A]] | +0.74 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[KMT2E-AS1]] | +0.68 | +0.63 / +0.55 | both halves | 1e-05 | same gene group |
| [[ZNF460-AS1]] | +0.66 | +0.57 / +0.49 | both halves | 1e-05 | same gene group |
| [[BORCS7-ASMT]] | +0.65 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ADCY10]] | +0.65 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[RSRP1]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[GNAS]] | +0.64 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[NXF1]] | +0.64 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[C12orf57]] | +0.64 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[CASS4]] | +0.64 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[LINC02680]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGAP1L]] | -0.55 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[COG2]] | -0.53 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[BRD7]] | -0.53 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[MPHOSPH6]] | -0.53 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[FARSB]] | -0.53 | -0.44 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIA]] | B | MIA activity raises EMC1-AS1's level | lines that do not express MIA (10) vs lines expressing it (40) | 1.32× lower at baseline in the lines without MIA | 0.046 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.591). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (28.6, -25.4); signed map (3.4, 14.9). **Vector** length 105, 26.8% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +19.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.0 | +7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.5 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.7 | +3.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.3 | -4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.7 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.7 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.9 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.4 | -2.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | EMC1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p36.13 — chr1:19,210,348-19,240,709 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54050) · Entrez [101927895](https://www.ncbi.nlm.nih.gov/gene/101927895) · Ensembl [ENSG00000230424](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230424)

## Data

Gene col 13746: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13746); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13746, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13746]; `tensor/DDL_lfc|DDL_z.npy` [13746]; `embed/gene_vectors.npy` [13746]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13746 or target_col == 13746). Every well: [[EMC1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMC1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
