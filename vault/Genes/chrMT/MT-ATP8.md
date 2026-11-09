---
symbol: "MT-ATP8"
type: "gene"
col: 13632
ensembl_id: "ENSG00000228253"
name: "mitochondrially encoded ATP synthase membrane subunit 8"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 248.21
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-ATP8

*mitochondrially encoded ATP synthase membrane subunit 8* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.70× (z +8.4, q 3e-14, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Docetaxel (Trihydrate) (drug)]] 0.5 µM: 2.04× (z +3.4, q 0.063, up in 48 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (HCT15 8.30×, NCI-H1573 6.99×, A498 6.98×, H4 7.35×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.307× (z -6.4, q 8e-08, down in 47 of 48 measured lines) ⚠ transcription drop. The strongest without an alert is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.453× (z -6.1, q 3e-07, down in 37 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13632.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (HCT15 8.30×, NCI-H1573 6.99×, A498 6.98×, H4 7.35×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.70×** | +8.4 | 3e-14 | 49/49 (HCT15, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.25×** | +6.1 | 3e-07 | 41/44 (A498, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +5.5 | 8e-06 | 44/45 (MIA PaCa-2, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +3.7 | 0.025 | 37/50 (RKO, C32, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +3.5 | 0.054 | 40/47 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **2.04×** | +3.4 | 0.063 | 48/48 (HS-578T, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.81× | +3.2 | 0.12 | 46/48 (A-172, HepG2/C3A, …) | top dose only | position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | 1.83× | +3.1 | 0.14 | 45/48 (SNU-423, SW1417, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13632.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.307×** | -6.4 | 8e-08 | 47/48 (SK-MEL-2, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.453×** | -6.1 | 3e-07 | 37/48 (PANC-1, NCI-H460, …) | top dose only | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.495×** | -3.5 | 0.072 | 46/48 (J82, NCI-H1573, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.529×** | -3.5 | 0.072 | 34/48 (RKO, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.550× | -3.3 | 0.13 | 33/48 (LS 180, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 266 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.78× (z +8.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.239× (z -10.4) |
| [[A549 (line)]] | wt | 274 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +8.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.253× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 226 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.11× (z +8.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.274× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 155 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.52× (z +8.6) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.273× (z -8.8) |
| [[A-427 (line)]] | wt | 253 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.249× (z -9.2) |
| [[A498 (line)]] | wt | 259 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.98× (z +8.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 168 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.35× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 189 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.30× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 178 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.234× (z -10.0) |
| [[Hs 766T (line)]] | wt | 235 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.240× (z -10.4) |
| [[HS-578T (line)]] | alt | 181 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.310× (z -8.5) |
| [[LoVo (line)]] | wt | 264 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.89× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 213 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.09× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 277 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.99× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 357 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.243× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 459 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.261× (z -9.5) |
| [[PANC-1 (line)]] | alt | 317 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.218× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 424 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.126× (z -11.2) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 254 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 322 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.261× (z -9.4) |
| [[A-172 (line)]] | wt | 209 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 225 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 166 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 182 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 244 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 194 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 170 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 260 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 256 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 332 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 196 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 306 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 246 | 0 | 0 | — | — |

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
| Name | mitochondrially encoded ATP synthase membrane subunit 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | mitochondria — chrMT:8,366-8,572 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATP8, A6L, URFA6L; previously MTATP8 |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits; Mitochondrially encoded protein coding genes |
| Reactome | 18 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; Formation of ATP by chemiosmotic coupling; tRNA processing in the mitochondrion |
| Matched by | ensembl_id |

**Function**, from UniProt [P03928](https://www.uniprot.org/uniprotkb/P03928) (ATP synthase F(0) complex subunit 8):

> Subunit 8, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain. ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) region and a stationary …

**Summary**, from NCBI Gene [4509](https://www.ncbi.nlm.nih.gov/gene/4509):

> Contributes to proton-transporting ATP synthase activity, rotational mechanism. Involved in proton motive force-driven mitochondrial ATP synthesis. Located in mitochondrion. Part of proton-transporting ATP synthase complex. Implicated in multiple sclerosis and urinary bladder cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7415](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7415) · Entrez [4509](https://www.ncbi.nlm.nih.gov/gene/4509) · UniProt [P03928](https://www.uniprot.org/uniprotkb/P03928) · Ensembl [ENSG00000228253](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228253)

## Data

Gene col 13632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13632); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13632, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13632]; `tensor/DDL_lfc|DDL_z.npy` [13632]; `embed/gene_vectors.npy` [13632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13632 or target_col == 13632). Every well: [[MT-ATP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-ATP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
