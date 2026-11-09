---
symbol: "LGALSL"
type: "gene"
col: 4126
ensembl_id: "ENSG00000119862"
name: "galectin like"
location: "2p14"
module: 16
arm: "+"
pooled_cpm: 5.81
n_lines_expressing: 46
n_dd_up: 23
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# LGALSL

*galectin like* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.48× (z +26.8, q 0e+00, up in 35 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.650× (z -6.3, q 2e-07, down in 18 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LGALSL-DT]] (+0.74, fdr 7e-06, ⚠ same locus), [[ZNF620]] (+0.65, fdr 1e-05), [[REPIN1]] (+0.64, fdr 2e-05), [[MARVELD2]] (+0.63, fdr 1e-05); moves opposite to [[PPHLN1]] (-0.59, fdr 2e-05), [[SENP5]] (-0.59, fdr 1e-05), [[SNHG30]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00960]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Vinblastine (sulfate) (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4126.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.48×** | +26.8 | 0e+00 | 35/38 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.75×** | +14.8 | 0e+00 | 34/41 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +12.0 | 5e-31 | 23/36 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.83×** | +9.2 | 6e-18 | 20/42 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +6.3 | 4e-08 | 15/42 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +6.0 | 2e-07 | 13/40 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +5.9 | 2e-07 | 5/8 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +5.9 | 3e-07 | 11/29 (A-427, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +5.5 | 2e-06 | 13/39 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +5.0 | 3e-05 | 9/43 (A498, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +5.0 | 3e-05 | 12/40 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.7 | 1e-04 | 11/29 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.6 | 2e-04 | 8/40 (HCT15, COLO 205, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +4.6 | 2e-04 | 3/13 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.002 | 4/43 (NCI-H1573, LoVo, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.008 | 6/43 (SW480, A-172, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.009 | 3/42 (SW480, AsPC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.010 | 3/41 (NCI-H1792, BT-474, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.010 | 4/43 (AsPC-1, KATO III, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4126.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.650×** | -6.3 | 2e-07 | 18/37 (SW48, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.692×** | -5.6 | 6e-06 | 19/43 (A-172, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -5.5 | 6e-06 | 13/35 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.727×** | -4.9 | 2e-04 | 13/42 (A-427, HT-29, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.560×** | -4.6 | 5e-04 | 7/41 (LS 180, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.796×** | -3.5 | 0.045 | 8/40 (NCI-H2030, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Resveratrol (drug)]] 5 µM |  | 0.851× | -3.5 | 0.045 | 6/43 (HCT15, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | **0.804×** | -3.3 | 0.066 | 14/38 (NCI-H1573, NCI-H23, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.801×** | -3.2 | 0.073 | 3/38 (J82, KATO III, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.816× | -3.1 | 0.12 | 12/43 (NCI-H2030, NCI-H1792, …) | rises with dose | composition shift |
| [[Trimetrexate (drug)]] 5 µM |  | 0.867× | -3.1 | 0.12 | 7/42 (PANC-1, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4126. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.76 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.0912× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 10.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 5.77 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0671× (z -11.1) ⚠ cell-cycle shift, explains ~12% of this change |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 2 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0786× (z -9.4) |
| [[A498 (line)]] | wt | 7.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +11.2) | — |
| [[A549 (line)]] | wt | 4.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 3.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.21× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 3.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +9.5) | — |
| [[J82 (line)]] | alt | 2.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.77× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 5.49 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0986× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 3.28 | 0 | 1 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM 0.0550× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 6.74 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0755× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[NCI-H2030 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.220× (z -8.8) ⚠ cell-cycle shift, explains ~12% of this change |
| [[NCI-H460 (line)]] | wt | 5.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 1.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +9.2) | — |
| [[RKO (line)]] | wt | 12.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -9.6) |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.776 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.726 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4126), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGALSL-DT]] | +0.74 | +0.78 / +0.68 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ZNF620]] | +0.65 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[REPIN1]] | +0.64 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[MARVELD2]] | +0.63 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[SLC35A4]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[PLD6]] | +0.61 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[ZBED9]] | +0.60 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[LIG4]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[METTL18]] | +0.60 | +0.69 / +0.40 | both halves | 5e-05 |  |
| [[TRIM47]] | +0.59 | +0.71 / +0.43 | both halves | 4e-05 |  |
| [[KRTAP5-AS1]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[FAM169A]] | +0.59 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[RHOU]] | +0.59 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPHLN1]] | -0.59 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[SENP5]] | -0.59 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.58 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[PIGF]] | -0.57 | -0.57 / -0.36 | both halves | 9e-05 |  |
| [[SBNO1]] | -0.57 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[DEPDC5]] | -0.56 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[SMARCD2]] | -0.56 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[ADIPOR1]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[SFI1]] | -0.55 | -0.57 / -0.40 | both halves | 4e-05 |  |
| [[POLR2F]] | -0.55 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[ASB16-AS1]] | -0.54 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[NFATC2IP]] | -0.54 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00960]] | B | LINC00960 activity lowers LGALSL's level | lines that do not express LINC00960 (21) vs lines expressing it (29) | 1.45× higher at baseline in the lines without LINC00960 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000282943, ENSG00000272297, ADAMTS3; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Vinblastine (sulfate) (drug)]] 0.05 µM | C | [[ATP11A]], LGALSL, [[LGALSL-DT]] activity raises the cells' numbers under Vinblastine (sulfate) 0.05 µM (protects the cells) | lines that do not express ATP11A, LGALSL, LGALSL-DT (4) vs lines expressing them (44) | the lines without ATP11A, LGALSL, LGALSL-DT: 0.81× the cells of the other lines | 0.088 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent; co-absent genes |
| [[KIAA0408]] | C | LGALSL activity lowers KIAA0408's level | lines that do not express LGALSL (4) vs lines expressing it (46) | 5.20× higher at baseline in the lines without LGALSL | 0.098 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.6, 10.8); signed map (13.6, -19.5). **Vector** length 75.4, 13.7% of its response variance represented; |z| ≥ 3 in 879 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +26.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.7 | +14.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +12.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +5.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +2.6 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.8 | -5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -5.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.4 | -4.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -4.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | galectin like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:64,453,969-64,461,381 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC159, GRP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3ZCW2](https://www.uniprot.org/uniprotkb/Q3ZCW2) (Galectin-related protein):

> Does not bind lactose, and may not bind carbohydrates.

**Summary**, from NCBI Gene [29094](https://www.ncbi.nlm.nih.gov/gene/29094):

> Predicted to enable carbohydrate binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25012](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25012) · Entrez [29094](https://www.ncbi.nlm.nih.gov/gene/29094) · UniProt [Q3ZCW2](https://www.uniprot.org/uniprotkb/Q3ZCW2) · Ensembl [ENSG00000119862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119862)

## Data

Gene col 4126: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4126); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4126, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4126]; `tensor/DDL_lfc|DDL_z.npy` [4126]; `embed/gene_vectors.npy` [4126]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4126 or target_col == 4126). Every well: [[LGALSL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LGALSL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
