---
symbol: "EVI2B"
type: "gene"
col: 11742
ensembl_id: "ENSG00000185862"
name: "ecotropic viral integration site 2B"
location: "17q11.2"
module: 21
arm: "+"
pooled_cpm: 2.02
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# EVI2B

*ecotropic viral integration site 2B* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.97× (z +9.7, q 2e-19, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.65× (z +6.6, q 1e-08, up in 13 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.824× (z -6.4, q 9e-08, down in 25 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Trametinib (drug)]] 5 µM: 0.659× (z -4.1, q 0.013, down in 14 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (J82 0.0470×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGF2BP2-AS1]] (+0.68, fdr 1e-05), [[INSYN2A]] (+0.67, fdr 1e-05), [[OMG]] (+0.65, fdr 3e-05, ⚠ same locus), [[TEX11]] (+0.64, fdr 3e-05); moves opposite to [[ECHS1]] (-0.54, fdr 1e-04), [[CS]] (-0.52, fdr 2e-04).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11742.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.97×** | +9.7 | 2e-19 | 2/3 (J82, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +9.1 | 4e-17 | 5/10 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.6 | 1e-08 | 13/27 (HS-578T, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +5.5 | 6e-06 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +5.0 | 7e-05 | 3/9 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.5 | 6e-04 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +3.7 | 0.017 | 1/2 (HOP62) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.11×** | +3.6 | 0.022 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.070 | 3/26 (SW480, A-427, …) | top dose only |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.41× | +3.1 | 0.12 | 2/18 (NCI-H1792, A498) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11742.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (J82 0.0470×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.824×** | -6.4 | 9e-08 | 25/47 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.659×** | -4.1 | 0.013 | 14/45 (HOP62, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.660×** | -3.6 | 0.072 | 11/44 (SK-MEL-2, SW 1271, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.696× | -3.1 | 0.28 | 2/43 (A498, NCI-H23) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11742. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 4.72 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0470× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11742), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGF2BP2-AS1]] | +0.68 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[INSYN2A]] | +0.67 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[OMG]] | +0.65 | +0.45 / +0.59 | both halves | 3e-05 | STRING 860; ⚠ same locus (6.2 kb, same strand: neighbours can correlate without regulation) |
| [[TEX11]] | +0.64 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[A2ML1-AS1]] | +0.63 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[SORCS3]] | +0.61 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[PRKCA-AS1]] | +0.61 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[HPSE2]] | +0.61 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[AKAP13-AS1]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[BIRC6-AS2-1]] | +0.61 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[VPS39-DT]] | +0.61 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[ADGRL4]] | +0.60 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[PLCG1-AS1]] | +0.60 | +0.46 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECHS1]] | -0.54 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[CS]] | -0.52 | -0.30 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.2, 29.3); signed map (32.3, 9.3). **Vector** length 30.0, 2.38% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +0.8 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | +1.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -1.5 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -6.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ecotropic viral integration site 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:31,303,770-31,314,105 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D17S376, EVDB, CD361 |
| Gene groups (HGNC) | CD molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P34910](https://www.uniprot.org/uniprotkb/P34910) (Protein EVI2B):

> Required for granulocyte differentiation and functionality of hematopoietic progenitor cells through the control of cell cycle progression and survival of hematopoietic progenitor cells.

**Summary**, from NCBI Gene [2124](https://www.ncbi.nlm.nih.gov/gene/2124):

> Involved in positive regulation of granulocyte differentiation. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3500](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3500) · Entrez [2124](https://www.ncbi.nlm.nih.gov/gene/2124) · UniProt [P34910](https://www.uniprot.org/uniprotkb/P34910) · Ensembl [ENSG00000185862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185862)

## Data

Gene col 11742: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11742); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11742, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11742]; `tensor/DDL_lfc|DDL_z.npy` [11742]; `embed/gene_vectors.npy` [11742]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11742 or target_col == 11742). Every well: [[EVI2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EVI2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
