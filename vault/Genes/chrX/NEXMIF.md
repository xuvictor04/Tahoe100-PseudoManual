---
symbol: "NEXMIF"
type: "gene"
col: 559
ensembl_id: "ENSG00000050030"
name: "neurite extension and migration factor"
location: "Xq13.3"
module: 19
arm: "+"
pooled_cpm: 5.17
n_lines_expressing: 26
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# NEXMIF

*neurite extension and migration factor* — Xq13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.38× (z +12.8, q 1e-34, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.25× (z +12.5, q 2e-33, up in 6 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-423 0.0934×, NCI-H460 0.237×, AN3 CA 0.255×); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.131×, NCI-H2347 0.187×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0970×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.116×); [[Panobinostat (drug)]] 0.5 µM in 1 line (BT-474 0.151×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WNK3]] (+0.65, fdr 1e-05), [[MIR9-3HG]] (+0.62, fdr 9e-06), [[LIN7A]] (+0.57, fdr 3e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 559.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.38×** | +12.8 | 1e-34 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +12.5 | 2e-33 | 6/14 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +10.2 | 6e-22 | 1/11 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +8.3 | 1e-14 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +7.9 | 3e-13 | 11/21 (A549, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +6.6 | 4e-09 | 2/16 (A549, HOP62) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +5.7 | 8e-07 | 4/17 (NCI-H1573, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.9 | 7e-05 | 5/20 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +4.7 | 1e-04 | 5/21 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +4.4 | 6e-04 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.002 | 13/19 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.017 | 5/19 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.24×** | +3.3 | 0.035 | 2/22 (NCI-H460, A549) | rises with dose | low cells (technical?) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.035 | 1/16 (NCI-H1573) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.090 | 3/15 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 559.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-423 0.0934×, NCI-H460 0.237×, AN3 CA 0.255×); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.131×, NCI-H2347 0.187×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0970×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.116×); [[Panobinostat (drug)]] 0.5 µM in 1 line (BT-474 0.151×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.721× | -3.6 | 0.20 | 7/22 (NCI-H460, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.735× | -3.4 | 0.22 | 4/20 (C-33 A, NCI-H460, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.742× | -3.1 | 0.32 | 5/21 (C-33 A, SNU-423, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.4 | 0 | 12 (9 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0997× (z -14.0) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 26.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0970× (z -14.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 5.44 | 0 | 2 (1 ⚠) | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0740× (z -9.1) |
| [[AN3 CA (line)]] | alt | 71.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.255× (z -9.0) |
| [[BT-474 (line)]] | alt | 51.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -13.0) |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0934× (z -14.0) |
| [[A-427 (line)]] | wt | 19.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0997× (z -12.0) |
| [[C-33 A (line)]] | alt | 11.8 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0600× (z -10.2) |
| [[A-172 (line)]] | wt | 0.749 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.673 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.839 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.734 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.983 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.890 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.760 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.747 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.952 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.997 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.958 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WNK3]] | +0.65 | +0.65 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[MIR9-3HG]] | +0.62 | +0.57 / +0.58 | both halves | 9e-06 | **novel candidate** |
| [[LIN7A]] | +0.57 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[SLITRK5]] | +0.55 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[NCKAP5-AS2]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[MAP3K15]] | +0.54 | +0.54 / +0.41 | both halves | 4e-05 | **novel candidate** |
| [[TMEM144]] | +0.53 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[DDIT4L]] | +0.52 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[ASXL3]] | +0.51 | +0.55 / +0.39 | both halves | 6e-05 |  |
| [[SCD5]] | +0.51 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[LINGO2]] | +0.51 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[FENDRR]] | +0.51 | +0.56 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NEXMIF's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.4, 39.4); signed map (41.3, 47.6). **Vector** length 43.5, 8.57% of its response variance represented; |z| ≥ 3 in 545 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +12.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +4.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.5 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.9 | +0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.9 | +1.2 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | -1.8 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.5 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.4 | +0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -1.4 | -1.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | +0.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | neurite extension and migration factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.3 — chrX:74,732,856-74,925,472 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XPN, MRX98, KIDLIA; previously KIAA2022 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5QGS0](https://www.uniprot.org/uniprotkb/Q5QGS0) (Neurite extension and migration factor):

> Involved in neurite outgrowth by regulating cell-cell adhesion via the N-cadherin signaling pathway. May act by regulating expression of protein-coding genes, such as N-cadherins and integrin beta-1 (ITGB1).

**Summary**, from NCBI Gene [340533](https://www.ncbi.nlm.nih.gov/gene/340533):

> An inversion on the X chromosome which disrupts this gene and a G-protein coupled purinergic receptor gene located in the pseudoautosomal region of the X chromosome has been linked to X linked cognitive disability.[provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:29433](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29433) · Entrez [340533](https://www.ncbi.nlm.nih.gov/gene/340533) · UniProt [Q5QGS0](https://www.uniprot.org/uniprotkb/Q5QGS0) · Ensembl [ENSG00000050030](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000050030)

## Data

Gene col 559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 559); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 559]; `tensor/DDL_lfc|DDL_z.npy` [559]; `embed/gene_vectors.npy` [559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 559 or target_col == 559). Every well: [[NEXMIF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEXMIF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
