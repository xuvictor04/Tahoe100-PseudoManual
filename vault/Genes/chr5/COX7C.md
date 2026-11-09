---
symbol: "COX7C"
type: "gene"
col: 4793
ensembl_id: "ENSG00000127184"
name: "cytochrome c oxidase subunit 7C"
location: "5q14.3"
module: 48
arm: "+"
pooled_cpm: 72.72
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# COX7C

*cytochrome c oxidase subunit 7C* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.53× (z +7.5, q 4e-11, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 4.79×, NCI-H1792 5.95×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A549 5.92×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.521× (z -6.1, q 6e-07, down in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (SNU-1 0.218×, KATO III 0.322×, A-427 0.315×, NCI-H460 0.358×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX6C]] (+0.87, fdr 7e-06), [[UQCRB]] (+0.86, fdr 7e-06, ⚠ UQCRB in the vector space only through flagged drug-doses), [[TOMM7]] (+0.85, fdr 7e-06), [[RPS14]] (+0.85, fdr 7e-06).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RPS6]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4793.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 4.79×, NCI-H1792 5.95×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A549 5.92×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.53×** | +7.5 | 4e-11 | 47/49 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.02×** | +7.0 | 5e-10 | 40/43 (A-172, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.21×** | +4.9 | 2e-04 | 39/45 (C-33 A, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **2.00×** | +4.6 | 6e-04 | 38/48 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.70×** | +3.5 | 0.045 | 36/48 (NCI-H1573, COLO 205, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.67× | +3.3 | 0.11 | 34/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4793.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (SNU-1 0.218×, KATO III 0.322×, A-427 0.315×, NCI-H460 0.358×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.521×** | -6.1 | 6e-07 | 43/48 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.556×** | -3.9 | 0.030 | 35/48 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4793. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 47.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.79× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.8) |
| [[A549 (line)]] | wt | 57.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 83.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 39.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.95× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H460 (line)]] | wt | 75.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -8.5) |
| [[SNU-1 (line)]] | wt | 63.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -10.9) |
| [[A498 (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 100 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 69.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 141 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 59.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4793), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 20 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX6C]] | +0.87 | +0.82 / +0.87 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[UQCRB]] ⚠ | +0.86 | +0.77 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[TOMM7]] | +0.85 | +0.80 / +0.86 | both halves | 7e-06 | STRING 859 |
| [[RPS14]] | +0.85 | +0.81 / +0.85 | both halves | 7e-06 | STRING 509 |
| [[COX6B1]] | +0.84 | +0.76 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[RPLP1]] | +0.83 | +0.80 / +0.82 | both halves | 7e-06 |  |
| [[RPS19]] | +0.83 | +0.77 / +0.85 | both halves | 7e-06 | same gene group |
| [[RPL35A]] | +0.83 | +0.74 / +0.85 | both halves | 7e-06 | STRING 809 |
| [[UQCR11]] | +0.83 | +0.76 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 995 |
| [[RPL31]] | +0.82 | +0.74 / +0.84 | both halves | 7e-06 | STRING 835 |
| [[NDUFA4]] | +0.82 | +0.75 / +0.86 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[UBA52]] | +0.82 | +0.76 / +0.83 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[ATP5MJ]] | +0.82 | +0.77 / +0.87 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 555 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPS6]] | C | RPS6's natural level strengthens COX7C's drug response | RPS6's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse -0.13; direction not clear | 0.0995 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.858). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.1, -23.3); signed map (-35.1, 8.7). **Vector** length 65.2, 29.1% of its response variance represented; |z| ≥ 3 in 424 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.74 to 7); *Complex I biogenesis* (reactome, mean cos +0.63 to 9); *Cristae formation* (reactome, mean cos +0.74 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | +2.6 | +3.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | -0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -1.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -3.9 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -3.8 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.6 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | +0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase subunit 7C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.3 — chr5:86,617,928-86,620,962 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits; MicroRNA protein coding host genes |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Complex IV assembly; Cytoprotection by HMOX1; TP53 Regulates Metabolic Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P15954](https://www.uniprot.org/uniprotkb/P15954) (Cytochrome c oxidase subunit 7C, mitochondrial):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [1350](https://www.ncbi.nlm.nih.gov/gene/1350):

> Cytochrome c oxidase (COX), the terminal component of the mitochondrial respiratory chain, catalyzes the electron transfer from reduced cytochrome c to oxygen. This component is a heteromeric complex consisting of 3 catalytic subunits encoded by mitochondrial genes and multiple structural subunits encoded by nuclear genes. The mitochondrially-encoded subunits function in electron transfer, and the nuclear-encoded subunits may function in the regulation and assembly of the complex. This nuclear …

**Accessions** — [HGNC:2292](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2292) · Entrez [1350](https://www.ncbi.nlm.nih.gov/gene/1350) · UniProt [P15954](https://www.uniprot.org/uniprotkb/P15954) · Ensembl [ENSG00000127184](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127184)

## Data

Gene col 4793: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4793); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4793, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4793]; `tensor/DDL_lfc|DDL_z.npy` [4793]; `embed/gene_vectors.npy` [4793]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4793 or target_col == 4793). Every well: [[COX7C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX7C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
