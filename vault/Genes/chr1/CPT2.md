---
symbol: "CPT2"
type: "gene"
col: 8048
ensembl_id: "ENSG00000157184"
name: "carnitine palmitoyltransferase 2"
location: "1p32.3"
module: 11
arm: "+"
pooled_cpm: 8.33
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CPT2

*carnitine palmitoyltransferase 2* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.98× (z +9.9, q 2e-20, up in 35 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.312× (z -12.0, q 3e-30, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBCC]] (+0.73, fdr 7e-06), [[C14orf119]] (+0.71, fdr 7e-06), [[RPP25L]] (+0.70, fdr 7e-06); moves opposite to [[CPSF6]] (-0.61, fdr 1e-05), [[SMG1P3]] (-0.59, fdr 1e-05), [[TCF3]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8048.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +9.9 | 2e-20 | 35/43 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.70×** | +7.7 | 4e-12 | 32/47 (KATO III, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +5.8 | 1e-06 | 25/40 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.007 | 18/47 (A498, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.008 | 18/41 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.9 | 0.008 | 16/36 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +3.9 | 0.008 | 13/40 (KATO III, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.39×** | +3.4 | 0.053 | 9/47 (NCI-H661, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.24×** | +3.2 | 0.093 | 11/46 (NCI-H2030, LS 180, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.099 | 6/46 (PANC-1, LS 180, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.34× | +3.0 | 0.13 | 1/44 (HEC-1-A) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8048.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.312×** | -12.0 | 3e-30 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.347×** | -10.9 | 4e-25 | 40/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.358×** | -10.6 | 9e-24 | 34/42 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.446×** | -8.3 | 1e-14 | 33/45 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.575×** | -5.7 | 2e-06 | 28/46 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.636×** | -4.6 | 3e-04 | 21/48 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.625×** | -4.6 | 3e-04 | 22/38 (Panc 03.27, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.431×** | -4.5 | 4e-04 | 22/41 (SK-MEL-2, BT-474, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.659×** | -4.3 | 0.001 | 15/47 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.466×** | -4.1 | 0.002 | 16/45 (PANC-1, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.679×** | -4.0 | 0.004 | 17/45 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.793×** | -3.4 | 0.037 | 14/48 (NCI-H1792, HCT15, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.745× | -3.0 | 0.11 | 13/45 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8048. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.2 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.144× (z -13.8) |
| [[LS 180 (line)]] | wt | 8.42 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0796× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.112× (z -9.0) |
| [[PANC-1 (line)]] | alt | 9.62 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -12.6) |
| [[HOP62 (line)]] | alt | 9.90 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 7.40 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0761× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 5.03 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 6.26 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0754× (z -13.0) |
| [[A-427 (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -9.4) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 5.68 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0736× (z -9.8) |
| [[C-33 A (line)]] | alt | 6.89 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0745× (z -8.9) |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0914× (z -10.9) |
| [[H4 (line)]] | wt | 9.82 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0572× (z -10.1) |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.148× (z -8.5) |
| [[HT-29 (line)]] | alt | 8.59 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0634× (z -11.4) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 8.68 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0536× (z -13.0) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 9.44 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0876× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8048), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCC]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[C14orf119]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.70 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[GPANK1]] | +0.68 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.68 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[SMG8]] | +0.68 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.67 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[RBM8A]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[PPCS]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ZNF101]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[MRPS31]] | +0.66 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[PDCD7]] | +0.65 | +0.64 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF6]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[SMG1P3]] | -0.59 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[TCF3]] | -0.58 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[COL18A1]] | -0.58 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[NCOR2]] | -0.57 | -0.57 / -0.46 | both halves | 2e-05 | pathway: PPARA activates gene expression |
| [[TBCD]] | -0.57 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.56 | -0.39 / -0.62 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CPT2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.674). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.1, 5.4); signed map (2.6, -17.7). **Vector** length 70.6, 13.0% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.5 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +2.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | -2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.3 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.9 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.5 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | carnitine palmitoyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:53,196,792-53,214,197 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CPTASE; previously CPT1 |
| Gene groups (HGNC) | Carnitine palmitoyltransferase family |
| Hallmark sets | FATTY_ACID_METABOLISM, ADIPOGENESIS |
| Reactome | 5 pathways, smallest: Carnitine shuttle; PPARA activates gene expression; Regulation of lipid metabolism by PPARalpha |
| Matched by | ensembl_id |

**Function**, from UniProt [P23786](https://www.uniprot.org/uniprotkb/P23786) (Carnitine O-palmitoyltransferase 2, mitochondrial):

> Involved in the intramitochondrial synthesis of acylcarnitines from accumulated acyl-CoA metabolites. Reconverts acylcarnitines back into the respective acyl-CoA esters that can then undergo beta-oxidation, an essential step for the mitochondrial uptake of long-chain fatty acids and their subsequent beta-oxidation in the mitochondrion. Active with medium (C8-C12) and long-chain (C14-C18) acyl-CoA esters.

**Summary**, from NCBI Gene [1376](https://www.ncbi.nlm.nih.gov/gene/1376):

> The protein encoded by this gene is a nuclear protein which is transported to the mitochondrial inner membrane. Together with carnitine palmitoyltransferase I, the encoded protein oxidizes long-chain fatty acids in the mitochondria. Defects in this gene are associated with mitochondrial long-chain fatty-acid (LCFA) oxidation disorders. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2330](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2330) · Entrez [1376](https://www.ncbi.nlm.nih.gov/gene/1376) · UniProt [P23786](https://www.uniprot.org/uniprotkb/P23786) · Ensembl [ENSG00000157184](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157184)

## Data

Gene col 8048: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8048); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8048, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8048]; `tensor/DDL_lfc|DDL_z.npy` [8048]; `embed/gene_vectors.npy` [8048]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8048 or target_col == 8048). Every well: [[CPT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
