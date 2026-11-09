---
symbol: "RAC2"
type: "gene"
col: 4878
ensembl_id: "ENSG00000128340"
name: "Rac family small GTPase 2"
location: "22q13.1"
module: 84
arm: "+"
pooled_cpm: 16.33
n_lines_expressing: 31
n_dd_up: 8
n_dd_down: 56
n_dd_up_clean: 6
n_dd_down_clean: 47
in_vector_space: true
direction_upstream: 45
direction_downstream: 37
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# RAC2

*Rac family small GTPase 2* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.67× (z +8.1, q 2e-13, up in 21 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 56 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.360× (z -16.2, q 0e+00, down in 23 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASA3]] (+0.78, fdr 7e-06), [[KCNN4]] (+0.74, fdr 7e-06), [[STC1]] (+0.74, fdr 7e-06); moves opposite to [[MGST1]] (-0.65, fdr 1e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 45 arrows point to it, the strongest [[MMP14]] → it (grade B ⚠); 37 go from it, the strongest it → [[SHB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4878.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +8.1 | 2e-13 | 21/29 (SW480, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +7.4 | 4e-11 | 11/18 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +5.0 | 1e-04 | 16/29 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.52×** | +4.7 | 3e-04 | 11/23 (KATO III, HT-29, …) | rises with dose | composition shift |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.002 | 10/29 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.059 | 10/29 (Hs 766T, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.064 | 8/29 (MIA PaCa-2, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.064 | 10/28 (LS 180, HCT15, …) | all doses, stronger at high dose | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | 1.22× | +3.1 | 0.12 | 10/29 (RPMI-7951, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 56 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4878.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.360×** | -16.2 | 0e+00 | 23/28 (SW 900, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.526×** | -10.2 | 9e-22 | 24/29 (NCI-H1792, SW 900, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.428×** | -9.5 | 6e-19 | 24/29 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.457×** | -8.7 | 3e-16 | 23/28 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.464×** | -8.6 | 1e-15 | 24/29 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.461×** | -8.3 | 7e-15 | 20/29 (HOP62, SW 900, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.478×** | -8.3 | 1e-14 | 25/29 (HOP62, SW 900, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.500×** | -7.4 | 7e-12 | 18/27 (HOP62, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -7.2 | 3e-11 | 21/27 (H4, SW 900, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.565×** | -7.2 | 3e-11 | 24/29 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.525×** | -7.2 | 3e-11 | 21/29 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.502×** | -7.1 | 5e-11 | 19/29 (HOP62, SW 900, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.556×** | -6.6 | 2e-09 | 25/29 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.578×** | -6.1 | 4e-08 | 22/29 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.589×** | -5.7 | 5e-07 | 17/26 (H4, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.603×** | -5.4 | 2e-06 | 19/28 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4878. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 79.5 | 0 | 14 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.148× (z -14.7) |
| [[SW 900 (line)]] | alt | 89.1 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -19.8) |
| [[NCI-H1792 (line)]] | alt | 35.9 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0694× (z -23.5) |
| [[H4 (line)]] | wt | 30.2 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0752× (z -11.7) |
| [[A-172 (line)]] | wt | 28.6 | 0 | 4 | — | [[Cobimetinib (drug)]] 5 µM 0.144× (z -12.6) |
| [[SW480 (line)]] | alt | 7.01 | 1 | 3 | [[Tucidinostat (drug)]] 5 µM 3.31× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -11.5) |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 29.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 6.55 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.110× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.225× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -10.4) |
| [[SNU-423 (line)]] | alt | 49.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 64.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -11.5) |
| [[HCT15 (line)]] | alt | 8.11 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0963× (z -10.4) |
| [[Hs 766T (line)]] | wt | 29.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 59.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -13.2) |
| [[LS 180 (line)]] | wt | 6.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 4.25 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.429× (z -9.4) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 38.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 30.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -11.7) |
| [[SW 1088 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -8.5) |
| [[A-427 (line)]] | wt | 0.997 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.87 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.975 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.26 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4878), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASA3]] | +0.78 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[KCNN4]] | +0.74 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[STC1]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[STX1A]] | +0.73 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[PAEP]] | +0.71 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[TMEM158]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[RFX8]] | +0.69 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[ADAM8]] | +0.69 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[LINC02813]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PLEK2]] | +0.69 | +0.66 / +0.58 | both halves | 7e-06 | STRING 464 |
| [[ARID3B]] | +0.69 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[SEMA7A]] | +0.68 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGST1]] | -0.65 | -0.63 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 33, C 12. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP14]] | B | MMP14 activity raises RAC2's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 4.84× lower at baseline in the lines without MMP14 | 0.001 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[PTPRE]] | B | PTPRE activity raises RAC2's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 3.37× lower at baseline in the lines without PTPRE | 0.006 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[EVA1A-AS]] | B | EVA1A-AS activity raises RAC2's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 3.37× lower at baseline in the lines without EVA1A-AS | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[PLAT]] | B | PLAT activity raises RAC2's level | lines that do not express PLAT (28) vs lines expressing it (22) | 4.08× lower at baseline in the lines without PLAT | 0.008 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[TMCC3]] | B | TMCC3 activity raises RAC2's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.91× lower at baseline in the lines without TMCC3 | 0.010 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[ITGA11]] | B | ITGA11 activity raises RAC2's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 4.52× lower at baseline in the lines without ITGA11 | 0.017 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[PLAUR]] | B | PLAUR activity raises RAC2's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 4.36× lower at baseline in the lines without PLAUR | 0.019 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[GNA15]] | B | GNA15 activity raises RAC2's level | lines that do not express GNA15 (25) vs lines expressing it (25) | 2.72× lower at baseline in the lines without GNA15 | 0.025 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent |
| [[FAM167A]] | B | FAM167A activity raises RAC2's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 2.96× lower at baseline in the lines without FAM167A | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[CREG2]] | B | CREG2 activity raises RAC2's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 2.74× lower at baseline in the lines without CREG2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[COL6A2]] | B | COL6A2 activity raises RAC2's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 3.59× lower at baseline in the lines without COL6A2 | 0.040 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[SHC3]] | B | SHC3 activity raises RAC2's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 2.83× lower at baseline in the lines without SHC3 | 0.041 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 28, C 9. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SHB]] | B | RAC2 activity raises SHB's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without RAC2 | 0.010 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[TRIOBP]] | B | RAC2 activity raises TRIOBP's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.44× lower at baseline in the lines without RAC2 | 0.018 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[PTPRE]] | B | RAC2 activity raises PTPRE's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 2.33× lower at baseline in the lines without RAC2 | 0.020 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[TMEM44]] | B | RAC2 activity raises TMEM44's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.70× lower at baseline in the lines without RAC2 | 0.021 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[PDE2A]] | B | RAC2 activity raises PDE2A's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.71× lower at baseline in the lines without RAC2 | 0.032 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[FAM110A]] | B | RAC2 activity raises FAM110A's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.58× lower at baseline in the lines without RAC2 | 0.039 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[PLCH2]] | B | RAC2 activity raises PLCH2's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without RAC2 | 0.042 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[SLC25A51]] | B | RAC2 activity raises SLC25A51's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without RAC2 | 0.043 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[ECE1]] | B | RAC2 activity raises ECE1's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.99× lower at baseline in the lines without RAC2 | 0.048 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[CFAP20DC]] | B | RAC2 activity raises CFAP20DC's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 2.30× lower at baseline in the lines without RAC2 | 0.050 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[TMCC3]] | B | RAC2 activity raises TMCC3's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 2.84× lower at baseline in the lines without RAC2 | 0.051 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[PLAUR]] | B | RAC2 activity raises PLAUR's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 2.59× lower at baseline in the lines without RAC2 | 0.055 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.833). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.5, 1.5); signed map (1.1, 48.1). **Vector** length 99.3, 30.7% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +8.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | -0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.8 | +3.4 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.7 | -9.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.6 | -7.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.9 | -7.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.8 | -8.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.7 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.4 | -8.3 |

## What is on record

|  |  |
|---|---|
| Name | Rac family small GTPase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,225,270-37,259,594 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EN-7 |
| Gene groups (HGNC) | Rho family GTPases; Receptor ligands |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 21 pathways, smallest: RHO GTPases Activate NADPH Oxidases; ROS and RNS production in phagocytes; GPVI-mediated activation cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [P15153](https://www.uniprot.org/uniprotkb/P15153) (Ras-related C3 botulinum toxin substrate 2):

> Plasma membrane-associated small GTPase which cycles between an active GTP-bound and inactive GDP-bound state. In its active state, binds to a variety of effector proteins to regulate cellular responses, such as secretory processes, phagocytose of apoptotic cells and epithelial cell polarization. Regulatory subunit of the phagocyte NADPH oxidase complex that mediates the transfer of electrons from cytosolic NADPH to O2 to produce the superoxide anion (O2(-)). Activates PLCG2.

**Summary**, from NCBI Gene [5880](https://www.ncbi.nlm.nih.gov/gene/5880):

> This gene encodes a member of the Ras superfamily of small guanosine triphosphate (GTP)-metabolizing proteins. The encoded protein localizes to the plasma membrane, where it regulates diverse processes, such as secretion, phagocytosis, and cell polarization. Activity of this protein is also involved in the generation of reactive oxygen species. Mutations in this gene are associated with neutrophil immunodeficiency syndrome. There is a pseudogene for this gene on chromosome 6. [provided by …

**Accessions** — [HGNC:9802](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9802) · Entrez [5880](https://www.ncbi.nlm.nih.gov/gene/5880) · UniProt [P15153](https://www.uniprot.org/uniprotkb/P15153) · Ensembl [ENSG00000128340](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128340)

## Data

Gene col 4878: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4878); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4878, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4878]; `tensor/DDL_lfc|DDL_z.npy` [4878]; `embed/gene_vectors.npy` [4878]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4878 or target_col == 4878). Every well: [[RAC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
