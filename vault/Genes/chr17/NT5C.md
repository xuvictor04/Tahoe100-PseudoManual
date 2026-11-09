---
symbol: "NT5C"
type: "gene"
col: 4619
ensembl_id: "ENSG00000125458"
name: "5', 3'-nucleotidase, cytosolic"
location: "17q25"
module: 11
arm: "+"
pooled_cpm: 11.09
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# NT5C

*5', 3'-nucleotidase, cytosolic* — 17q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.46× (z +5.1, q 2e-04, up in 25 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.33× (z +4.8, q 4e-04, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.530× (z -6.1, q 5e-07, down in 33 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SURF2]] (+0.74, fdr 1e-05), [[NSUN5]] (+0.74, fdr 7e-06), [[PPP1R35]] (+0.71, fdr 1e-05, ⚠ PPP1R35 in the vector space only through flagged drug-doses), [[TMEM70]] (+0.70, fdr 1e-05); moves opposite to [[TMEM30A]] (-0.73, fdr 7e-06), [[DDOST]] (-0.66, fdr 1e-05), [[MLEC]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4619.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +5.1 | 2e-04 | 25/32 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.33×** | +4.8 | 4e-04 | 38/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.99×** | +4.5 | 0.001 | 30/46 (NCI-H2030, SHP-77, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +4.2 | 0.003 | 14/22 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.78×** | +3.9 | 0.010 | 23/40 (SW480, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.68×** | +3.5 | 0.040 | 22/46 (A-172, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4619.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.530×** | -6.1 | 5e-07 | 33/44 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.472×** | -5.1 | 9e-05 | 34/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.507×** | -4.6 | 7e-04 | 32/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.536×** | -4.3 | 0.003 | 28/47 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.604×** | -3.4 | 0.066 | 25/47 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.610× | -3.2 | 0.11 | 23/45 (C-33 A, C32, …) | rises with dose | cell-cycle shift (explains ~22% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4619. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 9.70 | 0 | 1 (1 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.0523× (z -9.1) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 5.45 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0665× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 14.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -9.3) |
| [[A-172 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4619), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SURF2]] | +0.74 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[NSUN5]] | +0.74 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PPP1R35]] ⚠ | +0.71 | +0.51 / +0.76 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM70]] | +0.70 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[MRPS18B]] | +0.70 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[SURF6]] | +0.68 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[MRPL58]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.67 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[PDRG1]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ZNF593]] | +0.66 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[ATF4]] | +0.65 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[LENG1]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TMEM42]] | +0.64 | +0.52 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM30A]] | -0.73 | -0.60 / -0.74 | both halves | 7e-06 |  |
| [[DDOST]] | -0.66 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[MLEC]] | -0.65 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[TMED4]] | -0.64 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[TECR]] | -0.63 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[FKBP9]] | -0.62 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[RPN1]] | -0.62 | -0.40 / -0.65 | both halves | 4e-05 |  |
| [[STT3B]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[CRTAP]] | -0.61 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[CMPK1]] | -0.61 | -0.45 / -0.63 | both halves | 3e-05 | pathway: Metabolism of nucleotides; STRING 496 |
| [[LAPTM4A]] | -0.60 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[EDEM1]] | -0.60 | -0.45 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises NT5C's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.5, -3.4); signed map (-2.9, -19.4). **Vector** length 60.6, 13.0% of its response variance represented; |z| ≥ 3 in 598 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +5.9 | +4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.8 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -6.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.6 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.0 | -1.8 |
|  | [[Pimozide (drug)]] 5 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | 5', 3'-nucleotidase, cytosolic |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25 — chr17:75,130,225-75,131,757 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DNT1, DNT-1, PN-I, cdN, dNT-1; previously UMPH2 |
| Gene groups (HGNC) | 5'-nucleotidases |
| Hallmark sets | DNA_REPAIR |
| Reactome | 4 pathways, smallest: Pyrimidine catabolism; Purine catabolism; Nucleotide catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCD5](https://www.uniprot.org/uniprotkb/Q8TCD5) (5'(3')-deoxyribonucleotidase, cytosolic type):

> Dephosphorylates the 5' and 2'(3')-phosphates of deoxyribonucleotides, with a preference for dUMP. Also dephosphsphorylates dTMP, exhibits intermediate activity towards dGMP, and low activity towards dCMP and dAMP (By similarity).

**Summary**, from NCBI Gene [30833](https://www.ncbi.nlm.nih.gov/gene/30833):

> This gene encodes a nucleotidase that catalyzes the dephosphorylation of the 5' deoxyribonucleotides (dNTP) and 2'(3')-dNTP and ribonucleotides, but not 5' ribonucleotides. Of the different forms of nucleotidases characterized, this enzyme is unique in its preference for 5'-dNTP. It may be one of the enzymes involved in regulating the size of dNTP pools in cells. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:17144](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17144) · Entrez [30833](https://www.ncbi.nlm.nih.gov/gene/30833) · UniProt [Q8TCD5](https://www.uniprot.org/uniprotkb/Q8TCD5) · Ensembl [ENSG00000125458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125458)

## Data

Gene col 4619: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4619); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4619, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4619]; `tensor/DDL_lfc|DDL_z.npy` [4619]; `embed/gene_vectors.npy` [4619]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4619 or target_col == 4619). Every well: [[NT5C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NT5C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
