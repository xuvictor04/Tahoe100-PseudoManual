---
symbol: "TTC9"
type: "gene"
col: 5493
ensembl_id: "ENSG00000133985"
name: "tetratricopeptide repeat domain 9"
location: "14q24.2"
module: 31
arm: "+"
pooled_cpm: 15.06
n_lines_expressing: 27
n_dd_up: 24
n_dd_down: 16
n_dd_up_clean: 17
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 53
direction_downstream: 69
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# TTC9

*tetratricopeptide repeat domain 9* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.00× (z +9.4, q 2e-18, up in 1 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +7.9, q 1e-12, up in 7 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.506× (z -13.7, q 8e-40, down in 21 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HS3ST1]] (+0.71, fdr 7e-06), [[CRYBG2]] (+0.70, fdr 7e-06), [[MYO5B]] (+0.68, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 53 arrows point to it, the strongest [[TGFA]] → it (grade B ⚠); 69 go from it, the strongest it → [[TMC6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5493.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +9.4 | 2e-18 | 1/14 (SW1417) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.9 | 1e-12 | 7/23 (SHP-77, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +6.3 | 5e-08 | 2/19 (HCT15, NCI-H1573) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +5.0 | 8e-05 | 7/25 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +5.0 | 8e-05 | 4/24 (A-427, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.8 | 2e-04 | 6/24 (LoVo, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.6 | 3e-04 | 5/24 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.38×** | +4.5 | 4e-04 | 8/24 (COLO 205, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.37×** | +4.2 | 0.001 | 8/24 (COLO 205, LS 180, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 0.001 | 6/24 (LS 180, COLO 205, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.002 | 6/24 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +4.1 | 0.002 | 4/24 (J82, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.78×** | +4.1 | 0.002 | 5/23 (LoVo, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.002 | 7/24 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.003 | 8/24 (SW48, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.005 | 0/24 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.70×** | +3.7 | 0.006 | 11/24 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.011 | 9/24 (COLO 205, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.012 | 6/24 (NCI-H2030, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5493.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.506×** | -13.7 | 8e-40 | 21/23 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.524×** | -8.8 | 3e-16 | 16/24 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.597×** | -7.3 | 5e-11 | 19/25 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -7.0 | 3e-10 | 15/23 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.680×** | -5.5 | 5e-06 | 13/24 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.792×** | -4.7 | 3e-04 | 17/25 (NCI-H2347, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.717×** | -4.5 | 4e-04 | 3/24 (SW48, SW1417, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.741×** | -4.3 | 0.001 | 17/24 (NCI-H2347, HCT15, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.794×** | -4.2 | 0.002 | 11/24 (NCI-H2347, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.767×** | -3.8 | 0.009 | 16/24 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.769×** | -3.7 | 0.010 | 15/24 (LoVo, SW 900, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.829×** | -3.7 | 0.010 | 9/24 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.788×** | -3.4 | 0.030 | 10/24 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.634×** | -3.2 | 0.049 | 11/25 (NCI-H2347, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.801×** | -3.2 | 0.057 | 6/25 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.801×** | -3.2 | 0.057 | 8/24 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.862× | -3.0 | 0.090 | 5/24 (Panc 03.27, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5493. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 65.4 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -19.0) |
| [[NCI-H2347 (line)]] | alt | 148 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0760× (z -30.8) |
| [[HepG2_C3A (line)]] | wt | 41.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -11.0) |
| [[LoVo (line)]] | wt | 25.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -14.7) |
| [[Panc 03.27 (line)]] | alt | 28.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -15.7) |
| [[SW48 (line)]] | wt | 29.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0702× (z -16.4) |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -14.2) |
| [[LS 180 (line)]] | wt | 19.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 15.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0520× (z -17.1) |
| [[SW480 (line)]] | alt | 16.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.253× (z -10.0) |
| [[A549 (line)]] | wt | 8.94 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -10.9) |
| [[BT-474 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -11.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[COLO 205 (line)]] | alt | 31.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -17.7) |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -9.4) |
| [[J82 (line)]] | alt | 3.98 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.5 µM 0.0486× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 7.24 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0817× (z -9.7) |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 1 | — | [[Regorafenib (drug)]] 0.05 µM 0.0543× (z -11.6) |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -12.5) |
| [[SW1417 (line)]] | alt | 22.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -9.7) |
| [[A-172 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5493), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HS3ST1]] | +0.71 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[CRYBG2]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[MYO5B]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[TMC6]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[CLDN4]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[SEMA3B]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.65 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[CDH1]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[INAVA]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[NECTIN4]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[GJB3]] | +0.63 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[JUP]] | +0.62 | +0.70 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 9, C 44. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFA]] | B | TGFA activity raises TTC9's level | lines that do not express TGFA (17) vs lines expressing it (33) | 3.11× lower at baseline in the lines without TGFA | 0.015 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[LEMD1]] | B | LEMD1 activity raises TTC9's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.33× lower at baseline in the lines without LEMD1 | 0.030 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[KCNK1]] | B | KCNK1 activity raises TTC9's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.71× lower at baseline in the lines without KCNK1 | 0.042 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[BLACAT1]] | B | BLACAT1 activity raises TTC9's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 2.43× lower at baseline in the lines without BLACAT1 | 0.056 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[PCDH1]] | B | PCDH1 activity raises TTC9's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without PCDH1 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[EPS8L1]] | B | EPS8L1 activity raises TTC9's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.39× lower at baseline in the lines without EPS8L1 | 0.073 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[BARX2]] | B | BARX2 activity raises TTC9's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 2.69× lower at baseline in the lines without BARX2 | 0.097 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[WNT7B]] | B | WNT7B activity raises TTC9's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.97× lower at baseline in the lines without WNT7B | 0.097 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[PTK2B]] | B | PTK2B activity raises TTC9's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 2.86× lower at baseline in the lines without PTK2B | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[C1orf116]], [[IRF6]] | C | C1orf116, IRF6 activity raises TTC9's level | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (19) | 4.76× lower at baseline in the lines without C1orf116, IRF6 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target; co-absent genes |
| [[CDH1]] | C | CDH1 activity raises TTC9's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 5.20× lower at baseline in the lines without CDH1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |
| [[HS3ST1]] | C | HS3ST1 activity raises TTC9's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 4.27× lower at baseline in the lines without HS3ST1 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4; co-absent with the target |

### Downstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 29, C 40. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMC6]] | B | TTC9 activity raises TMC6's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 3.01× lower at baseline in the lines without TTC9 | 0.010 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[TGFA]] | B | TTC9 activity raises TGFA's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.68× lower at baseline in the lines without TTC9 | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[RDH13]] | B | TTC9 activity raises RDH13's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 1.98× lower at baseline in the lines without TTC9 | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[CORO2A]] | B | TTC9 activity raises CORO2A's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without TTC9 | 0.014 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[ARHGAP27]] | B | TTC9 activity raises ARHGAP27's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without TTC9 | 0.018 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[PKP3]] | B | TTC9 activity raises PKP3's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.65× lower at baseline in the lines without TTC9 | 0.019 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[MYO1D]] | B | TTC9 activity raises MYO1D's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.44× lower at baseline in the lines without TTC9 | 0.021 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[MAP3K9]] | B | TTC9 activity raises MAP3K9's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.48× lower at baseline in the lines without TTC9 | 0.030 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[EPS8L1]] | B | TTC9 activity raises EPS8L1's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without TTC9 | 0.031 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[PTK6]] | B | TTC9 activity raises PTK6's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without TTC9 | 0.038 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[PCDH1]] | B | TTC9 activity raises PCDH1's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.14× lower at baseline in the lines without TTC9 | 0.038 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[TMEM51-AS1]] | B | TTC9 activity raises TMEM51-AS1's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without TTC9 | 0.043 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.1, 56.5); signed map (-1.0, 38.4). **Vector** length 78.0, 23.0% of its response variance represented; |z| ≥ 3 in 596 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +7.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +2.9 | +0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +4.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +4.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -4.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -1.6 | -3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.0 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.1 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:70,641,916-70,675,366 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0227, TTC9A |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q92623](https://www.uniprot.org/uniprotkb/Q92623) carries no function annotation.

**Summary**, from NCBI Gene [23508](https://www.ncbi.nlm.nih.gov/gene/23508):

> This gene encodes a protein that contains three tetratricopeptide repeats. The gene has been shown to be hormonally regulated in breast cancer cells and may play a role in cancer cell invasion and metastasis. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:20267](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20267) · Entrez [23508](https://www.ncbi.nlm.nih.gov/gene/23508) · UniProt [Q92623](https://www.uniprot.org/uniprotkb/Q92623) · Ensembl [ENSG00000133985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133985)

## Data

Gene col 5493: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5493); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5493, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5493]; `tensor/DDL_lfc|DDL_z.npy` [5493]; `embed/gene_vectors.npy` [5493]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5493 or target_col == 5493). Every well: [[TTC9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
