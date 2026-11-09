---
symbol: "RPL23AP49"
type: "gene"
col: 14359
ensembl_id: "ENSG00000243422"
name: "ribosomal protein L23a pseudogene 49"
location: "3p12.3"
module: null
arm: null
pooled_cpm: 2.86
n_lines_expressing: 37
n_dd_up: 13
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# RPL23AP49

*ribosomal protein L23a pseudogene 49* — 3p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.58× (z +7.4, q 7e-11, up in 1 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 0.5 µM: 1.67× (z +4.2, q 0.005, up in 7 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.187× (z -13.6, q 2e-39, down in 28 of 32 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14359.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +7.4 | 7e-11 | 1/7 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.69×** | +6.0 | 4e-07 | 9/31 (RKO, HOP62, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.67×** | +4.2 | 0.005 | 7/29 (HEC-1-A, HOP62, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +4.2 | 0.005 | 1/7 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.40×** | +3.8 | 0.015 | 8/29 (NCI-H23, HOP62, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +3.8 | 0.015 | 7/24 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.58×** | +3.7 | 0.016 | 3/15 (SW 900, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.016 | 6/30 (NCI-H1573, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.032 | 9/32 (NCI-H23, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +3.4 | 0.035 | 1/9 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.055 | 1/28 (hTERT-HPNE) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.058 | 6/28 (NCI-H1573, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.47×** | +3.1 | 0.074 | 4/26 (SW 900, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14359.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.187×** | -13.6 | 2e-39 | 28/32 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.358×** | -7.7 | 5e-12 | 21/28 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.526×** | -7.4 | 3e-11 | 17/23 (HEC-1-A, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.417×** | -7.1 | 2e-10 | 15/17 (HOP62, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.447×** | -6.0 | 2e-07 | 19/28 (SHP-77, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.498×** | -5.7 | 2e-06 | 14/22 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.489×** | -5.6 | 2e-06 | 18/28 (HEC-1-A, A498, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.534×** | -5.1 | 3e-05 | 14/33 (NCI-H23, RKO, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.528×** | -5.0 | 4e-05 | 8/28 (SK-MEL-2, J82, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.587×** | -4.3 | 9e-04 | 10/31 (HEC-1-A, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.589×** | -4.3 | 9e-04 | 13/31 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.583×** | -4.0 | 0.003 | 13/28 (SW480, SNU-423, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.645×** | -3.6 | 0.016 | 10/26 (CHP-212, SHP-77, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.646×** | -3.5 | 0.016 | 12/29 (HEC-1-A, H4, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.459×** | -3.3 | 0.036 | 9/28 (J82, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.767×** | -3.0 | 0.078 | 7/31 (SW 900, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14359. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 22.3 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.4) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -10.9) |
| [[HOP62 (line)]] | alt | 8.91 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0347× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[J82 (line)]] | alt | 4.71 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 3.97 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0926× (z -12.4) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H2030 (line)]] | alt | 3.41 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0497× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 5.89 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0444× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 3.14 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +9.8) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[SW 900 (line)]] | alt | 5.83 | 0 | 1 | — | [[Methotrexate (drug)]] 0.5 µM 0.0344× (z -10.6) |
| [[SW480 (line)]] | alt | 1.77 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0517× (z -8.8) |
| [[A-172 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.591 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.599 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.894 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.754 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L23a pseudogene 49 |
| Locus type | pseudogene |
| Location | 3p12.3 — chr3:75,624,686-75,625,153 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:35689](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35689) · Entrez [653236](https://www.ncbi.nlm.nih.gov/gene/653236) · Ensembl [ENSG00000243422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243422)

## Data

Gene col 14359: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14359); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14359, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14359]; `tensor/DDL_lfc|DDL_z.npy` [14359]; `embed/gene_vectors.npy` [14359]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14359 or target_col == 14359). Every well: [[RPL23AP49 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL23AP49.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
