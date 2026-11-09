---
symbol: "HIPK1"
type: "gene"
col: 8674
ensembl_id: "ENSG00000163349"
name: "homeodomain interacting protein kinase 1"
location: "1p13.2"
module: 29
arm: "+"
pooled_cpm: 70.8
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# HIPK1

*homeodomain interacting protein kinase 1* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.92× (z +9.8, q 7e-20, up in 46 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.101×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.204×; ⚠ cell-cycle shift, explains ~0% of this change); [[Larotrectinib (drug)]] 0.5 µM in 1 line (CHP-212 0.0814×); [[Tofacitinib (citrate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0889×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMPK1]] (+0.64, fdr 1e-05), [[LAPTM4A]] (+0.63, fdr 7e-06), [[TMEM30A]] (+0.62, fdr 9e-06); moves opposite to [[ESF1]] (-0.69, fdr 7e-06), [[EIF5B]] (-0.59, fdr 1e-05), [[NIFK]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CYBRD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8674.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.92×** | +9.8 | 7e-20 | 46/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +9.6 | 2e-19 | 46/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +8.7 | 9e-16 | 34/49 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +8.0 | 2e-13 | 37/47 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +7.4 | 2e-11 | 36/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +7.3 | 4e-11 | 40/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.8 | 1e-09 | 39/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.3 | 2e-08 | 24/42 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +6.1 | 8e-08 | 30/49 (PANC-1, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.38×** | +5.7 | 9e-07 | 32/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +5.4 | 4e-06 | 25/44 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 1e-04 | 26/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.004 | 23/48 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.024 | 18/48 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.20× | +3.1 | 0.070 | 18/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8674.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.101×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.204×; ⚠ cell-cycle shift, explains ~0% of this change); [[Larotrectinib (drug)]] 0.5 µM in 1 line (CHP-212 0.0814×); [[Tofacitinib (citrate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0889×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.813× | -3.7 | 0.11 | 16/48 (MIA PaCa-2, SW 1088, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.818× | -3.6 | 0.11 | 20/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | 0.698× | -3.3 | 0.17 | 16/48 (Panc 03.27, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8674. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 46.4 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +15.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.40× (z +10.1) | — |
| [[SW480 (line)]] | alt | 70.4 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +11.3) | — |
| [[LoVo (line)]] | wt | 72.5 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 78.0 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 40.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 30.8 | 0 | 2 | — | [[Larotrectinib (drug)]] 0.5 µM 0.0814× (z -8.8) |
| [[A549 (line)]] | wt | 48.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.2) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[AN3 CA (line)]] | alt | 73.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 77.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +8.5) | — |
| [[KATO III (line)]] | alt | 59.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.80× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 61.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +8.6) | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.101× (z -11.1) |
| [[A-172 (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 76.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 95.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 146 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 69.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8674), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMPK1]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[LAPTM4A]] | +0.63 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[TMEM30A]] | +0.62 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[SCARB2]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[RPN1]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PRKACA]] | +0.58 | +0.36 / +0.71 | both halves | 9e-05 | pathway: Cardiac conduction |
| [[STRADB]] | +0.57 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[C2CD2L]] | +0.57 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[PGRMC1]] | +0.56 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[ITM2B]] | +0.56 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[SETD3]] | +0.55 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[ARF1]] | +0.55 | +0.43 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESF1]] | -0.69 | -0.59 / -0.72 | both halves | 7e-06 |  |
| [[EIF5B]] | -0.59 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[NIFK]] | -0.58 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[METTL2A]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[RPP14]] | -0.57 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[ZNF593]] | -0.56 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[MRPL46]] | -0.56 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[VPS37C]] | -0.55 | -0.24 / -0.65 | both halves | 4e-04 |  |
| [[ZNF611]] | -0.55 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[CEBPZ]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[THUMPD2]] | -0.55 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.54 | -0.46 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYBRD1]] | B | CYBRD1 activity raises HIPK1's level | lines that do not express CYBRD1 (17) vs lines expressing it (33) | 1.17× lower at baseline in the lines without CYBRD1 | 0.065 | ⚠ within organs, on part of the lines; also absent: MME, BDNF, APOBEC3G |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.604). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.6, -21.3); signed map (-24.4, -38.7). **Vector** length 96.9, 24.5% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.2 | +8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +7.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +2.1 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | -0.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.0 | +0.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.1 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | homeodomain interacting protein kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:113,929,324-113,977,869 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0630, Myak, MGC26642, Nbak2, MGC33446, MGC33548 |
| Gene groups (HGNC) | Homeodomain interacting protein kinase family |
| Reactome | 7 pathways, smallest: Physiological factors; YAP1- and WWTR1 (TAZ)-stimulated gene expression; Cardiac conduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Z02](https://www.uniprot.org/uniprotkb/Q86Z02) (Homeodomain-interacting protein kinase 1):

> Serine/threonine-protein kinase involved in transcription regulation and TNF-mediated cellular apoptosis. Plays a role as a corepressor for homeodomain transcription factors. Phosphorylates DAXX and MYB. Phosphorylates DAXX in response to stress, and mediates its translocation from the nucleus to the cytoplasm. Inactivates MYB transcription factor activity by phosphorylation. Prevents MAP3K5-JNK activation in the absence of TNF. TNF triggers its translocation to the cytoplasm in response to …

**Summary**, from NCBI Gene [204851](https://www.ncbi.nlm.nih.gov/gene/204851):

> The protein encoded by this gene belongs to the Ser/Thr family of protein kinases and HIPK subfamily. It phosphorylates homeodomain transcription factors and may also function as a co-repressor for homeodomain transcription factors. Alternative splicing results in four transcript variants encoding four distinct isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19006) · Entrez [204851](https://www.ncbi.nlm.nih.gov/gene/204851) · UniProt [Q86Z02](https://www.uniprot.org/uniprotkb/Q86Z02) · Ensembl [ENSG00000163349](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163349)

## Data

Gene col 8674: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8674); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8674, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8674]; `tensor/DDL_lfc|DDL_z.npy` [8674]; `embed/gene_vectors.npy` [8674]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8674 or target_col == 8674). Every well: [[HIPK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIPK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
