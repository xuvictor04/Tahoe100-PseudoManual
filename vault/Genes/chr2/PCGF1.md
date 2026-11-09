---
symbol: "PCGF1"
type: "gene"
col: 3652
ensembl_id: "ENSG00000115289"
name: "polycomb group ring finger 1"
location: "2p13.1"
module: 24
arm: "+"
pooled_cpm: 8.39
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# PCGF1

*polycomb group ring finger 1* — 2p13.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.73× (z +4.4, q 0.005, up in 22 of 38 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.0874×, SW 900 0.132×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2030 0.123×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (CFPAC-1 0.136×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Elagolix sodium (drug)]] 0.05 µM in 1 line (SNU-1 0.0649×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HS-578T 0.0894×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM26]] (+0.78, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[C1orf35]] (+0.75, fdr 7e-06), [[SNHG7]] (+0.74, fdr 1e-05), [[LEO1]] (+0.74, fdr 7e-06); moves opposite to [[MOB1A]] (-0.63, fdr 3e-05), [[GNG12]] (-0.63, fdr 7e-05), [[ACTR2]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3652.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.73×** | +4.4 | 0.005 | 22/38 (Panc 03.27, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +4.2 | 0.008 | 11/48 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.64×** | +4.0 | 0.011 | 19/43 (NCI-H1573, LS 180, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.9 | 0.013 | 23/38 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.59×** | +3.7 | 0.020 | 19/45 (LoVo, PANC-1, …) | top dose only | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.3 | 0.078 | 16/43 (NCI-H23, C32, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.76× | +3.0 | 0.19 | 14/44 (NCI-H1573, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3652.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.0874×, SW 900 0.132×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2030 0.123×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (CFPAC-1 0.136×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Elagolix sodium (drug)]] 0.05 µM in 1 line (SNU-1 0.0649×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HS-578T 0.0894×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.681× | -3.0 | 0.94 | 16/44 (HS-578T, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3652. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0874× (z -11.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 7.42 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 7.31 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0894× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 7.90 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0778× (z -8.8) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 9.05 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.05 µM 0.0649× (z -8.9) |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3652), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | +0.78 | +0.62 / +0.78 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[C1orf35]] | +0.75 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[SNHG7]] | +0.74 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[LEO1]] | +0.74 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.72 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[ZFAND2B]] | +0.72 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.71 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[RNF113A]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 | same gene group |
| [[RP9]] | +0.71 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[FBXW5]] | +0.71 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.71 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[MRPL43]] | +0.71 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[EPB41L4A-AS1]] | +0.70 | +0.54 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.63 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[GNG12]] | -0.63 | -0.37 / -0.67 | both halves | 7e-05 |  |
| [[ACTR2]] | -0.63 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[PSME3]] | -0.63 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[DHFR]] | -0.62 | -0.26 / -0.68 | both halves | 3e-04 |  |
| [[IPO5]] | -0.62 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[FGD5-AS1]] | -0.61 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[EPB41L2]] | -0.61 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[IL13RA1]] | -0.60 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[TARDBP]] | -0.60 | -0.39 / -0.63 | both halves | 6e-05 |  |
| [[FAM81A]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.59 | -0.47 / -0.65 | both halves | 2e-05 | STRING 941 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.741). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-39.0, -14.1); signed map (-16.3, -3.1). **Vector** length 67.3, 12.6% of its response variance represented; |z| ≥ 3 in 593 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +1.8 | +4.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.0 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.5 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.3 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.0 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | polycomb group ring finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,505,043-74,507,695 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NSPC1, RNF68, MGC10882 |
| Gene groups (HGNC) | Ring finger proteins; Polycomb group ring fingers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSM1](https://www.uniprot.org/uniprotkb/Q9BSM1) (Polycomb group RING finger protein 1):

> Component of the Polycomb group (PcG) multiprotein BCOR complex, a complex required to maintain the transcriptionally repressive state of some genes, such as BCL6 and the cyclin-dependent kinase inhibitor, CDKN1A. Transcriptional repressor that may be targeted to the DNA by BCL6; this transcription repressor activity may be related to PKC signaling pathway. Represses CDKN1A expression by binding to its promoter, and this repression is dependent on the retinoic acid response element (RARE …

**Summary**, from NCBI Gene [84759](https://www.ncbi.nlm.nih.gov/gene/84759):

> PCGF1 is a mammalian homolog of the Drosophila polycomb group genes, which act as transcriptional repressors to regulate anterior-posterior patterning in early embryonic development (Nunes et al., 2001 [PubMed 11287196]). See also PCGF2 (MIM 600346).[supplied by OMIM, Aug 2008]

**Accessions** — [HGNC:17615](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17615) · Entrez [84759](https://www.ncbi.nlm.nih.gov/gene/84759) · UniProt [Q9BSM1](https://www.uniprot.org/uniprotkb/Q9BSM1) · Ensembl [ENSG00000115289](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115289)

## Data

Gene col 3652: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3652); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3652, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3652]; `tensor/DDL_lfc|DDL_z.npy` [3652]; `embed/gene_vectors.npy` [3652]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3652 or target_col == 3652). Every well: [[PCGF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCGF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
