---
symbol: "LENG8"
type: "gene"
col: 9500
ensembl_id: "ENSG00000167615"
name: "leukocyte receptor cluster member 8"
location: "19q13.42"
module: 157
arm: "+"
pooled_cpm: 48.58
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# LENG8

*leukocyte receptor cluster member 8* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.16× (z +7.1, q 6e-10, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK5RAP3]] (+0.77, fdr 7e-06), [[RMRP]] (+0.72, fdr 1e-05), [[LY6G5B]] (+0.72, fdr 7e-06); moves opposite to [[PIGBOS1]] (-0.60, fdr 1e-05), [[MPLKIP]] (-0.59, fdr 1e-05), [[NDUFA7]] (-0.59, fdr 8e-05).
> It is in [[Module 157]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9500.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.16×** | +7.1 | 6e-10 | 45/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +5.3 | 3e-05 | 35/43 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.77×** | +5.3 | 3e-05 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +5.1 | 4e-05 | 30/39 (HT-29, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +4.9 | 1e-04 | 36/46 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.67×** | +4.7 | 2e-04 | 37/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.1 | 0.003 | 34/47 (PANC-1, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.17×** | +3.7 | 0.013 | 29/49 (RKO, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.049 | 27/48 (BT-474, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 1.40× | +3.1 | 0.11 | 21/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9500.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | 0.718× | -3.1 | 0.58 | 28/47 (A549, SW480, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | 0.794× | -3.1 | 0.58 | 24/48 (SW1417, C32, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9500. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 35.8 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.48× (z +11.1) | — |
| [[SW480 (line)]] | alt | 60.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +9.7) | — |
| [[A-172 (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 75.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 74.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9500), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK5RAP3]] | +0.77 | +0.71 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[RMRP]] | +0.72 | +0.53 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[LY6G5B]] | +0.72 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[LINC03009]] | +0.71 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[CCNL2]] | +0.71 | +0.58 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[AKT2]] | +0.70 | +0.57 / +0.76 | both halves | 9e-06 | **novel candidate** |
| [[ABHD17A]] | +0.68 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[NRBP2]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[EME2]] | +0.67 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[HFM1]] | +0.66 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[WASH9P]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[RPL10]] | +0.65 | +0.59 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGBOS1]] | -0.60 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[MPLKIP]] | -0.59 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[NDUFA7]] | -0.59 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[MRPL36]] | -0.58 | -0.38 / -0.65 | both halves | 6e-05 |  |
| [[CEP350]] | -0.58 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[C1orf131]] | -0.57 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[FDX2]] | -0.54 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[EMC6]] | -0.54 | -0.27 / -0.65 | both halves | 3e-04 |  |
| [[MRPL46]] | -0.54 | -0.41 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.0, -24.5); signed map (-16.3, -32.6). **Vector** length 112, 34.3% of its response variance represented; |z| ≥ 3 in 637 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +11.8 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.7 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.1 | +4.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.8 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.3 | +1.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +3.6 | +2.9 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +3.2 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +0.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -0.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.0 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -3.6 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.2 | -1.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Thymol (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | leukocyte receptor cluster member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:54,449,190-54,462,016 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1932, MGC40108, pp13842 |
| Matched by | ensembl_id |

UniProt [Q96PV6](https://www.uniprot.org/uniprotkb/Q96PV6) carries no function annotation.

**Summary**, from NCBI Gene [114823](https://www.ncbi.nlm.nih.gov/gene/114823):

> Predicted to be part of protein-containing complex. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15500](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15500) · Entrez [114823](https://www.ncbi.nlm.nih.gov/gene/114823) · UniProt [Q96PV6](https://www.uniprot.org/uniprotkb/Q96PV6) · Ensembl [ENSG00000167615](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167615)

## Data

Gene col 9500: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9500); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9500, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9500]; `tensor/DDL_lfc|DDL_z.npy` [9500]; `embed/gene_vectors.npy` [9500]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9500 or target_col == 9500). Every well: [[LENG8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LENG8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
