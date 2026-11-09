---
symbol: "ASB6"
type: "gene"
col: 7264
ensembl_id: "ENSG00000148331"
name: "ankyrin repeat and SOCS box containing 6"
location: "9q34.11"
module: 7
arm: "+"
pooled_cpm: 4.92
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 2
n_dd_up_clean: 23
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ASB6

*ankyrin repeat and SOCS box containing 6* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.72× (z +15.2, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.650× (z -4.8, q 7e-04, down in 18 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Brimonidine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0648×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.0836×; ⚠ toxic); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (BT-474 0.106×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (LS 180 0.0744×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C15orf39]] (+0.66, fdr 7e-06), [[LRRC14]] (+0.64, fdr 2e-05), [[ARFRP1]] (+0.63, fdr 7e-06); moves opposite to [[TRA2A]] (-0.49, fdr 3e-05), [[CRNDE]] (-0.47, fdr 4e-05), [[COX8A]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7264.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.72×** | +15.2 | 0e+00 | 46/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.22×** | +13.6 | 2e-39 | 43/46 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.73×** | +11.6 | 5e-29 | 42/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.10×** | +8.6 | 1e-15 | 30/44 (SW480, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +8.5 | 2e-15 | 20/40 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +8.3 | 8e-15 | 29/45 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.03×** | +8.2 | 2e-14 | 29/46 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.54×** | +7.7 | 1e-12 | 24/41 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +7.6 | 1e-12 | 23/38 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.81×** | +6.5 | 5e-09 | 18/43 (HEC-1-A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +6.3 | 2e-08 | 24/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.3 | 7e-06 | 12/28 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +5.2 | 8e-06 | 9/29 (J82, RKO, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.57×** | +5.2 | 8e-06 | 18/42 (A498, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.37×** | +5.2 | 8e-06 | 13/40 (J82, C32, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +5.1 | 1e-05 | 16/47 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +4.9 | 3e-05 | 15/41 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 8e-04 | 12/45 (HT-29, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7264.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Brimonidine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0648×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.0836×; ⚠ toxic); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (BT-474 0.106×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (LS 180 0.0744×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.650×** | -4.8 | 7e-04 | 18/43 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | **0.799×** | -3.7 | 0.054 | 12/47 (RPMI-7951, NCI-H1792, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.824× | -3.2 | 0.24 | 11/46 (MIA PaCa-2, CHP-212, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7264. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.62 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 4.69 | 0 | 2 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0836× (z -8.8) ⚠ toxic · without an alert: [[Cobimetinib (drug)]] 0.05 µM 0.0744× (z -8.6) |
| [[BT-474 (line)]] | alt | 7.62 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.106× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 3.20 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0648× (z -10.4) |
| [[A-172 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7264), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf39]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[LRRC14]] | +0.64 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[ARFRP1]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ZNF513]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[CPTP]] | +0.63 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[UCK1]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ZSCAN22]] | +0.62 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[UBL4A]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TMEM115]] | +0.58 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[RIPOR1]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ABCF3]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[POP4]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRA2A]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[CRNDE]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[COX8A]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.589). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-47.0, -1.0); signed map (-6.5, -27.6). **Vector** length 54.2, 6.84% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +8.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.1 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.3 | +8.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +2.5 |
| fall | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -1.4 | +5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +1.6 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.1 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and SOCS box containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,634,604-129,642,169 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWX5](https://www.uniprot.org/uniprotkb/Q9NWX5) (Ankyrin repeat and SOCS box protein 6):

> Probable substrate-recognition component of a SCF-like ECS (Elongin-Cullin-SOCS-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. May play a role in the regulation of cell proliferation and autophagy by promoting the ubiquitination and degradation of SQSTM1.

**Summary**, from NCBI Gene [140459](https://www.ncbi.nlm.nih.gov/gene/140459):

> The protein encoded by this gene belongs to a family of ankyrin repeat proteins that, along with four other protein families, contain a C-terminal SOCS box motif. Growing evidence suggests that the SOCS box, similar to the F-box, acts as a bridge between specific substrate-binding domains and the more generic proteins that comprise a large family of E3 ubiquitin protein ligases. Alternatively spliced transcript variants have been identified for this gene. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:17181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17181) · Entrez [140459](https://www.ncbi.nlm.nih.gov/gene/140459) · UniProt [Q9NWX5](https://www.uniprot.org/uniprotkb/Q9NWX5) · Ensembl [ENSG00000148331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148331)

## Data

Gene col 7264: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7264); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7264, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7264]; `tensor/DDL_lfc|DDL_z.npy` [7264]; `embed/gene_vectors.npy` [7264]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7264 or target_col == 7264). Every well: [[ASB6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASB6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
