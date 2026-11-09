---
symbol: "TIGD7"
type: "gene"
col: 6476
ensembl_id: "ENSG00000140993"
name: "tigger transposable element derived 7"
location: "16p13.3"
module: 15
arm: "+"
pooled_cpm: 7.07
n_lines_expressing: 41
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TIGD7

*tigger transposable element derived 7* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.81× (z +9.9, q 4e-20, up in 25 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.660× (z -6.7, q 2e-08, down in 18 of 37 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPN10-DT]] (+0.60, fdr 3e-05), [[ZNF460-AS1]] (+0.59, fdr 6e-05), [[ZKSCAN2-DT]] (+0.58, fdr 1e-04); moves opposite to [[HNRNPDL]] (-0.52, fdr 6e-04), [[CEP63]] (-0.46, fdr 5e-05), [[FIBP]] (-0.46, fdr 0.004, ⚠ not reproduced), [[COTL1]] (-0.46, fdr 4e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF790]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNF595]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6476.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +9.9 | 4e-20 | 25/38 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +7.0 | 9e-10 | 17/30 (HOP62, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.9 | 1e-09 | 8/39 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.5 | 9e-04 | 9/37 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.0 | 0.006 | 8/39 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.24×** | +3.3 | 0.085 | 5/18 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.085 | 4/38 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.095 | 6/37 (NCI-H23, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.14 | 6/34 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.14× | +3.0 | 0.14 | 6/38 (NCI-H2347, A-172, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6476.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.660×** | -6.7 | 2e-08 | 18/37 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.690×** | -6.2 | 2e-07 | 12/37 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.775×** | -6.0 | 3e-07 | 18/35 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.724×** | -5.4 | 1e-05 | 13/34 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.737×** | -5.1 | 3e-05 | 12/38 (LoVo, BT-474, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.737×** | -5.1 | 3e-05 | 14/28 (A549, SNU-423, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.620×** | -4.2 | 0.002 | 10/38 (MIA PaCa-2, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.802×** | -3.7 | 0.016 | 7/39 (SNU-423, C32, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.808×** | -3.6 | 0.023 | 7/33 (AsPC-1, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Diphenhydramine (drug)]] 5 µM |  | **0.805×** | -3.5 | 0.028 | 3/38 (AsPC-1, AN3 CA, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.869× | -3.3 | 0.044 | 6/38 (AsPC-1, H4, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.829×** | -3.1 | 0.080 | 6/38 (AN3 CA, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.700×** | -3.1 | 0.081 | 8/32 (C32, A-172, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.829× | -3.0 | 0.10 | 6/38 (PANC-1, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6476. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 15.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -13.6) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -9.4) |
| [[H4 (line)]] | wt | 12.2 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0800× (z -9.8) |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.2) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.297× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.746 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.905 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6476), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 17 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN10-DT]] | +0.60 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ZNF460-AS1]] | +0.59 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[ZKSCAN2-DT]] | +0.58 | +0.33 / +0.66 | both halves | 1e-04 |  |
| [[TMEM11-DT]] | +0.58 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[ANKRD42-DT]] | +0.58 | +0.36 / +0.51 | both halves | 9e-05 |  |
| [[PCF11-AS1]] | +0.58 | +0.28 / +0.51 | both halves | 3e-04 |  |
| [[GLUD1P3]] | +0.55 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[ZNF529-AS1]] | +0.55 | +0.24 / +0.57 | both halves | 4e-04 |  |
| [[ZNF394]] | +0.54 | +0.29 / +0.51 | both halves | 2e-04 |  |
| [[C2orf42]] | +0.53 | +0.41 / +0.35 | both halves | 1e-04 |  |
| [[DOCK7-DT]] | +0.53 | +0.37 / +0.39 | both halves | 9e-05 |  |
| [[ZBTB8OS]] | +0.53 | +0.38 / +0.41 | both halves | 7e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPDL]] | -0.52 | -0.23 / -0.39 | both halves | 6e-04 |  |
| [[CEP63]] | -0.46 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[FIBP]] | -0.46 | -0.46 / -0.07 | ⚠ not reproduced | 0.004 |  |
| [[COTL1]] | -0.46 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[CCDC85C]] | -0.45 | -0.30 / -0.25 | both halves | 4e-04 |  |
| [[ARHGDIA]] | -0.44 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[CSRP1]] | -0.44 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[INF2]] | -0.44 | -0.30 / -0.27 | both halves | 3e-04 |  |
| [[ACTR1B]] | -0.43 | -0.30 / -0.26 | both halves | 4e-04 |  |
| [[TTLL12]] | -0.43 | -0.13 / -0.38 | ⚠ not reproduced | 0.002 |  |
| [[CCDC6]] | -0.43 | -0.33 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF790]] | B | ZNF790 activity raises TIGD7's level | lines that do not express ZNF790 (14) vs lines expressing it (36) | 2.21× lower at baseline in the lines without ZNF790 | 0.064 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF606, ZNF569 |
| [[ZNF345]] | B | ZNF345 activity raises TIGD7's level | lines that do not express ZNF345 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without ZNF345 | 0.093 | ⚠ within organs, on part of the lines; also absent: ZNF790, DNAH14, ZNF606 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF595]] | C | TIGD7 activity raises ZNF595's level | lines that do not express TIGD7 (9) vs lines expressing it (41) | 5.78× lower at baseline in the lines without TIGD7 | 0.073 | ⚠ within organs, on part of the lines; also absent: SIX1, MSN, HDGFL3; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.559). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.3, 24.0); signed map (1.1, -1.7). **Vector** length 41.0, 4.56% of its response variance represented; |z| ≥ 3 in 818 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.0 | +9.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +1.8 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +4.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.9 | +1.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.5 | -1.0 |
|  | [[Infigratinib (drug)]] 5 µM |  | +0.5 | +1.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -2.4 | -6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -2.1 | -5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.6 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -1.4 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.8 | -3.1 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.7 | -1.8 |
|  | [[Artemether (drug)]] 0.05 µM |  | -0.7 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -0.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | tigger transposable element derived 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,298,808-3,305,729 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Sancho |
| Gene groups (HGNC) | Helix-turn-helix CENPB type domain family |
| Matched by | ensembl_id |

UniProt [Q6NT04](https://www.uniprot.org/uniprotkb/Q6NT04) carries no function annotation.

**Summary**, from NCBI Gene [91151](https://www.ncbi.nlm.nih.gov/gene/91151):

> The protein encoded by this gene belongs to the tigger subfamily of the pogo superfamily of DNA-mediated transposons in humans. These proteins are related to DNA transposons found in fungi and nematodes, and more distantly to the Tc1 and mariner transposases. They are also very similar to the major mammalian centromere protein B. The exact function of this gene is not known. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18331](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18331) · Entrez [91151](https://www.ncbi.nlm.nih.gov/gene/91151) · UniProt [Q6NT04](https://www.uniprot.org/uniprotkb/Q6NT04) · Ensembl [ENSG00000140993](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140993)

## Data

Gene col 6476: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6476); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6476, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6476]; `tensor/DDL_lfc|DDL_z.npy` [6476]; `embed/gene_vectors.npy` [6476]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6476 or target_col == 6476). Every well: [[TIGD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIGD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
