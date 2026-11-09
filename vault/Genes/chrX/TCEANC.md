---
symbol: "TCEANC"
type: "gene"
col: 10762
ensembl_id: "ENSG00000176896"
name: "transcription elongation factor A N-terminal and central domain containing"
location: "Xp22.2"
module: 12
arm: "+"
pooled_cpm: 2.46
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# TCEANC

*transcription elongation factor A N-terminal and central domain containing* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.00× (z +21.1, q 0e+00, up in 30 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.550× (z -6.5, q 6e-08, down in 15 of 44 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.648× (z -4.7, q 8e-04, down in 13 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00240]] (+0.73, fdr 7e-06), [[TEF]] (+0.69, fdr 7e-06), [[COQ5]] (+0.69, fdr 1e-05); moves opposite to [[BRI3BP]] (-0.68, fdr 2e-05), [[SNHG30]] (-0.64, fdr 1e-05), [[MFSD14B]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10762.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.00×** | +21.1 | 0e+00 | 30/31 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.62×** | +13.8 | 4e-41 | 25/31 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.62×** | +13.3 | 4e-38 | 33/37 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.87×** | +10.9 | 1e-25 | 9/15 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +8.4 | 5e-15 | 23/43 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.14×** | +8.2 | 2e-14 | 25/42 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +7.8 | 4e-13 | 18/44 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.6 | 2e-12 | 12/31 (NCI-H1792, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.01×** | +7.5 | 3e-12 | 18/40 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +7.1 | 5e-11 | 20/45 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +6.4 | 9e-09 | 0/0 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +5.9 | 1e-07 | 8/43 (NCI-H2347, SW1417, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +5.7 | 7e-07 | 8/42 (LoVo, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +5.1 | 1e-05 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.6 | 2e-04 | 13/38 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.51×** | +4.1 | 0.002 | 3/26 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.029 | 9/40 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.029 | 2/44 (NCI-H2347, A-172) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10762.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.550×** | -6.5 | 6e-08 | 15/44 (RPMI-7951, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.648×** | -4.7 | 8e-04 | 13/41 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.536×** | -3.5 | 0.082 | 4/22 (HS-578T, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.740× | -3.3 | 0.16 | 12/45 (HOP62, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | 0.580× | -3.1 | 0.24 | 6/31 (HOP62, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10762. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 5.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 4.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +9.5) | — |
| [[KATO III (line)]] | alt | 3.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +9.1) | — |
| [[A-172 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.868 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10762), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00240]] | +0.73 | +0.82 / +0.66 | both halves | 7e-06 |  |
| [[TEF]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[COQ5]] | +0.69 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[RAD52]] | +0.69 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[CLK4]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[HHLA3]] | +0.68 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[COMMD3]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[AMZ2P1-1]] | +0.67 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.67 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[GORAB]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ZNF385C]] | +0.66 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[LIPT1]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRI3BP]] | -0.68 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[SNHG30]] | -0.64 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[MFSD14B]] | -0.63 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[TUFM]] | -0.62 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[PMPCA]] | -0.62 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[ADAM15]] | -0.61 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[RNGTT]] | -0.60 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[PRIM2]] | -0.60 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[AHSA1]] | -0.60 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[TMEM97]] | -0.60 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TMED4]] | -0.59 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[HACD3]] | -0.59 | -0.57 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.613). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-28.9, 6.8); signed map (6.6, -20.6). **Vector** length 50.2, 6.36% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +21.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +13.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +7.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +5.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.0 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | transcription elongation factor A N-terminal and central domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:13,653,112-13,681,964 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC17403, TCEANC1 |
| Matched by | ensembl_id |

UniProt [Q8N8B7](https://www.uniprot.org/uniprotkb/Q8N8B7) carries no function annotation.

**Summary**, from NCBI Gene [170082](https://www.ncbi.nlm.nih.gov/gene/170082):

> Predicted to enable transcription elongation factor activity. Predicted to be involved in transcription elongation by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28277](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28277) · Entrez [170082](https://www.ncbi.nlm.nih.gov/gene/170082) · UniProt [Q8N8B7](https://www.uniprot.org/uniprotkb/Q8N8B7) · Ensembl [ENSG00000176896](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176896)

## Data

Gene col 10762: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10762); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10762, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10762]; `tensor/DDL_lfc|DDL_z.npy` [10762]; `embed/gene_vectors.npy` [10762]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10762 or target_col == 10762). Every well: [[TCEANC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCEANC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
