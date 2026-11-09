---
symbol: "MTND5P11"
type: "gene"
col: 14579
ensembl_id: "ENSG00000248923"
name: "MT-ND5 pseudogene 11"
location: "5q31.1"
module: null
arm: null
pooled_cpm: 2.1
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MTND5P11

*MT-ND5 pseudogene 11* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.51× (z +10.7, q 5e-24, up in 9 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.50× (z +4.0, q 0.005, up in 5 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.499× (z -7.0, q 1e-09, down in 27 of 42 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14579.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.51×** | +10.7 | 5e-24 | 9/9 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.11×** | +9.7 | 1e-19 | 1/1 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.95×** | +8.3 | 2e-14 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.21×** | +5.4 | 8e-06 | 8/16 (KATO III, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +4.4 | 0.001 | 3/10 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.005 | 5/42 (LoVo, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.95×** | +4.0 | 0.005 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.54× | +3.1 | 0.15 | 2/19 (NCI-H2030, NCI-H460) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14579.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.499×** | -7.0 | 1e-09 | 27/42 (PANC-1, NCI-H2030, …) | rises with dose | position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.533×** | -6.3 | 7e-08 | 26/42 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.800×** | -5.7 | 3e-06 | 32/45 (RKO, NCI-H2347, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.498×** | -5.0 | 1e-04 | 10/11 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.509×** | -4.8 | 2e-04 | 18/46 (SHP-77, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.610×** | -3.5 | 0.040 | 11/39 (KATO III, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Pentamidine (isethionate) (drug)]] 0.5 µM |  | **0.613×** | -3.5 | 0.040 | 10/41 (NCI-H460, A-427, …) | rises with dose | position effect removed |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.718×** | -3.3 | 0.059 | 10/45 (J82, A549, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.65 | 0 | 2 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.165× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 2.25 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.0884× (z -9.6) |
| [[A-172 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.35 | 0 | 0 | — | — |

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
| Name | MT-ND5 pseudogene 11 |
| Locus type | pseudogene |
| Location | 5q31.1 — chr5:134,924,648-134,926,459 (-) |
| Ensembl biotype | processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42273) · Entrez [100506169](https://www.ncbi.nlm.nih.gov/gene/100506169) · Ensembl [ENSG00000248923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248923)

## Data

Gene col 14579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14579); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14579, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14579]; `tensor/DDL_lfc|DDL_z.npy` [14579]; `embed/gene_vectors.npy` [14579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14579 or target_col == 14579). Every well: [[MTND5P11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTND5P11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
