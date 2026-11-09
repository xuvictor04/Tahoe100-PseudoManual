---
symbol: "AK1"
type: "gene"
col: 2818
ensembl_id: "ENSG00000106992"
name: "adenylate kinase 1"
location: "9q34.11"
module: 62
arm: "+"
pooled_cpm: 8.7
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# AK1

*adenylate kinase 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.63× (z +11.0, q 3e-25, up in 28 of 29 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.68× (z +5.3, q 1e-05, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.360× (z -3.9, q 0.066, down in 21 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pexidartinib (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0477×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H2030 0.0909×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRA2]] (+0.60, fdr 3e-05), [[ARSA]] (+0.57, fdr 1e-04), [[APLP1]] (+0.57, fdr 1e-05); moves opposite to [[ZNF507]] (-0.46, fdr 0.002, ⚠ not reproduced), [[MRRF]] (-0.44, fdr 6e-04), [[DCPS]] (-0.44, fdr 7e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2818.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **4.63×** | +11.0 | 3e-25 | 28/29 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **3.20×** | +8.0 | 3e-13 | 16/16 (KATO III, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.97×** | +7.8 | 1e-12 | 44/47 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **2.76×** | +7.3 | 5e-11 | 39/47 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.79×** | +7.1 | 2e-10 | 27/33 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **2.13×** | +5.4 | 6e-06 | 33/47 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.3 | 1e-05 | 26/48 (A549, A498, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.54×** | +5.2 | 1e-05 | 20/23 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.93×** | +4.5 | 4e-04 | 29/42 (A498, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.88×** | +4.3 | 8e-04 | 20/41 (A498, A549, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.79×** | +4.1 | 0.002 | 19/36 (KATO III, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.002 | 23/48 (A498, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.48×** | +3.9 | 0.003 | 20/42 (A549, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.72×** | +3.9 | 0.004 | 23/45 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.68×** | +3.7 | 0.008 | 21/47 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +3.5 | 0.019 | 18/46 (HCT15, HOP62, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.073 | 13/47 (A498, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2818.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pexidartinib (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0477×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H2030 0.0909×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.360×** | -3.9 | 0.066 | 21/45 (LS 180, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.441× | -3.1 | 0.58 | 15/48 (LS 180, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.81 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2818. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 22.2 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +8.6) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[A549 (line)]] | wt | 6.91 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +10.3) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H2030 (line)]] | alt | 7.25 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0909× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[NCI-H23 (line)]] | alt | 4.13 | 0 | 1 | — | [[Pexidartinib (hydrochloride) (drug)]] 5 µM 0.0477× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 6.01 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +9.0) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[A-172 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2818), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 17 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRA2]] | +0.60 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[ARSA]] | +0.57 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[APLP1]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[HES6]] | +0.54 | +0.33 / +0.63 | both halves | 1e-04 |  |
| [[CEP85L]] | +0.53 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[KDM4B]] | +0.53 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[HRAS]] | +0.53 | +0.38 / +0.52 | both halves | 6e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[PCSK1N]] | +0.53 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[C4orf48]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[NTN1]] | +0.52 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[CDKN1A]] | +0.52 | +0.41 / +0.59 | both halves | 4e-05 | pathway: HALLMARK_MYOGENESIS |
| [[SLC29A4]] | +0.51 | +0.33 / +0.48 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF507]] | -0.46 | -0.14 / -0.45 | ⚠ not reproduced | 0.002 |  |
| [[MRRF]] | -0.44 | -0.21 / -0.43 | both halves | 6e-04 | STRING 633 |
| [[DCPS]] | -0.44 | -0.21 / -0.36 | both halves | 7e-04 |  |
| [[UTP20]] | -0.43 | -0.16 / -0.41 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AK1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.479). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.9, -22.2); signed map (-37.5, 15.2). **Vector** length 59.3, 11.0% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.0 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +2.8 | +11.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +0.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +1.6 |
| fall | [[Sapanisertib (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -2.2 |
|  | [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | adenylate kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:127,866,486-127,877,675 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADK, Adk1 |
| Gene groups (HGNC) | Adenylate kinases; MicroRNA protein coding host genes |
| Hallmark sets | MYOGENESIS, DNA_REPAIR, P53_PATHWAY |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P00568](https://www.uniprot.org/uniprotkb/P00568) (Adenylate kinase isoenzyme 1):

> Catalyzes the reversible transfer of the terminal phosphate group between ATP and AMP. Also displays broad nucleoside diphosphate kinase activity. Plays an important role in cellular energy homeostasis and in adenine nucleotide metabolism (By similarity). Also catalyzes at a very low rate the synthesis of thiamine triphosphate (ThTP) from thiamine diphosphate (ThDP) and ADP (By similarity).

**Summary**, from NCBI Gene [203](https://www.ncbi.nlm.nih.gov/gene/203):

> This gene encodes an adenylate kinase enzyme involved in energy metabolism and homeostasis of cellular adenine nucleotide ratios in different intracellular compartments. This gene is highly expressed in skeletal muscle, brain and erythrocytes. Certain mutations in this gene resulting in a functionally inadequate enzyme are associated with a rare genetic disorder causing nonspherocytic hemolytic anemia. Alternative splicing of this gene results in multiple transcript variants encoding different …

**Accessions** — [HGNC:361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:361) · Entrez [203](https://www.ncbi.nlm.nih.gov/gene/203) · UniProt [P00568](https://www.uniprot.org/uniprotkb/P00568) · Ensembl [ENSG00000106992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106992)

## Data

Gene col 2818: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2818); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2818, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2818]; `tensor/DDL_lfc|DDL_z.npy` [2818]; `embed/gene_vectors.npy` [2818]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2818 or target_col == 2818). Every well: [[AK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
