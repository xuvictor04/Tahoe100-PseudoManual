---
symbol: "CSNK2B"
type: "gene"
col: 12872
ensembl_id: "ENSG00000204435"
name: "casein kinase 2 beta"
location: "6p21.33"
module: 7
arm: "+"
pooled_cpm: 27.04
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CSNK2B

*casein kinase 2 beta* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.51× (z +13.5, q 1e-38, up in 43 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +5.0, q 6e-05, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.742× (z -4.6, q 0.002, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.403×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UROD]] (+0.66, fdr 7e-06), [[APH1A]] (+0.66, fdr 1e-05), [[PRPF18]] (+0.61, fdr 6e-05); moves opposite to [[GPR63]] (-0.49, fdr 2e-04), [[SERBP1]] (-0.48, fdr 2e-04), [[FXN]] (-0.48, fdr 6e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.51×** | +13.5 | 1e-38 | 43/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.27×** | +12.2 | 6e-32 | 33/35 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.42×** | +7.6 | 8e-12 | 34/39 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.62×** | +5.2 | 4e-05 | 36/46 (J82, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.0 | 6e-05 | 29/47 (NCI-H2347, SNU-423, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +4.6 | 3e-04 | 30/47 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.004 | 28/48 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.6 | 0.026 | 24/45 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.74× | +3.1 | 0.14 | 17/44 (Hs 766T, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12872.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.403×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.742×** | -4.6 | 0.002 | 34/48 (LS 180, Panc 03.27, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 26.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.42× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 25.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +11.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 59.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +8.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 34.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +12.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +10.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 29.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 39.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 23.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 42.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 36.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -9.1) |
| [[SW480 (line)]] | alt | 22.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +13.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UROD]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[APH1A]] | +0.66 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[PRPF18]] | +0.61 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[RNF167]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[KIAA1191]] | +0.58 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[WBP1]] | +0.58 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[OTUB1]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[GET3]] | +0.57 | +0.28 / +0.66 | both halves | 3e-04 |  |
| [[XAB2]] | +0.57 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[STXBP2]] | +0.56 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[CDIPT]] | +0.56 | +0.39 / +0.51 | both halves | 5e-05 | pathway: Glycerophospholipid biosynthesis |
| [[TOX4]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR63]] | -0.49 | -0.29 / -0.64 | both halves | 2e-04 |  |
| [[SERBP1]] | -0.48 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[FXN]] | -0.48 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[TMEM177]] | -0.48 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[ASB13]] | -0.48 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[SLC27A2]] | -0.47 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[CEP83]] | -0.47 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[G3BP1]] | -0.46 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[POLR3G]] | -0.45 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[SLAIN1]] | -0.45 | -0.29 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.194). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-16.8, -17.1); signed map (-3.4, -4.0). **Vector** length 44.2, 7.87% of its response variance represented; |z| ≥ 3 in 533 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +4.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.9 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -1.1 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | casein kinase 2 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,665,227-31,670,343 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Ckb1, Ckb2 |
| Gene groups (HGNC) | Casein kinase 2 beta family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 60 pathways, smallest: Phosphorylation and nuclear translocation of BMAL1 (ARNTL) and CLOCK; WNT mediated activation of DVL; Condensation of Prometaphase Chromosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [P67870](https://www.uniprot.org/uniprotkb/P67870) (Casein kinase II subunit beta):

> Regulatory subunit of casein kinase II/CK2. As part of the kinase complex regulates the basal catalytic activity of the alpha subunit a constitutively active serine/threonine-protein kinase that phosphorylates a large number of substrates containing acidic residues C-terminal to the phosphorylated serine or threonine. Participates in Wnt signaling (By similarity).; (Microbial infection) Upon infection with Epstein-Barr virus (EBV), the interaction with viral EBNA1 increases the association of …

**Summary**, from NCBI Gene [1460](https://www.ncbi.nlm.nih.gov/gene/1460):

> This gene encodes the beta subunit of casein kinase II, a ubiquitous protein kinase which regulates metabolic pathways, signal transduction, transcription, translation, and replication. The enzyme is composed of three subunits, alpha, alpha prime and beta, which form a tetrameric holoenzyme. The alpha and alpha prime subunits are catalytic, while the beta subunit serves regulatory functions. The enzyme localizes to the endoplasmic reticulum and the Golgi apparatus. Two transcript variants …

**Accessions** — [HGNC:2460](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2460) · Entrez [1460](https://www.ncbi.nlm.nih.gov/gene/1460) · UniProt [P67870](https://www.uniprot.org/uniprotkb/P67870) · Ensembl [ENSG00000204435](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204435)

## Data

Gene col 12872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12872); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12872]; `tensor/DDL_lfc|DDL_z.npy` [12872]; `embed/gene_vectors.npy` [12872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12872 or target_col == 12872). Every well: [[CSNK2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSNK2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
