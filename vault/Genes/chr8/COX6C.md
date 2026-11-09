---
symbol: "COX6C"
type: "gene"
col: 9029
ensembl_id: "ENSG00000164919"
name: "cytochrome c oxidase subunit 6C"
location: "8q22.2"
module: 48
arm: "+"
pooled_cpm: 88.12
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# COX6C

*cytochrome c oxidase subunit 6C* — 8q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.16× (z +7.8, q 3e-12, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HOP62 6.15×, A549 6.73×, NCI-H460 5.70×, C32 5.76×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.539× (z -5.2, q 1e-04, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX6A1]] (+0.88, fdr 7e-06), [[UBL5]] (+0.88, fdr 7e-06), [[UQCRQ]] (+0.87, fdr 7e-06, ⚠ UQCRQ in the vector space only through flagged drug-doses), [[COX7C]] (+0.87, fdr 7e-06); moves opposite to [[TEX261]] (-0.68, fdr 7e-06), [[ZXDB]] (-0.66, fdr 1e-05), [[ZNF460]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KRTCAP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9029.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HOP62 6.15×, A549 6.73×, NCI-H460 5.70×, C32 5.76×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **4.16×** | +7.8 | 3e-12 | 48/49 (HOP62, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.83×** | +6.1 | 2e-07 | 40/44 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.35×** | +4.8 | 2e-04 | 41/45 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.96×** | +4.1 | 0.005 | 42/48 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.78×** | +3.5 | 0.046 | 33/48 (PANC-1, A549, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.69× | +3.1 | 0.17 | 29/47 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.43× | +3.1 | 0.18 | 34/48 (Hs 766T, KATO III, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9029.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.539×** | -5.2 | 1e-04 | 40/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.462×** | -4.7 | 8e-04 | 42/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.337×** | -3.5 | 0.099 | 43/49 (NCI-H23, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.344×** | -3.4 | 0.099 | 45/49 (SHP-77, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.379× | -3.1 | 0.23 | 41/48 (BT-474, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 60.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A549 (line)]] | wt | 60.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.73× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[C32 (line)]] | wt | 92.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.76× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HOP62 (line)]] | alt | 67.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.15× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LoVo (line)]] | wt | 159 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 61.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[RKO (line)]] | wt | 147 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -8.6) |
| [[A-427 (line)]] | wt | 82.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 97.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 134 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 80.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 67.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 18 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX6A1]] | +0.88 | +0.81 / +0.91 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[UBL5]] | +0.88 | +0.82 / +0.88 | both halves | 7e-06 | STRING 401 |
| [[UQCRQ]] ⚠ | +0.87 | +0.78 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 998; ⚠ in the vector space only through flagged drug-doses |
| [[COX7C]] | +0.87 | +0.82 / +0.87 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[NDUFA4]] | +0.86 | +0.79 / +0.90 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[COX6B1]] | +0.85 | +0.79 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[ATP5MJ]] | +0.83 | +0.77 / +0.85 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 588 |
| [[ROMO1]] | +0.82 | +0.75 / +0.83 | both halves | 7e-06 | STRING 631 |
| [[ATP5MK]] | +0.81 | +0.67 / +0.85 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 915 |
| [[NDUFA1]] | +0.80 | +0.72 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 885 |
| [[UQCR11]] | +0.80 | +0.74 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 994 |
| [[UQCRH]] | +0.80 | +0.75 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 985 |
| [[NEDD8]] | +0.79 | +0.72 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX261]] | -0.68 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[ZXDB]] | -0.66 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[ZNF460]] | -0.64 | -0.45 / -0.67 | both halves | 3e-05 |  |
| [[SRSF6]] | -0.63 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ZNF681]] | -0.62 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[ZNF252P-1]] | -0.62 | -0.61 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRTCAP3]] | B | KRTCAP3 activity lowers COX6C's level | lines that do not express KRTCAP3 (7) vs lines expressing it (43) | 1.28× higher at baseline in the lines without KRTCAP3 | 0.051 | ⚠ within organs, on part of the lines; also absent: RNF103-CHMP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.872). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.3, -22.4); signed map (-34.9, 9.3). **Vector** length 77.8, 39.1% of its response variance represented; |z| ≥ 3 in 548 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.75 to 7); *Complex I biogenesis* (reactome, mean cos +0.61 to 9); *Cristae formation* (reactome, mean cos +0.75 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -0.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | +3.0 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | -0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +0.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -6.2 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -6.2 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -5.7 | +7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.2 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase subunit 6C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.2 — chr8:99,873,200-99,893,707 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Complex IV assembly; Cytoprotection by HMOX1; TP53 Regulates Metabolic Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P09669](https://www.uniprot.org/uniprotkb/P09669) (Cytochrome c oxidase subunit 6C):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [1345](https://www.ncbi.nlm.nih.gov/gene/1345):

> Cytochrome c oxidase, the terminal enzyme of the mitochondrial respiratory chain, catalyzes the electron transfer from reduced cytochrome c to oxygen. It is a heteromeric complex consisting of 3 catalytic subunits encoded by mitochondrial genes and multiple structural subunits encoded by nuclear genes. The mitochondrially-encoded subunits function in electron transfer, and the nuclear-encoded subunits may be involved in the regulation and assembly of the complex. This nuclear gene encodes …

**Accessions** — [HGNC:2285](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2285) · Entrez [1345](https://www.ncbi.nlm.nih.gov/gene/1345) · UniProt [P09669](https://www.uniprot.org/uniprotkb/P09669) · Ensembl [ENSG00000164919](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164919)

## Data

Gene col 9029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9029); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9029]; `tensor/DDL_lfc|DDL_z.npy` [9029]; `embed/gene_vectors.npy` [9029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9029 or target_col == 9029). Every well: [[COX6C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX6C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
