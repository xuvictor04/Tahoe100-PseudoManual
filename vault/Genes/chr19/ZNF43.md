---
symbol: "ZNF43"
type: "gene"
col: 12608
ensembl_id: "ENSG00000198521"
name: "zinc finger protein 43"
location: "19p12"
module: 91
arm: "+"
pooled_cpm: 12.05
n_lines_expressing: 29
n_dd_up: 5
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# ZNF43

*zinc finger protein 43* — 19p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.62× (z +9.6, q 6e-19, up in 18 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.652× (z -8.4, q 2e-14, down in 16 of 26 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (AN3 CA 0.0586×, A-427 0.236×, J82 0.355×, A549 0.230×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (J82 0.295×, HOP62 0.230×, PANC-1 0.310×, AN3 CA 0.131×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.466×, AN3 CA 0.337×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.126×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.133×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF724]] (+0.60, fdr 1e-05), [[HROB]] (+0.59, fdr 1e-05), [[ZNF254]] (+0.58, fdr 3e-05); moves opposite to [[USP3]] (-0.49, fdr 3e-05), [[SERP1]] (-0.48, fdr 4e-05), [[DNAJC3]] (-0.48, fdr 3e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF100]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNF100]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12608.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +9.6 | 6e-19 | 18/27 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.98×** | +5.0 | 2e-04 | 11/27 (PANC-1, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +4.4 | 0.002 | 9/26 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.079 | 9/27 (NCI-H2347, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.59×** | +3.4 | 0.079 | 6/26 (SW 900, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.26× | +3.2 | 0.12 | 7/26 (J82, SW 900, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.16 | 5/27 (LS 180, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | 1.24× | +3.1 | 0.16 | 4/27 (BT-474, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12608.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (AN3 CA 0.0586×, A-427 0.236×, J82 0.355×, A549 0.230×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (J82 0.295×, HOP62 0.230×, PANC-1 0.310×, AN3 CA 0.131×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.466×, AN3 CA 0.337×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.126×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.133×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -8.4 | 2e-14 | 16/26 (HOP62, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.588×** | -6.8 | 4e-09 | 15/25 (NCI-H23, BT-474, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.636×** | -5.8 | 1e-06 | 12/17 (J82, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.676×** | -5.5 | 7e-06 | 13/23 (AN3 CA, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.729×** | -4.4 | 0.001 | 10/27 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.721×** | -4.2 | 0.003 | 11/15 (AN3 CA, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.616×** | -3.5 | 0.033 | 8/19 (SK-MEL-2, SW 900, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[palbociclib (drug)]] 0.05 µM |  | 0.790× | -3.1 | 0.14 | 10/27 (H4, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12608. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 90.3 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -16.2) |
| [[HOP62 (line)]] | alt | 34.1 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -8.9) |
| [[J82 (line)]] | alt | 80.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +15.5) | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -10.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -10.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 5.93 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.0724× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.174× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.707 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.815 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.696 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.907 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.848 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.875 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.694 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12608), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF724]] | +0.60 | +0.64 / +0.56 | both halves | 1e-05 | same gene group |
| [[HROB]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ZNF254]] | +0.58 | +0.46 / +0.60 | both halves | 3e-05 | same gene group |
| [[ZNF93]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 | same gene group |
| [[ZNF66]] | +0.56 | +0.63 / +0.52 | both halves | 1e-05 | same gene group |
| [[KIF24]] | +0.56 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[HYLS1]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[BRCA2]] | +0.56 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ZNF107]] | +0.55 | +0.55 / +0.54 | both halves | 1e-05 | same gene group |
| [[CEP295]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SGO1]] | +0.54 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[CPSF7]] | +0.53 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP3]] | -0.49 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[SERP1]] | -0.48 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[DNAJC3]] | -0.48 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[CBLB]] | -0.48 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[OSTC]] | -0.46 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[TRAM1]] | -0.46 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[MFN1]] | -0.45 | -0.49 / -0.29 | both halves | 3e-04 |  |
| [[SSR3]] | -0.45 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[FNBP1L]] | -0.45 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[TMED2]] | -0.45 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[TXNDC11]] | -0.45 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[L3MBTL3]] | -0.44 | -0.31 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF100]] | B | ZNF100 activity raises ZNF43's level | lines that do not express ZNF100 (9) vs lines expressing it (41) | 2.74× lower at baseline in the lines without ZNF100 | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF66, ENSG00000269237, SORT1 |
| [[ZNF66]] | B | ZNF66 activity raises ZNF43's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 3.64× lower at baseline in the lines without ZNF66 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF100]] | B | ZNF43 activity raises ZNF100's level | lines that do not express ZNF43 (21) vs lines expressing it (29) | 1.53× lower at baseline in the lines without ZNF43 | 0.063 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF354C, S1PR3 |

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-44.9, -49.4); signed map (-39.1, -36.3). **Vector** length 49.9, 9.80% of its response variance represented; |z| ≥ 3 in 516 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +9.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.7 | +0.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +1.7 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +1.3 | +3.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.2 | +1.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.1 | +2.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.0 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.9 | +2.0 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +0.8 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.0 | -8.4 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -1.1 | -2.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.0 | +0.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -2.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -0.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p12 — chr19:21,804,946-21,852,125 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HTF6, KOX27; previously ZNF39L1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17038](https://www.uniprot.org/uniprotkb/P17038) (Zinc finger protein 43):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7594](https://www.ncbi.nlm.nih.gov/gene/7594):

> This gene belongs to the C2H2-type zinc finger gene family. The zinc finger proteins are involved in gene regulation and development, and are quite conserved throughout evolution. Like this gene product, a third of the zinc finger proteins containing C2H2 fingers also contain the KRAB domain, which has been found to be involved in protein-protein interactions. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13109](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13109) · Entrez [7594](https://www.ncbi.nlm.nih.gov/gene/7594) · UniProt [P17038](https://www.uniprot.org/uniprotkb/P17038) · Ensembl [ENSG00000198521](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198521)

## Data

Gene col 12608: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12608); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12608, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12608]; `tensor/DDL_lfc|DDL_z.npy` [12608]; `embed/gene_vectors.npy` [12608]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12608 or target_col == 12608). Every well: [[ZNF43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
