---
symbol: "HINT2"
type: "gene"
col: 5972
ensembl_id: "ENSG00000137133"
name: "histidine triad nucleotide binding protein 2"
location: "9p13.3"
module: 58
arm: "+"
pooled_cpm: 5.71
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# HINT2

*histidine triad nucleotide binding protein 2* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.64× (z +11.0, q 3e-25, up in 26 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.40× (z +3.4, q 0.060, up in 15 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 6.96×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.556× (z -4.2, q 0.016, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WAC]] (+0.62, fdr 2e-05), [[BLOC1S1]] (+0.60, fdr 5e-05), [[NDUFA7]] (+0.59, fdr 1e-04); moves opposite to [[SEC14L1]] (-0.49, fdr 3e-04), [[ZNF587B]] (-0.48, fdr 2e-04), [[BRD9]] (-0.47, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5972.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 6.96×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.64×** | +11.0 | 3e-25 | 26/27 (A498, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.54×** | +10.4 | 8e-23 | 11/12 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **2.47×** | +6.4 | 2e-08 | 22/30 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.42×** | +5.8 | 8e-07 | 13/16 (A498, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.44×** | +3.7 | 0.023 | 12/47 (HOP62, HEC-1-A, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.060 | 15/39 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.086 | 8/45 (J82, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5972.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.556×** | -4.2 | 0.016 | 21/47 (AN3 CA, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.681×** | -3.9 | 0.029 | 22/38 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.590×** | -3.8 | 0.031 | 20/46 (LoVo, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.394×** | -3.5 | 0.072 | 16/36 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.639× | -3.2 | 0.13 | 17/46 (KATO III, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 0.640× | -3.2 | 0.13 | 15/45 (BT-474, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.649× | -3.1 | 0.16 | 16/47 (SK-MEL-2, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 6.02 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0528× (z -11.2) |
| [[A498 (line)]] | wt | 7.88 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.96× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 11 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WAC]] | +0.62 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[BLOC1S1]] | +0.60 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[NDUFA7]] | +0.59 | +0.35 / +0.69 | both halves | 1e-04 | STRING 411 |
| [[MRPL40]] | +0.59 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[FLVCR1-DT]] | +0.59 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[TMEM179B]] | +0.58 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[HDDC3]] | +0.58 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[NDUFAF3]] | +0.56 | +0.38 / +0.66 | both halves | 6e-05 |  |
| [[FAM104B]] | +0.56 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CDK5]] | +0.56 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[AKAP1-DT]] | +0.55 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[LAMTOR2]] | +0.54 | +0.30 / +0.66 | both halves | 2e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC14L1]] | -0.49 | -0.26 / -0.58 | both halves | 3e-04 |  |
| [[ZNF587B]] | -0.48 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[BRD9]] | -0.47 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[ZNF587]] | -0.47 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[CAPN15]] | -0.46 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[TPD52L2]] | -0.45 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[NPIPB11]] | -0.45 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[CDC37]] | -0.45 | -0.22 / -0.52 | both halves | 6e-04 |  |
| [[ZNF778]] | -0.45 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[GTPBP4]] | -0.44 | -0.29 / -0.42 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.520). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-48.8, -12.1); signed map (-21.3, -3.8). **Vector** length 45.4, 6.52% of its response variance represented; |z| ≥ 3 in 719 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.2 | +2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +1.8 | +11.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | histidine triad nucleotide binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,812,960-35,815,354 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Histidine triad superfamily |
| Reactome | 4 pathways, smallest: RHOD GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BX68](https://www.uniprot.org/uniprotkb/Q9BX68) (Adenosine 5'-monophosphoramidase HINT2):

> Exhibits adenosine 5'-monophosphoramidase activity, hydrolyzing purine nucleotide phosphoramidates with a single phosphate group such as adenosine 5'monophosphoramidate (AMP-NH2) to yield AMP and NH2. Hydrolyzes adenosine 5'-O-p-nitrophenylphosphoramidate (AMP-pNA). Hydrolyzes fluorogenic purine nucleoside tryptamine phosphoramidates in vitro. May be involved in steroid biosynthesis. May play a role in apoptosis.

**Summary**, from NCBI Gene [84681](https://www.ncbi.nlm.nih.gov/gene/84681):

> Histidine triad proteins, such as HINT2, are nucleotide hydrolases and transferases that act on the alpha-phosphate of ribonucleotides (Brenner, 2002 [PubMed 12119013]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18344](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18344) · Entrez [84681](https://www.ncbi.nlm.nih.gov/gene/84681) · UniProt [Q9BX68](https://www.uniprot.org/uniprotkb/Q9BX68) · Ensembl [ENSG00000137133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137133)

## Data

Gene col 5972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5972); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5972]; `tensor/DDL_lfc|DDL_z.npy` [5972]; `embed/gene_vectors.npy` [5972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5972 or target_col == 5972). Every well: [[HINT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HINT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
