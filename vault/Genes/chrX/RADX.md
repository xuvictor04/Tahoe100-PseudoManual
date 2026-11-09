---
symbol: "RADX"
type: "gene"
col: 7164
ensembl_id: "ENSG00000147231"
name: "RPA1 related single stranded DNA binding protein, X-linked"
location: "Xq22.3"
module: 83
arm: "-"
pooled_cpm: 8.56
n_lines_expressing: 36
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# RADX

*RPA1 related single stranded DNA binding protein, X-linked* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 5.39× (z +21.3, q 0e+00, up in 30 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.636× (z -8.1, q 2e-13, down in 20 of 32 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HACE1]] (+0.67, fdr 1e-05), [[L2HGDH]] (+0.65, fdr 4e-05), [[TMEM14A]] (+0.65, fdr 2e-05); moves opposite to [[ATXN1L]] (-0.68, fdr 2e-05), [[PBLD]] (-0.67, fdr 3e-05), [[UBE3B]] (-0.66, fdr 2e-05).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ENPP4]] → it (grade B ⚠); 3 go from it, the strongest it → [[ZFX]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7164.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **5.39×** | +21.3 | 0e+00 | 30/33 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.92×** | +20.2 | 0e+00 | 32/34 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.88×** | +18.9 | 0e+00 | 33/34 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.71×** | +16.6 | 0e+00 | 31/34 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.68×** | +16.5 | 0e+00 | 29/33 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.13×** | +14.4 | 3e-45 | 32/32 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.52×** | +11.7 | 9e-30 | 27/30 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.02×** | +9.2 | 2e-18 | 26/32 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +8.0 | 1e-13 | 17/28 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +5.6 | 2e-06 | 9/30 (hTERT-HPNE, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.27×** | +5.4 | 3e-06 | 15/32 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.45×** | +4.7 | 1e-04 | 11/33 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.002 | 7/30 (A-427, KATO III, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.002 | 12/33 (NCI-H2030, COLO 205, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.003 | 12/34 (NCI-H23, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.005 | 11/33 (LoVo, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7164.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.636×** | -8.1 | 2e-13 | 20/32 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.612×** | -6.2 | 1e-07 | 18/33 (A498, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.637×** | -5.7 | 2e-06 | 12/32 (A498, A-427, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.784×** | -4.4 | 0.002 | 16/34 (HEC-1-A, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.709×** | -4.2 | 0.003 | 12/31 (A498, SK-MEL-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.757×** | -3.3 | 0.100 | 10/30 (SW 900, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.704× | -3.2 | 0.12 | 10/32 (A498, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 0.842× | -3.1 | 0.13 | 10/34 (KATO III, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7164. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.2 | 7 (2 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 6.67× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 12.6 | 5 | 0 | [[Belinostat (drug)]] 5 µM 8.05× (z +14.1) | — |
| [[H4 (line)]] | wt | 25.4 | 0 | 3 (1 ⚠) | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0811× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 7.15 | 3 | 0 | [[Belinostat (drug)]] 5 µM 15.3× (z +10.6) | — |
| [[A498 (line)]] | wt | 18.5 | 2 | 0 | [[Belinostat (drug)]] 5 µM 4.99× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 7.93 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 8.65× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 7.43 | 1 | 1 | [[Belinostat (drug)]] 5 µM 8.62× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 8.45 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.28× (z +8.7) | — |
| [[SW480 (line)]] | alt | 18.0 | 2 | 0 | [[Panobinostat (drug)]] 0.05 µM 3.18× (z +9.1) | — |
| [[C32 (line)]] | wt | 8.56 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0974× (z -9.6) |
| [[KATO III (line)]] | alt | 14.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.51× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 7.88 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0794× (z -9.2) |
| [[A-172 (line)]] | wt | 0.725 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.879 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.984 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.934 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7164), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACE1]] | +0.67 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[L2HGDH]] | +0.65 | +0.40 / +0.60 | both halves | 4e-05 | same gene group |
| [[TMEM14A]] | +0.65 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[ARRB2]] | +0.63 | +0.30 / +0.54 | both halves | 2e-04 |  |
| [[HMGN3]] | +0.63 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[CDON]] | +0.63 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[PIP4P2]] | +0.63 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[STARD3NL]] | +0.62 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[ARL6]] | +0.62 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[SGSM1]] | +0.61 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[FRRS1]] | +0.60 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[HPSE]] | +0.60 | +0.32 / +0.64 | both halves | 2e-04 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN1L]] | -0.68 | -0.46 / -0.60 | both halves | 2e-05 |  |
| [[PBLD]] | -0.67 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[UBE3B]] | -0.66 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SPRY3]] | -0.65 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[INO80D]] | -0.65 | -0.37 / -0.54 | both halves | 7e-05 |  |
| [[LTO1]] | -0.64 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[MMADHC-DT]] | -0.64 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[BRD1]] | -0.63 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[RNF217-AS1]] | -0.63 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[LINC01004]] | -0.63 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[ITPA]] | -0.63 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[NSD1]] | -0.62 | -0.51 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPP4]] | B | ENPP4 activity raises RADX's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.46× lower at baseline in the lines without ENPP4 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[STARD4]] | C | STARD4 activity raises RADX's level | lines that do not express STARD4 (4) vs lines expressing it (46) | 2.26× lower at baseline in the lines without STARD4 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RNF103-CHMP3; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFX]] | B | RADX activity lowers ZFX's level | lines that do not express RADX (14) vs lines expressing it (36) | 1.15× higher at baseline in the lines without RADX | 0.069 | ⚠ within organs, on part of the lines; also absent: RNF128 |
| [[SCML1]] | B | RADX activity raises SCML1's level | lines that do not express RADX (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without RADX | 0.075 | ⚠ within organs, on part of the lines; also absent: RNF128 |
| [[STARD4]] | B | RADX activity raises STARD4's level | lines that do not express RADX (14) vs lines expressing it (36) | 1.52× lower at baseline in the lines without RADX | 0.093 | ⚠ within organs, on part of the lines; also absent: RNF128 |

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (6.9, 10.4); signed map (-28.7, -7.0). **Vector** length 79.6, 18.0% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +18.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +14.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.6 | +16.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.8 | +11.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +21.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +9.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +4.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | RPA1 related single stranded DNA binding protein, X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:106,611,930-106,679,439 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14191, FLJ10178; previously CXorf57 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NSI4](https://www.uniprot.org/uniprotkb/Q6NSI4) (RPA-related protein RADX):

> Single-stranded DNA-binding protein recruited to replication forks to maintain genome stability. Prevents fork collapse by antagonizing the accumulation of RAD51 at forks to ensure the proper balance of fork remodeling and protection without interfering with the capacity of cells to complete homologous recombination of double-strand breaks.

**Summary**, from NCBI Gene [55086](https://www.ncbi.nlm.nih.gov/gene/55086):

> Enables single-stranded DNA binding activity. Involved in negative regulation of double-strand break repair via homologous recombination. Located in nuclear speck and replication fork. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25486](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25486) · Entrez [55086](https://www.ncbi.nlm.nih.gov/gene/55086) · UniProt [Q6NSI4](https://www.uniprot.org/uniprotkb/Q6NSI4) · Ensembl [ENSG00000147231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147231)

## Data

Gene col 7164: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7164); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7164, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7164]; `tensor/DDL_lfc|DDL_z.npy` [7164]; `embed/gene_vectors.npy` [7164]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7164 or target_col == 7164). Every well: [[RADX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RADX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
