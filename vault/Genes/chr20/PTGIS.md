---
symbol: "PTGIS"
type: "gene"
col: 4500
ensembl_id: "ENSG00000124212"
name: "prostaglandin I2 synthase"
location: "20q13.13"
module: 9
arm: "+"
pooled_cpm: 6.3
n_lines_expressing: 11
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PTGIS

*prostaglandin I2 synthase* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.16× (z +10.2, q 8e-22, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.69× (z +10.1, q 3e-21, up in 0 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.589× (z -3.8, q 0.061, down in 8 of 9 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (Hs 766T 0.0628×, HS-578T 0.0719×, AsPC-1 0.0494×, NCI-H23 0.188×); [[Panobinostat (drug)]] 0.5 µM in 3 lines (Hs 766T 0.0434×, HS-578T 0.0536×, NCI-H23 0.0383×; ⚠ cell-cycle shift, explains ~88% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (Hs 766T 0.0449×, HS-578T 0.0782×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (Hs 766T 0.0531×, HS-578T 0.128×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.148×, HS-578T 0.257×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOK5]] (+0.72, fdr 7e-06), [[SIM1]] (+0.65, fdr 2e-05), [[EDIL3-DT]] (+0.54, fdr 4e-05); moves opposite to [[SLC26A2]] (-0.49, fdr 1e-04), [[HMGA2]] (-0.48, fdr 7e-05), [[TOP1]] (-0.44, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[UGT1A6]] → it (grade C ⚠); 7 go from it, the strongest it → [[HOXA-AS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4500.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.16×** | +10.2 | 8e-22 | 3/5 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.69×** | +10.1 | 3e-21 | 0/8 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.97×** | +9.5 | 3e-19 | 3/5 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +6.5 | 1e-08 | 1/5 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +5.9 | 5e-07 | 0/9 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +4.4 | 0.001 | 3/9 (A498, Panc 03.27, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.28×** | +4.2 | 0.002 | 1/7 (A498) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.68×** | +4.2 | 0.002 | 4/8 (AsPC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +4.1 | 0.002 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +4.1 | 0.002 | 0/9 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.18×** | +4.0 | 0.003 | 3/8 (AsPC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.8 | 0.006 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.73×** | +3.7 | 0.009 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +3.6 | 0.013 | 3/8 (A498, C-33 A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.60×** | +3.4 | 0.028 | 0/8 | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.64×** | +3.4 | 0.028 | 4/8 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.043 | 0/8 | rises with dose | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.53×** | +3.1 | 0.064 | 1/8 (A498) | inconsistent across doses |  |
| [[Alpelisib (drug)]] 5 µM |  | **2.24×** | +3.0 | 0.083 | 3/8 (AsPC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +2.9 | 0.100 | 2/9 (AsPC-1, NCI-H23) | top dose only | low cells (technical?); cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4500.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (Hs 766T 0.0628×, HS-578T 0.0719×, AsPC-1 0.0494×, NCI-H23 0.188×); [[Panobinostat (drug)]] 0.5 µM in 3 lines (Hs 766T 0.0434×, HS-578T 0.0536×, NCI-H23 0.0383×; ⚠ cell-cycle shift, explains ~88% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (Hs 766T 0.0449×, HS-578T 0.0782×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (Hs 766T 0.0531×, HS-578T 0.128×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.148×, HS-578T 0.257×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.589×** | -3.8 | 0.061 | 8/9 (HS-578T, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.586×** | -3.7 | 0.061 | 6/9 (Hs 766T, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.635× | -3.3 | 0.21 | 5/9 (HS-578T, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.627× | -3.1 | 0.23 | 0/9 | inconsistent across doses | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.629× | -3.1 | 0.23 | 1/9 (NCI-H661) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4500. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 45.4 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -19.2) |
| [[Hs 766T (line)]] | wt | 70.3 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0628× (z -20.2) |
| [[NCI-H1792 (line)]] | alt | 113 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 7.26 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0383× (z -12.4) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.188× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0494× (z -14.9) |
| [[C-33 A (line)]] | alt | 9.65 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0537× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.602 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.468 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.633 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.997 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.593 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.585 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4500), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOK5]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[SIM1]] | +0.65 | +0.48 / +0.66 | both halves | 2e-05 | **novel candidate** |
| [[EDIL3-DT]] | +0.54 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[PTPRR]] | +0.54 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[CDH6]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[GPRC5B]] | +0.52 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[CNTNAP3C]] | +0.52 | +0.37 / +0.51 | both halves | 7e-05 | **novel candidate** |
| [[DUOX2]] | +0.51 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[CYP26B1]] | +0.50 | +0.42 / +0.46 | both halves | 4e-05 | pathway: Biological oxidations |
| [[CCDC3]] | +0.50 | +0.36 / +0.44 | both halves | 1e-04 |  |
| [[BBOX1-AS1]] | +0.50 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[SULF1]] | +0.49 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC26A2]] | -0.49 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[HMGA2]] | -0.48 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[TOP1]] | -0.44 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[LDLRAD3]] | -0.42 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[C16orf74]] | -0.42 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ERRFI1]] | -0.41 | -0.29 / -0.36 | both halves | 3e-04 |  |
| [[ELK3]] | -0.41 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[TBC1D16]] | -0.41 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SPRY4-AS1]] | -0.40 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[FAM110C]] | -0.39 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[ST3GAL1]] | -0.39 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[BCL2L1]] | -0.39 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UGT1A6]] | C | UGT1A6 activity raises PTGIS's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 2.52× lower at baseline in the lines without UGT1A6 | 0.009 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; co-absent with the target |
| [[BBOX1-AS1]] | C | BBOX1-AS1 activity raises PTGIS's level | lines that do not express BBOX1-AS1 (21) vs lines expressing it (29) | 1.91× lower at baseline in the lines without BBOX1-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: GLDN, CHN2, CPVL; maybe low, not absent; co-absent with the target |
| [[UGT1A8]], [[UGT1A9]] | C | UGT1A8, UGT1A9 activity raises PTGIS's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 2.24× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.068 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[HTR1F]] | C | HTR1F activity raises PTGIS's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 2.01× lower at baseline in the lines without HTR1F | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA-AS2]] | B | PTGIS activity raises HOXA-AS2's level | lines that do not express PTGIS (39) vs lines expressing it (11) | 1.71× lower at baseline in the lines without PTGIS | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, PREX2, GCG |
| [[MECOM]] | B | PTGIS activity raises MECOM's level | lines that do not express PTGIS (39) vs lines expressing it (11) | 1.97× lower at baseline in the lines without PTGIS | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, PREX2, GCG |
| [[UGT1A6]] | C | PTGIS activity raises UGT1A6's level | lines that do not express PTGIS (39) vs lines expressing it (11) | 2.01× lower at baseline in the lines without PTGIS | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, PREX2, GCG; co-absent with the target |
| [[UGT1A9]] | C | PTGIS activity raises UGT1A9's level | lines that do not express PTGIS (39) vs lines expressing it (11) | 1.64× lower at baseline in the lines without PTGIS | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, PREX2, GCG; co-absent with the target |
| [[UGT1A8]] | C | PTGIS activity raises UGT1A8's level | lines that do not express PTGIS (39) vs lines expressing it (11) | 1.93× lower at baseline in the lines without PTGIS | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, PREX2, GCG; co-absent with the target |
| [[BBOX1-AS1]] | C | PTGIS activity raises BBOX1-AS1's level | lines that do not express PTGIS (39) vs lines expressing it (11) | 2.35× lower at baseline in the lines without PTGIS | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, PREX2, GCG; co-absent with the target |
| [[PTPRR]] | C | PTGIS activity raises PTPRR's level | lines that do not express PTGIS (39) vs lines expressing it (11) | 1.91× lower at baseline in the lines without PTGIS | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, PREX2, GCG; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.231). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.6, 20.3); signed map (35.4, 30.4). **Vector** length 43.1, 15.3% of its response variance represented; |z| ≥ 3 in 342 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.9 | +5.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.7 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.2 | +2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.2 | +2.4 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.1 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.1 | -0.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | prostaglandin I2 synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:49,503,874-49,568,137 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PGIS, CYP8A1 |
| Gene groups (HGNC) | Cytochrome P450 family 8; Hydroperoxy icosatetraenoate dehydratases |
| Hallmark sets | MYOGENESIS |
| Reactome | 8 pathways, smallest: Eicosanoids; Synthesis of Prostaglandins (PG) and Thromboxanes (TX); Cytochrome P450 - arranged by substrate type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16647](https://www.uniprot.org/uniprotkb/Q16647) (Prostacyclin synthase):

> Catalyzes the biosynthesis and metabolism of eicosanoids. Catalyzes the isomerization of prostaglandin H2 to prostacyclin (= prostaglandin I2), a potent mediator of vasodilation and inhibitor of platelet aggregation. Additionally, displays dehydratase activity, toward hydroperoxyeicosatetraenoates (HPETEs), especially toward (15S)-hydroperoxy-(5Z,8Z,11Z,13E)-eicosatetraenoate (15(S)-HPETE).

**Summary**, from NCBI Gene [5740](https://www.ncbi.nlm.nih.gov/gene/5740):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. However, this protein is considered a member of the cytochrome P450 superfamily on the basis of sequence similarity rather than functional similarity. This endoplasmic reticulum membrane protein catalyzes the conversion of prostglandin H2 to prostacyclin …

**Accessions** — [HGNC:9603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9603) · Entrez [5740](https://www.ncbi.nlm.nih.gov/gene/5740) · UniProt [Q16647](https://www.uniprot.org/uniprotkb/Q16647) · Ensembl [ENSG00000124212](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124212)

## Data

Gene col 4500: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4500); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4500, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4500]; `tensor/DDL_lfc|DDL_z.npy` [4500]; `embed/gene_vectors.npy` [4500]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4500 or target_col == 4500). Every well: [[PTGIS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTGIS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
