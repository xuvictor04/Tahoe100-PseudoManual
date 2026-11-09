---
symbol: "NUDT19"
type: "gene"
col: 13153
ensembl_id: "ENSG00000213965"
name: "nudix hydrolase 19"
location: "19q13.11"
module: 1
arm: "+"
pooled_cpm: 20.11
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NUDT19

*nudix hydrolase 19* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.40× (z +9.0, q 2e-16, up in 28 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.580× (z -10.4, q 2e-22, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QTRT2]] (+0.73, fdr 7e-06), [[DDX31]] (+0.70, fdr 7e-06), [[NOL9]] (+0.68, fdr 7e-06); moves opposite to [[MAGT1]] (-0.57, fdr 2e-05), [[MXD1]] (-0.55, fdr 1e-05), [[PHF1]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +9.0 | 2e-16 | 28/45 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.5 | 2e-11 | 25/45 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +7.2 | 1e-10 | 26/43 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +6.4 | 2e-08 | 28/45 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **1.20×** | +5.0 | 6e-05 | 17/46 (CFPAC-1, HOP62, …) | top dose only | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.62×** | +4.8 | 2e-04 | 10/46 (SW1417, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.3 | 0.002 | 11/46 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.0 | 0.004 | 10/23 (LoVo, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.007 | 12/45 (SW480, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.017 | 7/45 (NCI-H460, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.025 | 13/45 (SW48, BT-474, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.3 | 0.054 | 9/45 (HT-29, SW480, …) | two highest doses | composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.18× | +3.1 | 0.071 | 4/45 (BT-474, SW1417, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.095 | 4/43 (A498, SW480, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13153.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.580×** | -10.4 | 2e-22 | 30/46 (SW48, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -7.7 | 5e-12 | 20/30 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.685×** | -7.2 | 1e-10 | 28/46 (SW48, PANC-1, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.706×** | -6.6 | 4e-09 | 21/40 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -4.5 | 8e-04 | 13/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.803×** | -4.2 | 0.003 | 16/45 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.832×** | -3.5 | 0.035 | 19/45 (SW48, SW480, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.719×** | -3.3 | 0.065 | 8/44 (LOX-IMVI, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.842× | -3.3 | 0.065 | 15/45 (NCI-H23, HCT15, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.848× | -3.2 | 0.089 | 10/45 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Methotrexate (drug)]] 0.5 µM |  | 0.849× | -3.1 | 0.089 | 7/45 (LoVo, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -15.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -8.9) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -9.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 25.0 | 0 | 1 | — | [[Vandetanib (drug)]] 0.05 µM 0.0622× (z -10.1) |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.175× (z -9.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.9) | — |
| [[LoVo (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -11.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -11.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 43.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.73× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.266× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.395× (z -9.1) ⚠ cell-cycle shift, explains ~91% of this change |
| [[RKO (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -9.9) ⚠ cell-cycle shift, explains ~80% of this change |
| [[SW48 (line)]] | wt | 33.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -11.5) |
| [[A-427 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QTRT2]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[DDX31]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[NOL9]] | +0.68 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[SCO1]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ZNF777]] | +0.67 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[DHX30]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MTPAP]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ZNF354B]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[DNAAF2]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ZBTB24]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[POGK]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[RIOX2]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGT1]] | -0.57 | -0.47 / -0.57 | both halves | 2e-05 | pathway: Protein localization |
| [[MXD1]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[PHF1]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[NPTN]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises NUDT19's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises NUDT19's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.5, -38.1); signed map (0.7, -40.5). **Vector** length 78.4, 14.4% of its response variance represented; |z| ≥ 3 in 801 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.4 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +7.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | +3.5 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +4.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +3.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.6 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.0 | -0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:32,691,821-32,713,792 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP2 |
| Gene groups (HGNC) | Nudix hydrolase family |
| Hallmark sets | PEROXISOME |
| Reactome | 5 pathways, smallest: Peroxisomal lipid metabolism; Peroxisomal protein import; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MXV4](https://www.uniprot.org/uniprotkb/A8MXV4) (Acyl-coenzyme A diphosphatase NUDT19):

> Fatty acyl-coenzyme A (CoA) diphosphatase that hydrolyzes fatty acyl-CoA to yield acyl-4'-phosphopantetheine and adenosine 3',5'-bisphosphate (By similarity). Mediates the hydrolysis of a wide range of CoA esters, including choloyl-CoA and branched-chain fatty-acyl-CoA esters and at low substrate concentrations medium and long-chain fatty-acyl-CoA esters are the primary substrates (By similarity). Highest activity seen with medium-chain acyl-CoA esters and higher rates of activity seen with the …

**Summary**, from NCBI Gene [390916](https://www.ncbi.nlm.nih.gov/gene/390916):

> Predicted to enable magnesium ion binding activity. Predicted to be involved in acyl-CoA metabolic process and coenzyme A catabolic process. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32036) · Entrez [390916](https://www.ncbi.nlm.nih.gov/gene/390916) · UniProt [A8MXV4](https://www.uniprot.org/uniprotkb/A8MXV4) · Ensembl [ENSG00000213965](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213965)

## Data

Gene col 13153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13153); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13153]; `tensor/DDL_lfc|DDL_z.npy` [13153]; `embed/gene_vectors.npy` [13153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13153 or target_col == 13153). Every well: [[NUDT19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
