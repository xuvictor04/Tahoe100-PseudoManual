---
symbol: "HPS1"
type: "gene"
col: 2855
ensembl_id: "ENSG00000107521"
name: "HPS1 biogenesis of lysosomal organelles complex 3 subunit 1"
location: "10q24.2"
module: 23
arm: "+"
pooled_cpm: 24.89
n_lines_expressing: 47
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# HPS1

*HPS1 biogenesis of lysosomal organelles complex 3 subunit 1* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.12× (z +11.9, q 4e-30, up in 37 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.45× (z +8.4, q 8e-15, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.392× (z -7.8, q 4e-12, down in 36 of 43 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRAGC-DT]] (+0.74, fdr 7e-06), [[RRAGB]] (+0.71, fdr 1e-05), [[WASHC2C]] (+0.68, fdr 7e-06); moves opposite to [[LSM4]] (-0.62, fdr 1e-05), [[NCAPD3]] (-0.60, fdr 1e-05), [[RTTN]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC26A11]] → it (grade B ⚠); 4 go from it, the strongest it → cells under [[Tucidinostat (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2855.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +11.9 | 4e-30 | 37/40 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +11.4 | 1e-27 | 27/33 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +9.2 | 4e-18 | 29/38 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +8.4 | 8e-15 | 36/45 (A-427, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.0 | 2e-07 | 27/43 (COLO 205, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +5.9 | 4e-07 | 21/44 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +4.7 | 2e-04 | 22/45 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.6 | 2e-04 | 20/45 (LS 180, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +4.6 | 3e-04 | 19/45 (PANC-1, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.4 | 7e-04 | 18/45 (LS 180, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.008 | 18/44 (A498, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.015 | 7/43 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.018 | 10/44 (PANC-1, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.058 | 11/45 (LoVo, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.075 | 11/45 (NCI-H460, H4, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.075 | 12/45 (PANC-1, LS 180, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.075 | 9/43 (SW480, A498, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.082 | 12/45 (MIA PaCa-2, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2855.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.392×** | -7.8 | 4e-12 | 36/43 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.449×** | -6.6 | 9e-09 | 37/45 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -5.6 | 4e-06 | 29/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.719×** | -5.2 | 2e-05 | 22/45 (SNU-423, Hs 766T, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.725×** | -5.1 | 3e-05 | 20/45 (SNU-423, SW480, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.725×** | -5.1 | 3e-05 | 24/45 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.748×** | -4.6 | 3e-04 | 19/45 (A-172, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.778×** | -4.0 | 0.005 | 17/44 (PANC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.776×** | -3.8 | 0.009 | 19/44 (HS-578T, C32, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.801×** | -3.5 | 0.023 | 18/45 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.682×** | -3.2 | 0.076 | 11/43 (SHP-77, J82, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.826× | -3.0 | 0.11 | 16/44 (AsPC-1, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2855. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 32.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 25.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +10.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 27.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.02× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 20.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -11.4) |
| [[AN3 CA (line)]] | alt | 39.8 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0963× (z -10.0) |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -11.8) |
| [[C32 (line)]] | wt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.182× (z -10.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H1573 (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 27.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.5) | — |
| [[RKO (line)]] | wt | 22.6 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.228× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.392× (z -8.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +12.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.38 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.05 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2855), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAGC-DT]] | +0.74 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[RRAGB]] | +0.71 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[WASHC2C]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[DUSP3]] | +0.67 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[TMEM192]] | +0.67 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[C1orf43]] | +0.67 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[GPRASP3]] | +0.67 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[HEXA]] | +0.65 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[WASHC2A]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[GNPDA1]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[MR1]] | +0.64 | +0.65 / +0.36 | both halves | 9e-05 |  |
| [[N4BP2L1]] | +0.63 | +0.69 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM4]] | -0.62 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[NCAPD3]] | -0.60 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[RTTN]] | -0.59 | -0.55 / -0.40 | both halves | 4e-05 |  |
| [[NHP2]] | -0.59 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[NPHP4]] | -0.58 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[UBE2T]] | -0.57 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[RNF168]] | -0.57 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[SLX4]] | -0.57 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[GINS2]] | -0.56 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[GNB1L]] | -0.56 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[DGKD]] | -0.55 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[TCF19]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC26A11]] | B | SLC26A11 activity raises HPS1's level | lines that do not express SLC26A11 (5) vs lines expressing it (45) | 1.21× lower at baseline in the lines without SLC26A11 | 0.060 | ⚠ within organs, on part of the lines; also absent: DENND5B, SMAD4, MINAR1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises HPS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tucidinostat (drug)]] 5 µM | C | HPS1 activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express HPS1 (3) vs lines expressing it (45) | the lines without HPS1: 0.80× the cells of the other lines | 0.019 | ⚠ few lines (3 vs 47); across organs; also absent: SH3D19, PWWP2B, APOBEC3B; maybe low, not absent |
| cells under [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM | C | HPS1 activity raises the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express HPS1 (3) vs lines expressing it (45) | the lines without HPS1: 0.71× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: SH3D19, PWWP2B, APOBEC3B; maybe low, not absent |
| cells under [[Dabrafenib (drug)]] 5 µM | C | HPS1 activity lowers the cells' numbers under Dabrafenib 5 µM (makes them more sensitive) | lines that do not express HPS1 (3) vs lines expressing it (45) | the lines without HPS1: 1.68× the cells of the other lines | 0.044 | ⚠ few lines (3 vs 47); across organs; also absent: SH3D19, PWWP2B, APOBEC3B; maybe low, not absent |
| cells under [[Bimiralisib (drug)]] 0.05 µM | C | HPS1 activity raises the cells' numbers under Bimiralisib 0.05 µM (protects the cells) | lines that do not express HPS1 (3) vs lines expressing it (45) | the lines without HPS1: 0.70× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); across organs; also absent: SH3D19, PWWP2B, APOBEC3B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-18.8, 14.1); signed map (16.2, -14.4). **Vector** length 86.6, 19.3% of its response variance represented; |z| ≥ 3 in 771 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.5 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +5.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.9 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +4.6 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +2.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.9 | -5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -4.8 | -5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -4.6 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -7.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -4.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | HPS1 biogenesis of lysosomal organelles complex 3 subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:98,410,939-98,446,963 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BLOC3S1; previously HPS |
| Gene groups (HGNC) | Biogenesis of lysosomal organelles complex 3 ; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92902](https://www.uniprot.org/uniprotkb/Q92902) (BLOC-3 complex member HPS1):

> Component of the BLOC-3 complex, a complex that acts as a guanine exchange factor (GEF) for RAB32 and RAB38, promotes the exchange of GDP to GTP, converting them from an inactive GDP-bound form into an active GTP-bound form. The BLOC-3 complex plays an important role in the control of melanin production and melanosome biogenesis and promotes the membrane localization of RAB32 and RAB38.

**Summary**, from NCBI Gene [3257](https://www.ncbi.nlm.nih.gov/gene/3257):

> This gene encodes a protein that may play a role in organelle biogenesis associated with melanosomes, platelet dense granules, and lysosomes. The encoded protein is a component of three different protein complexes termed biogenesis of lysosome-related organelles complex (BLOC)-3, BLOC4, and BLOC5. Mutations in this gene are associated with Hermansky-Pudlak syndrome type 1. Alternative splicing results in multiple transcript variants. A pseudogene related to this gene is located on chromosome …

**Accessions** — [HGNC:5163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5163) · Entrez [3257](https://www.ncbi.nlm.nih.gov/gene/3257) · UniProt [Q92902](https://www.uniprot.org/uniprotkb/Q92902) · Ensembl [ENSG00000107521](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107521)

## Data

Gene col 2855: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2855); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2855, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2855]; `tensor/DDL_lfc|DDL_z.npy` [2855]; `embed/gene_vectors.npy` [2855]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2855 or target_col == 2855). Every well: [[HPS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HPS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
