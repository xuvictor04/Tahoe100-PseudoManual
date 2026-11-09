---
symbol: "RPS10P7"
type: "gene"
col: 13339
ensembl_id: "ENSG00000223396"
name: "ribosomal protein S10 pseudogene 7"
location: "1q32.1"
module: null
arm: null
pooled_cpm: 8.83
n_lines_expressing: 47
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 15
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# RPS10P7

*ribosomal protein S10 pseudogene 7* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.69× (z +5.9, q 2e-06, up in 23 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.336× (z -12.3, q 6e-32, down in 35 of 42 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13339.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +5.9 | 2e-06 | 23/42 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.016 | 9/39 (NCI-H2030, LoVo, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.8 | 0.019 | 8/32 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.019 | 9/43 (NCI-H2030, RPMI-7951, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.019 | 13/44 (NCI-H460, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.019 | 14/42 (HOP62, NCI-H1573, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.032 | 14/40 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.040 | 11/45 (LoVo, NCI-H2030, …) | two highest doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.040 | 6/35 (NCI-H460, SNU-423, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +3.4 | 0.045 | 6/16 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Afatinib (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.077 | 9/44 (A-427, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.085 | 3/38 (A-172, NCI-H23, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13339.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.336×** | -12.3 | 6e-32 | 35/42 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.353×** | -11.7 | 3e-29 | 35/44 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.418×** | -9.8 | 2e-20 | 25/38 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.452×** | -8.9 | 4e-17 | 27/41 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.452×** | -8.9 | 4e-17 | 31/43 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.271×** | -7.7 | 1e-12 | 25/37 (A-427, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.568×** | -6.4 | 2e-08 | 19/36 (C32, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.341×** | -6.3 | 2e-08 | 23/41 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.592×** | -5.9 | 2e-07 | 21/41 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.588×** | -5.7 | 9e-07 | 21/40 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.665×** | -4.6 | 2e-04 | 17/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.755×** | -4.5 | 4e-04 | 20/38 (C32, HS-578T, …) | two highest doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.667×** | -4.4 | 5e-04 | 19/31 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.767×** | -4.2 | 9e-04 | 14/43 (KATO III, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.685×** | -4.1 | 0.002 | 19/42 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.734×** | -3.5 | 0.017 | 13/41 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.832×** | -2.9 | 0.099 | 19/39 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fulvestrant (drug)]] 0.05 µM |  | **0.771×** | -2.9 | 0.099 | 7/43 (SK-MEL-2, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13339. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.1 | 0 | 13 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -15.5) |
| [[C32 (line)]] | wt | 26.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0437× (z -22.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0555× (z -14.7) |
| [[A-427 (line)]] | wt | 19.1 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.180× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 14.8 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 15.1 | 0 | 5 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.160× (z -12.8) |
| [[LoVo (line)]] | wt | 24.9 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 8.21 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0924× (z -10.9) |
| [[KATO III (line)]] | alt | 17.4 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.206× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 9.10 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -9.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -8.8) |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0676× (z -10.0) |
| [[A-172 (line)]] | wt | 7.59 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0924× (z -9.7) |
| [[A549 (line)]] | wt | 9.59 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -8.7) |
| [[HOP62 (line)]] | alt | 4.18 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.127× (z -8.5) |
| [[HS-578T (line)]] | alt | 6.64 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0695× (z -15.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[J82 (line)]] | alt | 6.42 | 0 | 1 | — | [[Bentamapimod (drug)]] 0.05 µM 0.0594× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 7.20 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0780× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 15.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +12.8) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2347 (line)]] | alt | 3.44 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.107× (z -8.6) |
| [[SW 900 (line)]] | alt | 7.60 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0694× (z -10.1) |
| [[SW1417 (line)]] | alt | 4.06 | 0 | 1 | — | [[Vismodegib (drug)]] 0.5 µM 0.0575× (z -9.5) |
| [[SW48 (line)]] | wt | 12.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0738× (z -9.0) |
| [[SW480 (line)]] | alt | 7.61 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -8.9) |
| [[A498 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.52 | 0 | 0 | — | — |

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
| Name | ribosomal protein S10 pseudogene 7 |
| Locus type | pseudogene |
| Location | 1q32.1 — chr1:201,520,056-201,520,549 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | lnc-MCEI |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:36423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:36423) · Entrez [376693](https://www.ncbi.nlm.nih.gov/gene/376693) · Ensembl [ENSG00000223396](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223396)

## Data

Gene col 13339: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13339); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13339, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13339]; `tensor/DDL_lfc|DDL_z.npy` [13339]; `embed/gene_vectors.npy` [13339]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13339 or target_col == 13339). Every well: [[RPS10P7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS10P7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
