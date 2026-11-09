---
symbol: "TFPT"
type: "gene"
col: 2630
ensembl_id: "ENSG00000105619"
name: "TCF3 fusion partner"
location: "19q13.42"
module: 118
arm: "+"
pooled_cpm: 9.64
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# TFPT

*TCF3 fusion partner* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.03× (z +8.4, q 4e-14, up in 36 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (C32 0.0823×); [[Dinaciclib (drug)]] 5 µM in 1 line (RPMI-7951 0.157×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HOP62 0.0950×); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (SNU-423 0.0857×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMM29]] (+0.64, fdr 1e-05), [[GPN2]] (+0.63, fdr 7e-06), [[NGDN]] (+0.62, fdr 2e-05); moves opposite to [[RBBP7]] (-0.57, fdr 2e-05), [[IPO5]] (-0.56, fdr 2e-05), [[IPO7]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 118]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2630.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.03×** | +8.4 | 4e-14 | 36/45 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.67×** | +5.9 | 1e-06 | 12/20 (SW480, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.62×** | +5.7 | 2e-06 | 20/32 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +5.1 | 4e-05 | 22/40 (SK-MEL-2, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.90×** | +4.8 | 2e-04 | 14/38 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.6 | 4e-04 | 18/38 (NCI-H2030, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.003 | 16/43 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.013 | 13/48 (KATO III, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.34×** | +3.5 | 0.029 | 8/42 (SW 900, NCI-H2030, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.3 | 0.053 | 0/48 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.35×** | +3.3 | 0.053 | 10/25 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.059 | 7/45 (A549, PANC-1, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | 1.51× | +3.0 | 0.10 | 1/45 (SK-MEL-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2630.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (C32 0.0823×); [[Dinaciclib (drug)]] 5 µM in 1 line (RPMI-7951 0.157×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HOP62 0.0950×); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (SNU-423 0.0857×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.752× | -3.1 | 0.88 | 8/47 (NCI-H1792, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2630. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 12.3 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0823× (z -10.0) |
| [[HOP62 (line)]] | alt | 3.53 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0950× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 6.35 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0857× (z -8.9) |
| [[SW480 (line)]] | alt | 12.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2630), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM29]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[GPN2]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[NGDN]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[LZTS2]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[RFXANK]] | +0.61 | +0.40 / +0.63 | both halves | 4e-05 |  |
| [[TMEM208]] | +0.60 | +0.43 / +0.70 | both halves | 3e-05 |  |
| [[WDR83]] | +0.59 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[DNLZ]] | +0.59 | +0.38 / +0.61 | both halves | 7e-05 |  |
| [[ZNF581]] | +0.59 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[PI4KB]] | +0.59 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[CCDC142]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ZNF580]] | +0.58 | +0.36 / +0.64 | both halves | 1e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP7]] | -0.57 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[IPO5]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[IPO7]] | -0.54 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[BCAP29]] | -0.54 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[AKAP11]] | -0.52 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[EFR3A]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[LBR]] | -0.50 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[MYBL1]] | -0.50 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[DNAJC10]] | -0.50 | -0.46 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.689). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-45.0, 9.3); signed map (-5.7, -5.2). **Vector** length 45.9, 5.81% of its response variance represented; |z| ≥ 3 in 663 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.1 | +8.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | +0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -0.9 | +0.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.9 | -2.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | TCF3 fusion partner |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:54,107,020-54,115,657 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FB1, amida, INO80F |
| Gene groups (HGNC) | INO80 complex subunits |
| Reactome | 6 pathways, smallest: DNA Damage Recognition in GG-NER; UCH proteinases; Global Genome Nucleotide Excision Repair (GG-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [P0C1Z6](https://www.uniprot.org/uniprotkb/P0C1Z6) (TCF3 fusion partner):

> Appears to promote apoptosis in a p53/TP53-independent manner.; Putative regulatory component of the chromatin remodeling INO80 complex which is involved in transcriptional regulation, DNA replication and probably DNA repair.

**Summary**, from NCBI Gene [29844](https://www.ncbi.nlm.nih.gov/gene/29844):

> Predicted to enable DNA binding activity and protein kinase binding activity. Involved in several processes, including apoptotic signaling pathway; positive regulation of DNA-templated transcription; and regulation of DNA metabolic process. Located in nucleoplasm. Part of Ino80 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13630](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13630) · Entrez [29844](https://www.ncbi.nlm.nih.gov/gene/29844) · UniProt [P0C1Z6](https://www.uniprot.org/uniprotkb/P0C1Z6) · Ensembl [ENSG00000105619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105619)

## Data

Gene col 2630: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2630); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2630, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2630]; `tensor/DDL_lfc|DDL_z.npy` [2630]; `embed/gene_vectors.npy` [2630]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2630 or target_col == 2630). Every well: [[TFPT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFPT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
