---
symbol: "PDCD2"
type: "gene"
col: 999
ensembl_id: "ENSG00000071994"
name: "programmed cell death 2"
location: "6q27"
module: 1
arm: "+"
pooled_cpm: 20.63
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PDCD2

*programmed cell death 2* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.60× (z +12.7, q 3e-34, up in 36 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.39× (z +4.4, q 0.001, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.708× (z -6.5, q 6e-08, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIOX2]] (+0.74, fdr 7e-06), [[DPH5]] (+0.70, fdr 7e-06), [[POGK]] (+0.70, fdr 7e-06); moves opposite to [[HLA-A]] (-0.57, fdr 2e-05), [[GNAS]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 999.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +12.7 | 3e-34 | 36/41 (NCI-H1792, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +10.9 | 2e-25 | 26/31 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +9.6 | 1e-19 | 32/37 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +7.5 | 7e-12 | 36/44 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +5.9 | 4e-07 | 24/44 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.4 | 0.001 | 23/47 (SHP-77, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.1 | 0.003 | 16/45 (SNU-423, J82, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +3.9 | 0.008 | 18/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.079 | 9/44 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.093 | 9/45 (PANC-1, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.094 | 10/45 (PANC-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.26×** | +3.1 | 0.094 | 11/47 (PANC-1, COLO 205, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.096 | 7/47 (SW480, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 1.54× | +3.0 | 0.11 | 9/46 (NCI-H1792, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 999.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -6.5 | 6e-08 | 26/47 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.643×** | -5.9 | 1e-06 | 28/47 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.676×** | -5.2 | 4e-05 | 25/47 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.761×** | -5.1 | 4e-05 | 24/47 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -4.7 | 3e-04 | 24/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.703×** | -4.7 | 3e-04 | 27/46 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.636× | -3.1 | 0.14 | 9/45 (CHP-212, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 999. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 34.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -18.7) |
| [[SNU-423 (line)]] | alt | 23.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.12× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 27.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.4) |
| [[LS 180 (line)]] | wt | 27.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.19× (z +10.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.121× (z -9.4) ⚠ toxic |
| [[LoVo (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +8.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 24.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -9.1) |
| [[PANC-1 (line)]] | alt | 40.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -11.0) |
| [[A-172 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 999), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIOX2]] | +0.74 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[DPH5]] | +0.70 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[POGK]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[PGAM5]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ATIC]] | +0.67 | +0.76 / +0.57 | both halves | 8e-06 |  |
| [[IFRD2]] | +0.66 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[NLE1]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[MRPL3]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[TMEM33]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[TXNRD3]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[MAPKAPK3]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-A]] | -0.57 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[GNAS]] | -0.56 | -0.53 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.7, -37.9); signed map (-0.4, -40.1). **Vector** length 64.8, 12.4% of its response variance represented; |z| ≥ 3 in 664 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +3.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.7 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +2.4 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -6.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | programmed cell death 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:170,575,295-170,584,692 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZMYND7, RP8 |
| Gene groups (HGNC) | Zinc fingers MYND-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16342](https://www.uniprot.org/uniprotkb/Q16342) (uS5 assembly chaperone PDCD2):

> Chaperone for ribosomal protein uS5; cotranslationally associates with uS5 and accompanies the ribosomal protein to assembly sites in the nucleus; appears to function redundantly to PDCD2L.

**Summary**, from NCBI Gene [5134](https://www.ncbi.nlm.nih.gov/gene/5134):

> This gene encodes a nuclear protein expressed in a variety of tissues. Expression of this gene has been shown to be repressed by B-cell CLL/lymphoma 6 (BCL6), a transcriptional repressor required for lymph node germinal center development, suggesting that BCL6 regulates apoptosis by its effects on this protein. Alternative splicing results in multiple transcript variants and pseudogenes have been identified on chromosomes 9 and 12. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:8762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8762) · Entrez [5134](https://www.ncbi.nlm.nih.gov/gene/5134) · UniProt [Q16342](https://www.uniprot.org/uniprotkb/Q16342) · Ensembl [ENSG00000071994](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071994)

## Data

Gene col 999: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 999); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 999, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 999]; `tensor/DDL_lfc|DDL_z.npy` [999]; `embed/gene_vectors.npy` [999]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 999 or target_col == 999). Every well: [[PDCD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
