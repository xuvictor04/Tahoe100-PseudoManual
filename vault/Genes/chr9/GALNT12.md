---
symbol: "GALNT12"
type: "gene"
col: 4074
ensembl_id: "ENSG00000119514"
name: "polypeptide N-acetylgalactosaminyltransferase 12"
location: "9q22.33"
module: 154
arm: "+"
pooled_cpm: 21.38
n_lines_expressing: 40
n_dd_up: 10
n_dd_down: 32
n_dd_up_clean: 9
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 10
direction_downstream: 15
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# GALNT12

*polypeptide N-acetylgalactosaminyltransferase 12* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.64× (z +8.6, q 3e-15, up in 28 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.291× (z -21.4, q 0e+00, down in 35 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WSCD1]] (+0.74, fdr 7e-06), [[KHDRBS3]] (+0.71, fdr 7e-06), [[PKIA]] (+0.67, fdr 7e-06); moves opposite to [[EFCAB2]] (-0.60, fdr 3e-05), [[LINC00886]] (-0.59, fdr 4e-05), [[BDNF-AS]] (-0.58, fdr 3e-04).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PODXL]] → it (grade B ⚠); 15 go from it, the strongest it → [[KIAA0825]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4074.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +8.6 | 3e-15 | 28/38 (A498, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +5.2 | 4e-05 | 16/37 (A498, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +5.2 | 5e-05 | 19/37 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.47×** | +4.8 | 3e-04 | 18/37 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.30×** | +4.7 | 3e-04 | 15/38 (NCI-H1573, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +4.5 | 6e-04 | 19/37 (LoVo, BT-474, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.29×** | +4.5 | 6e-04 | 18/38 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.071 | 11/38 (HOP62, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.071 | 8/35 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.088 | 8/35 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.05 µM |  | 1.31× | +3.1 | 0.10 | 11/37 (NCI-H2347, HOP62, …) | all doses, flat |  |
| [[Tazarotene (drug)]] 5 µM |  | 1.27× | +3.0 | 0.11 | 7/38 (A-172, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4074.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.291×** | -21.4 | 0e+00 | 35/37 (A549, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.220×** | -17.9 | 0e+00 | 33/36 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.292×** | -15.1 | 0e+00 | 24/33 (RPMI-7951, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.469×** | -13.1 | 3e-37 | 31/36 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.438×** | -10.1 | 5e-22 | 32/37 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.532×** | -7.7 | 1e-12 | 26/37 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.577×** | -6.7 | 1e-09 | 23/37 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.579×** | -6.7 | 2e-09 | 22/36 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.366×** | -6.4 | 7e-09 | 26/38 (A-172, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.373×** | -6.3 | 1e-08 | 25/34 (A-172, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.605×** | -6.2 | 4e-08 | 24/36 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.614×** | -5.7 | 4e-07 | 21/36 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.732×** | -5.4 | 3e-06 | 24/38 (A-172, A549, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.633×** | -5.3 | 5e-06 | 20/37 (SW48, SW480, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.763×** | -4.7 | 1e-04 | 19/38 (A-172, Hs 766T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.700×** | -4.4 | 5e-04 | 14/37 (A-172, NCI-H1792, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4074. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 64.9 | 0 | 16 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0154× (z -26.6) |
| [[NCI-H460 (line)]] | wt | 20.9 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0931× (z -25.2) |
| [[A549 (line)]] | wt | 38.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0449× (z -27.4) |
| [[HEC-1-A (line)]] | alt | 132 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -20.3) |
| [[RPMI-7951 (line)]] | alt | 41.9 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0244× (z -26.5) |
| [[Hs 766T (line)]] | wt | 31.7 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0739× (z -19.3) |
| [[LoVo (line)]] | wt | 42.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -15.8) |
| [[RKO (line)]] | wt | 21.5 | 2 (1 ⚠) | 3 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 7.06× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 44.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -17.0) |
| [[HT-29 (line)]] | alt | 32.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 26.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0816× (z -17.2) |
| [[Panc 03.27 (line)]] | alt | 22.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -16.4) |
| [[A498 (line)]] | wt | 15.8 | 2 (1 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 3.19× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -13.1) |
| [[KATO III (line)]] | alt | 28.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 20.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0808× (z -16.7) |
| [[SNU-423 (line)]] | alt | 23.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -14.2) |
| [[SW48 (line)]] | wt | 34.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.9) |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -13.4) |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -11.5) |
| [[A-427 (line)]] | wt | 11.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0639× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 41.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.135× (z -11.6) |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.144× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.170× (z -8.8) |
| [[SW480 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.267× (z -9.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.74 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4074), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WSCD1]] | +0.74 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[KHDRBS3]] | +0.71 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PKIA]] | +0.67 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[UBA6]] | +0.67 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[DNMT3B]] | +0.66 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[TNFRSF11A]] | +0.66 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[CELSR1]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[NRIP3]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[GRK5]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[FAM124A]] | +0.62 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[LPCAT2]] | +0.61 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[CALB2]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | -0.60 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[LINC00886]] | -0.59 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[BDNF-AS]] | -0.58 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[NNMT]] | -0.58 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZFX]] | -0.58 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ZRANB2-DT]] | -0.57 | -0.48 / -0.43 | both halves | 4e-05 |  |
| [[ZMYND11]] | -0.57 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[CFLAR]] | -0.56 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[CAPN3]] | -0.56 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[CHD1-DT]] | -0.55 | -0.59 / -0.22 | both halves | 6e-04 |  |
| [[ENTPD3-AS1]] | -0.55 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[HECTD1]] | -0.54 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL]] | B | PODXL activity raises GALNT12's level | lines that do not express PODXL (24) vs lines expressing it (26) | 3.00× lower at baseline in the lines without PODXL | 0.002 | ⚠ within organs, on part of the lines; also absent: IL32, LGR6, SERPINB9; maybe low, not absent |
| [[SYTL4]] | B | SYTL4 activity raises GALNT12's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 2.60× lower at baseline in the lines without SYTL4 | 0.029 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[TOP2A]] | B | TOP2A activity raises GALNT12's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KIAA0825]] | B | KIAA0825 activity lowers GALNT12's level | lines that do not express KIAA0825 (9) vs lines expressing it (41) | 1.90× higher at baseline in the lines without KIAA0825 | 0.055 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, SPART, CCDC102B; maybe low, not absent |
| [[PLCG2]] | B | PLCG2 activity raises GALNT12's level | lines that do not express PLCG2 (10) vs lines expressing it (40) | 2.81× lower at baseline in the lines without PLCG2 | 0.074 | ⚠ within organs, on part of the lines; also absent: CRACD; maybe low, not absent |
| [[PLAUR]] | B | PLAUR activity raises GALNT12's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 2.77× lower at baseline in the lines without PLAUR | 0.076 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers GALNT12's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds |
| [[OCIAD2]] | B | OCIAD2 activity raises GALNT12's level | lines that do not express OCIAD2 (10) vs lines expressing it (40) | 2.30× lower at baseline in the lines without OCIAD2 | 0.081 | ⚠ within organs, on part of the lines; also absent: CDCP1, STAMBPL1, SLCO4A1 |
| [[COL4A4]] | B | COL4A4 activity raises GALNT12's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 1.66× lower at baseline in the lines without COL4A4 | 0.093 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GALNT12's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA0825]] | B | GALNT12 activity lowers KIAA0825's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 1.38× higher at baseline in the lines without GALNT12 | 0.021 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[ATP1A3]] | B | GALNT12 activity lowers ATP1A3's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 1.01× higher at baseline in the lines without GALNT12 | 0.026 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[KIAA1671]] | B | GALNT12 activity raises KIAA1671's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 2.15× lower at baseline in the lines without GALNT12 | 0.032 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[CELSR1]] | B | GALNT12 activity raises CELSR1's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 2.42× lower at baseline in the lines without GALNT12 | 0.033 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[PBX4]] | B | GALNT12 activity raises PBX4's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 2.20× lower at baseline in the lines without GALNT12 | 0.047 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[ZFX]] | B | GALNT12 activity raises ZFX's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 1.35× lower at baseline in the lines without GALNT12 | 0.057 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[PLCG2]] | B | GALNT12 activity raises PLCG2's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 3.35× lower at baseline in the lines without GALNT12 | 0.057 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[CALB2]] | B | GALNT12 activity raises CALB2's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 3.01× lower at baseline in the lines without GALNT12 | 0.066 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[KRT15]] | B | GALNT12 activity raises KRT15's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 2.06× lower at baseline in the lines without GALNT12 | 0.069 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[SYTL4]] | B | GALNT12 activity raises SYTL4's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 2.86× lower at baseline in the lines without GALNT12 | 0.072 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[FABP5]] | B | GALNT12 activity lowers FABP5's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 1.13× higher at baseline in the lines without GALNT12 | 0.084 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[NGEF]] | B | GALNT12 activity raises NGEF's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 2.48× lower at baseline in the lines without GALNT12 | 0.086 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.760). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.3, -1.3); signed map (-3.1, 48.8). **Vector** length 112, 28.9% of its response variance represented; |z| ≥ 3 in 1,241 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.6 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.0 | +5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.7 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.2 | +1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.4 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -17.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.4 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -15.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.0 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.9 | -3.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.6 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -6.3 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:98,807,670-98,850,081 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GalNAc-T12 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases |
| Reactome | 6 pathways, smallest: Defective GALNT12 causes CRCS1; O-linked glycosylation of mucins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXK2](https://www.uniprot.org/uniprotkb/Q8IXK2) (Polypeptide N-acetylgalactosaminyltransferase 12):

> Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor. Has activity toward non-glycosylated peptides such as Muc5AC, Muc1a and EA2, and no detectable activity with Muc2 and Muc7. Displays enzymatic activity toward the Gal-NAc-Muc5AC glycopeptide, but no detectable activity to mono-GalNAc-glycosylated Muc1a, Muc2, Muc7 and EA2. May play an important role in the initial …

**Summary**, from NCBI Gene [79695](https://www.ncbi.nlm.nih.gov/gene/79695):

> This gene encodes a member of a family of UDP-GalNAc:polypeptide N-acetylgalactosaminyltransferases, which catalyze the transfer of N-acetylgalactosamine (GalNAc) from UDP-GalNAc to a serine or threonine residue on a polypeptide acceptor in the initial step of O-linked protein glycosylation. Mutations in this gene are associated with an increased susceptibility to colorectal cancer.[provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:19877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19877) · Entrez [79695](https://www.ncbi.nlm.nih.gov/gene/79695) · UniProt [Q8IXK2](https://www.uniprot.org/uniprotkb/Q8IXK2) · Ensembl [ENSG00000119514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119514)

## Data

Gene col 4074: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4074); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4074, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4074]; `tensor/DDL_lfc|DDL_z.npy` [4074]; `embed/gene_vectors.npy` [4074]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4074 or target_col == 4074). Every well: [[GALNT12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
