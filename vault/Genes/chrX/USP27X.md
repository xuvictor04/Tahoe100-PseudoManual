---
symbol: "USP27X"
type: "gene"
col: 15802
ensembl_id: "ENSG00000273820"
name: "ubiquitin specific peptidase 27 X-linked"
location: "Xp11.23"
module: 11
arm: "+"
pooled_cpm: 3.88
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# USP27X

*ubiquitin specific peptidase 27 X-linked* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.01× (z +6.6, q 2e-08, up in 22 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.395× (z -9.2, q 2e-17, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP25L]] (+0.72, fdr 7e-06), [[METTL18]] (+0.71, fdr 7e-06), [[TBCC]] (+0.71, fdr 7e-06); moves opposite to [[NUTF2]] (-0.62, fdr 1e-05), [[RPA1]] (-0.58, fdr 1e-05), [[CPSF6]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15802.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.01×** | +6.6 | 2e-08 | 22/43 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +5.9 | 9e-07 | 15/44 (Panc 03.27, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.79×** | +5.8 | 2e-06 | 19/44 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.4 | 8e-06 | 15/37 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +4.9 | 1e-04 | 0/8 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +4.4 | 9e-04 | 11/38 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.1 | 0.004 | 10/41 (NCI-H2030, HOP62, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.008 | 11/43 (NCI-H23, NCI-H2347, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.029 | 7/36 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.033 | 7/41 (Hs 766T, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.36× | +3.1 | 0.11 | 5/38 (Panc 03.27, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15802.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.395×** | -9.2 | 2e-17 | 30/46 (J82, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.406×** | -8.9 | 1e-16 | 27/44 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.451×** | -7.9 | 7e-13 | 22/36 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.501×** | -6.8 | 1e-09 | 27/44 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.656×** | -4.2 | 0.004 | 15/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.696×** | -3.6 | 0.034 | 13/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.513×** | -3.4 | 0.047 | 12/42 (NCI-H460, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.714×** | -3.3 | 0.061 | 11/45 (MIA PaCa-2, SW480, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -3.3 | 0.061 | 9/48 (HCT15, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15802. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 4.63 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0424× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.166× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 4.01 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.101× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 4.19 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.118× (z -9.6) |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0463× (z -13.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 3.55 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0685× (z -8.6) |
| [[A-172 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15802), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP25L]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[METTL18]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[TBCC]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[ZBED9]] | +0.69 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[C1orf131]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[GSPT2]] | +0.67 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[STK16]] | +0.67 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[TRIM47]] | +0.66 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[PEX12]] | +0.66 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[SNW1]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[PHAX]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUTF2]] | -0.62 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[RPA1]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[CPSF6]] | -0.58 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[TBCD]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CHID1]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[TMEM248]] | -0.56 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[SEPTIN7P14]] | -0.56 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[UBE2G2]] | -0.55 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[TM9SF2]] | -0.55 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[TUFM]] | -0.55 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[MLEC]] | -0.55 | -0.57 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.7, 7.1); signed map (3.2, -20.1). **Vector** length 55.2, 7.51% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.3 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | -0.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +1.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.0 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -8.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -9.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.9 | -4.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -0.9 | -2.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 27 X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:49,879,484-49,882,558 (+) |
| Ensembl biotype | protein_coding |
| Also known as | USP27 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NNY8](https://www.uniprot.org/uniprotkb/A6NNY8) (Ubiquitin carboxyl-terminal hydrolase 27):

> Deubiquitinase involved in innate antiviral immunity by mediating deubiquitination of CGAS and RIGI. Negatively regulates RIGI by mediating 'Lys-63'-linked deubiquitination of RIGI, inhibiting type I interferon signaling. Also regulates 'Lys-63'-linked ubiquitination level of MDA5/IFIH1. Acts as a positive regulator of the cGAS-STING pathway by catalyzing 'Lys-48'-linked deubiquitination of CGAS, thereby promoting its stabilization. Can reduce the levels of BCL2L11/BIM ubiquitination and …

**Summary**, from NCBI Gene [389856](https://www.ncbi.nlm.nih.gov/gene/389856):

> This gene encodes a member of the peptidase protein family. The encoded protein functions as a deubiquitinase that is involved in upregulation of the pro-apoptotic Bim protein. This protein may act as a tumor suppressor by increasing levels of Bim to counteract anti-apoptotic signals in cancer cells. Mutations in this gene have been associated with X-linked cognitive disability. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:13486](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13486) · Entrez [389856](https://www.ncbi.nlm.nih.gov/gene/389856) · UniProt [A6NNY8](https://www.uniprot.org/uniprotkb/A6NNY8) · Ensembl [ENSG00000273820](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273820)

## Data

Gene col 15802: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15802); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15802, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15802]; `tensor/DDL_lfc|DDL_z.npy` [15802]; `embed/gene_vectors.npy` [15802]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15802 or target_col == 15802). Every well: [[USP27X — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP27X.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
