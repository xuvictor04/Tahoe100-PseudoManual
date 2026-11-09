---
symbol: "IMP3"
type: "gene"
col: 10883
ensembl_id: "ENSG00000177971"
name: "IMP U3 small nucleolar ribonucleoprotein 3"
location: "15q24.2"
module: 54
arm: "+"
pooled_cpm: 21.42
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# IMP3

*IMP U3 small nucleolar ribonucleoprotein 3* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.17× (z +5.2, q 9e-05, up in 34 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +4.3, q 0.004, up in 31 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 0.259×, RKO 0.217×, C-33 A 0.226×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 0.193×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2H]] (+0.73, fdr 2e-05), [[NUDT22]] (+0.72, fdr 3e-05), [[NOG]] (+0.70, fdr 1e-05); moves opposite to [[DPY19L4]] (-0.68, fdr 3e-05), [[LIN7C]] (-0.66, fdr 3e-04), [[PAPOLA]] (-0.64, fdr 4e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10883.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +5.2 | 9e-05 | 34/43 (HT-29, KATO III, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.83×** | +4.3 | 0.004 | 28/44 (PANC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.3 | 0.004 | 31/47 (Hs 766T, HT-29, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 1.55× | +3.1 | 0.29 | 24/48 (SW480, SW1417, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10883.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 0.259×, RKO 0.217×, C-33 A 0.226×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 0.193×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.649× | -3.0 | 0.52 | 24/48 (Hs 766T, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10883. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -8.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 36.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -10.5) |
| [[RKO (line)]] | wt | 23.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -10.0) |
| [[A-427 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10883), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 10 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2H]] | +0.73 | +0.48 / +0.77 | both halves | 2e-05 | STRING 569 |
| [[NUDT22]] | +0.72 | +0.43 / +0.78 | both halves | 3e-05 |  |
| [[NOG]] | +0.70 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.69 | +0.37 / +0.77 | both halves | 8e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 855; ⚠ in the vector space only through flagged drug-doses |
| [[ADPRS]] | +0.69 | +0.48 / +0.74 | both halves | 2e-05 |  |
| [[C16orf91]] | +0.69 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[NCBP2AS2]] | +0.68 | +0.34 / +0.75 | both halves | 1e-04 |  |
| [[SCAND1]] | +0.68 | +0.41 / +0.78 | both halves | 4e-05 |  |
| [[EMC6]] | +0.68 | +0.27 / +0.78 | both halves | 3e-04 |  |
| [[SF3B5]] ⚠ | +0.68 | +0.35 / +0.77 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CCDC85B]] | +0.67 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[SLC25A4]] | +0.67 | +0.39 / +0.75 | both halves | 6e-05 |  |
| [[MINCR]] | +0.67 | +0.39 / +0.71 | both halves | 6e-05 |  |
| [[CHCHD1]] | +0.66 | +0.26 / +0.74 | both halves | 3e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L4]] | -0.68 | -0.43 / -0.71 | both halves | 3e-05 |  |
| [[LIN7C]] | -0.66 | -0.28 / -0.75 | both halves | 3e-04 |  |
| [[PAPOLA]] | -0.64 | -0.41 / -0.71 | both halves | 4e-05 |  |
| [[MOB1A]] | -0.64 | -0.44 / -0.70 | both halves | 3e-05 |  |
| [[UBQLN4]] | -0.64 | -0.50 / -0.66 | both halves | 1e-05 | STRING 451 |
| [[OCRL]] | -0.64 | -0.42 / -0.71 | both halves | 4e-05 |  |
| [[UBQLN1]] | -0.63 | -0.33 / -0.77 | both halves | 1e-04 | STRING 449 |
| [[DHFR]] | -0.63 | -0.17 / -0.74 | ⚠ one half (not replicated) | 0.001 |  |
| [[SGPL1]] | -0.62 | -0.42 / -0.67 | both halves | 4e-05 |  |
| [[LPGAT1]] | -0.62 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[CAPRIN1]] | -0.62 | -0.36 / -0.68 | both halves | 1e-04 |  |
| [[PSMD11]] | -0.62 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[NONO]] | -0.61 | -0.36 / -0.72 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-41.9, -18.9); signed map (-30.9, 11.1). **Vector** length 93.8, 30.2% of its response variance represented; |z| ≥ 3 in 460 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +2.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -11.9 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -11.4 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.6 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.5 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | IMP U3 small nucleolar ribonucleoprotein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:75,639,085-75,648,706 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10968, BRMS2; previously MRPS4, C15orf12 |
| Gene groups (HGNC) | MPP10 subcomplex |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NV31](https://www.uniprot.org/uniprotkb/Q9NV31) (U3 small nucleolar ribonucleoprotein protein IMP3):

> Component of the 60-80S U3 small nucleolar ribonucleoprotein (U3 snoRNP). Required for the early cleavages during pre-18S ribosomal RNA processing. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [55272](https://www.ncbi.nlm.nih.gov/gene/55272):

> This gene encodes the human homolog of the yeast Imp3 protein. The protein localizes to the nucleoli and interacts with the U3 snoRNP complex. The protein contains an S4 domain. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14497](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14497) · Entrez [55272](https://www.ncbi.nlm.nih.gov/gene/55272) · UniProt [Q9NV31](https://www.uniprot.org/uniprotkb/Q9NV31) · Ensembl [ENSG00000177971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177971)

## Data

Gene col 10883: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10883); `tables/drug_effects.parquet` (5 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10883, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10883]; `tensor/DDL_lfc|DDL_z.npy` [10883]; `embed/gene_vectors.npy` [10883]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10883 or target_col == 10883). Every well: [[IMP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IMP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
