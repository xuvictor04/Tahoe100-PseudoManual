---
symbol: "SRRM5"
type: "gene"
col: 13554
ensembl_id: "ENSG00000226763"
name: "serine/arginine repetitive matrix 5"
location: "19q13.31"
module: 38
arm: "+"
pooled_cpm: 3.85
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# SRRM5

*serine/arginine repetitive matrix 5* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +10.7, q 8e-24, up in 26 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.565× (z -6.3, q 2e-07, down in 18 of 31 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Naproxen (drug)]] 5 µM in 1 line (J82 0.0756×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (PANC-1 0.0886×; ⚠ toxic); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (J82 0.0972×); [[Belumosudil (drug)]] 5 µM in 1 line (HEC-1-A 0.164×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP2A1]] (+0.79, fdr 7e-06), [[ISY1-RAB43]] (+0.71, fdr 7e-06), [[MYO15A]] (+0.70, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13554.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +10.7 | 8e-24 | 26/37 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +8.1 | 1e-13 | 1/5 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +8.0 | 2e-13 | 18/37 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.33×** | +7.2 | 8e-11 | 26/40 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +5.8 | 8e-07 | 12/26 (NCI-H460, J82, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +5.1 | 4e-05 | 16/37 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +4.7 | 2e-04 | 12/45 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.4 | 8e-04 | 4/23 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +4.2 | 0.001 | 2/13 (HT-29, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.018 | 12/44 (NCI-H2030, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.36×** | +3.6 | 0.019 | 6/40 (COLO 205, NCI-H1792, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.031 | 15/39 (AsPC-1, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.064 | 8/37 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.065 | 2/43 (A-427, H4) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.084 | 4/45 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13554.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Naproxen (drug)]] 5 µM in 1 line (J82 0.0756×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (PANC-1 0.0886×; ⚠ toxic); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (J82 0.0972×); [[Belumosudil (drug)]] 5 µM in 1 line (HEC-1-A 0.164×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.565×** | -6.3 | 2e-07 | 18/31 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.741× | -3.3 | 0.28 | 13/43 (HEC-1-A, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13554. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 3.99 | 0 | 3 | — | [[Naproxen (drug)]] 5 µM 0.0756× (z -9.7) |
| [[A549 (line)]] | wt | 4.77 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0938× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[HEC-1-A (line)]] | alt | 6.45 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.164× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 4.36 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0917× (z -8.5) |
| [[PANC-1 (line)]] | alt | 1.87 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0886× (z -9.2) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 4.94 | 0 | 1 | — | [[ML264 (drug)]] 0.05 µM 0.0684× (z -8.6) |
| [[SW480 (line)]] | alt | 4.74 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0985× (z -8.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13554), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP2A1]] | +0.79 | +0.75 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ISY1-RAB43]] | +0.71 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.70 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[CHRNE]] | +0.69 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[RFPL3S]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[SYCE2]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[ARL9]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[SYCE1L]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[ZNF547]] | +0.66 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[NLGN3]] | +0.63 | +0.68 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.5, -19.5); signed map (12.6, 11.4). **Vector** length 51.2, 6.11% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +10.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.1 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +1.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.0 | -6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.4 | -2.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | serine/arginine repetitive matrix 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,596,617-43,614,498 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [B3KS81](https://www.uniprot.org/uniprotkb/B3KS81) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:37248](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37248) · Entrez [100170229](https://www.ncbi.nlm.nih.gov/gene/100170229) · UniProt [B3KS81](https://www.uniprot.org/uniprotkb/B3KS81) · Ensembl [ENSG00000226763](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226763)

## Data

Gene col 13554: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13554); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13554, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13554]; `tensor/DDL_lfc|DDL_z.npy` [13554]; `embed/gene_vectors.npy` [13554]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13554 or target_col == 13554). Every well: [[SRRM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRRM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
