---
symbol: "CYP3A5"
type: "gene"
col: 2734
ensembl_id: "ENSG00000106258"
name: "cytochrome P450 family 3 subfamily A member 5"
location: "7q22.1"
module: 73
arm: "+"
pooled_cpm: 61.54
n_lines_expressing: 18
n_dd_up: 23
n_dd_down: 19
n_dd_up_clean: 18
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 91
direction_downstream: 120
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# CYP3A5

*cytochrome P450 family 3 subfamily A member 5* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.07× (z +22.8, q 0e+00, up in 14 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.559× (z -8.3, q 4e-14, down in 14 of 16 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.567× (z -7.1, q 3e-10, down in 7 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIPH]] (+0.74, fdr 7e-06), [[HEPH]] (+0.72, fdr 7e-06), [[EPS8L1]] (+0.71, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 91 arrows point to it, the strongest [[HR]] → it (grade B ⚠); 120 go from it, the strongest it → [[KLF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.07×** | +22.8 | 0e+00 | 14/16 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.57×** | +17.6 | 0e+00 | 14/16 (CFPAC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.32×** | +17.2 | 0e+00 | 12/16 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +9.8 | 2e-20 | 14/16 (A498, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +9.5 | 2e-19 | 13/16 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +8.2 | 2e-14 | 1/17 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +6.9 | 4e-10 | 2/12 (HEC-1-A, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.61×** | +6.6 | 4e-09 | 13/16 (A549, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.46×** | +5.5 | 3e-06 | 1/16 (A498) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.4 | 3e-06 | 12/17 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 5e-05 | 12/16 (LoVo, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +4.6 | 2e-04 | 1/13 (NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.004 | 9/16 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.65×** | +3.8 | 0.005 | 5/16 (LoVo, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.005 | 2/16 (Hs 766T, AsPC-1) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.014 | 4/16 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.015 | 0/16 | inconsistent across doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.74×** | +3.3 | 0.025 | 7/16 (COLO 205, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.025 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2734.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.559×** | -8.3 | 4e-14 | 14/16 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.567×** | -7.1 | 3e-10 | 7/16 (LoVo, KATO III, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.779×** | -4.6 | 8e-04 | 4/16 (LoVo, KATO III, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -4.3 | 0.002 | 2/17 (NCI-H1573, SNU-1) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.739×** | -4.3 | 0.002 | 5/18 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.753×** | -4.1 | 0.005 | 14/16 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.826×** | -3.9 | 0.009 | 12/16 (AsPC-1, COLO 205, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.770×** | -3.7 | 0.013 | 9/16 (HepG2/C3A, COLO 205, …) | two highest doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.537×** | -3.7 | 0.013 | 7/16 (Hs 766T, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.778×** | -3.6 | 0.019 | 6/16 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.719×** | -3.4 | 0.030 | 1/16 (Hs 766T) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.569×** | -3.4 | 0.036 | 6/17 (COLO 205, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.793×** | -3.3 | 0.041 | 2/16 (SNU-1, NCI-H1573) | two highest doses |  |
| [[Riluzole hydrochloride (drug)]] 0.05 µM |  | **0.796×** | -3.3 | 0.044 | 1/16 (NCI-H1573) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.853× | -3.2 | 0.050 | 7/16 (Hs 766T, A498, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.801×** | -3.2 | 0.052 | 9/17 (KATO III, LoVo, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.596×** | -3.1 | 0.061 | 10/16 (AsPC-1, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 38.7 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 30.5× (z +24.3) | — |
| [[LS 180 (line)]] | wt | 240 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0740× (z -21.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 220 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +27.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.265× (z -10.1) |
| [[COLO 205 (line)]] | alt | 828 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0898× (z -19.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 883 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0602× (z -23.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.226× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 88.2 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +27.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.217× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 29.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +14.7) | — |
| [[KATO III (line)]] | alt | 270 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -18.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.0) |
| [[A549 (line)]] | wt | 29.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +21.0) | — |
| [[HepG2_C3A (line)]] | wt | 36.8 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +18.7) | [[Belinostat (drug)]] 0.5 µM 0.155× (z -9.9) |
| [[SW1417 (line)]] | alt | 51.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.37× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 40.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 41.6 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.36× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.57 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.80 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.00 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.97 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.53 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.67 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.63 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.20 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.05 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.26 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.81 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.58 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.41 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.53 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.45 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.97 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIPH]] | +0.74 | +0.62 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[HEPH]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[EPS8L1]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.69 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[NPSR1]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[NOSTRIN]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS2]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[C1orf116]] | +0.68 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[ABHD11]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[MUC17]] | +0.67 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[EHF]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[CDH17]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*91 arrows, 91 of them with an alert ⚠; grade A 0, B 10, C 81. Shown: the 12 strongest; 79 more arrows (79 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HR]] | B | HR activity raises CYP3A5's level | lines that do not express HR (23) vs lines expressing it (27) | 2.66× lower at baseline in the lines without HR | 0.032 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[JUP]] | B | JUP activity raises CYP3A5's level | lines that do not express JUP (16) vs lines expressing it (34) | 3.08× lower at baseline in the lines without JUP | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[PCDH1]] | B | PCDH1 activity raises CYP3A5's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.70× lower at baseline in the lines without PCDH1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[LMO7]] | B | LMO7 activity raises CYP3A5's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.52× lower at baseline in the lines without LMO7 | 0.060 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[LPAR5]] | B | LPAR5 activity raises CYP3A5's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.68× lower at baseline in the lines without LPAR5 | 0.061 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[TNFRSF14-AS1]] | B | TNFRSF14-AS1 activity raises CYP3A5's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.93× lower at baseline in the lines without TNFRSF14-AS1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[PPARG]] | B | PPARG activity raises CYP3A5's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without PPARG | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[KLF5]] | B | KLF5 activity raises CYP3A5's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.45× lower at baseline in the lines without KLF5 | 0.068 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises CYP3A5's level | compounds that target MAP2K1: 3 of 4 lower it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[RASEF]] | B | RASEF activity raises CYP3A5's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.42× lower at baseline in the lines without RASEF | 0.096 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[GCNT3]] | C | GCNT3 activity raises CYP3A5's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 11.52× lower at baseline in the lines without GCNT3 | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises CYP3A5's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 12.47× lower at baseline in the lines without MUC13 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |

### Downstream of this gene

*120 arrows, 120 of them with an alert ⚠; grade A 0, B 45, C 75. Shown: the 12 strongest; 108 more arrows (108 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF3]] | B | CYP3A5 activity raises KLF3's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.70× lower at baseline in the lines without CYP3A5 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[KLF5]] | B | CYP3A5 activity raises KLF5's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 4.44× lower at baseline in the lines without CYP3A5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[EPHA2]] | B | CYP3A5 activity raises EPHA2's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 3.48× lower at baseline in the lines without CYP3A5 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[LMO7]] | B | CYP3A5 activity raises LMO7's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 3.74× lower at baseline in the lines without CYP3A5 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[CD55]] | B | CYP3A5 activity raises CD55's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 3.04× lower at baseline in the lines without CYP3A5 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[EPS8L1]] | B | CYP3A5 activity raises EPS8L1's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 3.30× lower at baseline in the lines without CYP3A5 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[FOXO1]] | B | CYP3A5 activity raises FOXO1's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.69× lower at baseline in the lines without CYP3A5 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[BAIAP2L2]] | B | CYP3A5 activity raises BAIAP2L2's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 3.12× lower at baseline in the lines without CYP3A5 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[BAIAP2L1]] | B | CYP3A5 activity raises BAIAP2L1's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.45× lower at baseline in the lines without CYP3A5 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[ARHGAP27]] | B | CYP3A5 activity raises ARHGAP27's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.43× lower at baseline in the lines without CYP3A5 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[SDCBP2]] | B | CYP3A5 activity raises SDCBP2's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 3.37× lower at baseline in the lines without CYP3A5 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[RDH13]] | B | CYP3A5 activity raises RDH13's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.00× lower at baseline in the lines without CYP3A5 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.8, 51.9); signed map (64.5, 8.0). **Vector** length 78.2, 29.6% of its response variance represented; |z| ≥ 3 in 516 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +22.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +17.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +3.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.8 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -8.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -7.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.7 | -4.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.7 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 3 subfamily A member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,648,194-99,679,996 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PCN3, P450PCN3, CP35 |
| Gene groups (HGNC) | Cytochrome P450 family 3 |
| Reactome | 5 pathways, smallest: Aflatoxin activation and detoxification; Xenobiotics; Cytochrome P450 - arranged by substrate type |
| Matched by | ensembl_id |

**Function**, from UniProt [P20815](https://www.uniprot.org/uniprotkb/P20815) (Cytochrome P450 3A5):

> A cytochrome P450 monooxygenase involved in the metabolism of steroid hormones and vitamins. Mechanistically, uses molecular oxygen inserting one oxygen atom into a substrate, and reducing the second into a water molecule, with two electrons provided by NADPH via cytochrome P450 reductase (NADPH--hemoprotein reductase). Catalyzes the hydroxylation of carbon-hydrogen bonds. Exhibits high catalytic activity for the formation of catechol estrogens from 17beta-estradiol (E2) and estrone (E1), …

**Summary**, from NCBI Gene [1577](https://www.ncbi.nlm.nih.gov/gene/1577):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. The encoded protein metabolizes drugs as well as the steroid hormones testosterone and progesterone. This gene is part of a cluster of cytochrome P450 genes on chromosome 7q21.1. Two pseudogenes of this gene have been identified within this cluster on chromosome …

**Accessions** — [HGNC:2638](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2638) · Entrez [1577](https://www.ncbi.nlm.nih.gov/gene/1577) · UniProt [P20815](https://www.uniprot.org/uniprotkb/P20815) · Ensembl [ENSG00000106258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106258)

## Data

Gene col 2734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2734); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2734]; `tensor/DDL_lfc|DDL_z.npy` [2734]; `embed/gene_vectors.npy` [2734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2734 or target_col == 2734). Every well: [[CYP3A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP3A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
