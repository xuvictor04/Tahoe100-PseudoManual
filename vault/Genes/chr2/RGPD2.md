---
symbol: "RGPD2"
type: "gene"
col: 11658
ensembl_id: "ENSG00000185304"
name: "RANBP2 like and GRIP domain containing 2"
location: "2p11.2"
module: 70
arm: "+"
pooled_cpm: 3.11
n_lines_expressing: 13
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# RGPD2

*RANBP2 like and GRIP domain containing 2* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.17× (z +13.0, q 6e-36, up in 0 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.55× (z +10.5, q 1e-23, up in 8 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.585× (z -3.9, q 0.033, down in 0 of 11 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0966×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-A]] (+0.57, fdr 3e-05), [[B2M]] (+0.53, fdr 1e-04), [[MAK]] (+0.52, fdr 5e-05); moves opposite to [[PHB1]] (-0.54, fdr 2e-04), [[HMBS]] (-0.53, fdr 3e-05), [[SLC25A10]] (-0.50, fdr 9e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11658.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.17×** | +13.0 | 6e-36 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.38×** | +12.8 | 4e-35 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.97×** | +11.7 | 1e-29 | 1/6 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.55×** | +10.5 | 1e-23 | 8/10 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +6.6 | 6e-09 | 1/10 (AsPC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +6.5 | 6e-09 | 9/11 (BT-474, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.06×** | +5.7 | 9e-07 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.55×** | +5.3 | 8e-06 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.89×** | +5.0 | 3e-05 | 11/11 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.28×** | +4.9 | 5e-05 | 0/3 | top dose only | noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.61×** | +4.0 | 0.003 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.0 | 0.003 | 1/10 (AsPC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.013 | 7/11 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.39×** | +3.6 | 0.013 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.5 | 0.015 | 1/11 (BT-474) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.79×** | +3.3 | 0.035 | 1/10 (COLO 205) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.058 | 0/11 | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.73×** | +3.1 | 0.058 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.064 | 0/11 | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +3.0 | 0.068 | 5/10 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.69×** | +3.0 | 0.080 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.68×** | +2.9 | 0.083 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.45×** | +2.9 | 0.083 | 0/11 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11658.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0966×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.585×** | -3.9 | 0.033 | 0/11 | inconsistent across doses | position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.591×** | -3.9 | 0.033 | 0/11 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.661× | -3.1 | 0.36 | 0/11 | inconsistent across doses | position effect removed |
| [[AZD-7648 (drug)]] 0.05 µM |  | 0.669× | -3.0 | 0.37 | 0/11 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11658. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 27.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +16.0) | — |
| [[Panc 03.27 (line)]] | alt | 6.20 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0966× (z -8.8) |
| [[A-172 (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.382 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11658), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-A]] | +0.57 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[B2M]] | +0.53 | +0.33 / +0.53 | both halves | 1e-04 | STRING 620 |
| [[MAK]] | +0.52 | +0.44 / +0.39 | both halves | 5e-05 |  |
| [[HLA-E]] | +0.52 | +0.29 / +0.50 | both halves | 2e-04 |  |
| [[NFKBIB]] | +0.52 | +0.30 / +0.43 | both halves | 2e-04 |  |
| [[HLA-B]] | +0.52 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[STAP2]] | +0.51 | +0.43 / +0.36 | both halves | 9e-05 |  |
| [[FRMD4B]] | +0.50 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[LITAF]] | +0.50 | +0.39 / +0.36 | both halves | 9e-05 |  |
| [[EIF1B]] | +0.50 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[FOXC1]] | +0.48 | +0.37 / +0.38 | both halves | 9e-05 |  |
| [[RFX1]] | +0.47 | +0.39 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHB1]] | -0.54 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[HMBS]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[SLC25A10]] | -0.50 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[XPO7]] | -0.48 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[WDR36]] | -0.48 | -0.42 / -0.22 | both halves | 6e-04 |  |
| [[USP10]] | -0.47 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[TOMM40]] | -0.46 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[CDC123]] | -0.45 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[TATDN2]] | -0.45 | -0.33 / -0.23 | both halves | 5e-04 |  |
| [[UTP18]] | -0.45 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[CHCHD3]] | -0.44 | -0.45 / -0.29 | both halves | 3e-04 |  |
| [[RITA1]] | -0.44 | -0.36 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.499). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.8, -15.1); signed map (64.4, 25.9). **Vector** length 19.0, 3.47% of its response variance represented; |z| ≥ 3 in 219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.3 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.9 | +1.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.9 | +6.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.7 | +0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.7 | +0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.6 | +0.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +0.6 | +1.0 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -0.8 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.7 | +0.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.6 | +0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -0.9 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.4 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.4 | -1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | RANBP2 like and GRIP domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:87,755,960-87,825,796 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RGP2, RANBP2L2 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [P0DJD1](https://www.uniprot.org/uniprotkb/P0DJD1) carries no function annotation.

**Summary**, from NCBI Gene [729857](https://www.ncbi.nlm.nih.gov/gene/729857):

> Predicted to enable SUMO transferase activity. Predicted to be involved in NLS-bearing protein import into nucleus and nuclear export. Predicted to be part of nuclear pore. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32415](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32415) · Entrez [729857](https://www.ncbi.nlm.nih.gov/gene/729857) · UniProt [P0DJD1](https://www.uniprot.org/uniprotkb/P0DJD1) · Ensembl [ENSG00000185304](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185304)

## Data

Gene col 11658: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11658); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11658, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11658]; `tensor/DDL_lfc|DDL_z.npy` [11658]; `embed/gene_vectors.npy` [11658]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11658 or target_col == 11658). Every well: [[RGPD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGPD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
