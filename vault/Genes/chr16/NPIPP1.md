---
symbol: "NPIPP1"
type: "gene"
col: 12028
ensembl_id: "ENSG00000188599"
name: "nuclear pore complex interacting protein pseudogene 1"
location: "16p13.11"
module: 29
arm: "-"
pooled_cpm: 7.1
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# NPIPP1

*nuclear pore complex interacting protein pseudogene 1* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.67× (z +5.8, q 4e-06, up in 22 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.556× (z -6.6, q 2e-08, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATF4]] (+0.74, fdr 7e-06), [[NPIPA1]] (+0.69, fdr 7e-06), [[WASHC1]] (+0.67, fdr 7e-06); moves opposite to [[BANF1]] (-0.64, fdr 1e-05), [[PPT1]] (-0.64, fdr 1e-05), [[PPP2R1B]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12028.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +5.8 | 4e-06 | 22/42 (HEC-1-A, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.63×** | +5.5 | 1e-05 | 19/45 (HS-578T, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.2 | 4e-05 | 15/41 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +4.7 | 3e-04 | 3/12 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.5 | 8e-04 | 9/29 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.045 | 15/46 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.088 | 6/36 (HepG2/C3A, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12028.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.556×** | -6.6 | 2e-08 | 26/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.329×** | -6.6 | 2e-08 | 28/46 (HCT15, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.605×** | -5.7 | 3e-06 | 22/45 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.406×** | -5.3 | 1e-05 | 19/41 (HCT15, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.638×** | -5.1 | 4e-05 | 21/45 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.739× | -3.2 | 0.15 | 7/45 (COLO 205, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12028. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 7.04 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0742× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0831× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0751× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 3.92 | 0 | 1 | — | [[Sacubitril_Valsartan (drug)]] 5 µM 0.0633× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 3.51 | 0 | 1 | — | [[Sinomenine (drug)]] 0.05 µM 0.0573× (z -9.1) |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[RPMI-7951 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0926× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 8.11 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0852× (z -9.4) |
| [[SW1417 (line)]] | alt | 5.94 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0592× (z -10.8) |
| [[A-172 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12028), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF4]] | +0.74 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[NPIPA1]] | +0.69 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.67 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[AK6]] | +0.62 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[EIF4EBP3]] | +0.62 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[FBXL6]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SNHG11]] | +0.60 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[FBXW5]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[BRD4]] | +0.56 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[NBPF10]] | +0.56 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[CDK3]] | +0.56 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[SNHG12]] | +0.55 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BANF1]] | -0.64 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[PPT1]] | -0.64 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[PPP2R1B]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SNRPG]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[PIGK]] | -0.58 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[PGAM1]] | -0.58 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[TMEM30A]] | -0.58 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[PARK7]] ⚠ | -0.58 | -0.46 / -0.44 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[VMA21]] | -0.57 | -0.38 / -0.59 | both halves | 6e-05 |  |
| [[MRPL42]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[COPS7B]] | -0.56 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[CIPC]] | -0.56 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[FKBP1A]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-37.9, -29.9); signed map (1.4, -11.5). **Vector** length 54.9, 7.36% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.5 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +5.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.0 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +1.8 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.3 | +0.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | -2.1 | +2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.7 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -5.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | nuclear pore complex interacting protein pseudogene 1 |
| Locus type | pseudogene |
| Location | 16p13.11 — chr16:15,104,330-15,123,498 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | NPIPA4P |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:35407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35407) · Entrez [100874381](https://www.ncbi.nlm.nih.gov/gene/100874381) · Ensembl [ENSG00000188599](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188599)

## Data

Gene col 12028: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12028); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12028, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12028]; `tensor/DDL_lfc|DDL_z.npy` [12028]; `embed/gene_vectors.npy` [12028]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12028 or target_col == 12028). Every well: [[NPIPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPIPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
