---
symbol: "HOXB2"
type: "gene"
col: 10444
ensembl_id: "ENSG00000173917"
name: "homeobox B2"
location: "17q21.32"
module: 95
arm: "+"
pooled_cpm: 3.61
n_lines_expressing: 29
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# HOXB2

*homeobox B2* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.93× (z +10.9, q 9e-25, up in 9 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +5.4, q 1e-05, up in 11 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.432× (z -6.7, q 1e-08, down in 16 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZCCHC3]] (+0.62, fdr 1e-05), [[TBX2]] (+0.60, fdr 1e-05), [[ZBED5]] (+0.59, fdr 4e-05); moves opposite to [[STRAP]] (-0.54, fdr 9e-05), [[OPA1]] (-0.50, fdr 9e-05), [[NUTF2]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 3 go from it, the strongest it → [[HOXC10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10444.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.93×** | +10.9 | 9e-25 | 9/14 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +8.0 | 3e-13 | 2/4 (PANC-1, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +6.6 | 8e-09 | 13/20 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.4 | 1e-05 | 11/20 (C32, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +4.9 | 9e-05 | 7/14 (KATO III, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +4.6 | 3e-04 | 4/7 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.79×** | +4.6 | 3e-04 | 6/15 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.25×** | +4.6 | 3e-04 | 8/16 (C-33 A, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +4.3 | 0.001 | 8/24 (C32, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.73×** | +4.2 | 0.002 | 14/23 (A-172, PANC-1, …) | rises with dose | composition shift |
| [[Celecoxib (drug)]] 0.5 µM |  | **2.08×** | +4.1 | 0.002 | 5/21 (PANC-1, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.43×** | +4.0 | 0.003 | 7/23 (KATO III, RKO, …) | top dose only | composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.94×** | +3.7 | 0.008 | 7/20 (SW480, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +3.7 | 0.010 | 16/25 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +3.6 | 0.011 | 8/25 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.82×** | +3.4 | 0.025 | 10/21 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10444.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.432×** | -6.7 | 1e-08 | 16/25 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.520×** | -5.2 | 5e-05 | 16/25 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.531×** | -5.1 | 8e-05 | 21/25 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.543×** | -4.9 | 1e-04 | 13/25 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.387×** | -3.5 | 0.052 | 9/22 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10444. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -13.5) |
| [[C-33 A (line)]] | alt | 9.91 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0578× (z -10.7) |
| [[C32 (line)]] | wt | 4.65 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0171× (z -12.6) |
| [[RPMI-7951 (line)]] | alt | 6.78 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0246× (z -12.4) |
| [[SW1417 (line)]] | alt | 22.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -9.5) |
| [[A-172 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.926 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.609 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.867 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.661 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.395 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.850 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10444), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC3]] | +0.62 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[TBX2]] | +0.60 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ZBED5]] | +0.59 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[ZNF580]] | +0.59 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[SOCS2]] | +0.58 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[LINC02307]] | +0.58 | +0.36 / +0.45 | both halves | 1e-04 |  |
| [[FAM200B]] | +0.58 | +0.33 / +0.57 | both halves | 1e-04 |  |
| [[RBM42]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[UNK]] | +0.56 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[SIX5]] | +0.56 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[HOXC9]] | +0.55 | +0.37 / +0.47 | both halves | 9e-05 | same gene group |
| [[MAD2L1BP]] | +0.55 | +0.43 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRAP]] | -0.54 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[OPA1]] | -0.50 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[NUTF2]] | -0.50 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[GGCT]] | -0.49 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[AIF1L]] | -0.48 | -0.34 / -0.29 | both halves | 2e-04 |  |
| [[ATG16L1]] | -0.48 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[HSPD1]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[TPM3]] | -0.47 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[LPCAT1]] | -0.47 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[HSP90AB1]] | -0.47 | -0.40 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises HOXB2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HOXC10]] | B | HOXC10 activity raises HOXB2's level | lines that do not express HOXC10 (26) vs lines expressing it (24) | 1.66× lower at baseline in the lines without HOXC10 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: NTRK3, CES1, POTEE |
| [[HOXB-AS1]] | C | HOXB-AS1 activity raises HOXB2's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 2.84× lower at baseline in the lines without HOXB-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXC10]] | B | HOXB2 activity raises HOXC10's level | lines that do not express HOXB2 (21) vs lines expressing it (29) | 2.32× lower at baseline in the lines without HOXB2 | 0.066 | ⚠ within organs, on part of the lines; also absent: HOXB-AS1, SOX2, JAKMIP2-AS1 |
| [[TGFB3]] | B | HOXB2 activity raises TGFB3's level | lines that do not express HOXB2 (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without HOXB2 | 0.073 | ⚠ within organs, on part of the lines; also absent: HOXB-AS1, SOX2, JAKMIP2-AS1 |
| [[HOXB-AS1]] | C | HOXB2 activity raises HOXB-AS1's level | lines that do not express HOXB2 (21) vs lines expressing it (29) | 2.81× lower at baseline in the lines without HOXB2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: HOXB-AS1, SOX2, JAKMIP2-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.586). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-0.1, 24.9); signed map (19.6, -12.1). **Vector** length 34.6, 5.82% of its response variance represented; |z| ≥ 3 in 420 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.3 | +4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.3 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +2.2 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +10.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.2 | +3.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.2 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.1 | +2.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -1.4 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.3 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.2 | -5.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -0.7 | +0.7 |
|  | [[Rucaparib (phosphate) (drug)]] 5 µM |  | -0.7 | +0.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | homeobox B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,540,894-48,545,109 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX2, HOX2H |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Reactome | 2 pathways, smallest: Activation of HOX genes during differentiation; Activation of anterior HOX genes in hindbrain development during early embryogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P14652](https://www.uniprot.org/uniprotkb/P14652) (Homeobox protein Hox-B2):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3212](https://www.ncbi.nlm.nih.gov/gene/3212):

> This gene is a member of the Antp homeobox family and encodes a nuclear protein with a homeobox DNA-binding domain. It is included in a cluster of homeobox B genes located on chromosome 17. The encoded protein functions as a sequence-specific transcription factor that is involved in development. Increased expression of this gene is associated with pancreatic cancer. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5113](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5113) · Entrez [3212](https://www.ncbi.nlm.nih.gov/gene/3212) · UniProt [P14652](https://www.uniprot.org/uniprotkb/P14652) · Ensembl [ENSG00000173917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173917)

## Data

Gene col 10444: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10444); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10444, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10444]; `tensor/DDL_lfc|DDL_z.npy` [10444]; `embed/gene_vectors.npy` [10444]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10444 or target_col == 10444). Every well: [[HOXB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
