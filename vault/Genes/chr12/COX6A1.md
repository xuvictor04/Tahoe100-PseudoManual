---
symbol: "COX6A1"
type: "gene"
col: 3277
ensembl_id: "ENSG00000111775"
name: "cytochrome c oxidase subunit 6A1"
location: "12q24.31"
module: 48
arm: "+"
pooled_cpm: 71.16
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# COX6A1

*cytochrome c oxidase subunit 6A1* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.19× (z +6.8, q 5e-09, up in 43 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 4.68×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.635× (z -4.0, q 0.042, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.301×); [[Cytarabine (drug)]] 5 µM in 1 line (NCI-H661 0.0700×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBL5]] (+0.89, fdr 7e-06), [[COX6C]] (+0.88, fdr 7e-06), [[ATP5MJ]] (+0.86, fdr 7e-06); moves opposite to [[ZXDB]] (-0.75, fdr 7e-06), [[SRSF6]] (-0.69, fdr 1e-05), [[EIF4G2]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3277.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 4.68×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **3.19×** | +6.8 | 5e-09 | 43/43 (SW 900, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **4.26×** | +6.5 | 2e-08 | 47/49 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.87×** | +6.4 | 2e-08 | 48/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **2.29×** | +5.1 | 6e-05 | 48/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.40×** | +5.0 | 8e-05 | 43/45 (HS-578T, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.20×** | +4.8 | 1e-04 | 47/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **2.05×** | +4.4 | 9e-04 | 43/47 (HS-578T, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **2.05×** | +4.4 | 9e-04 | 45/47 (SW480, NCI-H23, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +4.0 | 0.003 | 44/47 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.44×** | +3.2 | 0.091 | 31/48 (NCI-H2347, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3277.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.301×); [[Cytarabine (drug)]] 5 µM in 1 line (NCI-H661 0.0700×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.635×** | -4.0 | 0.042 | 34/48 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 5 µM |  | 0.359× | -3.3 | 0.28 | 43/49 (AsPC-1, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.64 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3277. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H661 (line)]] | alt | 64.4 | 0 | 1 | — | [[Cytarabine (drug)]] 5 µM 0.0700× (z -8.7) |
| [[RKO (line)]] | wt | 63.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -9.0) |
| [[SW 900 (line)]] | alt | 78.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.68× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[A-172 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 95.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 73.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 70.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 108 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 58.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3277), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 14 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBL5]] | +0.89 | +0.90 / +0.89 | both halves | 7e-06 | STRING 424 |
| [[COX6C]] | +0.88 | +0.81 / +0.91 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[ATP5MJ]] | +0.86 | +0.78 / +0.83 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 413 |
| [[UQCRQ]] ⚠ | +0.86 | +0.77 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS; STRING 996; ⚠ in the vector space only through flagged drug-doses |
| [[ANAPC11]] | +0.85 | +0.82 / +0.78 | both halves | 7e-06 |  |
| [[ELOB]] | +0.84 | +0.78 / +0.77 | both halves | 7e-06 |  |
| [[ATP5MK]] | +0.83 | +0.78 / +0.84 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 461 |
| [[SNRPD2]] | +0.83 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[ROMO1]] | +0.83 | +0.77 / +0.86 | both halves | 7e-06 | STRING 464 |
| [[RPLP2]] | +0.82 | +0.77 / +0.81 | both halves | 7e-06 |  |
| [[UQCR11]] | +0.81 | +0.80 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS; STRING 971 |
| [[COMMD6]] | +0.80 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[COX7C]] | +0.79 | +0.76 / +0.85 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDB]] | -0.75 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[SRSF6]] | -0.69 | -0.57 / -0.67 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.68 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[NCR3LG1]] | -0.68 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[KICS2]] | -0.68 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[GUF1]] | -0.67 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[ZXDA]] | -0.67 | -0.57 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers COX6A1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[OXR1]] | C | OXR1 activity weakens COX6A1's drug response | lines that do not express OXR1 (4) vs lines expressing it (45) | the lines without OXR1 respond 1.08× as strongly (z diff -0.73); strongest at Panobinostat 5 µM: 3.25x vs 2.26x (z diff -1.5) | 0.047 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.895). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.2, -21.7); signed map (-34.4, 9.6). **Vector** length 73.6, 35.4% of its response variance represented; |z| ≥ 3 in 609 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.73 to 7); *Complex I biogenesis* (reactome, mean cos +0.55 to 9); *Cristae formation* (reactome, mean cos +0.73 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.6 | +6.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.5 | +4.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.1 | +5.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | +3.0 | +4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +0.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.0 | +1.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | -6.5 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -6.2 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -6.1 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | +0.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.7 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase subunit 6A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:120,438,090-120,440,737 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COX6AL; previously COX6A |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Complex IV assembly; Cytoprotection by HMOX1; TP53 Regulates Metabolic Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P12074](https://www.uniprot.org/uniprotkb/P12074) (Cytochrome c oxidase subunit 6A1, mitochondrial):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [1337](https://www.ncbi.nlm.nih.gov/gene/1337):

> Cytochrome c oxidase (COX), the terminal enzyme of the mitochondrial respiratory chain, catalyzes the electron transfer from reduced cytochrome c to oxygen. It is a heteromeric complex consisting of 3 catalytic subunits encoded by mitochondrial genes and multiple structural subunits encoded by nuclear genes. The mitochondrially-encoded subunits function in the electron transfer and the nuclear-encoded subunits may function in the regulation and assembly of the complex. This nuclear gene encodes …

**Accessions** — [HGNC:2277](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2277) · Entrez [1337](https://www.ncbi.nlm.nih.gov/gene/1337) · UniProt [P12074](https://www.uniprot.org/uniprotkb/P12074) · Ensembl [ENSG00000111775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111775)

## Data

Gene col 3277: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3277); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3277, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3277]; `tensor/DDL_lfc|DDL_z.npy` [3277]; `embed/gene_vectors.npy` [3277]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3277 or target_col == 3277). Every well: [[COX6A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX6A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
