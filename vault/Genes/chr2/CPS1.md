---
symbol: "CPS1"
type: "gene"
col: 331
ensembl_id: "ENSG00000021826"
name: "carbamoyl-phosphate synthase 1"
location: "2q34"
module: 19
arm: "+"
pooled_cpm: 124.52
n_lines_expressing: 14
n_dd_up: 26
n_dd_down: 14
n_dd_up_clean: 23
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CPS1

*carbamoyl-phosphate synthase 1* — 2q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.01× (z +11.0, q 3e-25, up in 9 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.97× (z +6.8, q 3e-09, up in 11 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.501× (z -9.7, q 1e-19, down in 12 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE1A]] (+0.69, fdr 7e-06), [[GPRIN3]] (+0.65, fdr 7e-06), [[TBXT]] (+0.63, fdr 7e-06, ⚠ TBXT in the vector space only through flagged drug-doses), [[LINC01035]] (+0.63, fdr 1e-05); moves opposite to [[KCNK6]] (-0.45, fdr 2e-04), [[APOBEC3G]] (-0.44, fdr 1e-04), [[NPIPP1]] (-0.43, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 8 go from it, the strongest it → [[PTPRM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 331.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +11.0 | 3e-25 | 9/13 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +9.2 | 1e-17 | 5/9 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.97×** | +6.8 | 3e-09 | 11/12 (A549, NCI-H460, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.84×** | +6.1 | 2e-07 | 3/12 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +5.7 | 1e-06 | 4/10 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 0.5 µM |  | **1.59×** | +4.7 | 3e-04 | 3/12 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 6e-04 | 5/12 (NCI-H460, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.44×** | +4.3 | 0.001 | 8/12 (HEC-1-A, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +4.2 | 0.002 | 8/13 (NCI-H1573, NCI-H2030, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.002 | 7/13 (NCI-H2030, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.005 | 6/12 (NCI-H2030, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.47×** | +3.9 | 0.005 | 3/14 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.007 | 2/13 (NCI-H460, A549) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.48×** | +3.6 | 0.011 | 7/11 (NCI-H460, A549, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.011 | 6/12 (NCI-H460, A549, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.011 | 6/11 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.018 | 7/12 (NCI-H460, A549, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.024 | 4/12 (HEC-1-A, SNU-1, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 331.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.501×** | -9.7 | 1e-19 | 12/12 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.405×** | -9.0 | 8e-17 | 11/12 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.600×** | -5.1 | 7e-05 | 9/12 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.715×** | -4.7 | 3e-04 | 8/13 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.618×** | -4.6 | 5e-04 | 10/12 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.632×** | -4.6 | 5e-04 | 7/12 (NCI-H2030, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.638×** | -4.5 | 6e-04 | 4/11 (SNU-1, SW48, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.647×** | -4.3 | 0.001 | 7/12 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.654×** | -4.2 | 0.001 | 11/12 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.654×** | -4.2 | 0.001 | 5/12 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.677×** | -3.9 | 0.005 | 8/12 (HEC-1-A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Menadione (drug)]] 5 µM |  | **0.719×** | -3.2 | 0.075 | 4/11 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.736×** | -3.0 | 0.094 | 0/12 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.736×** | -3.0 | 0.094 | 10/12 (NCI-H460, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 331. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1,128 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 378 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0776× (z -18.8) |
| [[NCI-H2030 (line)]] | alt | 1,476 | 1 (1 ⚠) | 4 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +8.7) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 36.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -11.4) |
| [[LS 180 (line)]] | wt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 38.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.1) |
| [[A-172 (line)]] | wt | 23.9 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.74 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 68.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.67 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.91 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.9 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.22 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 24.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 21.3 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.28 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 18.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.57 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 29.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.2 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.00 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 30.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 28.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.3 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 9.54 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.65 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 331), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE1A]] | +0.69 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[GPRIN3]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[TBXT]] ⚠ | +0.63 | +0.61 / +0.64 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[LINC01035]] | +0.63 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[MAPK4]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[SLC15A5]] | +0.60 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[LINC03000]] | +0.59 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[PDE4D]] | +0.59 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[ADGRD1]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SLITRK5]] | +0.58 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[LIN7A]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SNCA]] | +0.58 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[PBX1]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNK6]] | -0.45 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[APOBEC3G]] | -0.44 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[NPIPP1]] | -0.43 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[FAM98C]] | -0.42 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[ADRA2C]] | -0.42 | -0.30 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CPS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[KCNMB2]] | B | KCNMB2 activity raises CPS1's level | lines that do not express KCNMB2 (18) vs lines expressing it (32) | 2.38× lower at baseline in the lines without KCNMB2 | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC01980, LINC02398, LINC02306; maybe low, not absent |
| [[RSPO3]] | C | RSPO3 activity raises CPS1's level | lines that do not express RSPO3 (39) vs lines expressing it (11) | 5.80× lower at baseline in the lines without RSPO3 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2; co-absent with the target |
| [[PDE1A]] | C | PDE1A activity raises CPS1's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 4.24× lower at baseline in the lines without PDE1A | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[MAPK4]] | C | MAPK4 activity raises CPS1's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 3.56× lower at baseline in the lines without MAPK4 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRM]] | B | CPS1 activity raises PTPRM's level | lines that do not express CPS1 (36) vs lines expressing it (14) | 3.15× lower at baseline in the lines without CPS1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, ENSG00000241168, GLP2R |
| [[TGFB2]] | B | CPS1 activity raises TGFB2's level | lines that do not express CPS1 (36) vs lines expressing it (14) | 1.71× lower at baseline in the lines without CPS1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, ENSG00000241168, GLP2R |
| [[HORMAD1]] | B | CPS1 activity raises HORMAD1's level | lines that do not express CPS1 (36) vs lines expressing it (14) | 2.18× lower at baseline in the lines without CPS1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, ENSG00000241168, GLP2R |
| [[RSPO3]] | C | CPS1 activity raises RSPO3's level | lines that do not express CPS1 (36) vs lines expressing it (14) | 3.87× lower at baseline in the lines without CPS1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, ENSG00000241168, GLP2R; co-absent with the target |
| [[MAPK4]] | C | CPS1 activity raises MAPK4's level | lines that do not express CPS1 (36) vs lines expressing it (14) | 1.86× lower at baseline in the lines without CPS1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, ENSG00000241168, GLP2R; co-absent with the target |
| [[CDH19]] | C | CPS1 activity raises CDH19's level | lines that do not express CPS1 (36) vs lines expressing it (14) | 3.55× lower at baseline in the lines without CPS1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, ENSG00000241168, GLP2R; co-absent with the target |
| [[CHL1]] | C | CPS1 activity raises CHL1's level | lines that do not express CPS1 (36) vs lines expressing it (14) | 2.99× lower at baseline in the lines without CPS1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, ENSG00000241168, GLP2R; co-absent with the target |
| [[PDE1A]] | C | CPS1 activity raises PDE1A's level | lines that do not express CPS1 (36) vs lines expressing it (14) | 2.14× lower at baseline in the lines without CPS1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, ENSG00000241168, GLP2R; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.5, 37.7); signed map (44.7, 43.9). **Vector** length 49.6, 16.5% of its response variance represented; |z| ≥ 3 in 419 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +11.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +9.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.5 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.1 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +4.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.1 | +6.8 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | carbamoyl-phosphate synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q34 — chr2:210,477,682-210,679,107 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GATD6 |
| Gene groups (HGNC) | Glutamine amidotransferase class 1 domain containing; ATP-grasp fold containing; Carbamoyl-phosphate synthetases |
| Reactome | 4 pathways, smallest: Diseases of the urea cycle; Urea cycle; Diseases of metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P31327](https://www.uniprot.org/uniprotkb/P31327) (Carbamoyl-phosphate synthase):

> Involved in the urea cycle of ureotelic animals where the enzyme plays an important role in removing excess ammonia from the cell.

**Summary**, from NCBI Gene [1373](https://www.ncbi.nlm.nih.gov/gene/1373):

> The mitochondrial enzyme encoded by this gene catalyzes synthesis of carbamoyl phosphate from ammonia and bicarbonate. This reaction is the first committed step of the urea cycle, which is important in the removal of excess urea from cells. The encoded protein may also represent a core mitochondrial nucleoid protein. Three transcript variants encoding different isoforms have been found for this gene. The shortest isoform may not be localized to the mitochondrion. Mutations in this gene have …

**Accessions** — [HGNC:2323](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2323) · Entrez [1373](https://www.ncbi.nlm.nih.gov/gene/1373) · UniProt [P31327](https://www.uniprot.org/uniprotkb/P31327) · Ensembl [ENSG00000021826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000021826)

## Data

Gene col 331: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 331); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 331, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 331]; `tensor/DDL_lfc|DDL_z.npy` [331]; `embed/gene_vectors.npy` [331]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 331 or target_col == 331). Every well: [[CPS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
