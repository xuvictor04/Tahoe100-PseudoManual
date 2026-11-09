---
symbol: "PNPLA4"
type: "gene"
col: 131
ensembl_id: "ENSG00000006757"
name: "patatin like domain 4, phospholipase and triacylglycerol lipase"
location: "Xp22.31"
module: 12
arm: "+"
pooled_cpm: 3.41
n_lines_expressing: 39
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PNPLA4

*patatin like domain 4, phospholipase and triacylglycerol lipase* — Xp22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.81× (z +10.7, q 6e-24, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.55× (z +5.1, q 4e-05, up in 17 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.503× (z -5.7, q 6e-06, down in 19 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EBAG9]] (+0.70, fdr 7e-06), [[CCDC25]] (+0.67, fdr 7e-06), [[PPP4R2]] (+0.66, fdr 7e-06); moves opposite to [[RBM14-RBM4]] (-0.64, fdr 7e-06), [[MBOAT7]] (-0.57, fdr 3e-05), [[EHBP1L1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SPINK5]] → it (grade B ⚠); 3 go from it, the strongest it → [[EPC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 131.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.81×** | +10.7 | 6e-24 | 4/5 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.06×** | +9.3 | 4e-18 | 14/15 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.49×** | +6.7 | 3e-09 | 5/6 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +5.1 | 4e-05 | 17/37 (NCI-H2347, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.75×** | +4.7 | 3e-04 | 17/33 (LoVo, SW480, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.68×** | +4.3 | 0.002 | 15/34 (KATO III, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.67×** | +4.3 | 0.002 | 6/16 (BT-474, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +4.1 | 0.002 | 12/32 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.017 | 9/36 (C-33 A, SW480, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.017 | 9/32 (NCI-H2347, C32, …) | top dose only |  |
| [[palbociclib (drug)]] 0.05 µM |  | **1.57×** | +3.5 | 0.021 | 3/35 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.024 | 11/31 (NCI-H1792, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.54×** | +3.2 | 0.065 | 7/26 (SW480, Panc 03.27, …) | all doses, flat | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.2 | 0.065 | 5/30 (HOP62, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.47×** | +3.1 | 0.082 | 6/33 (HEC-1-A, RKO, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 131.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.503×** | -5.7 | 6e-06 | 19/36 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.540×** | -5.1 | 8e-05 | 16/35 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.560×** | -4.8 | 3e-04 | 14/36 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.568×** | -4.5 | 0.001 | 15/34 (HCT15, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.596×** | -4.3 | 0.002 | 11/28 (J82, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.644×** | -3.7 | 0.024 | 12/36 (A549, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.650×** | -3.6 | 0.027 | 16/35 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.684× | -3.2 | 0.10 | 8/29 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.481× | -3.1 | 0.10 | 11/32 (NCI-H1573, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 131. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 7.69 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.0774× (z -9.1) |
| [[A-172 (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.938 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.312 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.341 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 131), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EBAG9]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[CCDC25]] | +0.67 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[PPP4R2]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TMEM42]] | +0.65 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[MRPS33]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[TRMT1L]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[SDSL]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[DECR2]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[MSRB2]] | +0.65 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.64 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM14-RBM4]] | -0.64 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[MBOAT7]] | -0.57 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[EHBP1L1]] | -0.56 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[SNRPA]] | -0.56 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[TECR]] | -0.54 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[UFD1]] | -0.54 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[TPST2]] | -0.53 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[RAD9A]] | -0.53 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[ZNF731P]] | -0.53 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.53 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[CHAF1B]] | -0.52 | -0.49 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPINK5]] | B | SPINK5 activity raises PNPLA4's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 1.63× lower at baseline in the lines without SPINK5 | 0.041 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[PSMB5]] | B | PSMB5 activity raises PNPLA4's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPC1]] | B | PNPLA4 activity lowers EPC1's level | lines that do not express PNPLA4 (11) vs lines expressing it (39) | 1.13× higher at baseline in the lines without PNPLA4 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000285679, PRKCZ, GPR160 |
| [[ZNF731P]] | B | PNPLA4 activity raises ZNF731P's level | lines that do not express PNPLA4 (11) vs lines expressing it (39) | 1.35× lower at baseline in the lines without PNPLA4 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000285679, PRKCZ, GPR160 |
| [[ASNSD1]] | B | PNPLA4 activity lowers ASNSD1's level | lines that do not express PNPLA4 (11) vs lines expressing it (39) | 1.12× higher at baseline in the lines without PNPLA4 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000285679, PRKCZ, GPR160 |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.579). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-31.3, 2.9); signed map (5.6, -21.4). **Vector** length 38.5, 5.08% of its response variance represented; |z| ≥ 3 in 591 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.7 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.4 | +4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +3.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.0 | +2.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.0 | -5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.5 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -0.8 | -2.0 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -0.7 | -1.4 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.7 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | patatin like domain 4, phospholipase and triacylglycerol lipase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.31 — chrX:7,898,247-7,927,739 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DXS1283E, GS2, iPLA2eta |
| Gene groups (HGNC) | Patatin like phospholipase domain containing |
| Reactome | 3 pathways, smallest: Triglyceride catabolism; Triglyceride metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [P41247](https://www.uniprot.org/uniprotkb/P41247) (Patatin-like phospholipase domain-containing protein 4):

> Has abundant triacylglycerol lipase activity. Transfers fatty acid from triglyceride to retinol, hydrolyzes retinylesters, and generates 1,3-diacylglycerol from triglycerides. Additionally possesses acylglycerol transacylase and phospholipase A2 activities. Able to catalyze fatty acyl CoA-dependent retinol esterification during epidermal maturation, when pH becomes acidic.

**Summary**, from NCBI Gene [8228](https://www.ncbi.nlm.nih.gov/gene/8228):

> This gene encodes a member of the patatin-like family of phospholipases. The encoded enzyme has both triacylglycerol lipase and transacylase activities and may be involved in adipocyte triglyceride homeostasis. Alternate splicing results in multiple transcript variants. A pseudogene of this gene is found on chromosome Y. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:24887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24887) · Entrez [8228](https://www.ncbi.nlm.nih.gov/gene/8228) · UniProt [P41247](https://www.uniprot.org/uniprotkb/P41247) · Ensembl [ENSG00000006757](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006757)

## Data

Gene col 131: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 131); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 131, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 131]; `tensor/DDL_lfc|DDL_z.npy` [131]; `embed/gene_vectors.npy` [131]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 131 or target_col == 131). Every well: [[PNPLA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNPLA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
