---
symbol: "NAT9"
type: "gene"
col: 3021
ensembl_id: "ENSG00000109065"
name: "N-acetyltransferase 9"
location: "17q25.2"
module: 49
arm: "+"
pooled_cpm: 15.83
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# NAT9

*N-acetyltransferase 9* — 17q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.35× (z +5.3, q 5e-05, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.716× (z -5.7, q 7e-06, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKS3]] (+0.79, fdr 7e-06), [[ATG101]] (+0.75, fdr 7e-06), [[HM13]] (+0.75, fdr 7e-06); moves opposite to [[HNRNPK]] (-0.63, fdr 5e-05), [[HMGN2]] (-0.62, fdr 1e-05), [[EIF4G2]] (-0.60, fdr 3e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3021.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.35×** | +5.3 | 5e-05 | 29/48 (KATO III, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +5.1 | 9e-05 | 25/47 (SHP-77, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.006 | 20/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.010 | 18/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.56×** | +3.8 | 0.016 | 15/48 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +3.8 | 0.016 | 14/44 (SW480, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +3.7 | 0.018 | 13/34 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.7 | 0.018 | 15/42 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +3.6 | 0.021 | 19/44 (RKO, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +3.1 | 0.092 | 14/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.1 | 0.092 | 6/47 (C-33 A, NCI-H460, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.64×** | +3.1 | 0.098 | 8/46 (RPMI-7951, Hs 766T, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3021.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.716×** | -5.7 | 7e-06 | 28/47 (HS-578T, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.679×** | -4.5 | 0.002 | 20/46 (A549, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.725×** | -3.7 | 0.036 | 13/47 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.812×** | -3.5 | 0.056 | 14/48 (HS-578T, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.755×** | -3.4 | 0.070 | 13/48 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.749×** | -3.3 | 0.070 | 12/28 (A498, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -3.3 | 0.070 | 18/47 (A-172, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.599×** | -3.2 | 0.090 | 13/47 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.751×** | -3.2 | 0.090 | 13/47 (NCI-H23, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3021. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 13.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0981× (z -11.7) |
| [[A498 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -9.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 9.44 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.108× (z -9.3) ⚠ toxic |
| [[HS-578T (line)]] | alt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -12.3) |
| [[LoVo (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.251× (z -10.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[RKO (line)]] | wt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -8.8) |
| [[A-427 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3021), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKS3]] | +0.79 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[ATG101]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[HM13]] | +0.75 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[BET1L]] | +0.75 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[SNU13]] | +0.74 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[SSR2]] | +0.74 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[TMEM208]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[TMEM120B]] | +0.70 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[DPH7]] | +0.70 | +0.69 / +0.57 | both halves | 1e-05 | STRING 452 |
| [[DHDDS]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[PDIA5]] | +0.69 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[UTP6]] | +0.69 | +0.75 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.63 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[HMGN2]] | -0.62 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.60 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[SCRN1]] | -0.59 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ATF7IP]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.6, -32.0); signed map (-49.0, 6.5). **Vector** length 85.7, 19.0% of its response variance represented; |z| ≥ 3 in 652 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.54 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +5.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.8 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.0 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -5.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | N-acetyltransferase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.2 — chr17:74,770,529-74,776,367 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564C103 |
| Gene groups (HGNC) | GCN5 related N-acetyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTE0](https://www.uniprot.org/uniprotkb/Q9BTE0) (Alpha/beta-tubulin-N-acetyltransferase 9):

> N-acetyltransferase that mediates the acetylation of the N-terminal residues of alpha- and beta-tubulin.

**Summary**, from NCBI Gene [26151](https://www.ncbi.nlm.nih.gov/gene/26151):

> Predicted to enable tubulin N-terminal-methionine acetyltransferase activity. Predicted to be involved in regulation of mitotic spindle assembly. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23133](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23133) · Entrez [26151](https://www.ncbi.nlm.nih.gov/gene/26151) · UniProt [Q9BTE0](https://www.uniprot.org/uniprotkb/Q9BTE0) · Ensembl [ENSG00000109065](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109065)

## Data

Gene col 3021: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3021); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3021, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3021]; `tensor/DDL_lfc|DDL_z.npy` [3021]; `embed/gene_vectors.npy` [3021]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3021 or target_col == 3021). Every well: [[NAT9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAT9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
