---
symbol: "CPTP"
type: "gene"
col: 13376
ensembl_id: "ENSG00000224051"
name: "ceramide-1-phosphate transfer protein"
location: "1p36.33"
module: 7
arm: "+"
pooled_cpm: 3.13
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CPTP

*ceramide-1-phosphate transfer protein* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.78× (z +9.3, q 8e-18, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.566× (z -7.3, q 2e-10, down in 26 of 36 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPUSD1]] (+0.77, fdr 7e-06), [[UBL4A]] (+0.68, fdr 7e-06), [[STUB1]] (+0.67, fdr 1e-05); moves opposite to [[KMT2E-AS1]] (-0.59, fdr 1e-04), [[CYB5D2]] (-0.56, fdr 2e-04), [[RYR2]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.78×** | +9.3 | 8e-18 | 37/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.53×** | +8.4 | 9e-15 | 33/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.97×** | +6.2 | 1e-07 | 23/43 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.95×** | +6.1 | 2e-07 | 8/16 (NCI-H2030, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.2 | 0.003 | 8/27 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.1 | 0.004 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.011 | 8/44 (NCI-H23, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.064 | 6/43 (SW 900, Panc 03.27, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.43×** | +3.3 | 0.064 | 1/44 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13376.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.566×** | -7.3 | 2e-10 | 26/36 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.557×** | -5.3 | 3e-05 | 14/30 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.560×** | -5.3 | 3e-05 | 19/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.626×** | -4.1 | 0.006 | 18/41 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.643×** | -4.0 | 0.007 | 14/42 (RPMI-7951, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.665×** | -3.7 | 0.020 | 14/42 (KATO III, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 3.87 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -9.4) |
| [[A498 (line)]] | wt | 2.86 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0982× (z -8.5) |
| [[Hs 766T (line)]] | wt | 4.20 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -8.8) |
| [[J82 (line)]] | alt | 4.96 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0767× (z -9.3) |
| [[PANC-1 (line)]] | alt | 4.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 5.04 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0729× (z -8.9) |
| [[A-172 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPUSD1]] | +0.77 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[UBL4A]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[STUB1]] | +0.67 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[RIC8A]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ICE1]] | +0.65 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ASB6]] | +0.63 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CDPF1]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[TMEM115]] | +0.61 | +0.63 / +0.78 | both halves | 7e-06 |  |
| [[LRRC14]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[RGS19]] | +0.61 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[TM2D2]] | +0.60 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[SLC35C1]] | +0.59 | +0.61 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2E-AS1]] | -0.59 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[CYB5D2]] | -0.56 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[RYR2]] | -0.55 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[MROH8]] | -0.55 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[LYRM1]] | -0.55 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[FAM151B-DT]] | -0.54 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[MSTO1]] | -0.54 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[C12orf57]] | -0.54 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[SNAP25-AS1]] | -0.53 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[PNISR]] | -0.53 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[FAM81A]] | -0.53 | -0.38 / -0.60 | both halves | 7e-05 |  |
| [[CCDC170]] | -0.53 | -0.44 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.380). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-46.9, -1.4); signed map (-6.7, -27.8). **Vector** length 50.8, 6.43% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +8.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +9.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.6 | +6.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.1 | +6.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +2.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.2 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.0 | +0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -0.6 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | -1.0 | -1.7 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ceramide-1-phosphate transfer protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,324,756-1,328,896 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10334; previously GLTPD1 |
| Gene groups (HGNC) | Glycolipid transfer protein family |
| Reactome | 2 pathways, smallest: Glycosphingolipid transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TA50](https://www.uniprot.org/uniprotkb/Q5TA50) (Ceramide-1-phosphate transfer protein):

> Mediates the intracellular transfer of ceramide-1-phosphate (C1P) between organelle membranes and the cell membrane. Required for normal structure of the Golgi stacks. Can bind phosphoceramides with a variety of aliphatic chains, but has a preference for lipids with saturated C16:0 or monounsaturated C18:1 aliphatic chains, and is inefficient with phosphoceramides containing lignoceryl (C24:0). Plays a role in the regulation of the cellular levels of ceramide-1-phosphate, and thereby …

**Summary**, from NCBI Gene [80772](https://www.ncbi.nlm.nih.gov/gene/80772):

> Enables ceramide 1-phosphate binding activity and ceramide 1-phosphate transfer activity. Involved in several processes, including ceramide 1-phosphate transport; negative regulation of NLRP3 inflammasome complex assembly; and negative regulation of interleukin-1 beta production. Is active in cytosol and trans-Golgi network membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28116](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28116) · Entrez [80772](https://www.ncbi.nlm.nih.gov/gene/80772) · UniProt [Q5TA50](https://www.uniprot.org/uniprotkb/Q5TA50) · Ensembl [ENSG00000224051](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224051)

## Data

Gene col 13376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13376); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13376]; `tensor/DDL_lfc|DDL_z.npy` [13376]; `embed/gene_vectors.npy` [13376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13376 or target_col == 13376). Every well: [[CPTP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPTP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
