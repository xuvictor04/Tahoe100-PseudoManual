---
symbol: "BBLN"
type: "gene"
col: 10063
ensembl_id: "ENSG00000171159"
name: "bublin coiled coil protein"
location: "9q34.11"
module: 48
arm: "+"
pooled_cpm: 13.47
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# BBLN

*bublin coiled coil protein* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.72× (z +9.3, q 1e-17, up in 46 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 0.5 µM in 1 line (HOP62 7.74×).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.680× (z -3.8, q 0.068, down in 24 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.262×, LOX-IMVI 0.178×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (SNU-423 0.0649×; ⚠ cell-cycle shift, explains ~74% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELOB]] (+0.78, fdr 7e-06), [[COX6A1]] (+0.76, fdr 7e-06), [[NDUFA2]] (+0.75, fdr 1e-05); moves opposite to [[SRSF6]] (-0.64, fdr 2e-05), [[EXOSC10]] (-0.63, fdr 6e-05), [[EWSR1]] (-0.63, fdr 4e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10063.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 0.5 µM in 1 line (HOP62 7.74×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.72×** | +9.3 | 1e-17 | 46/47 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.20×** | +7.8 | 2e-12 | 33/36 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.93×** | +7.6 | 6e-12 | 44/47 (HOP62, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +6.8 | 1e-09 | 39/45 (A-172, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.40×** | +6.2 | 8e-08 | 43/47 (HOP62, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +5.8 | 7e-07 | 33/40 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **2.28×** | +5.6 | 2e-06 | 14/22 (Hs 766T, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.79×** | +4.1 | 0.003 | 24/41 (NCI-H2030, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.71×** | +3.8 | 0.009 | 29/47 (HOP62, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.73×** | +3.6 | 0.020 | 21/28 (LoVo, HOP62, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10063.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.262×, LOX-IMVI 0.178×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (SNU-423 0.0649×; ⚠ cell-cycle shift, explains ~74% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.680×** | -3.8 | 0.068 | 24/44 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.624× | -3.1 | 0.49 | 21/47 (BT-474, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10063. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 32.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -10.1) |
| [[HOP62 (line)]] | alt | 7.54 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.74× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 6.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -8.9) |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0649× (z -10.6) ⚠ cell-cycle shift, explains ~74% of this change |
| [[A-172 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10063), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELOB]] | +0.78 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[COX6A1]] | +0.76 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[NDUFA2]] | +0.75 | +0.52 / +0.77 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.75 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[TMEM256]] | +0.74 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ANAPC11]] | +0.74 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[MRPL41]] ⚠ | +0.73 | +0.62 / +0.69 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MPG]] | +0.73 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[SSR4]] | +0.73 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[ATP5MJ]] | +0.72 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[C4orf48]] | +0.72 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[UQCR11]] | +0.71 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[DDT]] | +0.71 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF6]] | -0.64 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[EXOSC10]] | -0.63 | -0.39 / -0.67 | both halves | 6e-05 |  |
| [[EWSR1]] | -0.63 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[TASOR]] | -0.63 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[NRAS]] | -0.61 | -0.39 / -0.68 | both halves | 5e-05 |  |
| [[U2SURP]] | -0.61 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[ZXDB]] | -0.60 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[YWHAE]] | -0.60 | -0.38 / -0.62 | both halves | 7e-05 |  |
| [[MAGOHB]] | -0.60 | -0.57 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers BBLN's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.764). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.1, -20.4); signed map (-33.4, 9.5). **Vector** length 71.6, 18.3% of its response variance represented; |z| ≥ 3 in 654 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.55 to 31); *Respiratory electron transport* (reactome, mean cos +0.54 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.56 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +9.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.9 | +7.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.8 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +1.2 |
|  | [[Decitabine (drug)]] 0.5 µM |  | +1.1 | +1.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.1 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | bublin coiled coil protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,160,265-128,163,924 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hero9, MGC4639, EST00098, FLJ12823; previously C9orf16 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUW7](https://www.uniprot.org/uniprotkb/Q9BUW7) (Bublin coiled-coil protein):

> Essential for intermediate filament organization in intestinal cells, interacts with intermediate filament and regulates intestinal lumen morphology.

**Summary**, from NCBI Gene [79095](https://www.ncbi.nlm.nih.gov/gene/79095):

> Enables molecular adaptor activity. Involved in intermediate filament bundle assembly. Located in cell junction; polymeric cytoskeletal fiber; and subapical part of cell. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17823](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17823) · Entrez [79095](https://www.ncbi.nlm.nih.gov/gene/79095) · UniProt [Q9BUW7](https://www.uniprot.org/uniprotkb/Q9BUW7) · Ensembl [ENSG00000171159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171159)

## Data

Gene col 10063: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10063); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10063, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10063]; `tensor/DDL_lfc|DDL_z.npy` [10063]; `embed/gene_vectors.npy` [10063]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10063 or target_col == 10063). Every well: [[BBLN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BBLN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
