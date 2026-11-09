---
symbol: "CUL2"
type: "gene"
col: 2917
ensembl_id: "ENSG00000108094"
name: "cullin 2"
location: "10p11.21"
module: 29
arm: "+"
pooled_cpm: 58.68
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CUL2

*cullin 2* — 10p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.73× (z +11.9, q 1e-29, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.695× (z -7.6, q 2e-11, down in 32 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 0.771× (z -3.8, q 0.019, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H23 0.194×, NCI-H460 0.324×, AsPC-1 0.334×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.133×, J82 0.406×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.216×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPS7B]] (+0.73, fdr 7e-06), [[MINPP1]] (+0.63, fdr 1e-05), [[ARHGEF7]] (+0.62, fdr 8e-06); moves opposite to [[NBPF10]] (-0.61, fdr 1e-05), [[LCAT]] (-0.61, fdr 1e-05), [[JUND]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF618]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2917.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.73×** | +11.9 | 1e-29 | 45/49 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.73×** | +9.0 | 4e-17 | 42/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.30×** | +7.7 | 3e-12 | 29/48 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +6.1 | 1e-07 | 32/48 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.33×** | +6.0 | 3e-07 | 32/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.29×** | +5.2 | 2e-05 | 28/48 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +5.0 | 5e-05 | 25/48 (LS 180, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.24×** | +4.5 | 4e-04 | 21/48 (LOX-IMVI, RPMI-7951, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.24×** | +4.3 | 0.001 | 21/48 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.21×** | +4.0 | 0.004 | 21/48 (LoVo, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.005 | 19/48 (HOP62, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.8 | 0.008 | 9/48 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.008 | 13/48 (A-172, LS 180, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.19× | +3.7 | 0.010 | 17/48 (PANC-1, NCI-H1792, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.19× | +3.6 | 0.011 | 14/48 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.022 | 13/48 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.035 | 9/48 (A549, MIA PaCa-2, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2917.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H23 0.194×, NCI-H460 0.324×, AsPC-1 0.334×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.133×, J82 0.406×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.216×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.695×** | -7.6 | 2e-11 | 32/49 (SW1417, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.712×** | -6.5 | 2e-08 | 27/45 (C-33 A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.814×** | -4.1 | 0.007 | 21/42 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.825×** | -4.0 | 0.009 | 21/48 (MIA PaCa-2, HEC-1-A, …) | two highest doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.771×** | -3.8 | 0.019 | 21/48 (SW 900, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.892× | -3.4 | 0.072 | 12/48 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.807× | -3.1 | 0.14 | 13/48 (HepG2/C3A, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.808× | -3.1 | 0.14 | 17/47 (CHP-212, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 64.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.70× (z +9.2) | — |
| [[SW480 (line)]] | alt | 57.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.54× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 38.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -8.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 73.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -17.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 70.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 44.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +8.6) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[LS 180 (line)]] | wt | 50.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 92.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 74.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -16.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 48.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -13.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 69.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.373× (z -10.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 83.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.86× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 65.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 65.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 73.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS7B]] | +0.73 | +0.79 / +0.68 | both halves | 7e-06 | pathway: Neddylation; STRING 882 |
| [[MINPP1]] | +0.63 | +0.64 / +0.51 | both halves | 1e-05 | same gene group |
| [[ARHGEF7]] | +0.62 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[USF1]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[RNF4]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[CIPC]] | +0.61 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PIK3R4]] | +0.60 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[ANP32A]] | +0.59 | +0.64 / +0.53 | both halves | 1e-05 | same gene group |
| [[PGAM1]] | +0.59 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[NAXD]] | +0.59 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[SUMO1]] | +0.58 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[PPP2R5E]] | +0.58 | +0.67 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF10]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[LCAT]] | -0.61 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[JUND]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[NBPF19]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[OFD1]] | -0.55 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[MATN1-AS1]] | -0.55 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[NBPF14]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[IER5]] | -0.53 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[MIR23AHG]] | -0.52 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[LIME1]] | -0.52 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[TINCR]] | -0.51 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[IER2]] | -0.51 | -0.50 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF618]] | B | ZNF618 activity raises CUL2's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without ZNF618 | 0.011 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |
| [[CCDC88A]] | B | CCDC88A activity raises CUL2's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.25× lower at baseline in the lines without CCDC88A | 0.087 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-11.0, -13.6); signed map (-36.4, -20.3). **Vector** length 86.6, 19.3% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +11.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.7 | +1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -3.6 | -4.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | cullin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.21 — chr10:35,008,504-35,127,006 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cullins; MicroRNA protein coding host genes |
| Reactome | 15 pathways, smallest: Oxygen-dependent proline hydroxylation of Hypoxia-inducible Factor Alpha; Cellular response to hypoxia; Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13617](https://www.uniprot.org/uniprotkb/Q13617) (Cullin-2):

> Core component of multiple cullin-RING-based ECS (ElonginB/C-CUL2/5-SOCS-box protein) E3 ubiquitin-protein ligase complexes, which mediate the ubiquitination of target proteins. CUL2 serves as a rigid scaffold in the complex and may contribute to catalysis through positioning of the substrate and the E2 ubiquitin-conjugating enzyme. The E3 ubiquitin-protein ligase activity of the complex is dependent on the neddylation of the cullin subunit and is inhibited by the association of the …

**Summary**, from NCBI Gene [8453](https://www.ncbi.nlm.nih.gov/gene/8453):

> Enables ubiquitin ligase complex scaffold activity and ubiquitin protein ligase binding activity. Involved in ubiquitin-dependent protein catabolic process via the C-end degron rule pathway. Located in nucleoplasm. Part of Cul2-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:2552](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2552) · Entrez [8453](https://www.ncbi.nlm.nih.gov/gene/8453) · UniProt [Q13617](https://www.uniprot.org/uniprotkb/Q13617) · Ensembl [ENSG00000108094](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108094)

## Data

Gene col 2917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2917); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2917]; `tensor/DDL_lfc|DDL_z.npy` [2917]; `embed/gene_vectors.npy` [2917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2917 or target_col == 2917). Every well: [[CUL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
