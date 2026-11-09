---
symbol: "TMEM199"
type: "gene"
col: 14388
ensembl_id: "ENSG00000244045"
name: "vacuolar ATPase assembly factor VMA12"
location: "17q11.2"
module: 7
arm: "+"
pooled_cpm: 8.15
n_lines_expressing: 50
n_dd_up: 43
n_dd_down: 3
n_dd_up_clean: 28
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TMEM199

*vacuolar ATPase assembly factor VMA12* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +14.4, q 4e-44, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.769× (z -5.4, q 4e-05, down in 18 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMG8]] (+0.75, fdr 7e-06), [[SMCR8]] (+0.74, fdr 7e-06), [[TSSC4]] (+0.73, fdr 7e-06); moves opposite to [[PCMT1]] (-0.60, fdr 1e-04), [[INPP5F]] (-0.59, fdr 4e-05), [[LPCAT2]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14388.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +14.4 | 4e-44 | 40/43 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +13.5 | 6e-39 | 28/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.55×** | +13.4 | 8e-39 | 41/47 (PANC-1, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.25×** | +11.6 | 4e-29 | 33/40 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.96×** | +9.2 | 3e-18 | 29/45 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +8.9 | 6e-17 | 13/23 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.6 | 3e-12 | 24/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +6.9 | 5e-10 | 26/46 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +6.7 | 2e-09 | 21/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +6.1 | 8e-08 | 21/46 (SK-MEL-2, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +6.0 | 8e-08 | 13/36 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.52×** | +5.7 | 5e-07 | 18/42 (SW480, NCI-H2030, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +5.6 | 1e-06 | 19/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.49×** | +5.5 | 1e-06 | 16/45 (BT-474, NCI-H2030, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +5.4 | 2e-06 | 16/46 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +5.3 | 4e-06 | 19/43 (HOP62, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +5.2 | 5e-06 | 13/46 (KATO III, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.97×** | +5.1 | 1e-05 | 18/40 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +4.8 | 5e-05 | 14/46 (NCI-H1573, HCT15, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14388.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.769×** | -5.4 | 4e-05 | 18/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.703×** | -5.1 | 9e-05 | 16/46 (HCT15, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.748×** | -4.1 | 0.009 | 15/45 (AsPC-1, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14388. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 11.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 9.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 9.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 9.71 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0467× (z -12.4) |
| [[SW48 (line)]] | wt | 6.72 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.05 µM 0.0479× (z -9.1) |
| [[A-172 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14388), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG8]] | +0.75 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[SMCR8]] | +0.74 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[TSSC4]] | +0.73 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.72 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[WDR81]] | +0.72 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[PEF1]] | +0.72 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[CHTF8]] | +0.71 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[FEM1A]] | +0.69 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[MOCS3]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[SLC38A7]] | +0.68 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[MRM3]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[DNAJB12]] | +0.68 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMT1]] | -0.60 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[INPP5F]] | -0.59 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[LPCAT2]] | -0.59 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[RADX]] | -0.59 | -0.43 / -0.46 | both halves | 3e-05 | same gene group |
| [[FCHO1]] | -0.59 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMEM199's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.780). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-39.7, 11.2); signed map (-7.4, -20.6). **Vector** length 64.5, 9.77% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.9 | +13.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +14.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +6.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +4.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | vacuolar ATPase assembly factor VMA12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,357,642-28,363,683 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VPH2, MGC45714; previously TMEM199, C17orf32 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N511](https://www.uniprot.org/uniprotkb/Q8N511) (Vacuolar ATPase assembly protein VMA12):

> Accessory component of the proton-transporting vacuolar (V)-ATPase protein pump involved in intracellular iron homeostasis. In aerobic conditions, required for intracellular iron homeostasis, thus triggering the activity of Fe(2+) prolyl hydroxylase (PHD) enzymes, and leading to HIF1A hydroxylation and subsequent proteasomal degradation. Necessary for endolysosomal acidification and lysosomal degradation. May be involved in Golgi homeostasis. Binds 20(S)-hydroxycholesterol (20(S)-OHC) (By …

**Summary**, from NCBI Gene [147007](https://www.ncbi.nlm.nih.gov/gene/147007):

> The protein encoded by this gene has been observed to localize to the endoplasmic reticulum (ER)-Golgi intermediate compartment (ERGIC) and coat protein complex I (COPI) in some human cells. The encoded protein shares some homology with the yeast protein Vma12. Defects in this gene are a cause of congenital disorder of glycosylation, type IIp. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:18085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18085) · Entrez [147007](https://www.ncbi.nlm.nih.gov/gene/147007) · UniProt [Q8N511](https://www.uniprot.org/uniprotkb/Q8N511) · Ensembl [ENSG00000244045](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244045)

## Data

Gene col 14388: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14388); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14388, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14388]; `tensor/DDL_lfc|DDL_z.npy` [14388]; `embed/gene_vectors.npy` [14388]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14388 or target_col == 14388). Every well: [[TMEM199 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM199.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
