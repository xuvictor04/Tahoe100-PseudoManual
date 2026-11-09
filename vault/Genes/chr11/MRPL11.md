---
symbol: "MRPL11"
type: "gene"
col: 10502
ensembl_id: "ENSG00000174547"
name: "mitochondrial ribosomal protein L11"
location: "11q13.2"
module: 15
arm: "+"
pooled_cpm: 12.77
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# MRPL11

*mitochondrial ribosomal protein L11* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.56× (z +11.7, q 8e-29, up in 33 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +8.4, q 1e-14, up in 35 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 4.34×, LoVo 6.52×, A549 7.17×, PANC-1 3.63×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 3.57×, NCI-H460 4.80×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.117×); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 0.361×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS15]] (+0.61, fdr 3e-05), [[PDHX]] (+0.59, fdr 3e-05), [[SDHD]] (+0.58, fdr 3e-05); moves opposite to [[MMP17]] (-0.48, fdr 1e-04), [[IER2]] (-0.48, fdr 2e-04), [[CCDC112]] (-0.46, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10502.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 4.34×, LoVo 6.52×, A549 7.17×, PANC-1 3.63×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 3.57×, NCI-H460 4.80×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.56×** | +11.7 | 8e-29 | 33/36 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.09×** | +10.9 | 5e-25 | 19/20 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +8.4 | 1e-14 | 35/45 (BT-474, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.22×** | +7.4 | 2e-11 | 25/28 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.74×** | +5.6 | 3e-06 | 27/41 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.7 | 2e-04 | 22/39 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.68× | +3.1 | 0.13 | 7/44 (LoVo, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.38× | +3.1 | 0.13 | 21/44 (SW480, KATO III, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.38× | +3.1 | 0.13 | 14/45 (HOP62, NCI-H23, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10502.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.117×); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 0.361×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Baicalin (drug)]] 5 µM |  | 0.779× | -3.5 | 0.22 | 13/48 (SW1417, NCI-H1573, …) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.733× | -3.0 | 0.75 | 12/47 (LOX-IMVI, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 10.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.17× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.117× (z -9.7) |
| [[KATO III (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 9.86 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.52× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 9.28 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.80× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 10 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS15]] | +0.61 | +0.44 / +0.58 | both halves | 3e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 998 |
| [[PDHX]] | +0.59 | +0.43 / +0.51 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[SDHD]] | +0.58 | +0.51 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[HIGD2A]] | +0.57 | +0.33 / +0.62 | both halves | 1e-04 |  |
| [[SUMO3]] | +0.56 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[TIAL1]] | +0.56 | +0.22 / +0.59 | both halves | 6e-04 |  |
| [[FBXW9]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[LEMD3]] | +0.54 | +0.29 / +0.43 | both halves | 2e-04 |  |
| [[WDR20]] | +0.54 | +0.18 / +0.50 | ⚠ one half (not replicated) | 0.001 |  |
| [[PRDM10]] | +0.54 | +0.28 / +0.42 | both halves | 3e-04 |  |
| [[DIDO1]] | +0.53 | +0.47 / +0.30 | both halves | 2e-04 |  |
| [[RPRD1B]] | +0.53 | +0.48 / +0.32 | both halves | 2e-04 |  |
| [[EIF2D]] | +0.53 | +0.56 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP17]] | -0.48 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[IER2]] | -0.48 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[CCDC112]] | -0.46 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[LIMA1]] | -0.46 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[R3HDM4]] | -0.45 | -0.23 / -0.42 | both halves | 5e-04 |  |
| [[USP4]] | -0.45 | -0.36 / -0.24 | both halves | 4e-04 | STRING 412 |
| [[MOCS1]] | -0.45 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[CBX6]] | -0.44 | -0.20 / -0.46 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.485). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.1, 24.4); signed map (-19.2, -30.0). **Vector** length 44.3, 6.31% of its response variance represented; |z| ≥ 3 in 605 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +8.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.6 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +11.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | +1.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +0.9 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.8 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,435,075-66,466,738 (-) |
| Ensembl biotype | protein_coding |
| Also known as | uL11m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9Y3B7](https://www.uniprot.org/uniprotkb/Q9Y3B7) carries no function annotation.

**Summary**, from NCBI Gene [65003](https://www.ncbi.nlm.nih.gov/gene/65003):

> This nuclear gene encodes a 39S subunit component of the mitochondial ribosome. Alternative splicing results in multiple transcript variants. Pseudogenes for this gene are found on chromosomes 5 and 12. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:14042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14042) · Entrez [65003](https://www.ncbi.nlm.nih.gov/gene/65003) · UniProt [Q9Y3B7](https://www.uniprot.org/uniprotkb/Q9Y3B7) · Ensembl [ENSG00000174547](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174547)

## Data

Gene col 10502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10502); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10502]; `tensor/DDL_lfc|DDL_z.npy` [10502]; `embed/gene_vectors.npy` [10502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10502 or target_col == 10502). Every well: [[MRPL11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
