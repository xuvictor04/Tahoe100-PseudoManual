---
symbol: "MRPS33"
type: "gene"
col: 1614
ensembl_id: "ENSG00000090263"
name: "mitochondrial ribosomal protein S33"
location: "7q34"
module: 12
arm: "+"
pooled_cpm: 12.02
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MRPS33

*mitochondrial ribosomal protein S33* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.47× (z +11.2, q 3e-26, up in 33 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A498 6.76×, NCI-H1573 11.8×, PANC-1 5.15×, NCI-H1792 8.70×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 5.91×, A498 5.32×, A549 7.48×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.487× (z -5.4, q 5e-05, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EBAG9]] (+0.73, fdr 7e-06), [[CHURC1]] (+0.73, fdr 7e-06), [[PPP4R2]] (+0.71, fdr 7e-06); moves opposite to [[MLEC]] (-0.58, fdr 1e-05), [[GUCD1]] (-0.58, fdr 3e-05), [[PMPCA]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[REPIN1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1614.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A498 6.76×, NCI-H1573 11.8×, PANC-1 5.15×, NCI-H1792 8.70×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 5.91×, A498 5.32×, A549 7.48×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **4.47×** | +11.2 | 3e-26 | 33/34 (A498, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.23×** | +10.4 | 1e-22 | 21/22 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.75×** | +7.0 | 5e-10 | 27/29 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.88×** | +4.7 | 3e-04 | 29/41 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.75×** | +4.0 | 0.006 | 28/46 (A-172, NCI-H23, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.46×** | +4.0 | 0.006 | 23/45 (LoVo, HCT15, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.7 | 0.019 | 24/39 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.59×** | +3.5 | 0.035 | 27/48 (A498, A-427, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.59×** | +3.5 | 0.035 | 23/45 (A-172, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.55×** | +3.3 | 0.055 | 23/46 (A-427, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1614.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.487×** | -5.4 | 5e-05 | 34/47 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.530×** | -4.7 | 7e-04 | 28/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.619×** | -3.6 | 0.067 | 23/46 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1614. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 18.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.76× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A549 (line)]] | wt | 12.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.48× (z +8.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 9.24 | 0 | 1 | — | [[Clotrimazole (drug)]] 0.05 µM 0.0509× (z -8.9) |
| [[LoVo (line)]] | wt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.91× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 7.09 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.8× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.70× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.167× (z -8.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 1 | — | [[Cytarabine (hydrochloride) (drug)]] 5 µM 0.0491× (z -10.0) |
| [[A-172 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1614), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EBAG9]] | +0.73 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[CHURC1]] | +0.73 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[PPP4R2]] | +0.71 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[SNAPIN]] | +0.70 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[MRPL57]] | +0.70 | +0.73 / +0.76 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 904 |
| [[MRPL47]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 956 |
| [[MSRB2]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[IFTAP]] | +0.68 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[MRPL58]] | +0.68 | +0.71 / +0.68 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 875 |
| [[NSMCE1]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[GORAB]] | +0.67 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.67 | +0.72 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLEC]] | -0.58 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[GUCD1]] | -0.58 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[PMPCA]] | -0.57 | -0.60 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[REPIN1]] | C | MRPS33's natural level strengthens REPIN1's drug response | MRPS33's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.23; direction not clear | 0.084 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.694). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-31.0, 3.5); signed map (5.4, -22.9). **Vector** length 54.0, 10.1% of its response variance represented; |z| ≥ 3 in 579 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | +4.9 | +4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +4.8 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.2 | +3.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.3 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.8 | -3.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.7 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | +0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.8 | -2.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.8 | -1.0 |
|  | [[Tirabrutinib (drug)]] 0.05 µM |  | -0.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:141,002,610-141,015,228 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-139, mS33 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9Y291](https://www.uniprot.org/uniprotkb/Q9Y291) carries no function annotation.

**Summary**, from NCBI Gene [51650](https://www.ncbi.nlm.nih.gov/gene/51650):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:16634](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16634) · Entrez [51650](https://www.ncbi.nlm.nih.gov/gene/51650) · UniProt [Q9Y291](https://www.uniprot.org/uniprotkb/Q9Y291) · Ensembl [ENSG00000090263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090263)

## Data

Gene col 1614: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1614); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1614, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1614]; `tensor/DDL_lfc|DDL_z.npy` [1614]; `embed/gene_vectors.npy` [1614]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1614 or target_col == 1614). Every well: [[MRPS33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
