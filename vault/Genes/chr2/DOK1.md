---
symbol: "DOK1"
type: "gene"
col: 3660
ensembl_id: "ENSG00000115325"
name: "docking protein 1"
location: "2p13.1"
module: 7
arm: "+"
pooled_cpm: 3.53
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# DOK1

*docking protein 1* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.55× (z +8.7, q 2e-15, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +6.1, q 3e-07, up in 10 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.521× (z -6.3, q 1e-07, down in 17 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOE1]] (+0.59, fdr 1e-05), [[WNT3]] (+0.58, fdr 3e-05), [[ZNF32]] (+0.58, fdr 4e-05); moves opposite to [[AP3S1]] (-0.48, fdr 5e-05), [[MAGT1]] (-0.48, fdr 8e-05), [[SEPTIN2]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BOLA3-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3660.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +8.7 | 2e-15 | 2/4 (NCI-H460, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.1 | 3e-07 | 10/31 (HOP62, HCT15, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.0 | 1e-04 | 3/14 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.9 | 2e-04 | 5/16 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +4.7 | 2e-04 | 6/18 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +4.1 | 0.003 | 2/5 (SW480, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.39× | +3.1 | 0.14 | 3/30 (SW480, RKO, …) | top dose only |  |
| [[Saquinavir (drug)]] 0.5 µM |  | 1.38× | +3.1 | 0.14 | 6/32 (NCI-H460, PANC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3660.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.521×** | -6.3 | 1e-07 | 17/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.559×** | -5.7 | 4e-06 | 18/33 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.617×** | -4.7 | 5e-04 | 18/40 (SNU-1, SW480, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.665×** | -4.0 | 0.009 | 15/40 (hTERT-HPNE, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.666×** | -4.0 | 0.009 | 12/25 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.687×** | -3.7 | 0.023 | 14/41 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3660. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.69 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 6.24 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0679× (z -8.8) |
| [[LoVo (line)]] | wt | 2.50 | 0 | 1 | — | [[Finasteride (drug)]] 0.05 µM 0.0579× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 8.44 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0737× (z -13.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.878 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.877 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.919 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3660), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOE1]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[WNT3]] | +0.58 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[ZNF32]] | +0.58 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[ZBTB45]] | +0.55 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[GINS3]] | +0.54 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[MRM1]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[DDX28]] | +0.53 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[ZNF691]] | +0.52 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[TMEM147-AS1]] | +0.52 | +0.60 / +0.36 | both halves | 1e-04 |  |
| [[HPS6]] | +0.52 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[TMEM17]] | +0.51 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[GABPB1]] | +0.51 | +0.48 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP3S1]] | -0.48 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[MAGT1]] | -0.48 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[SEPTIN2]] | -0.47 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[VAMP7]] | -0.45 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[STAT3]] | -0.44 | -0.39 / -0.38 | both halves | 6e-05 | pathway: Signaling by Non-Receptor Tyrosine Kinases |
| [[OS9]] | -0.44 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[PTTG1IP]] | -0.43 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[CCNG1]] | -0.43 | -0.32 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3-DT]] | B | BOLA3-DT activity raises DOK1's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 1.38× lower at baseline in the lines without BOLA3-DT | 0.032 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[GABBR2]] | B | GABBR2 activity raises DOK1's level | lines that do not express GABBR2 (25) vs lines expressing it (25) | 1.32× lower at baseline in the lines without GABBR2 | 0.060 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, LMX1B; maybe low, not absent |
| [[ARHGEF25]] | B | ARHGEF25 activity raises DOK1's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 1.11× lower at baseline in the lines without ARHGEF25 | 0.079 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10 |
| [[DLX1]] | B | DLX1 activity raises DOK1's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 1.17× lower at baseline in the lines without DLX1 | 0.083 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.454). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-30.5, 17.6); signed map (-3.7, -28.7). **Vector** length 39.9, 4.25% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +4.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.6 | +4.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +0.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.8 | +1.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +0.8 | +2.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -4.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.4 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.4 | -3.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | docking protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,549,026-74,557,551 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p62dok |
| Gene groups (HGNC) | Docking protein family |
| Reactome | 6 pathways, smallest: PTK6 Regulates RTKs and Their Effectors AKT1 and DOK1; RET signaling; Signaling by Non-Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99704](https://www.uniprot.org/uniprotkb/Q99704) (Docking protein 1):

> DOK proteins are enzymatically inert adaptor or scaffolding proteins. They provide a docking platform for the assembly of multimolecular signaling complexes. DOK1 appears to be a negative regulator of the insulin signaling pathway. Modulates integrin activation by competing with talin for the same binding site on ITGB3.

**Summary**, from NCBI Gene [1796](https://www.ncbi.nlm.nih.gov/gene/1796):

> The protein encoded by this gene is part of a signal transduction pathway downstream of receptor tyrosine kinases. The encoded protein is a scaffold protein that helps form a platform for the assembly of multiprotein signaling complexes. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:2990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2990) · Entrez [1796](https://www.ncbi.nlm.nih.gov/gene/1796) · UniProt [Q99704](https://www.uniprot.org/uniprotkb/Q99704) · Ensembl [ENSG00000115325](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115325)

## Data

Gene col 3660: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3660); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3660, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3660]; `tensor/DDL_lfc|DDL_z.npy` [3660]; `embed/gene_vectors.npy` [3660]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3660 or target_col == 3660). Every well: [[DOK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
