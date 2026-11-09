---
symbol: "DNLZ"
type: "gene"
col: 13092
ensembl_id: "ENSG00000213221"
name: "DNL-type zinc finger"
location: "9q34.3"
module: 24
arm: "+"
pooled_cpm: 3.08
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# DNLZ

*DNL-type zinc finger* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.44× (z +7.8, q 4e-12, up in 12 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.84× (z +4.6, q 5e-04, up in 15 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPS9]] (+0.76, fdr 7e-06), [[SNHG9]] (+0.73, fdr 1e-05), [[UQCC3]] (+0.72, fdr 1e-05); moves opposite to [[NONO]] (-0.68, fdr 1e-05), [[SRP9]] (-0.64, fdr 7e-05), [[SPTBN1]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13092.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.44×** | +7.8 | 4e-12 | 12/18 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.44×** | +7.5 | 2e-11 | 2/5 (PANC-1, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.21×** | +7.1 | 3e-10 | 13/18 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +4.9 | 1e-04 | 18/29 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.11×** | +4.7 | 3e-04 | 9/19 (AsPC-1, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.84×** | +4.6 | 5e-04 | 15/25 (A549, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +4.3 | 0.002 | 2/6 (J82, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.005 | 13/35 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.31×** | +3.7 | 0.016 | 10/32 (SW480, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **2.27×** | +3.6 | 0.019 | 11/29 (MIA PaCa-2, AsPC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.2 | 0.065 | 8/31 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.66× | +3.0 | 0.11 | 9/32 (HT-29, LoVo, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 2.00× | +3.0 | 0.11 | 3/17 (SW480, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13092.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clofarabine (drug)]] 0.5 µM |  | 0.613× | -3.1 | 0.95 | 9/45 (HS-578T, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13092. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.951 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13092), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 13 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS9]] | +0.76 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[SNHG9]] | +0.73 | +0.49 / +0.75 | both halves | 1e-05 |  |
| [[UQCC3]] | +0.72 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[C1orf122]] | +0.70 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[RPP21]] | +0.69 | +0.54 / +0.77 | both halves | 1e-05 |  |
| [[ZNF593]] | +0.68 | +0.45 / +0.72 | both halves | 3e-05 |  |
| [[MRPL41]] ⚠ | +0.66 | +0.58 / +0.71 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RANGRF]] | +0.66 | +0.34 / +0.73 | both halves | 1e-04 |  |
| [[TMEM134]] | +0.64 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[LAMTOR4]] | +0.64 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[MRPS12]] | +0.64 | +0.30 / +0.70 | both halves | 2e-04 |  |
| [[DCTN6-DT]] | +0.64 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[CIAO2B]] | +0.63 | +0.46 / +0.68 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NONO]] | -0.68 | -0.49 / -0.71 | both halves | 1e-05 |  |
| [[SRP9]] | -0.64 | -0.38 / -0.66 | both halves | 7e-05 |  |
| [[SPTBN1]] | -0.63 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[EIF4H]] | -0.63 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[LIN7C]] | -0.63 | -0.39 / -0.68 | both halves | 5e-05 |  |
| [[HMGN1]] | -0.63 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[CBX5]] | -0.61 | -0.35 / -0.67 | both halves | 1e-04 |  |
| [[PRELID3B]] | -0.60 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.59 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[DHFR]] | -0.58 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[MYBL1]] | -0.57 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[HNRNPA3]] | -0.57 | -0.35 / -0.61 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.0, -20.3); signed map (-29.5, 8.4). **Vector** length 40.3, 5.14% of its response variance represented; |z| ≥ 3 in 637 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +7.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +4.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.4 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.2 | +2.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.7 |
|  | [[Decitabine (drug)]] 5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | DNL-type zinc finger |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,359,480-136,363,744 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RP11-413M3.2, ZIM17, bA413M3.2, TIMM15, HEP; previously C9orf151 |
| Gene groups (HGNC) | Zinc fingers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SXM8](https://www.uniprot.org/uniprotkb/Q5SXM8) (DNL-type zinc finger protein):

> May function as a co-chaperone towards HSPA9/mortalin which, by itself, is prone to self-aggregation.

**Summary**, from NCBI Gene [728489](https://www.ncbi.nlm.nih.gov/gene/728489):

> Enables protein folding chaperone. Involved in chaperone-mediated protein complex assembly. Is active in cytosol; mitochondrion; and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33879) · Entrez [728489](https://www.ncbi.nlm.nih.gov/gene/728489) · UniProt [Q5SXM8](https://www.uniprot.org/uniprotkb/Q5SXM8) · Ensembl [ENSG00000213221](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213221)

## Data

Gene col 13092: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13092); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13092, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13092]; `tensor/DDL_lfc|DDL_z.npy` [13092]; `embed/gene_vectors.npy` [13092]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13092 or target_col == 13092). Every well: [[DNLZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNLZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
