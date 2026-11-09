---
symbol: "GALNT16"
type: "gene"
col: 2004
ensembl_id: "ENSG00000100626"
name: "polypeptide N-acetylgalactosaminyltransferase 16"
location: "14q24.1"
module: 19
arm: "+"
pooled_cpm: 3.1
n_lines_expressing: 42
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GALNT16

*polypeptide N-acetylgalactosaminyltransferase 16* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.04× (z +14.5, q 7e-45, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.52× (z +14.1, q 7e-43, up in 13 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.627× (z -5.1, q 2e-04, down in 14 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.199×, HEC-1-A 0.146×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (HEC-1-A 0.0777×; ⚠ cell-cycle shift, explains ~35% of this change); [[Rifaximin (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0603×); [[Penfluridol (drug)]] 5 µM in 1 line (A-172 0.0840×); [[Bimatoprost (drug)]] 0.5 µM in 1 line (SW480 0.0901×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RADIL]] (+0.62, fdr 3e-05), [[EBF2]] (+0.56, fdr 6e-05), [[SLITRK4]] (+0.56, fdr 1e-05); moves opposite to [[KRIT1]] (-0.51, fdr 1e-04), [[UEVLD]] (-0.50, fdr 6e-05), [[UPF3A]] (-0.50, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[COL4A4]] → it (grade B ⚠); 4 go from it, the strongest it → [[FAM234B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2004.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.04×** | +14.5 | 7e-45 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +14.1 | 7e-43 | 13/19 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.40×** | +13.3 | 2e-38 | 23/36 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.29×** | +12.9 | 1e-35 | 24/37 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.18×** | +12.5 | 9e-34 | 4/8 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.98×** | +11.1 | 7e-27 | 21/34 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.78×** | +11.1 | 2e-26 | 25/38 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.64×** | +10.5 | 7e-24 | 20/34 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.33×** | +9.1 | 5e-18 | 15/24 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +7.6 | 1e-12 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +7.0 | 1e-10 | 8/35 (NCI-H2030, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.90×** | +6.7 | 1e-09 | 4/10 (SW480, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.59×** | +5.4 | 3e-06 | 7/25 (SW480, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +5.2 | 7e-06 | 4/25 (SW480, SW 900, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +5.0 | 3e-05 | 10/20 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.065 | 3/18 (BT-474, SW480, …) | inconsistent across doses |  |
| [[Valdecoxib (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.069 | 1/25 (RPMI-7951) | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.44×** | +2.9 | 0.099 | 0/18 | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2004.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.199×, HEC-1-A 0.146×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (HEC-1-A 0.0777×; ⚠ cell-cycle shift, explains ~35% of this change); [[Rifaximin (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0603×); [[Penfluridol (drug)]] 5 µM in 1 line (A-172 0.0840×); [[Bimatoprost (drug)]] 0.5 µM in 1 line (SW480 0.0901×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.627×** | -5.1 | 2e-04 | 14/36 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.636×** | -4.7 | 7e-04 | 11/30 (HEC-1-A, NCI-H460, …) | rises with dose | composition shift |
| [[Erythromycin (drug)]] 0.05 µM |  | **0.720×** | -3.6 | 0.070 | 9/33 (HCT15, Panc 03.27, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.545×** | -3.4 | 0.085 | 2/17 (LoVo, C-33 A) | top dose only | noisy plate (z scaled) |
| [[Fostamatinib (disodium hexahydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.739× | -3.3 | 0.11 | 6/36 (NCI-H23, RKO, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.729× | -3.2 | 0.11 | 5/20 (HS-578T, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Tadalafil (drug)]] 0.5 µM |  | 0.748× | -3.1 | 0.13 | 3/38 (AN3 CA, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2004. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 4.66 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 4.60 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0840× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 5.99 | 0 | 1 | — | [[Rifaximin (drug)]] 0.5 µM 0.0603× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -16.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 2.33 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0901× (z -8.8) |
| [[A-427 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.944 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.900 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.728 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.820 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.855 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.865 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2004), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RADIL]] | +0.62 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[EBF2]] | +0.56 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[SLITRK4]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TMEM108]] | +0.55 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[NXPH4]] | +0.55 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[COL4A4]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[CNTN1]] | +0.53 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[ADGRB2]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[UNC5D]] | +0.52 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[SCUBE1]] | +0.51 | +0.29 / +0.49 | both halves | 2e-04 |  |
| [[ASXL3]] | +0.50 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[KIF26A]] | +0.50 | +0.39 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRIT1]] | -0.51 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[UEVLD]] | -0.50 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[UPF3A]] | -0.50 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[ARMCX4]] | -0.49 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[HCG11]] | -0.49 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[CHMP4A]] | -0.49 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[SLF2]] | -0.48 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[GPALPP1]] | -0.48 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[EFCAB2]] | -0.48 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[TMEM192]] | -0.48 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[TRMT13]] | -0.48 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[C15orf40]] | -0.48 | -0.34 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL4A4]] | B | COL4A4 activity raises GALNT16's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 1.82× lower at baseline in the lines without COL4A4 | 0.013 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A |
| [[ARMCX4]] | B | ARMCX4 activity lowers GALNT16's level | lines that do not express ARMCX4 (18) vs lines expressing it (32) | 1.54× higher at baseline in the lines without ARMCX4 | 0.019 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC |
| [[COL4A3]] | B | COL4A3 activity raises GALNT16's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 1.84× lower at baseline in the lines without COL4A3 | 0.022 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4 |
| [[FAM124A]] | B | FAM124A activity raises GALNT16's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 1.80× lower at baseline in the lines without FAM124A | 0.068 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM234B]] | B | GALNT16 activity raises FAM234B's level | lines that do not express GALNT16 (8) vs lines expressing it (42) | 2.44× lower at baseline in the lines without GALNT16 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000237356, PRKAR2B, FRG1-DT; maybe low, not absent |
| [[RPAP2]] | B | GALNT16 activity raises RPAP2's level | lines that do not express GALNT16 (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without GALNT16 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000237356, PRKAR2B, FRG1-DT; maybe low, not absent |
| [[RASSF2]] | B | GALNT16 activity raises RASSF2's level | lines that do not express GALNT16 (8) vs lines expressing it (42) | 2.73× lower at baseline in the lines without GALNT16 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000237356, PRKAR2B, FRG1-DT; maybe low, not absent |
| [[TRMT61B]] | B | GALNT16 activity raises TRMT61B's level | lines that do not express GALNT16 (8) vs lines expressing it (42) | 1.34× lower at baseline in the lines without GALNT16 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000237356, PRKAR2B, FRG1-DT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.451). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.4, 39.9); signed map (40.3, 47.8). **Vector** length 39.7, 5.17% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +13.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | +0.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.1 | -4.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -0.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:69,259,277-69,357,033 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1130, GalNAc-T16; previously GALNTL1 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N428](https://www.uniprot.org/uniprotkb/Q8N428) (Polypeptide N-acetylgalactosaminyltransferase 16):

> Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor.

**Summary**, from NCBI Gene [57452](https://www.ncbi.nlm.nih.gov/gene/57452):

> Enables polypeptide N-acetylgalactosaminyltransferase activity. Involved in protein O-linked glycosylation via N-acetyl-galactosamine. Predicted to be located in Golgi membrane. Predicted to be active in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23233) · Entrez [57452](https://www.ncbi.nlm.nih.gov/gene/57452) · UniProt [Q8N428](https://www.uniprot.org/uniprotkb/Q8N428) · Ensembl [ENSG00000100626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100626)

## Data

Gene col 2004: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2004); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2004, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2004]; `tensor/DDL_lfc|DDL_z.npy` [2004]; `embed/gene_vectors.npy` [2004]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2004 or target_col == 2004). Every well: [[GALNT16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
