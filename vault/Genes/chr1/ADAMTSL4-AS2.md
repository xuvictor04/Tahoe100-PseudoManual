---
symbol: "ADAMTSL4-AS2"
type: "gene"
col: 14151
ensembl_id: "ENSG00000237781"
name: "ADAMTSL4 antisense RNA 2"
location: "1q21.2"
module: 38
arm: "+"
pooled_cpm: 12.65
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 37
n_dd_up_clean: 13
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# ADAMTSL4-AS2

*ADAMTSL4 antisense RNA 2* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.23× (z +14.9, q 0e+00, up in 33 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (6 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 0.454× (z -7.1, q 6e-10, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THUMPD3-AS1]] (+0.78, fdr 7e-06), [[MCL1]] (+0.77, fdr 7e-06, ⚠ read-through risk), [[C21orf91-OT1]] (+0.73, fdr 7e-06), [[ERI2]] (+0.72, fdr 7e-06); moves opposite to [[ARHGAP17]] (-0.58, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DNAH17]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14151.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.23×** | +14.9 | 0e+00 | 33/41 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.74×** | +12.8 | 4e-35 | 38/43 (MIA PaCa-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.75×** | +9.1 | 2e-17 | 33/44 (HT-29, NCI-H2347, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +5.9 | 5e-07 | 22/41 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.40×** | +5.0 | 6e-05 | 23/44 (NCI-H460, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.74×** | +5.0 | 6e-05 | 25/47 (HT-29, A498, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.8 | 1e-04 | 15/46 (NCI-H2347, A-172, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +4.6 | 3e-04 | 19/42 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **1.43×** | +4.5 | 4e-04 | 20/46 (NCI-H1792, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.86×** | +4.3 | 1e-03 | 6/18 (A498, NCI-H2030, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.1 | 0.002 | 17/41 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **2.38×** | +3.5 | 0.019 | 7/46 (HT-29, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Naproxen (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.051 | 9/43 (SW48, CHP-212, …) | all doses, flat | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.14×** | +3.1 | 0.078 | 9/41 (A498, HT-29, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14151.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.454×** | -7.1 | 6e-10 | 31/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.457×** | -7.0 | 6e-10 | 32/43 (HepG2/C3A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.439×** | -6.8 | 3e-09 | 28/44 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.481×** | -6.6 | 7e-09 | 32/46 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.483×** | -6.5 | 7e-09 | 28/47 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.513×** | -6.3 | 3e-08 | 32/47 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.234×** | -5.9 | 2e-07 | 25/41 (hTERT-HPNE, HS-578T, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.586×** | -5.9 | 3e-07 | 23/46 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.497×** | -5.7 | 6e-07 | 27/41 (NCI-H1573, AsPC-1, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.446×** | -5.3 | 5e-06 | 24/46 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -5.2 | 1e-05 | 23/41 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.670×** | -5.1 | 2e-05 | 22/46 (AsPC-1, NCI-H23, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.561×** | -4.8 | 8e-05 | 21/43 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.561×** | -4.8 | 8e-05 | 24/43 (Panc 03.27, SW 900, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.683×** | -4.7 | 8e-05 | 15/46 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.615×** | -4.6 | 2e-04 | 20/47 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.617×** | -4.3 | 5e-04 | 17/46 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14151. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 32.5 | 0 | 5 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0649× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 41.3 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0109× (z -20.2) ⚠ toxic · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0311× (z -15.5) |
| [[PANC-1 (line)]] | alt | 20.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 30.2 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0812× (z -11.3) |
| [[BT-474 (line)]] | alt | 32.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0773× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0673× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.0955× (z -8.6) |
| [[HT-29 (line)]] | alt | 11.8 | 1 | 1 | [[Auranofin (drug)]] 5 µM 8.65× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 7.18 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.47× (z +9.4) | [[Benproperine (phosphate) (drug)]] 5 µM 0.0539× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 8.92 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 21.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +15.7) | [[Digitoxin (drug)]] 5 µM 0.122× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 8.55 | 2 | 0 | [[Auranofin (drug)]] 5 µM 12.4× (z +8.5) | — |
| [[C32 (line)]] | wt | 5.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.8× (z +13.3) | — |
| [[HEC-1-A (line)]] | alt | 7.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0824× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HS-578T (line)]] | alt | 5.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.30× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 20.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0857× (z -9.6) |
| [[J82 (line)]] | alt | 4.48 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0682× (z -9.4) |
| [[LoVo (line)]] | wt | 4.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 25.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.77× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.139× (z -9.7) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 6.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.34× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 5.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.39× (z +9.6) | — |
| [[SW480 (line)]] | alt | 5.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.89× (z +12.1) | — |
| [[A-172 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14151), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THUMPD3-AS1]] | +0.78 | +0.77 / +0.72 | both halves | 7e-06 | same gene group |
| [[MCL1]] | +0.77 | +0.75 / +0.77 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 3.2 kb 3′ of MCL1 on the same strand (can correlate by spillover, not regulation) |
| [[C21orf91-OT1]] | +0.73 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[ERI2]] | +0.72 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[PPIEL]] | +0.71 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[PPIEL-1]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[LAT2]] | +0.70 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[NOP14-AS1]] | +0.70 | +0.71 / +0.64 | both halves | 7e-06 | same gene group |
| [[SLC9A5]] | +0.70 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.68 | +0.69 / +0.59 | both halves | 7e-06 | same gene group |
| [[TRIM72]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MMP25]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP17]] | -0.58 | -0.61 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAH17]] | B | DNAH17 activity raises ADAMTSL4-AS2's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 2.02× lower at baseline in the lines without DNAH17 | 0.017 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ADAMTSL4-AS2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.2, -16.9); signed map (11.1, 13.9). **Vector** length 124, 33.7% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.4 | +9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +14.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +12.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.7 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +1.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.6 | -6.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.6 | -7.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.2 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.2 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.2 | -7.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.1 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.1 | -6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.0 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | ADAMTSL4 antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q21.2 — chr1:150,548,562-150,557,724 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40895](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40895) · Entrez [100289061](https://www.ncbi.nlm.nih.gov/gene/100289061) · Ensembl [ENSG00000237781](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237781)

## Data

Gene col 14151: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14151); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14151, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14151]; `tensor/DDL_lfc|DDL_z.npy` [14151]; `embed/gene_vectors.npy` [14151]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14151 or target_col == 14151). Every well: [[ADAMTSL4-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTSL4-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
