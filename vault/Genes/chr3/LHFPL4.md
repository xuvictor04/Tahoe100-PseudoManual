---
symbol: "LHFPL4"
type: "gene"
col: 8027
ensembl_id: "ENSG00000156959"
name: "LHFPL tetraspan subfamily member 4"
location: "3p25.3"
module: 16
arm: "+"
pooled_cpm: 7.26
n_lines_expressing: 17
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# LHFPL4

*LHFPL tetraspan subfamily member 4* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.43× (z +14.3, q 1e-43, up in 1 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.684× (z -4.4, q 0.008, down in 2 of 14 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Rutin (trihydrate) (drug)]] 0.05 µM: 0.718× (z -3.5, q 0.091, down in 0 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H2347 0.193×, NCI-H23 0.216×, C-33 A 0.261×, Panc 03.27 0.313×, …); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (C-33 A 0.129×, A-427 0.179×, NCI-H23 0.195×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.0575×, NCI-H23 0.122×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0512×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CERS4]] (+0.55, fdr 4e-05), [[GMEB2]] (+0.53, fdr 6e-05), [[ZSCAN18]] (+0.53, fdr 2e-05); moves opposite to [[RECQL]] (-0.42, fdr 1e-04), [[ADAM10]] (-0.41, fdr 2e-04), [[FAM120A]] (-0.41, fdr 1e-04).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[PAPLN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8027.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +14.3 | 1e-43 | 1/15 (RPMI-7951) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +12.1 | 5e-31 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +9.9 | 6e-21 | 1/10 (A549) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.12×** | +8.3 | 1e-14 | 2/14 (SW 900, RPMI-7951) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +7.2 | 5e-11 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +7.0 | 2e-10 | 8/14 (HOP62, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +6.2 | 5e-08 | 3/13 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +5.4 | 4e-06 | 4/13 (RKO, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.18×** | +4.6 | 2e-04 | 1/5 (C-33 A) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 7e-04 | 9/14 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.9 | 0.005 | 1/11 (SW 1271) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +3.8 | 0.008 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.010 | 0/14 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.028 | 1/14 (HOP62) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.48×** | +3.2 | 0.056 | 2/10 (NCI-H1792, NCI-H23) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.056 | 4/14 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.092 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.096 | 1/13 (NCI-H1792) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +2.9 | 0.096 | 1/14 (A-427) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.43×** | +2.9 | 0.096 | 0/13 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8027.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H2347 0.193×, NCI-H23 0.216×, C-33 A 0.261×, Panc 03.27 0.313×, …); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (C-33 A 0.129×, A-427 0.179×, NCI-H23 0.195×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.0575×, NCI-H23 0.122×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0512×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.684×** | -4.4 | 0.008 | 2/14 (Panc 03.27, SW 900) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.718×** | -3.5 | 0.091 | 0/14 | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.729×** | -3.5 | 0.091 | 7/14 (NCI-H23, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8027. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 62.9 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -18.2) |
| [[C-33 A (line)]] | alt | 68.0 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0575× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -13.8) |
| [[A-427 (line)]] | wt | 68.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -16.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 46.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -18.3) |
| [[HOP62 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.202× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 3.17 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0512× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 15.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -8.7) |
| [[RKO (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -8.5) |
| [[A-172 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.871 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.890 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.951 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.983 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.860 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.938 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.983 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8027), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CERS4]] | +0.55 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[GMEB2]] | +0.53 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[ZSCAN18]] | +0.53 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[APBB1]] | +0.52 | +0.32 / +0.53 | both halves | 1e-04 |  |
| [[LINC01203]] | +0.51 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[SRSF12]] | +0.51 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[THUMPD2]] | +0.51 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[ZNF790-AS1]] | +0.50 | +0.40 / +0.58 | both halves | 4e-05 |  |
| [[ZNF793]] | +0.49 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[EPHA5-AS1]] | +0.48 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[MMRN1]] | +0.47 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ZNF134]] | +0.47 | +0.37 / +0.44 | both halves | 8e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RECQL]] | -0.42 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[ADAM10]] | -0.41 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[FAM120A]] | -0.41 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[GDI2]] | -0.41 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[SDCCAG8]] | -0.40 | -0.30 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAPLN]] | B | LHFPL4 activity raises PAPLN's level | lines that do not express LHFPL4 (33) vs lines expressing it (17) | 2.36× lower at baseline in the lines without LHFPL4 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC6A11, INA, ENSG00000251652 |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.319). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.5, 25.7); signed map (-1.5, -13.1). **Vector** length 34.2, 7.93% of its response variance represented; |z| ≥ 3 in 294 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.6 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.6 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +8.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.8 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.8 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.7 | +1.2 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.6 | +0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.5 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -1.2 | +0.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.8 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | -1.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -1.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -0.6 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | LHFPL tetraspan subfamily member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,498,361-9,553,822 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GARLH4 |
| Gene groups (HGNC) | LHFPL tetraspan proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7J7](https://www.uniprot.org/uniprotkb/Q7Z7J7) (LHFPL tetraspan subfamily member 4 protein):

> Plays a role in the regulation of inhibitory synapse formation and function by being involved in maintening gamma-aminobutyric acid receptors (GABAARs) clustering and their associated scaffold proteins at inhibitory synaptic sites. Acts in concert with NLGN2 to recruit or stabilize GABAARs.

**Summary**, from NCBI Gene [375323](https://www.ncbi.nlm.nih.gov/gene/375323):

> This gene is a member of the lipoma HMGIC fusion partner (LHFP) gene family, which is a subset of the superfamily of tetraspan transmembrane protein encoding genes. Mutations in one LHFP-like gene result in deafness in humans and mice, and a second LHFP-like gene is fused to a high-mobility group gene in a translocation-associated lipoma. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:29568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29568) · Entrez [375323](https://www.ncbi.nlm.nih.gov/gene/375323) · UniProt [Q7Z7J7](https://www.uniprot.org/uniprotkb/Q7Z7J7) · Ensembl [ENSG00000156959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156959)

## Data

Gene col 8027: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8027); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8027, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8027]; `tensor/DDL_lfc|DDL_z.npy` [8027]; `embed/gene_vectors.npy` [8027]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8027 or target_col == 8027). Every well: [[LHFPL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LHFPL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
