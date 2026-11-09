---
symbol: "SMG1P1"
type: "gene"
col: 14124
ensembl_id: "ENSG00000237296"
name: "SMG1 pseudogene 1"
location: "16p12.2"
module: 20
arm: "+"
pooled_cpm: 5.49
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SMG1P1

*SMG1 pseudogene 1* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.23× (z +7.4, q 9e-11, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 0.622× (z -4.4, q 0.007, down in 22 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Busulfan (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0721×); [[Trifluridine (drug)]] 0.5 µM in 1 line (A-427 0.0770×; ⚠ cell-cycle shift, explains ~20% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMG1P3]] (+0.69, fdr 7e-06), [[RPS3A]] (+0.68, fdr 7e-06), [[CTC1]] (+0.67, fdr 7e-06); moves opposite to [[MRFAP1]] (-0.62, fdr 8e-06), [[CEP350]] (-0.60, fdr 1e-05), [[FAM32A]] (-0.60, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14124.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.23×** | +7.4 | 9e-11 | 33/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +7.3 | 9e-11 | 26/40 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +6.0 | 4e-07 | 21/34 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.91×** | +5.9 | 4e-07 | 25/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.14×** | +5.5 | 4e-06 | 18/43 (PANC-1, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.79×** | +5.3 | 9e-06 | 23/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.60×** | +4.6 | 4e-04 | 15/39 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.004 | 17/41 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.19×** | +3.8 | 0.010 | 7/13 (NCI-H1573, A549, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.011 | 12/46 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +3.6 | 0.020 | 7/18 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.033 | 12/45 (SK-MEL-2, Hs 766T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.43×** | +3.1 | 0.091 | 6/43 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.39×** | +3.0 | 0.098 | 10/45 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14124.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Busulfan (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0721×); [[Trifluridine (drug)]] 0.5 µM in 1 line (A-427 0.0770×; ⚠ cell-cycle shift, explains ~20% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.622×** | -4.4 | 0.007 | 22/41 (RKO, NCI-H1792, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[SBI-0640756 (drug)]] 0.05 µM |  | 0.681× | -3.3 | 0.17 | 10/46 (MIA PaCa-2, HCT15, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.697× | -3.3 | 0.17 | 9/46 (A498, NCI-H661, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.711× | -3.1 | 0.24 | 10/46 (NCI-H2030, A-172, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14124. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 3.81 | 0 | 1 (1 ⚠) | — | [[Trifluridine (drug)]] 0.5 µM 0.0770× (z -8.5) ⚠ cell-cycle shift, explains ~20% of this change |
| [[Panc 03.27 (line)]] | alt | 4.70 | 0 | 1 | — | [[Busulfan (drug)]] 0.05 µM 0.0721× (z -8.7) |
| [[A-172 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14124), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P3]] | +0.69 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[RPS3A]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[CTC1]] | +0.67 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[RPS10-NUDT3]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[RPL6]] | +0.59 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[NPEPPSP1]] | +0.59 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[OTUD6B]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CPSF6]] | +0.58 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MAT2A]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[RPSA]] | +0.57 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[ANKRD10]] | +0.57 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[SMG1P5]] | +0.56 | +0.69 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRFAP1]] | -0.62 | -0.66 / -0.58 | both halves | 8e-06 |  |
| [[CEP350]] | -0.60 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[FAM32A]] | -0.60 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[FAF2]] | -0.60 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[MFAP1]] | -0.59 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[METTL23]] | -0.59 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[PPP1R12A]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[TRIP11]] | -0.58 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[CWC22]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[CEBPZ]] | -0.57 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[SON]] | -0.57 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[LENG1]] | -0.56 | -0.47 / -0.66 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.548). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.5, -26.5); signed map (-26.3, -34.0). **Vector** length 44.4, 4.99% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.53 to 10); *Peptide chain elongation* (reactome, mean cos +0.53 to 9); *Influenza Viral RNA Transcription and Replication* (reactome, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +3.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.9 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.5 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.5 | -1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.0 | +2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +0.9 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | -1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.8 | -0.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +0.7 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.7 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.0 | -1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.9 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | SMG1 pseudogene 1 |
| Locus type | pseudogene |
| Location | 16p12.2 — chr16:22,437,401-22,491,826 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44186](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44186) · Entrez [641298](https://www.ncbi.nlm.nih.gov/gene/641298) · Ensembl [ENSG00000237296](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237296)

## Data

Gene col 14124: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14124); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14124, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14124]; `tensor/DDL_lfc|DDL_z.npy` [14124]; `embed/gene_vectors.npy` [14124]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14124 or target_col == 14124). Every well: [[SMG1P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMG1P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
