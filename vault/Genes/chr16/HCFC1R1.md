---
symbol: "HCFC1R1"
type: "gene"
col: 2323
ensembl_id: "ENSG00000103145"
name: "host cell factor C1 regulator 1"
location: "16p13.3"
module: 24
arm: "+"
pooled_cpm: 16.73
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# HCFC1R1

*host cell factor C1 regulator 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.60× (z +5.6, q 1e-05, up in 28 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 1.59× (z +3.8, q 0.024, up in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 6.24×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.524× (z -5.3, q 5e-05, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM7-AS2]] (+0.67, fdr 7e-06), [[NAT14]] (+0.66, fdr 1e-05), [[DBP]] (+0.64, fdr 1e-05); moves opposite to [[GNL3L]] (-0.63, fdr 1e-05), [[DPH5-DT]] (-0.60, fdr 1e-05), [[MTHFD2L]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PCSK1N]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2323.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 6.24×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.60×** | +5.6 | 1e-05 | 28/38 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.04×** | +4.0 | 0.016 | 15/27 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.024 | 30/47 (RKO, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.87×** | +3.7 | 0.033 | 29/44 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2323.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.524×** | -5.3 | 5e-05 | 31/46 (SNU-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.418×** | -5.1 | 9e-05 | 37/48 (AN3 CA, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.440×** | -4.8 | 3e-04 | 35/46 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.466×** | -4.5 | 0.001 | 29/46 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.485×** | -4.2 | 0.003 | 32/46 (HOP62, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.477×** | -4.1 | 0.004 | 30/46 (RPMI-7951, SNU-423, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.519×** | -3.8 | 0.010 | 28/48 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.542×** | -3.6 | 0.024 | 28/47 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.323×** | -3.5 | 0.034 | 30/46 (SK-MEL-2, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.537×** | -3.4 | 0.034 | 30/47 (SNU-1, AN3 CA, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.573×** | -3.3 | 0.058 | 26/48 (H4, HOP62, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.594× | -3.0 | 0.10 | 21/47 (LOX-IMVI, A498, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.596× | -3.0 | 0.10 | 21/46 (A498, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.598× | -3.0 | 0.10 | 23/48 (LOX-IMVI, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2323. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 26.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0422× (z -11.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[Hs 766T (line)]] | wt | 27.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -8.9) |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0815× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 40.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -9.3) |
| [[SNU-423 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.111× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2323), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM7-AS2]] | +0.67 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[NAT14]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[DBP]] | +0.64 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[PCSK1N]] | +0.63 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[ARL3]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[HCFC2]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[TTC21A]] | +0.61 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[CUTA]] | +0.61 | +0.46 / +0.71 | both halves | 3e-05 |  |
| [[RNASE4]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[VEGFB]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CCDC85B]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[NDUFA2]] | +0.60 | +0.41 / +0.62 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL3L]] | -0.63 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[DPH5-DT]] | -0.60 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[MTHFD2L]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PRMT3]] | -0.58 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.57 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[PSME3]] | -0.57 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[NBPF20]] | -0.56 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[MRPS25]] | -0.54 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[PCBD2]] | -0.54 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TMX3]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK1N]] | B | PCSK1N activity raises HCFC1R1's level | lines that do not express PCSK1N (21) vs lines expressing it (29) | 1.03× lower at baseline in the lines without PCSK1N | 0.050 | ⚠ within organs, on part of the lines; also absent: MAP6, CERS4, CACNG4 |
| [[RPH3AL]] | B | RPH3AL activity lowers HCFC1R1's level | lines that do not express RPH3AL (10) vs lines expressing it (40) | 1.26× higher at baseline in the lines without RPH3AL | 0.093 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, PATJ; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises HCFC1R1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.580). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-43.0, -17.8); signed map (-26.3, 11.3). **Vector** length 87.7, 25.9% of its response variance represented; |z| ≥ 3 in 755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +3.5 | +3.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.1 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | -0.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -5.5 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.1 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.8 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.9 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.6 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | host cell factor C1 regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,022,625-3,024,286 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HPIP, FLJ20568 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWW0](https://www.uniprot.org/uniprotkb/Q9NWW0) (Host cell factor C1 regulator 1):

> Regulates HCFC1 activity by modulating its subcellular localization. Overexpression of HCFC1R1 leads to accumulation of HCFC1 in the cytoplasm. HCFC1R1-mediated export may provide the pool of cytoplasmic HCFC1 required for import of virion-derived VP16 into the nucleus.

**Summary**, from NCBI Gene [54985](https://www.ncbi.nlm.nih.gov/gene/54985):

> Predicted to be located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21198](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21198) · Entrez [54985](https://www.ncbi.nlm.nih.gov/gene/54985) · UniProt [Q9NWW0](https://www.uniprot.org/uniprotkb/Q9NWW0) · Ensembl [ENSG00000103145](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103145)

## Data

Gene col 2323: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2323); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2323, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2323]; `tensor/DDL_lfc|DDL_z.npy` [2323]; `embed/gene_vectors.npy` [2323]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2323 or target_col == 2323). Every well: [[HCFC1R1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCFC1R1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
