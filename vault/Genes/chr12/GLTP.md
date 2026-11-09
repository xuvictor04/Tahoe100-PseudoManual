---
symbol: "GLTP"
type: "gene"
col: 6305
ensembl_id: "ENSG00000139433"
name: "glycolipid transfer protein"
location: "12q24.11"
module: 3
arm: "+"
pooled_cpm: 54.44
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# GLTP

*glycolipid transfer protein* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.37× (z +4.0, q 0.037, up in 25 of 47 measured lines) ⚠ toxic. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (MIA PaCa-2 2.99×, NCI-H1573 1.95×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 2.63×, A498 2.09×; ⚠ cell-cycle shift, explains ~6% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.678× (z -4.9, q 6e-04, down in 31 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.808× (z -3.9, q 0.025, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO9B]] (+0.64, fdr 7e-06), [[DNAJC5]] (+0.64, fdr 1e-05), [[PPP2R5B]] (+0.64, fdr 7e-06); moves opposite to [[EWSR1]] (-0.62, fdr 1e-05), [[FUBP1]] (-0.59, fdr 1e-05), [[MTHFD1]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6305.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (MIA PaCa-2 2.99×, NCI-H1573 1.95×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 2.63×, A498 2.09×; ⚠ cell-cycle shift, explains ~6% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.0 | 0.037 | 25/47 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.34×** | +3.7 | 0.059 | 21/40 (NCI-H1573, HEC-1-A, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | 1.45× | +3.3 | 0.12 | 24/48 (LoVo, SNU-423, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | 1.28× | +3.3 | 0.12 | 23/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.19× | +3.2 | 0.12 | 20/48 (LS 180, A498, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.12 | 20/49 (MIA PaCa-2, NCI-H1573, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.27× | +3.1 | 0.15 | 23/48 (MIA PaCa-2, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6305.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.678×** | -4.9 | 6e-04 | 31/47 (C32, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.808×** | -3.9 | 0.025 | 26/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 5 µM |  | **0.602×** | -3.5 | 0.094 | 23/49 (NCI-H1573, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.761×** | -3.4 | 0.094 | 24/48 (C32, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | 0.621× | -3.2 | 0.12 | 21/48 (SK-MEL-2, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.622× | -3.2 | 0.12 | 19/49 (C32, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[olaparib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.785× | -3.1 | 0.14 | 16/48 (A-427, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6305. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 83.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -17.4) |
| [[AsPC-1 (line)]] | alt | 89.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 70.9 | 1 | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.95× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 111 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -15.0) |
| [[A-427 (line)]] | wt | 49.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.334× (z -8.5) ⚠ toxic |
| [[A498 (line)]] | wt | 37.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.9) ⚠ cell-cycle shift, explains ~6% of this change | — |
| [[BT-474 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -12.0) ⚠ toxic |
| [[HOP62 (line)]] | alt | 64.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -8.5) |
| [[HS-578T (line)]] | alt | 65.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -8.5) |
| [[LS 180 (line)]] | wt | 41.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.0) ⚠ cell-cycle shift, explains ~6% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 45.3 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.99× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 60.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 75.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6305), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9B]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[DNAJC5]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[PPP2R5B]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[MAP2K1]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[GUK1]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ARID3A]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SLC35E1]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[SEC61G]] | +0.60 | +0.63 / +0.57 | both halves | 8e-06 |  |
| [[IL17RA]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[MPG]] | +0.59 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[ORMDL2]] | +0.59 | +0.49 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EWSR1]] | -0.62 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[FUBP1]] | -0.59 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.58 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[BACE1-AS]] | -0.58 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[HNRNPD]] | -0.58 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[ILF3]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[DHX9]] | -0.56 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[PIGO]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[TBL1XR1]] | -0.55 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[SRSF1]] | -0.54 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ADGRA3]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[SMG7]] | -0.53 | -0.39 / -0.60 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.7, -14.6); signed map (-34.4, 19.2). **Vector** length 98.7, 29.0% of its response variance represented; |z| ≥ 3 in 593 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +4.3 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.0 | -4.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | -0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -0.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | glycolipid transfer protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:109,850,945-109,880,541 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glycolipid transfer protein family |
| Reactome | 2 pathways, smallest: Glycosphingolipid transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZD2](https://www.uniprot.org/uniprotkb/Q9NZD2) (Glycolipid transfer protein):

> Accelerates the intermembrane transfer of various glycolipids. Catalyzes the transfer of various glycosphingolipids between membranes but does not catalyze the transfer of phospholipids. May be involved in the intracellular translocation of glucosylceramides.

**Summary**, from NCBI Gene [51228](https://www.ncbi.nlm.nih.gov/gene/51228):

> The protein encoded by this gene is similar to bovine and porcine proteins which accelerate transfer of certain glycosphingolipids and glyceroglycolipids between membranes. It is thought to be a cytoplasmic protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24867) · Entrez [51228](https://www.ncbi.nlm.nih.gov/gene/51228) · UniProt [Q9NZD2](https://www.uniprot.org/uniprotkb/Q9NZD2) · Ensembl [ENSG00000139433](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139433)

## Data

Gene col 6305: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6305); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6305, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6305]; `tensor/DDL_lfc|DDL_z.npy` [6305]; `embed/gene_vectors.npy` [6305]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6305 or target_col == 6305). Every well: [[GLTP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLTP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
