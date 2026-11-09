---
symbol: "TMEM115"
type: "gene"
col: 4711
ensembl_id: "ENSG00000126062"
name: "transmembrane protein 115"
location: "3p21.31"
module: 7
arm: "+"
pooled_cpm: 4.23
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TMEM115

*transmembrane protein 115* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.00× (z +6.2, q 3e-07, up in 15 of 28 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.59× (z +4.6, q 6e-04, up in 15 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.564× (z -5.1, q 2e-04, down in 23 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 0.114×, SW1417 0.142×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (SW480 0.0386×); [[Fingolimod (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.0726×; ⚠ toxic); [[Vandetanib (drug)]] 0.05 µM in 1 line (SNU-423 0.0584×); [[Daidzin (drug)]] 0.05 µM in 1 line (SHP-77 0.0454×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL20-AS1]] (+0.71, fdr 7e-06), [[TSSC4]] (+0.68, fdr 7e-06), [[C6orf47]] (+0.68, fdr 7e-06); moves opposite to [[CD83]] (-0.48, fdr 2e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4711.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +6.2 | 3e-07 | 15/28 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +5.0 | 1e-04 | 13/27 (LoVo, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +5.0 | 1e-04 | 0/9 | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.59×** | +4.6 | 6e-04 | 15/42 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.5 | 8e-04 | 18/41 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +4.3 | 0.002 | 11/45 (SW480, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.053 | 9/40 (A-427, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | 1.26× | +3.0 | 0.17 | 3/46 (HepG2/C3A, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4711.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 0.114×, SW1417 0.142×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (SW480 0.0386×); [[Fingolimod (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.0726×; ⚠ toxic); [[Vandetanib (drug)]] 0.05 µM in 1 line (SNU-423 0.0584×); [[Daidzin (drug)]] 0.05 µM in 1 line (SHP-77 0.0454×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.564×** | -5.1 | 2e-04 | 23/42 (SW480, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.769× | -3.5 | 0.15 | 20/39 (SNU-423, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4711. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 6.09 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0726× (z -11.0) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 3.42 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 3.77 | 0 | 1 | — | [[Daidzin (drug)]] 0.05 µM 0.0454× (z -8.8) |
| [[SNU-423 (line)]] | alt | 4.82 | 0 | 1 | — | [[Vandetanib (drug)]] 0.05 µM 0.0584× (z -10.4) |
| [[SW1417 (line)]] | alt | 7.03 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 4.01 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0386× (z -16.0) |
| [[A-172 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4711), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL20-AS1]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[TSSC4]] | +0.68 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[C6orf47]] | +0.68 | +0.60 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[MFSD5]] | +0.67 | +0.50 / +0.68 | both halves | 1e-05 | STRING 506 |
| [[SMG8]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[FASTKD5]] | +0.66 | +0.55 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[C12orf43]] | +0.65 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[MRM3]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[GPATCH3]] | +0.63 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[TM2D2]] | +0.63 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[LRRC14]] | +0.63 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[TIMM22]] | +0.63 | +0.51 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD83]] | -0.48 | -0.31 / -0.53 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.679). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-46.6, -0.5); signed map (-5.1, -25.7). **Vector** length 53.5, 7.21% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +4.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.8 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +1.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.9 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.2 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Capivasertib (drug)]] 0.5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 115 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,354,750-50,359,521 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PL6 |
| Gene groups (HGNC) | Rhomboid family |
| Reactome | 6 pathways, smallest: COPI-mediated anterograde transport; ER to Golgi Anterograde Transport; Transport to the Golgi and subsequent modification |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12893](https://www.uniprot.org/uniprotkb/Q12893) (Transmembrane protein 115):

> May play a role in retrograde transport of proteins from the Golgi to the endoplasmic reticulum. May indirectly play a role in protein glycosylation in the Golgi.

**Summary**, from NCBI Gene [11070](https://www.ncbi.nlm.nih.gov/gene/11070):

> Enables identical protein binding activity. Involved in retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum. Located in COG complex; Golgi cisterna membrane; and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30055](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30055) · Entrez [11070](https://www.ncbi.nlm.nih.gov/gene/11070) · UniProt [Q12893](https://www.uniprot.org/uniprotkb/Q12893) · Ensembl [ENSG00000126062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126062)

## Data

Gene col 4711: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4711); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4711, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4711]; `tensor/DDL_lfc|DDL_z.npy` [4711]; `embed/gene_vectors.npy` [4711]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4711 or target_col == 4711). Every well: [[TMEM115 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM115.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
