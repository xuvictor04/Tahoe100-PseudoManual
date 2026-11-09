---
symbol: "KCTD17"
type: "gene"
col: 1944
ensembl_id: "ENSG00000100379"
name: "potassium channel tetramerization domain containing 17"
location: "22q12.3"
module: 83
arm: "-"
pooled_cpm: 3.14
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# KCTD17

*potassium channel tetramerization domain containing 17* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.57× (z +13.8, q 1e-40, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.528× (z -8.3, q 8e-14, down in 21 of 37 measured lines).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ROGDI]] (+0.73, fdr 1e-05), [[RHPN1]] (+0.73, fdr 3e-05), [[PAFAH1B3]] (+0.72, fdr 3e-05); moves opposite to [[MFF-DT]] (-0.70, fdr 7e-05), [[GALNT7-DT]] (-0.67, fdr 5e-05), [[PCBP1-AS1]] (-0.67, fdr 1e-04).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FSD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1944.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.57×** | +13.8 | 1e-40 | 40/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.90×** | +12.4 | 1e-32 | 42/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +11.0 | 6e-26 | 4/5 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.30×** | +10.9 | 3e-25 | 13/15 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.92×** | +9.7 | 3e-20 | 35/45 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +7.3 | 4e-11 | 26/45 (LS 180, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +7.2 | 5e-11 | 5/5 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.97×** | +6.2 | 5e-08 | 26/46 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.87×** | +5.7 | 9e-07 | 7/18 (HS-578T, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +5.0 | 3e-05 | 10/35 (J82, SHP-77, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +4.9 | 6e-05 | 16/41 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.90×** | +4.1 | 0.002 | 6/26 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.08×** | +3.5 | 0.023 | 6/39 (KATO III, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.69×** | +3.4 | 0.031 | 4/33 (PANC-1, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +3.3 | 0.035 | 2/5 (HS-578T, A498) | top dose only | noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.070 | 2/27 (A498, SHP-77) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.070 | 5/32 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1944.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.528×** | -8.3 | 8e-14 | 21/37 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.558×** | -7.6 | 1e-11 | 22/36 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.432×** | -7.3 | 8e-11 | 23/43 (RPMI-7951, C32, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.502×** | -6.3 | 4e-08 | 18/33 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.667×** | -3.7 | 0.020 | 13/44 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.668×** | -3.7 | 0.020 | 11/43 (SW480, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.698×** | -3.3 | 0.078 | 18/42 (RPMI-7951, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.507×** | -3.2 | 0.082 | 13/30 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1944. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 6.82 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0955× (z -8.8) |
| [[LoVo (line)]] | wt | 1.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -9.0) |
| [[PANC-1 (line)]] | alt | 3.85 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -8.6) |
| [[A-172 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.902 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1944), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROGDI]] | +0.73 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[RHPN1]] | +0.73 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[PAFAH1B3]] | +0.72 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[FCHO1]] | +0.70 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[SMARCD3]] | +0.70 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ARRB2]] | +0.70 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[NAA40]] | +0.69 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[STUB1]] | +0.68 | +0.54 / +0.26 | both halves | 4e-04 |  |
| [[PLPPR2]] | +0.67 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[GPRIN1]] | +0.66 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[ANTKMT]] | +0.66 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[HPSE]] | +0.65 | +0.45 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFF-DT]] | -0.70 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[GALNT7-DT]] | -0.67 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[PCBP1-AS1]] | -0.67 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[AP5M1]] | -0.66 | -0.51 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[EFCAB2]] | -0.65 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[CASS4]] | -0.65 | -0.56 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[PBLD]] | -0.65 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[PKN2-AS1]] | -0.63 | -0.43 / -0.23 | both halves | 5e-04 |  |
| [[YARS2]] | -0.63 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[KLRA1P]] | -0.63 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[MMADHC-DT]] | -0.63 | -0.45 / -0.06 | ⚠ not reproduced | 0.005 |  |
| [[ANXA2R-OT1]] | -0.63 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[MAIP1]] | -0.62 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[SEPTIN7-DT]] | -0.62 | -0.45 / -0.24 | both halves | 5e-04 |  |
| [[ZNF460-AS1]] | -0.61 | -0.33 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSD1]] | B | FSD1 activity raises KCTD17's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.62× lower at baseline in the lines without FSD1 | 0.010 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[TMEM92]] | B | TMEM92 activity lowers KCTD17's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.48× higher at baseline in the lines without TMEM92 | 0.013 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[CBLC]] | B | CBLC activity lowers KCTD17's level | lines that do not express CBLC (31) vs lines expressing it (19) | 1.43× higher at baseline in the lines without CBLC | 0.069 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[ATP1A3]] | B | ATP1A3 activity raises KCTD17's level | lines that do not express ATP1A3 (12) vs lines expressing it (38) | 1.44× lower at baseline in the lines without ATP1A3 | 0.081 | ⚠ within organs, on part of the lines; also absent: KIF26A; maybe low, not absent |
| [[VSIR]] | B | VSIR activity lowers KCTD17's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.37× higher at baseline in the lines without VSIR | 0.086 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[RGS14]] | C | RGS14 activity lowers KCTD17's level | lines that do not express RGS14 (4) vs lines expressing it (46) | 1.45× higher at baseline in the lines without RGS14 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.701). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.8, -4.5); signed map (-31.1, 1.3). **Vector** length 59.1, 8.62% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +13.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +7.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +12.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.0 | +9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +4.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +4.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +3.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -8.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:37,051,739-37,063,390 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12242 |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5Z5](https://www.uniprot.org/uniprotkb/Q8N5Z5) (BTB/POZ domain-containing protein KCTD17):

> Substrate-adapter for CUL3-RING ubiquitin ligase complexes which mediates the ubiquitination and subsequent proteasomal degradation of TCHP, a protein involved in ciliogenesis down-regulation. Thereby, positively regulates ciliogenesis, playing a crucial role in the initial steps of axoneme extension. May also play a role in endoplasmic reticulum calcium ion homeostasis.

**Summary**, from NCBI Gene [79734](https://www.ncbi.nlm.nih.gov/gene/79734):

> This gene encodes a protein that belongs to a conserved family of potassium channel tetramerization domain (KCTD)-containing proteins. The encoded protein functions in ciliogenesis by acting as a substrate adaptor for the cullin3-based ubiquitin-conjugating enzyme E3 ligase, and targets trichoplein, a keratin-binding protein, for degradation via polyubiquitinylation. A mutation in this gene is associated with autosomal dominant myoclonic dystonia 26. [provided by RefSeq, Nov 2016]

**Accessions** — [HGNC:25705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25705) · Entrez [79734](https://www.ncbi.nlm.nih.gov/gene/79734) · UniProt [Q8N5Z5](https://www.uniprot.org/uniprotkb/Q8N5Z5) · Ensembl [ENSG00000100379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100379)

## Data

Gene col 1944: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1944); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1944, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1944]; `tensor/DDL_lfc|DDL_z.npy` [1944]; `embed/gene_vectors.npy` [1944]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1944 or target_col == 1944). Every well: [[KCTD17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
