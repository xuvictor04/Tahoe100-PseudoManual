---
symbol: "ENO3"
type: "gene"
col: 2959
ensembl_id: "ENSG00000108515"
name: "enolase 3"
location: "17p13.2"
module: 80
arm: "+"
pooled_cpm: 5.03
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 9
n_dd_up_clean: 17
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# ENO3

*enolase 3* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.94× (z +32.6, q 0e+00, up in 38 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.471× (z -7.6, q 2e-11, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEK8]] (+0.78, fdr 7e-06), [[SIX5]] (+0.76, fdr 7e-06), [[GPR137]] (+0.75, fdr 3e-05); moves opposite to [[GUSBP1]] (-0.62, fdr 1e-05), [[INPP4A]] (-0.62, fdr 3e-05), [[NUTF2]] (-0.60, fdr 2e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2959.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.94×** | +32.6 | 0e+00 | 38/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.74×** | +24.8 | 0e+00 | 37/38 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.25×** | +13.7 | 2e-40 | 35/39 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **4.08×** | +13.6 | 1e-39 | 40/45 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.77×** | +9.5 | 4e-19 | 8/9 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +8.4 | 4e-15 | 24/40 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +8.1 | 5e-14 | 20/34 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +7.3 | 3e-11 | 3/4 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +7.2 | 5e-11 | 12/22 (A549, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.09×** | +5.3 | 8e-06 | 14/30 (NCI-H23, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +4.7 | 1e-04 | 16/46 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.87×** | +4.5 | 4e-04 | 11/35 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +4.4 | 6e-04 | 6/22 (NCI-H460, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +4.3 | 8e-04 | 8/46 (SHP-77, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.78×** | +4.1 | 0.002 | 6/39 (SW480, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.46×** | +3.5 | 0.017 | 5/31 (A498, A549, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.5 | 0.018 | 8/45 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.021 | 10/46 (A-427, SW480, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.57×** | +3.2 | 0.038 | 5/22 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2959.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.471×** | -7.6 | 2e-11 | 25/46 (LOX-IMVI, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.533×** | -6.4 | 4e-08 | 20/45 (C32, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.533×** | -6.4 | 4e-08 | 21/43 (RPMI-7951, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.585×** | -5.4 | 7e-06 | 13/47 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.585×** | -5.4 | 7e-06 | 17/31 (NCI-H2030, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.606×** | -5.1 | 4e-05 | 15/44 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.657×** | -4.3 | 0.002 | 16/47 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.666×** | -4.1 | 0.003 | 16/47 (SW480, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.693×** | -3.7 | 0.013 | 16/46 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.743× | -3.0 | 0.14 | 8/45 (A-427, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2959. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 4.43 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.3× (z +18.5) | — |
| [[PANC-1 (line)]] | alt | 5.20 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +19.1) | — |
| [[LOX-IMVI (line)]] | wt | 3.68 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +11.3) | [[Digitoxin (drug)]] 0.5 µM 0.0636× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 9.25 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +15.1) | [[Digitoxin (drug)]] 5 µM 0.179× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 31.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.155× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 3.70 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.9× (z +18.5) | — |
| [[SW480 (line)]] | alt | 9.79 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +15.8) | — |
| [[A549 (line)]] | wt | 8.18 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.85× (z +13.8) | — |
| [[C32 (line)]] | wt | 5.44 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.91× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0543× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 3.42 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +9.1) | — |
| [[J82 (line)]] | alt | 3.74 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.41× (z +10.5) | [[Erlotinib (drug)]] 5 µM 0.0762× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 3.36 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +12.3) | [[Digitoxin (drug)]] 0.5 µM 0.0583× (z -9.2) |
| [[A-172 (line)]] | wt | 5.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +13.7) | — |
| [[A-427 (line)]] | wt | 17.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.171× (z -9.3) |
| [[A498 (line)]] | wt | 3.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 1.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +9.9) | — |
| [[HCT15 (line)]] | alt | 3.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +10.5) | — |
| [[HepG2_C3A (line)]] | wt | 6.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 1.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.5× (z +12.5) | — |
| [[Hs 766T (line)]] | wt | 2.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 1.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 2.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +9.2) | — |
| [[KATO III (line)]] | alt | 2.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.3× (z +12.4) | — |
| [[RPMI-7951 (line)]] | alt | 2.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 2.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.5× (z +12.5) | — |
| [[SW48 (line)]] | wt | 4.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2959), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEK8]] | +0.78 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[SIX5]] | +0.76 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[GPR137]] | +0.75 | +0.84 / +0.44 | both halves | 3e-05 |  |
| [[PIGV]] | +0.74 | +0.80 / +0.47 | both halves | 2e-05 |  |
| [[MMRN2]] | +0.73 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[WAKMAR2]] | +0.72 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[C19orf54]] | +0.72 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[NANOS3]] | +0.71 | +0.77 / +0.43 | both halves | 3e-05 |  |
| [[LETM2]] | +0.71 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[LPXN]] | +0.71 | +0.74 / +0.46 | both halves | 2e-05 |  |
| [[SEPTIN7-DT]] | +0.70 | +0.75 / +0.41 | both halves | 4e-05 |  |
| [[MZF1-AS1]] | +0.70 | +0.75 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUSBP1]] | -0.62 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[INPP4A]] | -0.62 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[NUTF2]] | -0.60 | -0.61 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ENO3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[OVOL1]] | B | OVOL1 activity lowers ENO3's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.61× higher at baseline in the lines without OVOL1 | 0.040 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[LHFPL6]] | B | LHFPL6 activity raises ENO3's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.46× lower at baseline in the lines without LHFPL6 | 0.079 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[MAGEA4-AS1]] | B | MAGEA4-AS1 activity raises ENO3's level | lines that do not express MAGEA4-AS1 (41) vs lines expressing it (9) | 2.10× lower at baseline in the lines without MAGEA4-AS1 | 0.091 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.824). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, 10.3); signed map (21.0, -6.0). **Vector** length 88.1, 17.1% of its response variance represented; |z| ≥ 3 in 1,124 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.8 | +32.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +24.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.6 | +13.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.5 | +13.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +8.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +3.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -5.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.9 | -7.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.2 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | enolase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,948,092-4,957,131 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Enolases |
| Hallmark sets | FATTY_ACID_METABOLISM, MYOGENESIS, IL2_STAT5_SIGNALING, HYPOXIA |
| Reactome | 4 pathways, smallest: Gluconeogenesis; Glycolysis; Glucose metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P13929](https://www.uniprot.org/uniprotkb/P13929) (Beta-enolase):

> Enolase that catalyzes the conversion of 2-phosphoglycerate to phosphoenolpyruvate in glycolysis and the reverse reaction in gluconeogenesis. Appears to have a function in striated muscle development and regeneration.

**Summary**, from NCBI Gene [2027](https://www.ncbi.nlm.nih.gov/gene/2027):

> This gene encodes one of the three enolase isoenzymes found in mammals. This isoenzyme is found in skeletal muscle cells in the adult where it may play a role in muscle development and regeneration. A switch from alpha enolase to beta enolase occurs in muscle tissue during development in rodents. Mutations in this gene have be associated glycogen storage disease. Alternatively spliced transcript variants encoding different isoforms have been described.[provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:3354](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3354) · Entrez [2027](https://www.ncbi.nlm.nih.gov/gene/2027) · UniProt [P13929](https://www.uniprot.org/uniprotkb/P13929) · Ensembl [ENSG00000108515](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108515)

## Data

Gene col 2959: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2959); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2959, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2959]; `tensor/DDL_lfc|DDL_z.npy` [2959]; `embed/gene_vectors.npy` [2959]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2959 or target_col == 2959). Every well: [[ENO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
