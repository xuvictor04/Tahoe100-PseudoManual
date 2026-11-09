---
symbol: "AURKAIP1"
type: "gene"
col: 10644
ensembl_id: "ENSG00000175756"
name: "aurora kinase A interacting protein 1"
location: "1p36.33"
module: 54
arm: "+"
pooled_cpm: 18.74
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# AURKAIP1

*aurora kinase A interacting protein 1* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.69× (z +7.1, q 9e-10, up in 27 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Arbutin (drug)]] 5 µM: 1.59× (z +3.3, q 0.076, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.595× (z -5.5, q 3e-05, down in 32 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.185×, NCI-H2030 0.317×, NCI-H23 0.318×).
> Its strongest partners by |cos| (79 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFS8]] (+0.70, fdr 7e-06), [[MRPS12]] (+0.69, fdr 1e-05), [[SF3B5]] (+0.68, fdr 2e-04, ⚠ SF3B5 in the vector space only through flagged drug-doses), [[EMC6]] (+0.67, fdr 3e-04); moves opposite to [[CROCC]] (-0.56, fdr 2e-04), [[DDX39B]] (-0.54, fdr 4e-04), [[SRRM2]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10644.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.69×** | +7.1 | 9e-10 | 27/30 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.26×** | +6.7 | 5e-09 | 34/40 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.90×** | +4.8 | 3e-04 | 35/45 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.8 | 3e-04 | 35/43 (CFPAC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.87×** | +4.3 | 0.002 | 23/36 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.39×** | +3.4 | 0.060 | 26/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.59×** | +3.3 | 0.076 | 25/46 (NCI-H2030, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10644.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.185×, NCI-H2030 0.317×, NCI-H23 0.318×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.595×** | -5.5 | 3e-05 | 32/47 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.643× | -3.2 | 0.33 | 24/47 (LoVo, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10644. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -8.5) |
| [[A-172 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10644), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 25 of them with an alert (⚠; 21 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFS8]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[MRPS12]] | +0.69 | +0.52 / +0.70 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 979 |
| [[SF3B5]] ⚠ | +0.68 | +0.32 / +0.74 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL41]] ⚠ | +0.68 | +0.37 / +0.74 | both halves | 8e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 968; ⚠ in the vector space only through flagged drug-doses |
| [[EMC6]] | +0.67 | +0.29 / +0.77 | both halves | 3e-04 |  |
| [[C19orf53]] | +0.67 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[RAB5IF]] | +0.67 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[TOMM22]] | +0.66 | +0.53 / +0.66 | both halves | 1e-05 | STRING 615 |
| [[POP7]] | +0.66 | +0.40 / +0.66 | both halves | 4e-05 |  |
| [[MICOS13]] | +0.65 | +0.39 / +0.70 | both halves | 5e-05 | STRING 425 |
| [[MRPL12]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 868 |
| [[TMEM160]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[CENPX]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TMEM147]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCC]] | -0.56 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[DDX39B]] | -0.54 | -0.24 / -0.52 | both halves | 4e-04 |  |
| [[SRRM2]] | -0.54 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[RYR2]] | -0.54 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[CHD3]] | -0.52 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[GALC]] | -0.52 | -0.24 / -0.48 | both halves | 4e-04 |  |
| [[ACADM]] | -0.52 | -0.23 / -0.52 | both halves | 5e-04 |  |
| [[PRKAR1A]] | -0.51 | -0.23 / -0.48 | both halves | 5e-04 |  |
| [[CYB5D2]] | -0.51 | -0.31 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-45.3, -12.0); signed map (-36.8, 5.9). **Vector** length 48.0, 10.6% of its response variance represented; |z| ≥ 3 in 477 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.3 | +0.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.3 | +0.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.0 | +1.9 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.0 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +0.7 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +0.7 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -3.9 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -3.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -2.5 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | aurora kinase A interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,373,730-1,375,207 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cox24, AKIP, AIP, FLJ20608, mS38 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWT8](https://www.uniprot.org/uniprotkb/Q9NWT8) (Small ribosomal subunit protein bS22, mitochondrial):

> May act as a negative regulator of Aurora-A kinase, by down-regulation through proteasome-dependent degradation.

**Summary**, from NCBI Gene [54998](https://www.ncbi.nlm.nih.gov/gene/54998):

> Acts upstream of or within positive regulation of proteolysis. Located in mitochondrial matrix and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24114) · Entrez [54998](https://www.ncbi.nlm.nih.gov/gene/54998) · UniProt [Q9NWT8](https://www.uniprot.org/uniprotkb/Q9NWT8) · Ensembl [ENSG00000175756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175756)

## Data

Gene col 10644: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10644); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10644, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10644]; `tensor/DDL_lfc|DDL_z.npy` [10644]; `embed/gene_vectors.npy` [10644]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10644 or target_col == 10644). Every well: [[AURKAIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AURKAIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
