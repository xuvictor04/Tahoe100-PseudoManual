---
symbol: "RMRP"
type: "gene"
col: 15884
ensembl_id: "ENSG00000277027"
name: "RNA component of mitochondrial RNA processing endoribonuclease"
location: "9p13.3"
module: 157
arm: "+"
pooled_cpm: 3.85
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# RMRP

*RNA component of mitochondrial RNA processing endoribonuclease* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.61× (z +10.4, q 1e-22, up in 7 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.95× (z +7.1, q 2e-10, up in 30 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBED6]] (+0.75, fdr 7e-06), [[LENG8]] (+0.72, fdr 1e-05), [[HFM1]] (+0.67, fdr 1e-05); moves opposite to [[MRPS12]] (-0.53, fdr 5e-04), [[MBD4]] (-0.53, fdr 5e-05), [[NDUFA7]] (-0.53, fdr 2e-04).
> It is in [[Module 157]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15884.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.61×** | +10.4 | 1e-22 | 7/7 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.46×** | +9.8 | 4e-20 | 17/19 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.97×** | +8.3 | 1e-14 | 7/9 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.95×** | +7.1 | 2e-10 | 30/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +7.0 | 4e-10 | 26/38 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +4.9 | 1e-04 | 13/27 (A498, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.72×** | +4.5 | 5e-04 | 15/40 (Hs 766T, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +4.5 | 5e-04 | 9/30 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.90×** | +4.2 | 0.002 | 7/22 (A498, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.77×** | +3.5 | 0.028 | 7/34 (LS 180, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.39× | +3.0 | 0.12 | 5/46 (Hs 766T, Panc 03.27, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15884.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bosentan (hydrate) (drug)]] 0.05 µM |  | 0.559× | -3.6 | 0.15 | 14/38 (NCI-H460, LoVo, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.574× | -3.5 | 0.15 | 9/42 (HT-29, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.604× | -3.3 | 0.16 | 19/44 (LOX-IMVI, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Levobupivacaine (hydrochloride) (drug)]] 5 µM |  | 0.588× | -3.2 | 0.17 | 5/42 (A-172, A549, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED6]] | +0.75 | +0.72 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[LENG8]] | +0.72 | +0.53 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[HFM1]] | +0.67 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[GET4]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SCRIB]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[BAG6]] | +0.63 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SRSF1]] | +0.63 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[U2AF2]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[AKT2]] | +0.62 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.62 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[RYR2]] | +0.61 | +0.37 / +0.62 | both halves | 7e-05 |  |
| [[DHFR]] | +0.61 | +0.42 / +0.62 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS12]] | -0.53 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[MBD4]] | -0.53 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[NDUFA7]] | -0.53 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[BFAR]] | -0.52 | -0.25 / -0.57 | both halves | 4e-04 |  |
| [[C16orf91]] | -0.51 | -0.15 / -0.57 | ⚠ one half (not replicated) | 0.001 |  |
| [[RNF181]] | -0.50 | -0.21 / -0.51 | both halves | 6e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.678). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.2, -24.6); signed map (-16.0, -32.5). **Vector** length 50.2, 6.14% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.3 | +2.5 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -0.8 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.6 | -0.3 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.5 | +1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.5 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +1.4 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.2 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | +0.3 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | RNA component of mitochondrial RNA processing endoribonuclease |
| Locus type | RNA, misc (non-coding RNA) |
| Location | 9p13.3 — chr9:35,657,754-35,658,017 (-) |
| Ensembl biotype | ribozyme |
| Also known as | RMRPR, RRP2, NME1; previously CHH |
| Gene groups (HGNC) | RNase MRP complex subunits |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [6023](https://www.ncbi.nlm.nih.gov/gene/6023):

> This gene encodes the RNA component of mitochondrial RNA processing endoribonuclease, which cleaves mitochondrial RNA at a priming site of mitochondrial DNA replication. This RNA also interacts with the telomerase reverse transcriptase catalytic subunit to form a distinct ribonucleoprotein complex that has RNA-dependent RNA polymerase activity and produces double-stranded RNAs that can be processed into small interfering RNA. Mutations in this gene are associated with cartilage-hair …

**Accessions** — [HGNC:10031](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10031) · Entrez [6023](https://www.ncbi.nlm.nih.gov/gene/6023) · Ensembl [ENSG00000277027](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000277027)

## Data

Gene col 15884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15884); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15884]; `tensor/DDL_lfc|DDL_z.npy` [15884]; `embed/gene_vectors.npy` [15884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15884 or target_col == 15884). Every well: [[RMRP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RMRP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
