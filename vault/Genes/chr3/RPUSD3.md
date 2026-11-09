---
symbol: "RPUSD3"
type: "gene"
col: 8034
ensembl_id: "ENSG00000156990"
name: "RNA pseudouridine synthase D3"
location: "3p25.3"
module: 1
arm: "+"
pooled_cpm: 8.34
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RPUSD3

*RNA pseudouridine synthase D3* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.48× (z +9.1, q 7e-17, up in 12 of 14 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.68× (z +5.4, q 1e-05, up in 19 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.507× (z -7.0, q 1e-09, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTCD2]] (+0.66, fdr 7e-06), [[BCS1L]] (+0.63, fdr 1e-05), [[MRPL40]] (+0.63, fdr 2e-05); moves opposite to [[GNAS]] (-0.58, fdr 3e-05), [[RSPH9]] (-0.53, fdr 1e-04), [[PTMS]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8034.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.48×** | +9.1 | 7e-17 | 12/14 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.33×** | +8.8 | 5e-16 | 26/31 (A498, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.68×** | +5.4 | 1e-05 | 19/46 (HOP62, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.55×** | +4.2 | 0.003 | 15/23 (NCI-H2030, A498, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.46×** | +4.0 | 0.008 | 14/37 (SHP-77, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.46×** | +3.9 | 0.008 | 10/47 (A498, CFPAC-1, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +3.7 | 0.015 | 16/46 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +3.5 | 0.035 | 16/42 (RKO, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.37×** | +3.3 | 0.064 | 8/47 (A-172, NCI-H2347, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.66×** | +3.2 | 0.077 | 8/35 (SW480, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.1 | 0.081 | 0/48 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.35×** | +3.1 | 0.081 | 10/47 (NCI-H2347, A-172, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.36×** | +3.1 | 0.091 | 12/37 (LoVo, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8034.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.507×** | -7.0 | 1e-09 | 32/47 (C-33 A, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.522×** | -6.7 | 6e-09 | 33/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.334×** | -5.9 | 6e-07 | 26/46 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.347×** | -5.7 | 2e-06 | 30/44 (NCI-H23, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.712×** | -4.9 | 9e-05 | 25/44 (PANC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.635×** | -4.7 | 3e-04 | 23/44 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.676×** | -4.0 | 0.004 | 21/47 (C-33 A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8034. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 6.25 | 0 | 2 | — | [[Estrone sulfate (potassium) (drug)]] 0.05 µM 0.0647× (z -9.5) |
| [[A-172 (line)]] | wt | 7.57 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0970× (z -10.1) |
| [[BT-474 (line)]] | alt | 8.47 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0857× (z -9.1) |
| [[C-33 A (line)]] | alt | 11.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0394× (z -12.9) |
| [[LOX-IMVI (line)]] | wt | 8.28 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -8.9) |
| [[PANC-1 (line)]] | alt | 10.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.3) |
| [[A-427 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8034), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTCD2]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 | STRING 408 |
| [[BCS1L]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[MRPL40]] | +0.63 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[GRHPR]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[VPS25]] | +0.61 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[METTL5]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[RPP40]] | +0.60 | +0.48 / +0.61 | both halves | 2e-05 | pathway: rRNA processing |
| [[MRPL24]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 | STRING 673 |
| [[PRMT5]] | +0.59 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[YDJC]] | +0.58 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[MRPL15]] | +0.58 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[MRPL12]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.58 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[RSPH9]] | -0.53 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[PTMS]] | -0.51 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[ALOX12-AS1]] | -0.50 | -0.21 / -0.43 | both halves | 7e-04 |  |
| [[PINK1-AS]] | -0.50 | -0.29 / -0.41 | both halves | 3e-04 |  |
| [[LAMTOR5-AS1]] | -0.50 | -0.21 / -0.54 | both halves | 7e-04 |  |
| [[NUCB2]] | -0.49 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[HYPK]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ZNF451-AS1]] | -0.48 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[PNPLA7]] | -0.48 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ERFL]] | -0.48 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[ITGA7]] | -0.48 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.463). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-44.9, -7.3); signed map (-16.5, -25.6). **Vector** length 52.9, 7.57% of its response variance represented; |z| ≥ 3 in 767 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +0.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.9 | -5.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.7 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | +0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | RNA pseudouridine synthase D3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,837,849-9,844,602 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC29784 |
| Gene groups (HGNC) | RNA pseudouridylate synthase domain containing; Pseudouridine synthases |
| Reactome | 5 pathways, smallest: rRNA modification in the mitochondrion; Mitochondrial mRNA modification; rRNA processing in the mitochondrion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P087](https://www.uniprot.org/uniprotkb/Q6P087) (Mitochondrial mRNA pseudouridine synthase RPUSD3):

> Catalyzes uridine to pseudouridine isomerization (pseudouridylation) of specific mitochondrial mRNAs (mt-mRNAs), a post-transcriptional modification necessary for their translation. Acts at position 390 in COXI mt-mRNA and at position 697-699 in mitochondrial COXIII mt-mRNA. As a component of a functional protein-RNA module, consisting of RCC1L, NGRN, RPUSD3, RPUSD4, TRUB2, FASTKD2 and 16S mitochondrial ribosomal RNA (16S mt-rRNA), controls 16S mt-rRNA abundance and may play a role in …

**Summary**, from NCBI Gene [285367](https://www.ncbi.nlm.nih.gov/gene/285367):

> This gene encodes a protein that functions in the assembly of the mitochondrial ribosome by adding a pseudouridine group to 16S rRNA. Loss of this gene results in causes defects in mitochondrial protein production. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:28437](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28437) · Entrez [285367](https://www.ncbi.nlm.nih.gov/gene/285367) · UniProt [Q6P087](https://www.uniprot.org/uniprotkb/Q6P087) · Ensembl [ENSG00000156990](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156990)

## Data

Gene col 8034: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8034); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8034, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8034]; `tensor/DDL_lfc|DDL_z.npy` [8034]; `embed/gene_vectors.npy` [8034]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8034 or target_col == 8034). Every well: [[RPUSD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPUSD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
