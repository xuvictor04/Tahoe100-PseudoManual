---
symbol: "TMEFF2"
type: "gene"
col: 6866
ensembl_id: "ENSG00000144339"
name: "transmembrane protein with EGF like and two follistatin like domains 2"
location: "2q32.3"
module: 61
arm: "+"
pooled_cpm: 2.65
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# TMEFF2

*transmembrane protein with EGF like and two follistatin like domains 2* — 2q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 15.6× (z +23.8, q 0e+00, up in 33 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGCZ]] (+0.70, fdr 7e-06), [[PLCL1]] (+0.69, fdr 7e-06), [[GPM6A]] (+0.68, fdr 7e-06); moves opposite to [[DZANK1]] (-0.48, fdr 3e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FAM133A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6866.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **15.6×** | +23.8 | 0e+00 | 33/46 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.49×** | +22.9 | 0e+00 | 26/28 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **12.6×** | +21.9 | 0e+00 | 31/43 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.11×** | +19.9 | 0e+00 | 27/30 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **4.90×** | +19.4 | 0e+00 | 34/43 (NCI-H460, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **7.97×** | +17.9 | 0e+00 | 31/44 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.59×** | +10.6 | 2e-24 | 3/4 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.33×** | +10.4 | 2e-23 | 22/27 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.18×** | +10.0 | 1e-21 | 19/34 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.13×** | +9.9 | 3e-21 | 24/46 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.97×** | +9.4 | 3e-19 | 8/13 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.09×** | +9.4 | 3e-19 | 22/37 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.75×** | +8.7 | 1e-16 | 26/40 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.73×** | +8.4 | 3e-15 | 20/32 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +8.2 | 7e-15 | 3/4 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +7.1 | 6e-11 | 11/25 (A-172, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.72×** | +5.9 | 1e-07 | 17/36 (NCI-H460, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +5.5 | 1e-06 | 10/36 (SK-MEL-2, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6866.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.875× | -4.1 | 0.023 | 15/48 (LoVo, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6866. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 19.1 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +15.9) | — |
| [[HOP62 (line)]] | alt | 1.97 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +11.1) | — |
| [[J82 (line)]] | alt | 4.81 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 60.8× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 2.96 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 21.7× (z +15.3) | — |
| [[LOX-IMVI (line)]] | wt | 3.00 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 80.8× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 1.23 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 39.8× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 4.68 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 68.9× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 5.42 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 27.6× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 2.51 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 28.3× (z +9.8) | — |
| [[A549 (line)]] | wt | 2.22 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 50.8× (z +8.8) | — |
| [[C32 (line)]] | wt | 1.45 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 22.6× (z +8.8) | — |
| [[H4 (line)]] | wt | 2.61 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 89.1× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 1.48 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 59.3× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 1.85 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 42.2× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 8.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.22× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 2.15 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 52.2× (z +8.5) | — |
| [[A-427 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.896 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.985 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6866), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGCZ]] | +0.70 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[PLCL1]] | +0.69 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[GPM6A]] | +0.68 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[SNTG2]] | +0.67 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[LINC02511]] | +0.63 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[DACH2]] | +0.63 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[PPFIA2]] | +0.63 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[COL25A1]] | +0.62 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[SLC35F1]] | +0.62 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.62 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[KCNB1]] | +0.62 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[TMEM266]] | +0.61 | +0.52 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZANK1]] | -0.48 | -0.28 / -0.46 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM133A]] | B | FAM133A activity raises TMEFF2's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 1.84× lower at baseline in the lines without FAM133A | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4 |
| [[SYT12]] | B | SYT12 activity lowers TMEFF2's level | lines that do not express SYT12 (9) vs lines expressing it (41) | 1.34× higher at baseline in the lines without SYT12 | 0.050 | ⚠ within organs, on part of the lines; also absent: EMSLR; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers TMEFF2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KLF5]] | B | KLF5 activity weakens TMEFF2's drug response | lines that do not express KLF5 (16) vs lines expressing it (30) | the lines without KLF5 respond 1.40× as strongly (z diff -1.79); strongest at Panobinostat 0.05 µM: 6.73x vs 2.64x (z diff -2.7) | 0.073 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[FMN2]] | B | FMN2 activity raises TMEFF2's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 1.85× lower at baseline in the lines without FMN2 | 0.077 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent |
| [[SYT11]] | B | SYT11 activity raises TMEFF2's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 1.67× lower at baseline in the lines without SYT11 | 0.097 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.5, 30.7); signed map (32.3, 23.3). **Vector** length 56.0, 8.20% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +19.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +19.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +22.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.2 | +9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +5.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein with EGF like and two follistatin like domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.3 — chr2:191,949,043-192,194,933 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TENB2, HPP1, TR, TPEF, CT120.2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIK5](https://www.uniprot.org/uniprotkb/Q9UIK5) (Tomoregulin-2):

> May be a survival factor for hippocampal and mesencephalic neurons. The shedded form up-regulates cancer cell proliferation, probably by promoting ERK1/2 phosphorylation.

**Summary**, from NCBI Gene [23671](https://www.ncbi.nlm.nih.gov/gene/23671):

> This gene encodes a member of the tomoregulin family of transmembrane proteins. This protein has been shown to function as both an oncogene and a tumor suppressor depending on the cellular context and may regulate prostate cancer cell invasion. Multiple soluble forms of this protein have been identified that arise from both an alternative splice variant and ectodomain shedding. Additionally, this gene has been found to be hypermethylated in multiple cancer types. Alternative splicing results in …

**Accessions** — [HGNC:11867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11867) · Entrez [23671](https://www.ncbi.nlm.nih.gov/gene/23671) · UniProt [Q9UIK5](https://www.uniprot.org/uniprotkb/Q9UIK5) · Ensembl [ENSG00000144339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144339)

## Data

Gene col 6866: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6866); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6866, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6866]; `tensor/DDL_lfc|DDL_z.npy` [6866]; `embed/gene_vectors.npy` [6866]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6866 or target_col == 6866). Every well: [[TMEFF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEFF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
