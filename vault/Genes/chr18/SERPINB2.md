---
symbol: "SERPINB2"
type: "gene"
col: 12435
ensembl_id: "ENSG00000197632"
name: "serpin family B member 2"
location: "18q21.33-q22.1"
module: 19
arm: "+"
pooled_cpm: 35.03
n_lines_expressing: 14
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SERPINB2

*serpin family B member 2* — 18q21.33-q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.09× (z +10.5, q 6e-23, up in 7 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.26× (z +8.6, q 1e-15, up in 8 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 0.05 µM: 0.651× (z -4.4, q 0.006, down in 3 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCC9]] (+0.59, fdr 3e-05), [[CREB5]] (+0.58, fdr 4e-05), [[AADAC]] (+0.57, fdr 1e-05); moves opposite to [[SMIM3]] (-0.49, fdr 3e-05), [[PKD1P6]] (-0.47, fdr 4e-05), [[C12orf76]] (-0.47, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LSAMP]] → it (grade B ⚠); 6 go from it, the strongest it → [[AJAP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12435.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.09×** | +10.5 | 6e-23 | 7/11 (LOX-IMVI, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.94×** | +9.8 | 3e-20 | 6/10 (LOX-IMVI, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.61×** | +8.8 | 2e-16 | 7/11 (SNU-423, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.26×** | +8.6 | 1e-15 | 8/12 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +5.8 | 6e-07 | 6/12 (hTERT-HPNE, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.11×** | +5.6 | 2e-06 | 9/12 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.79×** | +4.0 | 0.005 | 10/12 (RPMI-7951, hTERT-HPNE, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +3.7 | 0.014 | 8/12 (RPMI-7951, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.58×** | +3.4 | 0.044 | 7/12 (hTERT-HPNE, A-427, …) | rises with dose | composition shift |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.79× | +3.1 | 0.11 | 2/12 (NCI-H1792, SNU-423) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | 2.17× | +3.0 | 0.13 | 6/11 (A-427, RPMI-7951, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12435.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **0.651×** | -4.4 | 0.006 | 3/12 (NCI-H1573, A-427, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.568×** | -4.2 | 0.008 | 12/12 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.691×** | -3.9 | 0.022 | 10/12 (LS 180, Panc 03.27, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.610×** | -3.6 | 0.037 | 6/12 (H4, NCI-H1792, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.632×** | -3.4 | 0.071 | 10/12 (Panc 03.27, NCI-H1792, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.634×** | -3.4 | 0.071 | 11/12 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.651× | -3.2 | 0.12 | 1/12 (H4) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 0.633× | -3.1 | 0.12 | 3/12 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses |  |
| [[Vandetanib (drug)]] 5 µM |  | 0.661× | -3.1 | 0.14 | 7/12 (H4, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12435. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 239 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0900× (z -16.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -13.7) |
| [[Panc 03.27 (line)]] | alt | 94.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0800× (z -15.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0815× (z -10.6) |
| [[LS 180 (line)]] | wt | 18.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0846× (z -9.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.111× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 97.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -11.2) |
| [[A-172 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 662 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.16 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.09 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.44 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.07 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.15 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12435), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC9]] | +0.59 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[CREB5]] | +0.58 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[AADAC]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[GTF2IP7]] | +0.57 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[CXCL8]] | +0.56 | +0.43 / +0.63 | both halves | 3e-05 | STRING 494 |
| [[NRG1]] | +0.55 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[CLDN16]] | +0.55 | +0.41 / +0.51 | both halves | 4e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[NAV3]] | +0.53 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[STEAP1B-AS1]] | +0.52 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[NCKAP5]] | +0.52 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[INHBA]] | +0.52 | +0.43 / +0.57 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[AADACP1]] | +0.52 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM3]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PKD1P6]] | -0.47 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[C12orf76]] | -0.47 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[PRKRA]] | -0.46 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[EEF2K]] | -0.45 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[TTC9C]] | -0.43 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[NISCH]] | -0.42 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[CLPP]] | -0.41 | -0.26 / -0.41 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSAMP]] | B | LSAMP activity raises SERPINB2's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 2.87× lower at baseline in the lines without LSAMP | 0.062 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[CPED1]] | C | CPED1 activity raises SERPINB2's level | lines that do not express CPED1 (24) vs lines expressing it (26) | 2.66× lower at baseline in the lines without CPED1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CCNYL2, LINC01885, ENSG00000291032; maybe low, not absent; co-absent with the target |
| [[IL1B]] | C | IL1B activity raises SERPINB2's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.82× lower at baseline in the lines without IL1B | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AJAP1]] | C | SERPINB2 activity raises AJAP1's level | lines that do not express SERPINB2 (36) vs lines expressing it (14) | 3.91× lower at baseline in the lines without SERPINB2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000254337, TMPRSS15, LINC00824; co-absent with the target |
| [[PKIA]] | C | SERPINB2 activity raises PKIA's level | lines that do not express SERPINB2 (36) vs lines expressing it (14) | 3.66× lower at baseline in the lines without SERPINB2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000254337, TMPRSS15, LINC00824; co-absent with the target |
| [[ADAMTS1]] | C | SERPINB2 activity raises ADAMTS1's level | lines that do not express SERPINB2 (36) vs lines expressing it (14) | 3.77× lower at baseline in the lines without SERPINB2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000254337, TMPRSS15, LINC00824; co-absent with the target |
| [[INHBA]] | C | SERPINB2 activity raises INHBA's level | lines that do not express SERPINB2 (36) vs lines expressing it (14) | 4.12× lower at baseline in the lines without SERPINB2 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000254337, TMPRSS15, LINC00824; co-absent with the target |
| [[TMPRSS15]] | C | SERPINB2 activity raises TMPRSS15's level | lines that do not express SERPINB2 (36) vs lines expressing it (14) | 2.58× lower at baseline in the lines without SERPINB2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000254337, TMPRSS15, LINC00824; co-absent with the target |
| [[IL1A]] | C | SERPINB2 activity raises IL1A's level | lines that do not express SERPINB2 (36) vs lines expressing it (14) | 3.31× lower at baseline in the lines without SERPINB2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000254337, TMPRSS15, LINC00824; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.498). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.8, 16.7); signed map (18.0, 53.6). **Vector** length 51.1, 17.3% of its response variance represented; |z| ≥ 3 in 435 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +5.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +0.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.1 | +1.9 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -3.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | serpin family B member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.33-q22.1 — chr18:63,871,692-63,903,888 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HsT1201, PAI-2; previously PLANH2, PAI2 |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Hallmark sets | COAGULATION, KRAS_SIGNALING_DN, COMPLEMENT, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 7 pathways, smallest: Dissolution of Fibrin Clot; Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P05120](https://www.uniprot.org/uniprotkb/P05120) (Plasminogen activator inhibitor 2):

> Inhibits urokinase-type plasminogen activator. The monocyte derived PAI-2 is distinct from the endothelial cell-derived PAI-1.

**Summary**, from NCBI Gene [5055](https://www.ncbi.nlm.nih.gov/gene/5055):

> Predicted to enable serine-type endopeptidase inhibitor activity. Predicted to be involved in fibrinolysis and negative regulation of apoptotic process. Predicted to be located in extracellular region and plasma membrane. Predicted to be active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8584](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8584) · Entrez [5055](https://www.ncbi.nlm.nih.gov/gene/5055) · UniProt [P05120](https://www.uniprot.org/uniprotkb/P05120) · Ensembl [ENSG00000197632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197632)

## Data

Gene col 12435: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12435); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12435, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12435]; `tensor/DDL_lfc|DDL_z.npy` [12435]; `embed/gene_vectors.npy` [12435]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12435 or target_col == 12435). Every well: [[SERPINB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
