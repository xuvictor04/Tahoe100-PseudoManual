---
symbol: "TMED7-TICAM2"
type: "gene"
col: 14748
ensembl_id: "ENSG00000251201"
name: "TMED7-TICAM2 readthrough"
location: "5q22.3"
module: 179
arm: "+"
pooled_cpm: 19.26
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# TMED7-TICAM2

*TMED7-TICAM2 readthrough* — 5q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.25× (z +10.7, q 5e-24, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.429× (z -10.8, q 3e-24, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TICAM2]] (+0.80, fdr 7e-06, ⚠ same locus), [[PCGF3-AS1]] (+0.74, fdr 7e-06), [[GOSR2]] (+0.72, fdr 7e-06), [[HYPK]] (+0.71, fdr 7e-06); moves opposite to [[C2CD5]] (-0.61, fdr 1e-05), [[TIGD2]] (-0.57, fdr 1e-05), [[CENPS]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14748.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.25×** | +10.7 | 5e-24 | 42/48 (SW480, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.8 | 2e-12 | 34/47 (AsPC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +6.2 | 1e-07 | 6/48 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +5.8 | 1e-06 | 17/36 (NCI-H1573, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +4.8 | 2e-04 | 22/46 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 2e-04 | 22/48 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +4.6 | 3e-04 | 21/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +4.1 | 0.003 | 20/44 (SK-MEL-2, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.7 | 0.012 | 12/27 (NCI-H1573, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.090 | 12/47 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 1.26× | +3.0 | 0.13 | 14/47 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14748.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.429×** | -10.8 | 3e-24 | 37/47 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.571×** | -10.5 | 2e-23 | 33/47 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.607×** | -6.4 | 4e-08 | 29/48 (SK-MEL-2, NCI-H1573, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.684×** | -5.0 | 7e-05 | 26/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.608×** | -3.5 | 0.063 | 16/46 (NCI-H1792, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.778×** | -3.3 | 0.066 | 13/48 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.779×** | -3.3 | 0.066 | 13/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.620×** | -3.3 | 0.066 | 17/46 (SHP-77, SNU-1, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.785×** | -3.2 | 0.079 | 13/48 (KATO III, H4, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.786×** | -3.2 | 0.079 | 8/48 (LS 180, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 18.2 | 1 | 1 | [[Auranofin (drug)]] 5 µM 4.78× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 22.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.1) |
| [[A498 (line)]] | wt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 32.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -9.6) |
| [[HOP62 (line)]] | alt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.3) |
| [[Hs 766T (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 50.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.34× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.8) |
| [[PANC-1 (line)]] | alt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -12.2) |
| [[RKO (line)]] | wt | 18.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.115× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 26.2 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.187× (z -10.6) |
| [[SW48 (line)]] | wt | 13.3 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0745× (z -9.3) |
| [[SW480 (line)]] | alt | 16.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.67× (z +11.0) | — |
| [[A-172 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14748), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TICAM2]] | +0.80 | +0.77 / +0.84 | both halves | 7e-06 | STRING 800; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PCGF3-AS1]] | +0.74 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[GOSR2]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[HYPK]] | +0.71 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[CRYBB2P1-1]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[SURF4]] | +0.70 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[CDC26]] | +0.69 | +0.57 / +0.72 | both halves | 9e-06 |  |
| [[CDC20-DT]] | +0.69 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[CAPN10-DT]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[CHST7]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[WDR49]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[PPP1R32]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[GOLT1B]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2CD5]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[TIGD2]] | -0.57 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[CENPS]] | -0.55 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[COMMD8]] | -0.55 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[DCLRE1A]] | -0.54 | -0.56 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.729). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (17.9, -28.4); signed map (-46.1, 10.7). **Vector** length 109, 25.8% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.7 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +4.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +2.6 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +0.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.1 | -10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.7 | -6.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | -3.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.9 | -3.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | TMED7-TICAM2 readthrough |
| Locus type | readthrough (other) |
| Location | 5q22.3 — chr5:115,578,642-115,626,161 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100302736](https://www.ncbi.nlm.nih.gov/gene/100302736):

> This locus represents naturally occurring read-through transcription between the neighboring transmembrane emp24 protein transport domain containing 7 (TMED7) and toll-like receptor adaptor molecule 2 (TICAM2) genes. Alternative splicing results in multiple transcript variants, one of which encodes a fusion protein that shares sequence identity with the products of each individual gene. This fusion product functions to negatively regulate the adaptor MyD88-independent toll-like receptor 4 …

**Accessions** — [HGNC:33945](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33945) · Entrez [100302736](https://www.ncbi.nlm.nih.gov/gene/100302736) · Ensembl [ENSG00000251201](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251201)

## Data

Gene col 14748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14748); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14748, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14748]; `tensor/DDL_lfc|DDL_z.npy` [14748]; `embed/gene_vectors.npy` [14748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14748 or target_col == 14748). Every well: [[TMED7-TICAM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMED7-TICAM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
