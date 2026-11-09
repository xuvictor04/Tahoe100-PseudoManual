---
symbol: "PMS2P1"
type: "gene"
col: 1218
ensembl_id: "ENSG00000078319"
name: "PMS1 homolog 2, mismatch repair system component pseudogene 1"
location: "7q22.1"
module: 168
arm: "+"
pooled_cpm: 3.57
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# PMS2P1

*PMS1 homolog 2, mismatch repair system component pseudogene 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.34× (z +10.3, q 4e-22, up in 32 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.92× (z +9.4, q 1e-18, up in 25 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.670× (z -3.9, q 0.047, down in 7 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.150×; ⚠ toxic; transcription drop); [[Decitabine (drug)]] 0.5 µM in 1 line (A-172 0.0678×); [[BI-78D3 (drug)]] 0.5 µM in 1 line (A-427 0.0590×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIGD1]] (+0.61, fdr 1e-05), [[RWDD4]] (+0.60, fdr 1e-05), [[NSUN5P1]] (+0.60, fdr 2e-05); moves opposite to [[ZSWIM6]] (-0.62, fdr 1e-05), [[DNAJA1]] (-0.53, fdr 3e-05), [[FAM222A]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 168]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1218.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.34×** | +10.3 | 4e-22 | 32/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +9.4 | 1e-18 | 25/35 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +7.8 | 1e-12 | 2/7 (PANC-1, HOP62) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +5.9 | 7e-07 | 6/46 (A549, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.4 | 8e-06 | 6/18 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +4.9 | 1e-04 | 1/4 (PANC-1) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +4.8 | 1e-04 | 5/17 (A-427, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.1 | 0.002 | 4/20 (NCI-H2030, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.1 | 0.003 | 3/30 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.017 | 7/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.90×** | +3.4 | 0.030 | 0/7 | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.030 | 5/44 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.084 | 2/30 (C-33 A, NCI-H460) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.1 | 0.087 | 7/29 (BT-474, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1218.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.150×; ⚠ toxic; transcription drop); [[Decitabine (drug)]] 0.5 µM in 1 line (A-172 0.0678×); [[BI-78D3 (drug)]] 0.5 µM in 1 line (A-427 0.0590×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.670×** | -3.9 | 0.047 | 7/43 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.720× | -3.4 | 0.22 | 6/42 (AsPC-1, BT-474, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.732× | -3.2 | 0.26 | 6/46 (HepG2/C3A, NCI-H23, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.739× | -3.1 | 0.28 | 6/36 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.18 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0678× (z -8.9) |
| [[A-427 (line)]] | wt | 6.74 | 0 | 1 | — | [[BI-78D3 (drug)]] 0.5 µM 0.0590× (z -8.7) |
| [[SW480 (line)]] | alt | 3.85 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -9.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIGD1]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[RWDD4]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[NSUN5P1]] | +0.60 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[LINC00115]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[RFT1]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[GOT1-DT]] | +0.59 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[CCDC61]] | +0.58 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[PMS2]] | +0.57 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[PACRGL]] | +0.56 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[TMEM231]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SDHAF4]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ZNF333]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM6]] | -0.62 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[DNAJA1]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[FAM222A]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[UBR1]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[KLHL4]] | -0.49 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[TLE4]] | -0.49 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[CLEC16A]] | -0.48 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[TUT7]] | -0.48 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[MRFAP1]] | -0.46 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[LINC02803]] | -0.46 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ABAT]] | -0.46 | -0.38 / -0.38 | both halves | 6e-05 |  |
| [[NEK1]] | -0.46 | -0.40 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-9.8, -14.7); signed map (-36.9, -22.5). **Vector** length 42.3, 4.35% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +4.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +5.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.1 | +1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.0 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +2.8 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +0.9 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | PMS1 homolog 2, mismatch repair system component pseudogene 1 |
| Locus type | pseudogene |
| Location | 7q22.1 — chr7:100,328,836-100,335,860 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | PMS3, PMS8, PMS2L13, PMSR2, PMSR1; previously PMS2L6, PMS2L8, PMS2L7, PMS2L1 |
| Matched by | ensembl_id |

UniProt [A4D2B8](https://www.uniprot.org/uniprotkb/A4D2B8) carries no function annotation.

**Summary**, from NCBI Gene [5379](https://www.ncbi.nlm.nih.gov/gene/5379):

> Predicted to enable ATP hydrolysis activity; ATP-dependent DNA damage sensor activity; and kinase activity. Predicted to be involved in mismatch repair. Predicted to be part of mismatch repair complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9123](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9123) · Entrez [5379](https://www.ncbi.nlm.nih.gov/gene/5379) · UniProt [A4D2B8](https://www.uniprot.org/uniprotkb/A4D2B8) · Ensembl [ENSG00000078319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078319)

## Data

Gene col 1218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1218); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1218]; `tensor/DDL_lfc|DDL_z.npy` [1218]; `embed/gene_vectors.npy` [1218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1218 or target_col == 1218). Every well: [[PMS2P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMS2P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
