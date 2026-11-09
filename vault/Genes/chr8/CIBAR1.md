---
symbol: "CIBAR1"
type: "gene"
col: 12007
ensembl_id: "ENSG00000188343"
name: "CBY1 interacting BAR domain containing 1"
location: "8q22.1"
module: 190
arm: "+"
pooled_cpm: 17.1
n_lines_expressing: 46
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# CIBAR1

*CBY1 interacting BAR domain containing 1* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.30× (z +11.8, q 4e-29, up in 34 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.41× (z +6.8, q 1e-09, up in 28 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Capmatinib (drug)]] 0.05 µM in 1 line (NCI-H661 0.0658×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.385×); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (NCI-H661 0.0880×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYSMD2]] (+0.61, fdr 1e-05), [[HSF2]] (+0.59, fdr 1e-05), [[WWP1]] (+0.58, fdr 1e-05); moves opposite to [[CYTH2]] (-0.53, fdr 1e-05), [[SAP30BP]] (-0.52, fdr 1e-05), [[SEC16A]] (-0.51, fdr 2e-05).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF618]] → it (grade B ⚠); 2 go from it, the strongest it → [[RWDD3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12007.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.30×** | +11.8 | 4e-29 | 34/39 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.11×** | +10.2 | 8e-22 | 20/28 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +6.8 | 1e-09 | 28/44 (SNU-423, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +6.1 | 1e-07 | 29/40 (RKO, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.56×** | +5.8 | 8e-07 | 18/31 (LoVo, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.47×** | +5.5 | 4e-06 | 25/43 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +5.4 | 4e-06 | 23/43 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +5.0 | 4e-05 | 21/40 (NCI-H460, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.0 | 4e-05 | 25/43 (SW 900, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +4.5 | 5e-04 | 18/43 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.001 | 17/44 (RKO, C-33 A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.1 | 0.002 | 13/35 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.31×** | +3.7 | 0.010 | 16/43 (C-33 A, A-427, …) | top dose only | composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.012 | 15/43 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.025 | 8/44 (HS-578T, NCI-H1792, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +3.1 | 0.058 | 7/44 (PANC-1, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.081 | 11/44 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12007.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Capmatinib (drug)]] 0.05 µM in 1 line (NCI-H661 0.0658×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.385×); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (NCI-H661 0.0880×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.911× | -4.5 | 0.004 | 4/44 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H661 (line)]] | alt | 44.7 | 0 | 2 | — | [[Capmatinib (drug)]] 0.05 µM 0.0658× (z -9.8) |
| [[A-427 (line)]] | wt | 21.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.385× (z -9.6) |
| [[LoVo (line)]] | wt | 14.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 13.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.76× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.185× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~63% of this change |
| [[SW1417 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 26.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYSMD2]] | +0.61 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[HSF2]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[WWP1]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TMEM38B]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[GNPDA2]] | +0.58 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[NAA16]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[IRAK1BP1]] | +0.58 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[SNX4]] | +0.57 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[RAVER2]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[SLC18B1]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TPD52L1]] | +0.56 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[RNF2]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYTH2]] | -0.53 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[SAP30BP]] | -0.52 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[SEC16A]] | -0.51 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[ZKSCAN5]] | -0.50 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ADAMTSL4-AS2]] | -0.49 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[THUMPD3-AS1]] | -0.49 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[DNAH1]] | -0.49 | -0.37 / -0.49 | both halves | 7e-05 |  |
| [[ZNF597]] | -0.47 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[ARMC5]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[POLG]] | -0.47 | -0.54 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF618]] | B | ZNF618 activity raises CIBAR1's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 2.55× lower at baseline in the lines without ZNF618 | 0.007 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |
| [[LRP3]] | B | LRP3 activity raises CIBAR1's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 2.44× lower at baseline in the lines without LRP3 | 0.040 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[LRP12]] | C | LRP12 activity raises CIBAR1's level | lines that do not express LRP12 (8) vs lines expressing it (42) | 2.52× lower at baseline in the lines without LRP12 | 0.047 | ⚠ within organs, on part of the lines; also absent: CFAP54, RNF217, RNF217-AS1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RWDD3]] | C | CIBAR1 activity raises RWDD3's level | lines that do not express CIBAR1 (4) vs lines expressing it (46) | 1.33× lower at baseline in the lines without CIBAR1 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: CLTCL1, SPIRE1, ZNF480; maybe low, not absent; its own permutation p |
| [[LRP12]] | C | CIBAR1 activity raises LRP12's level | lines that do not express CIBAR1 (4) vs lines expressing it (46) | 6.92× lower at baseline in the lines without CIBAR1 | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: CLTCL1, SPIRE1, ZNF480; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.3, -8.6); signed map (-29.8, -17.1). **Vector** length 59.0, 9.92% of its response variance represented; |z| ≥ 3 in 639 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.3 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.3 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +2.6 | +10.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | +0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | +1.0 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | CBY1 interacting BAR domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:93,698,561-93,731,527 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38979, BARMR1; previously FAM92A1, FAM92A |
| Matched by | ensembl_id |

**Function**, from UniProt [A1XBS5](https://www.uniprot.org/uniprotkb/A1XBS5) (CBY1-interacting BAR domain-containing protein 1):

> Plays a critical role in regulating mitochondrial ultrastructure and function by maintaining the integrity of mitochondrial morphology, particularly the organization of cristae. Preferentially binds to negatively charged phospholipids like cardiolipin and phosphatidylinositol 4,5-bisphosphate enhancing its interaction with mitochondrial membranes. Induces membrane curvature and tubulation, which are critical for maintaining mitochondrial ultrastructure and the organization of cristae. Plays a …

**Summary**, from NCBI Gene [137392](https://www.ncbi.nlm.nih.gov/gene/137392):

> Enables phospholipid binding activity. Involved in several processes, including inner mitochondrial membrane organization; limb morphogenesis; and membrane tubulation. Located in several cellular components, including centriole; ciliary base; and mitochondrial crista. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30452) · Entrez [137392](https://www.ncbi.nlm.nih.gov/gene/137392) · UniProt [A1XBS5](https://www.uniprot.org/uniprotkb/A1XBS5) · Ensembl [ENSG00000188343](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188343)

## Data

Gene col 12007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12007); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12007]; `tensor/DDL_lfc|DDL_z.npy` [12007]; `embed/gene_vectors.npy` [12007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12007 or target_col == 12007). Every well: [[CIBAR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIBAR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
