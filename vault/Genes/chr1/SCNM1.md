---
symbol: "SCNM1"
type: "gene"
col: 8645
ensembl_id: "ENSG00000163156"
name: "sodium channel modifier 1"
location: "1q21.3"
module: 118
arm: "+"
pooled_cpm: 17.85
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# SCNM1

*sodium channel modifier 1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.79× (z +6.9, q 4e-09, up in 31 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.59× (z +5.6, q 5e-06, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.703× (z -4.3, q 0.008, down in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ligustrazine (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0567×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 0.127×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.179×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SW 900 0.253×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNHIT3]] (+0.73, fdr 7e-06), [[TMEM208]] (+0.73, fdr 7e-06), [[TMEM11]] (+0.73, fdr 7e-06); moves opposite to [[NPIPB4]] (-0.58, fdr 3e-05), [[CBX5]] (-0.58, fdr 4e-05), [[SFPQ]] (-0.58, fdr 4e-04).
> It sits in the **+** arm of [[Module 118]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8645.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +6.9 | 4e-09 | 31/42 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +5.6 | 5e-06 | 28/47 (A-427, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.6 | 5e-06 | 29/46 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +5.3 | 2e-05 | 29/48 (NCI-H2347, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.008 | 18/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.35×** | +3.7 | 0.025 | 18/44 (Hs 766T, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.31×** | +3.3 | 0.068 | 13/47 (KATO III, SHP-77, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.095 | 12/47 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.41× | +3.0 | 0.15 | 12/44 (SHP-77, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8645.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ligustrazine (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0567×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 0.127×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.179×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SW 900 0.253×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.703×** | -4.3 | 0.008 | 21/47 (SW 900, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.726×** | -3.9 | 0.024 | 23/46 (CFPAC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.827× | -3.3 | 0.17 | 17/48 (LS 180, NCI-H2347, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.775× | -3.1 | 0.24 | 18/48 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.779× | -3.1 | 0.24 | 16/46 (NCI-H2347, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8645. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 1 | — | [[Ligustrazine (drug)]] 5 µM 0.0567× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 13.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.179× (z -10.1) |
| [[SW 900 (line)]] | alt | 29.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.253× (z -8.8) |
| [[A-427 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8645), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNHIT3]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[TMEM208]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[TMEM11]] | +0.73 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[MRPL55]] | +0.72 | +0.65 / +0.80 | both halves | 7e-06 |  |
| [[DRG1]] | +0.70 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[C1orf35]] | +0.70 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[CWC15]] | +0.70 | +0.68 / +0.73 | both halves | 7e-06 | STRING 818 |
| [[MTF1]] | +0.70 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[EIF4E2]] | +0.69 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[TFIP11]] | +0.69 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[MAPKAPK5-AS1]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[C16orf91]] | +0.69 | +0.53 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPB4]] | -0.58 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[CBX5]] | -0.58 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[SFPQ]] | -0.58 | -0.25 / -0.67 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.655). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-41.5, -8.7); signed map (-12.1, -9.9). **Vector** length 82.3, 17.9% of its response variance represented; |z| ≥ 3 in 636 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.7 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +6.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +0.6 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.9 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.7 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Esmolol (hydrochloride) (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | sodium channel modifier 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,156,664-151,170,296 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3180 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWG6](https://www.uniprot.org/uniprotkb/Q9BWG6) (Sodium channel modifier 1):

> As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs. Plays a role in the regulation of primary cilia length and Hedgehog signaling.

**Summary**, from NCBI Gene [79005](https://www.ncbi.nlm.nih.gov/gene/79005):

> SCNM1 is a zinc finger protein and putative splicing factor. In mice, Scnm1 modifies phenotypic expression of Scn8a (MIM 600702) mutations (Buchner et al., 2003 [PubMed 12920299]).[supplied by OMIM, Oct 2009]

**Accessions** — [HGNC:23136](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23136) · Entrez [79005](https://www.ncbi.nlm.nih.gov/gene/79005) · UniProt [Q9BWG6](https://www.uniprot.org/uniprotkb/Q9BWG6) · Ensembl [ENSG00000163156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163156)

## Data

Gene col 8645: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8645); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8645, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8645]; `tensor/DDL_lfc|DDL_z.npy` [8645]; `embed/gene_vectors.npy` [8645]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8645 or target_col == 8645). Every well: [[SCNM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCNM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
