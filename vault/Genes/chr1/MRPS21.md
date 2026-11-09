---
symbol: "MRPS21"
type: "gene"
col: 15492
ensembl_id: "ENSG00000266472"
name: "mitochondrial ribosomal protein S21"
location: "1q21.2"
module: 54
arm: "+"
pooled_cpm: 35.5
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# MRPS21

*mitochondrial ribosomal protein S21* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.43× (z +8.3, q 5e-14, up in 42 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 3.87×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 3.94×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 4.13×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.568× (z -7.5, q 4e-11, down in 37 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (Panc 03.27 0.302×, SNU-1 0.270×, C-33 A 0.335×); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.0618×); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.228×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNU13]] (+0.75, fdr 7e-06), [[RBIS]] (+0.70, fdr 1e-05), [[SF3B6]] (+0.69, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.58, fdr 3e-05), [[SEPTIN11]] (-0.56, fdr 3e-05), [[MAPRE1]] (-0.55, fdr 3e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15492.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 3.87×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 3.94×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 4.13×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.43×** | +8.3 | 5e-14 | 42/46 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.84×** | +5.5 | 1e-05 | 29/39 (Hs 766T, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.71×** | +4.2 | 0.005 | 26/42 (Hs 766T, HT-29, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.55×** | +4.1 | 0.005 | 31/46 (HEC-1-A, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.1 | 0.005 | 33/46 (NCI-H1573, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[vincristine (drug)]] 0.5 µM |  | 1.92× | +3.2 | 0.13 | 26/47 (NCI-H460, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.88× | +3.1 | 0.15 | 24/45 (LoVo, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15492.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (Panc 03.27 0.302×, SNU-1 0.270×, C-33 A 0.335×); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.0618×); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.228×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.568×** | -7.5 | 4e-11 | 37/47 (Panc 03.27, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.691× | -3.5 | 0.14 | 26/48 (BT-474, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15492. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 49.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.0) |
| [[Hs 766T (line)]] | wt | 43.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.94× (z +8.5) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -10.9) |
| [[SNU-1 (line)]] | wt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -9.1) |
| [[SW48 (line)]] | wt | 21.5 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0618× (z -11.0) |
| [[SW480 (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A-172 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15492), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNU13]] | +0.75 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[RBIS]] | +0.70 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[SF3B6]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[CTU1]] | +0.67 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[RPS26]] | +0.66 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[NCBP2AS2]] | +0.65 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[SLIRP]] | +0.64 | +0.41 / +0.67 | both halves | 4e-05 | STRING 418 |
| [[SELENOH]] | +0.63 | +0.40 / +0.75 | both halves | 5e-05 |  |
| [[CHCHD5]] | +0.63 | +0.34 / +0.70 | both halves | 1e-04 |  |
| [[ATP5MJ]] | +0.62 | +0.41 / +0.74 | both halves | 4e-05 |  |
| [[DHX57]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ATP5ME]] | +0.62 | +0.44 / +0.71 | both halves | 3e-05 | STRING 707 |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.58 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[SEPTIN11]] | -0.56 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[MAPRE1]] | -0.55 | -0.29 / -0.67 | both halves | 3e-04 |  |
| [[TWF1]] | -0.54 | -0.29 / -0.67 | both halves | 2e-04 |  |
| [[ZNF664]] | -0.53 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[MOB1A]] | -0.53 | -0.40 / -0.60 | both halves | 4e-05 |  |
| [[CHRAC1]] | -0.53 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[UBE2A]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[PGRMC1]] | -0.53 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[NID1]] | -0.53 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[SCRN1]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[HNRNPK]] | -0.52 | -0.32 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.6, -24.1); signed map (-35.0, 6.3). **Vector** length 62.5, 16.1% of its response variance represented; |z| ≥ 3 in 435 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -1.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | -0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.7 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.6 | +1.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.6 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -2.7 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -2.1 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -1.8 | +4.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.6 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:150,293,861-150,308,979 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bS21m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [P82921](https://www.uniprot.org/uniprotkb/P82921) carries no function annotation.

**Summary**, from NCBI Gene [54460](https://www.ncbi.nlm.nih.gov/gene/54460):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14046) · Entrez [54460](https://www.ncbi.nlm.nih.gov/gene/54460) · UniProt [P82921](https://www.uniprot.org/uniprotkb/P82921) · Ensembl [ENSG00000266472](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266472)

## Data

Gene col 15492: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15492); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15492, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15492]; `tensor/DDL_lfc|DDL_z.npy` [15492]; `embed/gene_vectors.npy` [15492]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15492 or target_col == 15492). Every well: [[MRPS21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
