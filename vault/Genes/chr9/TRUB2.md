---
symbol: "TRUB2"
type: "gene"
col: 9419
ensembl_id: "ENSG00000167112"
name: "TruB pseudouridine synthase family member 2"
location: "9q34.11"
module: 1
arm: "+"
pooled_cpm: 13.65
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TRUB2

*TruB pseudouridine synthase family member 2* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.70× (z +7.2, q 5e-10, up in 23 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.32× (z +5.3, q 2e-05, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.763× (z -5.1, q 2e-04, down in 20 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC30]] (+0.64, fdr 1e-05), [[DDX28]] (+0.63, fdr 7e-06), [[QTRT2]] (+0.62, fdr 1e-05); moves opposite to [[CSRP2]] (-0.52, fdr 2e-05), [[TSC22D2]] (-0.48, fdr 4e-05), [[RELL1]] (-0.48, fdr 9e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9419.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.2 | 5e-10 | 23/39 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.3 | 2e-05 | 15/25 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +5.3 | 2e-05 | 22/48 (A-172, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.6 | 7e-04 | 18/48 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +4.3 | 0.002 | 16/31 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.006 | 16/45 (HT-29, Hs 766T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +3.9 | 0.006 | 14/47 (SHP-77, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.68×** | +3.7 | 0.018 | 11/45 (A498, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.6 | 0.018 | 20/43 (SHP-77, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.20×** | +3.5 | 0.026 | 8/48 (Hs 766T, NCI-H2030, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.026 | 11/46 (RKO, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +3.3 | 0.053 | 10/43 (RPMI-7951, Panc 03.27, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9419.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.763×** | -5.1 | 2e-04 | 20/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.753×** | -3.8 | 0.048 | 15/46 (NCI-H23, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.770×** | -3.5 | 0.098 | 17/47 (A498, SW 1271, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.793× | -3.1 | 0.30 | 16/47 (hTERT-HPNE, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9419. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 10.1 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.125× (z -8.5) |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.183× (z -8.7) ⚠ cell-cycle shift, explains ~99% of this change |
| [[NCI-H23 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -10.3) ⚠ cell-cycle shift, explains ~11% of this change |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0952× (z -9.6) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9419), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC30]] | +0.64 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[DDX28]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 | STRING 856 |
| [[QTRT2]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 | STRING 629 |
| [[C12orf43]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[FARS2]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[PEX10]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[MRTO4]] | +0.58 | +0.63 / +0.52 | both halves | 1e-05 | STRING 593 |
| [[SMARCAD1]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[LSG1]] | +0.57 | +0.65 / +0.43 | both halves | 3e-05 | STRING 438 |
| [[FAHD1]] | +0.57 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[MOCS3]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[AKAP8]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSRP2]] | -0.52 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[TSC22D2]] | -0.48 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[RELL1]] | -0.48 | -0.48 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-41.6, 9.9); signed map (-4.1, -25.9). **Vector** length 59.3, 9.27% of its response variance represented; |z| ≥ 3 in 620 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.6 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +3.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.1 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.7 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.5 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | TruB pseudouridine synthase family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,305,159-128,322,447 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLONE24922 |
| Gene groups (HGNC) | Pseudouridine synthases |
| Reactome | 5 pathways, smallest: rRNA modification in the mitochondrion; Mitochondrial mRNA modification; rRNA processing in the mitochondrion |
| Matched by | ensembl_id |

**Function**, from UniProt [O95900](https://www.uniprot.org/uniprotkb/O95900) (Pseudouridylate synthase TRUB2, mitochondrial):

> Minor enzyme contributing to the isomerization of uridine to pseudouridine (pseudouridylation) of specific mitochondrial mRNAs (mt-mRNAs) such as COXI and COXIII mt-mRNAs. As a component of a functional protein-RNA module, consisting of RCC1L, NGRN, RPUSD3, RPUSD4, TRUB2, FASTKD2 and 16S mitochondrial ribosomal RNA (16S mt-rRNA), controls 16S mt-rRNA abundance and is required for intra-mitochondrial translation. Also catalyzes pseudouridylation of some tRNAs, including synthesis of …

**Summary**, from NCBI Gene [26995](https://www.ncbi.nlm.nih.gov/gene/26995):

> Pseudouridine is an abundant component of rRNAs and tRNAs and is enzymatically generated by isomerization of uridine by pseudouridine synthase (Zucchini et al., 2003 [PubMed 12736709]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:17170](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17170) · Entrez [26995](https://www.ncbi.nlm.nih.gov/gene/26995) · UniProt [O95900](https://www.uniprot.org/uniprotkb/O95900) · Ensembl [ENSG00000167112](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167112)

## Data

Gene col 9419: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9419); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9419, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9419]; `tensor/DDL_lfc|DDL_z.npy` [9419]; `embed/gene_vectors.npy` [9419]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9419 or target_col == 9419). Every well: [[TRUB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRUB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
