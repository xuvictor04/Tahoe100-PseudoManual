---
symbol: "CTU1"
type: "gene"
col: 6630
ensembl_id: "ENSG00000142544"
name: "cytosolic thiouridylase subunit 1"
location: "19q13.41"
module: 33
arm: "+"
pooled_cpm: 3.76
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 9
n_dd_up_clean: 21
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# CTU1

*cytosolic thiouridylase subunit 1* — 19q13.41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.30× (z +11.0, q 1e-25, up in 36 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.729× (z -5.2, q 1e-04, down in 15 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDCD11]] (+0.73, fdr 7e-06), [[WDR3]] (+0.71, fdr 7e-06), [[SNU13]] (+0.71, fdr 7e-06); moves opposite to [[RO60]] (-0.59, fdr 1e-05), [[HMGN2]] (-0.58, fdr 3e-05), [[NUCKS1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF28]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6630.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.30×** | +11.0 | 1e-25 | 36/41 (SW480, RKO, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.48×** | +9.0 | 6e-17 | 25/37 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +7.0 | 4e-10 | 12/23 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +6.8 | 1e-09 | 9/44 (A549, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.80×** | +6.7 | 2e-09 | 16/45 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +5.6 | 2e-06 | 15/45 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +5.5 | 2e-06 | 4/9 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +4.5 | 4e-04 | 14/44 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.51×** | +4.3 | 1e-03 | 3/33 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.2 | 0.001 | 3/28 (HT-29, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.42×** | +4.0 | 0.003 | 6/33 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.92×** | +3.9 | 0.004 | 2/31 (SW1417, A498) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +3.9 | 0.004 | 9/42 (HCT15, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.006 | 3/43 (PANC-1, SW480, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.006 | 7/34 (KATO III, SW48, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.58×** | +3.7 | 0.006 | 8/43 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.010 | 2/41 (KATO III, SW480) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.023 | 5/44 (Hs 766T, HepG2/C3A, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.032 | 9/42 (LOX-IMVI, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6630.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.729×** | -5.2 | 1e-04 | 15/38 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.636×** | -5.0 | 1e-04 | 16/43 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -4.1 | 0.009 | 22/39 (RKO, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.526×** | -3.9 | 0.015 | 4/41 (SK-MEL-2, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.738×** | -3.5 | 0.044 | 1/45 (A-427) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.740×** | -3.5 | 0.044 | 10/20 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.747×** | -3.4 | 0.053 | 10/44 (LoVo, Hs 766T, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.786×** | -3.4 | 0.053 | 9/44 (AN3 CA, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.823×** | -3.2 | 0.085 | 8/44 (RKO, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6630. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 4.72 | 0 | 2 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0556× (z -11.4) |
| [[HOP62 (line)]] | alt | 1.55 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0393× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 5.08 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 4.72 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.0555× (z -10.0) |
| [[RKO (line)]] | wt | 8.34 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -9.8) |
| [[SHP-77 (line)]] | alt | 6.39 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.5 µM 0.0794× (z -10.1) |
| [[SW1417 (line)]] | alt | 6.50 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -10.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 4.61 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6630), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD11]] | +0.73 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[WDR3]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SNU13]] | +0.71 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[DDX55]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[YRDC]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 | pathway: tRNA processing; STRING 548 |
| [[MRPS23]] | +0.70 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[SNHG17]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[ZNF692]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[ZNF551]] | +0.69 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[NOL10]] | +0.68 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[ZNF787]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[MRPS21]] | +0.67 | +0.69 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RO60]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[HMGN2]] | -0.58 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[NUCKS1]] | -0.57 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.56 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[TMEM107]] | -0.56 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[PRKAR1A]] | -0.56 | -0.52 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF28]] | B | ZNF28 activity lowers CTU1's level | lines that do not express ZNF28 (6) vs lines expressing it (44) | 1.61× higher at baseline in the lines without ZNF28 | 0.022 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF701, ZNF888 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.737). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-31.9, -8.2); signed map (-15.6, -21.2). **Vector** length 56.5, 7.64% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.55 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +9.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +7.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +11.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +6.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +3.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -1.8 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -0.5 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cytosolic thiouridylase subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.41 — chr19:51,097,606-51,108,409 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC17332, NCS6; previously ATPBD3 |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7A3](https://www.uniprot.org/uniprotkb/Q7Z7A3) (Cytoplasmic tRNA 2-thiolation protein 1):

> Plays a central role in 2-thiolation of mcm(5)S(2)U at tRNA wobble positions of tRNA(Lys), tRNA(Glu) and tRNA(Gln). Directly binds tRNAs and probably acts by catalyzing adenylation of tRNAs, an intermediate required for 2-thiolation. It is unclear whether it acts as a sulfurtransferase that transfers sulfur from thiocarboxylated URM1 onto the uridine of tRNAs at wobble position.

**Summary**, from NCBI Gene [90353](https://www.ncbi.nlm.nih.gov/gene/90353):

> Predicted to enable tRNA binding activity. Predicted to be involved in tRNA wobble position uridine thiolation. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29590) · Entrez [90353](https://www.ncbi.nlm.nih.gov/gene/90353) · UniProt [Q7Z7A3](https://www.uniprot.org/uniprotkb/Q7Z7A3) · Ensembl [ENSG00000142544](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142544)

## Data

Gene col 6630: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6630); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6630, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6630]; `tensor/DDL_lfc|DDL_z.npy` [6630]; `embed/gene_vectors.npy` [6630]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6630 or target_col == 6630). Every well: [[CTU1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTU1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
