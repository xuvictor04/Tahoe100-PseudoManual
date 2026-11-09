---
symbol: "RPL23AP53"
type: "gene"
col: 13344
ensembl_id: "ENSG00000223508"
name: "ribosomal protein L23a pseudogene 53"
location: "8p23.3"
module: null
arm: null
pooled_cpm: 8.48
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# RPL23AP53

*ribosomal protein L23a pseudogene 53* — 8p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.17× (z +11.9, q 4e-30, up in 28 of 34 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.97× (z +10.8, q 6e-25, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.564× (z -4.8, q 9e-04, down in 13 of 36 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +11.9 | 4e-30 | 28/34 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +10.8 | 6e-25 | 32/44 (SW480, SHP-77, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +10.4 | 6e-23 | 25/45 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +8.8 | 2e-16 | 29/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +8.5 | 2e-15 | 24/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +7.6 | 3e-12 | 27/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +7.4 | 9e-12 | 24/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +6.7 | 1e-09 | 19/43 (KATO III, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +6.6 | 3e-09 | 20/45 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 4e-05 | 15/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.37×** | +5.0 | 4e-05 | 10/45 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 1e-04 | 15/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.7 | 1e-04 | 16/40 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.002 | 3/39 (SHP-77, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.26×** | +3.5 | 0.017 | 8/43 (NCI-H460, LS 180, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.057 | 7/45 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.060 | 5/43 (NCI-H460, HepG2/C3A, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.14× | +3.0 | 0.066 | 6/46 (LS 180, LoVo, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.44×** | +3.0 | 0.066 | 2/41 (SW48, HT-29) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13344.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.564×** | -4.8 | 9e-04 | 13/36 (BT-474, KATO III, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.774×** | -4.1 | 0.011 | 10/46 (H4, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.625×** | -3.9 | 0.012 | 13/45 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.776×** | -3.9 | 0.012 | 6/44 (SNU-423, C-33 A, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.856× | -3.6 | 0.043 | 11/46 (RPMI-7951, hTERT-HPNE, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.814×** | -3.3 | 0.087 | 4/46 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 8.15 | 8 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 7.94× (z +13.9) | — |
| [[NCI-H460 (line)]] | wt | 10.9 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +15.0) | — |
| [[LOX-IMVI (line)]] | wt | 21.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.8) |
| [[A-172 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0938× (z -12.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 14.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -8.7) |
| [[BT-474 (line)]] | alt | 7.17 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0646× (z -10.3) |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -8.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[COLO 205 (line)]] | alt | 3.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.6× (z +11.5) | — |
| [[H4 (line)]] | wt | 9.69 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0671× (z -8.8) |
| [[HCT15 (line)]] | alt | 9.24 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.0933× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 7.67 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 4.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 5.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 16.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.62× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 4.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +10.8) | — |
| [[A498 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.29 | 0 | 0 | — | — |

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
| Name | ribosomal protein L23a pseudogene 53 |
| Locus type | pseudogene |
| Location | 8p23.3 — chr8:213,251-213,707 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:35921](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35921) · Entrez [644128](https://www.ncbi.nlm.nih.gov/gene/644128) · Ensembl [ENSG00000223508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223508)

## Data

Gene col 13344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13344); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13344, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13344]; `tensor/DDL_lfc|DDL_z.npy` [13344]; `embed/gene_vectors.npy` [13344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13344 or target_col == 13344). Every well: [[RPL23AP53 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL23AP53.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
