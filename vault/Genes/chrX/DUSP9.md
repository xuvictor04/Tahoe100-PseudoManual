---
symbol: "DUSP9"
type: "gene"
col: 5139
ensembl_id: "ENSG00000130829"
name: "dual specificity phosphatase 9"
location: "Xq28"
module: 45
arm: "+"
pooled_cpm: 2.16
n_lines_expressing: 33
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# DUSP9

*dual specificity phosphatase 9* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.47× (z +10.3, q 3e-22, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.66× (z +5.1, q 4e-05, up in 7 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.385× (z -6.9, q 4e-09, down in 13 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OTX1]] (+0.66, fdr 1e-05), [[SEPTIN6]] (+0.59, fdr 3e-05), [[ANO8]] (+0.58, fdr 2e-05); moves opposite to [[HEXIM2-AS1]] (-0.52, fdr 1e-04), [[RAB30-DT]] (-0.52, fdr 1e-04), [[CLHC1]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TBX1]] → it (grade B ⚠); 4 go from it, the strongest it → [[CFD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5139.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.47×** | +10.3 | 3e-22 | 3/4 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.19×** | +8.3 | 3e-14 | 5/7 (HepG2/C3A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.26×** | +5.8 | 1e-06 | 3/10 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +5.1 | 4e-05 | 7/25 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +4.7 | 3e-04 | 1/4 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.67×** | +4.5 | 6e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.73×** | +3.8 | 0.014 | 1/4 (HepG2/C3A) | top dose only | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +3.4 | 0.043 | 1/22 (A498) | top dose only | cell-cycle shift (explains ~5% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.08×** | +3.4 | 0.045 | 1/8 (HepG2/C3A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.045 | 1/26 (MIA PaCa-2) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.3 | 0.045 | 1/6 (HepG2/C3A) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.53× | +3.1 | 0.10 | 6/20 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | 1.53× | +3.0 | 0.10 | 0/22 | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.52× | +3.0 | 0.10 | 2/13 (HepG2/C3A, LoVo) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5139.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.385×** | -6.9 | 4e-09 | 13/15 (PANC-1, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.516×** | -4.8 | 5e-04 | 14/22 (PANC-1, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.647×** | -4.4 | 0.002 | 14/18 (PANC-1, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.570×** | -4.1 | 0.007 | 10/26 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.588×** | -3.7 | 0.026 | 9/22 (Hs 766T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.628×** | -3.4 | 0.058 | 10/21 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.629×** | -3.4 | 0.058 | 11/23 (A-172, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.412×** | -3.3 | 0.058 | 3/26 (Hs 766T, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.656× | -3.0 | 0.13 | 6/24 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.446× | -3.0 | 0.13 | 5/26 (LoVo, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.448× | -3.0 | 0.13 | 1/21 (SW48) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5139. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0315× (z -12.2) |
| [[A498 (line)]] | wt | 5.62 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.221× (z -9.8) |
| [[PANC-1 (line)]] | alt | 5.02 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0437× (z -16.1) |
| [[A-172 (line)]] | wt | 2.28 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0520× (z -8.6) |
| [[A-427 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.939 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.604 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.145 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.866 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.714 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.609 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.233 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.140 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.202 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.214 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.622 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.163 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.151 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.658 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.790 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.648 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.668 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5139), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OTX1]] | +0.66 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[SEPTIN6]] | +0.59 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[ANO8]] | +0.58 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[THRA]] | +0.57 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[ANKMY2]] | +0.56 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[THYN1]] | +0.56 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[PPP1R14A]] | +0.56 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[RAB3A]] | +0.55 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[PAX2]] | +0.55 | +0.64 / +0.34 | both halves | 1e-04 |  |
| [[DMBX1]] | +0.55 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[HAUS4]] | +0.55 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[ACACB]] | +0.55 | +0.47 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEXIM2-AS1]] | -0.52 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[RAB30-DT]] | -0.52 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[CLHC1]] | -0.49 | -0.33 / -0.32 | both halves | 2e-04 |  |
| [[ENOX2]] | -0.48 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[ACYP2]] | -0.48 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[LTO1]] | -0.47 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[WSB2]] | -0.47 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[TMEM232]] | -0.47 | -0.42 / -0.24 | both halves | 5e-04 |  |
| [[RFX3-DT]] | -0.46 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[BDNF-AS]] | -0.46 | -0.33 / -0.29 | both halves | 2e-04 |  |
| [[AVEN]] | -0.46 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[ARRDC3-AS1]] | -0.46 | -0.34 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBX1]] | B | TBX1 activity raises DUSP9's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 1.35× lower at baseline in the lines without TBX1 | 0.072 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1 |
| [[BRSK2]] | B | BRSK2 activity raises DUSP9's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.34× lower at baseline in the lines without BRSK2 | 0.083 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[NOVA2]] | C | NOVA2 activity raises DUSP9's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.48× lower at baseline in the lines without NOVA2 | 0.074 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFD]] | B | DUSP9 activity raises CFD's level | lines that do not express DUSP9 (17) vs lines expressing it (33) | 1.97× lower at baseline in the lines without DUSP9 | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC47A1, SMO, LAMC3 |
| [[CYS1]] | B | DUSP9 activity raises CYS1's level | lines that do not express DUSP9 (17) vs lines expressing it (33) | 1.61× lower at baseline in the lines without DUSP9 | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC47A1, SMO, LAMC3 |
| [[OSBPL7]] | B | DUSP9 activity lowers OSBPL7's level | lines that do not express DUSP9 (17) vs lines expressing it (33) | 1.52× higher at baseline in the lines without DUSP9 | 0.078 | ⚠ within organs, on part of the lines; also absent: SLC47A1, SMO, LAMC3 |
| [[PDZD4]] | C | DUSP9 activity raises PDZD4's level | lines that do not express DUSP9 (17) vs lines expressing it (33) | 2.41× lower at baseline in the lines without DUSP9 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC47A1, SMO, LAMC3; co-absent with the target |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.542). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (7.4, -5.7); signed map (-29.7, -1.8). **Vector** length 36.6, 5.83% of its response variance represented; |z| ≥ 3 in 634 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.3 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.2 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.1 | +2.0 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +0.9 | +0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.9 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.8 | +0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.5 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.5 | -6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,642,492-153,651,326 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MKP-4, MKP4 |
| Gene groups (HGNC) | MAP kinase phosphatases |
| Reactome | 8 pathways, smallest: Signaling by MAPK mutants; RAF-independent MAPK1/3 activation; Negative regulation of MAPK pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99956](https://www.uniprot.org/uniprotkb/Q99956) (Dual specificity protein phosphatase 9):

> Inactivates MAP kinases. Has a specificity for the ERK family.

**Summary**, from NCBI Gene [1852](https://www.ncbi.nlm.nih.gov/gene/1852):

> The protein encoded by this gene is a member of the dual specificity protein phosphatase subfamily. These phosphatases inactivate their target kinases by dephosphorylating both the phosphoserine/threonine and phosphotyrosine residues. They negatively regulate members of the mitogen-activated protein (MAP) kinase superfamily (MAPK/ERK, SAPK/JNK, p38), which is associated with cellular proliferation and differentiation. Different members of the family of dual specificity phosphatases show …

**Accessions** — [HGNC:3076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3076) · Entrez [1852](https://www.ncbi.nlm.nih.gov/gene/1852) · UniProt [Q99956](https://www.uniprot.org/uniprotkb/Q99956) · Ensembl [ENSG00000130829](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130829)

## Data

Gene col 5139: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5139); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5139, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5139]; `tensor/DDL_lfc|DDL_z.npy` [5139]; `embed/gene_vectors.npy` [5139]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5139 or target_col == 5139). Every well: [[DUSP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
