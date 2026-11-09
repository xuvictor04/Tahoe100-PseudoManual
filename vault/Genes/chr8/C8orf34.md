---
symbol: "C8orf34"
type: "gene"
col: 9063
ensembl_id: "ENSG00000165084"
name: "chromosome 8 open reading frame 34"
location: "8q13.2"
module: 140
arm: "+"
pooled_cpm: 2.42
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# C8orf34

*chromosome 8 open reading frame 34* — 8q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.62× (z +18.3, q 0e+00, up in 28 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.812× (z -7.4, q 9e-11, down in 31 of 47 measured lines) ⚠ position not correctable.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC4C]] (+0.82, fdr 7e-06), [[GALNTL6]] (+0.81, fdr 7e-06), [[USH2A]] (+0.81, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9063.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.62×** | +18.3 | 0e+00 | 28/29 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.04×** | +14.1 | 2e-42 | 9/12 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +11.1 | 2e-26 | 0/0 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.94×** | +10.1 | 1e-21 | 1/2 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +8.8 | 1e-16 | 20/32 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.38×** | +8.5 | 2e-15 | 22/40 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +6.6 | 4e-09 | 16/43 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.46×** | +4.7 | 1e-04 | 1/3 (J82) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.33×** | +4.4 | 5e-04 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.2 | 0.001 | 5/35 (SW480, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.1 | 0.002 | 9/35 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.50×** | +4.1 | 0.002 | 3/37 (HOP62, Panc 03.27, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.005 | 9/27 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Neratinib (drug)]] 0.05 µM |  | **1.44×** | +3.7 | 0.009 | 4/34 (SW 900, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.5 | 0.017 | 1/9 (SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.023 | 6/31 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.093 | 3/33 (NCI-H23, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9063.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.812×** | -7.4 | 9e-11 | 31/47 (RPMI-7951, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9063. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.4× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 1.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.59× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 2.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.38× (z +8.7) | — |
| [[SW480 (line)]] | alt | 1.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.62× (z +8.5) | — |
| [[A-172 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9063), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC4C]] | +0.82 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.81 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[USH2A]] | +0.81 | +0.71 / +0.80 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.79 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.79 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[SORCS3]] | +0.79 | +0.65 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[LINC00861]] | +0.79 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.77 | +0.61 / +0.78 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.77 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[TTN]] | +0.76 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[MEIOC]] | +0.75 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[GALNT17]] | +0.75 | +0.63 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.871). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.7, 28.7); signed map (33.0, 13.6). **Vector** length 40.5, 4.21% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +18.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +14.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -7.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.0 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 8 open reading frame 34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.2 — chr8:68,330,955-68,819,023 (+) |
| Ensembl biotype | protein_coding |
| Also known as | vest-1, VEST1 |
| Matched by | ensembl_id |

UniProt [Q49A92](https://www.uniprot.org/uniprotkb/Q49A92) carries no function annotation.

**Summary**, from NCBI Gene [116328](https://www.ncbi.nlm.nih.gov/gene/116328):

> This gene encodes a protein that is related to the cyclic AMP dependent protein kinase regulators. Naturally occurring mutations in this gene are associated with an increased risk for severe toxicities, such as diarrhea and neutropenia, in patients undergoing chemotherapeutic treatment. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:30905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30905) · Entrez [116328](https://www.ncbi.nlm.nih.gov/gene/116328) · UniProt [Q49A92](https://www.uniprot.org/uniprotkb/Q49A92) · Ensembl [ENSG00000165084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165084)

## Data

Gene col 9063: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9063); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9063, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9063]; `tensor/DDL_lfc|DDL_z.npy` [9063]; `embed/gene_vectors.npy` [9063]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9063 or target_col == 9063). Every well: [[C8orf34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C8orf34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
