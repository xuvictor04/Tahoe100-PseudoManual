---
symbol: "CUTA"
type: "gene"
col: 3374
ensembl_id: "ENSG00000112514"
name: "cutA divalent cation tolerance homolog"
location: "6p21.32"
module: 24
arm: "+"
pooled_cpm: 21.42
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# CUTA

*cutA divalent cation tolerance homolog* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.15× (z +9.8, q 6e-20, up in 38 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +5.0, q 7e-05, up in 35 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 4.64×, HT-29 4.59×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 3.57×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 4.37×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.360× (z -4.0, q 0.038, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPC2]] (+0.76, fdr 7e-06), [[GABARAP]] (+0.71, fdr 7e-06, ⚠ GABARAP in the vector space only through flagged drug-doses), [[RNASEK]] (+0.71, fdr 7e-06), [[CNNM2]] (+0.70, fdr 1e-05); moves opposite to [[CCT5]] (-0.67, fdr 1e-05), [[CCT6A]] (-0.62, fdr 1e-05), [[CCT7]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3374.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 4.64×, HT-29 4.59×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 3.57×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 4.37×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.15×** | +9.8 | 6e-20 | 38/40 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.52×** | +7.6 | 9e-12 | 29/32 (A-172, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **2.18×** | +6.6 | 6e-09 | 36/44 (KATO III, Panc 03.27, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.82×** | +5.1 | 4e-05 | 34/46 (KATO III, SW480, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.0 | 7e-05 | 35/47 (NCI-H2347, KATO III, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.84×** | +4.8 | 1e-04 | 29/36 (A-172, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.8 | 0.011 | 25/45 (HepG2/C3A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.48×** | +3.3 | 0.060 | 21/47 (HS-578T, A549, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | 1.44× | +3.0 | 0.17 | 17/46 (HT-29, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3374.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.360×** | -4.0 | 0.038 | 33/46 (RKO, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 28.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HT-29 (line)]] | alt | 23.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 27.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPC2]] | +0.76 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[GABARAP]] ⚠ | +0.71 | +0.71 / +0.66 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RNASEK]] | +0.71 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[CNNM2]] | +0.70 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[DPM3]] | +0.67 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[SNHG9]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[TRIM52-AS1]] | +0.65 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[GABARAPL2]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[VEGFB]] | +0.64 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[SCAMP3]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[MIEN1]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[NDUFA2]] | +0.63 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[SIRT2]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | -0.67 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[CCT6A]] | -0.62 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[CCT7]] | -0.61 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.61 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[STIP1]] | -0.60 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[PTPN11]] | -0.59 | -0.39 / -0.67 | both halves | 6e-05 |  |
| [[NUDC]] | -0.58 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.58 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[CCT3]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[TCOF1]] | -0.57 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[CCT2]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.56 | -0.41 / -0.64 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-8.4, -46.0); signed map (-10.7, 6.9). **Vector** length 58.8, 13.4% of its response variance represented; |z| ≥ 3 in 526 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +3.4 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +0.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -0.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cutA divalent cation tolerance homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,416,442-33,418,317 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C6orf82, ACHAP |
| Matched by | ensembl_id |

**Function**, from UniProt [O60888](https://www.uniprot.org/uniprotkb/O60888) (Protein CutA):

> May form part of a complex of membrane proteins attached to acetylcholinesterase (AChE).

**Summary**, from NCBI Gene [51596](https://www.ncbi.nlm.nih.gov/gene/51596):

> Enables enzyme binding activity. Involved in intracellular protein localization. Located in membrane and mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21101) · Entrez [51596](https://www.ncbi.nlm.nih.gov/gene/51596) · UniProt [O60888](https://www.uniprot.org/uniprotkb/O60888) · Ensembl [ENSG00000112514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112514)

## Data

Gene col 3374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3374); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3374]; `tensor/DDL_lfc|DDL_z.npy` [3374]; `embed/gene_vectors.npy` [3374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3374 or target_col == 3374). Every well: [[CUTA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUTA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
