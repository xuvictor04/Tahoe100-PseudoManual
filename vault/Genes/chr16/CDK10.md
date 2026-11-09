---
symbol: "CDK10"
type: "gene"
col: 11661
ensembl_id: "ENSG00000185324"
name: "cyclin dependent kinase 10"
location: "16q24.3"
module: 2
arm: "+"
pooled_cpm: 15.11
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CDK10

*cyclin dependent kinase 10* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.38× (z +5.5, q 2e-05, up in 21 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.47× (z +4.7, q 9e-04, up in 13 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.526× (z -5.7, q 6e-06, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (MIA PaCa-2 0.0623×, NCI-H1573 0.199×, NCI-H1792 0.227×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change); [[Hesperidin (drug)]] 5 µM in 1 line (AsPC-1 0.0908×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (H4 0.165×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Hesperidin (drug)]] 0.05 µM in 1 line (COLO 205 0.237×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TELO2]] (+0.72, fdr 7e-06), [[ZMYND19]] (+0.65, fdr 7e-06), [[WDR90]] (+0.62, fdr 7e-06); moves opposite to [[CFL2]] (-0.55, fdr 1e-05), [[TOR1AIP2]] (-0.51, fdr 2e-05), [[DSG2]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.38×** | +5.5 | 2e-05 | 21/48 (NCI-H1573, LoVo, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +4.7 | 9e-04 | 13/43 (NCI-H1792, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.29×** | +4.1 | 0.006 | 14/41 (A-427, NCI-H1792, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.1 | 0.006 | 1/48 (hTERT-HPNE) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.27×** | +4.0 | 0.006 | 14/47 (SNU-423, NCI-H460, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.018 | 11/43 (HOP62, NCI-H2030, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.043 | 8/44 (HCT15, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.15× | +3.4 | 0.046 | 14/47 (NCI-H1792, SHP-77, …) | top dose only |  |
| [[Bergenin (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.094 | 8/46 (SW480, SW48, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | 1.19× | +3.0 | 0.15 | 7/46 (NCI-H1573, A549, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11661.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (MIA PaCa-2 0.0623×, NCI-H1573 0.199×, NCI-H1792 0.227×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change); [[Hesperidin (drug)]] 5 µM in 1 line (AsPC-1 0.0908×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (H4 0.165×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Hesperidin (drug)]] 0.05 µM in 1 line (COLO 205 0.237×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.526×** | -5.7 | 6e-06 | 21/48 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.676× | -3.5 | 0.14 | 13/44 (HS-578T, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.869× | -3.4 | 0.14 | 16/47 (A-172, COLO 205, …) | all doses, stronger at high dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 17.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +10.8) ⚠ cell-cycle shift, explains ~57% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[AsPC-1 (line)]] | alt | 6.15 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0908× (z -9.6) |
| [[COLO 205 (line)]] | alt | 26.5 | 0 | 1 | — | [[Hesperidin (drug)]] 0.05 µM 0.237× (z -8.6) |
| [[H4 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.165× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0623× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[A-172 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TELO2]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[ZMYND19]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[WDR90]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SPOUT1]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[DUS1L]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TONSL]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[RHOT2]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CHTF18]] | +0.57 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[SPPL2B]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[SMPD4BP]] | +0.56 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[ADCK5]] | +0.56 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[FHIP2B]] | +0.55 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL2]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[TOR1AIP2]] | -0.51 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[DSG2]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[COMMD8]] | -0.49 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[AFF4]] | -0.47 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[NCOA4]] | -0.47 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CLU]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[SMARCA5]] | -0.47 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[SDCBP]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SCOC]] | -0.46 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[TWF1]] | -0.46 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-26.5, -45.6); signed map (-47.7, -15.8). **Vector** length 62.3, 9.43% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +4.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | +2.1 | +3.0 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.0 | +3.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | +2.0 | +4.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +3.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,680,737-89,696,354 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PISSLRE |
| Gene groups (HGNC) | Cyclin dependent kinases; Spliceosomal C complex; Spliceosomal P complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15131](https://www.uniprot.org/uniprotkb/Q15131) (Cyclin-dependent kinase 10):

> Cyclin-dependent kinase that phosphorylates the transcription factor ETS2 (in vitro) and positively controls its proteasomal degradation (in cells). Involved in the regulation of actin cytoskeleton organization through the phosphorylation of actin dynamics regulators such as PKN2. Is a negative regulator of ciliogenesis through phosphorylation of PKN2 and promotion of RhoA signaling.

**Summary**, from NCBI Gene [8558](https://www.ncbi.nlm.nih.gov/gene/8558):

> The protein encoded by this gene belongs to the CDK subfamily of the Ser/Thr protein kinase family. The CDK subfamily members are highly similar to the gene products of S. cerevisiae cdc28, and S. pombe cdc2, and are known to be essential for cell cycle progression. This kinase has been shown to play a role in cellular proliferation and its function is limited to cell cycle G2-M phase. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, …

**Accessions** — [HGNC:1770](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1770) · Entrez [8558](https://www.ncbi.nlm.nih.gov/gene/8558) · UniProt [Q15131](https://www.uniprot.org/uniprotkb/Q15131) · Ensembl [ENSG00000185324](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185324)

## Data

Gene col 11661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11661); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11661]; `tensor/DDL_lfc|DDL_z.npy` [11661]; `embed/gene_vectors.npy` [11661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11661 or target_col == 11661). Every well: [[CDK10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
