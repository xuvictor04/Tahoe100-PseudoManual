---
symbol: "HTRA2"
type: "gene"
col: 3658
ensembl_id: "ENSG00000115317"
name: "HtrA serine peptidase 2"
location: "2p13.1"
module: 58
arm: "+"
pooled_cpm: 5.76
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# HTRA2

*HtrA serine peptidase 2* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.38× (z +7.2, q 4e-10, up in 22 of 29 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +6.7, q 2e-09, up in 29 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.634× (z -5.4, q 4e-05, down in 24 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Sunitinib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0654×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (NCI-H2030 0.0968×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-423 0.154×).
> Its strongest partners by |cos| (78 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MICOS13]] (+0.66, fdr 1e-05), [[RIC8A]] (+0.64, fdr 5e-05), [[PHF13]] (+0.63, fdr 1e-05); moves opposite to [[DPY19L4]] (-0.52, fdr 0.003, ⚠ one half only (not replicated)), [[MCCC2]] (-0.52, fdr 9e-05), [[EWSR1]] (-0.51, fdr 0.002, ⚠ one half only (not replicated)), [[GUF1]] (-0.51, fdr 9e-05), [[NDUFS1]] (-0.50, fdr 4e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3658.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.38×** | +7.2 | 4e-10 | 22/29 (A498, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.31×** | +6.9 | 8e-10 | 34/47 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.31×** | +6.9 | 8e-10 | 38/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.33×** | +6.7 | 2e-09 | 4/9 (A498, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.25×** | +6.7 | 2e-09 | 38/46 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +6.7 | 2e-09 | 29/40 (KATO III, A498, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.22×** | +6.6 | 4e-09 | 33/45 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +5.9 | 3e-07 | 26/48 (A498, SW1417, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +4.1 | 0.003 | 17/40 (HepG2/C3A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.007 | 15/47 (PANC-1, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +3.6 | 0.018 | 11/47 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.53×** | +3.5 | 0.022 | 14/35 (A-427, SW1417, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3658.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Sunitinib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0654×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (NCI-H2030 0.0968×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-423 0.154×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.634×** | -5.4 | 4e-05 | 24/40 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.672× | -3.2 | 0.31 | 14/45 (RKO, LS 180, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.691× | -3.1 | 0.31 | 11/48 (KATO III, H4, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.694× | -3.1 | 0.31 | 12/39 (HCT15, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3658. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 3.39 | 0 | 1 | — | [[Sunitinib (drug)]] 0.05 µM 0.0654× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 5.51 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0968× (z -8.6) |
| [[SNU-423 (line)]] | alt | 4.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -8.5) |
| [[A-172 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3658), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 19 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICOS13]] | +0.66 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[RIC8A]] | +0.64 | +0.40 / +0.69 | both halves | 5e-05 |  |
| [[PHF13]] | +0.63 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[EXOSC4]] | +0.62 | +0.29 / +0.73 | both halves | 3e-04 |  |
| [[TMEM276]] | +0.60 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[PLSCR3]] | +0.58 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[EMC6]] | +0.57 | +0.27 / +0.67 | both halves | 3e-04 |  |
| [[MRPS12]] | +0.56 | +0.17 / +0.66 | ⚠ one half (not replicated) | 0.001 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[DNASE1L1]] | +0.56 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[TIMM10]] | +0.56 | +0.40 / +0.58 | both halves | 5e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[TUSC2]] | +0.56 | +0.26 / +0.51 | both halves | 4e-04 |  |
| [[CDC34]] | +0.55 | +0.26 / +0.64 | both halves | 4e-04 |  |
| [[PAQR4]] | +0.55 | +0.43 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L4]] | -0.52 | -0.10 / -0.66 | ⚠ one half (not replicated) | 0.003 |  |
| [[MCCC2]] | -0.52 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[EWSR1]] | -0.51 | -0.12 / -0.60 | ⚠ one half (not replicated) | 0.002 |  |
| [[OXCT1]] | -0.51 | -0.17 / -0.51 | ⚠ one half (not replicated) | 0.001 | pathway: Mitochondrial protein degradation |
| [[GUF1]] | -0.51 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[NDUFS1]] | -0.50 | -0.26 / -0.45 | both halves | 4e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[SUGT1P3]] | -0.50 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[NBN]] | -0.50 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[ZC3H7A]] | -0.50 | -0.29 / -0.44 | both halves | 3e-04 |  |
| [[FUBP1]] | -0.50 | -0.10 / -0.55 | ⚠ one half (not replicated) | 0.003 |  |
| [[MATR3]] | -0.48 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[NELFCD]] | -0.48 | -0.18 / -0.56 | ⚠ one half (not replicated) | 9e-04 |  |
| [[TIA1]] | -0.47 | -0.28 / -0.34 | both halves | 3e-04 | STRING 482 |
| [[EXOSC8]] | -0.47 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[AGL]] | -0.46 | -0.23 / -0.42 | both halves | 5e-04 |  |
| [[PGGT1B]] | -0.46 | -0.26 / -0.39 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.9, -10.7); signed map (-26.1, 3.7). **Vector** length 45.7, 6.25% of its response variance represented; |z| ≥ 3 in 676 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.3 | +6.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.1 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.1 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +6.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.3 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | -5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -0.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | HtrA serine peptidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,529,596-74,533,350 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OMI, PARK13; previously PRSS25 |
| Gene groups (HGNC) | PDZ domain containing; HtrA serine protease family |
| Hallmark sets | HEME_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Mitochondrial unfolded protein response (UPRmt); Mitochondrial protein degradation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [O43464](https://www.uniprot.org/uniprotkb/O43464) (Serine protease HTRA2, mitochondrial):

> [Isoform 1]: Serine protease that shows proteolytic activity against a non-specific substrate beta-casein. Promotes apoptosis by either relieving the inhibition of BIRC proteins on caspases, leading to an increase in caspase activity; or by a BIRC inhibition-independent, caspase-independent and serine protease activity-dependent mechanism. Cleaves BIRC6 and relieves its inhibition on CASP3, CASP7 and CASP9, but it is also prone to inhibition by BIRC6. Cleaves THAP5 and promotes its degradation …

**Summary**, from NCBI Gene [27429](https://www.ncbi.nlm.nih.gov/gene/27429):

> This gene encodes a serine protease. The protein has been localized in the endoplasmic reticulum and interacts with an alternatively spliced form of mitogen-activated protein kinase 14. The protein has also been localized to the mitochondria with release to the cytosol following apoptotic stimulus. The protein is thought to induce apoptosis by binding the apoptosis inhibitory protein baculoviral IAP repeat-containing 4. Nuclear localization of this protein has also been observed. Alternate …

**Accessions** — [HGNC:14348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14348) · Entrez [27429](https://www.ncbi.nlm.nih.gov/gene/27429) · UniProt [O43464](https://www.uniprot.org/uniprotkb/O43464) · Ensembl [ENSG00000115317](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115317)

## Data

Gene col 3658: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3658); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3658, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3658]; `tensor/DDL_lfc|DDL_z.npy` [3658]; `embed/gene_vectors.npy` [3658]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3658 or target_col == 3658). Every well: [[HTRA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HTRA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
