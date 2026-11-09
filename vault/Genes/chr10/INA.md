---
symbol: "INA"
type: "gene"
col: 7314
ensembl_id: "ENSG00000148798"
name: "internexin neuronal intermediate filament protein alpha"
location: "10q24.33"
module: 9
arm: "+"
pooled_cpm: 4.6
n_lines_expressing: 14
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# INA

*internexin neuronal intermediate filament protein alpha* — 10q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.65× (z +12.5, q 7e-33, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.50× (z +9.7, q 6e-20, up in 8 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSTR2]] (+0.58, fdr 1e-05), [[TNFRSF9]] (+0.57, fdr 1e-05), [[TRIM58]] (+0.55, fdr 3e-05); moves opposite to [[TNFSF12]] (-0.45, fdr 7e-05), [[SPCS1]] (-0.43, fdr 3e-04), [[WDR20]] (-0.43, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.65×** | +12.5 | 7e-33 | 4/5 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.26×** | +10.8 | 7e-25 | 6/8 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.50×** | +9.7 | 6e-20 | 8/11 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +7.7 | 3e-12 | 2/11 (A549, NCI-H23) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.99×** | +7.6 | 4e-12 | 4/7 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.59×** | +7.1 | 1e-10 | 9/11 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.28×** | +6.2 | 5e-08 | 2/9 (HOP62, J82) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +6.2 | 5e-08 | 7/12 (J82, HOP62, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.88×** | +5.7 | 1e-06 | 2/8 (SHP-77, A549) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +5.6 | 2e-06 | 2/9 (J82, A549) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +5.3 | 6e-06 | 12/12 (HOP62, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +5.3 | 6e-06 | 6/11 (A-427, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.4 | 6e-04 | 6/9 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +4.3 | 6e-04 | 3/12 (A-427, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.00×** | +4.3 | 7e-04 | 1/8 (NCI-H2347) | top dose only | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.021 | 4/12 (NCI-H23, CHP-212, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.53×** | +2.9 | 0.083 | 4/10 (A-427, A549, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7314.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.613× | -3.7 | 0.15 | 0/12 | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 14.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +12.7) | — |
| [[J82 (line)]] | alt | 11.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +13.5) | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +12.7) | — |
| [[A-172 (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.393 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.372 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSTR2]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[TNFRSF9]] | +0.57 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[TRIM58]] | +0.55 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[TEX15]] | +0.54 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[OLR1]] | +0.53 | +0.34 / +0.54 | both halves | 1e-04 |  |
| [[ELOVL4]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[FMN2]] | +0.50 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[TLL1]] | +0.49 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[TMEM52B]] | +0.49 | +0.33 / +0.52 | both halves | 1e-04 |  |
| [[SYNM]] | +0.49 | +0.48 / +0.49 | both halves | 2e-05 | same gene group; STRING 535 |
| [[ACSL5]] | +0.48 | +0.43 / +0.34 | both halves | 1e-04 |  |
| [[PEG10]] | +0.48 | +0.46 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFSF12]] | -0.45 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[SPCS1]] | -0.43 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[WDR20]] | -0.43 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[LINC01118]] | -0.43 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[MZT2A]] | -0.42 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[MZT2B]] | -0.41 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[ZBTB47-AS1]] | -0.41 | -0.45 / -0.22 | both halves | 6e-04 |  |
| [[SRGAP2D]] | -0.41 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[FBLN7]] | -0.41 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[NDUFA4]] | -0.41 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[TMEM165]] | -0.41 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[CDC27]] | -0.40 | -0.41 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.342). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.1, 25.5); signed map (44.3, 17.9). **Vector** length 27.1, 6.15% of its response variance represented; |z| ≥ 3 in 252 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +6.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.7 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.8 | -0.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.5 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.5 | -0.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.4 | -1.6 |
|  | [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift | -0.4 | -2.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.4 | -0.3 |
|  | [[Malotilate (drug)]] 5 µM |  | -0.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | internexin neuronal intermediate filament protein alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.33 — chr10:103,277,138-103,290,346 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NF-66; previously NEF5 |
| Gene groups (HGNC) | Intermediate filaments Type IV |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16352](https://www.uniprot.org/uniprotkb/Q16352) (Alpha-internexin):

> Class-IV neuronal intermediate filament that is able to self-assemble. It is involved in the morphogenesis of neurons. It may form an independent structural network without the involvement of other neurofilaments or it may cooperate with NEFL to form the filamentous backbone to which NEFM and NEFH attach to form the cross-bridges. May also cooperate with the neuronal intermediate filament protein PRPH to form filamentous networks (By similarity).

**Summary**, from NCBI Gene [9118](https://www.ncbi.nlm.nih.gov/gene/9118):

> Neurofilaments are type IV intermediate filament heteropolymers composed of light, medium, and heavy chains. Neurofilaments comprise the axoskeleton and they functionally maintain the neuronal caliber. They may also play a role in intracellular transport to axons and dendrites. This gene is a member of the intermediate filament family and is involved in the morphogenesis of neurons. [provided by RefSeq, Jun 2009]

**Accessions** — [HGNC:6057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6057) · Entrez [9118](https://www.ncbi.nlm.nih.gov/gene/9118) · UniProt [Q16352](https://www.uniprot.org/uniprotkb/Q16352) · Ensembl [ENSG00000148798](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148798)

## Data

Gene col 7314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7314); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7314]; `tensor/DDL_lfc|DDL_z.npy` [7314]; `embed/gene_vectors.npy` [7314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7314 or target_col == 7314). Every well: [[INA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
