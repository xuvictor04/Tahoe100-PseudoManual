---
symbol: "ANAPC11"
type: "gene"
col: 6543
ensembl_id: "ENSG00000141552"
name: "anaphase promoting complex subunit 11"
location: "17q25.3"
module: 48
arm: "+"
pooled_cpm: 35.29
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ANAPC11

*anaphase promoting complex subunit 11* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.24× (z +7.1, q 7e-10, up in 41 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.480× (z -7.3, q 2e-10, down in 42 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.112×, NCI-H2030 0.287×, NCI-H2347 0.373×, SW 900 0.321×); [[Harringtonine (drug)]] 5 µM in 1 line (H4 0.0787×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.180×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX6A1]] (+0.85, fdr 7e-06), [[ELOB]] (+0.83, fdr 7e-06), [[MRPL41]] (+0.83, fdr 7e-06, ⚠ MRPL41 in the vector space only through flagged drug-doses), [[ATP5MJ]] (+0.82, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.75, fdr 1e-05), [[RNF6]] (-0.71, fdr 2e-05), [[EIF5]] (-0.69, fdr 1e-04).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF655]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.24×** | +7.1 | 7e-10 | 41/43 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.49×** | +5.7 | 3e-06 | 32/36 (A549, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **2.09×** | +5.2 | 5e-05 | 43/46 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.95×** | +4.3 | 0.002 | 35/41 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.60×** | +3.3 | 0.089 | 34/48 (COLO 205, RKO, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.3 | 0.089 | 31/46 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6543.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.112×, NCI-H2030 0.287×, NCI-H2347 0.373×, SW 900 0.321×); [[Harringtonine (drug)]] 5 µM in 1 line (H4 0.0787×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.180×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.480×** | -7.3 | 2e-10 | 42/47 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.592×** | -3.7 | 0.068 | 29/47 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.386× | -3.3 | 0.19 | 35/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 40.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -16.9) |
| [[H4 (line)]] | wt | 28.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0787× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 58.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 50.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.0) |
| [[SW 900 (line)]] | alt | 36.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -8.9) |
| [[A-172 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 34.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 10 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX6A1]] | +0.85 | +0.82 / +0.78 | both halves | 7e-06 |  |
| [[ELOB]] | +0.83 | +0.75 / +0.76 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 661 |
| [[MRPL41]] ⚠ | +0.83 | +0.61 / +0.84 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MJ]] | +0.82 | +0.67 / +0.81 | both halves | 7e-06 |  |
| [[LSM2]] | +0.81 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[SIVA1]] | +0.79 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[C4orf48]] | +0.79 | +0.59 / +0.80 | both halves | 7e-06 |  |
| [[SNRPD2]] | +0.79 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[TMEM256]] | +0.79 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[LAMTOR5]] | +0.77 | +0.63 / +0.82 | both halves | 7e-06 |  |
| [[UQCRQ]] ⚠ | +0.77 | +0.71 / +0.79 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[YIF1B]] | +0.77 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[UQCR11]] | +0.76 | +0.71 / +0.79 | both halves | 7e-06 | STRING 458 |
| [[TMEM160]] | +0.75 | +0.55 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.75 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[RNF6]] | -0.71 | -0.67 / -0.47 | both halves | 2e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[EIF5]] | -0.69 | -0.69 / -0.34 | both halves | 1e-04 |  |
| [[ZXDB]] | -0.68 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[ZXDA]] | -0.67 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[HNRNPU]] | -0.66 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ZNF300]] | -0.66 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[KRT8P12]] | -0.65 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[PSME3IP1]] | -0.65 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[KRR1]] | -0.65 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[ZNF655]] | -0.65 | -0.47 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF655]] | B | ZNF655 activity lowers ANAPC11's level | lines that do not express ZNF655 (7) vs lines expressing it (43) | 1.41× higher at baseline in the lines without ZNF655 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.811). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.3, -19.2); signed map (-33.7, 7.9). **Vector** length 67.7, 24.0% of its response variance represented; |z| ≥ 3 in 430 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.61 to 31); *Respiratory electron transport* (reactome, mean cos +0.60 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.62 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.2 | +3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.2 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.4 | +0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.0 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | -1.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -4.5 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -4.3 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | anaphase promoting complex subunit 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,890,790-81,900,991 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC214, APC11, Apc11p, MGC882 |
| Gene groups (HGNC) | Ring finger proteins; Anaphase promoting complex; RING finger E3 ubiquitin protein ligases; Degenerate RING E3 ubiquitin ligases |
| Reactome | 42 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYG5](https://www.uniprot.org/uniprotkb/Q9NYG5) (Anaphase-promoting complex subunit 11):

> Component of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated E3 ubiquitin ligase that controls progression through the cell cycle. Together with ANAPC2, forms the catalytic component of the E3 ubiquitin ligase complex. APC/C acts by mediating ubiquitination and subsequent degradation of target proteins: it mainly mediates the formation of 'Lys-11'-linked polyubiquitin chains and, to a lower extent, the formation of 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains. …

**Summary**, from NCBI Gene [51529](https://www.ncbi.nlm.nih.gov/gene/51529):

> Enables cullin family protein binding activity and ubiquitin-ubiquitin ligase activity. Contributes to ubiquitin-protein transferase activity. Involved in anaphase-promoting complex-dependent catabolic process; positive regulation of mitotic metaphase/anaphase transition; and protein polyubiquitination. Located in nucleolus and nucleoplasm. Part of anaphase-promoting complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14452) · Entrez [51529](https://www.ncbi.nlm.nih.gov/gene/51529) · UniProt [Q9NYG5](https://www.uniprot.org/uniprotkb/Q9NYG5) · Ensembl [ENSG00000141552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141552)

## Data

Gene col 6543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6543); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6543]; `tensor/DDL_lfc|DDL_z.npy` [6543]; `embed/gene_vectors.npy` [6543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6543 or target_col == 6543). Every well: [[ANAPC11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANAPC11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
