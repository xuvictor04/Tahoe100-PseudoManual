---
symbol: "ZBTB39"
type: "gene"
col: 9374
ensembl_id: "ENSG00000166860"
name: "zinc finger and BTB domain containing 39"
location: "12q13.3"
module: 7
arm: "+"
pooled_cpm: 8.41
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ZBTB39

*zinc finger and BTB domain containing 39* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.87× (z +7.6, q 2e-11, up in 24 of 34 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.43× (z +6.3, q 6e-08, up in 19 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.612× (z -6.2, q 2e-07, down in 20 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.798× (z -4.1, q 0.013, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 0.198×, LoVo 0.222×, NCI-H2030 0.175×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.0760×, A549 0.122×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF746]] (+0.69, fdr 7e-06), [[POGK]] (+0.68, fdr 7e-06), [[FEM1B]] (+0.66, fdr 1e-05); moves opposite to [[PRKCA-AS1]] (-0.56, fdr 3e-05), [[LINC01019]] (-0.56, fdr 7e-05), [[EHBP1-AS1]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9374.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +7.6 | 2e-11 | 24/34 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +6.3 | 6e-08 | 19/43 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.35×** | +5.3 | 2e-05 | 16/47 (A498, hTERT-HPNE, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +4.8 | 3e-04 | 14/47 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +3.9 | 0.010 | 8/47 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.011 | 10/47 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.033 | 16/44 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.054 | 8/46 (SNU-1, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.084 | 9/46 (SW480, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.29× | +3.1 | 0.11 | 8/44 (BT-474, HT-29, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 1.60× | +3.1 | 0.11 | 2/28 (Panc 03.27, A498) | inconsistent across doses | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9374.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 0.198×, LoVo 0.222×, NCI-H2030 0.175×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.0760×, A549 0.122×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.612×** | -6.2 | 2e-07 | 20/34 (NCI-H2030, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.798×** | -4.1 | 0.013 | 16/48 (SK-MEL-2, SW1417, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -3.9 | 0.018 | 18/46 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.752×** | -3.5 | 0.068 | 10/15 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.715× | -3.0 | 0.26 | 11/41 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0760× (z -14.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 8.86 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[NCI-H1573 (line)]] | alt | 8.38 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[A-172 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF746]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 | same gene group |
| [[POGK]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[FEM1B]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[MANBAL]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[ZBTB24]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 | same gene group |
| [[DNAJC14]] | +0.63 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[ZSCAN32]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 | same gene group |
| [[ATMIN]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 | same gene group |
| [[ZNF845]] | +0.61 | +0.57 / +0.60 | both halves | 9e-06 | same gene group |
| [[ZNF354B]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 | same gene group |
| [[ZNF649]] | +0.60 | +0.55 / +0.65 | both halves | 1e-05 | same gene group |
| [[ZFP62]] | +0.60 | +0.50 / +0.66 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKCA-AS1]] | -0.56 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[LINC01019]] | -0.56 | -0.38 / -0.60 | both halves | 7e-05 |  |
| [[EHBP1-AS1]] | -0.50 | -0.43 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.532). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-34.4, 11.3); signed map (-1.6, -33.9). **Vector** length 61.2, 8.60% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | +7.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.9 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.3 | +4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.7 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.6 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.3 | +0.4 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.6 | -6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -2.4 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -4.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,998,836-57,006,546 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0352, ZNF922 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O15060](https://www.uniprot.org/uniprotkb/O15060) (Zinc finger and BTB domain-containing protein 39):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [9880](https://www.ncbi.nlm.nih.gov/gene/9880):

> Predicted to enable DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II; regulation of cytokine production; and regulation of immune system process. Predicted to be located in nucleus. Predicted to be active in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29014) · Entrez [9880](https://www.ncbi.nlm.nih.gov/gene/9880) · UniProt [O15060](https://www.uniprot.org/uniprotkb/O15060) · Ensembl [ENSG00000166860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166860)

## Data

Gene col 9374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9374); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9374]; `tensor/DDL_lfc|DDL_z.npy` [9374]; `embed/gene_vectors.npy` [9374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9374 or target_col == 9374). Every well: [[ZBTB39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
