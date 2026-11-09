---
symbol: "MTND2P28"
type: "gene"
col: 13470
ensembl_id: "ENSG00000225630"
name: "MT-ND2 pseudogene 28"
location: "1p36.33"
module: null
arm: null
pooled_cpm: 7.58
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MTND2P28

*MT-ND2 pseudogene 28* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 6.09× (z +12.7, q 4e-34, up in 46 of 46 measured lines) ⚠ unreliable plate only; position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Carbidopa (monohydrate) (drug)]] 0.05 µM in 2 lines (SW480 6.42×, PANC-1 6.00×; ⚠ unreliable plate only; position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 11.2×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.390× (z -6.6, q 2e-08, down in 25 of 37 measured lines) ⚠ transcription drop. The strongest without an alert is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.564× (z -5.7, q 3e-06, down in 25 of 47 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13470.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Carbidopa (monohydrate) (drug)]] 0.05 µM in 2 lines (SW480 6.42×, PANC-1 6.00×; ⚠ unreliable plate only; position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 11.2×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **6.09×** | +12.7 | 4e-34 | 46/46 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.26×** | +11.2 | 1e-26 | 11/12 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.55×** | +10.6 | 4e-24 | 26/29 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +7.9 | 5e-13 | 21/22 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.7 | 0.021 | 20/35 (SW 900, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.61× | +3.2 | 0.13 | 16/44 (HEC-1-A, NCI-H2347, …) | top dose only | position effect removed |
| [[Palmatine (chloride) (drug)]] 5 µM |  | 1.38× | +3.2 | 0.13 | 17/46 (SW1417, SNU-423, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13470.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.390×** | -6.6 | 2e-08 | 25/37 (NCI-H23, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here); position effect removed |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.564×** | -5.7 | 3e-06 | 25/47 (Hs 766T, NCI-H460, …) | top dose only | position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.575×** | -5.5 | 6e-06 | 26/46 (NCI-H460, PANC-1, …) | top dose only | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.533×** | -4.4 | 0.001 | 23/46 (A549, HEC-1-A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.556×** | -4.1 | 0.004 | 22/44 (HEC-1-A, NCI-H2030, …) | top dose only | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.614×** | -3.4 | 0.050 | 14/46 (CFPAC-1, RKO, …) | rises with dose | position effect removed |
| [[Voriconazole (drug)]] 5 µM |  | **0.619×** | -3.4 | 0.050 | 10/46 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.602×** | -3.4 | 0.050 | 17/43 (J82, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | **0.627×** | -3.3 | 0.060 | 11/46 (AsPC-1, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.638×** | -3.2 | 0.085 | 15/46 (Hs 766T, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.644×** | -3.1 | 0.098 | 18/46 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.1 | 0 | 3 (1 ⚠) | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.194× (z -10.5) |
| [[PANC-1 (line)]] | alt | 9.83 | 1 (1 ⚠) | 1 | [[Carbidopa (monohydrate) (drug)]] 0.05 µM 6.00× (z +8.6) ⚠ unreliable plate only; position not correctable | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.211× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0761× (z -9.8) ⚠ transcription drop · without an alert: [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM 0.0825× (z -9.5) |
| [[A-427 (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0615× (z -10.3) ⚠ transcription drop |
| [[A498 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0658× (z -12.4) ⚠ transcription drop |
| [[A549 (line)]] | wt | 8.81 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.5 µM 0.0264× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 7.21 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.103× (z -9.4) ⚠ transcription drop |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.181× (z -9.3) |
| [[KATO III (line)]] | alt | 8.45 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0794× (z -9.5) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 4.89 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.2× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0534× (z -12.5) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0956× (z -8.6) ⚠ transcription drop |
| [[SW 900 (line)]] | alt | 8.23 | 0 | 1 | — | [[Amsacrine (drug)]] 0.5 µM 0.0558× (z -10.1) |
| [[SW480 (line)]] | alt | 7.23 | 1 (1 ⚠) | 0 | [[Carbidopa (monohydrate) (drug)]] 0.05 µM 6.42× (z +9.2) ⚠ unreliable plate only; position not correctable | — |
| [[A-172 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.34 | 0 | 0 | — | — |

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
| Name | MT-ND2 pseudogene 28 |
| Locus type | pseudogene |
| Location | 1p36.33 — chr1:629,640-630,683 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42129](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42129) · Entrez [100652939](https://www.ncbi.nlm.nih.gov/gene/100652939) · Ensembl [ENSG00000225630](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225630)

## Data

Gene col 13470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13470); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13470, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13470]; `tensor/DDL_lfc|DDL_z.npy` [13470]; `embed/gene_vectors.npy` [13470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13470 or target_col == 13470). Every well: [[MTND2P28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTND2P28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
