---
symbol: "SECTM1"
type: "gene"
col: 6551
ensembl_id: "ENSG00000141574"
name: "secreted and transmembrane 1"
location: "17q25.3"
module: 139
arm: "+"
pooled_cpm: 3.9
n_lines_expressing: 40
n_dd_up: 27
n_dd_down: 24
n_dd_up_clean: 22
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 10
direction_downstream: 3
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# SECTM1

*secreted and transmembrane 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.29× (z +9.0, q 9e-17, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Binimetinib (drug)]] 5 µM: 2.07× (z +5.8, q 1e-06, up in 20 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.462× (z -8.6, q 4e-15, down in 21 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB9]] (+0.69, fdr 1e-05), [[RNF213]] (+0.68, fdr 1e-05), [[TRANK1]] (+0.67, fdr 1e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LCN2]] → it (grade B ⚠); 3 go from it, the strongest it → [[HLA-C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6551.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.29×** | +9.0 | 9e-17 | 1/4 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +7.9 | 1e-12 | 7/18 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **2.07×** | +5.8 | 1e-06 | 20/35 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **2.14×** | +5.8 | 1e-06 | 21/32 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.89×** | +5.6 | 2e-06 | 16/34 (KATO III, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +5.2 | 1e-05 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.2 | 1e-05 | 13/30 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.77×** | +5.1 | 2e-05 | 16/34 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.7 | 2e-04 | 10/35 (NCI-H460, KATO III, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.50×** | +4.5 | 5e-04 | 13/35 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.70×** | +4.2 | 0.001 | 13/34 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.46×** | +4.2 | 0.002 | 13/35 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.68×** | +4.1 | 0.002 | 13/35 (KATO III, AsPC-1, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.65×** | +4.0 | 0.003 | 12/33 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.70×** | +3.9 | 0.003 | 11/34 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.005 | 13/35 (KATO III, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **2.46×** | +3.7 | 0.006 | 8/24 (CFPAC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.7 | 0.006 | 10/29 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6551.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.462×** | -8.6 | 4e-15 | 21/29 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.357×** | -8.1 | 2e-13 | 21/28 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.521×** | -7.3 | 8e-11 | 18/34 (NCI-H2347, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.400×** | -7.2 | 8e-11 | 22/35 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.410×** | -7.0 | 2e-10 | 21/35 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.580×** | -6.1 | 1e-07 | 22/34 (BT-474, LoVo, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.497×** | -5.5 | 3e-06 | 17/33 (LoVo, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.509×** | -5.3 | 7e-06 | 20/35 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.625×** | -5.2 | 1e-05 | 18/35 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.528×** | -5.0 | 3e-05 | 16/35 (KATO III, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.527×** | -4.8 | 1e-04 | 18/33 (Panc 03.27, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.568×** | -4.4 | 4e-04 | 18/35 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.569×** | -4.4 | 4e-04 | 17/35 (A-172, RPMI-7951, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.580×** | -4.1 | 0.002 | 16/33 (LOX-IMVI, A-172, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.611×** | -3.9 | 0.004 | 16/35 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.613×** | -3.8 | 0.004 | 15/32 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.639×** | -3.5 | 0.013 | 12/35 (A-172, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6551. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 12.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0988× (z -12.6) |
| [[LoVo (line)]] | wt | 8.66 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 4.38 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0413× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -9.6) |
| [[A-172 (line)]] | wt | 6.70 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0301× (z -12.4) |
| [[COLO 205 (line)]] | alt | 10.00 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0443× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 6.93 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0558× (z -10.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -11.1) |
| [[KATO III (line)]] | alt | 10.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.109× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 8.05 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.187× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 6.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -9.1) |
| [[PANC-1 (line)]] | alt | 2.17 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0922× (z -8.7) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 1.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0392× (z -11.1) |
| [[A-427 (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.222 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.232 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6551), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB9]] | +0.69 | +0.55 / +0.74 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[RNF213]] | +0.68 | +0.56 / +0.71 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TRANK1]] | +0.67 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[UBE2L6]] | +0.67 | +0.49 / +0.75 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[GBP1]] | +0.66 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[PSMB8]] | +0.66 | +0.61 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TAP1]] | +0.65 | +0.53 / +0.71 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TAP2]] | +0.65 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[MUC1]] | +0.65 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[IFI35]] | +0.65 | +0.50 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TRIM22]] | +0.65 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[PDZK1IP1]] | +0.65 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LCN2]] | B | LCN2 activity raises SECTM1's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 1.99× lower at baseline in the lines without LCN2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[TOP2A]] | B | TOP2A activity lowers SECTM1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLAAT4]] | B | PLAAT4 activity raises SECTM1's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 1.59× lower at baseline in the lines without PLAAT4 | 0.047 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[MUC4]] | B | MUC4 activity raises SECTM1's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 1.88× lower at baseline in the lines without MUC4 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[STEAP4]] | B | STEAP4 activity raises SECTM1's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 1.90× lower at baseline in the lines without STEAP4 | 0.060 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[GBP1]] | B | GBP1 activity raises SECTM1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.73× lower at baseline in the lines without GBP1 | 0.062 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[IFI44]] | B | IFI44 activity raises SECTM1's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without IFI44 | 0.086 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[GBP4]] | B | GBP4 activity raises SECTM1's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without GBP4 | 0.087 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[OAS2]] | B | OAS2 activity raises SECTM1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without OAS2 | 0.091 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SECTM1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-C]] | B | SECTM1 activity raises HLA-C's level | lines that do not express SECTM1 (10) vs lines expressing it (40) | 2.18× lower at baseline in the lines without SECTM1 | 0.034 | ⚠ within organs, on part of the lines |
| [[IFI44]] | B | SECTM1 activity raises IFI44's level | lines that do not express SECTM1 (10) vs lines expressing it (40) | 2.25× lower at baseline in the lines without SECTM1 | 0.037 | ⚠ within organs, on part of the lines |
| [[ZC3HAV1]] | B | SECTM1 activity raises ZC3HAV1's level | lines that do not express SECTM1 (10) vs lines expressing it (40) | 1.62× lower at baseline in the lines without SECTM1 | 0.097 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.4, 52.6); signed map (62.9, 29.9). **Vector** length 76.8, 16.3% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +5.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.3 | +5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +5.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -4.1 | -6.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.2 | -5.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.2 | -5.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | secreted and transmembrane 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,321,024-82,334,074 (-) |
| Ensembl biotype | protein_coding |
| Also known as | K12 |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVN6](https://www.uniprot.org/uniprotkb/Q8WVN6) (Secreted and transmembrane protein 1):

> May be involved in thymocyte signaling.

**Summary**, from NCBI Gene [6398](https://www.ncbi.nlm.nih.gov/gene/6398):

> This gene encodes a transmembrane and secreted protein with characteristics of a type 1a transmembrane protein. It is found in a perinuclear Golgi-like pattern and thought to be involved in hematopoietic and/or immune system processes. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10707](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10707) · Entrez [6398](https://www.ncbi.nlm.nih.gov/gene/6398) · UniProt [Q8WVN6](https://www.uniprot.org/uniprotkb/Q8WVN6) · Ensembl [ENSG00000141574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141574)

## Data

Gene col 6551: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6551); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6551, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6551]; `tensor/DDL_lfc|DDL_z.npy` [6551]; `embed/gene_vectors.npy` [6551]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6551 or target_col == 6551). Every well: [[SECTM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SECTM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
