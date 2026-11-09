---
symbol: "STARD5"
type: "gene"
col: 10244
ensembl_id: "ENSG00000172345"
name: "StAR related lipid transfer domain containing 5"
location: "15q25.1"
module: 83
arm: "-"
pooled_cpm: 2.14
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# STARD5

*StAR related lipid transfer domain containing 5* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 11.0× (z +21.6, q 0e+00, up in 45 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LS 180 0.0668×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LS 180 0.0964×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP2]] (+0.68, fdr 8e-06), [[TENT5C]] (+0.67, fdr 7e-06), [[FOXO6]] (+0.64, fdr 1e-05); moves opposite to [[MSANTD2]] (-0.66, fdr 3e-05), [[ANXA2R-OT1]] (-0.64, fdr 2e-05), [[DNAJB14]] (-0.63, fdr 1e-04).
> It sits in the **-** arm of [[Module 083]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **11.0×** | +21.6 | 0e+00 | 45/45 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **8.92×** | +19.7 | 0e+00 | 40/42 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.36×** | +16.7 | 0e+00 | 41/43 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.19×** | +14.8 | 0e+00 | 25/32 (CFPAC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.24×** | +10.6 | 4e-24 | 36/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.06×** | +9.7 | 4e-20 | 7/10 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +8.2 | 2e-14 | 1/2 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +7.6 | 1e-12 | 20/43 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.88×** | +5.7 | 9e-07 | 12/26 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +5.5 | 2e-06 | 7/43 (SHP-77, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +5.3 | 6e-06 | 1/4 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +4.5 | 3e-04 | 11/29 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.56×** | +4.4 | 4e-04 | 5/36 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +3.8 | 0.006 | 2/10 (CFPAC-1, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.013 | 8/44 (LS 180, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.049 | 13/37 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.093 | 3/43 (LoVo, J82, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10244.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LS 180 0.0668×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LS 180 0.0964×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.701× | -3.2 | 0.51 | 11/38 (SHP-77, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.714× | -3.1 | 0.51 | 2/42 (J82, LS 180) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 8.46 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0668× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A-172 (line)]] | wt | 0.794 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.611 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.786 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.806 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.647 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP2]] | +0.68 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[TENT5C]] | +0.67 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[FOXO6]] | +0.64 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CYRIA]] | +0.62 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[MLF1]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[RAB3A]] | +0.60 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[LGMN]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 | pathway: Metabolism of steroids |
| [[CDK18]] | +0.59 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[EPHB3]] | +0.59 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[AHDC1]] | +0.59 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[MAPRE2]] | +0.59 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[TUFT1]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSANTD2]] | -0.66 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[ANXA2R-OT1]] | -0.64 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[DNAJB14]] | -0.63 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[GABPB1]] | -0.61 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[DNAAF10]] | -0.61 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[POC1B-AS1]] | -0.60 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TMEM11-DT]] | -0.57 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ITPA]] | -0.57 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[AP5M1]] | -0.57 | -0.26 / -0.25 | both halves | 4e-04 |  |
| [[LTO1]] | -0.56 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[DUS2]] | -0.55 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[AP4S1]] | -0.55 | -0.15 / -0.47 | ⚠ not reproduced | 0.001 |  |
| [[GABPB1-AS1]] | -0.55 | -0.24 / -0.36 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.4, -6.2); signed map (-0.6, 19.3). **Vector** length 51.3, 6.50% of its response variance represented; |z| ≥ 3 in 1,314 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +21.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +19.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +8.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.0 | +16.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.9 | +2.7 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +0.9 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +0.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -3.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.3 | -2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | StAR related lipid transfer domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:81,309,053-81,324,183 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10327 |
| Gene groups (HGNC) | StAR related lipid transfer domain containing |
| Reactome | 4 pathways, smallest: Recycling of bile acids and salts; Bile acid and bile salt metabolism; Metabolism of steroids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSY2](https://www.uniprot.org/uniprotkb/Q9NSY2) (StAR-related lipid transfer protein 5):

> May be involved in the intracellular transport of sterols or other lipids. May bind cholesterol or other sterols (By similarity).

**Summary**, from NCBI Gene [80765](https://www.ncbi.nlm.nih.gov/gene/80765):

> Proteins containing a steroidogenic acute regulatory-related lipid transfer (START) domain are often involved in the trafficking of lipids and cholesterol between diverse intracellular membranes. This gene is a member of the StarD subfamily that encodes START-related lipid transfer proteins. The protein encoded by this gene is a cholesterol transporter and is also able to bind and transport other sterol-derived molecules related to the cholesterol/bile acid biosynthetic pathways such as …

**Accessions** — [HGNC:18065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18065) · Entrez [80765](https://www.ncbi.nlm.nih.gov/gene/80765) · UniProt [Q9NSY2](https://www.uniprot.org/uniprotkb/Q9NSY2) · Ensembl [ENSG00000172345](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172345)

## Data

Gene col 10244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10244); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10244]; `tensor/DDL_lfc|DDL_z.npy` [10244]; `embed/gene_vectors.npy` [10244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10244 or target_col == 10244). Every well: [[STARD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STARD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
