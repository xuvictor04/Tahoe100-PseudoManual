---
symbol: "MT-ND3"
type: "gene"
col: 12703
ensembl_id: "ENSG00000198840"
name: "mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 3"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 70.51
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-ND3

*mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 3* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.10× (z +10.3, q 6e-22, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Darinaparsin (drug)]] 5 µM: 1.64× (z +4.4, q 0.001, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.374× (z -8.7, q 1e-15, down in 43 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12703.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.10×** | +10.3 | 6e-22 | 48/48 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +7.0 | 1e-09 | 37/42 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.17×** | +6.7 | 4e-09 | 43/45 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM |  | **1.64×** | +4.4 | 0.001 | 47/48 (Hs 766T, A549, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +4.3 | 0.002 | 41/47 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.96×** | +4.3 | 0.002 | 46/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.009 | 31/48 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.83×** | +3.7 | 0.019 | 43/48 (LS 180, HEC-1-A, …) | top dose only | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.3 | 0.065 | 43/47 (SW 900, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12703.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.374×** | -8.7 | 1e-15 | 43/48 (A549, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.336×** | -6.8 | 2e-09 | 43/47 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.340×** | -6.8 | 2e-09 | 40/48 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.417×** | -5.5 | 6e-06 | 38/48 (RKO, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.590×** | -4.7 | 3e-04 | 35/49 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.578×** | -3.4 | 0.055 | 34/47 (SHP-77, C-33 A, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.594×** | -3.3 | 0.088 | 29/48 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.613× | -3.1 | 0.13 | 25/47 (RKO, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.603× | -3.0 | 0.13 | 26/47 (CHP-212, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.617× | -3.0 | 0.13 | 29/48 (NCI-H661, SW48, …) | top dose only |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.595× | -3.0 | 0.13 | 38/48 (J82, LoVo, …) | inconsistent across doses | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.596× | -3.0 | 0.13 | 41/48 (HT-29, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 83.4 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.87× (z +10.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.219× (z -13.3) |
| [[Hs 766T (line)]] | wt | 68.8 | 0 | 3 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.258× (z -10.6) |
| [[PANC-1 (line)]] | alt | 76.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +8.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.185× (z -14.1) |
| [[A-172 (line)]] | wt | 57.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +9.6) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.262× (z -9.5) |
| [[A498 (line)]] | wt | 66.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +9.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.230× (z -10.8) |
| [[A549 (line)]] | wt | 79.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +9.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.138× (z -15.4) |
| [[HOP62 (line)]] | alt | 43.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +8.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.258× (z -9.5) |
| [[LoVo (line)]] | wt | 87.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +9.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 46.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +9.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.256× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 65.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.61× (z +11.2) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.319× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 97.7 | 0 | 2 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.219× (z -11.2) |
| [[SHP-77 (line)]] | alt | 69.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +9.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.171× (z -9.5) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 81.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.76× (z +9.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.295× (z -9.7) |
| [[A-427 (line)]] | wt | 136 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.185× (z -12.8) |
| [[CFPAC-1 (line)]] | alt | 46.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 55.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0638× (z -9.2) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 98.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.203× (z -8.5) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 52.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 57.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 65.8 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.254× (z -8.9) |
| [[HS-578T (line)]] | alt | 40.3 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.236× (z -10.4) |
| [[HT-29 (line)]] | alt | 62.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +9.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 76.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 63.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 64.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.37× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 44.5 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.261× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 118 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.191× (z -13.1) |
| [[RKO (line)]] | wt | 63.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0984× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.134× (z -12.4) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 47.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.34× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 61.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 91.2 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.195× (z -12.9) |
| [[AN3 CA (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 83.9 | 0 | 0 | — | — |

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
| Name | mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | mitochondria — chrMT:10,059-10,404 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ND3, NAD3; previously MTND3 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase core subunits; Mitochondrially encoded protein coding genes |
| Reactome | 16 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; tRNA processing in the mitochondrion; Mitochondrial mRNA modification |
| Matched by | ensembl_id |

**Function**, from UniProt [P03897](https://www.uniprot.org/uniprotkb/P03897) (NADH-ubiquinone oxidoreductase chain 3):

> Core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which catalyzes electron transfer from NADH through the respiratory chain, using ubiquinone as an electron acceptor. Essential for the catalytic activity of complex I.

**Summary**, from NCBI Gene [4537](https://www.ncbi.nlm.nih.gov/gene/4537):

> Enables NADH dehydrogenase (ubiquinone) activity. Involved in mitochondrial electron transport, NADH to ubiquinone. Located in mitochondrial inner membrane. Part of respiratory chain complex I. Implicated in Leber hereditary optic neuropathy; Leigh disease; and Parkinson's disease. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7458](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7458) · Entrez [4537](https://www.ncbi.nlm.nih.gov/gene/4537) · UniProt [P03897](https://www.uniprot.org/uniprotkb/P03897) · Ensembl [ENSG00000198840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198840)

## Data

Gene col 12703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12703); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12703, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12703]; `tensor/DDL_lfc|DDL_z.npy` [12703]; `embed/gene_vectors.npy` [12703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12703 or target_col == 12703). Every well: [[MT-ND3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-ND3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
