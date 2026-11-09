---
symbol: "SYMPK"
type: "gene"
col: 4659
ensembl_id: "ENSG00000125755"
name: "symplekin scaffold protein"
location: "19q13.32"
module: 5
arm: "+"
pooled_cpm: 65.24
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SYMPK

*symplekin scaffold protein* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.95× (z +14.1, q 4e-42, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.706× (z -9.2, q 2e-17, down in 35 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTEL1]] (+0.71, fdr 7e-06), [[TMEM138]] (+0.64, fdr 1e-05), [[EFTUD2]] (+0.63, fdr 1e-05); moves opposite to [[RAB33B]] (-0.62, fdr 1e-05), [[IFRD1]] (-0.55, fdr 1e-05), [[RYBP]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4659.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.95×** | +14.1 | 4e-42 | 44/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.89×** | +13.4 | 9e-39 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +11.1 | 2e-26 | 41/47 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.63×** | +10.3 | 8e-23 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +5.5 | 4e-06 | 28/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +5.4 | 4e-06 | 26/47 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +5.4 | 4e-06 | 28/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +4.9 | 7e-05 | 28/48 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.006 | 19/48 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.20×** | +3.6 | 0.015 | 20/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4659.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.706×** | -9.2 | 2e-17 | 35/49 (RPMI-7951, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.782×** | -5.0 | 2e-04 | 25/48 (A-172, AN3 CA, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.790×** | -4.8 | 4e-04 | 25/50 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.808×** | -4.5 | 0.001 | 21/48 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.843× | -4.2 | 0.003 | 22/48 (SW1417, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.839× | -3.7 | 0.020 | 21/48 (HOP62, A-427, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | 0.839× | -3.7 | 0.020 | 17/47 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.842× | -3.6 | 0.022 | 18/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.6 | 0.023 | 19/48 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.885× | -3.2 | 0.079 | 12/48 (J82, CHP-212, …) | top dose only | low cells (technical?) |
| [[AZD-7648 (drug)]] 0.5 µM |  | 0.795× | -3.1 | 0.11 | 16/48 (A-172, H4, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4659. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 208 | 2 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -10.1) |
| [[LoVo (line)]] | wt | 52.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +12.5) | — |
| [[SW480 (line)]] | alt | 76.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +14.3) | — |
| [[AsPC-1 (line)]] | alt | 37.6 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +9.8) | [[Docetaxel (drug)]] 0.05 µM 0.401× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HT-29 (line)]] | alt | 88.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +13.8) | — |
| [[HS-578T (line)]] | alt | 59.9 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.64× (z +10.1) | — |
| [[J82 (line)]] | alt | 58.9 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.1) | [[Selinexor (drug)]] 5 µM 0.537× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 62.0 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +10.1) | [[Lonafarnib (drug)]] 5 µM 0.215× (z -9.3) ⚠ toxic |
| [[LS 180 (line)]] | wt | 67.4 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 42.9 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.22× (z +9.8) | — |
| [[RKO (line)]] | wt | 64.4 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 43.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -11.0) |
| [[A549 (line)]] | wt | 76.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 48.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -9.3) |
| [[COLO 205 (line)]] | alt | 56.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +11.8) | — |
| [[HCT15 (line)]] | alt | 90.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 80.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 60.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -8.7) |
| [[NCI-H661 (line)]] | alt | 47.3 | 0 | 1 | — | [[γ-Oryzanol (drug)]] 0.5 µM 0.0822× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 62.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 99.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -10.5) |
| [[SNU-1 (line)]] | wt | 80.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 74.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +9.2) | — |
| [[A-427 (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4659), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTEL1]] | +0.71 | +0.75 / +0.71 | both halves | 7e-06 | STRING 549 |
| [[TMEM138]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[EFTUD2]] | +0.63 | +0.56 / +0.74 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 511 |
| [[SIN3B]] | +0.61 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[KAT8]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[C1orf159]] | +0.59 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[PEX26]] | +0.58 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[MCM3AP]] | +0.58 | +0.35 / +0.76 | both halves | 1e-04 |  |
| [[SENP3]] | +0.57 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[MZF1]] | +0.57 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[QSOX2]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MTA1]] | +0.56 | +0.36 / +0.73 | both halves | 1e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB33B]] | -0.62 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[IFRD1]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 | same gene group |
| [[RYBP]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[CDK7]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[KDM5B]] | -0.52 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[GTF2B]] | -0.52 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[LNX2]] | -0.51 | -0.53 / -0.49 | both halves | 2e-05 |  |
| [[NRBF2]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[NMD3]] | -0.49 | -0.56 / -0.26 | both halves | 4e-04 |  |
| [[RIOK3]] | -0.49 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[EFNB1]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ABI1]] | -0.48 | -0.48 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SYMPK's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers SYMPK's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.437). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-16.3, -30.1); signed map (-8.6, -41.7). **Vector** length 104, 25.7% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +8.2 | +13.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.6 | +14.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +11.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.3 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.2 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.0 | +1.2 |
|  | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +1.8 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.3 | -3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.6 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -9.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -4.2 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -2.0 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -0.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | symplekin scaffold protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,815,410-45,863,225 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SYM, SPK, Pta1 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 13 pathways, smallest: Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92797](https://www.uniprot.org/uniprotkb/Q92797) (Symplekin):

> Scaffold protein that functions as a component of a multimolecular complex involved in histone mRNA 3'-end processing. Specific component of the tight junction (TJ) plaque, but might not be an exclusively junctional component. May have a house-keeping rule. Is involved in pre-mRNA polyadenylation. Enhances SSU72 phosphatase activity.

**Summary**, from NCBI Gene [8189](https://www.ncbi.nlm.nih.gov/gene/8189):

> This gene encodes a nuclear protein that functions in the regulation of polyadenylation and promotes gene expression. The protein forms a high-molecular weight complex with components of the polyadenylation machinery. It is thought to serve as a scaffold for recruiting regulatory factors to the polyadenylation complex. It also participates in 3'-end maturation of histone mRNAs, which do not undergo polyadenylation. The protein also localizes to the cytoplasmic plaques of tight junctions in some …

**Accessions** — [HGNC:22935](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22935) · Entrez [8189](https://www.ncbi.nlm.nih.gov/gene/8189) · UniProt [Q92797](https://www.uniprot.org/uniprotkb/Q92797) · Ensembl [ENSG00000125755](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125755)

## Data

Gene col 4659: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4659); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4659, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4659]; `tensor/DDL_lfc|DDL_z.npy` [4659]; `embed/gene_vectors.npy` [4659]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4659 or target_col == 4659). Every well: [[SYMPK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYMPK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
