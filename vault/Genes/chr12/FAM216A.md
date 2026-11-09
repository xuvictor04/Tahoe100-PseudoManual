---
symbol: "FAM216A"
type: "gene"
col: 12927
ensembl_id: "ENSG00000204856"
name: "family with sequence similarity 216 member A"
location: "12q24.11"
module: 144
arm: "+"
pooled_cpm: 24.53
n_lines_expressing: 43
n_dd_up: 16
n_dd_down: 23
n_dd_up_clean: 10
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 15
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# FAM216A

*family with sequence similarity 216 member A* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.91× (z +7.4, q 8e-11, up in 24 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +6.9, q 2e-09, up in 25 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.410× (z -10.2, q 1e-21, down in 37 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIPK2A]] (+0.63, fdr 1e-05), [[ACAD11]] (+0.59, fdr 2e-05), [[MIX23]] (+0.58, fdr 3e-05); moves opposite to [[RMC1]] (-0.50, fdr 3e-05), [[GDI1]] (-0.50, fdr 3e-05), [[PHF1]] (-0.49, fdr 9e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SMAD9]] → it (grade B ⚠); 15 go from it, the strongest it → [[TSR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12927.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.91×** | +7.4 | 8e-11 | 24/38 (A498, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +6.9 | 2e-09 | 25/41 (NCI-H1792, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.57×** | +5.0 | 1e-04 | 15/26 (A549, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.52×** | +4.8 | 2e-04 | 21/41 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.47×** | +4.1 | 0.005 | 17/40 (NCI-H460, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.007 | 18/41 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.23×** | +3.4 | 0.048 | 13/41 (A-172, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.37×** | +3.4 | 0.051 | 12/32 (SW480, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.3 | 0.059 | 14/39 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.063 | 16/41 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.072 | 11/39 (AsPC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.094 | 10/40 (SW480, SNU-1, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.67×** | +3.1 | 0.094 | 11/39 (AsPC-1, A549, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.66×** | +3.0 | 0.094 | 10/41 (HS-578T, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.50×** | +3.0 | 0.095 | 11/40 (Hs 766T, NCI-H23, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.095 | 10/40 (AsPC-1, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12927.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.410×** | -10.2 | 1e-21 | 37/41 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.543×** | -9.9 | 2e-20 | 31/40 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.511×** | -7.7 | 3e-12 | 39/40 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.517×** | -7.5 | 7e-12 | 35/40 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.542×** | -7.0 | 3e-10 | 32/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.546×** | -6.9 | 5e-10 | 28/41 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.602×** | -5.8 | 6e-07 | 27/41 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.607×** | -5.7 | 9e-07 | 28/40 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.633×** | -5.2 | 1e-05 | 27/40 (AN3 CA, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.442×** | -4.9 | 6e-05 | 22/40 (C-33 A, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.679×** | -4.2 | 0.001 | 23/40 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.514×** | -4.0 | 0.003 | 20/39 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.706×** | -4.0 | 0.003 | 17/40 (LoVo, HCT15, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.740×** | -3.4 | 0.025 | 14/40 (SNU-423, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.741×** | -3.4 | 0.025 | 14/40 (NCI-H2030, J82, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | **0.809×** | -3.4 | 0.025 | 13/41 (A-427, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.744×** | -3.4 | 0.026 | 18/40 (SK-MEL-2, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12927. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 76.7 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -15.7) |
| [[C-33 A (line)]] | alt | 51.8 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0941× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.195× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 82.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -15.6) |
| [[RKO (line)]] | wt | 34.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -9.7) |
| [[SNU-1 (line)]] | wt | 58.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -10.5) |
| [[A-172 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[A-427 (line)]] | wt | 16.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.200× (z -9.0) |
| [[AN3 CA (line)]] | alt | 35.7 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0927× (z -9.2) |
| [[C32 (line)]] | wt | 23.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.272× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.6) |
| [[Hs 766T (line)]] | wt | 33.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.387× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.304× (z -12.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 53.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 24.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -10.5) |
| [[SNU-423 (line)]] | alt | 34.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.262× (z -9.7) |
| [[SW 1271 (line)]] | alt | 71.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0974× (z -8.7) |
| [[SW480 (line)]] | alt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -11.3) |
| [[A498 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.00 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.03 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12927), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIPK2A]] | +0.63 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ACAD11]] | +0.59 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[MIX23]] | +0.58 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[HDHD5]] | +0.57 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[TUBGCP5]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[PRELID2]] | +0.54 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[AK4]] | +0.54 | +0.37 / +0.48 | both halves | 9e-05 |  |
| [[NAT10]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[AASDH]] | +0.53 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[CRYBG3]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SMAD9]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[TMA16]] | +0.52 | +0.49 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMC1]] | -0.50 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[GDI1]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[PHF1]] | -0.49 | -0.51 / -0.37 | both halves | 9e-05 |  |
| [[SMURF1]] | -0.48 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[CHP1]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[CACFD1]] | -0.45 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[ADAMTSL5]] | -0.45 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[GALNS]] | -0.45 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[ATP6V0C]] | -0.44 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[A1BG-AS1]] | -0.44 | -0.46 / -0.24 | both halves | 5e-04 |  |
| [[ZBTB46]] | -0.43 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[PITPNM1]] | -0.42 | -0.38 / -0.44 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD9]] | B | SMAD9 activity raises FAM216A's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 2.06× lower at baseline in the lines without SMAD9 | 0.063 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[PLEKHA2]] | C | PLEKHA2 activity lowers FAM216A's level | lines that do not express PLEKHA2 (4) vs lines expressing it (45) | 2.95× higher at baseline in the lines without PLEKHA2 | 0.093 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: LSMEM2, ENSG00000285868; maybe low, not absent |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSR1]] | B | FAM216A activity raises TSR1's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 2.06× lower at baseline in the lines without FAM216A | 0.004 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[TFB1M]] | B | FAM216A activity raises TFB1M's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 2.29× lower at baseline in the lines without FAM216A | 0.020 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[ZNF25]] | B | FAM216A activity raises ZNF25's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 2.02× lower at baseline in the lines without FAM216A | 0.023 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[ANKRD16]] | B | FAM216A activity raises ANKRD16's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without FAM216A | 0.036 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[TFB1M]] | B | FAM216A activity strengthens TFB1M's drug response | lines that do not express FAM216A (7) vs lines expressing it (40) | the lines without FAM216A respond 0.66× as strongly (z diff +2.14); strongest at Dinaciclib 0.05 µM: 1.08x vs 0.35x (z diff +7.1) | 0.045 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TMEM45A]] | B | FAM216A activity raises TMEM45A's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 4.08× lower at baseline in the lines without FAM216A | 0.051 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[PAICS]] | B | FAM216A activity raises PAICS's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without FAM216A | 0.055 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[INTS13]] | B | FAM216A activity raises INTS13's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without FAM216A | 0.056 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[AGPAT5]] | B | FAM216A activity raises AGPAT5's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without FAM216A | 0.069 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM | B | FAM216A activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (protects the cells) | lines that do not express FAM216A (7) vs lines expressing it (41) | the lines without FAM216A: 0.78× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[USP28]] | B | FAM216A activity raises USP28's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 1.46× lower at baseline in the lines without FAM216A | 0.090 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| cells under [[Afatinib (drug)]] 0.5 µM | B | FAM216A activity raises the cells' numbers under Afatinib 0.5 µM (protects the cells) | lines that do not express FAM216A (7) vs lines expressing it (41) | the lines without FAM216A: 0.83× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.539). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.0, 19.3); signed map (-41.7, 28.1). **Vector** length 85.7, 21.9% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.0 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +3.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -7.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.4 | -2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | -3.0 | +5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -3.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.9 | -2.5 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 216 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:110,468,415-110,490,385 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSU79274; previously C12orf24 |
| Matched by | ensembl_id |

UniProt [Q8WUB2](https://www.uniprot.org/uniprotkb/Q8WUB2) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:30180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30180) · Entrez [29902](https://www.ncbi.nlm.nih.gov/gene/29902) · UniProt [Q8WUB2](https://www.uniprot.org/uniprotkb/Q8WUB2) · Ensembl [ENSG00000204856](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204856)

## Data

Gene col 12927: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12927); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12927, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12927]; `tensor/DDL_lfc|DDL_z.npy` [12927]; `embed/gene_vectors.npy` [12927]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12927 or target_col == 12927). Every well: [[FAM216A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM216A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
