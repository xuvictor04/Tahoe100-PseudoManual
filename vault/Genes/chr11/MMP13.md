---
symbol: "MMP13"
type: "gene"
col: 6059
ensembl_id: "ENSG00000137745"
name: "matrix metallopeptidase 13"
location: "11q22.2"
module: 70
arm: "+"
pooled_cpm: 2.46
n_lines_expressing: 20
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 52
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# MMP13

*matrix metallopeptidase 13* — 11q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.54× (z +11.2, q 2e-26, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 3.68× (z +10.6, q 8e-24, up in 14 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.487× (z -4.2, q 0.016, down in 8 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBP4]] (+0.65, fdr 7e-06), [[CFB]] (+0.64, fdr 1e-05), [[GBP2]] (+0.64, fdr 1e-05); moves opposite to [[PYGB]] (-0.50, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MX2]] → it (grade B ⚠); 52 go from it, the strongest it → [[MX2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6059.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.54×** | +11.2 | 2e-26 | 1/4 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.68×** | +10.6 | 8e-24 | 14/16 (BT-474, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.33×** | +8.9 | 9e-17 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.16×** | +8.2 | 3e-14 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.16×** | +6.6 | 4e-09 | 11/13 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +6.6 | 4e-09 | 2/11 (HOP62, BT-474) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +4.6 | 3e-04 | 6/15 (BT-474, SW 900, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.23×** | +4.6 | 3e-04 | 0/15 | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +4.5 | 5e-04 | 0/5 | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.21×** | +4.4 | 6e-04 | 0/5 | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.07×** | +4.2 | 0.002 | 1/4 (CFPAC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **2.02×** | +4.0 | 0.002 | 0/6 | inconsistent across doses | low cells (technical?) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.66×** | +4.0 | 0.003 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +3.9 | 0.005 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.44×** | +3.7 | 0.009 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.024 | 1/16 (BT-474) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.029 | 2/11 (NCI-H2347, CFPAC-1) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Saquinavir (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.042 | 1/11 (NCI-H2347) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6059.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.487×** | -4.2 | 0.016 | 8/17 (NCI-H2347, SW 900, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.645×** | -3.6 | 0.086 | 1/16 (KATO III) | rises with dose | position effect removed |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.521×** | -3.5 | 0.089 | 2/17 (BT-474, HT-29) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.676× | -3.2 | 0.18 | 7/15 (SW 900, NCI-H2347, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6059. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 12.4 | 4 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 9.04× (z +12.4) | [[Tofacitinib (drug)]] 5 µM 0.0812× (z -14.2) |
| [[BT-474 (line)]] | alt | 11.1 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 28.6× (z +12.8) | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.26× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 65.4 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.132× (z -9.0) |
| [[A-172 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.193 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.637 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.921 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.926 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.960 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.682 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.897 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.880 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.204 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.267 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.266 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6059), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP4]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[CFB]] | +0.64 | +0.57 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[GBP2]] | +0.64 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[APOL3]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[IDO1]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[TNFSF10]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[HLA-F]] | +0.60 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ETV7]] | +0.60 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[CD5L]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[HERC5]] | +0.60 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[GPR158]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[SYTL2]] | +0.58 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYGB]] | -0.50 | -0.49 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MX2]] | B | MX2 activity raises MMP13's level | lines that do not express MX2 (16) vs lines expressing it (34) | 1.71× lower at baseline in the lines without MX2 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[BST2]] | C | BST2 activity raises MMP13's level | lines that do not express BST2 (18) vs lines expressing it (32) | 1.77× lower at baseline in the lines without BST2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3; co-absent with the target |
| [[CD74]] | C | CD74 activity raises MMP13's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.68× lower at baseline in the lines without CD74 | 0.033 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5; co-absent with the target |

### Downstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 40, C 12. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MX2]] | B | MMP13 activity raises MX2's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 3.09× lower at baseline in the lines without MMP13 | 0.003 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[FBXO39]] | B | MMP13 activity raises FBXO39's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without MMP13 | 0.003 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[XAF1]] | B | MMP13 activity raises XAF1's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.68× lower at baseline in the lines without MMP13 | 0.004 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[TMEM140]] | B | MMP13 activity raises TMEM140's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 1.87× lower at baseline in the lines without MMP13 | 0.004 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[GBP2]] | B | MMP13 activity raises GBP2's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.92× lower at baseline in the lines without MMP13 | 0.005 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[FBXO32]] | B | MMP13 activity raises FBXO32's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.46× lower at baseline in the lines without MMP13 | 0.006 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[SAMD9]] | B | MMP13 activity raises SAMD9's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.67× lower at baseline in the lines without MMP13 | 0.007 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[GBP1]] | B | MMP13 activity raises GBP1's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without MMP13 | 0.008 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[RND1]] | B | MMP13 activity raises RND1's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 1.86× lower at baseline in the lines without MMP13 | 0.008 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[OAS2]] | B | MMP13 activity raises OAS2's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without MMP13 | 0.008 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[SAMD9L]] | B | MMP13 activity raises SAMD9L's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 3.02× lower at baseline in the lines without MMP13 | 0.008 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[ATP1B1]] | B | MMP13 activity raises ATP1B1's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.33× lower at baseline in the lines without MMP13 | 0.008 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.3, 50.5); signed map (60.7, 28.6). **Vector** length 43.3, 10.5% of its response variance represented; |z| ≥ 3 in 500 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon gamma signaling* (reactome, mean cos +0.52 to 13); *Interferon alpha/beta signaling* (reactome, mean cos +0.51 to 10); *Interferon Signaling* (reactome, mean cos +0.52 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +10.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +6.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.3 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +2.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -4.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | matrix metallopeptidase 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.2 — chr11:102,942,995-102,955,732 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLG3 |
| Gene groups (HGNC) | Receptor ligands; M10 matrix metallopeptidases |
| Hallmark sets | COMPLEMENT |
| Reactome | 8 pathways, smallest: RUNX2 regulates genes involved in cell migration; Activation of Matrix Metalloproteinases; Collagen degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P45452](https://www.uniprot.org/uniprotkb/P45452) (Collagenase 3):

> Plays a role in the degradation of extracellular matrix proteins including fibrillar collagen, fibronectin, TNC and ACAN. Cleaves triple helical collagens, including type I, type II and type III collagen, but has the highest activity with soluble type II collagen. Can also degrade collagen type IV, type XIV and type X. May also function by activating or degrading key regulatory proteins, such as TGFB1 and CCN2. Plays a role in wound healing, tissue remodeling, cartilage degradation, bone …

**Summary**, from NCBI Gene [4322](https://www.ncbi.nlm.nih.gov/gene/4322):

> This gene encodes a member of the peptidase M10 family of matrix metalloproteinases (MMPs). Proteins in this family are involved in the breakdown of extracellular matrix in normal physiological processes, such as embryonic development, reproduction, and tissue remodeling, as well as in disease processes, such as arthritis and metastasis. The encoded preproprotein is proteolytically processed to generate the mature protease. This protease cleaves type II collagen more efficiently than types I …

**Accessions** — [HGNC:7159](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7159) · Entrez [4322](https://www.ncbi.nlm.nih.gov/gene/4322) · UniProt [P45452](https://www.uniprot.org/uniprotkb/P45452) · Ensembl [ENSG00000137745](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137745)

## Data

Gene col 6059: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6059); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6059, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6059]; `tensor/DDL_lfc|DDL_z.npy` [6059]; `embed/gene_vectors.npy` [6059]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6059 or target_col == 6059). Every well: [[MMP13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMP13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
