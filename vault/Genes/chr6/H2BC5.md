---
symbol: "H2BC5"
type: "gene"
col: 8155
ensembl_id: "ENSG00000158373"
name: "H2B clustered histone 5"
location: "6p22.2"
module: null
arm: null
pooled_cpm: 23.93
n_lines_expressing: 50
n_dd_up: 47
n_dd_down: 5
n_dd_up_clean: 37
n_dd_down_clean: 2
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# H2BC5

*H2B clustered histone 5* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.24× (z +33.7, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Cytarabine (drug)]] 5 µM: 0.689× (z -4.1, q 0.019, down in 21 of 47 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.703× (z -4.0, q 0.019, down in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (H4 0.0812×).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8155.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.24×** | +33.7 | 0e+00 | 47/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.65×** | +20.7 | 0e+00 | 46/46 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.78×** | +17.7 | 0e+00 | 42/44 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.46×** | +16.9 | 0e+00 | 45/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.70×** | +16.8 | 0e+00 | 47/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.79×** | +16.4 | 0e+00 | 46/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.83×** | +14.0 | 7e-43 | 33/36 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.06×** | +12.2 | 4e-32 | 28/34 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.41×** | +9.9 | 2e-21 | 41/48 (SW48, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.16×** | +8.7 | 2e-16 | 38/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +8.5 | 7e-16 | 39/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **2.00×** | +7.8 | 3e-13 | 35/47 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +7.7 | 4e-13 | 31/47 (SNU-423, C32, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.92×** | +7.4 | 7e-12 | 33/47 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.92×** | +7.3 | 8e-12 | 32/46 (LS 180, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +7.1 | 3e-11 | 33/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.88×** | +7.1 | 4e-11 | 32/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.86×** | +7.0 | 9e-11 | 29/48 (A-172, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.86×** | +7.0 | 9e-11 | 36/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8155.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (H4 0.0812×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.689×** | -4.1 | 0.019 | 21/47 (A549, H4, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.703×** | -4.0 | 0.019 | 21/47 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.729×** | -3.6 | 0.058 | 17/47 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.550×** | -3.5 | 0.058 | 13/39 (COLO 205, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.745×** | -3.3 | 0.096 | 11/47 (SW480, SHP-77, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.739× | -3.2 | 0.12 | 12/48 (AN3 CA, NCI-H1573, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.764× | -3.0 | 0.19 | 16/47 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8155. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 15.3 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +19.2) | — |
| [[LoVo (line)]] | wt | 13.4 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +18.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +17.2) | — |
| [[NCI-H460 (line)]] | wt | 12.2 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +24.1) | — |
| [[PANC-1 (line)]] | alt | 22.6 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +23.8) | — |
| [[LOX-IMVI (line)]] | wt | 18.0 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +22.5) | — |
| [[C32 (line)]] | wt | 15.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 28.4× (z +20.5) | — |
| [[J82 (line)]] | alt | 38.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +22.2) | — |
| [[LS 180 (line)]] | wt | 20.9 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.38× (z +16.1) | — |
| [[SW480 (line)]] | alt | 28.6 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.55× (z +21.6) | — |
| [[HOP62 (line)]] | alt | 25.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +18.9) | — |
| [[NCI-H2347 (line)]] | alt | 18.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +21.5) | — |
| [[A498 (line)]] | wt | 8.97 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +18.6) | — |
| [[HS-578T (line)]] | alt | 10.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +16.4) | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +16.7) | — |
| [[KATO III (line)]] | alt | 48.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.56× (z +18.5) | — |
| [[NCI-H23 (line)]] | alt | 25.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +20.8) | — |
| [[Panc 03.27 (line)]] | alt | 49.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +13.9) | — |
| [[SW1417 (line)]] | alt | 42.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +14.1) | — |
| [[A-427 (line)]] | wt | 19.0 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.53× (z +12.3) | — |
| [[BT-474 (line)]] | alt | 23.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.86× (z +12.8) | — |
| [[H4 (line)]] | wt | 16.9 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +13.0) | [[Pimozide (drug)]] 0.05 µM 0.0812× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 25.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +15.3) | — |
| [[SW48 (line)]] | wt | 19.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +11.6) | — |
| [[A-172 (line)]] | wt | 29.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +13.2) | — |
| [[A549 (line)]] | wt | 18.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.88× (z +14.2) | — |
| [[AsPC-1 (line)]] | alt | 11.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.35× (z +12.4) | — |
| [[COLO 205 (line)]] | alt | 46.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.30× (z +14.3) | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.88× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 34.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 35.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.97× (z +15.3) | — |
| [[RKO (line)]] | wt | 15.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +13.4) | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +13.2) | — |
| [[SHP-77 (line)]] | alt | 18.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 30.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +14.2) | — |
| [[SW 900 (line)]] | alt | 22.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +13.1) | — |
| [[CFPAC-1 (line)]] | alt | 60.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +12.3) | — |
| [[HT-29 (line)]] | alt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +12.7) | — |
| [[SW 1271 (line)]] | alt | 22.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |

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
| Name | H2B clustered histone 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:26,158,122-26,171,349 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H2B/b; previously H2BFB, HIST1H2BD |
| Gene groups (HGNC) | H2B histones |
| Reactome | 133 pathways, smallest: Replacement of protamines by nucleosomes in the male pronucleus; ChAHP complex assembly; DNA methylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P58876](https://www.uniprot.org/uniprotkb/P58876) (Histone H2B type 1-D):

> Core component of nucleosome. Nucleosomes wrap and compact DNA into chromatin, limiting DNA accessibility to the cellular machineries which require DNA as a template. Histones thereby play a central role in transcription regulation, DNA repair, DNA replication and chromosomal stability. DNA accessibility is regulated via a complex set of post-translational modifications of histones, also called histone code, and nucleosome remodeling.

**Summary**, from NCBI Gene [3017](https://www.ncbi.nlm.nih.gov/gene/3017):

> Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Nucleosomes consist of approximately 146 bp of DNA wrapped around a histone octamer composed of pairs of each of the four core histones (H2A, H2B, H3, and H4). The chromatin fiber is further compacted through the interaction of a linker histone, H1, with the DNA between the nucleosomes to form higher order chromatin structures. This gene is intronless and encodes a …

**Accessions** — [HGNC:4747](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4747) · Entrez [3017](https://www.ncbi.nlm.nih.gov/gene/3017) · UniProt [P58876](https://www.uniprot.org/uniprotkb/P58876) · Ensembl [ENSG00000158373](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158373)

## Data

Gene col 8155: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8155); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8155, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8155]; `tensor/DDL_lfc|DDL_z.npy` [8155]; `embed/gene_vectors.npy` [8155]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8155 or target_col == 8155). Every well: [[H2BC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/H2BC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
