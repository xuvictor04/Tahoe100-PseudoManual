---
symbol: "MT-ND6"
type: "gene"
col: 12645
ensembl_id: "ENSG00000198695"
name: "mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 6"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 110.6
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-ND6

*mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 6* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.58× (z +11.5, q 8e-28, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Palmatine (chloride) (drug)]] 5 µM: 1.34× (z +4.2, q 0.003, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.564× (z -8.3, q 5e-14, down in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pentamidine (isethionate) (drug)]] 5 µM in 5 lines (PANC-1 0.315×, A549 0.360×, SW480 0.406×, A498 0.357×, …); [[Larotrectinib sulfate (drug)]] 0.5 µM in 1 line (SW 1088 0.0701×; ⚠ unreliable plate only).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12645.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.58×** | +11.5 | 8e-28 | 48/49 (HT-29, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +10.3 | 1e-22 | 43/44 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.72×** | +9.4 | 7e-19 | 43/45 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +5.1 | 4e-05 | 13/50 (A549, BT-474, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +4.9 | 1e-04 | 37/48 (AsPC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Palmatine (chloride) (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.003 | 26/48 (SNU-423, COLO 205, …) | top dose only | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.005 | 34/47 (HepG2/C3A, NCI-H460, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.005 | 38/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.31×** | +3.8 | 0.008 | 32/48 (HepG2/C3A, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.030 | 32/48 (A-427, LoVo, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.27×** | +3.4 | 0.031 | 28/49 (AsPC-1, HepG2/C3A, …) | top dose only | position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.070 | 26/48 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.070 | 23/48 (LoVo, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 1.76× | +3.0 | 0.10 | 26/49 (A549, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 0.05 µM |  | 1.34× | +3.0 | 0.10 | 27/48 (LS 180, Hs 766T, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12645.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pentamidine (isethionate) (drug)]] 5 µM in 5 lines (PANC-1 0.315×, A549 0.360×, SW480 0.406×, A498 0.357×, …); [[Larotrectinib sulfate (drug)]] 0.5 µM in 1 line (SW 1088 0.0701×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.564×** | -8.3 | 5e-14 | 43/48 (PANC-1, A549, …) | top dose only | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.545×** | -6.2 | 1e-07 | 44/49 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.696×** | -3.7 | 0.029 | 29/48 (AN3 CA, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.697×** | -3.7 | 0.029 | 32/48 (Hs 766T, RKO, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.730× | -3.1 | 0.21 | 23/48 (KATO III, C-33 A, …) | rises with dose | composition shift; position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM |  | 0.729× | -3.0 | 0.25 | 26/48 (SNU-423, NCI-H1573, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12645. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 95.1 | 4 (3 ⚠) | 0 | [[Palmatine (chloride) (drug)]] 5 µM 2.52× (z +10.1) | — |
| [[A549 (line)]] | wt | 140 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +10.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.360× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 105 | 3 (2 ⚠) | 0 | [[Palmatine (chloride) (drug)]] 5 µM 2.63× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 96.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +11.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 77.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 87.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +9.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 90.3 | 3 (2 ⚠) | 0 | [[Palmatine (chloride) (drug)]] 5 µM 2.72× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 124 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 127 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +10.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.406× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 92.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 80.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +8.9) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 89.8 | 2 (1 ⚠) | 0 | [[Palmatine (chloride) (drug)]] 5 µM 4.00× (z +14.5) | — |
| [[H4 (line)]] | wt | 87.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 106 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 86.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +10.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 76.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 85.7 | 1 | 0 | [[Palmatine (chloride) (drug)]] 5 µM 3.12× (z +8.9) | — |
| [[A498 (line)]] | wt | 153 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.357× (z -9.4) |
| [[AN3 CA (line)]] | alt | 108 | 1 | 0 | [[Palmatine (chloride) (drug)]] 5 µM 4.44× (z +11.2) | — |
| [[BT-474 (line)]] | alt | 136 | 1 | 0 | [[Palmatine (chloride) (drug)]] 5 µM 4.51× (z +14.5) | — |
| [[C32 (line)]] | wt | 86.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 83.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +8.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 147 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.399× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 89.6 | 1 | 0 | [[Palmatine (chloride) (drug)]] 5 µM 2.83× (z +10.2) | — |
| [[KATO III (line)]] | alt | 122 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 109 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 146 | 1 | 0 | [[Palmatine (chloride) (drug)]] 5 µM 2.40× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 139 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.315× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 100 | 1 | 0 | [[Palmatine (chloride) (drug)]] 5 µM 3.20× (z +11.4) | — |
| [[SNU-1 (line)]] | wt | 106 | 1 | 0 | [[Palmatine (chloride) (drug)]] 5 µM 2.91× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 144 | 1 | 0 | [[Palmatine (chloride) (drug)]] 5 µM 5.12× (z +16.2) | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Larotrectinib sulfate (drug)]] 0.5 µM 0.0701× (z -9.6) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 92.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 121 | 1 | 0 | [[Palmatine (chloride) (drug)]] 5 µM 3.44× (z +13.9) | — |
| [[A-172 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 93.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 101 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 128 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 105 | 0 | 0 | — | — |

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
| Name | mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | mitochondria — chrMT:14,149-14,673 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NAD6, ND6; previously MTND6 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase core subunits; Mitochondrially encoded protein coding genes |
| Reactome | 15 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; tRNA processing in the mitochondrion; Mitochondrial mRNA modification |
| Matched by | ensembl_id |

**Function**, from UniProt [P03923](https://www.uniprot.org/uniprotkb/P03923) (NADH-ubiquinone oxidoreductase chain 6):

> Core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which catalyzes electron transfer from NADH through the respiratory chain, using ubiquinone as an electron acceptor. Essential for the catalytic activity and assembly of complex I.

**Summary**, from NCBI Gene [4541](https://www.ncbi.nlm.nih.gov/gene/4541):

> Enables NADH dehydrogenase (ubiquinone) activity. Involved in mitochondrial electron transport, NADH to ubiquinone and mitochondrial respiratory chain complex I assembly. Located in mitochondrial inner membrane. Implicated in Leber hereditary optic neuropathy; Leigh disease; and spinal muscular atrophy with lower extremity predominant 2B. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7462](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7462) · Entrez [4541](https://www.ncbi.nlm.nih.gov/gene/4541) · UniProt [P03923](https://www.uniprot.org/uniprotkb/P03923) · Ensembl [ENSG00000198695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198695)

## Data

Gene col 12645: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12645); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12645, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12645]; `tensor/DDL_lfc|DDL_z.npy` [12645]; `embed/gene_vectors.npy` [12645]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12645 or target_col == 12645). Every well: [[MT-ND6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-ND6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
