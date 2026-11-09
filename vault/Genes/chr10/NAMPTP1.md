---
symbol: "NAMPTP1"
type: "gene"
col: 13711
ensembl_id: "ENSG00000229644"
name: "nicotinamide phosphoribosyltransferase pseudogene 1"
location: "10p11.21"
module: 139
arm: "+"
pooled_cpm: 5.01
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# NAMPTP1

*nicotinamide phosphoribosyltransferase pseudogene 1* — 10p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.94× (z +6.4, q 1e-07, up in 22 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.800× (z -7.2, q 3e-10, down in 26 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.394× (z -4.6, q 0.001, down in 14 of 40 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAMPT]] (+0.66, fdr 1e-05), [[BIRC3]] (+0.55, fdr 1e-04), [[CEBPB]] (+0.54, fdr 1e-05); moves opposite to [[SMPD4BP]] (-0.52, fdr 2e-05), [[IQCK]] (-0.46, fdr 1e-04), [[SLC12A9]] (-0.46, fdr 4e-04).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13711.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +6.4 | 1e-07 | 22/45 (C32, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +5.0 | 2e-04 | 3/10 (NCI-H460, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +4.9 | 2e-04 | 17/41 (C32, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +4.7 | 4e-04 | 13/41 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.6 | 4e-04 | 14/46 (CFPAC-1, LS 180, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +4.4 | 0.001 | 2/14 (NCI-H1573, Hs 766T) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.007 | 18/37 (C32, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.048 | 9/47 (SW 900, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +3.2 | 0.085 | 5/21 (A549, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.1 | 0.096 | 7/42 (C32, A-172, …) | all doses, flat | position effect removed |
| [[Decitabine (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.096 | 5/42 (NCI-H23, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13711.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.800×** | -7.2 | 3e-10 | 26/47 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.394×** | -4.6 | 0.001 | 14/40 (SW 900, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.687×** | -3.5 | 0.063 | 13/37 (KATO III, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Gallic acid (drug)]] 5 µM |  | **0.768×** | -3.5 | 0.063 | 8/47 (SK-MEL-2, RKO, …) | top dose only | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **0.697×** | -3.4 | 0.076 | 9/31 (Hs 766T, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.727× | -3.0 | 0.21 | 10/46 (NCI-H460, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13711. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.228× (z -9.4) |
| [[A498 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.189× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 9.20 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.120× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 7.52 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0819× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 8.25 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0894× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13711), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAMPT]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[BIRC3]] | +0.55 | +0.36 / +0.61 | both halves | 1e-04 |  |
| [[CEBPB]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[FTH1]] | +0.54 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[SAA2-SAA4]] | +0.53 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[SAA2]] | +0.52 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[BCL6]] | +0.50 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[NCOA3]] | +0.50 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[SLC39A14]] | +0.48 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[FKBP5]] | +0.47 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[PLIN2]] | +0.46 | +0.42 / +0.39 | both halves | 5e-05 |  |
| [[MYO1B]] | +0.46 | +0.32 / +0.46 | both halves | 2e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMPD4BP]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[IQCK]] | -0.46 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[SLC12A9]] | -0.46 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[MAMDC2]] | -0.45 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[ALYREF]] | -0.44 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[P4HTM]] | -0.44 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[HOXB5]] | -0.44 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[SMPD4]] | -0.43 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[TNFSF12]] | -0.43 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[SNHG10]] | -0.43 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[ITGA9-AS1]] | -0.42 | -0.24 / -0.42 | both halves | 5e-04 |  |
| [[CEP43]] | -0.42 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.5, 16.6); signed map (16.7, 27.7). **Vector** length 55.8, 7.54% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.3 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.2 | +4.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +1.9 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.7 | +2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.3 | +1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.9 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -4.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.4 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | nicotinamide phosphoribosyltransferase pseudogene 1 |
| Locus type | pseudogene |
| Location | 10p11.21 — chr10:36,521,721-36,524,234 (-) |
| Ensembl biotype | processed_pseudogene |
| Also known as | bA92J19.4; previously PBEF2, NAMPTL |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:17633](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17633) · Entrez [646309](https://www.ncbi.nlm.nih.gov/gene/646309) · Ensembl [ENSG00000229644](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229644)

## Data

Gene col 13711: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13711); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13711, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13711]; `tensor/DDL_lfc|DDL_z.npy` [13711]; `embed/gene_vectors.npy` [13711]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13711 or target_col == 13711). Every well: [[NAMPTP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAMPTP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
