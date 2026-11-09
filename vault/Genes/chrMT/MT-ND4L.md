---
symbol: "MT-ND4L"
type: "gene"
col: 13071
ensembl_id: "ENSG00000212907"
name: "mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 4L"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 41.32
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-ND4L

*mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 4L* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.58× (z +8.8, q 1e-15, up in 43 of 45 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 5.29×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LOX-IMVI 6.09×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 7.30×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.489× (z -6.9, q 2e-09, down in 37 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13071.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 5.29×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LOX-IMVI 6.09×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 7.30×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.58×** | +8.8 | 1e-15 | 43/45 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.42×** | +8.1 | 1e-13 | 39/41 (LOX-IMVI, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.29×** | +7.4 | 3e-11 | 42/42 (Panc 03.27, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +4.3 | 0.003 | 33/47 (MIA PaCa-2, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 2.51× | +3.3 | 0.11 | 30/49 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13071.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.489×** | -6.9 | 2e-09 | 37/48 (NCI-H460, NCI-H2030, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.412×** | -6.1 | 3e-07 | 40/46 (COLO 205, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.560×** | -5.6 | 4e-06 | 43/49 (NCI-H460, A549, …) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.508×** | -4.6 | 5e-04 | 43/47 (J82, A-427, …) | inconsistent across doses | position effect removed |
| [[Decitabine (drug)]] 5 µM |  | **0.533×** | -4.2 | 0.004 | 44/47 (A-172, A-427, …) | top dose only | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.558×** | -4.0 | 0.006 | 36/47 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Tazarotene (drug)]] 5 µM |  | **0.591×** | -3.6 | 0.021 | 41/48 (A-427, BT-474, …) | inconsistent across doses | position effect removed |
| [[Voriconazole (drug)]] 5 µM |  | **0.591×** | -3.6 | 0.021 | 38/48 (RKO, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.593×** | -3.6 | 0.021 | 29/46 (Hs 766T, RKO, …) | rises with dose |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | **0.595×** | -3.6 | 0.021 | 39/48 (NCI-H23, A-427, …) | inconsistent across doses | position effect removed |
| [[Malotilate (drug)]] 5 µM |  | **0.603×** | -3.5 | 0.027 | 41/48 (J82, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.615×** | -3.3 | 0.041 | 33/47 (HEC-1-A, A-427, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Captopril (drug)]] 5 µM |  | **0.622×** | -3.3 | 0.050 | 34/48 (SW1417, J82, …) | rises with dose | position effect removed |
| [[Thymol (drug)]] 0.05 µM |  | **0.639×** | -3.1 | 0.088 | 28/48 (HCT15, NCI-H1573, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13071. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 47.6 | 0 | 2 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.239× (z -10.8) |
| [[BT-474 (line)]] | alt | 64.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.156× (z -9.0) ⚠ transcription drop |
| [[CFPAC-1 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.113× (z -11.1) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0736× (z -11.5) ⚠ transcription drop |
| [[Hs 766T (line)]] | wt | 44.8 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.228× (z -10.1) |
| [[KATO III (line)]] | alt | 50.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.155× (z -10.4) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 33.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 25.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.09× (z +8.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 35.1 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.225× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 42.7 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.253× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 50.8 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.232× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 23.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.30× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 55.0 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.310× (z -9.7) |
| [[SW 900 (line)]] | alt | 39.6 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.254× (z -9.8) |
| [[SW48 (line)]] | wt | 55.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.127× (z -9.6) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 37.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.188× (z -9.3) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 95.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.0 | 0 | 0 | — | — |

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
| Name | mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 4L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | mitochondria — chrMT:10,470-10,766 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ND4L, NAD4L; previously MTND4L |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase core subunits; Mitochondrially encoded protein coding genes |
| Reactome | 13 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; tRNA processing in the mitochondrion; Mitochondrial mRNA modification |
| Matched by | ensembl_id |

**Function**, from UniProt [P03901](https://www.uniprot.org/uniprotkb/P03901) (NADH-ubiquinone oxidoreductase chain 4L):

> Core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which catalyzes electron transfer from NADH through the respiratory chain, using ubiquinone as an electron acceptor. Part of the enzyme membrane arm which is embedded in the lipid bilayer and involved in proton translocation.

**Summary**, from NCBI Gene [4539](https://www.ncbi.nlm.nih.gov/gene/4539):

> Enables NADH dehydrogenase (ubiquinone) activity. Predicted to be involved in mitochondrial electron transport, NADH to ubiquinone and proton motive force-driven mitochondrial ATP synthesis. Located in mitochondrial inner membrane. Part of respiratory chain complex I. Implicated in Leber hereditary optic neuropathy and diabetes mellitus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7460](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7460) · Entrez [4539](https://www.ncbi.nlm.nih.gov/gene/4539) · UniProt [P03901](https://www.uniprot.org/uniprotkb/P03901) · Ensembl [ENSG00000212907](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000212907)

## Data

Gene col 13071: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13071); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13071, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13071]; `tensor/DDL_lfc|DDL_z.npy` [13071]; `embed/gene_vectors.npy` [13071]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13071 or target_col == 13071). Every well: [[MT-ND4L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-ND4L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
