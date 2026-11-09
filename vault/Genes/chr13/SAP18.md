---
symbol: "SAP18"
type: "gene"
col: 7437
ensembl_id: "ENSG00000150459"
name: "Sin3A associated protein 18"
location: "13q12.11"
module: 12
arm: "+"
pooled_cpm: 56.68
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# SAP18

*Sin3A associated protein 18* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.95× (z +9.8, q 8e-20, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIR1]] (+0.70, fdr 7e-06), [[SNRPB2]] (+0.67, fdr 7e-06), [[CTR9]] (+0.65, fdr 7e-06); moves opposite to [[UBE2G2]] (-0.64, fdr 7e-06), [[MACROH2A1]] (-0.62, fdr 2e-05), [[TCOF1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +9.8 | 8e-20 | 45/48 (J82, C32, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.52×** | +8.6 | 3e-15 | 43/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.26×** | +8.1 | 9e-14 | 35/41 (A-172, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.68×** | +7.6 | 4e-12 | 37/48 (C32, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.97×** | +7.0 | 3e-10 | 47/48 (SW480, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.96×** | +7.0 | 3e-10 | 45/48 (SW480, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +6.9 | 3e-10 | 47/47 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +6.3 | 2e-08 | 41/48 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.48×** | +4.9 | 5e-05 | 37/49 (COLO 205, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.61×** | +4.9 | 5e-05 | 38/47 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.61×** | +4.9 | 5e-05 | 38/48 (SW480, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.4 | 5e-04 | 31/48 (A-172, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.55×** | +4.4 | 6e-04 | 32/48 (COLO 205, NCI-H1573, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.57×** | +4.2 | 9e-04 | 32/45 (A549, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.001 | 30/48 (A-427, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.1 | 0.067 | 24/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 42.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +11.7) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 40.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[A-172 (line)]] | wt | 44.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.8) | — |
| [[A549 (line)]] | wt | 37.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.6) | — |
| [[KATO III (line)]] | alt | 96.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 46.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.5) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.7) | — |
| [[A498 (line)]] | wt | 72.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.2) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[AsPC-1 (line)]] | alt | 53.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.1) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[CFPAC-1 (line)]] | alt | 52.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 150 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.7) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[HEC-1-A (line)]] | alt | 54.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 39.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.1) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[HT-29 (line)]] | alt | 103 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 51.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.7) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[J82 (line)]] | alt | 75.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.3) | — |
| [[LoVo (line)]] | wt | 64.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.9) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[NCI-H1573 (line)]] | alt | 28.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.1) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[NCI-H1792 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +10.8) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[NCI-H23 (line)]] | alt | 82.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H2347 (line)]] | alt | 69.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 34.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.2) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[Panc 03.27 (line)]] | alt | 101 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.0) | — |
| [[A-427 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 70.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIR1]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SNRPB2]] | +0.67 | +0.75 / +0.59 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 539 |
| [[CTR9]] | +0.65 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[ZNF350]] | +0.65 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[ZNF490]] | +0.64 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[SYF2]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[EAPP]] | +0.62 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[MED19]] | +0.62 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[CCDC115]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[RBM8A]] | +0.61 | +0.72 / +0.55 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 916 |
| [[SUGP1]] | +0.61 | +0.64 / +0.61 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[BRAP]] | +0.61 | +0.69 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G2]] | -0.64 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[MACROH2A1]] | -0.62 | -0.46 / -0.68 | both halves | 2e-05 |  |
| [[TCOF1]] | -0.61 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[XPO5]] | -0.61 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[LRP8]] | -0.61 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[GMPS]] | -0.60 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.60 | -0.41 / -0.67 | both halves | 4e-05 |  |
| [[SUGP2]] | -0.59 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[NUP210]] | -0.59 | -0.50 / -0.59 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[NUP188]] | -0.59 | -0.29 / -0.69 | both halves | 2e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[R3HDM1]] | -0.59 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[DDX11]] | -0.59 | -0.58 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SAP18's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDCA7]] | B | CDCA7 activity raises SAP18's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without CDCA7 | 0.072 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[MED6]] | C | MED6's natural level weakens SAP18's drug response | MED6's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.06; direction clear | 0.006 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-31.6, -34.8); signed map (-10.0, -9.4). **Vector** length 63.9, 18.8% of its response variance represented; |z| ≥ 3 in 726 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.7 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +3.1 | +7.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.1 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.8 | +6.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +1.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.3 | -1.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.6 | +0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | +0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | Sin3A associated protein 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:21,140,119-21,149,097 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAP18p, 2HOR0202, MGC27131 |
| Gene groups (HGNC) | ASAP complex subunits; SIN3 histone deacetylase complex subunits; Spliceosomal Bact complex; Spliceosomal C complex |
| Reactome | 13 pathways, smallest: HDACs deacetylate histones; NoRC negatively regulates rRNA expression; Negative epigenetic regulation of rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [O00422](https://www.uniprot.org/uniprotkb/O00422) (Histone deacetylase complex subunit SAP18):

> Component of the SIN3-repressing complex. Enhances the ability of SIN3-HDAC1-mediated transcriptional repression. When tethered to the promoter, it can direct the formation of a repressive complex to core histone proteins. Auxiliary component of the splicing-dependent multiprotein exon junction complex (EJC) deposited at splice junction on mRNAs. The EJC is a dynamic structure consisting of core proteins and several peripheral nuclear and cytoplasmic associated factors that join the complex …

**Summary**, from NCBI Gene [10284](https://www.ncbi.nlm.nih.gov/gene/10284):

> Histone acetylation plays a key role in the regulation of eukaryotic gene expression. Histone acetylation and deacetylation are catalyzed by multisubunit complexes. The protein encoded by this gene is a component of the histone deacetylase complex, which includes SIN3, SAP30, HDAC1, HDAC2, RbAp46, RbAp48, and other polypeptides. This protein directly interacts with SIN3 and enhances SIN3-mediated transcriptional repression when tethered to the promoter. A pseudogene has been identified on …

**Accessions** — [HGNC:10530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10530) · Entrez [10284](https://www.ncbi.nlm.nih.gov/gene/10284) · UniProt [O00422](https://www.uniprot.org/uniprotkb/O00422) · Ensembl [ENSG00000150459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150459)

## Data

Gene col 7437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7437); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7437]; `tensor/DDL_lfc|DDL_z.npy` [7437]; `embed/gene_vectors.npy` [7437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7437 or target_col == 7437). Every well: [[SAP18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAP18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
