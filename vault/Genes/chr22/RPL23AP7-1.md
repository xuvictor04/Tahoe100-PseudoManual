---
symbol: "RPL23AP7-1"
type: "gene"
col: 16560
ensembl_id: "ENSG00000291064"
name: ""
location: ""
module: null
arm: null
pooled_cpm: 2.78
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# RPL23AP7-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.66× (z +10.3, q 5e-22, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.82× (z +6.5, q 1e-08, up in 17 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.678× (z -4.3, q 0.011, down in 10 of 46 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16560.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +10.3 | 5e-22 | 1/2 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +8.7 | 8e-16 | 2/5 (PANC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +6.6 | 7e-09 | 8/16 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.82×** | +6.5 | 1e-08 | 17/46 (SW480, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +6.2 | 8e-08 | 16/45 (SW480, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +4.9 | 7e-05 | 9/44 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.7 | 3e-04 | 4/17 (NCI-H1573, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +4.1 | 0.003 | 4/16 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.005 | 8/34 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.006 | 8/39 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.006 | 7/46 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.009 | 4/45 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.021 | 5/41 (LS 180, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.021 | 7/41 (A-427, HOP62, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +3.0 | 0.091 | 0/26 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.091 | 4/45 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.091 | 4/37 (H4, NCI-H23, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.091 | 2/42 (LOX-IMVI, NCI-H23) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16560.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.678×** | -4.3 | 0.011 | 10/46 (SNU-423, HCT15, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.719×** | -3.6 | 0.073 | 9/46 (HOP62, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.725×** | -3.5 | 0.073 | 12/43 (KATO III, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.760× | -3.0 | 0.34 | 8/42 (LOX-IMVI, H4, …) | all doses, flat | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 6.72 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 14.2× (z +9.5) | — |
| [[A-172 (line)]] | wt | 4.69 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 3.38 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0867× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~15% of this change |
| [[NCI-H2347 (line)]] | alt | 1.84 | 0 | 1 | — | [[Norepinephrine (hydrochloride) (drug)]] 0.05 µM 0.0487× (z -9.4) |
| [[A-427 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.52 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

> [!warning] No registry record
> RPL23AP7-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16560); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16560, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16560]; `tensor/DDL_lfc|DDL_z.npy` [16560]; `embed/gene_vectors.npy` [16560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16560 or target_col == 16560). Every well: [[RPL23AP7-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL23AP7-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
