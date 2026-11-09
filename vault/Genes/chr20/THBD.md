---
symbol: "THBD"
type: "gene"
col: 10953
ensembl_id: "ENSG00000178726"
name: "thrombomodulin"
location: "20p11.21"
module: 34
arm: "+"
pooled_cpm: 15.05
n_lines_expressing: 22
n_dd_up: 20
n_dd_down: 27
n_dd_up_clean: 14
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 10
direction_downstream: 8
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# THBD

*thrombomodulin* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.87× (z +7.5, q 4e-11, up in 3 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 2.61× (z +6.7, q 4e-09, up in 10 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.455× (z -8.2, q 1e-13, down in 17 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABTB3]] (+0.69, fdr 7e-06), [[S100A16]] (+0.64, fdr 8e-06), [[CAPRIN2]] (+0.60, fdr 1e-05); moves opposite to [[REL]] (-0.58, fdr 1e-05), [[TNFAIP2]] (-0.57, fdr 2e-05), [[NR0B1]] (-0.56, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CREG2]] → it (grade B ⚠); 8 go from it, the strongest it → [[IL18R1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10953.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +7.5 | 4e-11 | 3/13 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +6.9 | 1e-09 | 6/17 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.61×** | +6.7 | 4e-09 | 10/17 (A498, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.39×** | +6.4 | 2e-08 | 13/19 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **5.48×** | +5.4 | 8e-06 | 12/16 (AsPC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.84×** | +4.5 | 6e-04 | 12/18 (A498, AsPC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.83×** | +4.5 | 6e-04 | 11/18 (NCI-H460, Panc 03.27, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.78×** | +4.1 | 0.003 | 14/18 (Panc 03.27, NCI-H1792, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.003 | 8/17 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.70×** | +3.9 | 0.005 | 9/18 (NCI-H1792, SNU-423, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.08×** | +3.9 | 0.006 | 9/17 (A498, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +3.6 | 0.014 | 8/18 (AsPC-1, NCI-H1573, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.62×** | +3.5 | 0.017 | 11/18 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.60×** | +3.5 | 0.020 | 3/17 (RPMI-7951, J82, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.94×** | +3.5 | 0.020 | 6/17 (NCI-H1792, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.048 | 10/18 (RPMI-7951, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.80×** | +3.1 | 0.061 | 4/17 (PANC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +3.0 | 0.086 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.088 | 9/19 (J82, RPMI-7951, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, none with an alert; shown: the 15 strongest. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10953.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.455×** | -8.2 | 1e-13 | 17/18 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.372×** | -7.1 | 5e-10 | 16/18 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.405×** | -6.2 | 1e-07 | 16/19 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.478×** | -5.5 | 6e-06 | 14/19 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.470×** | -5.4 | 7e-06 | 15/19 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.504×** | -5.1 | 4e-05 | 15/18 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.528×** | -4.7 | 2e-04 | 10/17 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.528×** | -4.7 | 2e-04 | 15/19 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.582×** | -4.7 | 2e-04 | 14/18 (NCI-H460, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.547×** | -4.5 | 4e-04 | 13/17 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.653×** | -4.5 | 4e-04 | 15/18 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.549×** | -4.5 | 4e-04 | 16/19 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.547×** | -4.3 | 7e-04 | 13/17 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.565×** | -4.2 | 9e-04 | 15/19 (SNU-1, SW 900, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.597×** | -4.0 | 0.003 | 12/20 (NCI-H460, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10953. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.2 | 0 | 21 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0578× (z -22.3) |
| [[CFPAC-1 (line)]] | alt | 69.2 | 0 | 12 | — | [[Selinexor (drug)]] 5 µM 0.158× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 125 | 5 (1 ⚠) | 3 | [[Ixazomib citrate (drug)]] 5 µM 6.00× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 72.4 | 1 (1 ⚠) | 7 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 7.64× (z +10.8) ⚠ unreliable plate only | [[Adagrasib (drug)]] 0.05 µM 0.498× (z -13.2) ⚠ position not correctable · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0922× (z -12.6) |
| [[A498 (line)]] | wt | 18.9 | 3 | 3 | [[Bortezomib (drug)]] 0.05 µM 18.0× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -12.2) |
| [[Hs 766T (line)]] | wt | 155 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -21.7) |
| [[SNU-1 (line)]] | wt | 91.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0537× (z -24.3) |
| [[J82 (line)]] | alt | 6.29 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0641× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 31.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -13.3) |
| [[SW 900 (line)]] | alt | 30.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -13.4) |
| [[A549 (line)]] | wt | 8.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0269× (z -17.7) |
| [[HEC-1-A (line)]] | alt | 5.04 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0852× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 8.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0997× (z -9.1) |
| [[PANC-1 (line)]] | alt | 4.94 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0897× (z -12.9) |
| [[A-172 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.801 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.907 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.956 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.955 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.810 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.850 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.921 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.894 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10953), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABTB3]] | +0.69 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[S100A16]] | +0.64 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[CAPRIN2]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[ST3GAL1]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CLMP]] | +0.57 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ENTPD7]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[FXYD5]] | +0.56 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[STX1A]] | +0.56 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[FLNB-AS1]] | +0.56 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[PLEKHG5]] | +0.55 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[MMP1]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_COAGULATION |
| [[LINC00941]] | +0.55 | +0.60 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REL]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[TNFAIP2]] | -0.57 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[NR0B1]] | -0.56 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[TSPAN15]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[RARRES1]] | -0.52 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[STAT5A]] | -0.52 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[ELF3-AS1]] | -0.52 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[MYOF]] | -0.51 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ZNF608]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SLC39A1]] | -0.50 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[AJUBA]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[APOLD1]] | -0.49 | -0.53 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREG2]] | B | CREG2 activity raises THBD's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 2.16× lower at baseline in the lines without CREG2 | 0.025 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[ABTB3]] | B | ABTB3 activity raises THBD's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 1.56× lower at baseline in the lines without ABTB3 | 0.068 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[IL18R1]] | B | IL18R1 activity raises THBD's level | lines that do not express IL18R1 (15) vs lines expressing it (35) | 3.14× lower at baseline in the lines without IL18R1 | 0.069 | ⚠ within organs, on part of the lines; also absent: JCAD |
| [[BCAR3]] | B | BCAR3 activity raises THBD's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.70× lower at baseline in the lines without BCAR3 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[TSPAN15]] | B | TSPAN15 activity raises THBD's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 2.26× lower at baseline in the lines without TSPAN15 | 0.076 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[SERPIND1]] | B | SERPIND1 activity raises THBD's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 1.37× lower at baseline in the lines without SERPIND1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises THBD's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[LINC02725]] | C | LINC02725 activity raises THBD's level | lines that do not express LINC02725 (35) vs lines expressing it (15) | 3.76× lower at baseline in the lines without LINC02725 | 0.035 | ⚠ within organs, on part of the lines; also absent: DHRS9, ENSG00000203434, LINC01425; co-absent with the target |
| [[DHRS9]] | C | DHRS9 activity raises THBD's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 4.83× lower at baseline in the lines without DHRS9 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610; co-absent with the target |
| [[FOXL1]] | C | FOXL1 activity raises THBD's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 2.23× lower at baseline in the lines without FOXL1 | 0.090 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL18R1]] | B | THBD activity raises IL18R1's level | lines that do not express THBD (28) vs lines expressing it (22) | 2.57× lower at baseline in the lines without THBD | 0.005 | ⚠ within organs, on part of the lines; also absent: EFEMP1, KRT7, LINC02742 |
| [[TSPAN15]] | B | THBD activity raises TSPAN15's level | lines that do not express THBD (28) vs lines expressing it (22) | 1.95× lower at baseline in the lines without THBD | 0.012 | ⚠ within organs, on part of the lines; also absent: EFEMP1, KRT7, LINC02742 |
| [[CDCP1]] | B | THBD activity raises CDCP1's level | lines that do not express THBD (28) vs lines expressing it (22) | 3.00× lower at baseline in the lines without THBD | 0.015 | ⚠ within organs, on part of the lines; also absent: EFEMP1, KRT7, LINC02742 |
| [[CREG2]] | B | THBD activity raises CREG2's level | lines that do not express THBD (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without THBD | 0.024 | ⚠ within organs, on part of the lines; also absent: EFEMP1, KRT7, LINC02742 |
| [[CPEB2]] | B | THBD activity raises CPEB2's level | lines that do not express THBD (28) vs lines expressing it (22) | 1.61× lower at baseline in the lines without THBD | 0.061 | ⚠ within organs, on part of the lines; also absent: EFEMP1, KRT7, LINC02742 |
| [[MYOF]] | B | THBD activity raises MYOF's level | lines that do not express THBD (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without THBD | 0.062 | ⚠ within organs, on part of the lines; also absent: EFEMP1, KRT7, LINC02742 |
| [[ST3GAL1]] | B | THBD activity raises ST3GAL1's level | lines that do not express THBD (28) vs lines expressing it (22) | 1.61× lower at baseline in the lines without THBD | 0.082 | ⚠ within organs, on part of the lines; also absent: EFEMP1, KRT7, LINC02742 |
| [[TNFAIP2]] | C | THBD activity raises TNFAIP2's level | lines that do not express THBD (28) vs lines expressing it (22) | 3.85× lower at baseline in the lines without THBD | 0.021 | ⚠ within organs, on part of the lines; also absent: EFEMP1, KRT7, LINC02742; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.6, 3.4); signed map (2.7, 46.7). **Vector** length 81.1, 24.0% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.0 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +4.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +3.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.8 | -5.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -3.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -6.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.9 | -4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | thrombomodulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:23,045,633-23,049,672 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD141, THRM, BDCA-3 |
| Gene groups (HGNC) | CD molecules; C-type lectin domain containing |
| Hallmark sets | ANGIOGENESIS, COAGULATION |
| Reactome | 4 pathways, smallest: Regulation of clotting cascade; Coagulation pathway; Cell surface interactions at the vascular wall |
| Matched by | ensembl_id |

**Function**, from UniProt [P07204](https://www.uniprot.org/uniprotkb/P07204) (Thrombomodulin):

> Endothelial cell receptor that plays a critical role in regulating several physiological processes including hemostasis, coagulation, fibrinolysis, inflammation, and angiogenesis. Acts as a cofactor for thrombin activation of protein C/PROC on the surface of vascular endothelial cells leading to initiation of the activated protein C anticoagulant pathway. Also accelerates the activation of the plasma carboxypeptidase B2/CPB2, which catalyzes removal of C-terminal basic amino acids from its …

**Summary**, from NCBI Gene [7056](https://www.ncbi.nlm.nih.gov/gene/7056):

> The protein encoded by this intronless gene is an endothelial-specific type I membrane receptor that binds thrombin. This binding results in the activation of protein C, which degrades clotting factors Va and VIIIa and reduces the amount of thrombin generated. Mutations in this gene are a cause of thromboembolic disease, also known as inherited thrombophilia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11784) · Entrez [7056](https://www.ncbi.nlm.nih.gov/gene/7056) · UniProt [P07204](https://www.uniprot.org/uniprotkb/P07204) · Ensembl [ENSG00000178726](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178726)

## Data

Gene col 10953: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10953); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10953, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10953]; `tensor/DDL_lfc|DDL_z.npy` [10953]; `embed/gene_vectors.npy` [10953]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10953 or target_col == 10953). Every well: [[THBD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THBD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
