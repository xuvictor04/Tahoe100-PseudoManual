---
symbol: "SNRPE"
type: "gene"
col: 11231
ensembl_id: "ENSG00000182004"
name: "small nuclear ribonucleoprotein polypeptide E"
location: "1q32.1"
module: 4
arm: "+"
pooled_cpm: 28.75
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SNRPE

*small nuclear ribonucleoprotein polypeptide E* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.25× (z +8.5, q 1e-14, up in 35 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.09× (z +7.5, q 2e-11, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.233×, C-33 A 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.210×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.218×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRPD1]] (+0.77, fdr 7e-06), [[TRMT10C]] (+0.71, fdr 7e-06), [[LCLAT1]] (+0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11231.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.25×** | +8.5 | 1e-14 | 35/45 (NCI-H23, A-172, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.09×** | +7.5 | 2e-11 | 40/48 (PANC-1, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.71×** | +5.7 | 2e-06 | 26/37 (A549, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.43×** | +4.7 | 3e-04 | 29/46 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.7 | 3e-04 | 29/46 (RKO, Hs 766T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.52×** | +4.6 | 4e-04 | 30/46 (NCI-H2347, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.51×** | +4.2 | 0.002 | 26/43 (HT-29, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.42×** | +3.7 | 0.018 | 24/48 (NCI-H1792, LOX-IMVI, …) | all doses, flat |  |
| [[Arbutin (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.021 | 26/46 (BT-474, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | 1.22× | +3.1 | 0.11 | 17/48 (C32, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.35× | +3.1 | 0.11 | 19/46 (C32, NCI-H460, …) | all doses, flat | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11231.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.233×, C-33 A 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.210×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.218×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.734× | -3.2 | 0.67 | 19/47 (A-172, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11231. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 33.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 33.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.78× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -11.1) |
| [[A-172 (line)]] | wt | 28.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A498 (line)]] | wt | 34.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A549 (line)]] | wt | 26.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[AN3 CA (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.111× (z -9.2) ⚠ toxic |
| [[C-33 A (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[NCI-H1792 (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 34.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[RKO (line)]] | wt | 40.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 29.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 34.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11231), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPD1]] | +0.77 | +0.77 / +0.73 | both halves | 7e-06 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 999 |
| [[TRMT10C]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[LCLAT1]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[COA4]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[ZNF551]] | +0.65 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[PRPF4]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 999 |
| [[AAR2]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 | STRING 775 |
| [[NARS2]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[CLYBL]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[COA1]] | +0.63 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[VTA1]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-17.6, -42.3); signed map (-9.6, -48.5). **Vector** length 64.9, 14.7% of its response variance represented; |z| ≥ 3 in 634 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +4.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +4.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.2 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +3.1 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.9 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.8 | +2.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein polypeptide E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:203,861,599-203,871,152 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Sm-E |
| Gene groups (HGNC) | Sm spliceosomal proteins |
| Reactome | 24 pathways, smallest: SLBP independent Processing of Histone Pre-mRNAs; SLBP Dependent Processing of Replication-Dependent Histone Pre-mRNAs; Processing of Capped Intronless Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P62304](https://www.uniprot.org/uniprotkb/P62304) (Small nuclear ribonucleoprotein E):

> Plays a role in pre-mRNA splicing as a core component of the spliceosomal U1, U2, U4 and U5 small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome. Component of both the pre-catalytic spliceosome B complex and activated spliceosome C complexes. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs. As part of the U7 snRNP it is involved in histone 3'-end processing.

**Summary**, from NCBI Gene [6635](https://www.ncbi.nlm.nih.gov/gene/6635):

> The protein encoded by this gene is a core component of U small nuclear ribonucleoproteins, which are key components of the pre-mRNA processing spliceosome. The encoded protein plays a role in the 3' end processing of histone transcripts. This protein is one of the targets in the autoimmune disease systemic lupus erythematosus, and mutations in this gene have been associated with hypotrichosis. Several pseudogenes of this gene have been identified. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:11161](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11161) · Entrez [6635](https://www.ncbi.nlm.nih.gov/gene/6635) · UniProt [P62304](https://www.uniprot.org/uniprotkb/P62304) · Ensembl [ENSG00000182004](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182004)

## Data

Gene col 11231: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11231); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11231, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11231]; `tensor/DDL_lfc|DDL_z.npy` [11231]; `embed/gene_vectors.npy` [11231]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11231 or target_col == 11231). Every well: [[SNRPE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRPE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
