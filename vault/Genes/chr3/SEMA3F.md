---
symbol: "SEMA3F"
type: "gene"
col: 12
ensembl_id: "ENSG00000001617"
name: "semaphorin 3F"
location: "3p21.31"
module: 161
arm: "+"
pooled_cpm: 5.06
n_lines_expressing: 44
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# SEMA3F

*semaphorin 3F* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.97× (z +12.9, q 5e-35, up in 31 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.621× (z -5.6, q 1e-05, down in 16 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.201×; ⚠ cell-cycle shift, explains ~39% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (PANC-1 0.122×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pioglitazone (drug)]] 0.5 µM in 1 line (BT-474 0.0732×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (BT-474 0.0996×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCHO1]] (+0.67, fdr 1e-05), [[BAIAP3]] (+0.65, fdr 1e-05), [[FGFR3]] (+0.64, fdr 5e-05); moves opposite to [[TBCK]] (-0.59, fdr 2e-05), [[QRSL1]] (-0.57, fdr 3e-05), [[PUS10]] (-0.54, fdr 5e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FCHO1]] → it (grade B ⚠); 7 go from it, the strongest it → [[CADM4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.97×** | +12.9 | 5e-35 | 31/39 (Panc 03.27, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.69×** | +11.7 | 4e-29 | 31/39 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.50×** | +10.8 | 7e-25 | 31/39 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +7.8 | 1e-12 | 17/39 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +7.7 | 1e-12 | 11/30 (HepG2/C3A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +7.6 | 3e-12 | 13/34 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.85×** | +7.3 | 3e-11 | 22/39 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +5.7 | 6e-07 | 2/9 (PANC-1, SW1417) | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +5.0 | 4e-05 | 10/36 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.20×** | +4.9 | 6e-05 | 2/6 (SW1417, A498) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +4.8 | 8e-05 | 1/10 (SW1417) | inconsistent across doses | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +4.6 | 2e-04 | 8/28 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.43×** | +3.9 | 0.004 | 3/25 (SW480, J82, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.040 | 10/36 (A-172, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.047 | 0/33 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.069 | 0/27 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.069 | 4/27 (A-172, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.28×** | +2.9 | 0.095 | 3/30 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.201×; ⚠ cell-cycle shift, explains ~39% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (PANC-1 0.122×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pioglitazone (drug)]] 0.5 µM in 1 line (BT-474 0.0732×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (BT-474 0.0996×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -5.6 | 1e-05 | 16/38 (A-427, LoVo, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -4.9 | 3e-04 | 10/41 (KATO III, HOP62, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -3.5 | 0.077 | 10/36 (A498, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 7.60 | 0 | 2 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0732× (z -9.6) |
| [[Hs 766T (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -11.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[PANC-1 (line)]] | alt | 5.28 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.122× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHO1]] | +0.67 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.65 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[FGFR3]] | +0.64 | +0.39 / +0.68 | both halves | 5e-05 |  |
| [[GPR153]] | +0.64 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[MYRF]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ITGA7]] | +0.63 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[SOX13]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CADM4]] | +0.62 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[AHDC1]] | +0.62 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[ANKDD1A]] | +0.62 | +0.40 / +0.59 | both halves | 4e-05 |  |
| [[INPP5A]] | +0.61 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[HEYL]] | +0.60 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCK]] | -0.59 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[QRSL1]] | -0.57 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PUS10]] | -0.54 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[ZFR]] | -0.54 | -0.41 / -0.43 | both halves | 4e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FCHO1]] | B | FCHO1 activity raises SEMA3F's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without FCHO1 | 0.028 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[LAMA5]] | B | LAMA5 activity raises SEMA3F's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 2.21× lower at baseline in the lines without LAMA5 | 0.036 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[BCAM]] | B | BCAM activity raises SEMA3F's level | lines that do not express BCAM (8) vs lines expressing it (42) | 2.25× lower at baseline in the lines without BCAM | 0.054 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[JAG2]] | B | JAG2 activity raises SEMA3F's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.79× lower at baseline in the lines without JAG2 | 0.075 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[ANKRD20A1]] | B | ANKRD20A1 activity raises SEMA3F's level | lines that do not express ANKRD20A1 (20) vs lines expressing it (30) | 1.37× lower at baseline in the lines without ANKRD20A1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ANKRD20A4P, CTNNA2, SCN8A |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CADM4]] | B | SEMA3F activity raises CADM4's level | lines that do not express SEMA3F (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without SEMA3F | 0.050 | ⚠ within organs, on part of the lines; also absent: MCM2, PIMREG, GKAP1 |
| [[PRSS3]] | B | SEMA3F activity lowers PRSS3's level | lines that do not express SEMA3F (6) vs lines expressing it (44) | 2.50× higher at baseline in the lines without SEMA3F | 0.056 | ⚠ within organs, on part of the lines; also absent: MCM2, PIMREG, GKAP1 |
| [[ASMTL]] | B | SEMA3F activity raises ASMTL's level | lines that do not express SEMA3F (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without SEMA3F | 0.062 | ⚠ within organs, on part of the lines; also absent: MCM2, PIMREG, GKAP1 |
| [[QRSL1]] | B | SEMA3F activity raises QRSL1's level | lines that do not express SEMA3F (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without SEMA3F | 0.074 | ⚠ within organs, on part of the lines; also absent: MCM2, PIMREG, GKAP1 |
| [[ITGA7]] | B | SEMA3F activity raises ITGA7's level | lines that do not express SEMA3F (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without SEMA3F | 0.093 | ⚠ within organs, on part of the lines; also absent: MCM2, PIMREG, GKAP1 |
| [[SMARCAL1]] | B | SEMA3F activity raises SMARCAL1's level | lines that do not express SEMA3F (6) vs lines expressing it (44) | 1.12× lower at baseline in the lines without SEMA3F | 0.094 | ⚠ within organs, on part of the lines; also absent: MCM2, PIMREG, GKAP1 |
| [[PTK7]] | B | SEMA3F activity raises PTK7's level | lines that do not express SEMA3F (6) vs lines expressing it (44) | 2.43× lower at baseline in the lines without SEMA3F | 0.0999 | ⚠ within organs, on part of the lines; also absent: MCM2, PIMREG, GKAP1 |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.784). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.0, 32.2); signed map (-15.0, 34.5). **Vector** length 53.4, 7.85% of its response variance represented; |z| ≥ 3 in 859 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +7.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +12.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +3.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -2.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -1.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 3F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,155,045-50,189,075 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SEMAK, Sema4 |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Semaphorins; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13275](https://www.uniprot.org/uniprotkb/Q13275) (Semaphorin-3F):

> May play a role in cell motility and cell adhesion.

**Summary**, from NCBI Gene [6405](https://www.ncbi.nlm.nih.gov/gene/6405):

> This gene encodes a member of the semaphorin III family of secreted signaling proteins that are involved in axon guidance during neuronal development. The encoded protein contains an N-terminal Sema domain, an immunoglobulin loop and a C-terminal basic domain. This gene is expressed by the endothelial cells where it was found to act in an autocrine fashion to induce apoptosis, inhibit cell proliferation and survival, and function as an anti-tumorigenic agent. Alternative splicing results in …

**Accessions** — [HGNC:10728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10728) · Entrez [6405](https://www.ncbi.nlm.nih.gov/gene/6405) · UniProt [Q13275](https://www.uniprot.org/uniprotkb/Q13275) · Ensembl [ENSG00000001617](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000001617)

## Data

Gene col 12: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12]; `tensor/DDL_lfc|DDL_z.npy` [12]; `embed/gene_vectors.npy` [12]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12 or target_col == 12). Every well: [[SEMA3F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA3F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
