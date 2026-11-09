---
symbol: "SDR16C5"
type: "gene"
col: 10004
ensembl_id: "ENSG00000170786"
name: "short chain dehydrogenase/reductase family 16C member 5"
location: "8q12.1"
module: 31
arm: "+"
pooled_cpm: 5.99
n_lines_expressing: 22
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 81
direction_downstream: 85
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# SDR16C5

*short chain dehydrogenase/reductase family 16C member 5* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.23× (z +10.9, q 1e-24, up in 1 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.09× (z +10.1, q 2e-21, up in 18 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.571× (z -5.4, q 4e-05, down in 13 of 20 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Trametinib (drug)]] 5 µM: 0.614× (z -5.2, q 5e-05, down in 9 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMPRSS4]] (+0.72, fdr 7e-06), [[PTK6]] (+0.69, fdr 7e-06), [[CEACAM1]] (+0.68, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 81 arrows point to it, the strongest [[KRT86]] → it (grade B ⚠); 85 go from it, the strongest it → [[CD55]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10004.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.23×** | +10.9 | 1e-24 | 1/8 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.09×** | +10.1 | 2e-21 | 18/20 (LS 180, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.30×** | +8.0 | 2e-13 | 1/15 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.13×** | +7.3 | 5e-11 | 13/19 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +7.2 | 6e-11 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +4.9 | 8e-05 | 4/18 (SW 900, HCT15, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.02×** | +4.8 | 1e-04 | 0/14 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.7 | 1e-04 | 2/18 (LS 180, BT-474) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.3 | 9e-04 | 2/19 (NCI-H460, KATO III) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.50×** | +3.9 | 0.005 | 7/20 (KATO III, CFPAC-1, …) | two highest doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.54×** | +3.9 | 0.006 | 7/18 (HT-29, A549, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Estrone sulfate (potassium) (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.022 | 1/20 (LoVo) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.65×** | +3.4 | 0.025 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.030 | 3/20 (LoVo, KATO III, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.2 | 0.047 | 2/20 (SW48, A549) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.048 | 4/18 (SW 900, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +3.2 | 0.049 | 1/16 (SW 900) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Naproxen (drug)]] 0.05 µM |  | **1.42×** | +3.1 | 0.058 | 2/18 (LoVo, SW480) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.5 µM |  | **1.54×** | +3.0 | 0.086 | 1/20 (LoVo) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.53×** | +2.9 | 0.093 | 3/18 (LoVo, KATO III, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.097 | 2/20 (Panc 03.27, NCI-H1573) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.097 | 2/18 (CFPAC-1, NCI-H1792) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10004.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.571×** | -5.4 | 4e-05 | 13/20 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.614×** | -5.2 | 5e-05 | 9/20 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.633×** | -4.4 | 0.002 | 11/20 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -4.0 | 0.010 | 17/20 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.681×** | -3.7 | 0.026 | 13/20 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.672×** | -3.5 | 0.039 | 5/20 (KATO III, BT-474, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.698×** | -3.5 | 0.045 | 13/20 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.712× | -3.1 | 0.15 | 15/20 (HT-29, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10004. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 29.4 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.123× (z -12.7) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.210× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0891× (z -12.3) |
| [[HT-29 (line)]] | alt | 21.5 | 0 | 5 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0942× (z -13.1) |
| [[LoVo (line)]] | wt | 14.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.171× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 32.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0671× (z -8.7) |
| [[A549 (line)]] | wt | 4.53 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.05 µM 0.0454× (z -10.1) |
| [[KATO III (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 2.09 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0731× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.486 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10004), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMPRSS4]] | +0.72 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[PTK6]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[CEACAM1]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LIPH]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[HS3ST1]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[SH2D3A]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[KIAA0040]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[ARHGEF34P]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[TMC6]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[TMEM45B]] | +0.63 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[KLF5]] | +0.61 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[PTK2B]] | +0.60 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*81 arrows, 81 of them with an alert ⚠; grade A 0, B 11, C 70. Shown: the 12 strongest; 69 more arrows (69 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT86]] | B | KRT86 activity raises SDR16C5's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 2.73× lower at baseline in the lines without KRT86 | 0.007 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[LRATD2]] | B | LRATD2 activity raises SDR16C5's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 2.68× lower at baseline in the lines without LRATD2 | 0.008 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[GPRC5A]] | B | GPRC5A activity raises SDR16C5's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.08× lower at baseline in the lines without GPRC5A | 0.016 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[PSORS1C1]] | B | PSORS1C1 activity raises SDR16C5's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 2.53× lower at baseline in the lines without PSORS1C1 | 0.028 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[TJP2]] | B | TJP2 activity raises SDR16C5's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.12× lower at baseline in the lines without TJP2 | 0.030 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[CD55]] | B | CD55 activity raises SDR16C5's level | lines that do not express CD55 (16) vs lines expressing it (34) | 2.86× lower at baseline in the lines without CD55 | 0.036 | ⚠ within organs, on part of the lines; also absent: IL32, IL2RG, ENSG00000271933; maybe low, not absent |
| [[DUSP4]] | B | DUSP4 activity raises SDR16C5's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.63× lower at baseline in the lines without DUSP4 | 0.055 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[PCDH1]] | B | PCDH1 activity raises SDR16C5's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.19× lower at baseline in the lines without PCDH1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[LMO7]] | B | LMO7 activity raises SDR16C5's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.36× lower at baseline in the lines without LMO7 | 0.075 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[CCDC120]] | B | CCDC120 activity raises SDR16C5's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 2.66× lower at baseline in the lines without CCDC120 | 0.083 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[PTK2B]] | B | PTK2B activity raises SDR16C5's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 2.51× lower at baseline in the lines without PTK2B | 0.094 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[C1orf116]] | C | C1orf116 activity raises SDR16C5's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 5.64× lower at baseline in the lines without C1orf116 | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |

### Downstream of this gene

*85 arrows, 85 of them with an alert ⚠; grade A 0, B 27, C 58. Shown: the 12 strongest; 73 more arrows (73 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD55]] | B | SDR16C5 activity raises CD55's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 3.95× lower at baseline in the lines without SDR16C5 | 0.001 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[PTK2B]] | B | SDR16C5 activity raises PTK2B's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 3.03× lower at baseline in the lines without SDR16C5 | 0.003 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[GPRC5A]] | B | SDR16C5 activity raises GPRC5A's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 4.34× lower at baseline in the lines without SDR16C5 | 0.007 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[TCF7L2]] | B | SDR16C5 activity raises TCF7L2's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 2.10× lower at baseline in the lines without SDR16C5 | 0.009 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[ABHD17C]] | B | SDR16C5 activity raises ABHD17C's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 3.14× lower at baseline in the lines without SDR16C5 | 0.009 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[LMO7]] | B | SDR16C5 activity raises LMO7's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 4.18× lower at baseline in the lines without SDR16C5 | 0.013 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[PSORS1C1]] | B | SDR16C5 activity raises PSORS1C1's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without SDR16C5 | 0.015 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[PKP3]] | B | SDR16C5 activity raises PKP3's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 3.13× lower at baseline in the lines without SDR16C5 | 0.015 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[TJP2]] | B | SDR16C5 activity raises TJP2's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 2.43× lower at baseline in the lines without SDR16C5 | 0.020 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[EPS8L1]] | B | SDR16C5 activity raises EPS8L1's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 3.00× lower at baseline in the lines without SDR16C5 | 0.023 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[DUSP4]] | B | SDR16C5 activity raises DUSP4's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 3.36× lower at baseline in the lines without SDR16C5 | 0.032 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[SQOR]] | B | SDR16C5 activity strengthens SQOR's drug response | lines that do not express SDR16C5 (22) vs lines expressing it (20) | the lines without SDR16C5 respond 0.54× as strongly (z diff +1.75); strongest at Idarubicin (hydrochloride) 5 µM: 0.95x vs 0.58x (z diff +4.4) | 0.033 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.737). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, 55.1); signed map (1.3, 37.6). **Vector** length 68.8, 20.8% of its response variance represented; |z| ≥ 3 in 584 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +7.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -3.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.3 | -5.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.1 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.9 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | short chain dehydrogenase/reductase family 16C member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:56,300,005-56,320,776 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RDHE2, RDH-E2, EPHD-2 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 3 pathways, smallest: RA biosynthesis pathway; Signaling by Retinoic Acid; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3Y7](https://www.uniprot.org/uniprotkb/Q8N3Y7) (Epidermal retinol dehydrogenase 2):

> Oxidoreductase with strong preference for NAD. Active in both the oxidative and reductive directions. Oxidizes all-trans-retinol in all-trans-retinaldehyde. No activity was detected with 11-cis-retinol or 11-cis-retinaldehyde as substrates with either NAD(+)/NADH or NADP(+)/NADPH.

**Summary**, from NCBI Gene [195814](https://www.ncbi.nlm.nih.gov/gene/195814):

> This gene encodes a member of the short-chain alcohol dehydrogenase/reductase superfamily of proteins and is involved in the oxidation of retinol to retinaldehyde. The encoded protein is associated with the endoplasmic reticulum and is predicted to contain three transmembrane helices, suggesting that it is an integral membrane protein. It recognizes all-trans-retinol and all-trans-retinaldehyde as substrates and exhibits a strong preference for NAD(+)/NADH as cofactors. Alternative splicing …

**Accessions** — [HGNC:30311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30311) · Entrez [195814](https://www.ncbi.nlm.nih.gov/gene/195814) · UniProt [Q8N3Y7](https://www.uniprot.org/uniprotkb/Q8N3Y7) · Ensembl [ENSG00000170786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170786)

## Data

Gene col 10004: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10004); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10004, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10004]; `tensor/DDL_lfc|DDL_z.npy` [10004]; `embed/gene_vectors.npy` [10004]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10004 or target_col == 10004). Every well: [[SDR16C5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDR16C5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
