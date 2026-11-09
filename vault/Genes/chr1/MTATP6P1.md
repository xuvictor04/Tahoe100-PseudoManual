---
symbol: "MTATP6P1"
type: "gene"
col: 14548
ensembl_id: "ENSG00000248527"
name: "MT-ATP6 pseudogene 1"
location: "1p36.33"
module: null
arm: null
pooled_cpm: 91.61
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MTATP6P1

*MT-ATP6 pseudogene 1* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.54× (z +8.7, q 1e-15, up in 42 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (HCT15 12.5×, A498 5.87×, HT-29 6.00×, LS 180 5.52×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 5.75×, HCT15 7.89×, LS 180 6.01×, A498 5.06×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.0783× (z -15.4, q 0e+00, down in 48 of 48 measured lines) ⚠ transcription drop. The strongest without an alert is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.472× (z -6.4, q 4e-08, down in 43 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14548.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (HCT15 12.5×, A498 5.87×, HT-29 6.00×, LS 180 5.52×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 5.75×, HCT15 7.89×, LS 180 6.01×, A498 5.06×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.54×** | +8.7 | 1e-15 | 42/44 (HCT15, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.92×** | +8.2 | 7e-14 | 48/49 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.27×** | +6.6 | 1e-08 | 43/45 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.5 | 0.071 | 33/47 (HS-578T, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.96×** | +3.4 | 0.071 | 43/49 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.69× | +3.0 | 0.25 | 35/47 (HEC-1-A, NCI-H2347, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14548.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.0783×** | -15.4 | 0e+00 | 48/48 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here); position effect removed |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.472×** | -6.4 | 4e-08 | 43/48 (PANC-1, HS-578T, …) | top dose only | position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.503×** | -5.8 | 1e-06 | 41/49 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.569×** | -3.5 | 0.063 | 31/48 (NCI-H2030, RKO, …) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.572×** | -3.4 | 0.063 | 37/47 (LoVo, J82, …) | inconsistent across doses | position effect removed |
| [[Afatinib (drug)]] 0.5 µM |  | **0.676×** | -3.4 | 0.063 | 45/49 (A-427, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.578×** | -3.4 | 0.063 | 30/48 (LS 180, CHP-212, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.590×** | -3.2 | 0.076 | 35/47 (HT-29, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.590×** | -3.2 | 0.076 | 36/48 (SW 1088, J82, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14548. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 80.5 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.01× (z +9.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.0788× (z -13.8) ⚠ transcription drop |
| [[A498 (line)]] | wt | 94.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.87× (z +9.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.1000× (z -13.6) ⚠ transcription drop |
| [[A549 (line)]] | wt | 108 | 0 | 3 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0892× (z -13.5) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.285× (z -9.9) |
| [[HCT15 (line)]] | alt | 54.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 12.5× (z +11.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.0396× (z -15.2) ⚠ transcription drop |
| [[Hs 766T (line)]] | wt | 90.0 | 0 | 3 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0768× (z -13.1) ⚠ transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.225× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 96.8 | 0 | 3 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.113× (z -11.9) ⚠ transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.249× (z -10.6) |
| [[A-172 (line)]] | wt | 77.6 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0723× (z -14.6) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.287× (z -9.8) |
| [[A-427 (line)]] | wt | 98.4 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0334× (z -17.0) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.286× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 81.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.07× (z +8.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.0460× (z -16.9) ⚠ transcription drop |
| [[HOP62 (line)]] | alt | 58.0 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0533× (z -14.0) ⚠ transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.230× (z -9.8) |
| [[HS-578T (line)]] | alt | 64.7 | 0 | 2 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.214× (z -10.9) |
| [[HT-29 (line)]] | alt | 68.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.00× (z +9.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.148× (z -10.6) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 86.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +9.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.0710× (z -15.2) ⚠ transcription drop |
| [[NCI-H1573 (line)]] | alt | 98.6 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0594× (z -13.9) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.277× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 131 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.136× (z -10.0) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.248× (z -9.8) |
| [[PANC-1 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0568× (z -14.9) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.197× (z -11.8) |
| [[AN3 CA (line)]] | alt | 87.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0777× (z -10.1) ⚠ transcription drop |
| [[BT-474 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.120× (z -10.9) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 65.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.115× (z -9.3) ⚠ transcription drop |
| [[C32 (line)]] | wt | 47.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0561× (z -12.9) ⚠ transcription drop |
| [[CFPAC-1 (line)]] | alt | 58.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0645× (z -13.3) ⚠ transcription drop |
| [[CHP-212 (line)]] | wt | 69.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0516× (z -10.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 74.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0873× (z -13.1) ⚠ transcription drop |
| [[H4 (line)]] | wt | 59.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.121× (z -9.1) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 84.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.100× (z -13.2) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 59.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0444× (z -13.7) ⚠ transcription drop |
| [[hTERT-HPNE (line)]] | wt | 58.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.76× (z +8.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 67.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0738× (z -13.6) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 96.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0933× (z -11.6) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 74.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0982× (z -12.1) ⚠ transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 76.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0615× (z -12.7) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 54.6 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.289× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 68.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0773× (z -13.5) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 73.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0355× (z -17.6) ⚠ transcription drop |
| [[RKO (line)]] | wt | 99.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.136× (z -10.4) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0453× (z -13.8) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0682× (z -12.9) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0233× (z -20.7) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 70.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.155× (z -8.8) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 90.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.113× (z -10.7) ⚠ transcription drop |
| [[SW 900 (line)]] | alt | 96.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0687× (z -13.4) ⚠ transcription drop |
| [[SW1417 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0751× (z -13.8) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 90.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0650× (z -16.2) ⚠ transcription drop |
| [[NCI-H2122 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 90.1 | 0 | 0 | — | — |

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
| Name | MT-ATP6 pseudogene 1 |
| Locus type | pseudogene |
| Location | 1p36.33 — chr1:633,696-634,376 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44575) · Entrez [106480796](https://www.ncbi.nlm.nih.gov/gene/106480796) · Ensembl [ENSG00000248527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248527)

## Data

Gene col 14548: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14548); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14548, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14548]; `tensor/DDL_lfc|DDL_z.npy` [14548]; `embed/gene_vectors.npy` [14548]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14548 or target_col == 14548). Every well: [[MTATP6P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTATP6P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
