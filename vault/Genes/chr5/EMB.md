---
symbol: "EMB"
type: "gene"
col: 9976
ensembl_id: "ENSG00000170571"
name: "embigin"
location: "5q11.1"
module: 29
arm: "+"
pooled_cpm: 20.02
n_lines_expressing: 29
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# EMB

*embigin* — 5q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.43× (z +18.4, q 0e+00, up in 23 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.33× (z +4.2, q 0.003, up in 10 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.310× (z -24.9, q 0e+00, down in 26 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GALNT1]] (+0.73, fdr 7e-06), [[PPT1]] (+0.67, fdr 1e-05), [[MOB1A]] (+0.67, fdr 7e-06); moves opposite to [[TRAPPC2B]] (-0.66, fdr 7e-06), [[INAFM1]] (-0.65, fdr 7e-06), [[PIAS4]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[TBC1D1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9976.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.43×** | +18.4 | 0e+00 | 23/24 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +15.3 | 0e+00 | 15/16 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +11.3 | 4e-27 | 19/23 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.25×** | +4.7 | 4e-04 | 10/27 (NCI-H1792, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.003 | 10/27 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.011 | 10/27 (LoVo, NCI-H460, …) | rises with dose | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.064 | 5/27 (LOX-IMVI, SHP-77, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.10 | 5/27 (LOX-IMVI, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9976.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.310×** | -24.9 | 0e+00 | 26/27 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.461×** | -11.6 | 9e-29 | 19/27 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.450×** | -11.5 | 2e-28 | 25/27 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.494×** | -10.6 | 5e-24 | 22/27 (Panc 03.27, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.542×** | -9.2 | 4e-18 | 21/27 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.620×** | -7.2 | 6e-11 | 20/27 (Panc 03.27, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.677×** | -5.9 | 3e-07 | 17/27 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.696×** | -5.1 | 2e-05 | 14/27 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.728×** | -4.8 | 1e-04 | 14/27 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.791×** | -3.5 | 0.023 | 9/27 (A-427, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.799×** | -3.4 | 0.034 | 14/27 (SW 900, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.812×** | -3.1 | 0.079 | 7/27 (PANC-1, NCI-H460, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9976. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 58.5 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -25.9) |
| [[A-427 (line)]] | wt | 92.7 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.385× (z -13.6) |
| [[HS-578T (line)]] | alt | 52.0 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 6.57× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 72.9 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.26× (z +16.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 13.8 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -17.6) |
| [[J82 (line)]] | alt | 18.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -18.4) |
| [[NCI-H2030 (line)]] | alt | 47.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -16.6) |
| [[NCI-H2347 (line)]] | alt | 70.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -23.2) |
| [[Panc 03.27 (line)]] | alt | 62.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -14.9) |
| [[RKO (line)]] | wt | 19.8 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.112× (z -12.3) |
| [[LoVo (line)]] | wt | 9.74 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0948× (z -20.2) |
| [[LOX-IMVI (line)]] | wt | 26.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -17.2) |
| [[NCI-H1573 (line)]] | alt | 15.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.55× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0880× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 14.3 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -9.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.319× (z -8.9) |
| [[SW 900 (line)]] | alt | 23.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.77× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 32.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -14.4) |
| [[SHP-77 (line)]] | alt | 42.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -9.6) |
| [[Hs 766T (line)]] | wt | 8.21 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.3) |
| [[A-172 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9976), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GALNT1]] | +0.73 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[PPT1]] | +0.67 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[MOB1A]] | +0.67 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[DHFR]] | +0.64 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[FUCA2]] | +0.64 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[HNRNPA3]] | +0.64 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[BTBD1]] | +0.64 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[NAE1]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[NCKAP1]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[CRTAP]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[STRADB]] | +0.62 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[IPO5]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC2B]] | -0.66 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.65 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[PIAS4]] | -0.63 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[NFKBIL1]] | -0.62 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[ZKSCAN1]] | -0.61 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ZNF324]] | -0.60 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[TTF1]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[MED19]] | -0.59 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[MTHFR]] | -0.59 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[PMM1]] | -0.59 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[SMIM26]] ⚠ | -0.59 | -0.53 / -0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ING2]] | -0.58 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[CCDC174]] | -0.58 | -0.57 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises EMB's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises EMB's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SUSD5]] | C | SUSD5 activity raises EMB's level | lines that do not express SUSD5 (23) vs lines expressing it (27) | 5.29× lower at baseline in the lines without SUSD5 | 0.025 | ⚠ within organs, on part of the lines; also absent: EDIL3, BVES, MAP9; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D1]] | B | EMB activity lowers TBC1D1's level | lines that do not express EMB (21) vs lines expressing it (29) | 1.17× higher at baseline in the lines without EMB | 0.061 | ⚠ within organs, on part of the lines; also absent: CACNA2D1, SUSD5, PKIA |
| [[GPATCH1]] | B | EMB activity lowers GPATCH1's level | lines that do not express EMB (21) vs lines expressing it (29) | 1.29× higher at baseline in the lines without EMB | 0.071 | ⚠ within organs, on part of the lines; also absent: CACNA2D1, SUSD5, PKIA |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.716). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-27.9, -21.0); signed map (-19.3, -38.5). **Vector** length 74.7, 19.2% of its response variance represented; |z| ≥ 3 in 611 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +18.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +11.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.5 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | -2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -24.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -11.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -5.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.4 | -0.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | embigin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.1 — chr5:50,396,192-50,443,248 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC71745, GP70 |
| Gene groups (HGNC) | I-set domain containing; Basigin family |
| Reactome | 4 pathways, smallest: Proton-coupled monocarboxylate transport; SLC-mediated transport of organic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PCB8](https://www.uniprot.org/uniprotkb/Q6PCB8) (Embigin):

> Plays a role in the outgrowth of motoneurons and in the formation of neuromuscular junctions. Following muscle denervation, promotes nerve terminal sprouting and the formation of additional acetylcholine receptor clusters at synaptic sites without affecting terminal Schwann cell number or morphology. Delays the retraction of terminal sprouts following re-innervation of denervated endplates. May play a role in targeting the monocarboxylate transporters SLC16A1, SLC16A6 and SLC16A7 to the cell …

**Summary**, from NCBI Gene [133418](https://www.ncbi.nlm.nih.gov/gene/133418):

> This gene encodes a transmembrane glycoprotein that is a member of the immunoglobulin superfamily. The encoded protein may be involved in cell growth and development by mediating interactions between the cell and extracellular matrix. A pseudogene of this gene is found on chromosome 1. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:30465](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30465) · Entrez [133418](https://www.ncbi.nlm.nih.gov/gene/133418) · UniProt [Q6PCB8](https://www.uniprot.org/uniprotkb/Q6PCB8) · Ensembl [ENSG00000170571](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170571)

## Data

Gene col 9976: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9976); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9976, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9976]; `tensor/DDL_lfc|DDL_z.npy` [9976]; `embed/gene_vectors.npy` [9976]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9976 or target_col == 9976). Every well: [[EMB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
