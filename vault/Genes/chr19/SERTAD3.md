---
symbol: "SERTAD3"
type: "gene"
col: 9492
ensembl_id: "ENSG00000167565"
name: "SERTA domain containing 3"
location: "19q13.2"
module: 41
arm: "+"
pooled_cpm: 6.06
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# SERTAD3

*SERTA domain containing 3* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.77× (z +11.3, q 6e-27, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.640× (z -4.9, q 7e-04, down in 16 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEF2D]] (+0.60, fdr 1e-05), [[NAB2]] (+0.58, fdr 1e-05), [[TBC1D10B]] (+0.58, fdr 2e-05); moves opposite to [[SUCLG2]] (-0.50, fdr 1e-04), [[NAE1]] (-0.48, fdr 3e-05), [[GCFC2]] (-0.48, fdr 2e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9492.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.77×** | +11.3 | 6e-27 | 42/45 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.94×** | +8.1 | 1e-13 | 28/42 (SW480, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +5.7 | 3e-06 | 19/42 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +5.2 | 2e-05 | 16/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +4.8 | 2e-04 | 16/37 (A498, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.003 | 13/46 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.091 | 14/45 (LoVo, SNU-1, …) | rises with dose | position effect removed |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | 1.32× | +3.2 | 0.11 | 8/44 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.21× | +3.1 | 0.13 | 13/42 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.31× | +3.0 | 0.15 | 10/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9492.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.640×** | -4.9 | 7e-04 | 16/39 (A498, J82, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.708×** | -3.7 | 0.034 | 14/46 (C-33 A, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.721×** | -3.7 | 0.034 | 8/44 (SNU-423, A498, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.723×** | -3.7 | 0.034 | 14/47 (A-427, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9492. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 8.41 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.150× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~5% of this change |
| [[C-33 A (line)]] | alt | 7.47 | 0 | 1 | — | [[RMC-6236 (drug)]] 0.05 µM 0.0561× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 7.65 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0732× (z -10.8) |
| [[SW480 (line)]] | alt | 4.86 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 25.4× (z +8.8) | — |
| [[A-172 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9492), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEF2D]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[NAB2]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TBC1D10B]] | +0.58 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[VPS18]] | +0.56 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[PEX13]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[MAP3K11]] | +0.53 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[NLGN2]] | +0.53 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[RNF31]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[PHF23]] | +0.52 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[NECTIN2]] | +0.52 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SKIC2]] | +0.51 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[SOX12]] | +0.51 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUCLG2]] | -0.50 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[NAE1]] | -0.48 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[GCFC2]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[NT5DC1]] | -0.47 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[METTL8]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ADK]] | -0.46 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TMA16]] | -0.45 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[MYO5C]] | -0.43 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[ME2]] | -0.43 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[NBEAP2]] | -0.43 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[DCAF17]] | -0.43 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[PRMT3]] | -0.42 | -0.49 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.220). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (22.0, -28.6); signed map (-28.3, 30.5). **Vector** length 66.3, 10.3% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +11.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +8.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.5 | +4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.2 | +2.6 |
| fall | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.9 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.3 | -2.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.8 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | SERTA domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,440,844-40,444,335 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RBT1 |
| Gene groups (HGNC) | SERTA domain containing |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJW9](https://www.uniprot.org/uniprotkb/Q9UJW9) (SERTA domain-containing protein 3):

> Antiviral interferon-stimulated protein that plays a role in innate immunity and in the suppression of viruses through different mechanisms. Plays a role in the late phase response of TLR-induced immune effector expression (By similarity). During influenza infection, interacts with PB2, PB1, and PA to disrupt the formation of the viral RdRp complex. Inhibits zika virus by interacting with the capsid protein in the nucleolus and reducing its abundance through proteasomal degradation. Strong …

**Summary**, from NCBI Gene [29946](https://www.ncbi.nlm.nih.gov/gene/29946):

> The protein encoded by this gene was identified in a yeast two-hybrid assay employing the second subunit of human replication protein A as bait. It is localized to the nucleus and its expression is significantly higher in cancer cell lines compared to normal cell lines. This protein has also been shown to be a strong transcriptional co-activator. Alternative splicing has been observed at this locus and two variants, both encoding the same protein, have been identified. [provided by RefSeq, Jul …

**Accessions** — [HGNC:17931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17931) · Entrez [29946](https://www.ncbi.nlm.nih.gov/gene/29946) · UniProt [Q9UJW9](https://www.uniprot.org/uniprotkb/Q9UJW9) · Ensembl [ENSG00000167565](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167565)

## Data

Gene col 9492: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9492); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9492, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9492]; `tensor/DDL_lfc|DDL_z.npy` [9492]; `embed/gene_vectors.npy` [9492]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9492 or target_col == 9492). Every well: [[SERTAD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERTAD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
