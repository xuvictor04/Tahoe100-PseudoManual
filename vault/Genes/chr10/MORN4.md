---
symbol: "MORN4"
type: "gene"
col: 10064
ensembl_id: "ENSG00000171160"
name: "MORN repeat containing 4"
location: "10q24.2"
module: 198
arm: "+"
pooled_cpm: 5.74
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# MORN4

*MORN repeat containing 4* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.42× (z +8.5, q 7e-15, up in 21 of 28 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.54× (z +6.2, q 2e-07, up in 17 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 0.05 µM: 0.617× (z -4.6, q 0.002, down in 14 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RWDD3]] (+0.76, fdr 7e-06), [[TATDN3]] (+0.71, fdr 7e-06), [[MTO1]] (+0.71, fdr 7e-06); moves opposite to [[ZSWIM6]] (-0.62, fdr 7e-06), [[KPNA4]] (-0.58, fdr 2e-05), [[DIAPH1]] (-0.57, fdr 2e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10064.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +8.5 | 7e-15 | 21/28 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +6.2 | 2e-07 | 17/44 (NCI-H460, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.79×** | +5.8 | 1e-06 | 25/45 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.2 | 0.004 | 12/40 (SNU-423, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +3.7 | 0.021 | 8/17 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +3.6 | 0.023 | 6/22 (CFPAC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +3.6 | 0.023 | 2/9 (NCI-H2347, A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.074 | 7/44 (J82, A498, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.2 | 0.074 | 6/32 (A498, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Carbamazepine (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.074 | 7/43 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.074 | 4/45 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.074 | 9/35 (SW480, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.36×** | +3.1 | 0.084 | 8/40 (Panc 03.27, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10064.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **0.617×** | -4.6 | 0.002 | 14/43 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.446×** | -4.3 | 0.005 | 19/39 (PANC-1, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.706×** | -3.5 | 0.072 | 13/45 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Allantoin (drug)]] 5 µM |  | **0.789×** | -3.4 | 0.072 | 9/46 (HEC-1-A, A549, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.715×** | -3.4 | 0.072 | 15/44 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.728× | -3.2 | 0.11 | 11/45 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.740× | -3.1 | 0.17 | 14/45 (PANC-1, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10064. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 11.3 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.102× (z -9.5) |
| [[HOP62 (line)]] | alt | 6.69 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.134× (z -8.7) |
| [[HS-578T (line)]] | alt | 6.86 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -8.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[LOX-IMVI (line)]] | wt | 4.40 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0497× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 4.67 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0934× (z -8.5) |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -13.2) ⚠ cell-cycle shift, explains ~89% of this change |
| [[SW480 (line)]] | alt | 5.41 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0878× (z -9.4) ⚠ toxic |
| [[A-172 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10064), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RWDD3]] | +0.76 | +0.70 / +0.78 | both halves | 7e-06 |  |
| [[TATDN3]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[MTO1]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[ZNF594-DT]] | +0.65 | +0.58 / +0.72 | both halves | 8e-06 |  |
| [[ACTR10]] | +0.64 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[LAMTOR4]] | +0.63 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[MAPKAPK5-AS1]] | +0.63 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[NISCH]] | +0.63 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[B9D1]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[DYNC2LI1]] | +0.62 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[DCP1B]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[CDADC1]] | +0.62 | +0.58 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM6]] | -0.62 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[KPNA4]] | -0.58 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[DIAPH1]] | -0.57 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[SGMS2]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[TPM4]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[YWHAZ]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[MYLK2]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[VCL]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[ACTN1]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[BZW1]] | -0.53 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[TEAD1]] | -0.53 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[CHD4]] | -0.53 | -0.40 / -0.61 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction 0.746). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.2, 21.9); signed map (-15.4, -14.1). **Vector** length 63.5, 10.3% of its response variance represented; |z| ≥ 3 in 723 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +8.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.4 | +6.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +5.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.9 | +3.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.0 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -1.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -1.6 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -1.6 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | MORN repeat containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:97,614,553-97,633,500 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA548K23.4, FLJ25925, rtp; previously C10orf83 |
| Gene groups (HGNC) | MORN repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDC4](https://www.uniprot.org/uniprotkb/Q8NDC4) (MORN repeat-containing protein 4):

> Plays a role in promoting axonal degeneration following neuronal injury by toxic insult or trauma.

**Summary**, from NCBI Gene [118812](https://www.ncbi.nlm.nih.gov/gene/118812):

> Predicted to be involved in response to axon injury. Located in cytoplasm and filopodium tip. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24001) · Entrez [118812](https://www.ncbi.nlm.nih.gov/gene/118812) · UniProt [Q8NDC4](https://www.uniprot.org/uniprotkb/Q8NDC4) · Ensembl [ENSG00000171160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171160)

## Data

Gene col 10064: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10064); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10064, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10064]; `tensor/DDL_lfc|DDL_z.npy` [10064]; `embed/gene_vectors.npy` [10064]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10064 or target_col == 10064). Every well: [[MORN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MORN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
