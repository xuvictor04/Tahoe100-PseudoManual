---
symbol: "CDC42BPB"
type: "gene"
col: 12666
ensembl_id: "ENSG00000198752"
name: "CDC42 binding protein kinase beta"
location: "14q32.32"
module: 2
arm: "+"
pooled_cpm: 154.91
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CDC42BPB

*CDC42 binding protein kinase beta* — 14q32.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.31× (z +6.5, q 4e-08, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.543× (z -20.8, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPRIP]] (+0.70, fdr 7e-06), [[RHOA]] (+0.65, fdr 7e-06), [[ZDHHC3]] (+0.64, fdr 9e-06); moves opposite to [[LIPT1]] (-0.60, fdr 9e-06), [[LINC00944]] (-0.60, fdr 5e-05), [[STAP2]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAOB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12666.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +6.5 | 4e-08 | 28/47 (NCI-H460, A-172, …) | two highest doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.29×** | +5.8 | 2e-06 | 29/47 (NCI-H460, HOP62, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +5.2 | 3e-05 | 22/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +5.1 | 4e-05 | 31/48 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.19× | +4.3 | 0.002 | 21/48 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.006 | 22/49 (SK-MEL-2, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.6 | 0.024 | 17/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12666.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.543×** | -20.8 | 0e+00 | 40/48 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.616×** | -11.2 | 9e-27 | 41/47 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.634×** | -10.5 | 1e-23 | 41/48 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.736×** | -10.4 | 2e-23 | 36/49 (AsPC-1, A549, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.623×** | -9.6 | 9e-20 | 38/48 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.778×** | -8.6 | 1e-15 | 34/48 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.821×** | -4.7 | 2e-04 | 26/48 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.826×** | -4.6 | 3e-04 | 25/48 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.822×** | -4.4 | 7e-04 | 24/45 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.807×** | -4.4 | 7e-04 | 26/48 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -3.9 | 0.005 | 18/49 (HOP62, BT-474, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.847× | -3.8 | 0.006 | 20/48 (SW480, J82, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.867× | -3.5 | 0.024 | 12/48 (BT-474, NCI-H2347, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.767×** | -3.3 | 0.033 | 17/47 (HCT15, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.872× | -3.2 | 0.055 | 18/50 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.878× | -3.2 | 0.056 | 8/48 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.788×** | -3.1 | 0.056 | 15/47 (AsPC-1, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.915× | -3.1 | 0.070 | 13/48 (J82, HEC-1-A, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.796×** | -3.0 | 0.077 | 13/48 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.863× | -3.0 | 0.078 | 13/48 (SW 1271, PANC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12666. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 303 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -19.9) |
| [[A-172 (line)]] | wt | 114 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -28.7) |
| [[J82 (line)]] | alt | 145 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -20.6) |
| [[NCI-H1573 (line)]] | alt | 206 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -22.5) |
| [[C32 (line)]] | wt | 132 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -16.6) |
| [[CFPAC-1 (line)]] | alt | 280 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -16.0) |
| [[LoVo (line)]] | wt | 167 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 153 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -22.7) |
| [[NCI-H460 (line)]] | wt | 120 | 2 | 2 | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.16× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.637× (z -10.2) |
| [[A549 (line)]] | wt | 240 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -13.5) |
| [[Hs 766T (line)]] | wt | 202 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -19.1) |
| [[hTERT-HPNE (line)]] | wt | 168 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -17.0) |
| [[NCI-H2347 (line)]] | alt | 193 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -13.7) |
| [[Panc 03.27 (line)]] | alt | 216 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.565× (z -10.9) |
| [[A-427 (line)]] | wt | 133 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.457× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.438× (z -9.4) |
| [[HOP62 (line)]] | alt | 154 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -17.1) |
| [[HT-29 (line)]] | alt | 143 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -10.9) |
| [[LS 180 (line)]] | wt | 234 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -13.9) |
| [[NCI-H2030 (line)]] | alt | 212 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 85.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -11.2) |
| [[SW 900 (line)]] | alt | 143 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.436× (z -10.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.594× (z -10.0) |
| [[SW480 (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -10.7) |
| [[A498 (line)]] | wt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -12.2) |
| [[C-33 A (line)]] | alt | 149 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.489× (z -8.5) ⚠ toxic |
| [[HCT15 (line)]] | alt | 198 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.600× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 228 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -13.3) |
| [[HS-578T (line)]] | alt | 98.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -13.9) |
| [[PANC-1 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.480× (z -11.6) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 97.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.565× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 132 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -16.8) |
| [[SW1417 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.536× (z -8.6) ⚠ toxic |
| [[SW48 (line)]] | wt | 415 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -13.3) |
| [[AN3 CA (line)]] | alt | 121 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 93.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 110 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 122 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 192 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12666), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPRIP]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 | STRING 532 |
| [[RHOA]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 | STRING 561 |
| [[ZDHHC3]] | +0.64 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[KIF1C]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[DIAPH1]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[CAPN1]] | +0.63 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[BCAP31]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[KLF13]] | +0.62 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[CYB5R3]] | +0.62 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CAP1]] | +0.61 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[SETD3]] | +0.61 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[MAPK9]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIPT1]] | -0.60 | -0.63 / -0.57 | both halves | 9e-06 |  |
| [[LINC00944]] | -0.60 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[STAP2]] | -0.58 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ZNF764]] | -0.57 | -0.68 / -0.32 | both halves | 1e-04 |  |
| [[TIFA]] | -0.57 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[SBF2-AS1]] | -0.57 | -0.64 / -0.30 | both halves | 2e-04 |  |
| [[ZNF226]] | -0.56 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[EPC1]] | -0.56 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[N4BP2L1]] | -0.56 | -0.65 / -0.32 | both halves | 2e-04 |  |
| [[HELQ]] | -0.55 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[NNT-AS1]] | -0.55 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[BTN2A3P-1]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAOB]] | B | MAOB activity raises CDC42BPB's level | lines that do not express MAOB (34) vs lines expressing it (16) | 1.34× lower at baseline in the lines without MAOB | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[CROCCP3-1]] | C | CROCCP3-1's natural level strengthens CDC42BPB's drug response | CROCCP3-1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.22; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (14.9, 1.1); signed map (-11.1, 36.4). **Vector** length 124, 39.4% of its response variance represented; |z| ≥ 3 in 1,166 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.4 | +0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.6 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.4 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.0 | +6.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.6 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +1.2 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +5.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.5 | -20.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.8 | -10.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.0 | -9.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.8 | -8.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.2 | -11.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | CDC42 binding protein kinase beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.32 — chr14:102,932,380-103,057,549 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRCKB, KIAA1124 |
| Gene groups (HGNC) | CDC42 binding protein kinase family |
| Reactome | 6 pathways, smallest: RHOJ GTPase cycle; RHOQ GTPase cycle; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5S2](https://www.uniprot.org/uniprotkb/Q9Y5S2) (Serine/threonine-protein kinase MRCK beta):

> Serine/threonine-protein kinase which is an important downstream effector of CDC42 and plays a role in the regulation of cytoskeleton reorganization and cell migration. Regulates actin cytoskeletal reorganization via phosphorylation of PPP1R12C and MYL9/MLC2. In concert with MYO18A and LURAP1, is involved in modulating lamellar actomyosin retrograde flow that is crucial to cell protrusion and migration. Phosphorylates PPP1R12A. In concert with FAM89B/LRAP25 mediates the targeting of LIMK1 to …

**Summary**, from NCBI Gene [9578](https://www.ncbi.nlm.nih.gov/gene/9578):

> This gene encodes a member of the serine/threonine protein kinase family. The encoded protein contains a Cdc42/Rac-binding p21 binding domain resembling that of PAK kinase. The kinase domain of this protein is most closely related to that of myotonic dystrophy kinase-related ROK. Studies of the similar gene in rat suggested that this kinase may act as a downstream effector of Cdc42 in cytoskeletal reorganization. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1738](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1738) · Entrez [9578](https://www.ncbi.nlm.nih.gov/gene/9578) · UniProt [Q9Y5S2](https://www.uniprot.org/uniprotkb/Q9Y5S2) · Ensembl [ENSG00000198752](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198752)

## Data

Gene col 12666: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12666); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12666, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12666]; `tensor/DDL_lfc|DDL_z.npy` [12666]; `embed/gene_vectors.npy` [12666]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12666 or target_col == 12666). Every well: [[CDC42BPB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC42BPB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
