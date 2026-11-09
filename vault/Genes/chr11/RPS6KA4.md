---
symbol: "RPS6KA4"
type: "gene"
col: 8498
ensembl_id: "ENSG00000162302"
name: "ribosomal protein S6 kinase A4"
location: "11q13.1"
module: 2
arm: "+"
pooled_cpm: 10.96
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# RPS6KA4

*ribosomal protein S6 kinase A4* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.78× (z +15.7, q 0e+00, up in 28 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.57× (z +6.9, q 5e-10, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.658× (z -9.0, q 1e-16, down in 27 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW48 0.188×, Hs 766T 0.293×, HT-29 0.294×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 0.328×, PANC-1 0.463×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.136×); [[Ixazomib (drug)]] 0.05 µM in 1 line (C-33 A 0.0567×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD52]] (+0.72, fdr 7e-06), [[RIPOR1]] (+0.63, fdr 1e-05), [[MAPKAPK3]] (+0.61, fdr 1e-05); moves opposite to [[SYNRG]] (-0.51, fdr 4e-05), [[GCC2]] (-0.51, fdr 3e-05), [[RSPRY1]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LAMA5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +15.7 | 0e+00 | 28/34 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +12.4 | 4e-33 | 15/20 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +8.0 | 3e-13 | 30/44 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +6.9 | 5e-10 | 28/46 (PANC-1, C-33 A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.4 | 2e-08 | 18/39 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +5.9 | 5e-07 | 15/26 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +5.6 | 2e-06 | 20/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.37×** | +4.9 | 6e-05 | 15/47 (SW480, AsPC-1, …) | rises with dose | composition shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +4.9 | 6e-05 | 14/47 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **1.35×** | +4.7 | 2e-04 | 14/38 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.35×** | +4.6 | 2e-04 | 11/47 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 2e-04 | 18/45 (AsPC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.34×** | +4.5 | 3e-04 | 13/46 (SW480, AsPC-1, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +4.4 | 5e-04 | 13/46 (A549, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +4.1 | 0.001 | 9/44 (SW480, Hs 766T, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.001 | 13/45 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.001 | 10/47 (NCI-H23, SNU-423, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.001 | 16/46 (AsPC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.002 | 7/44 (PANC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.002 | 6/47 (NCI-H2030, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.006 | 11/47 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.7 | 0.006 | 12/48 (NCI-H2030, J82, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.030 | 4/33 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.056 | 5/45 (HEC-1-A, AsPC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8498.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW48 0.188×, Hs 766T 0.293×, HT-29 0.294×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 0.328×, PANC-1 0.463×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.136×); [[Ixazomib (drug)]] 0.05 µM in 1 line (C-33 A 0.0567×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.658×** | -9.0 | 1e-16 | 27/46 (SW48, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.673× | -3.2 | 0.38 | 11/46 (A-172, H4, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.817× | -3.1 | 0.38 | 9/47 (SNU-1, Panc 03.27, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.21× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 13.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +8.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -9.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 10.7 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.0567× (z -10.8) |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -9.3) |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 6.97 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0685× (z -9.4) |
| [[J82 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 14.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -10.9) |
| [[SHP-77 (line)]] | alt | 7.41 | 0 | 1 | — | [[BI-78D3 (drug)]] 0.05 µM 0.0993× (z -8.8) |
| [[SW48 (line)]] | wt | 19.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -10.5) |
| [[SW480 (line)]] | alt | 9.84 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.93× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD52]] | +0.72 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[RIPOR1]] | +0.63 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[MAPKAPK3]] | +0.61 | +0.49 / +0.69 | both halves | 1e-05 | same gene group |
| [[PSEN2]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ABCC10]] | +0.61 | +0.64 / +0.50 | both halves | 1e-05 | same gene group |
| [[HEATR3]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NBEAL2]] | +0.60 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[SHANK3]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[LZTR1]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[DGKZ]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 | same gene group |
| [[KLHL17]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[UBE2F]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNRG]] | -0.51 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[GCC2]] | -0.51 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[RSPRY1]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ANKHD1]] | -0.48 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ARID4B]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 | same gene group |
| [[SAP18]] | -0.48 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[GTF2B]] | -0.47 | -0.33 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA5]] | B | LAMA5 activity raises RPS6KA4's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without LAMA5 | 0.020 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-9.4, -27.4); signed map (-27.2, -46.6). **Vector** length 75.4, 13.3% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.8 | +6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +0.5 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.8 | -9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.8 | -0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -3.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S6 kinase A4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,359,148-64,372,215 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RSK-B, MSK2 |
| Gene groups (HGNC) | MAPK activated protein kinases; MicroRNA protein coding host genes; Ribosomal protein S6 kinase family |
| Reactome | 4 pathways, smallest: Recycling pathway of L1; L1CAM interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [O75676](https://www.uniprot.org/uniprotkb/O75676) (Ribosomal protein S6 kinase alpha-4):

> Serine/threonine-protein kinase that is required for the mitogen or stress-induced phosphorylation of the transcription factors CREB1 and ATF1 and for the regulation of the transcription factor RELA, and that contributes to gene activation by histone phosphorylation and functions in the regulation of inflammatory genes. Phosphorylates CREB1 and ATF1 in response to mitogenic or stress stimuli such as UV-C irradiation, epidermal growth factor (EGF) and anisomycin. Plays an essential role in the …

**Summary**, from NCBI Gene [8986](https://www.ncbi.nlm.nih.gov/gene/8986):

> This gene encodes a member of the RSK (ribosomal S6 kinase) family of serine/threonine kinases. This kinase contains 2 non-identical kinase catalytic domains and phosphorylates various substrates, including CREB1 and ATF1. The encoded protein can also phosphorylate histone H3 to regulate certain inflammatory genes. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:10433](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10433) · Entrez [8986](https://www.ncbi.nlm.nih.gov/gene/8986) · UniProt [O75676](https://www.uniprot.org/uniprotkb/O75676) · Ensembl [ENSG00000162302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162302)

## Data

Gene col 8498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8498); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8498]; `tensor/DDL_lfc|DDL_z.npy` [8498]; `embed/gene_vectors.npy` [8498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8498 or target_col == 8498). Every well: [[RPS6KA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS6KA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
