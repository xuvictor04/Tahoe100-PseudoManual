---
symbol: "CARMIL2"
type: "gene"
col: 8275
ensembl_id: "ENSG00000159753"
name: "capping protein regulator and myosin 1 linker 2"
location: "16q22.1"
module: 46
arm: "-"
pooled_cpm: 2.32
n_lines_expressing: 44
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# CARMIL2

*capping protein regulator and myosin 1 linker 2* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.82× (z +12.0, q 2e-30, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.22× (z +6.3, q 4e-08, up in 14 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.497× (z -5.6, q 1e-05, down in 12 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETNK2]] (+0.61, fdr 4e-05), [[TSNARE1]] (+0.61, fdr 2e-05), [[FBXL16]] (+0.61, fdr 1e-04); moves opposite to [[CASD1]] (-0.68, fdr 1e-05), [[DECR1]] (-0.65, fdr 4e-05), [[C5orf15]] (-0.59, fdr 6e-05).
> It sits in the **-** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CTSO]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GPRIN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8275.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.82×** | +12.0 | 2e-30 | 1/2 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.21×** | +9.3 | 6e-18 | 4/8 (SHP-77, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.86×** | +7.9 | 5e-13 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +6.3 | 4e-08 | 14/33 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.21×** | +6.3 | 4e-08 | 14/29 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.14×** | +6.0 | 2e-07 | 11/17 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.80×** | +4.7 | 2e-04 | 3/8 (A-172, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +4.6 | 2e-04 | 15/36 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.0 | 0.003 | 4/19 (NCI-H460, HOP62, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.7 | 0.011 | 2/15 (SW1417, MIA PaCa-2) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.95×** | +3.6 | 0.017 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.027 | 8/25 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +3.3 | 0.036 | 7/34 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.050 | 0/34 | top dose only | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.50×** | +3.2 | 0.050 | 5/19 (SW1417, C-33 A, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +3.1 | 0.061 | 6/31 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.77×** | +3.1 | 0.067 | 3/12 (SW480, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.081 | 1/15 (A-172) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8275.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.497×** | -5.6 | 1e-05 | 12/29 (NCI-H23, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.519×** | -5.3 | 4e-05 | 16/37 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.534×** | -5.0 | 9e-05 | 10/28 (HOP62, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.744× | -3.3 | 0.12 | 3/28 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.666× | -3.3 | 0.12 | 5/34 (C-33 A, LoVo, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -11.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 8.59 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -10.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.650 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.708 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.720 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.596 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.668 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.741 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.691 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.337 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.620 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.865 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.646 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.980 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.835 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETNK2]] | +0.61 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[TSNARE1]] | +0.61 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[FBXL16]] | +0.61 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[ST6GALNAC6]] | +0.60 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[DVL1]] | +0.59 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[RBAK-RBAKDN]] | +0.59 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[HEYL]] | +0.59 | +0.49 / +0.33 | both halves | 1e-04 |  |
| [[ANKRD27]] | +0.59 | +0.37 / +0.43 | both halves | 8e-05 |  |
| [[CCDC112]] | +0.58 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[TRIM11]] | +0.57 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[MAST1]] | +0.57 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[GPRIN1]] | +0.57 | +0.51 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASD1]] | -0.68 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[DECR1]] | -0.65 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[C5orf15]] | -0.59 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[TMX4]] | -0.58 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[RC3H2]] | -0.57 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[ERAP1]] | -0.57 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[PNISR-AS1]] | -0.57 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[CTSO]] | -0.56 | -0.46 / -0.26 | both halves | 4e-04 |  |
| [[TAX1BP3]] | -0.54 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[COG4]] | -0.54 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[HFE]] | -0.54 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[HMGN2]] | -0.54 | -0.33 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSO]] | B | CTSO activity lowers CARMIL2's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.81× higher at baseline in the lines without CTSO | 0.043 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[KIF1A]] | B | KIF1A activity raises CARMIL2's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 1.72× lower at baseline in the lines without KIF1A | 0.081 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[FSD1]] | B | FSD1 activity raises CARMIL2's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.48× lower at baseline in the lines without FSD1 | 0.098 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRIN1]] | B | CARMIL2 activity raises GPRIN1's level | lines that do not express CARMIL2 (6) vs lines expressing it (44) | 2.33× lower at baseline in the lines without CARMIL2 | 0.054 | ⚠ within organs, on part of the lines; also absent: CHN1, HCN2, QKI; maybe low, not absent |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **-** arm (projection on the module's main direction -0.433). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (3.5, 3.1); signed map (-40.1, -4.9). **Vector** length 34.1, 4.32% of its response variance represented; |z| ≥ 3 in 665 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +2.2 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +12.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.8 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.7 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.9 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -5.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | capping protein regulator and myosin 1 linker 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,644,988-67,657,569 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LRRC16C; previously RLTPR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6F5E8](https://www.uniprot.org/uniprotkb/Q6F5E8) (Capping protein, Arp2/3 and myosin-I linker protein 2):

> Cell membrane-cytoskeleton-associated protein that plays a role in the regulation of actin polymerization at the barbed end of actin filaments. Prevents F-actin heterodimeric capping protein (CP) activity at the leading edges of migrating cells, and hence generates uncapped barbed ends and enhances actin polymerization. Plays a role in cell protrusion formations; involved in cell polarity, lamellipodial assembly, membrane ruffling and macropinosome formations. Involved as well in cell migration …

**Summary**, from NCBI Gene [146206](https://www.ncbi.nlm.nih.gov/gene/146206):

> This gene encodes a member of the CARMIL (capping protein, Arp2/3, myosin-I linker) family of proteins. The encoded protein interacts with and negatively regulates the heterodimeric capping protein and promotes cell migration. Reduced expression of this gene has been observed in human psoriasis patients. Mutations in this gene cause a human immunodeficiency syndrome characterized by smooth muscle tumors and impaired T-cell function. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:27089](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27089) · Entrez [146206](https://www.ncbi.nlm.nih.gov/gene/146206) · UniProt [Q6F5E8](https://www.uniprot.org/uniprotkb/Q6F5E8) · Ensembl [ENSG00000159753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159753)

## Data

Gene col 8275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8275); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8275]; `tensor/DDL_lfc|DDL_z.npy` [8275]; `embed/gene_vectors.npy` [8275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8275 or target_col == 8275). Every well: [[CARMIL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARMIL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
