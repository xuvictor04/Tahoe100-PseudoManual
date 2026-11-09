---
symbol: "TRMT2A"
type: "gene"
col: 1825
ensembl_id: "ENSG00000099899"
name: "tRNA methyltransferase 2A"
location: "22q11.21"
module: 107
arm: "+"
pooled_cpm: 5.3
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# TRMT2A

*tRNA methyltransferase 2A* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.83× (z +6.5, q 6e-08, up in 5 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.60× (z +5.2, q 3e-05, up in 18 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.571× (z -8.8, q 1e-15, down in 26 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPH7]] (+0.71, fdr 7e-06), [[COASY]] (+0.70, fdr 1e-05), [[ARFGAP1]] (+0.65, fdr 7e-06); moves opposite to [[PFN1]] (-0.53, fdr 1e-04), [[CALM2]] (-0.53, fdr 3e-05), [[RNF19A]] (-0.53, fdr 3e-05).
> It is in [[Module 107]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1825.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +6.5 | 6e-08 | 5/10 (CFPAC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +5.7 | 3e-06 | 4/14 (HS-578T, SW1417, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +5.2 | 3e-05 | 18/45 (SK-MEL-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +5.2 | 3e-05 | 17/44 (HT-29, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +5.1 | 3e-05 | 9/25 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +4.5 | 7e-04 | 9/33 (NCI-H2347, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +4.5 | 7e-04 | 18/44 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +4.3 | 0.002 | 17/43 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.65×** | +3.9 | 0.005 | 7/42 (J82, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +3.7 | 0.011 | 12/46 (NCI-H460, SW1417, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.057 | 6/43 (PANC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | **1.37×** | +3.2 | 0.064 | 4/42 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.33×** | +3.1 | 0.075 | 6/42 (A549, HOP62, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.1 | 0.075 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1825.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.571×** | -8.8 | 1e-15 | 26/39 (SW1417, SW48, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.528×** | -7.1 | 4e-10 | 24/38 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.636×** | -5.0 | 1e-04 | 17/44 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.763×** | -4.2 | 0.003 | 14/45 (A549, SW 900, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.697×** | -3.9 | 0.013 | 9/43 (COLO 205, A549, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.724×** | -3.6 | 0.033 | 10/46 (AsPC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | 0.741× | -3.2 | 0.11 | 14/43 (NCI-H2030, AsPC-1, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1825. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.26 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0369× (z -20.2) |
| [[HCT15 (line)]] | alt | 7.29 | 0 | 1 | — | [[Retinoic acid (drug)]] 0.5 µM 0.0697× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 4.22 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0690× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 8.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -8.6) |
| [[SW 900 (line)]] | alt | 5.23 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0686× (z -9.1) |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -10.0) |
| [[SW48 (line)]] | wt | 7.29 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -9.2) |
| [[A-172 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1825), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH7]] | +0.71 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[COASY]] | +0.70 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[ARFGAP1]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 | same gene group |
| [[L3MBTL2]] | +0.63 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[PHRF1]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[XAB2]] | +0.62 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[B4GALT3]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ADPGK]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[BAP1]] | +0.61 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[AARS2]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[NUP214]] | +0.61 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[WDR24]] | +0.61 | +0.49 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFN1]] | -0.53 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[CALM2]] | -0.53 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[RNF19A]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[TMSB4X]] | -0.51 | -0.32 / -0.60 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.6, -4.4); signed map (-12.0, -26.4). **Vector** length 54.6, 7.22% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.2 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.2 | +3.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.9 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -7.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,111,875-20,117,392 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HTF9C |
| Gene groups (HGNC) | MicroRNA protein coding host genes; 7BS C5-uridine RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZ69](https://www.uniprot.org/uniprotkb/Q8IZ69) (tRNA):

> S-adenosyl-L-methionine-dependent methyltransferase that catalyzes the formation of 5-methyl-uridine in tRNAs and some mRNAs. Mainly catalyzes the methylation of uridine at position 54 (m5U54) in cytosolic tRNAs. Also able to mediate the formation of 5-methyl-uridine in some mRNAs.

**Summary**, from NCBI Gene [27037](https://www.ncbi.nlm.nih.gov/gene/27037):

> The protein encoded by this gene is of unknown function. However, it is orthologous to the mouse Trmt2a gene and contains an RNA methyltransferase domain. Expression of this gene varies during the cell cycle, with aberrant expression being a possible biomarker in certain breast cancers. Several transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:24974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24974) · Entrez [27037](https://www.ncbi.nlm.nih.gov/gene/27037) · UniProt [Q8IZ69](https://www.uniprot.org/uniprotkb/Q8IZ69) · Ensembl [ENSG00000099899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099899)

## Data

Gene col 1825: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1825); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1825, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1825]; `tensor/DDL_lfc|DDL_z.npy` [1825]; `embed/gene_vectors.npy` [1825]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1825 or target_col == 1825). Every well: [[TRMT2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
