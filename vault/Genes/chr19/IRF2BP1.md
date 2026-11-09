---
symbol: "IRF2BP1"
type: "gene"
col: 9980
ensembl_id: "ENSG00000170604"
name: "interferon regulatory factor 2 binding protein 1"
location: "19q13.32"
module: 16
arm: "+"
pooled_cpm: 2.82
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# IRF2BP1

*interferon regulatory factor 2 binding protein 1* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.18× (z +10.1, q 3e-21, up in 22 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Brimonidine (drug)]] 0.5 µM in 1 line (HT-29 0.0690×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW1417 0.113×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (PANC-1 0.0659×; ⚠ cell-cycle shift, explains ~17% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C7orf25]] (+0.71, fdr 7e-06), [[RBM15B]] (+0.71, fdr 7e-06), [[SRCAP]] (+0.70, fdr 7e-06); moves opposite to [[UQCRH]] (-0.59, fdr 3e-05), [[DPM1]] (-0.57, fdr 1e-05), [[GNRH1]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +10.1 | 3e-21 | 22/36 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +8.3 | 3e-14 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +7.3 | 6e-11 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.02×** | +6.5 | 2e-08 | 8/18 (SW480, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +5.8 | 8e-07 | 17/44 (HEC-1-A, A549, …) | two highest doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +5.0 | 6e-05 | 4/44 (SHP-77, HCT15, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +4.8 | 1e-04 | 13/33 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +4.5 | 4e-04 | 3/16 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.65×** | +4.4 | 6e-04 | 11/39 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.1 | 0.003 | 5/47 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.21×** | +3.8 | 0.007 | 6/38 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.011 | 8/45 (LOX-IMVI, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.011 | 5/45 (A549, NCI-H460, …) | top dose only | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.025 | 5/30 (A498, NCI-H1792, …) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.026 | 7/45 (Panc 03.27, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.042 | 4/42 (J82, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.47×** | +3.2 | 0.048 | 2/44 (COLO 205, SW480) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.0 | 0.071 | 4/40 (LS 180, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.087 | 5/45 (SW1417, NCI-H2347, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9980.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Brimonidine (drug)]] 0.5 µM in 1 line (HT-29 0.0690×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW1417 0.113×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (PANC-1 0.0659×; ⚠ cell-cycle shift, explains ~17% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.671× | -3.7 | 0.13 | 15/44 (CFPAC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.684× | -3.3 | 0.27 | 10/40 (SHP-77, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.713× | -3.1 | 0.28 | 7/38 (A549, RPMI-7951, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.790× | -3.1 | 0.28 | 4/45 (PANC-1, J82, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 4.62 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0690× (z -9.6) |
| [[PANC-1 (line)]] | alt | 1.67 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0659× (z -8.9) ⚠ cell-cycle shift, explains ~17% of this change |
| [[SW1417 (line)]] | alt | 6.16 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.113× (z -8.9) |
| [[A-172 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.946 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C7orf25]] | +0.71 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[RBM15B]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[SRCAP]] | +0.70 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[PRRC2A]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ZNF574]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PABIR1]] | +0.68 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[ZNF614]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[ZNF747]] | +0.66 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ZNF687]] | +0.66 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[CHTOP]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[RTL6]] | +0.66 | +0.69 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRH]] | -0.59 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[DPM1]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[GNRH1]] | -0.57 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[RNF149]] | -0.57 | -0.67 / -0.39 | both halves | 5e-05 | same gene group |
| [[MED31]] | -0.56 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[RAB6A]] | -0.56 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[RARS2]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[GPR89B]] | -0.54 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[GPR89A]] | -0.54 | -0.56 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.707). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.5, 11.8); signed map (1.3, -32.0). **Vector** length 45.8, 4.97% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +10.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.2 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +2.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.1 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | +0.0 |
|  | [[Fumaric acid (drug)]] 0.5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | interferon regulatory factor 2 binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,883,608-45,886,141 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434M154, IRF-2BP1 |
| Gene groups (HGNC) | RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IU81](https://www.uniprot.org/uniprotkb/Q8IU81) (Interferon regulatory factor 2-binding protein 1):

> Acts as a transcriptional corepressor in a IRF2-dependent manner; this repression is not mediated by histone deacetylase activities. May act as an E3 ligase towards JDP2, enhancing its polyubiquitination. Represses ATF2-dependent transcriptional activation.

**Summary**, from NCBI Gene [26145](https://www.ncbi.nlm.nih.gov/gene/26145):

> Enables transcription corepressor activity and ubiquitin protein ligase activity. Involved in protein polyubiquitination. Acts upstream of or within negative regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21728) · Entrez [26145](https://www.ncbi.nlm.nih.gov/gene/26145) · UniProt [Q8IU81](https://www.uniprot.org/uniprotkb/Q8IU81) · Ensembl [ENSG00000170604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170604)

## Data

Gene col 9980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9980); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9980]; `tensor/DDL_lfc|DDL_z.npy` [9980]; `embed/gene_vectors.npy` [9980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9980 or target_col == 9980). Every well: [[IRF2BP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRF2BP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
