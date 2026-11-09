---
symbol: "TMEM259"
type: "gene"
col: 11236
ensembl_id: "ENSG00000182087"
name: "transmembrane protein 259"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 28.27
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TMEM259

*transmembrane protein 259* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.43× (z +10.6, q 2e-23, up in 40 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.66× (z +6.0, q 3e-07, up in 38 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.389×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP2K2]] (+0.74, fdr 7e-06), [[PGGHG]] (+0.69, fdr 7e-06), [[GDI1]] (+0.65, fdr 8e-06); moves opposite to [[AASDHPPT]] (-0.55, fdr 3e-05), [[EBAG9]] (-0.54, fdr 7e-05), [[THNSL1]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11236.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +10.6 | 2e-23 | 40/43 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +10.2 | 5e-22 | 32/36 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +6.0 | 3e-07 | 38/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +5.2 | 3e-05 | 35/47 (NCI-H2030, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.54×** | +5.1 | 3e-05 | 35/47 (LoVo, LS 180, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +4.9 | 1e-04 | 31/40 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +4.3 | 0.001 | 31/48 (HEC-1-A, A498, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.003 | 23/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +4.1 | 0.003 | 28/46 (AsPC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.7 | 0.012 | 20/38 (SW480, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.013 | 24/48 (SW480, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.048 | 19/48 (NCI-H2030, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.67×** | +3.1 | 0.092 | 11/48 (A-172, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11236.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.389×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.721× | -3.1 | 0.35 | 15/48 (SW 900, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.775× | -3.1 | 0.35 | 12/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bestatin (hydrochloride) (drug)]] 5 µM |  | 0.776× | -3.1 | 0.35 | 10/48 (HepG2/C3A, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.0 | 0.35 | 18/47 (NCI-H661, SNU-1, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11236. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 27.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +8.7) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.389× (z -8.7) |
| [[A498 (line)]] | wt | 34.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 36.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +8.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 120 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11236), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP2K2]] | +0.74 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[PGGHG]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[GDI1]] | +0.65 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[UCKL1]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PLA2G4B]] | +0.62 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[PNPLA6]] | +0.61 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[B4GALT3]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[SBF1]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[LENG8]] | +0.61 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[AP2A1]] | +0.60 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[TCIRG1]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AASDHPPT]] | -0.55 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[EBAG9]] | -0.54 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[THNSL1]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ASNSD1]] | -0.50 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[METTL18]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ZBED9]] | -0.50 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[DMAC1]] | -0.50 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[GIN1]] | -0.49 | -0.42 / -0.37 | both halves | 9e-05 |  |
| [[CFAP97]] | -0.49 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.4, -22.9); signed map (-28.0, 0.1). **Vector** length 72.4, 17.1% of its response variance represented; |z| ≥ 3 in 477 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.0 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.5 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +1.4 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.9 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 259 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,009,648-1,021,179 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4022, ASBABP1, MBRL; previously C19orf6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4ZIN3](https://www.uniprot.org/uniprotkb/Q4ZIN3) (Membralin):

> May have a role in the ERAD pathway required for clearance of misfolded proteins in the endoplasmic reticulum (ER). Promotes survival of motor neurons, probably by protecting against ER stress.

**Summary**, from NCBI Gene [91304](https://www.ncbi.nlm.nih.gov/gene/91304):

> Predicted to be involved in positive regulation of ERAD pathway and response to endoplasmic reticulum stress. Predicted to be located in endoplasmic reticulum membrane. Predicted to be active in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17039](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17039) · Entrez [91304](https://www.ncbi.nlm.nih.gov/gene/91304) · UniProt [Q4ZIN3](https://www.uniprot.org/uniprotkb/Q4ZIN3) · Ensembl [ENSG00000182087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182087)

## Data

Gene col 11236: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11236); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11236, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11236]; `tensor/DDL_lfc|DDL_z.npy` [11236]; `embed/gene_vectors.npy` [11236]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11236 or target_col == 11236). Every well: [[TMEM259 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM259.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
