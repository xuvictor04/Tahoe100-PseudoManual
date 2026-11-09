---
symbol: "MT-TL1"
type: "gene"
col: 13056
ensembl_id: "ENSG00000209082"
name: "mitochondrially encoded tRNA-Leu (UUA/G) 1"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 4.16
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-TL1

*mitochondrially encoded tRNA-Leu (UUA/G) 1* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.58× (z +8.0, q 3e-13, up in 23 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 3.20× (z +7.2, q 1e-10, up in 40 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (CFPAC-1 0.0615×; ⚠ cell-cycle shift, explains ~9% of this change); [[Vortioxetine (drug)]] 5 µM in 1 line (A549 0.0695×; ⚠ toxic).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13056.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.58×** | +8.0 | 3e-13 | 23/26 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.66×** | +8.0 | 3e-13 | 6/7 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **3.20×** | +7.2 | 1e-10 | 40/43 (A549, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **1.97×** | +6.2 | 1e-07 | 31/48 (PANC-1, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.49×** | +5.9 | 5e-07 | 28/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +5.6 | 2e-06 | 7/9 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +5.6 | 2e-06 | 23/38 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +4.8 | 1e-04 | 21/37 (NCI-H2030, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.08×** | +4.7 | 2e-04 | 25/45 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Palmatine (chloride) (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.002 | 24/45 (PANC-1, LOX-IMVI, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.68×** | +3.3 | 0.045 | 10/45 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Pentoxifylline (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +3.2 | 0.067 | 11/44 (J82, SW 900, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.41×** | +3.1 | 0.076 | 11/38 (C32, RKO, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13056.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (CFPAC-1 0.0615×; ⚠ cell-cycle shift, explains ~9% of this change); [[Vortioxetine (drug)]] 5 µM in 1 line (A549 0.0695×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM |  | 0.685× | -3.5 | 0.21 | 13/46 (Hs 766T, A-427, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.576× | -3.4 | 0.21 | 13/45 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 0.593× | -3.3 | 0.22 | 18/44 (J82, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13056. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.09 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0695× (z -8.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 3.84 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0615× (z -9.0) ⚠ cell-cycle shift, explains ~9% of this change |
| [[A-172 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.16 | 0 | 0 | — | — |

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
| Name | mitochondrially encoded tRNA-Leu (UUA/G) 1 |
| Locus type | RNA, transfer (non-coding RNA) |
| Location | mitochondria — chrMT:3,230-3,304 (+) |
| Ensembl biotype | Mt_tRNA |
| Also known as | TRNL1; previously MTTL1 |
| Gene groups (HGNC) | Mitochondrially encoded transfer RNAs |
| Reactome | 8 pathways, smallest: tRNA processing in the mitochondrion; rRNA processing in the mitochondrion; Mitochondrial ribosome-associated quality control |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [4567](https://www.ncbi.nlm.nih.gov/gene/4567):

> Predicted to enable triplet codon-amino acid adaptor activity. Predicted to be involved in translation. Implicated in cardiomyopathy. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7490) · Entrez [4567](https://www.ncbi.nlm.nih.gov/gene/4567) · Ensembl [ENSG00000209082](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000209082)

## Data

Gene col 13056: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13056); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13056, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13056]; `tensor/DDL_lfc|DDL_z.npy` [13056]; `embed/gene_vectors.npy` [13056]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13056 or target_col == 13056). Every well: [[MT-TL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-TL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
