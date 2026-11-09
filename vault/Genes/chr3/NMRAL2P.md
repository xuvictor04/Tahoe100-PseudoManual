---
symbol: "NMRAL2P"
type: "gene"
col: 10145
ensembl_id: "ENSG00000171658"
name: "NmrA like redox sensor 2, pseudogene"
location: "3q27.2"
module: 117
arm: "+"
pooled_cpm: 27.33
n_lines_expressing: 32
n_dd_up: 29
n_dd_down: 15
n_dd_up_clean: 25
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 9
direction_downstream: 24
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# NMRAL2P

*NmrA like redox sensor 2, pseudogene* — 3q27.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.46× (z +14.3, q 2e-43, up in 24 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.260× (z -18.2, q 0e+00, down in 27 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMRAL2P-1]] (+0.90, fdr 7e-06, ⚠ same locus), [[CYP4F11]] (+0.73, fdr 7e-06), [[VEGFD]] (+0.72, fdr 7e-06), [[GCLM]] (+0.72, fdr 7e-06); moves opposite to [[MAN1B1]] (-0.49, fdr 2e-04), [[ACTR1B]] (-0.47, fdr 1e-04), [[DDHD2]] (-0.47, fdr 4e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[AKR1C2]] → it (grade B ⚠); 24 go from it, the strongest it → [[AIFM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10145.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.46×** | +14.3 | 2e-43 | 24/28 (LoVo, SW1417, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.20×** | +10.5 | 3e-23 | 23/29 (LoVo, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.72×** | +9.6 | 2e-19 | 21/29 (COLO 205, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.23×** | +7.7 | 3e-12 | 18/29 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.16×** | +7.4 | 2e-11 | 26/29 (HEC-1-A, Panc 03.27, …) | top dose only |  |
| [[Auranofin (drug)]] 0.5 µM |  | **1.90×** | +6.1 | 1e-07 | 16/29 (KATO III, LoVo, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **2.82×** | +5.2 | 2e-05 | 16/29 (KATO III, SW1417, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Darinaparsin (drug)]] 5 µM |  | **1.41×** | +4.7 | 2e-04 | 16/30 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.62×** | +4.6 | 3e-04 | 13/29 (J82, H4, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.55×** | +4.6 | 3e-04 | 14/31 (SW1417, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.92×** | +4.5 | 4e-04 | 13/30 (COLO 205, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.38×** | +4.3 | 7e-04 | 17/30 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.27×** | +4.1 | 0.002 | 11/25 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.54×** | +3.9 | 0.003 | 11/29 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.47×** | +3.5 | 0.017 | 14/29 (C32, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.017 | 10/30 (A498, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10145.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.260×** | -18.2 | 0e+00 | 27/30 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.213×** | -14.8 | 0e+00 | 29/29 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.230×** | -14.1 | 1e-42 | 29/29 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.283×** | -12.1 | 2e-31 | 28/29 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.299×** | -11.1 | 1e-26 | 22/29 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.445×** | -11.0 | 6e-26 | 26/30 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.545×** | -5.6 | 2e-06 | 16/29 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.563×** | -5.5 | 3e-06 | 15/28 (NCI-H1573, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.349×** | -5.3 | 9e-06 | 21/30 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.706×** | -4.7 | 1e-04 | 20/30 (KATO III, LoVo, …) | two highest doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[APTO-253 (drug)]] 5 µM |  | **0.439×** | -4.1 | 0.002 | 11/28 (A498, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.454×** | -4.0 | 0.004 | 18/30 (NCI-H1573, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.691×** | -3.4 | 0.029 | 13/30 (NCI-H2030, H4, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.706×** | -3.3 | 0.035 | 13/28 (RPMI-7951, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Roxadustat (drug)]] 5 µM |  | **0.716×** | -3.1 | 0.078 | 7/28 (SW 900, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10145. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 25.8 | 2 | 8 (2 ⚠) | [[Auranofin (drug)]] 5 µM 7.04× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.0687× (z -20.5) |
| [[NCI-H1573 (line)]] | alt | 245 | 1 | 7 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.80× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.0791× (z -27.0) |
| [[NCI-H460 (line)]] | wt | 131 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0717× (z -25.3) |
| [[COLO 205 (line)]] | alt | 29.8 | 3 | 4 | [[Ixazomib citrate (drug)]] 0.5 µM 20.5× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.0260× (z -14.5) |
| [[LoVo (line)]] | wt | 14.5 | 2 | 5 | [[Auranofin (drug)]] 5 µM 7.16× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.0751× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 31.8 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.0573× (z -14.9) |
| [[KATO III (line)]] | alt | 12.4 | 2 | 4 | [[Auranofin (drug)]] 5 µM 11.6× (z +9.8) | [[Selinexor (drug)]] 5 µM 0.133× (z -11.4) |
| [[SW480 (line)]] | alt | 16.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -17.4) |
| [[AsPC-1 (line)]] | alt | 36.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -14.2) |
| [[H4 (line)]] | wt | 94.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0409× (z -21.7) |
| [[Panc 03.27 (line)]] | alt | 11.9 | 1 | 4 | [[Auranofin (drug)]] 5 µM 10.8× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.0367× (z -12.0) |
| [[A498 (line)]] | wt | 47.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0191× (z -29.6) |
| [[A549 (line)]] | wt | 27.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0916× (z -15.8) |
| [[Hs 766T (line)]] | wt | 28.3 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -11.0) |
| [[LS 180 (line)]] | wt | 9.95 | 1 | 3 | [[Auranofin (drug)]] 5 µM 8.82× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -13.0) |
| [[A-172 (line)]] | wt | 14.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -10.7) |
| [[HS-578T (line)]] | alt | 9.74 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0441× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 66.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -12.5) |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -11.3) |
| [[J82 (line)]] | alt | 12.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.106× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 8.10 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.50× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.59 | 0 | 1 | — | [[Tomivosertib (drug)]] 0.05 µM 0.0599× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 25.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0499× (z -14.1) |
| [[RPMI-7951 (line)]] | alt | 8.22 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0757× (z -8.5) |
| [[A-427 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.19 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10145), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMRAL2P-1]] | +0.90 | +0.90 / +0.88 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CYP4F11]] | +0.73 | +0.68 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[VEGFD]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[GCLM]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[LINC01564]] | +0.71 | +0.67 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SLC7A11]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TRIM16L]] | +0.69 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[PIR]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[ABCC2]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[AKR1C1]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TXNRD1]] | +0.61 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[GCLC]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PSMA4]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAN1B1]] | -0.49 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[ACTR1B]] | -0.47 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[DDHD2]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SLC25A23]] | -0.46 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[NOTCH2NLA]] | -0.46 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PAIP2B]] | -0.46 | -0.22 / -0.42 | both halves | 6e-04 |  |
| [[LIX1L]] | -0.46 | -0.36 / -0.36 | both halves | 9e-05 |  |
| [[LRRC40]] | -0.46 | -0.32 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C2]] | B | AKR1C2 activity raises NMRAL2P's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 3.55× lower at baseline in the lines without AKR1C2 | 6e-04 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2 |
| [[AKR1C1]] | B | AKR1C1 activity raises NMRAL2P's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 2.68× lower at baseline in the lines without AKR1C1 | 0.012 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[MGST1]] | B | MGST1 activity raises NMRAL2P's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 2.57× lower at baseline in the lines without MGST1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[LINC02057]] | B | LINC02057 activity raises NMRAL2P's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 2.54× lower at baseline in the lines without LINC02057 | 0.094 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[NMRAL2P-1]] | C | NMRAL2P-1 activity raises NMRAL2P's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 4.39× lower at baseline in the lines without NMRAL2P-1 | 4e-05 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1; co-absent with the target |
| [[CYP4F3]] | C | CYP4F3 activity raises NMRAL2P's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.56× lower at baseline in the lines without CYP4F3 | 0.003 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6; co-absent with the target |
| [[AKR1C3]] | C | AKR1C3 activity raises NMRAL2P's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.74× lower at baseline in the lines without AKR1C3 | 0.005 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3; co-absent with the target |
| [[CYP4F11]] | C | CYP4F11 activity raises NMRAL2P's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 3.14× lower at baseline in the lines without CYP4F11 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |
| [[LINC01564]] | C | LINC01564 activity raises NMRAL2P's level | lines that do not express LINC01564 (24) vs lines expressing it (26) | 2.71× lower at baseline in the lines without LINC01564 | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 18, C 6. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AIFM2]] | B | NMRAL2P activity raises AIFM2's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.61× lower at baseline in the lines without NMRAL2P | 0.029 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[RAB5IF]] | B | NMRAL2P activity raises RAB5IF's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.49× lower at baseline in the lines without NMRAL2P | 0.031 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[WARS1]] | B | NMRAL2P activity raises WARS1's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.90× lower at baseline in the lines without NMRAL2P | 0.034 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[GCLC]] | B | NMRAL2P activity raises GCLC's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.74× lower at baseline in the lines without NMRAL2P | 0.038 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[ABCC2]] | B | NMRAL2P activity raises ABCC2's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 2.24× lower at baseline in the lines without NMRAL2P | 0.046 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[ZFAND5]] | B | NMRAL2P activity raises ZFAND5's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.27× lower at baseline in the lines without NMRAL2P | 0.047 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[AKR1C1]] | B | NMRAL2P activity raises AKR1C1's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 2.87× lower at baseline in the lines without NMRAL2P | 0.050 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[MYOM3]] | B | NMRAL2P activity raises MYOM3's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 2.04× lower at baseline in the lines without NMRAL2P | 0.052 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[SLC7A11]] | B | NMRAL2P activity raises SLC7A11's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.76× lower at baseline in the lines without NMRAL2P | 0.057 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[CASP7]] | B | NMRAL2P activity raises CASP7's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.50× lower at baseline in the lines without NMRAL2P | 0.067 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[SEL1L3]] | B | NMRAL2P activity raises SEL1L3's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.81× lower at baseline in the lines without NMRAL2P | 0.070 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[TIRAP]] | B | NMRAL2P activity raises TIRAP's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.16× lower at baseline in the lines without NMRAL2P | 0.082 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.804). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.6, 48.1); signed map (51.4, -10.3). **Vector** length 98.9, 28.2% of its response variance represented; |z| ≥ 3 in 830 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NRF2* (control, mean cos +0.58 to 8); *Nuclear events mediated by NFE2L2* (reactome, mean cos +0.61 to 7); *KEAP1-NFE2L2 pathway* (reactome, mean cos +0.61 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.8 | +14.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.4 | +10.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.0 | +9.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.7 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +7.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.4 | -12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -18.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -14.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -11.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -14.1 |
|  | [[Salicylic acid (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Roxadustat (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | NmrA like redox sensor 2, pseudogene |
| Locus type | pseudogene |
| Location | 3q27.2 — chr3:185,960,039-185,979,837 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | LOC344887; previously NMRAL1P1 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52332) · Entrez [344887](https://www.ncbi.nlm.nih.gov/gene/344887) · Ensembl [ENSG00000171658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171658)

## Data

Gene col 10145: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10145); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10145, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10145]; `tensor/DDL_lfc|DDL_z.npy` [10145]; `embed/gene_vectors.npy` [10145]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10145 or target_col == 10145). Every well: [[NMRAL2P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NMRAL2P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
