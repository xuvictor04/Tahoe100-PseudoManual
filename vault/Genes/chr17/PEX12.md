---
symbol: "PEX12"
type: "gene"
col: 2989
ensembl_id: "ENSG00000108733"
name: "peroxisomal biogenesis factor 12"
location: "17q12"
module: 12
arm: "+"
pooled_cpm: 3.0
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PEX12

*peroxisomal biogenesis factor 12* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +7.9, q 1e-12, up in 20 of 35 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.20× (z +6.9, q 1e-09, up in 25 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.425× (z -7.5, q 3e-11, down in 28 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf131]] (+0.81, fdr 7e-06), [[CCDC174]] (+0.81, fdr 7e-06), [[PHAX]] (+0.80, fdr 7e-06); moves opposite to [[BCAP31]] (-0.68, fdr 7e-06), [[GRK6]] (-0.64, fdr 1e-05), [[TPST2]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNF830]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2989.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.89×** | +7.9 | 1e-12 | 20/35 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.20×** | +6.9 | 1e-09 | 25/33 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.69×** | +6.5 | 1e-08 | 16/44 (KATO III, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.14×** | +6.4 | 2e-08 | 21/39 (SK-MEL-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.06×** | +6.4 | 2e-08 | 23/45 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +4.0 | 0.005 | 14/42 (A498, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +3.8 | 0.011 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.80×** | +3.7 | 0.015 | 4/17 (A-172, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.51×** | +3.6 | 0.017 | 4/40 (LoVo, HOP62, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.49×** | +3.5 | 0.026 | 5/18 (LOX-IMVI, A498, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.04×** | +3.3 | 0.051 | 4/31 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.2 | 0.065 | 2/47 (HOP62, NCI-H23) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2989.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.425×** | -7.5 | 3e-11 | 28/43 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.502×** | -6.1 | 3e-07 | 25/45 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.534×** | -5.5 | 6e-06 | 23/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.567×** | -5.0 | 8e-05 | 17/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.558×** | -4.9 | 9e-05 | 14/23 (SW1417, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.602×** | -4.5 | 7e-04 | 18/45 (LS 180, RPMI-7951, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.618×** | -4.2 | 0.002 | 15/42 (J82, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.667×** | -3.6 | 0.026 | 13/44 (A-172, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.677×** | -3.4 | 0.037 | 13/42 (SK-MEL-2, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.701×** | -3.1 | 0.095 | 15/28 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.702×** | -3.1 | 0.095 | 15/45 (COLO 205, KATO III, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2989. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.69 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0502× (z -12.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 4.04 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.142× (z -8.6) |
| [[A549 (line)]] | wt | 3.22 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 5 µM 0.0623× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 5.68 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0792× (z -10.2) |
| [[PANC-1 (line)]] | alt | 3.99 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0922× (z -11.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 3.70 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0708× (z -12.5) |
| [[A-427 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2989), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf131]] | +0.81 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.81 | +0.81 / +0.72 | both halves | 7e-06 |  |
| [[PHAX]] | +0.80 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.80 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[ZNF585A]] | +0.79 | +0.83 / +0.65 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.79 | +0.81 / +0.75 | both halves | 7e-06 |  |
| [[METTL18]] | +0.78 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[CLK4]] | +0.78 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.77 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.77 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[COIL]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[STK16]] | +0.75 | +0.79 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | -0.68 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[GRK6]] | -0.64 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[TPST2]] | -0.64 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[NUTF2]] | -0.64 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[FAM20B]] | -0.64 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[TSPAN17]] | -0.64 | -0.72 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PEX12's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF830]] | C | PEX12's natural level strengthens ZNF830's drug response | PEX12's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.22; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.794). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-33.3, 4.6); signed map (4.1, -20.5). **Vector** length 60.7, 9.09% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.5 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.5 | +6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.8 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -5.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.3 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -0.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:35,574,795-35,578,863 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Peroxins; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 5 pathways, smallest: Class I peroxisomal membrane protein import; E3 ubiquitin ligases ubiquitinate target proteins; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [O00623](https://www.uniprot.org/uniprotkb/O00623) (Peroxisome assembly protein 12):

> Component of a retrotranslocation channel required for peroxisome organization by mediating export of the PEX5 receptor from peroxisomes to the cytosol, thereby promoting PEX5 recycling. The retrotranslocation channel is composed of PEX2, PEX10 and PEX12; each subunit contributing transmembrane segments that coassemble into an open channel that specifically allows the passage of PEX5 through the peroxisomal membrane (By similarity). PEX12 also regulates PEX5 recycling by activating the E3 …

**Summary**, from NCBI Gene [5193](https://www.ncbi.nlm.nih.gov/gene/5193):

> This gene belongs to the peroxin-12 family. Peroxins (PEXs) are proteins that are essential for the assembly of functional peroxisomes. The peroxisome biogenesis disorders (PBDs) are a group of genetically heterogeneous autosomal recessive, lethal diseases characterized by multiple defects in peroxisome function. The peroxisomal biogenesis disorders are a heterogeneous group with at least 14 complementation groups and with more than 1 phenotype being observed in cases falling into particular …

**Accessions** — [HGNC:8854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8854) · Entrez [5193](https://www.ncbi.nlm.nih.gov/gene/5193) · UniProt [O00623](https://www.uniprot.org/uniprotkb/O00623) · Ensembl [ENSG00000108733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108733)

## Data

Gene col 2989: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2989); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2989, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2989]; `tensor/DDL_lfc|DDL_z.npy` [2989]; `embed/gene_vectors.npy` [2989]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2989 or target_col == 2989). Every well: [[PEX12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
