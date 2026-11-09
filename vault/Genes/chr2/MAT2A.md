---
symbol: "MAT2A"
type: "gene"
col: 9721
ensembl_id: "ENSG00000168906"
name: "methionine adenosyltransferase 2A"
location: "2p11.2"
module: 20
arm: "+"
pooled_cpm: 39.31
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# MAT2A

*methionine adenosyltransferase 2A* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 3.28× (z +9.0, q 2e-16, up in 43 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.263×, NCI-H23 0.392×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (RPMI-7951 0.0617×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.174×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPSA]] (+0.71, fdr 7e-06), [[HNRNPA3]] (+0.70, fdr 7e-06), [[SLC19A1]] (+0.70, fdr 7e-06); moves opposite to [[ZMYM5]] (-0.73, fdr 7e-06), [[MED19]] (-0.70, fdr 7e-06), [[NKAP]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9721.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.28×** | +9.0 | 2e-16 | 43/48 (SK-MEL-2, HOP62, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.06×** | +5.4 | 2e-05 | 36/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.82×** | +4.5 | 0.001 | 36/48 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +4.3 | 0.002 | 29/48 (HS-578T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.46×** | +3.5 | 0.044 | 33/47 (NCI-H1573, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +3.3 | 0.080 | 5/48 (SNU-1, C-33 A, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 1.52× | +3.1 | 0.13 | 21/48 (A-172, AsPC-1, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.58× | +3.1 | 0.13 | 25/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 1.54× | +3.0 | 0.16 | 25/47 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9721.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.263×, NCI-H23 0.392×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (RPMI-7951 0.0617×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.174×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | 0.634× | -3.5 | 0.29 | 23/48 (SW48, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 39.9 | 6 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 6.03× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 75.5 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -10.9) |
| [[HOP62 (line)]] | alt | 26.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.61× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 98.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0617× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 31.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.30× (z +9.6) | — |
| [[SW48 (line)]] | wt | 63.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -9.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SW480 (line)]] | alt | 57.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.42× (z +9.0) | — |
| [[A-172 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 66.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPSA]] | +0.71 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[HNRNPA3]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[SLC19A1]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[DHX15]] | +0.67 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[PFKM]] | +0.66 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[ARHGAP4]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[AHCY]] | +0.65 | +0.72 / +0.56 | both halves | 1e-05 | pathway: Biological oxidations; STRING 848 |
| [[PPT1]] | +0.65 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[APP]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SMG1P3]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[NUP210]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[VMA21]] | +0.62 | +0.48 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM5]] | -0.73 | -0.71 / -0.72 | both halves | 7e-06 |  |
| [[MED19]] | -0.70 | -0.62 / -0.70 | both halves | 7e-06 |  |
| [[NKAP]] | -0.69 | -0.65 / -0.71 | both halves | 7e-06 |  |
| [[SUMO4]] | -0.67 | -0.57 / -0.62 | both halves | 9e-06 |  |
| [[ING2]] | -0.65 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.65 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[PPP1R12A]] | -0.64 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[RBX1]] | -0.63 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[GPATCH1]] | -0.63 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[RSF1]] | -0.63 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[CEP350]] | -0.62 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.62 | -0.61 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.1, -28.0); signed map (-21.1, -43.9). **Vector** length 120, 38.4% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.50 to 10); *Peptide chain elongation* (reactome, mean cos +0.51 to 9); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.1 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.7 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.8 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +0.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.5 | +1.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.5 | -1.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -5.7 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -1.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.5 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | methionine adenosyltransferase 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:85,539,168-85,545,281 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAMS2, MATA2, MATII, MAT-II |
| Gene groups (HGNC) | Methionine adenosyltransferase family |
| Reactome | 3 pathways, smallest: Methylation; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [P31153](https://www.uniprot.org/uniprotkb/P31153) (S-adenosylmethionine synthase isoform type-2):

> Catalyzes the formation of S-adenosylmethionine from methionine and ATP. The reaction comprises two steps that are both catalyzed by the same enzyme: formation of S-adenosylmethionine (AdoMet) and triphosphate, and subsequent hydrolysis of the triphosphate.

**Summary**, from NCBI Gene [4144](https://www.ncbi.nlm.nih.gov/gene/4144):

> The protein encoded by this gene catalyzes the production of S-adenosylmethionine (AdoMet) from methionine and ATP. AdoMet is the key methyl donor in cellular processes. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:6904](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6904) · Entrez [4144](https://www.ncbi.nlm.nih.gov/gene/4144) · UniProt [P31153](https://www.uniprot.org/uniprotkb/P31153) · Ensembl [ENSG00000168906](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168906)

## Data

Gene col 9721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9721); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9721]; `tensor/DDL_lfc|DDL_z.npy` [9721]; `embed/gene_vectors.npy` [9721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9721 or target_col == 9721). Every well: [[MAT2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAT2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
