---
symbol: "PPIC"
type: "gene"
col: 9727
ensembl_id: "ENSG00000168938"
name: "peptidylprolyl isomerase C"
location: "5q23.2"
module: 29
arm: "+"
pooled_cpm: 12.4
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PPIC

*peptidylprolyl isomerase C* — 5q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.75× (z +13.4, q 2e-38, up in 34 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.65× (z +7.2, q 1e-10, up in 28 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.473× (z -10.8, q 3e-24, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL13RA1]] (+0.60, fdr 1e-05), [[PIGK]] (+0.59, fdr 4e-05), [[ITM2B]] (+0.57, fdr 2e-05); moves opposite to [[ZNF23]] (-0.55, fdr 4e-05), [[ZNF473]] (-0.51, fdr 1e-05), [[ZNF761]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9727.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +13.4 | 2e-38 | 34/34 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.60×** | +12.5 | 2e-33 | 20/22 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.75×** | +9.5 | 3e-19 | 26/29 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.2 | 1e-10 | 28/44 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.3 | 0.002 | 20/44 (SNU-423, A-427, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.004 | 22/46 (A-172, H4, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.46×** | +3.8 | 0.011 | 15/38 (J82, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.35× | +3.0 | 0.17 | 13/45 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9727.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.473×** | -10.8 | 3e-24 | 32/42 (Panc 03.27, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.534×** | -6.4 | 5e-08 | 26/42 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.398×** | -4.9 | 2e-04 | 28/44 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.636×** | -4.4 | 0.001 | 22/45 (SNU-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.696×** | -3.7 | 0.026 | 20/45 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.519×** | -3.5 | 0.046 | 17/42 (LoVo, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.547× | -3.2 | 0.11 | 13/46 (Hs 766T, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.806× | -3.1 | 0.13 | 16/45 (NCI-H2347, SHP-77, …) | rises with dose | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.725× | -3.1 | 0.13 | 13/46 (HS-578T, HCT15, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9727. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 25.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -12.5) |
| [[HS-578T (line)]] | alt | 26.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -9.8) |
| [[H4 (line)]] | wt | 12.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0724× (z -9.3) |
| [[HOP62 (line)]] | alt | 10.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.84× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 11.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.21× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 8.12 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.1) |
| [[PANC-1 (line)]] | alt | 19.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 13.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 19.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 18.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.65× (z +11.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -10.4) |
| [[HT-29 (line)]] | alt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -8.8) |
| [[J82 (line)]] | alt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -12.6) |
| [[LoVo (line)]] | wt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 7.72 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.8× (z +10.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 3.71 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.0675× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 9.01 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.26× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 9.14 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.262× (z -10.7) ⚠ cell-cycle shift, explains ~69% of this change |
| [[Panc 03.27 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -12.1) |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -11.8) |
| [[A-427 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9727), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL13RA1]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[PIGK]] | +0.59 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[ITM2B]] | +0.57 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[RPN2]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SUMF2]] | +0.53 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[PIGS]] | +0.53 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PDIA3]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ATRAID]] | +0.52 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[CST3]] | +0.51 | +0.55 / +0.33 | both halves | 1e-04 |  |
| [[SCARB2]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[PRKACA]] | +0.51 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[EMC7]] | +0.50 | +0.43 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF23]] | -0.55 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ZNF473]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ZNF761]] | -0.50 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[METAP2]] | -0.50 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[ZNF229]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ZNF765]] | -0.49 | -0.50 / -0.37 | both halves | 9e-05 |  |
| [[ZNF222]] | -0.47 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[NDUFB9]] | -0.46 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[MRPS2]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[TAF1A]] | -0.46 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[ESF1]] | -0.45 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[RSL1D1]] | -0.45 | -0.43 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PPIC's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.9, -20.6); signed map (-24.5, -38.0). **Vector** length 69.9, 13.6% of its response variance represented; |z| ≥ 3 in 708 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +13.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +12.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.2 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -6.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -4.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -2.1 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -1.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl isomerase C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.2 — chr5:123,023,250-123,036,725 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CYPC |
| Gene groups (HGNC) | Cyclophilin peptidylprolyl isomerases |
| Matched by | ensembl_id |

**Function**, from UniProt [P45877](https://www.uniprot.org/uniprotkb/P45877) (Peptidyl-prolyl cis-trans isomerase C):

> PPIase that catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and may therefore assist protein folding.

**Summary**, from NCBI Gene [5480](https://www.ncbi.nlm.nih.gov/gene/5480):

> The protein encoded by this gene is a member of the peptidyl-prolyl cis-trans isomerase (PPIase)) family. PPIases catalyze the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and accelerate the folding of proteins. Similar to other PPIases, this protein can bind immunosuppressant cyclosporin A. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9256](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9256) · Entrez [5480](https://www.ncbi.nlm.nih.gov/gene/5480) · UniProt [P45877](https://www.uniprot.org/uniprotkb/P45877) · Ensembl [ENSG00000168938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168938)

## Data

Gene col 9727: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9727); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9727, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9727]; `tensor/DDL_lfc|DDL_z.npy` [9727]; `embed/gene_vectors.npy` [9727]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9727 or target_col == 9727). Every well: [[PPIC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
