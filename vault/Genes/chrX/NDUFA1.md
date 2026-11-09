---
symbol: "NDUFA1"
type: "gene"
col: 4606
ensembl_id: "ENSG00000125356"
name: "NADH:ubiquinone oxidoreductase subunit A1"
location: "Xq24"
module: 48
arm: "+"
pooled_cpm: 65.87
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# NDUFA1

*NADH:ubiquinone oxidoreductase subunit A1* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.89× (z +7.9, q 2e-12, up in 48 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 8.22×, A549 6.35×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.639× (z -3.8, q 0.075, down in 34 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.327×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX6B1]] (+0.87, fdr 7e-06), [[COX7A2]] (+0.84, fdr 7e-06, ⚠ COX7A2 in the vector space only through flagged drug-doses), [[UQCRB]] (+0.84, fdr 7e-06, ⚠ UQCRB in the vector space only through flagged drug-doses), [[ATP5MK]] (+0.84, fdr 7e-06), [[NDUFA4]] (+0.82, fdr 7e-06); moves opposite to [[PSMG1]] (-0.67, fdr 7e-06), [[NRAS]] (-0.66, fdr 7e-06), [[PRELID3B]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Bendamustine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4606.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 8.22×, A549 6.35×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.89×** | +7.9 | 2e-12 | 48/48 (RKO, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.93×** | +6.3 | 7e-08 | 40/41 (HEC-1-A, C32, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.08×** | +4.5 | 0.001 | 46/48 (NCI-H460, PANC-1, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.06×** | +4.1 | 0.006 | 37/44 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.86×** | +3.8 | 0.016 | 39/47 (Panc 03.27, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4606.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.327×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.639×** | -3.8 | 0.075 | 34/47 (Panc 03.27, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Folic acid (drug)]] 5 µM |  | 0.686× | -3.2 | 0.20 | 37/48 (NCI-H1573, SW1417, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.352× | -3.2 | 0.20 | 39/48 (A-427, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.572× | -3.1 | 0.20 | 42/48 (HCT15, HEC-1-A, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.363× | -3.1 | 0.20 | 43/49 (HEC-1-A, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.576× | -3.1 | 0.20 | 40/48 (C32, LoVo, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.584× | -3.0 | 0.21 | 42/48 (SW 1271, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4606. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 64.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.35× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[Panc 03.27 (line)]] | alt | 49.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -8.5) |
| [[RKO (line)]] | wt | 46.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.22× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 88.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 76.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 126 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 77.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 76.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4606), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 25 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX6B1]] | +0.87 | +0.82 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 979 |
| [[COX7A2]] ⚠ | +0.84 | +0.78 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 824; ⚠ in the vector space only through flagged drug-doses |
| [[UQCRB]] ⚠ | +0.84 | +0.80 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 948; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | +0.84 | +0.80 / +0.89 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 485 |
| [[NDUFA4]] | +0.82 | +0.75 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 995 |
| [[NDUFB11]] ⚠ | +0.82 | +0.81 / +0.78 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5PD]] | +0.81 | +0.64 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 725 |
| [[ROMO1]] | +0.81 | +0.80 / +0.84 | both halves | 7e-06 | STRING 498 |
| [[SERF2]] | +0.81 | +0.81 / +0.79 | both halves | 7e-06 |  |
| [[ATP5F1E]] | +0.80 | +0.76 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 840 |
| [[COX4I1]] ⚠ | +0.80 | +0.75 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 943; ⚠ in the vector space only through flagged drug-doses |
| [[COX6C]] | +0.80 | +0.72 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 885 |
| [[COX7C]] | +0.79 | +0.71 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 990 |
| [[TMEM258]] | +0.79 | +0.73 / +0.83 | both halves | 7e-06 |  |
| [[UBL5]] | +0.79 | +0.76 / +0.84 | both halves | 7e-06 | STRING 403 |
| [[LAMTOR5]] | +0.78 | +0.73 / +0.85 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMG1]] | -0.67 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[NRAS]] | -0.66 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[PRELID3B]] | -0.65 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[SF3B4]] | -0.65 | -0.56 / -0.72 | both halves | 1e-05 |  |
| [[AKAP11]] | -0.64 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[TWF1]] | -0.64 | -0.57 / -0.64 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bendamustine (drug)]] 0.5 µM | C | NDUFA1's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | NDUFA1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.425 over the table, 0.085 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.854). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.1, -22.6); signed map (-35.0, 9.3). **Vector** length 66.1, 29.2% of its response variance represented; |z| ≥ 3 in 449 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Complex IV assembly* (reactome, mean cos +0.74 to 11); *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.76 to 7); *Cytoprotection by HMOX1* (reactome, mean cos +0.74 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +3.9 | +4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | -0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | -0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | -0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -4.6 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -4.2 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -3.9 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | +0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | +0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -0.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | +0.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.4 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:119,871,832-119,876,662 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MWFE, CI-MWFE |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O15239](https://www.uniprot.org/uniprotkb/O15239) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4694](https://www.ncbi.nlm.nih.gov/gene/4694):

> The human NDUFA1 gene codes for an essential component of complex I of the respiratory chain, which transfers electrons from NADH to ubiquinone. It has been noted that the N-terminal hydrophobic domain has the potential to be folded into an alpha-helix spanning the inner mitochondrial membrane with a C-terminal hydrophilic domain interacting with globular subunits of complex I. The highly conserved two-domain structure suggests that this feature is critical for the protein function and might …

**Accessions** — [HGNC:7683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7683) · Entrez [4694](https://www.ncbi.nlm.nih.gov/gene/4694) · UniProt [O15239](https://www.uniprot.org/uniprotkb/O15239) · Ensembl [ENSG00000125356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125356)

## Data

Gene col 4606: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4606); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4606, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4606]; `tensor/DDL_lfc|DDL_z.npy` [4606]; `embed/gene_vectors.npy` [4606]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4606 or target_col == 4606). Every well: [[NDUFA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
