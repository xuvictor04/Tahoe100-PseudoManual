---
symbol: "FBXW5"
type: "gene"
col: 8212
ensembl_id: "ENSG00000159069"
name: "F-box and WD repeat domain containing 5"
location: "9q34.3"
module: 24
arm: "+"
pooled_cpm: 18.35
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# FBXW5

*F-box and WD repeat domain containing 5* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.16× (z +6.7, q 9e-09, up in 32 of 37 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.376× (z -4.4, q 0.005, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFAND2B]] (+0.72, fdr 7e-06), [[PCGF1]] (+0.71, fdr 7e-06, ⚠ PCGF1 in the vector space only through flagged drug-doses), [[RCE1]] (+0.71, fdr 1e-05), [[SNHG32]] (+0.70, fdr 7e-06); moves opposite to [[HNRNPA3]] (-0.64, fdr 2e-05), [[VMA21]] (-0.62, fdr 1e-05), [[TMX1]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8212.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +6.7 | 9e-09 | 32/37 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +5.6 | 6e-06 | 21/31 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.59×** | +4.0 | 0.010 | 26/43 (CFPAC-1, A-427, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8212.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.376×** | -4.4 | 0.005 | 31/43 (H4, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.647×** | -3.8 | 0.047 | 28/47 (SNU-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | 0.687× | -3.2 | 0.22 | 20/47 (AsPC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Tadalafil (drug)]] 5 µM |  | 0.690× | -3.1 | 0.28 | 18/47 (HS-578T, SNU-423, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.693× | -3.0 | 0.30 | 21/47 (Panc 03.27, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFAND2B]] | +0.72 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[PCGF1]] ⚠ | +0.71 | +0.60 / +0.68 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RCE1]] | +0.71 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[SNHG32]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.69 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[RNF166]] | +0.69 | +0.46 / +0.75 | both halves | 2e-05 |  |
| [[GGNBP2]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[SNHG12]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[SNHG7]] | +0.67 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[RILP]] | +0.66 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[SAT2]] | +0.66 | +0.46 / +0.71 | both halves | 2e-05 |  |
| [[SMIM26]] ⚠ | +0.66 | +0.47 / +0.72 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EPB41L4A-AS1]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ENKD1]] | +0.65 | +0.47 / +0.70 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA3]] | -0.64 | -0.48 / -0.72 | both halves | 2e-05 |  |
| [[VMA21]] | -0.62 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[TMX1]] | -0.61 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[C1QBP]] | -0.61 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[BANF1]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[EIF5A]] | -0.59 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[PAICS]] | -0.59 | -0.45 / -0.68 | both halves | 3e-05 |  |
| [[IPO5]] | -0.57 | -0.40 / -0.64 | both halves | 4e-05 |  |
| [[RBBP7]] | -0.56 | -0.43 / -0.64 | both halves | 3e-05 | same gene group; pathway: Neddylation |
| [[FKBP1A]] | -0.56 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[NUP155]] | -0.56 | -0.50 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.657). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-38.5, -14.9); signed map (-16.5, -1.9). **Vector** length 57.1, 11.3% of its response variance represented; |z| ≥ 3 in 498 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | -0.8 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +0.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.4 | +1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.3 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.2 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.8 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | F-box and WD repeat domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,940,435-136,944,738 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434B205, MGC20962, Fbw5 |
| Gene groups (HGNC) | WD repeat domain containing; F-box and WD repeat domain containing |
| Reactome | 7 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969U6](https://www.uniprot.org/uniprotkb/Q969U6) (F-box/WD repeat-containing protein 5):

> Substrate recognition component of both SCF (SKP1-CUL1-F-box protein) and DCX (DDB1-CUL4-X-box) E3 ubiquitin-protein ligase complexes. Substrate recognition component of the SCF(FBXW5) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of SASS6 during S phase, leading to prevent centriole reduplication. The SCF(FBXW5) complex also mediates ubiquitination and degradation of actin-regulator EPS8 during G2 phase, leading to the transient …

**Summary**, from NCBI Gene [54461](https://www.ncbi.nlm.nih.gov/gene/54461):

> This gene encodes a member of the F-box protein family, members of which are characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into three classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein …

**Accessions** — [HGNC:13613](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13613) · Entrez [54461](https://www.ncbi.nlm.nih.gov/gene/54461) · UniProt [Q969U6](https://www.uniprot.org/uniprotkb/Q969U6) · Ensembl [ENSG00000159069](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159069)

## Data

Gene col 8212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8212); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8212]; `tensor/DDL_lfc|DDL_z.npy` [8212]; `embed/gene_vectors.npy` [8212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8212 or target_col == 8212). Every well: [[FBXW5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXW5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
