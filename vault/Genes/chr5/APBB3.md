---
symbol: "APBB3"
type: "gene"
col: 3431
ensembl_id: "ENSG00000113108"
name: "amyloid beta precursor protein binding family B member 3"
location: "5q31.3"
module: 2
arm: "+"
pooled_cpm: 6.21
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# APBB3

*amyloid beta precursor protein binding family B member 3* — 5q31.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 4.09×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.413× (z -7.9, q 1e-12, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFEMP2]] (+0.64, fdr 1e-05), [[AAAS]] (+0.64, fdr 2e-05), [[RHOT2]] (+0.63, fdr 9e-06); moves opposite to [[GNAQ]] (-0.52, fdr 2e-05), [[DPY19L1P1]] (-0.51, fdr 4e-05), [[ITFG1]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3431.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 4.09×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +5.0 | 4e-04 | 13/48 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 2.06× | +3.4 | 0.17 | 4/17 (LoVo, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.46× | +3.3 | 0.17 | 14/42 (NCI-H1792, HCT15, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.45× | +3.0 | 0.30 | 9/41 (KATO III, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.27× | +3.0 | 0.30 | 13/47 (HT-29, A498, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3431.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.413×** | -7.9 | 1e-12 | 35/48 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.422×** | -7.7 | 3e-12 | 22/40 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.516×** | -6.0 | 5e-07 | 27/46 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.553×** | -5.1 | 3e-05 | 22/41 (C-33 A, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -5.1 | 3e-05 | 25/43 (CFPAC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.568×** | -5.1 | 3e-05 | 25/46 (NCI-H1792, RKO, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.565×** | -4.9 | 6e-05 | 22/37 (J82, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.603×** | -4.6 | 4e-04 | 25/47 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.707× | -3.1 | 0.11 | 11/47 (NCI-H23, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | 0.710× | -3.1 | 0.11 | 13/46 (Panc 03.27, A-172, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.705× | -3.0 | 0.12 | 21/42 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3431. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 7.55 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0794× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 6.77 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Canagliflozin (drug)]] 0.05 µM 0.149× (z -8.7) |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0846× (z -8.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 6.93 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0953× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 7.22 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -9.6) ⚠ toxic |
| [[LoVo (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[NCI-H1792 (line)]] | alt | 6.66 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0561× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 5.80 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0675× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 4.77 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.120× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 7.51 | 0 | 1 | — | [[crizotinib (drug)]] 0.05 µM 0.0559× (z -8.7) |
| [[SNU-423 (line)]] | alt | 7.04 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0796× (z -10.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 7.40 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0926× (z -10.4) |
| [[SW480 (line)]] | alt | 4.70 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -9.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3431), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFEMP2]] | +0.64 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[AAAS]] | +0.64 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[RHOT2]] | +0.63 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[PLXNA3]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[SKIC2]] | +0.63 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[GPSM1]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[PLA2G4B]] | +0.61 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[BAIAP3]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[KLHL26]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[EEF1A2]] | +0.59 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[TCIRG1]] | +0.59 | +0.41 / +0.61 | both halves | 4e-05 | same gene group |
| [[ARFIP2]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAQ]] | -0.52 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[DPY19L1P1]] | -0.51 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[ITFG1]] | -0.50 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ARID1B]] | -0.50 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[TCF12]] | -0.50 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[ARID2]] | -0.49 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[ARHGEF11]] | -0.49 | -0.43 / -0.32 | both halves | 2e-04 | same gene group |
| [[FBXL17]] | -0.49 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[SNTB2]] | -0.49 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[TBC1D5]] | -0.48 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.511). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (11.2, -3.6); signed map (-29.1, 1.2). **Vector** length 68.9, 10.7% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.5 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.7 | -0.6 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.7 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +3.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | -6.0 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.8 | -1.2 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | amyloid beta precursor protein binding family B member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,558,268-140,564,781 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FE65L2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O95704](https://www.uniprot.org/uniprotkb/O95704) (Amyloid-beta A4 precursor protein-binding family B member 3):

> May modulate the internalization of amyloid-beta precursor protein.

**Summary**, from NCBI Gene [10307](https://www.ncbi.nlm.nih.gov/gene/10307):

> The protein encoded by this gene is a member of the APBB protein family. It is found in the cytoplasm and binds to the intracellular domain of the Alzheimer's disease beta-amyloid precursor protein (APP) as well as to other APP-like proteins. It is thought that the protein encoded by this gene may modulate the internalization of APP. Multiple transcript variants encoding several different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20708) · Entrez [10307](https://www.ncbi.nlm.nih.gov/gene/10307) · UniProt [O95704](https://www.uniprot.org/uniprotkb/O95704) · Ensembl [ENSG00000113108](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113108)

## Data

Gene col 3431: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3431); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3431, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3431]; `tensor/DDL_lfc|DDL_z.npy` [3431]; `embed/gene_vectors.npy` [3431]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3431 or target_col == 3431). Every well: [[APBB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APBB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
