---
symbol: "ZNHIT3"
type: "gene"
col: 15792
ensembl_id: "ENSG00000273611"
name: "zinc finger HIT-type containing 3"
location: "17q12"
module: 24
arm: "+"
pooled_cpm: 19.3
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 7
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ZNHIT3

*zinc finger HIT-type containing 3* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.61× (z +5.3, q 6e-05, up in 29 of 42 measured lines) ⚠ transcription drop.
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.490× (z -8.0, q 9e-13, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM23]] (+0.80, fdr 7e-06), [[MRPL43]] (+0.79, fdr 7e-06), [[MTIF3]] (+0.77, fdr 7e-06); moves opposite to [[SRSF1]] (-0.64, fdr 1e-04), [[NUP188]] (-0.62, fdr 1e-05), [[MAPRE1]] (-0.61, fdr 7e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15792.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +5.3 | 6e-05 | 29/42 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.67× | +3.1 | 0.53 | 12/46 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15792.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.490×** | -8.0 | 9e-13 | 42/48 (LOX-IMVI, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.519×** | -7.3 | 7e-11 | 40/47 (H4, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.587×** | -5.9 | 6e-07 | 30/47 (KATO III, SW1417, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.622×** | -5.3 | 2e-05 | 31/47 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -5.2 | 2e-05 | 31/46 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.754×** | -4.4 | 9e-04 | 22/47 (SNU-423, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.739×** | -3.4 | 0.062 | 19/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15792. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 24.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.5) |
| [[H4 (line)]] | wt | 15.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0590× (z -11.4) |
| [[KATO III (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 25.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SK-MEL-2 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.327× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15792), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM23]] | +0.80 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[MRPL43]] | +0.79 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.77 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.74 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[SCNM1]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[RPP21]] | +0.73 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[CGRRF1]] | +0.73 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[MRPL55]] | +0.73 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[CIR1]] | +0.72 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[RNF113A]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.72 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[HEATR5B]] | +0.71 | +0.65 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF1]] | -0.64 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[NUP188]] | -0.62 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.61 | -0.38 / -0.68 | both halves | 7e-05 |  |
| [[HNRNPA2B1]] | -0.61 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[EIF5A]] | -0.60 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[PSME3]] | -0.60 | -0.47 / -0.62 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-38.7, -12.3); signed map (-16.1, -5.3). **Vector** length 79.4, 18.2% of its response variance represented; |z| ≥ 3 in 538 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -5.3 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.2 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | +2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.5 | -8.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger HIT-type containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:36,486,629-36,499,310 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hit1; previously TRIP3 |
| Gene groups (HGNC) | Zinc fingers HIT-type |
| Matched by | ensembl_id |

UniProt [Q15649](https://www.uniprot.org/uniprotkb/Q15649) carries no function annotation.

**Summary**, from NCBI Gene [9326](https://www.ncbi.nlm.nih.gov/gene/9326):

> Predicted to enable nuclear thyroid hormone receptor binding activity. Predicted to be involved in box C/D snoRNP assembly and maturation of LSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Located in cytoplasm and nucleus. Implicated in PEHO syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12309) · Entrez [9326](https://www.ncbi.nlm.nih.gov/gene/9326) · UniProt [Q15649](https://www.uniprot.org/uniprotkb/Q15649) · Ensembl [ENSG00000273611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273611)

## Data

Gene col 15792: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15792); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15792, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15792]; `tensor/DDL_lfc|DDL_z.npy` [15792]; `embed/gene_vectors.npy` [15792]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15792 or target_col == 15792). Every well: [[ZNHIT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNHIT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
