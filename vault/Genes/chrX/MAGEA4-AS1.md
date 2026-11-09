---
symbol: "MAGEA4-AS1"
type: "gene"
col: 13724
ensembl_id: "ENSG00000229967"
name: "MAGEA4 antisense RNA 1"
location: "Xq28"
module: 109
arm: "+"
pooled_cpm: 3.23
n_lines_expressing: 9
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# MAGEA4-AS1

*MAGEA4 antisense RNA 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.92× (z +9.2, q 1e-17, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +4.2, q 0.002, up in 0 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX10]] (+0.52, fdr 3e-05), [[CD163L1]] (+0.51, fdr 3e-05), [[NSUN6]] (+0.50, fdr 4e-05); moves opposite to [[MAPK4]] (-0.45, fdr 2e-04), [[ADAM15]] (-0.44, fdr 1e-04), [[PPA1]] (-0.40, fdr 1e-04).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → [[ZNF397]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13724.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.92×** | +9.2 | 1e-17 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.50×** | +9.2 | 1e-17 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.39×** | +7.3 | 4e-11 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.54×** | +5.0 | 8e-05 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.49×** | +4.7 | 3e-04 | 2/5 (NCI-H1573, A-427) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.33×** | +4.4 | 0.001 | 2/6 (C-33 A, SHP-77) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.06×** | +4.3 | 0.001 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +4.2 | 0.002 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +4.2 | 0.002 | 3/7 (SHP-77, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.54×** | +3.6 | 0.021 | 1/5 (SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.44×** | +3.4 | 0.033 | 1/5 (A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.037 | 3/6 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +3.3 | 0.048 | 0/6 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.049 | 0/7 | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.2 | 0.050 | 2/6 (C-33 A, NCI-H23) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.78×** | +3.1 | 0.072 | 3/5 (C-33 A, A-427, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +3.1 | 0.072 | 4/7 (SHP-77, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13724.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.525× | -3.2 | 0.63 | 0/7 | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.543× | -3.1 | 0.63 | 3/7 (C-33 A, A-427, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.227 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.302 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.377 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.271 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX10]] | +0.52 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[CD163L1]] | +0.51 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[NSUN6]] | +0.50 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[ST20-MTHFS]] | +0.50 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[ADGRG7]] | +0.49 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[DGUOK]] | +0.49 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[MYOM1]] | +0.49 | +0.49 / +0.38 | both halves | 7e-05 |  |
| [[ASTL]] | +0.48 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[MAGEA4]] | +0.47 | +0.45 / +0.51 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NOS1]] | +0.47 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[TADA3]] | +0.47 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[PIK3IP1-DT]] | +0.46 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[OFD1]] | +0.46 | +0.41 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK4]] | -0.45 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[ADAM15]] | -0.44 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[PPA1]] | -0.40 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[TRAF6]] | -0.39 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[OPN3]] | -0.39 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[MAP2]] | -0.38 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[SLC35A3]] | -0.38 | -0.37 / -0.30 | both halves | 2e-04 |  |
| [[CNN3]] | -0.37 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[AP3M1]] | -0.37 | -0.23 / -0.38 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF397]] | B | MAGEA4-AS1 activity raises ZNF397's level | lines that do not express MAGEA4-AS1 (41) vs lines expressing it (9) | 1.70× lower at baseline in the lines without MAGEA4-AS1 | 0.024 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[SYT5]] | B | MAGEA4-AS1 activity raises SYT5's level | lines that do not express MAGEA4-AS1 (41) vs lines expressing it (9) | 1.61× lower at baseline in the lines without MAGEA4-AS1 | 0.035 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[CDKL3]] | B | MAGEA4-AS1 activity raises CDKL3's level | lines that do not express MAGEA4-AS1 (41) vs lines expressing it (9) | 1.49× lower at baseline in the lines without MAGEA4-AS1 | 0.040 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[MYOM1]] | B | [[MAGEA4]], MAGEA4-AS1 activity raises MYOM1's level | lines that do not express MAGEA4, MAGEA4-AS1 (41) vs lines expressing them (9) | 2.69× lower at baseline in the lines without MAGEA4, MAGEA4-AS1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, GCG; co-absent genes |
| [[ENO3]] | B | MAGEA4-AS1 activity raises ENO3's level | lines that do not express MAGEA4-AS1 (41) vs lines expressing it (9) | 2.10× lower at baseline in the lines without MAGEA4-AS1 | 0.091 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[CLBA1]] | B | MAGEA4-AS1 activity raises CLBA1's level | lines that do not express MAGEA4-AS1 (41) vs lines expressing it (9) | 1.41× lower at baseline in the lines without MAGEA4-AS1 | 0.098 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.359). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.8, -6.3); signed map (15.9, 20.1). **Vector** length 19.2, 5.96% of its response variance represented; |z| ≥ 3 in 124 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.8 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.7 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +0.7 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.6 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.5 | +3.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +0.4 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.4 | +0.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.4 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | +1.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.5 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.5 | -1.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.5 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | MAGEA4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq28 — chrX:151,904,431-151,913,968 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53860](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53860) · Entrez [105373368](https://www.ncbi.nlm.nih.gov/gene/105373368) · Ensembl [ENSG00000229967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229967)

## Data

Gene col 13724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13724); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13724]; `tensor/DDL_lfc|DDL_z.npy` [13724]; `embed/gene_vectors.npy` [13724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13724 or target_col == 13724). Every well: [[MAGEA4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGEA4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
