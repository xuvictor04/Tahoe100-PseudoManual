---
symbol: "MAPKAPK5"
type: "gene"
col: 1560
ensembl_id: "ENSG00000089022"
name: "MAPK activated protein kinase 5"
location: "12q24.12-q24.13"
module: 5
arm: "+"
pooled_cpm: 35.23
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MAPKAPK5

*MAPK activated protein kinase 5* — 12q24.12-q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.54× (z +7.3, q 2e-10, up in 39 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.11× (z +6.5, q 2e-08, up in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 3.30×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.681× (z -9.1, q 3e-17, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM3AP]] (+0.76, fdr 7e-06), [[ABCF2]] (+0.76, fdr 7e-06), [[DNAJC11]] (+0.76, fdr 7e-06); moves opposite to [[RNF24]] (-0.72, fdr 7e-06), [[HILPDA]] (-0.68, fdr 7e-06), [[FBXO33]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NR3C2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1560.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 3.30×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +7.3 | 2e-10 | 39/48 (NCI-H460, AsPC-1, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +6.5 | 2e-08 | 34/48 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.2 | 0.005 | 20/41 (KATO III, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +4.1 | 0.005 | 25/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.25×** | +3.5 | 0.062 | 18/43 (A-427, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.3 | 0.10 | 0/48 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | 1.15× | +3.2 | 0.11 | 12/48 (NCI-H1573, Panc 03.27, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | 1.21× | +3.0 | 0.16 | 16/46 (NCI-H1573, LOX-IMVI, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 1.41× | +3.0 | 0.16 | 10/48 (PANC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1560.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.681×** | -9.1 | 3e-17 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.595×** | -8.7 | 8e-16 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.652×** | -7.2 | 1e-10 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.697×** | -6.1 | 2e-07 | 31/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.702×** | -6.0 | 3e-07 | 27/47 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.713×** | -5.7 | 1e-06 | 31/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.761×** | -4.6 | 3e-04 | 28/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 47.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.441× (z -9.5) |
| [[A-427 (line)]] | wt | 36.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.375× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 46.7 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -10.7) ⚠ cell-cycle shift, explains ~81% of this change |
| [[HCT15 (line)]] | alt | 36.7 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.193× (z -11.0) |
| [[AN3 CA (line)]] | alt | 45.4 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.155× (z -8.6) |
| [[BT-474 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.370× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 52.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -9.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 39.7 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.116× (z -9.5) |
| [[LS 180 (line)]] | wt | 36.7 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.337× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.395× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 37.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.469× (z -8.6) |
| [[SW48 (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0634× (z -8.5) ⚠ toxic |
| [[SW480 (line)]] | alt | 47.0 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.577× (z -8.8) |
| [[A-172 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1560), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM3AP]] | +0.76 | +0.61 / +0.81 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.76 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.76 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[ALG8]] | +0.73 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[SCO1]] | +0.73 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[SPRYD4]] | +0.72 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[VPS52]] | +0.71 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[NOL9]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[DHX37]] | +0.70 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[WDR46]] | +0.70 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ANKRD40]] | +0.70 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ZNF202]] | +0.70 | +0.71 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF24]] | -0.72 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[HILPDA]] | -0.68 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[FBXO33]] | -0.67 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.66 | -0.45 / -0.62 | both halves | 3e-05 | pathway: Cellular Senescence |
| [[GABARAPL2]] | -0.66 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[CARHSP1]] | -0.66 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[TNNI3]] | -0.66 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[RNF114]] | -0.66 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[RFX2]] | -0.66 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[ANKRD37]] | -0.65 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[JPT1]] | -0.65 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[SIRT2]] | -0.64 | -0.60 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C2]] | B | NR3C2 activity weakens MAPKAPK5's drug response | lines that do not express NR3C2 (15) vs lines expressing it (33) | the lines without NR3C2 respond 1.20× as strongly (z diff -0.65); strongest at Panobinostat 5 µM: 0.54x vs 0.68x (z diff -2.2) | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MAPKAPK5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises MAPKAPK5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.703). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-16.8, -31.7); signed map (-6.5, -42.1). **Vector** length 103, 24.1% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.59 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.9 | +7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +4.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | +4.5 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.6 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.9 | -9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.7 | -6.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.0 | -4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.7 | -8.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -7.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | MAPK activated protein kinase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.12-q24.13 — chr12:111,842,013-111,902,222 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRAK, MK5 |
| Gene groups (HGNC) | MAPK activated protein kinases; MAPKAPK family |
| Reactome | 9 pathways, smallest: MAPK6/MAPK4 signaling; Oxidative Stress Induced Senescence; Regulation of TP53 Activity through Phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IW41](https://www.uniprot.org/uniprotkb/Q8IW41) (MAP kinase-activated protein kinase 5):

> Tumor suppressor serine/threonine-protein kinase involved in mTORC1 signaling and post-transcriptional regulation. Phosphorylates FOXO3, ERK3/MAPK6, ERK4/MAPK4, HSP27/HSPB1, p53/TP53 and RHEB. Acts as a tumor suppressor by mediating Ras-induced senescence and phosphorylating p53/TP53. Involved in post-transcriptional regulation of MYC by mediating phosphorylation of FOXO3: phosphorylation of FOXO3 leads to promote nuclear localization of FOXO3, enabling expression of miR-34b and miR-34c, 2 …

**Summary**, from NCBI Gene [8550](https://www.ncbi.nlm.nih.gov/gene/8550):

> The protein encoded by this gene is a tumor suppressor and member of the serine/threonine kinase family. In response to cellular stress and proinflammatory cytokines, this kinase is activated through its phosphorylation by MAP kinases including MAPK1/ERK, MAPK14/p38-alpha, and MAPK11/p38-beta. The encoded protein is found in the nucleus but translocates to the cytoplasm upon phosphorylation and activation. This kinase phosphorylates heat shock protein HSP27 at its physiologically relevant …

**Accessions** — [HGNC:6889](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6889) · Entrez [8550](https://www.ncbi.nlm.nih.gov/gene/8550) · UniProt [Q8IW41](https://www.uniprot.org/uniprotkb/Q8IW41) · Ensembl [ENSG00000089022](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089022)

## Data

Gene col 1560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1560); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1560, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1560]; `tensor/DDL_lfc|DDL_z.npy` [1560]; `embed/gene_vectors.npy` [1560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1560 or target_col == 1560). Every well: [[MAPKAPK5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPKAPK5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
