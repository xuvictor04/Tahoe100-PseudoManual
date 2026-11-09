---
symbol: "ALKBH8"
type: "gene"
col: 6060
ensembl_id: "ENSG00000137760"
name: "alkB homolog 8, tRNA methyltransferase"
location: "11q22.3"
module: 4
arm: "+"
pooled_cpm: 15.67
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 7
n_dd_up_clean: 23
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ALKBH8

*alkB homolog 8, tRNA methyltransferase* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.99× (z +11.5, q 1e-27, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.452× (z -18.7, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MINDY4]] (+0.74, fdr 7e-06), [[TTC5]] (+0.70, fdr 1e-05), [[CWC27]] (+0.70, fdr 7e-06); moves opposite to [[CDK19]] (-0.59, fdr 1e-05), [[FAM177A1]] (-0.58, fdr 1e-05), [[DLEU2]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6060.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.99×** | +11.5 | 1e-27 | 40/47 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.78×** | +9.6 | 2e-19 | 35/47 (LoVo, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.82×** | +9.0 | 3e-17 | 32/46 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.86×** | +8.7 | 7e-16 | 37/48 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +8.3 | 1e-14 | 28/48 (NCI-H1792, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.29×** | +7.3 | 4e-11 | 22/48 (SW480, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.46×** | +6.4 | 2e-08 | 24/47 (hTERT-HPNE, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.43×** | +6.0 | 1e-07 | 17/48 (AsPC-1, HT-29, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +5.7 | 7e-07 | 19/48 (HOP62, BT-474, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +5.6 | 9e-07 | 18/37 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.6 | 1e-06 | 20/46 (LS 180, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +5.3 | 5e-06 | 17/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.0 | 2e-05 | 18/47 (A-427, A549, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +5.0 | 2e-05 | 19/46 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.34×** | +4.8 | 7e-05 | 19/45 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +4.6 | 1e-04 | 14/48 (SHP-77, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.6 | 1e-04 | 19/47 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 2e-04 | 14/47 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 2e-04 | 14/47 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6060.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.452×** | -18.7 | 0e+00 | 44/48 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.491×** | -11.4 | 1e-27 | 35/47 (SNU-423, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -10.7 | 1e-24 | 33/48 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.541×** | -5.4 | 1e-05 | 19/47 (MIA PaCa-2, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **0.738×** | -3.6 | 0.036 | 6/48 (RPMI-7951, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.810×** | -3.5 | 0.044 | 12/47 (KATO III, HOP62, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.814×** | -3.4 | 0.049 | 13/47 (NCI-H1573, hTERT-HPNE, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.865× | -3.4 | 0.049 | 8/48 (PANC-1, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6060. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 32.1 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -18.2) |
| [[LS 180 (line)]] | wt | 16.0 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.1) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.01× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -10.3) |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 21.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0618× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 19.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -12.2) |
| [[SNU-1 (line)]] | wt | 20.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0805× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -10.1) |
| [[SW480 (line)]] | alt | 25.3 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -9.8) |
| [[C32 (line)]] | wt | 22.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -12.7) |
| [[COLO 205 (line)]] | alt | 9.39 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0732× (z -9.8) |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0876× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 19.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -8.7) |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 21.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 23.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -10.1) |
| [[SNU-423 (line)]] | alt | 11.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0782× (z -12.0) |
| [[SW1417 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 21.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -12.4) |
| [[A-172 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6060), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINDY4]] | +0.74 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[TTC5]] | +0.70 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[CWC27]] | +0.70 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[COA1]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[IRAK1BP1]] | +0.68 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[FAM98B]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 | pathway: tRNA processing |
| [[CSTF2]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 | same gene group; pathway: tRNA processing |
| [[MRPL19]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[FXN]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[VTA1]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[SAAL1]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[NAA25]] | +0.65 | +0.68 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK19]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[FAM177A1]] | -0.58 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[DLEU2]] | -0.56 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[AHCYL1]] | -0.56 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[STX5]] | -0.55 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[SMIM14]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ALKBH8's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.0, -1.5); signed map (-21.4, -20.5). **Vector** length 106, 24.6% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +11.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.0 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +9.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.4 | +8.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +9.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.4 | -18.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -11.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -4.0 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.5 | -5.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | alkB homolog 8, tRNA methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:107,502,727-107,565,742 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10235, TRM9, TRMT9A |
| Gene groups (HGNC) | Alkylation repair homologs; RNA binding motif containing; 7BS DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BT7](https://www.uniprot.org/uniprotkb/Q96BT7) (tRNA):

> Catalyzes the methylation of 5-carboxymethyl uridine to 5-methylcarboxymethyl uridine at the wobble position of the anticodon loop in tRNA via its methyltransferase domain. Catalyzes the last step in the formation of 5-methylcarboxymethyl uridine at the wobble position of the anticodon loop in target tRNA. Has a preference for tRNA(Arg) and tRNA(Glu), and does not bind tRNA(Lys). Binds tRNA and catalyzes the iron and alpha-ketoglutarate dependent hydroxylation of 5-methylcarboxymethyl uridine …

**Summary**, from NCBI Gene [91801](https://www.ncbi.nlm.nih.gov/gene/91801):

> Enables tRNA (uridine) methyltransferase activity; tRNA binding activity; and zinc ion binding activity. Involved in DNA damage response; tRNA methylation; and tRNA wobble uridine modification. Located in cytosol and nucleoplasm. Implicated in autosomal recessive intellectual developmental disorder 71. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25189) · Entrez [91801](https://www.ncbi.nlm.nih.gov/gene/91801) · UniProt [Q96BT7](https://www.uniprot.org/uniprotkb/Q96BT7) · Ensembl [ENSG00000137760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137760)

## Data

Gene col 6060: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6060); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6060, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6060]; `tensor/DDL_lfc|DDL_z.npy` [6060]; `embed/gene_vectors.npy` [6060]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6060 or target_col == 6060). Every well: [[ALKBH8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALKBH8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
