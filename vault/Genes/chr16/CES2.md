---
symbol: "CES2"
type: "gene"
col: 10304
ensembl_id: "ENSG00000172831"
name: "carboxylesterase 2"
location: "16q22.1"
module: 62
arm: "+"
pooled_cpm: 28.87
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# CES2

*carboxylesterase 2* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.09× (z +7.0, q 1e-09, up in 24 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +5.9, q 1e-06, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.507× (z -6.7, q 1e-08, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PI4KB]] (+0.71, fdr 7e-06), [[PHLDA3]] (+0.70, fdr 1e-05), [[NKAPD1]] (+0.69, fdr 1e-05); moves opposite to [[METAP1]] (-0.64, fdr 1e-05), [[LRRC20]] (-0.61, fdr 2e-05), [[WRNIP1]] (-0.60, fdr 3e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10304.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +7.0 | 1e-09 | 24/33 (HepG2/C3A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +5.9 | 1e-06 | 30/47 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +5.8 | 1e-06 | 28/41 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +5.3 | 2e-05 | 24/44 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.7 | 3e-04 | 27/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +4.6 | 4e-04 | 29/47 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +3.8 | 0.011 | 24/45 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +3.7 | 0.017 | 18/36 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.045 | 15/48 (Hs 766T, A498, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.36× | +3.1 | 0.12 | 20/47 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 1.24× | +3.0 | 0.12 | 20/48 (A498, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10304.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.507×** | -6.7 | 1e-08 | 37/48 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.636×** | -4.5 | 0.002 | 30/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.646×** | -4.3 | 0.003 | 29/47 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.664×** | -4.0 | 0.008 | 27/46 (COLO 205, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.679×** | -3.8 | 0.015 | 25/47 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.802× | -3.1 | 0.21 | 17/48 (RPMI-7951, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.144× (z -14.5) |
| [[A-172 (line)]] | wt | 33.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.0) | — |
| [[A498 (line)]] | wt | 73.0 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.21× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0603× (z -13.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 57.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +10.3) | — |
| [[A-427 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 91.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PI4KB]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[PHLDA3]] | +0.70 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[NKAPD1]] | +0.69 | +0.79 / +0.55 | both halves | 1e-05 |  |
| [[ZNF764]] | +0.67 | +0.77 / +0.52 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.66 | +0.74 / +0.57 | both halves | 8e-06 |  |
| [[ANKRD49]] | +0.65 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[XPC]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[BAX]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[SNRNP27]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[ZNF79]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ABCA12]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TJAP1]] | +0.63 | +0.72 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | -0.64 | -0.73 / -0.50 | both halves | 1e-05 |  |
| [[LRRC20]] | -0.61 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[WRNIP1]] | -0.60 | -0.73 / -0.46 | both halves | 3e-05 |  |
| [[PRPS2]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[TBC1D24]] | -0.58 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[TMEM109]] | -0.57 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[DDX12P]] | -0.57 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[NCAPD3]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[GMPS]] | -0.56 | -0.64 / -0.54 | both halves | 1e-05 | pathway: Drug ADME |
| [[MAD2L1]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[LDHB]] | -0.56 | -0.54 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.4, 4.6); signed map (-0.2, -15.9). **Vector** length 95.3, 25.7% of its response variance represented; |z| ≥ 3 in 742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +3.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.2 | +4.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.0 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -1.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.2 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | -6.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Lonafarnib (drug)]] 0.5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | carboxylesterase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:66,934,444-66,945,096 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CE-2, iCE, CES2A1 |
| Gene groups (HGNC) | Carboxylesterases |
| Reactome | 4 pathways, smallest: Aspirin ADME; Drug ADME; Phase I - Functionalization of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [O00748](https://www.uniprot.org/uniprotkb/O00748) (Cocaine esterase):

> Involved in the detoxification of xenobiotics and in the activation of ester and amide prodrugs. Shows high catalytic efficiency for hydrolysis of cocaine, 4-methylumbelliferyl acetate, heroin and 6-monoacetylmorphine. Hydrolyzes aspirin, substrates with large alcohol group and small acyl group and endogenous lipids such as triacylglycerol. Converts monoacylglycerides to free fatty acids and glycerol. Hydrolyzes of 2-arachidonoylglycerol and prostaglandins.

**Summary**, from NCBI Gene [8824](https://www.ncbi.nlm.nih.gov/gene/8824):

> This gene encodes a member of the carboxylesterase large family. The family members are responsible for the hydrolysis or transesterification of various xenobiotics, such as cocaine and heroin, and endogenous substrates with ester, thioester, or amide bonds. They may participate in fatty acyl and cholesterol ester metabolism, and may play a role in the blood-brain barrier system. The protein encoded by this gene is the major intestinal enzyme and functions in intestine drug clearance. …

**Accessions** — [HGNC:1864](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1864) · Entrez [8824](https://www.ncbi.nlm.nih.gov/gene/8824) · UniProt [O00748](https://www.uniprot.org/uniprotkb/O00748) · Ensembl [ENSG00000172831](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172831)

## Data

Gene col 10304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10304); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10304]; `tensor/DDL_lfc|DDL_z.npy` [10304]; `embed/gene_vectors.npy` [10304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10304 or target_col == 10304). Every well: [[CES2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CES2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
