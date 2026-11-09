---
symbol: "GPKOW"
type: "gene"
col: 890
ensembl_id: "ENSG00000068394"
name: "G-patch domain and KOW motifs"
location: "Xp11.23"
module: 7
arm: "+"
pooled_cpm: 12.86
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# GPKOW

*G-patch domain and KOW motifs* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.78× (z +10.0, q 7e-21, up in 35 of 46 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.69× (z +9.5, q 4e-19, up in 33 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bicalutamide (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0748×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POP4]] (+0.67, fdr 7e-06), [[MRPS18A]] (+0.67, fdr 7e-06), [[RNF40]] (+0.66, fdr 7e-06); moves opposite to [[EIF2S3]] (-0.57, fdr 5e-05), [[SNHG16]] (-0.56, fdr 4e-05), [[SRD5A1]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.78×** | +10.0 | 7e-21 | 35/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +9.5 | 4e-19 | 33/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.73×** | +9.5 | 4e-19 | 34/48 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.44×** | +9.2 | 4e-18 | 31/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +6.9 | 5e-10 | 3/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.46×** | +6.9 | 5e-10 | 23/47 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +6.4 | 1e-08 | 22/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +6.0 | 1e-07 | 19/47 (PANC-1, SW480, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.38×** | +5.8 | 4e-07 | 20/46 (SW480, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +5.8 | 4e-07 | 19/43 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.36×** | +5.6 | 1e-06 | 18/42 (HCT15, SW 900, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +5.5 | 2e-06 | 13/47 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.38×** | +5.4 | 2e-06 | 18/46 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +5.3 | 5e-06 | 16/46 (PANC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.37×** | +5.3 | 5e-06 | 18/43 (NCI-H460, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.028 | 5/48 (SHP-77, NCI-H23, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +2.9 | 0.087 | 6/46 (J82, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 890.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bicalutamide (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0748×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.869× | -3.6 | 0.21 | 13/48 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.832× | -3.3 | 0.24 | 8/47 (hTERT-HPNE, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.832× | -3.1 | 0.32 | 6/45 (SW 900, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +10.2) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.08× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 7.88 | 0 | 1 | — | [[Bicalutamide (drug)]] 0.5 µM 0.0748× (z -9.4) |
| [[PANC-1 (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.5) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[A-172 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP4]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[MRPS18A]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[RNF40]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ASB8]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ZSCAN26]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[COA3]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[MRFAP1L1]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CRNKL1]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 832 |
| [[CSTF2T]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[DPF2]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TBCC]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[DHX16]] | +0.61 | +0.64 / +0.61 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 999 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2S3]] | -0.57 | -0.39 / -0.62 | both halves | 5e-05 |  |
| [[SNHG16]] | -0.56 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[SRD5A1]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.643). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-33.5, -1.0); signed map (-0.0, -25.9). **Vector** length 52.6, 7.03% of its response variance represented; |z| ≥ 3 in 777 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.3 | +9.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.2 | +10.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | +2.4 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +6.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.0 | +9.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | +5.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +0.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | +0.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | +0.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | G-patch domain and KOW motifs |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:49,113,407-49,123,735 (-) |
| Ensembl biotype | protein_coding |
| Also known as | T54, GPATC5, GPATCH5, Spp2, Mos2 |
| Gene groups (HGNC) | G-patch domain containing; NTC associated proteins; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92917](https://www.uniprot.org/uniprotkb/Q92917) (G-patch domain and KOW motifs-containing protein):

> RNA-binding protein involved in pre-mRNA splicing. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable).

**Summary**, from NCBI Gene [27238](https://www.ncbi.nlm.nih.gov/gene/27238):

> This gene encodes a putative RNA-binding protein containing G-patch and KOW (Kyprides, Ouzounis, Woese) domains. The encoded protein interacts directly with protein kinase A and protein kinase X and is also found associated with the spliceosome. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:30677](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30677) · Entrez [27238](https://www.ncbi.nlm.nih.gov/gene/27238) · UniProt [Q92917](https://www.uniprot.org/uniprotkb/Q92917) · Ensembl [ENSG00000068394](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068394)

## Data

Gene col 890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 890); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 890]; `tensor/DDL_lfc|DDL_z.npy` [890]; `embed/gene_vectors.npy` [890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 890 or target_col == 890). Every well: [[GPKOW — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPKOW.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
