---
symbol: "MICOS13"
type: "gene"
col: 10542
ensembl_id: "ENSG00000174917"
name: "mitochondrial contact site and cristae organizing system subunit 13"
location: "19p13.3"
module: 58
arm: "+"
pooled_cpm: 7.56
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# MICOS13

*mitochondrial contact site and cristae organizing system subunit 13* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.01× (z +8.1, q 4e-13, up in 28 of 30 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 7.98×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.238× (z -11.8, q 4e-29, down in 40 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H2030 0.0845×, PANC-1 0.114×, SW480 0.103×, NCI-H460 0.129×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0384×); [[Roxadustat (drug)]] 5 µM in 1 line (NCI-H23 0.0550×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C4orf48]] (+0.82, fdr 7e-06), [[MRPL41]] (+0.79, fdr 1e-05, ⚠ MRPL41 in the vector space only through flagged drug-doses), [[TMEM276]] (+0.78, fdr 7e-06), [[UQCR11]] (+0.77, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.62, fdr 5e-05), [[PRKAR1A]] (-0.60, fdr 8e-04, ⚠ one half only (not replicated)).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10542.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 7.98×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.01×** | +8.1 | 4e-13 | 28/30 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +6.4 | 6e-08 | 11/12 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **2.01×** | +4.0 | 0.010 | 21/38 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.94×** | +3.5 | 0.057 | 13/21 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.69× | +3.1 | 0.24 | 13/40 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.71× | +3.0 | 0.24 | 15/33 (RPMI-7951, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10542.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H2030 0.0845×, PANC-1 0.114×, SW480 0.103×, NCI-H460 0.129×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0384×); [[Roxadustat (drug)]] 5 µM in 1 line (NCI-H23 0.0550×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.238×** | -11.8 | 4e-29 | 40/42 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.305×** | -6.9 | 2e-09 | 35/41 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.556× | -3.2 | 0.24 | 19/45 (LOX-IMVI, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10542. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.98× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -9.5) |
| [[A549 (line)]] | wt | 5.51 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0886× (z -11.2) |
| [[BT-474 (line)]] | alt | 5.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0998× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 4.49 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0576× (z -9.5) |
| [[Hs 766T (line)]] | wt | 6.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0762× (z -11.2) |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -11.1) |
| [[J82 (line)]] | alt | 6.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -10.7) |
| [[LoVo (line)]] | wt | 6.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 6.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0384× (z -11.3) |
| [[LS 180 (line)]] | wt | 7.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0969× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0845× (z -15.0) |
| [[NCI-H23 (line)]] | alt | 5.36 | 0 | 1 | — | [[Roxadustat (drug)]] 5 µM 0.0550× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 4.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 8.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -10.6) |
| [[PANC-1 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 8.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -9.7) |
| [[SW480 (line)]] | alt | 6.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -13.5) |
| [[A-427 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10542), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 14 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C4orf48]] | +0.82 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[MRPL41]] ⚠ | +0.79 | +0.53 / +0.76 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM276]] | +0.78 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[UQCR11]] | +0.77 | +0.73 / +0.69 | both halves | 7e-06 | STRING 597 |
| [[NDUFA11]] ⚠ | +0.77 | +0.53 / +0.76 | both halves | 1e-05 | STRING 641; ⚠ in the vector space only through flagged drug-doses |
| [[METRN]] | +0.76 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[ANAPC11]] | +0.75 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SLC39A4]] | +0.74 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[SF3B5]] ⚠ | +0.74 | +0.47 / +0.77 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MJ]] | +0.74 | +0.45 / +0.72 | both halves | 3e-05 | pathway: Cristae formation |
| [[LAMTOR2]] | +0.74 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[TMEM256]] | +0.74 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ANTKMT]] | +0.73 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[LSM2]] | +0.72 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[ATP5MK]] | +0.72 | +0.57 / +0.67 | both halves | 1e-05 | pathway: Cristae formation |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.62 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[PRKAR1A]] | -0.60 | -0.20 / -0.65 | ⚠ one half (not replicated) | 8e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.862). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-46.6, -18.9); signed map (-33.4, 7.1). **Vector** length 52.7, 10.4% of its response variance represented; |z| ≥ 3 in 560 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *oxidative phosphorylation* (hallmark, mean cos +0.51 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | -0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | +2.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.7 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.1 | +1.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.1 | +1.4 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.1 | +3.1 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.1 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -11.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial contact site and cristae organizing system subunit 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:5,678,421-5,680,516 (-) |
| Ensembl biotype | protein_coding |
| Also known as | QIL1, P117, MIC13, MIC12; previously C19orf70 |
| Gene groups (HGNC) | Mitochondrial contact site and cristae organizing system subunits |
| Reactome | 3 pathways, smallest: Cristae formation; Mitochondrial biogenesis; Organelle biogenesis and maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5XKP0](https://www.uniprot.org/uniprotkb/Q5XKP0) (MICOS complex subunit MIC13):

> Component of the MICOS complex, a large protein complex of the mitochondrial inner membrane that plays crucial roles in the maintenance of crista junctions, inner membrane architecture, and formation of contact sites to the outer membrane. Constituent of mature MICOS complex, it is required for the formation of cristae junction (CJ) and maintenance of cristae morphology. Required for the incorporation of MICOS10/MIC10 into the MICOS complex.

**Summary**, from NCBI Gene [125988](https://www.ncbi.nlm.nih.gov/gene/125988):

> Involved in cristae formation. Located in mitochondrial crista junction. Part of MICOS complex. Implicated in combined oxidative phosphorylation deficiency 37. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33702](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33702) · Entrez [125988](https://www.ncbi.nlm.nih.gov/gene/125988) · UniProt [Q5XKP0](https://www.uniprot.org/uniprotkb/Q5XKP0) · Ensembl [ENSG00000174917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174917)

## Data

Gene col 10542: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10542); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10542, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10542]; `tensor/DDL_lfc|DDL_z.npy` [10542]; `embed/gene_vectors.npy` [10542]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10542 or target_col == 10542). Every well: [[MICOS13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MICOS13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
