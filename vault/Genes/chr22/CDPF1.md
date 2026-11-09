---
symbol: "CDPF1"
type: "gene"
col: 12999
ensembl_id: "ENSG00000205643"
name: "cysteine rich DPF motif domain containing 1"
location: "22q13.31"
module: 12
arm: "+"
pooled_cpm: 2.36
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CDPF1

*cysteine rich DPF motif domain containing 1* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.69× (z +4.8, q 1e-03, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 1.56× (z +3.9, q 0.010, up in 6 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.303× (z -11.3, q 7e-27, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDDC3]] (+0.68, fdr 1e-05), [[FANCF]] (+0.68, fdr 7e-06), [[ZNF74]] (+0.68, fdr 7e-06); moves opposite to [[FAM81A]] (-0.64, fdr 3e-05), [[PPP1R15B-AS1]] (-0.52, fdr 7e-05), [[CCNT2-AS1]] (-0.51, fdr 3e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12999.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +4.8 | 1e-03 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +4.6 | 1e-03 | 2/10 (PANC-1, HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.2 | 0.004 | 2/12 (KATO III, SNU-423) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.0 | 0.007 | 2/46 (SHP-77, LoVo) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.56×** | +3.9 | 0.010 | 6/28 (C32, HS-578T, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.021 | 1/44 (HOP62) | top dose only | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.63×** | +3.3 | 0.074 | 2/11 (NCI-H460, KATO III) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.39× | +3.1 | 0.13 | 6/22 (HEC-1-A, A549, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12999.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.303×** | -11.3 | 7e-27 | 38/46 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.438×** | -7.8 | 2e-12 | 12/20 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.456×** | -7.4 | 2e-11 | 24/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.514×** | -6.3 | 4e-08 | 22/41 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.685×** | -5.1 | 5e-05 | 20/34 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.592×** | -5.0 | 6e-05 | 15/45 (SW48, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.500×** | -3.4 | 0.047 | 11/28 (A549, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12999. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.37 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0552× (z -11.6) |
| [[HOP62 (line)]] | alt | 2.96 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0750× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 2.64 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0808× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 2.76 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0736× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 2.07 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0781× (z -13.5) |
| [[SNU-423 (line)]] | alt | 2.77 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -8.6) |
| [[A-172 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.994 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.884 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.978 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12999), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDDC3]] | +0.68 | +0.55 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[FANCF]] | +0.68 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ZNF74]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ZNF691]] | +0.66 | +0.69 / +0.64 | both halves | 7e-06 | STRING 485 |
| [[FAHD2B]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[ZNF287]] | +0.62 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[CPTP]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[RANBP2]] | +0.61 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[MRPS2]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[JMJD4]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[MYG1]] | +0.59 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[PTCD2]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM81A]] | -0.64 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[PPP1R15B-AS1]] | -0.52 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[CCNT2-AS1]] | -0.51 | -0.29 / -0.56 | both halves | 3e-04 |  |
| [[BCL2L14]] | -0.51 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[LINC01019]] | -0.50 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[PTMS]] | -0.49 | -0.34 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-45.0, -6.6); signed map (-4.0, -29.9). **Vector** length 35.4, 3.19% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.9 | +4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.3 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +1.2 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +3.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +0.8 | +2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.7 | +2.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -11.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -7.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.2 | -7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.7 | -1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | cysteine rich DPF motif domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:46,244,011-46,250,311 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDKN1A; previously C22orf40 |
| Matched by | ensembl_id |

UniProt [Q6NVV7](https://www.uniprot.org/uniprotkb/Q6NVV7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33710](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33710) · Entrez [150383](https://www.ncbi.nlm.nih.gov/gene/150383) · UniProt [Q6NVV7](https://www.uniprot.org/uniprotkb/Q6NVV7) · Ensembl [ENSG00000205643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205643)

## Data

Gene col 12999: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12999); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12999, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12999]; `tensor/DDL_lfc|DDL_z.npy` [12999]; `embed/gene_vectors.npy` [12999]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12999 or target_col == 12999). Every well: [[CDPF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDPF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
