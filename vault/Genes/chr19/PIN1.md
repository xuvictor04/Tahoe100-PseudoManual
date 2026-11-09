---
symbol: "PIN1"
type: "gene"
col: 4810
ensembl_id: "ENSG00000127445"
name: "peptidylprolyl cis/trans isomerase, NIMA-interacting 1"
location: "19p13"
module: 3
arm: "+"
pooled_cpm: 20.32
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PIN1

*peptidylprolyl cis/trans isomerase, NIMA-interacting 1* — 19p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.17× (z +10.6, q 2e-23, up in 40 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 4.80×, SW480 4.47×, SNU-423 4.47×, NCI-H1573 6.88×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 4.52×, PANC-1 4.08×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.745× (z -3.8, q 0.041, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCTN3]] (+0.67, fdr 3e-05), [[NDUFS7]] (+0.67, fdr 3e-05), [[SLC25A11]] (+0.66, fdr 1e-04); moves opposite to [[NCR3LG1]] (-0.68, fdr 1e-05), [[SNHG26]] (-0.66, fdr 6e-05), [[DPH5-DT]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SNHG26]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4810.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 4.80×, SW480 4.47×, SNU-423 4.47×, NCI-H1573 6.88×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 4.52×, PANC-1 4.08×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **3.17×** | +10.6 | 2e-23 | 40/42 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.80×** | +9.1 | 2e-17 | 33/35 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.21×** | +7.3 | 6e-11 | 45/48 (HOP62, HEC-1-A, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.03×** | +6.5 | 1e-08 | 44/48 (LS 180, SW480, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.11×** | +6.3 | 3e-08 | 30/37 (NCI-H2030, A549, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.86×** | +5.7 | 1e-06 | 43/47 (HOP62, LoVo, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.68×** | +4.8 | 1e-04 | 27/45 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.2 | 0.002 | 26/43 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.52×** | +3.7 | 0.013 | 24/48 (SNU-423, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4810.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.745×** | -3.8 | 0.041 | 26/47 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.633×** | -3.8 | 0.041 | 25/47 (Panc 03.27, HEC-1-A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.433×** | -3.7 | 0.041 | 27/46 (LS 180, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.489× | -3.2 | 0.22 | 19/46 (H4, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.505× | -3.0 | 0.28 | 14/48 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4810. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A-172 (line)]] | wt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A-427 (line)]] | wt | 28.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -8.8) |
| [[A498 (line)]] | wt | 18.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[HCT15 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.40× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H1573 (line)]] | alt | 9.66 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.88× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SNU-423 (line)]] | alt | 30.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SW480 (line)]] | alt | 22.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A549 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4810), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN3]] | +0.67 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[NDUFS7]] | +0.67 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[SLC25A11]] | +0.66 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[BAD]] | +0.65 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[ANAPC11]] | +0.65 | +0.36 / +0.59 | both halves | 1e-04 |  |
| [[DHTKD1]] | +0.64 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[METTL26]] | +0.64 | +0.25 / +0.53 | both halves | 4e-04 |  |
| [[TMEM256]] | +0.63 | +0.38 / +0.48 | both halves | 7e-05 |  |
| [[YIF1B]] | +0.63 | +0.34 / +0.43 | both halves | 1e-04 |  |
| [[ARL3]] | +0.63 | +0.32 / +0.49 | both halves | 2e-04 |  |
| [[KIAA1328]] | +0.63 | +0.32 / +0.44 | both halves | 2e-04 |  |
| [[CABIN1]] | +0.63 | +0.40 / +0.47 | both halves | 5e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCR3LG1]] | -0.68 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[SNHG26]] | -0.66 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[DPH5-DT]] | -0.62 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[SPTY2D1OS]] | -0.60 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[WNT3]] | -0.59 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[MCPH1]] | -0.58 | -0.34 / -0.29 | both halves | 2e-04 |  |
| [[ZC3H4]] | -0.57 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[GABPB1-AS1]] | -0.57 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[ZNF300]] | -0.57 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[SLC16A1-AS1]] | -0.57 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[UTP20]] | -0.57 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[FRG1-DT]] | -0.56 | -0.38 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG26]] | B | SNHG26 activity raises PIN1's level | lines that do not express SNHG26 (11) vs lines expressing it (39) | 1.36× lower at baseline in the lines without SNHG26 | 0.020 | ⚠ within organs, on part of the lines; also absent: HEG1, GPR63, FAM171A1 |
| [[HDAC6]] | B | HDAC6 activity lowers PIN1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SLC2A9]] | B | SLC2A9 activity lowers PIN1's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.35× higher at baseline in the lines without SLC2A9 | 0.094 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.5, -14.0); signed map (-34.3, 15.9). **Vector** length 49.2, 9.52% of its response variance represented; |z| ≥ 3 in 623 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.0 | +5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.9 | +7.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.8 | +6.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +2.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +0.9 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | -3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +1.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | +0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl cis/trans isomerase, NIMA-interacting 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13 — chr19:9,835,257-9,849,689 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dod |
| Gene groups (HGNC) | Parvulins |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 16 pathways, smallest: PI5P Regulates TP53 Acetylation; RHO GTPases Activate NADPH Oxidases; Regulation of TP53 Activity through Acetylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13526](https://www.uniprot.org/uniprotkb/Q13526) (Peptidyl-prolyl cis-trans isomerase NIMA-interacting 1):

> Peptidyl-prolyl cis/trans isomerase (PPIase) that binds to and isomerizes specific phosphorylated Ser/Thr-Pro (pSer/Thr-Pro) motifs. By inducing conformational changes in a subset of phosphorylated proteins, acts as a molecular switch in multiple cellular processes. Displays a preference for acidic residues located N-terminally to the proline bond to be isomerized. Regulates mitosis presumably by interacting with NIMA and attenuating its mitosis-promoting activity. Down-regulates kinase …

**Summary**, from NCBI Gene [5300](https://www.ncbi.nlm.nih.gov/gene/5300):

> Peptidyl-prolyl cis/trans isomerases (PPIases) catalyze the cis/trans isomerization of peptidyl-prolyl peptide bonds. This gene encodes one of the PPIases, which specifically binds to phosphorylated ser/thr-pro motifs to catalytically regulate the post-phosphorylation conformation of its substrates. The conformational regulation catalyzed by this PPIase has a profound impact on key proteins involved in the regulation of cell growth, genotoxic and other stress responses, the immune response, …

**Accessions** — [HGNC:8988](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8988) · Entrez [5300](https://www.ncbi.nlm.nih.gov/gene/5300) · UniProt [Q13526](https://www.uniprot.org/uniprotkb/Q13526) · Ensembl [ENSG00000127445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127445)

## Data

Gene col 4810: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4810); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4810, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4810]; `tensor/DDL_lfc|DDL_z.npy` [4810]; `embed/gene_vectors.npy` [4810]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4810 or target_col == 4810). Every well: [[PIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
