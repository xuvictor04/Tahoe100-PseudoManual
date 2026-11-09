---
symbol: "H2BC8"
type: "gene"
col: 15800
ensembl_id: "ENSG00000273802"
name: "H2B clustered histone 8"
location: "6p22.2"
module: null
arm: null
pooled_cpm: 2.74
n_lines_expressing: 37
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# H2BC8

*H2B clustered histone 8* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.42× (z +8.9, q 3e-16, up in 23 of 29 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.30× (z +4.3, q 0.002, up in 19 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Gemcitabine (drug)]] 0.05 µM: 0.502× (z -4.8, q 0.001, down in 21 of 34 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15800.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.42×** | +8.9 | 3e-16 | 23/29 (KATO III, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.10×** | +7.0 | 8e-10 | 2/2 (PANC-1, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.86×** | +6.9 | 8e-10 | 9/14 (PANC-1, LOX-IMVI, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.25×** | +6.9 | 9e-10 | 3/5 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.54×** | +6.2 | 5e-08 | 26/33 (SW480, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.33×** | +4.3 | 0.001 | 21/34 (KATO III, LoVo, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.30×** | +4.3 | 0.002 | 19/34 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +3.7 | 0.015 | 12/28 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +3.7 | 0.016 | 15/34 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.99×** | +3.5 | 0.025 | 10/24 (KATO III, LoVo, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.99×** | +3.4 | 0.035 | 6/18 (LoVo, A-427, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | 1.81× | +3.0 | 0.12 | 5/17 (BT-474, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15800.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.502×** | -4.8 | 0.001 | 21/34 (BT-474, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.429×** | -4.2 | 0.008 | 19/32 (HEC-1-A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Trimetrexate (drug)]] 5 µM |  | **0.593×** | -3.8 | 0.025 | 17/32 (A-172, HT-29, …) | all doses, flat | position effect removed |
| [[Trimetrexate (drug)]] 0.5 µM |  | **0.519×** | -3.4 | 0.072 | 10/30 (LS 180, HEC-1-A, …) | all doses, flat | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM |  | **0.521×** | -3.4 | 0.072 | 12/34 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.522×** | -3.4 | 0.072 | 17/34 (SNU-423, A-427, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **0.531×** | -3.3 | 0.072 | 12/31 (C-33 A, Hs 766T, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.5 µM |  | **0.533×** | -3.3 | 0.072 | 12/34 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here); position effect removed |
| [[Trimetrexate (drug)]] 0.05 µM |  | **0.533×** | -3.3 | 0.072 | 11/29 (SHP-77, RPMI-7951, …) | all doses, flat | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.540× | -3.0 | 0.15 | 12/27 (LS 180, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 4.46 | 0 | 1 | — | [[Sulfatinib (drug)]] 0.05 µM 0.0523× (z -8.9) |
| [[KATO III (line)]] | alt | 6.10 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 16.0× (z +8.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A-172 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.129 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.156 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.947 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.127 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.175 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.179 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.35 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | H2B clustered histone 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:26,216,200-26,216,688 (-) |
| Ensembl biotype | protein_coding |
| Also known as | H2B/a, H2B.1A; previously H2BFA, HIST1H2BG |
| Gene groups (HGNC) | H2B histones; Proteins encoded by multiple genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P62807](https://www.uniprot.org/uniprotkb/P62807) (Histone H2B type 1-C/E/F/G/I):

> Core component of nucleosome. Nucleosomes wrap and compact DNA into chromatin, limiting DNA accessibility to the cellular machineries which require DNA as a template. Histones thereby play a central role in transcription regulation, DNA repair, DNA replication and chromosomal stability. DNA accessibility is regulated via a complex set of post-translational modifications of histones, also called histone code, and nucleosome remodeling.; Has broad antibacterial activity. May contribute to the …

**Summary**, from NCBI Gene [8339](https://www.ncbi.nlm.nih.gov/gene/8339):

> Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Nucleosomes consist of approximately 146 bp of DNA wrapped around a histone octamer composed of pairs of each of the four core histones (H2A, H2B, H3, and H4). The chromatin fiber is further compacted through the interaction of a linker histone, H1, with the DNA between the nucleosomes to form higher order chromatin structures. The protein has antibacterial and …

**Accessions** — [HGNC:4746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4746) · Entrez [8339](https://www.ncbi.nlm.nih.gov/gene/8339) · UniProt [P62807](https://www.uniprot.org/uniprotkb/P62807) · Ensembl [ENSG00000273802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273802)

## Data

Gene col 15800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15800); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15800, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15800]; `tensor/DDL_lfc|DDL_z.npy` [15800]; `embed/gene_vectors.npy` [15800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15800 or target_col == 15800). Every well: [[H2BC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/H2BC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
