---
symbol: "TUBA8"
type: "gene"
col: 11458
ensembl_id: "ENSG00000183785"
name: "tubulin alpha 8"
location: "22q11.21"
module: 47
arm: "+"
pooled_cpm: 4.11
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# TUBA8

*tubulin alpha 8* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.92× (z +6.1, q 3e-07, up in 11 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.88× (z +6.1, q 3e-07, up in 21 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.395× (z -9.0, q 1e-16, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FERMT3]] (+0.70, fdr 7e-06), [[LINC02133]] (+0.70, fdr 7e-06), [[MSANTD1]] (+0.68, fdr 7e-06); moves opposite to [[KBTBD3]] (-0.59, fdr 1e-05), [[TXNDC16]] (-0.59, fdr 1e-05), [[RCOR3]] (-0.58, fdr 1e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SPTBN5]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +6.1 | 3e-07 | 11/20 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +6.1 | 3e-07 | 21/45 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +5.8 | 1e-06 | 2/6 (CFPAC-1, HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +5.1 | 5e-05 | 1/10 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.44×** | +4.9 | 9e-05 | 12/44 (NCI-H460, A498, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.63×** | +4.5 | 7e-04 | 11/44 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +4.1 | 0.004 | 13/36 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.41×** | +3.2 | 0.095 | 4/45 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11458.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.395×** | -9.0 | 1e-16 | 30/46 (NCI-H2030, BT-474, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.468×** | -7.4 | 5e-11 | 26/45 (NCI-H2030, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.521×** | -6.3 | 5e-08 | 21/36 (RKO, BT-474, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.584×** | -5.2 | 3e-05 | 20/44 (KATO III, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.716×** | -4.6 | 5e-04 | 14/44 (RKO, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 5.39 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0521× (z -10.6) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0907× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 3.39 | 0 | 2 | — | [[Cilostazol (drug)]] 0.05 µM 0.0824× (z -9.4) |
| [[A498 (line)]] | wt | 5.08 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0926× (z -9.0) |
| [[BT-474 (line)]] | alt | 6.74 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 4.70 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0823× (z -9.3) ⚠ cell-cycle shift, explains ~90% of this change |
| [[RKO (line)]] | wt | 9.42 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FERMT3]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[LINC02133]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[MSANTD1]] | +0.68 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[LINC02236]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[MRPS28]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[HSD17B2-AS1]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[C16orf95]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[GTPBP4]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[LINC02803]] | +0.62 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[SPON2]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[MYH3]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[CHADL]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD3]] | -0.59 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.59 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.58 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[HMGCL]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SPATA7]] | -0.57 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[SAP30]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[MBIP]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[PRKRA]] | -0.54 | -0.58 / -0.45 | both halves | 3e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[LNX2]] | -0.54 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[SLC35A1]] | -0.53 | -0.56 / -0.50 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[TBC1D12]] | -0.52 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[PLAG1]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPTBN5]] | C | SPTBN5 activity lowers TUBA8's level | lines that do not express SPTBN5 (3) vs lines expressing it (47) | 1.73× higher at baseline in the lines without SPTBN5 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with SMAD3; also absent: UACA, MYH16, PER3; maybe low, not absent; its own permutation p |
| [[IFITM10]] | C | IFITM10's natural level weakens TUBA8's drug response | IFITM10's natural level across 42 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.04; direction not clear | 0.097 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.9, -22.6); signed map (18.8, 12.5). **Vector** length 63.5, 8.87% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.5 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.6 | +4.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +2.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -9.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | -6.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.6 | -1.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | tubulin alpha 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:18,110,100-18,146,683 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TUBAL2 |
| Gene groups (HGNC) | Tubulin alpha family |
| Reactome | 79 pathways, smallest: Microtubule-dependent trafficking of connexons from Golgi to the plasma membrane; Transport of connexons to the plasma membrane; Gap junction assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY65](https://www.uniprot.org/uniprotkb/Q9NY65) (Tubulin alpha-8 chain):

> Tubulin is the major constituent of microtubules, a cylinder consisting of laterally associated linear protofilaments composed of alpha- and beta-tubulin heterodimers. Microtubules grow by the addition of GTP-tubulin dimers to the microtubule end, where a stabilizing cap forms. Below the cap, tubulin dimers are in GDP-bound state, owing to GTPase activity of alpha-tubulin.

**Summary**, from NCBI Gene [51807](https://www.ncbi.nlm.nih.gov/gene/51807):

> This gene encodes a member of the alpha tubulin protein family. Alpha tubulins are one of two core protein families (alpha and beta tubulins) that heterodimerize and assemble to form microtubules. Mutations in this gene are associated with polymicrogyria and optic nerve hypoplasia. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:12410](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12410) · Entrez [51807](https://www.ncbi.nlm.nih.gov/gene/51807) · UniProt [Q9NY65](https://www.uniprot.org/uniprotkb/Q9NY65) · Ensembl [ENSG00000183785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183785)

## Data

Gene col 11458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11458); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11458]; `tensor/DDL_lfc|DDL_z.npy` [11458]; `embed/gene_vectors.npy` [11458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11458 or target_col == 11458). Every well: [[TUBA8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBA8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
