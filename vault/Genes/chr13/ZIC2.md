---
symbol: "ZIC2"
type: "gene"
col: 495
ensembl_id: "ENSG00000043355"
name: "Zic family zinc finger 2"
location: "13q32.3"
module: 20
arm: "-"
pooled_cpm: 7.04
n_lines_expressing: 40
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ZIC2

*Zic family zinc finger 2* — 13q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +7.2, q 2e-10, up in 21 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 10.2×, HS-578T 7.49×; ⚠ cell-cycle shift, explains ~98% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HS-578T 9.45×; ⚠ cell-cycle shift, explains ~67% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 5.08×).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.420× (z -9.1, q 5e-17, down in 25 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXC8]] (+0.68, fdr 2e-05), [[GLIS2]] (+0.68, fdr 9e-06), [[BCOR]] (+0.67, fdr 9e-06); moves opposite to [[OPA1]] (-0.60, fdr 2e-05), [[API5]] (-0.57, fdr 4e-05), [[NAPG]] (-0.57, fdr 2e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HOXC6]] → it (grade B ⚠); 4 go from it, the strongest it → [[HOXC9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 495.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 10.2×, HS-578T 7.49×; ⚠ cell-cycle shift, explains ~98% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HS-578T 9.45×; ⚠ cell-cycle shift, explains ~67% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 5.08×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +7.2 | 2e-10 | 21/35 (A549, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.48×** | +5.6 | 5e-06 | 16/32 (COLO 205, HS-578T, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.4 | 2e-05 | 16/27 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.53×** | +4.5 | 0.001 | 12/29 (SW1417, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.50×** | +4.3 | 0.002 | 16/36 (SW480, LoVo, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.1 | 0.004 | 11/32 (SNU-423, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.41×** | +3.6 | 0.024 | 13/37 (LOX-IMVI, HS-578T, …) | two highest doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.051 | 7/37 (LoVo, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.36×** | +3.2 | 0.081 | 11/33 (HS-578T, SNU-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | 1.24× | +3.0 | 0.12 | 8/37 (PANC-1, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Omeprazole (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.12 | 6/37 (AsPC-1, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.05 µM |  | 1.35× | +3.0 | 0.12 | 5/37 (J82, C-33 A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 495.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.420×** | -9.1 | 5e-17 | 25/37 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.427×** | -8.9 | 1e-16 | 23/37 (Hs 766T, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.582×** | -5.7 | 3e-06 | 22/37 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.608×** | -4.9 | 1e-04 | 18/37 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.666×** | -4.3 | 0.002 | 16/37 (SW 900, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.676×** | -4.1 | 0.004 | 14/37 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.895× | -4.0 | 0.004 | 6/38 (COLO 205, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 495. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 6.96 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +11.4) ⚠ cell-cycle shift, explains ~98% of this change | — |
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -9.5) |
| [[A549 (line)]] | wt | 5.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0728× (z -8.7) |
| [[COLO 205 (line)]] | alt | 12.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +13.0) ⚠ cell-cycle shift, explains ~98% of this change | — |
| [[Hs 766T (line)]] | wt | 8.80 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -8.6) |
| [[J82 (line)]] | alt | 14.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -10.1) |
| [[A-172 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.690 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.468 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 495), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXC8]] | +0.68 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[GLIS2]] | +0.68 | +0.75 / +0.57 | both halves | 9e-06 | same gene group |
| [[BCOR]] | +0.67 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[ERF]] | +0.63 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[IRX5]] | +0.62 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ATP23]] | +0.60 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[YY1]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 | same gene group |
| [[FBXL14]] | +0.59 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[RSBN1]] | +0.59 | +0.37 / +0.66 | both halves | 8e-05 |  |
| [[HOXC10]] | +0.59 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[POLR1H]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[HOXC9]] | +0.59 | +0.38 / +0.51 | both halves | 6e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPA1]] | -0.60 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[API5]] | -0.57 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[NAPG]] | -0.57 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[USP14]] | -0.57 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[EIF3H]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.55 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.54 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[RTF2]] | -0.53 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[CAPZB]] | -0.52 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[ASCC2]] | -0.51 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[RPRD1A]] | -0.51 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[TTC14]] | -0.51 | -0.57 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXC6]] | B | HOXC6 activity raises ZIC2's level | lines that do not express HOXC6 (10) vs lines expressing it (40) | 1.92× lower at baseline in the lines without HOXC6 | 0.026 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC8, FLJ12825; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises ZIC2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises ZIC2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXC9]] | B | ZIC2 activity raises HOXC9's level | lines that do not express ZIC2 (10) vs lines expressing it (40) | 1.82× lower at baseline in the lines without ZIC2 | 0.060 | ⚠ within organs, on part of the lines; also absent: FOXD1, BEND7 |
| [[SLC41A1]] | B | ZIC2 activity raises SLC41A1's level | lines that do not express ZIC2 (10) vs lines expressing it (40) | 1.38× lower at baseline in the lines without ZIC2 | 0.089 | ⚠ within organs, on part of the lines; also absent: FOXD1, BEND7 |
| [[HOXC6]] | B | ZIC2 activity raises HOXC6's level | lines that do not express ZIC2 (10) vs lines expressing it (40) | 1.58× lower at baseline in the lines without ZIC2 | 0.091 | ⚠ within organs, on part of the lines; also absent: FOXD1, BEND7 |
| [[HOXC8]] | B | ZIC2 activity raises HOXC8's level | lines that do not express ZIC2 (10) vs lines expressing it (40) | 1.68× lower at baseline in the lines without ZIC2 | 0.094 | ⚠ within organs, on part of the lines; also absent: FOXD1, BEND7 |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.422). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (22.0, -3.5); signed map (-3.3, 12.7). **Vector** length 60.9, 11.0% of its response variance represented; |z| ≥ 3 in 637 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | +3.1 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.0 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.0 | -2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.3 | -4.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.0 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -0.8 | -0.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -0.8 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | Zic family zinc finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.3 — chr13:99,981,784-99,986,765 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HPE5 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZIC family zinc fingers |
| Reactome | 2 pathways, smallest: Formation of the anterior neural plate; Gastrulation |
| Matched by | ensembl_id |

**Function**, from UniProt [O95409](https://www.uniprot.org/uniprotkb/O95409) (Zinc finger protein ZIC 2):

> Acts as a transcriptional activator or repressor. Plays important roles in the early stage of organogenesis of the CNS. Activates the transcription of the serotonin transporter SERT in uncrossed ipsilateral retinal ganglion cells (iRGCs) to refine eye-specific projections in primary visual targets. Its transcriptional activity is repressed by MDFIC. Involved in the formation of the ipsilateral retinal projection at the optic chiasm midline. Drives the expression of EPHB1 on ipsilaterally …

**Summary**, from NCBI Gene [7546](https://www.ncbi.nlm.nih.gov/gene/7546):

> This gene encodes a member of the ZIC family of C2H2-type zinc finger proteins. This protein functions as a transcriptional repressor and may regulate tissue specific expression of dopamine receptor D1. Expansion of an alanine repeat in the C-terminus of the encoded protein and other mutations in this gene cause holoprosencephaly type 5. Holoprosencephaly is the most common structural anomaly of the human brain. A polyhistidine tract polymorphism in this gene may be associated with increased …

**Accessions** — [HGNC:12873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12873) · Entrez [7546](https://www.ncbi.nlm.nih.gov/gene/7546) · UniProt [O95409](https://www.uniprot.org/uniprotkb/O95409) · Ensembl [ENSG00000043355](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000043355)

## Data

Gene col 495: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 495); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 495, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 495]; `tensor/DDL_lfc|DDL_z.npy` [495]; `embed/gene_vectors.npy` [495]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 495 or target_col == 495). Every well: [[ZIC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZIC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
