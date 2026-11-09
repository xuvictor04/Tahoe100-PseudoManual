---
symbol: "MRM3"
type: "gene"
col: 10176
ensembl_id: "ENSG00000171861"
name: "mitochondrial rRNA methyltransferase 3"
location: "17p13.3"
module: 7
arm: "+"
pooled_cpm: 7.11
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MRM3

*mitochondrial rRNA methyltransferase 3* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.95× (z +9.1, q 4e-17, up in 31 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.733× (z -4.3, q 0.011, down in 9 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNTTIP2]] (+0.75, fdr 7e-06), [[C12orf43]] (+0.74, fdr 7e-06), [[SMG8]] (+0.73, fdr 7e-06); moves opposite to [[C12orf75]] (-0.66, fdr 1e-05), [[TMEM50B]] (-0.62, fdr 7e-06), [[SEPTIN2]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10176.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +9.1 | 4e-17 | 31/45 (NCI-H460, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +7.2 | 2e-10 | 24/41 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +7.1 | 2e-10 | 18/34 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +6.9 | 6e-10 | 26/46 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +6.6 | 4e-09 | 24/46 (A498, SW 900, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +6.1 | 1e-07 | 21/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +5.8 | 4e-07 | 19/45 (A498, NCI-H460, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +5.5 | 3e-06 | 15/47 (NCI-H2347, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.54×** | +5.4 | 4e-06 | 7/21 (NCI-H460, NCI-H2347, …) | inconsistent across doses | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +4.9 | 7e-05 | 17/43 (A-172, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.7 | 1e-04 | 14/48 (SW 900, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.40×** | +4.6 | 2e-04 | 13/47 (COLO 205, LOX-IMVI, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.002 | 9/47 (SW1417, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.32×** | +3.8 | 0.007 | 15/34 (HOP62, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.21×** | +3.7 | 0.007 | 15/41 (NCI-H1792, A549, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.022 | 11/42 (LS 180, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +3.0 | 0.073 | 3/46 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10176.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.733×** | -4.3 | 0.011 | 9/45 (SW 900, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Rifaximin (drug)]] 5 µM |  | **0.733×** | -4.1 | 0.011 | 13/46 (NCI-H23, HT-29, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -4.0 | 0.011 | 12/47 (Hs 766T, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.798× | -3.1 | 0.26 | 6/47 (SW 1271, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10176. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.15 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0956× (z -10.3) |
| [[A-427 (line)]] | wt | 6.38 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -9.1) |
| [[BT-474 (line)]] | alt | 5.62 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0773× (z -9.3) ⚠ transcription drop |
| [[C32 (line)]] | wt | 5.60 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0677× (z -9.9) ⚠ toxic |
| [[HCT15 (line)]] | alt | 4.79 | 0 | 1 | — | [[Ritonavir (drug)]] 0.05 µM 0.0517× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 2.98 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0763× (z -9.5) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 9.71 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[SNU-423 (line)]] | alt | 4.93 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM 0.0841× (z -9.0) |
| [[A498 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10176), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNTTIP2]] | +0.75 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[C12orf43]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[SMG8]] | +0.73 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[POP4]] | +0.73 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.72 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[CBLL1]] | +0.72 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[MRPL50]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 | STRING 889 |
| [[ZNF317]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[GTF3C4]] | +0.70 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[PSMD7]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[TSSC4]] | +0.70 | +0.61 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf75]] | -0.66 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[TMEM50B]] | -0.62 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[SEPTIN2]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[ATP6AP2]] | -0.59 | -0.51 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.820). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.3, 9.8); signed map (-3.0, -25.1). **Vector** length 51.4, 6.39% of its response variance represented; |z| ≥ 3 in 816 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.1 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.7 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +6.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.3 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.8 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -0.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial rRNA methyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:782,353-792,509 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10581, HC90, RMTL1; previously RNMTL1 |
| Gene groups (HGNC) | SPOUT methyltransferase domain containing; DNA/RNA methyltransferases |
| Reactome | 4 pathways, smallest: rRNA modification in the mitochondrion; rRNA processing in the mitochondrion; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC36](https://www.uniprot.org/uniprotkb/Q9HC36) (rRNA methyltransferase 3, mitochondrial):

> S-adenosyl-L-methionine-dependent 2'-O-ribose methyltransferase that catalyzes the formation of 2'-O-methylguanosine at position 1370 (Gm1370) in the 16S mitochondrial large subunit ribosomal RNA (mtLSU rRNA), a conserved modification in the peptidyl transferase domain of the mtLSU rRNA. Also required for formation of 2'-O-methyluridine at position 1369 (Um1369) mediated by MRM2.

**Summary**, from NCBI Gene [55178](https://www.ncbi.nlm.nih.gov/gene/55178):

> Efficient translation of mitochondrial-derived transcripts requires proper assembly of the large subunit of the mitochondrial ribosome. Central to the biogenesis of this large subunit is the A-loop of mitochondrial 16S rRNA, which is modified by three rRNA methyltransferases located near mtDNA nucleoids. The protein encoded by this gene methylates G(1370) of 16S rRNA, and this modification is necessary for proper ribosomal large subnit assembly. Two transcript variants encoding different …

**Accessions** — [HGNC:18485](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18485) · Entrez [55178](https://www.ncbi.nlm.nih.gov/gene/55178) · UniProt [Q9HC36](https://www.uniprot.org/uniprotkb/Q9HC36) · Ensembl [ENSG00000171861](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171861)

## Data

Gene col 10176: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10176); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10176, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10176]; `tensor/DDL_lfc|DDL_z.npy` [10176]; `embed/gene_vectors.npy` [10176]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10176 or target_col == 10176). Every well: [[MRM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
