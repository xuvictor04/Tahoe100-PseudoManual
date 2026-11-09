---
symbol: "GPX4"
type: "gene"
col: 9469
ensembl_id: "ENSG00000167468"
name: "glutathione peroxidase 4"
location: "19p13.3"
module: 43
arm: "+"
pooled_cpm: 88.36
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# GPX4

*glutathione peroxidase 4* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.51× (z +6.7, q 1e-08, up in 46 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.95× (z +4.3, q 0.002, up in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 7.78×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.661× (z -3.8, q 0.091, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~95% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.0731×; ⚠ toxic; cell-cycle shift, explains ~61% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.242×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX4I1]] (+0.75, fdr 7e-06, ⚠ COX4I1 in the vector space only through flagged drug-doses), [[CDKN2D]] (+0.72, fdr 7e-06), [[RPL36]] (+0.70, fdr 9e-06), [[MIEN1]] (+0.70, fdr 7e-06); moves opposite to [[TMX3]] (-0.69, fdr 7e-06), [[SLC35B4]] (-0.66, fdr 1e-05), [[NUP155]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FBXO32]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9469.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 7.78×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.51×** | +6.7 | 1e-08 | 46/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.78×** | +6.4 | 5e-08 | 43/44 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.98×** | +4.4 | 0.002 | 44/48 (RPMI-7951, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +4.3 | 0.002 | 36/48 (Panc 03.27, KATO III, …) | two highest doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +4.3 | 0.002 | 28/50 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.98×** | +4.1 | 0.004 | 39/45 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.80×** | +3.8 | 0.012 | 40/48 (NCI-H460, RPMI-7951, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +3.4 | 0.043 | 28/48 (Panc 03.27, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9469.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.0731×; ⚠ toxic; cell-cycle shift, explains ~61% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.242×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.661×** | -3.8 | 0.091 | 36/48 (SK-MEL-2, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.569× | -3.4 | 0.16 | 36/47 (A-172, Panc 03.27, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.622× | -3.1 | 0.32 | 29/48 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.719× | -3.0 | 0.32 | 35/48 (CFPAC-1, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.82 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9469. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 93.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0731× (z -13.8) ⚠ toxic; cell-cycle shift, explains ~61% of this change |
| [[NCI-H1573 (line)]] | alt | 62.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.78× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 86.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 123 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 102 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 90.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 80.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 80.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9469), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 18 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX4I1]] ⚠ | +0.75 | +0.69 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 726; ⚠ in the vector space only through flagged drug-doses |
| [[CDKN2D]] | +0.72 | +0.59 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY |
| [[RPL36]] | +0.70 | +0.57 / +0.73 | both halves | 9e-06 |  |
| [[MIEN1]] | +0.70 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[HDAC5]] | +0.70 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[COX5A]] ⚠ | +0.70 | +0.57 / +0.68 | both halves | 9e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; ⚠ in the vector space only through flagged drug-doses |
| [[TOMM7]] | +0.70 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[GABARAP]] ⚠ | +0.69 | +0.60 / +0.66 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS16]] ⚠ | +0.69 | +0.51 / +0.69 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5ME]] | +0.68 | +0.49 / +0.71 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[GABARAPL2]] | +0.68 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[RPS27A]] ⚠ | +0.68 | +0.56 / +0.70 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS27]] | +0.66 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[RPS29]] | +0.66 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[RPS12]] | +0.65 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[ELOB]] | +0.65 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[ATP5F1E]] | +0.65 | +0.49 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMX3]] | -0.69 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[SLC35B4]] | -0.66 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[NUP155]] | -0.66 | -0.63 / -0.73 | both halves | 7e-06 |  |
| [[DPP3]] | -0.65 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[DARS2]] | -0.64 | -0.37 / -0.71 | both halves | 9e-05 |  |
| [[CRACR2A]] | -0.64 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[PSMD12]] | -0.64 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[ABCF2]] | -0.64 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[CCT5]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[PSME3]] | -0.62 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[NUP205]] | -0.61 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[NAA50]] | -0.61 | -0.54 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO32]] | B | FBXO32 activity lowers GPX4's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.49× higher at baseline in the lines without FBXO32 | 0.042 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[TBXAS1]] | B | TBXAS1 activity lowers GPX4's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 1.57× higher at baseline in the lines without TBXAS1 | 0.065 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-7.0, -47.0); signed map (-22.1, 13.3). **Vector** length 88.3, 43.1% of its response variance represented; |z| ≥ 3 in 501 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.51 to 55); *Peptide chain elongation* (reactome, mean cos +0.52 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.50 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.8 | +2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.6 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +1.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.7 | +0.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +1.9 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -6.6 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -6.5 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -6.2 | +6.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.2 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.2 | -0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.9 | -0.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | glutathione peroxidase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,103,982-1,106,791 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PHGPx, MCSP |
| Gene groups (HGNC) | Selenoproteins; Glutathione peroxidase family |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, APOPTOSIS, DNA_REPAIR, IL2_STAT5_SIGNALING, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 13 pathways, smallest: Biosynthesis of E-series 18(R)-resolvins; Biosynthesis of aspirin-triggered D-series resolvins; Biosynthesis of D-series resolvins |
| Matched by | ensembl_id |

**Function**, from UniProt [P36969](https://www.uniprot.org/uniprotkb/P36969) (Phospholipid hydroperoxide glutathione peroxidase GPX4):

> Essential antioxidant peroxidase that directly reduces phospholipid hydroperoxide even if they are incorporated in membranes and lipoproteins. Can also reduce cholesterol hydroperoxide and thymine hydroperoxide (By similarity). Plays a key role in protecting cells from oxidative damage by preventing membrane lipid peroxidation. Required to prevent cells from ferroptosis, a non-apoptotic cell death resulting from an iron-dependent accumulation of lipid reactive oxygen species. The presence of …

**Summary**, from NCBI Gene [2879](https://www.ncbi.nlm.nih.gov/gene/2879):

> The protein encoded by this gene belongs to the glutathione peroxidase family, members of which catalyze the reduction of hydrogen peroxide, organic hydroperoxides and lipid hydroperoxides, and thereby protect cells against oxidative damage. Several isozymes of this gene family exist in vertebrates, which vary in cellular location and substrate specificity. This isozyme has a high preference for lipid hydroperoxides and protects cells against membrane lipid peroxidation and cell death. It is …

**Accessions** — [HGNC:4556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4556) · Entrez [2879](https://www.ncbi.nlm.nih.gov/gene/2879) · UniProt [P36969](https://www.uniprot.org/uniprotkb/P36969) · Ensembl [ENSG00000167468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167468)

## Data

Gene col 9469: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9469); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9469, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9469]; `tensor/DDL_lfc|DDL_z.npy` [9469]; `embed/gene_vectors.npy` [9469]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9469 or target_col == 9469). Every well: [[GPX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
