---
symbol: "PTMAP5"
type: "gene"
col: 13181
ensembl_id: "ENSG00000214182"
name: "prothymosin alpha pseudogene 5"
location: "13q31.1"
module: 58
arm: "+"
pooled_cpm: 5.69
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# PTMAP5

*prothymosin alpha pseudogene 5* — 13q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.49× (z +12.0, q 2e-30, up in 9 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Arbutin (drug)]] 5 µM: 1.43× (z +3.4, q 0.058, up in 5 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.549× (z -6.0, q 9e-07, down in 24 of 42 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTMA]] (+0.85, fdr 7e-06), [[A2MP1]] (+0.74, fdr 7e-06), [[PTMAP2]] (+0.72, fdr 7e-06, ⚠ PTMAP2 in the vector space only through flagged drug-doses), [[PODXL2]] (+0.59, fdr 3e-05); moves opposite to [[CBLL1]] (-0.64, fdr 4e-05), [[ZXDB]] (-0.61, fdr 3e-05), [[ZSCAN29]] (-0.60, fdr 5e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CARD6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13181.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.49×** | +12.0 | 2e-30 | 9/10 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +9.5 | 4e-19 | 25/27 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.72×** | +9.2 | 6e-18 | 10/15 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.41×** | +8.7 | 3e-16 | 25/31 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.68×** | +5.1 | 3e-05 | 19/37 (PANC-1, SW480, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.058 | 5/43 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | 1.39× | +3.1 | 0.14 | 7/32 (NCI-H2030, HS-578T, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13181.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.549×** | -6.0 | 9e-07 | 24/42 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.659×** | -5.9 | 9e-07 | 20/42 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.694×** | -3.5 | 0.076 | 18/44 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.704×** | -3.4 | 0.094 | 9/44 (SW48, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.717×** | -3.3 | 0.094 | 10/46 (SW48, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.732× | -3.1 | 0.16 | 12/44 (H4, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.741× | -3.0 | 0.21 | 11/46 (NCI-H1573, HCT15, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13181. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 16.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -9.4) |
| [[SW480 (line)]] | alt | 5.41 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0874× (z -12.5) |
| [[KATO III (line)]] | alt | 5.14 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0835× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 5.20 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.0) |
| [[SHP-77 (line)]] | alt | 6.22 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.05 µM 0.0873× (z -8.6) |
| [[SW1417 (line)]] | alt | 8.94 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.135× (z -8.9) |
| [[A-172 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13181), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTMA]] | +0.85 | +0.90 / +0.72 | both halves | 7e-06 |  |
| [[A2MP1]] | +0.74 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[PTMAP2]] ⚠ | +0.72 | +0.79 / +0.64 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PODXL2]] | +0.59 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[RFX2]] | +0.58 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[METRN]] | +0.58 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[IGFBP2]] | +0.58 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[GUSBP18]] | +0.57 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[CALM3]] | +0.57 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[KIAA1958]] | +0.56 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[PDK3]] | +0.55 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[PDXP]] | +0.55 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[SREBF1]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBLL1]] | -0.64 | -0.68 / -0.40 | both halves | 4e-05 |  |
| [[ZXDB]] | -0.61 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[ZSCAN29]] | -0.60 | -0.63 / -0.39 | both halves | 5e-05 |  |
| [[ZNF621]] | -0.59 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[NME6]] | -0.59 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[ZBED9]] | -0.58 | -0.66 / -0.34 | both halves | 1e-04 |  |
| [[ZNF181]] | -0.57 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[EIF5]] | -0.57 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[ERCC4]] | -0.56 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[ABRAXAS2]] | -0.56 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[RNF6]] | -0.56 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[RIMOC1]] | -0.56 | -0.63 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD6]] | B | CARD6 activity lowers PTMAP5's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.43× higher at baseline in the lines without CARD6 | 0.063 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[PODXL2]] | B | PODXL2 activity raises PTMAP5's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.34× lower at baseline in the lines without PODXL2 | 0.066 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.376). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-55.4, -16.5); signed map (-39.1, 16.4). **Vector** length 50.6, 6.52% of its response variance represented; |z| ≥ 3 in 823 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | -1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +2.2 | +5.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.0 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +0.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.8 | +0.9 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +0.8 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | prothymosin alpha pseudogene 5 |
| Locus type | pseudogene |
| Location | 13q31.1 — chr13:81,690,068-81,690,400 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:9628](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9628) · Entrez [150928](https://www.ncbi.nlm.nih.gov/gene/150928) · Ensembl [ENSG00000214182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214182)

## Data

Gene col 13181: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13181); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13181, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13181]; `tensor/DDL_lfc|DDL_z.npy` [13181]; `embed/gene_vectors.npy` [13181]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13181 or target_col == 13181). Every well: [[PTMAP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTMAP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
