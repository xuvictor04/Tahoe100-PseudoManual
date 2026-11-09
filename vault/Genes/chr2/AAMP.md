---
symbol: "AAMP"
type: "gene"
col: 4835
ensembl_id: "ENSG00000127837"
name: "angio associated migratory cell protein"
location: "2q35"
module: 76
arm: "+"
pooled_cpm: 42.1
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# AAMP

*angio associated migratory cell protein* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.92× (z +8.6, q 6e-15, up in 43 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.146×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.427×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCHSD1]] (+0.61, fdr 4e-05), [[SPSB3]] (+0.60, fdr 1e-05), [[CDC34]] (+0.60, fdr 1e-05); moves opposite to [[TIA1]] (-0.58, fdr 4e-05), [[SENP1]] (-0.57, fdr 3e-05), [[POGLUT3]] (-0.57, fdr 3e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4835.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +8.6 | 6e-15 | 43/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.90×** | +7.7 | 4e-12 | 39/47 (A-427, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +7.5 | 1e-11 | 42/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.66×** | +6.6 | 5e-09 | 40/48 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.69×** | +6.6 | 5e-09 | 27/40 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.60×** | +6.2 | 6e-08 | 35/47 (PANC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +5.7 | 7e-07 | 39/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.56×** | +5.4 | 5e-06 | 30/43 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.4 | 5e-06 | 28/46 (NCI-H2030, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.45×** | +4.6 | 2e-04 | 29/47 (NCI-H460, C32, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.28×** | +4.6 | 2e-04 | 27/48 (A-427, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +4.3 | 1e-03 | 30/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +4.1 | 0.002 | 28/48 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.34×** | +3.9 | 0.005 | 28/46 (Panc 03.27, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.31×** | +3.5 | 0.015 | 24/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.028 | 21/47 (HOP62, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4835.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.146×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.427×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | 0.837× | -3.2 | 0.38 | 20/48 (LoVo, COLO 205, …) | inconsistent across doses |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.846× | -3.1 | 0.38 | 17/48 (LS 180, RKO, …) | top dose only | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.847× | -3.1 | 0.38 | 10/48 (LS 180, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4835. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 47.2 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.84× (z +10.1) | — |
| [[A-427 (line)]] | wt | 36.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 39.3 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.69× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 52.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4835), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHSD1]] | +0.61 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[SPSB3]] | +0.60 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CDC34]] | +0.60 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[ABTB1]] | +0.60 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[MOB2]] | +0.59 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[RAB40B]] | +0.57 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[FBRSL1]] | +0.57 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[BICD2]] | +0.57 | +0.52 / +0.35 | both halves | 1e-04 |  |
| [[ORMDL3]] | +0.55 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[HDAC11]] | +0.55 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[DOK4]] | +0.55 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[SEMA6C]] | +0.55 | +0.37 / +0.44 | both halves | 8e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.58 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SENP1]] | -0.57 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[POGLUT3]] | -0.57 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[FAM111A]] | -0.55 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[LACTB2]] | -0.53 | -0.46 / -0.21 | both halves | 7e-04 |  |
| [[TLCD4-RWDD3]] | -0.53 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[LGALSL-DT]] | -0.52 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[VEZF1]] | -0.52 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[DPY19L2P2-1]] | -0.51 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[AGL]] | -0.51 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[CFAP418]] | -0.51 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[ZNF681]] | -0.51 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.2, -44.0); signed map (-20.2, 11.7). **Vector** length 71.9, 17.5% of its response variance represented; |z| ≥ 3 in 721 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +8.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.9 | +5.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.7 | +6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.6 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +4.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.6 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +0.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -0.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.8 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | angio associated migratory cell protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:218,264,129-218,270,178 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 10 pathways, smallest: Thromboxane signalling through TP receptor; Signal amplification; NOD1/2 Signaling Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13685](https://www.uniprot.org/uniprotkb/Q13685) (Angio-associated migratory cell protein):

> Plays a role in angiogenesis and cell migration. In smooth muscle cell migration, may act through the RhoA pathway.

**Summary**, from NCBI Gene [14](https://www.ncbi.nlm.nih.gov/gene/14):

> The gene is a member of the immunoglobulin superfamily. The encoded protein is associated with angiogenesis, with potential roles in endothelial tube formation and the migration of endothelial cells. It may also regulate smooth muscle cell migration via the RhoA pathway. The encoded protein can bind to heparin and may mediate heparin-sensitive cell adhesion. [provided by RefSeq, Oct 2014]

**Accessions** — [HGNC:18](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18) · Entrez [14](https://www.ncbi.nlm.nih.gov/gene/14) · UniProt [Q13685](https://www.uniprot.org/uniprotkb/Q13685) · Ensembl [ENSG00000127837](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127837)

## Data

Gene col 4835: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4835); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4835, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4835]; `tensor/DDL_lfc|DDL_z.npy` [4835]; `embed/gene_vectors.npy` [4835]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4835 or target_col == 4835). Every well: [[AAMP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AAMP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
