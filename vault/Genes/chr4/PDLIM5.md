---
symbol: "PDLIM5"
type: "gene"
col: 8634
ensembl_id: "ENSG00000163110"
name: "PDZ and LIM domain 5"
location: "4q22.3"
module: 111
arm: "+"
pooled_cpm: 396.41
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# PDLIM5

*PDZ and LIM domain 5* — 4q22.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (SNU-1 2.69×, MIA PaCa-2 2.14×, C32 2.38×, RKO 1.70×; ⚠ cell-cycle shift, explains ~26% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A-427 2.74×, RKO 2.70×, SNU-1 3.09×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 2.84×, A-427 2.21×, SNU-1 2.89×); [[Peretinoin (drug)]] 5 µM in 1 line (NCI-H1573 2.95×).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.631× (z -9.9, q 2e-20, down in 34 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VCL]] (+0.63, fdr 1e-05), [[DIAPH1]] (+0.63, fdr 7e-06), [[MYO1E]] (+0.55, fdr 1e-05); moves opposite to [[PMS2CL]] (-0.61, fdr 3e-05), [[ZFP64]] (-0.54, fdr 8e-05), [[TRMU]] (-0.52, fdr 6e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NTN4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8634.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (SNU-1 2.69×, MIA PaCa-2 2.14×, C32 2.38×, RKO 1.70×; ⚠ cell-cycle shift, explains ~26% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A-427 2.74×, RKO 2.70×, SNU-1 3.09×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 2.84×, A-427 2.21×, SNU-1 2.89×); [[Peretinoin (drug)]] 5 µM in 1 line (NCI-H1573 2.95×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.25× | +3.3 | 0.51 | 23/48 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | 1.23× | +3.1 | 0.51 | 25/48 (NCI-H23, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8634.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -9.9 | 2e-20 | 34/49 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.588×** | -7.8 | 2e-12 | 40/47 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.642×** | -6.7 | 3e-09 | 35/48 (HT-29, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.649×** | -6.6 | 7e-09 | 38/48 (SW48, HT-29, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.715×** | -5.1 | 4e-05 | 31/48 (NCI-H23, A-172, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.797×** | -4.9 | 8e-05 | 31/48 (C32, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.801×** | -4.8 | 1e-04 | 27/48 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.732×** | -4.6 | 3e-04 | 24/44 (NCI-H460, NCI-H2347, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.574×** | -4.4 | 6e-04 | 30/49 (LS 180, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.755×** | -4.2 | 0.002 | 29/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.759×** | -4.1 | 0.002 | 30/48 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | 0.842× | -3.7 | 0.009 | 21/48 (A549, J82, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.639×** | -3.6 | 0.016 | 28/45 (A549, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.783×** | -3.4 | 0.024 | 23/48 (A549, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.660×** | -3.3 | 0.035 | 24/48 (RPMI-7951, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.686×** | -3.0 | 0.090 | 21/48 (J82, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8634. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 692 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -15.4) |
| [[NCI-H460 (line)]] | wt | 1,200 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -20.0) |
| [[J82 (line)]] | alt | 384 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -15.1) |
| [[NCI-H1573 (line)]] | alt | 559 | 3 (2 ⚠) | 1 | [[Daptomycin (drug)]] 5 µM 3.24× (z +10.2) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 2.95× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -12.2) |
| [[SNU-1 (line)]] | wt | 113 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +9.6) | — |
| [[A549 (line)]] | wt | 617 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -21.2) |
| [[BT-474 (line)]] | alt | 472 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -11.9) |
| [[HT-29 (line)]] | alt | 613 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 426 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -16.0) |
| [[NCI-H2030 (line)]] | alt | 651 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -12.1) |
| [[RKO (line)]] | wt | 125 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +11.3) | — |
| [[A-427 (line)]] | wt | 119 | 2 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +12.6) | — |
| [[C32 (line)]] | wt | 227 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Radotinib (drug)]] 5 µM 0.484× (z -9.0) |
| [[KATO III (line)]] | alt | 290 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 297 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.409× (z -8.8) |
| [[A-172 (line)]] | wt | 157 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 504 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -8.6) |
| [[C-33 A (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[CFPAC-1 (line)]] | alt | 401 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 613 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -14.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 453 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -9.6) |
| [[LoVo (line)]] | wt | 482 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2347 (line)]] | alt | 471 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.429× (z -9.4) ⚠ toxic |
| [[SW48 (line)]] | wt | 470 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.332× (z -10.6) |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 823 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 216 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 316 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 251 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 314 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 191 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 511 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 508 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 406 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 418 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 355 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 464 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 390 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 285 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8634), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VCL]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 508 |
| [[DIAPH1]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MYO1E]] | +0.55 | +0.52 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ITGB1]] | +0.53 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ACTN4]] | +0.53 | +0.51 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 735 |
| [[STK38L]] | +0.53 | +0.39 / +0.50 | both halves | 6e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ACTR3]] | +0.52 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TPM4]] | +0.51 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[GLS]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 | pathway: Neuronal System |
| [[ITSN1]] | +0.50 | +0.38 / +0.49 | both halves | 6e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[PRKCA]] | +0.50 | +0.40 / +0.48 | both halves | 5e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[LUZP1]] | +0.50 | +0.50 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2CL]] | -0.61 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[ZFP64]] | -0.54 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[TRMU]] | -0.52 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[TMLHE]] | -0.50 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[RBSN]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[POM121C]] | -0.49 | -0.23 / -0.51 | both halves | 5e-04 |  |
| [[PDPR]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[THAP3]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[MORN4]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[MTO1]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[NISCH]] | -0.47 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[TFAP4]] | -0.47 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NTN4]] | B | NTN4 activity raises PDLIM5's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without NTN4 | 0.020 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[PRKCA]] | B | PRKCA activity raises PDLIM5's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 2.44× lower at baseline in the lines without PRKCA | 0.021 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[MYO1E]] | B | MYO1E activity raises PDLIM5's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 2.09× lower at baseline in the lines without MYO1E | 0.063 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[LMO7]] | B | LMO7 activity raises PDLIM5's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 1.83× lower at baseline in the lines without LMO7 | 0.085 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.5, 26.9); signed map (-9.5, 37.2). **Vector** length 135, 45.9% of its response variance represented; |z| ≥ 3 in 1,156 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +3.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.5 | +2.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.1 | +1.4 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | +3.0 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | -0.4 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | +3.0 | +2.1 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -6.7 | -5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.4 | -7.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -6.0 | -6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.2 | -4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.0 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -6.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.1 | -2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -4.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | PDZ and LIM domain 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.3 — chr4:94,451,857-94,668,227 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LIM, Enh |
| Gene groups (HGNC) | LIM domain containing; PDZ domain containing |
| Hallmark sets | ANDROGEN_RESPONSE, UV_RESPONSE_DN, XENOBIOTIC_METABOLISM, TNFA_SIGNALING_VIA_NFKB, MITOTIC_SPINDLE |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HC4](https://www.uniprot.org/uniprotkb/Q96HC4) (PDZ and LIM domain protein 5):

> May play an important role in the heart development by scaffolding PKC to the Z-disk region. May play a role in the regulation of cardiomyocyte expansion. Isoforms lacking the LIM domains may negatively modulate the scaffolding activity of isoform 1. Overexpression promotes the development of heart hypertrophy. Contributes to the regulation of dendritic spine morphogenesis in neurons. May be required to restrain postsynaptic growth of excitatory synapses. Isoform 1, but not isoform 2, …

**Summary**, from NCBI Gene [10611](https://www.ncbi.nlm.nih.gov/gene/10611):

> This gene encodes a member of a family of proteins that possess a 100-amino acid PDZ domain at the N terminus and one to three LIM domains at the C-terminus. This family member functions as a scaffold protein that tethers protein kinases to the Z-disk in striated muscles. It is thought to function in cardiomyocyte expansion and in restraining postsynaptic growth of excitatory synapses. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:17468](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17468) · Entrez [10611](https://www.ncbi.nlm.nih.gov/gene/10611) · UniProt [Q96HC4](https://www.uniprot.org/uniprotkb/Q96HC4) · Ensembl [ENSG00000163110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163110)

## Data

Gene col 8634: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8634); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8634, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8634]; `tensor/DDL_lfc|DDL_z.npy` [8634]; `embed/gene_vectors.npy` [8634]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8634 or target_col == 8634). Every well: [[PDLIM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDLIM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
