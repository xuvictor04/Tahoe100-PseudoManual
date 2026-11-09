---
symbol: "NOC4L"
type: "gene"
col: 11597
ensembl_id: "ENSG00000184967"
name: "nucleolar complex associated 4 homolog"
location: "12q24.33"
module: 1
arm: "+"
pooled_cpm: 6.27
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NOC4L

*nucleolar complex associated 4 homolog* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.52× (z +10.3, q 6e-22, up in 40 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.35× (z +9.5, q 6e-19, up in 34 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (AsPC-1 0.0718×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTU2]] (+0.73, fdr 7e-06), [[BCS1L]] (+0.72, fdr 7e-06), [[DPH2]] (+0.70, fdr 7e-06); moves opposite to [[NAP1L1]] (-0.52, fdr 3e-05), [[ATP5F1E]] (-0.50, fdr 2e-05), [[OLMALINC]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BSN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11597.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.52×** | +10.3 | 6e-22 | 40/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.35×** | +9.5 | 6e-19 | 34/38 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.28×** | +9.1 | 1e-17 | 20/29 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +9.1 | 1e-17 | 19/32 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.35×** | +8.8 | 2e-16 | 12/17 (HOP62, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.25×** | +8.7 | 5e-16 | 6/10 (SNU-423, A498, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.66×** | +7.9 | 2e-13 | 27/41 (COLO 205, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.97×** | +7.5 | 5e-12 | 30/47 (SW480, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.90×** | +6.8 | 6e-10 | 24/45 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +6.3 | 2e-08 | 27/46 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.74×** | +6.1 | 5e-08 | 26/47 (HepG2/C3A, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.64×** | +5.5 | 2e-06 | 15/36 (A-172, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +4.9 | 5e-05 | 16/45 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.55×** | +4.8 | 5e-05 | 18/47 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +4.6 | 1e-04 | 16/47 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.082 | 7/46 (SW480, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11597.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (AsPC-1 0.0718×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.731× | -3.5 | 0.27 | 11/45 (C32, A498, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11597. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 7.82 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0718× (z -10.8) |
| [[LoVo (line)]] | wt | 6.46 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.59× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A-172 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11597), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTU2]] | +0.73 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[BCS1L]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[DPH2]] | +0.70 | +0.73 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[TRMT61A]] | +0.70 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[TBL3]] | +0.67 | +0.63 / +0.71 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[ZPR1]] | +0.65 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[RRP9]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 999 |
| [[E2F4]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[NOL6]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 998 |
| [[RHOT2]] | +0.61 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ZNF598]] | +0.61 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[IMP4]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 999 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAP1L1]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ATP5F1E]] | -0.50 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[OLMALINC]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[RPLP1]] | -0.46 | -0.52 / -0.45 | both halves | 3e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BSN]] | B | BSN activity raises NOC4L's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.08× lower at baseline in the lines without BSN | 0.093 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.437). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.3, -39.5); signed map (-3.4, -44.3). **Vector** length 46.5, 5.63% of its response variance represented; |z| ≥ 3 in 839 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +3.5 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.2 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +3.1 | +8.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | +2.8 | +5.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +4.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.2 | -3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -2.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Berbamine (drug)]] 5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar complex associated 4 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:132,144,457-132,152,473 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3162, NET49, UTP19, Noc4 |
| Gene groups (HGNC) | SSU processome; Armadillo like helical domain containing |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVI4](https://www.uniprot.org/uniprotkb/Q9BVI4) (Nucleolar complex protein 4 homolog):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Required for the translation of mRNAs related to activation of …

**Summary**, from NCBI Gene [79050](https://www.ncbi.nlm.nih.gov/gene/79050):

> Enables RNA binding activity. Predicted to be involved in rRNA processing. Located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28461) · Entrez [79050](https://www.ncbi.nlm.nih.gov/gene/79050) · UniProt [Q9BVI4](https://www.uniprot.org/uniprotkb/Q9BVI4) · Ensembl [ENSG00000184967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184967)

## Data

Gene col 11597: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11597); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11597, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11597]; `tensor/DDL_lfc|DDL_z.npy` [11597]; `embed/gene_vectors.npy` [11597]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11597 or target_col == 11597). Every well: [[NOC4L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOC4L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
