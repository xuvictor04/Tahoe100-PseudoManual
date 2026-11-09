---
symbol: "HUS1"
type: "gene"
col: 5849
ensembl_id: "ENSG00000136273"
name: "HUS1 checkpoint clamp component"
location: "7p12.3"
module: 1
arm: "+"
pooled_cpm: 27.35
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# HUS1

*HUS1 checkpoint clamp component* — 7p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.14× (z +20.0, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.597× (z -13.6, q 2e-39, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[N6AMT1]] (+0.70, fdr 1e-05), [[GMFB]] (+0.69, fdr 9e-06), [[GTF2H3]] (+0.65, fdr 7e-06); moves opposite to [[PPP2R5E]] (-0.72, fdr 7e-06), [[CSNK1G2]] (-0.68, fdr 7e-06), [[UBL5]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +20.0 | 0e+00 | 45/47 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +17.0 | 0e+00 | 43/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +13.8 | 8e-41 | 46/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.88×** | +12.1 | 2e-31 | 44/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.57×** | +8.6 | 8e-16 | 30/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +8.6 | 8e-16 | 24/36 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +6.9 | 5e-10 | 31/48 (AsPC-1, NCI-H2030, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +6.7 | 2e-09 | 25/48 (HT-29, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +6.5 | 7e-09 | 29/48 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +5.2 | 1e-05 | 21/48 (LoVo, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.5 | 3e-04 | 16/48 (LS 180, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.2 | 0.001 | 14/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.002 | 18/48 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.002 | 11/47 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.24×** | +4.1 | 0.002 | 17/45 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.013 | 19/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.3 | 0.023 | 9/48 (A-427, KATO III, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.2 | 0.032 | 15/48 (LoVo, A498, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5849.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -13.6 | 2e-39 | 40/47 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.593×** | -9.7 | 1e-19 | 35/48 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.563×** | -5.8 | 1e-06 | 26/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.761×** | -5.3 | 2e-05 | 23/48 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -5.1 | 4e-05 | 27/48 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Bergenin (drug)]] 0.5 µM |  | **0.820×** | -3.8 | 0.012 | 15/48 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.873× | -3.6 | 0.024 | 11/48 (A549, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.831×** | -3.6 | 0.024 | 16/48 (A-172, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.879× | -3.4 | 0.040 | 7/48 (SW 1088, SK-MEL-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.842× | -3.3 | 0.051 | 9/48 (SW 1271, J82, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.790×** | -3.2 | 0.060 | 12/46 (A-172, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.793×** | -3.2 | 0.066 | 13/48 (SW 1088, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.889× | -3.1 | 0.092 | 15/48 (HOP62, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 60.3 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -10.7) |
| [[A498 (line)]] | wt | 27.6 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 30.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +17.5) | — |
| [[AsPC-1 (line)]] | alt | 31.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 15.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +12.8) | — |
| [[KATO III (line)]] | alt | 23.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.1) | — |
| [[NCI-H2030 (line)]] | alt | 28.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 23.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +12.3) | — |
| [[PANC-1 (line)]] | alt | 40.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.0) | — |
| [[SNU-1 (line)]] | wt | 31.6 | 0 | 2 | — | [[Thymol (drug)]] 0.5 µM 0.0659× (z -15.2) |
| [[A-172 (line)]] | wt | 28.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.5) | — |
| [[A-427 (line)]] | wt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.28× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 33.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.128× (z -8.9) |
| [[LoVo (line)]] | wt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 19.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.91× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 18.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.3) | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 21.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.0) | — |
| [[RKO (line)]] | wt | 41.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 32.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -8.8) |
| [[SHP-77 (line)]] | alt | 25.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -10.1) |
| [[SNU-423 (line)]] | alt | 25.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -10.6) |
| [[SW 900 (line)]] | alt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 29.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.7) | — |
| [[SW48 (line)]] | wt | 27.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -10.3) |
| [[A549 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N6AMT1]] | +0.70 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[GMFB]] | +0.69 | +0.57 / +0.75 | both halves | 9e-06 |  |
| [[GTF2H3]] | +0.65 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[PTAR1]] | +0.64 | +0.40 / +0.75 | both halves | 4e-05 |  |
| [[MANBAL]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[DRG2]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SRRD]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[YTHDC2]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[OCRL]] | +0.60 | +0.39 / +0.69 | both halves | 6e-05 |  |
| [[ZMYM1]] | +0.60 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[C12orf29]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ZNF678]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R5E]] | -0.72 | -0.70 / -0.65 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[CSNK1G2]] | -0.68 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[UBL5]] | -0.64 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[GLRX5]] | -0.61 | -0.48 / -0.72 | both halves | 2e-05 |  |
| [[COX6C]] | -0.60 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[CASTOR3P]] | -0.59 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[EMSY]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[HIGD2A]] | -0.59 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[KDELR1]] | -0.58 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[UBE2G1]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[ATP5PF]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[KIAA2026]] | -0.58 | -0.40 / -0.66 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises HUS1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PRKG2-AS1]] | B | PRKG2-AS1 activity strengthens HUS1's drug response | lines that do not express PRKG2-AS1 (23) vs lines expressing it (25) | the lines without PRKG2-AS1 respond 0.95× as strongly (z diff +0.07); strongest at Homoharringtonine 0.5 µM: 2.33x vs 2.58x (z diff +1.2) | 0.099 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.9, 0.9); signed map (-0.7, -35.1). **Vector** length 104, 24.2% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.9 | +17.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.0 | +12.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.9 | +13.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +20.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.2 | +8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +6.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.6 | -13.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -9.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.9 | -5.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.8 | -5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -3.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.1 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | HUS1 checkpoint clamp component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p12.3 — chr7:47,963,288-47,979,615 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Checkpoint clamp complex |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 21 pathways, smallest: Impaired BRCA2 binding to RAD51; Activation of ATR in response to replication stress; HDR through Single Strand Annealing (SSA) |
| Matched by | ensembl_id |

**Function**, from UniProt [O60921](https://www.uniprot.org/uniprotkb/O60921) (Checkpoint protein HUS1):

> Component of the 9-1-1 cell-cycle checkpoint response complex that plays a major role in DNA repair. The 9-1-1 complex is recruited to DNA lesion upon damage by the RAD17-replication factor C (RFC) clamp loader complex. Acts then as a sliding clamp platform on DNA for several proteins involved in long-patch base excision repair (LP-BER). The 9-1-1 complex stimulates DNA polymerase beta (POLB) activity by increasing its affinity for the 3'-OH end of the primer-template and stabilizes POLB to …

**Summary**, from NCBI Gene [3364](https://www.ncbi.nlm.nih.gov/gene/3364):

> The protein encoded by this gene is a component of an evolutionarily conserved, genotoxin-activated checkpoint complex that is involved in the cell cycle arrest in response to DNA damage. This protein forms a heterotrimeric complex with checkpoint proteins RAD9 and RAD1. In response to DNA damage, the trimeric complex interacts with another protein complex consisting of checkpoint protein RAD17 and four small subunits of the replication factor C (RFC), which loads the combined complex onto the …

**Accessions** — [HGNC:5309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5309) · Entrez [3364](https://www.ncbi.nlm.nih.gov/gene/3364) · UniProt [O60921](https://www.uniprot.org/uniprotkb/O60921) · Ensembl [ENSG00000136273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136273)

## Data

Gene col 5849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5849); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5849]; `tensor/DDL_lfc|DDL_z.npy` [5849]; `embed/gene_vectors.npy` [5849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5849 or target_col == 5849). Every well: [[HUS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HUS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
