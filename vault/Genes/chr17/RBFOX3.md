---
symbol: "RBFOX3"
type: "gene"
col: 9446
ensembl_id: "ENSG00000167281"
name: "RNA binding fox-1 homolog 3"
location: "17q25.3"
module: 75
arm: "+"
pooled_cpm: 3.55
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# RBFOX3

*RNA binding fox-1 homolog 3* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.04× (z +25.2, q 0e+00, up in 26 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.0607×; ⚠ toxic; transcription drop); [[Cabozantinib (S-malate) (drug)]] 0.5 µM in 1 line (SW480 0.0555×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLGAP2]] (+0.82, fdr 7e-06), [[MIR4300HG]] (+0.76, fdr 7e-06), [[LRRC4C]] (+0.75, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9446.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.04×** | +25.2 | 0e+00 | 26/30 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.76×** | +24.5 | 0e+00 | 26/27 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.40×** | +19.8 | 0e+00 | 8/10 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.57×** | +18.0 | 0e+00 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.98×** | +14.7 | 0e+00 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.63×** | +13.6 | 6e-40 | 31/42 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.80×** | +10.2 | 2e-22 | 23/44 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.59×** | +9.4 | 2e-19 | 16/27 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.53×** | +8.8 | 6e-17 | 20/36 (BT-474, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.42×** | +8.8 | 1e-16 | 19/36 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.85×** | +8.6 | 3e-16 | 13/42 (NCI-H2030, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.25×** | +7.7 | 6e-13 | 3/12 (LOX-IMVI, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.95×** | +6.6 | 1e-09 | 15/39 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +6.1 | 5e-08 | 17/40 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +5.8 | 3e-07 | 17/33 (LOX-IMVI, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.8 | 5e-05 | 5/23 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +4.4 | 2e-04 | 11/46 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +4.2 | 6e-04 | 10/41 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.81×** | +4.2 | 6e-04 | 1/10 (NCI-H2030) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9446.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.0607×; ⚠ toxic; transcription drop); [[Cabozantinib (S-malate) (drug)]] 0.5 µM in 1 line (SW480 0.0555×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.886× | -4.4 | 0.005 | 14/45 (KATO III, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9446. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 1.30 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.32× (z +9.4) | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0555× (z -8.6) |
| [[A-172 (line)]] | wt | 2.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.17× (z +9.1) | — |
| [[A498 (line)]] | wt | 1.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +10.1) | — |
| [[A549 (line)]] | wt | 65.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0607× (z -13.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 5.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.9× (z +14.3) | — |
| [[C32 (line)]] | wt | 1.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.7× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 1.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.2× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 1.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +11.5) | — |
| [[LoVo (line)]] | wt | 1.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 1.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +10.2) | — |
| [[A-427 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9446), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP2]] | +0.82 | +0.75 / +0.84 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.76 | +0.69 / +0.84 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.75 | +0.68 / +0.80 | both halves | 7e-06 |  |
| [[MEIOC]] | +0.75 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[PLD5]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.73 | +0.56 / +0.88 | both halves | 1e-05 |  |
| [[SPATA21]] | +0.73 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[CDH23]] | +0.73 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[LINC02006]] | +0.73 | +0.61 / +0.78 | both halves | 7e-06 |  |
| [[SLC9C1]] | +0.72 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[KCNIP1]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[SLC27A6]] | +0.72 | +0.57 / +0.75 | both halves | 9e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RBFOX3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.7% of all compounds | 0.015 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.813). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.4, 30.5); signed map (31.2, 16.2). **Vector** length 51.1, 6.92% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +18.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +24.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +19.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +13.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +25.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +8.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +0.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | +0.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -0.8 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding fox-1 homolog 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:79,089,345-79,611,051 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FOX-3, NeuN, HRNBP3 |
| Gene groups (HGNC) | RNA binding motif containing; RNA binding fox-1 homologs |
| Reactome | 2 pathways, smallest: NPAS4 regulates expression of target genes; Transcriptional Regulation by NPAS4 |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NFN3](https://www.uniprot.org/uniprotkb/A6NFN3) (RNA binding protein fox-1 homolog 3):

> Pre-mRNA alternative splicing regulator. Regulates alternative splicing of RBFOX2 to enhance the production of mRNA species that are targeted for nonsense-mediated decay (NMD).

**Summary**, from NCBI Gene [146713](https://www.ncbi.nlm.nih.gov/gene/146713):

> This gene encodes a member of the RNA-binding FOX protein family which is involved in the regulation of alternative splicing of pre-mRNA. The protein has an N-terminal proline-rich region, an RNA recognition motif (RRM) domain, and a C-terminal alanine-rich region. This gene produces the neuronal nuclei (NeuN) antigen that has been widely used as a marker for post-mitotic neurons. This gene has its highest expression in the central nervous system and plays a prominent role in neural tissue …

**Accessions** — [HGNC:27097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27097) · Entrez [146713](https://www.ncbi.nlm.nih.gov/gene/146713) · UniProt [A6NFN3](https://www.uniprot.org/uniprotkb/A6NFN3) · Ensembl [ENSG00000167281](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167281)

## Data

Gene col 9446: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9446); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9446, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9446]; `tensor/DDL_lfc|DDL_z.npy` [9446]; `embed/gene_vectors.npy` [9446]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9446 or target_col == 9446). Every well: [[RBFOX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBFOX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
