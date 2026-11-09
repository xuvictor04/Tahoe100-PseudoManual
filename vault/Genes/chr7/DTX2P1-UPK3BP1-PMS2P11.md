---
symbol: "DTX2P1-UPK3BP1-PMS2P11"
type: "gene"
col: 15458
ensembl_id: "ENSG00000265479"
name: "DTX2P1-UPK3BP1-PMS2P11 readthrough, transcribed pseudogene"
location: "7q11.23"
module: 25
arm: "-"
pooled_cpm: 15.68
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# DTX2P1-UPK3BP1-PMS2P11

*DTX2P1-UPK3BP1-PMS2P11 readthrough, transcribed pseudogene* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.60× (z +5.4, q 4e-05, up in 20 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.382× (z -21.6, q 0e+00, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTX2]] (+0.78, fdr 7e-06), [[ZNF816-ZNF321P]] (+0.63, fdr 1e-05), [[RPL36AL]] (+0.62, fdr 3e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[TUBD1]] (+0.62, fdr 1e-05); moves opposite to [[LIN7C]] (-0.65, fdr 1e-05), [[SCRN1]] (-0.65, fdr 1e-05), [[TEX261]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[DTX2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +5.4 | 4e-05 | 20/41 (Hs 766T, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.23× | +3.3 | 0.28 | 6/47 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15458.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.382×** | -21.6 | 0e+00 | 40/46 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.397×** | -14.6 | 0e+00 | 36/43 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.416×** | -13.9 | 1e-41 | 31/36 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.421×** | -12.7 | 1e-34 | 25/30 (MIA PaCa-2, C32, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.471×** | -11.5 | 2e-28 | 34/46 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.512×** | -10.2 | 2e-22 | 28/38 (LoVo, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.524×** | -9.8 | 7e-21 | 22/28 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.539×** | -9.8 | 1e-20 | 34/47 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.559×** | -9.2 | 2e-18 | 28/46 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.622×** | -7.5 | 3e-12 | 27/45 (LoVo, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.634×** | -7.2 | 3e-11 | 24/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.638×** | -7.1 | 5e-11 | 23/46 (SK-MEL-2, C32, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.686×** | -6.0 | 1e-07 | 24/47 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.701×** | -5.6 | 8e-07 | 22/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.773×** | -4.1 | 0.002 | 16/46 (NCI-H460, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.613×** | -4.0 | 0.002 | 18/47 (SK-MEL-2, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.770×** | -4.0 | 0.002 | 18/45 (J82, SNU-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.675×** | -3.2 | 0.033 | 9/45 (COLO 205, A498, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.683×** | -3.2 | 0.044 | 17/43 (C32, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.811×** | -3.1 | 0.048 | 13/47 (A549, HOP62, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.827×** | -3.0 | 0.069 | 17/47 (A498, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 39.9 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -17.8) |
| [[NCI-H460 (line)]] | wt | 10.4 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -15.0) |
| [[LoVo (line)]] | wt | 29.2 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -25.7) |
| [[C32 (line)]] | wt | 28.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -21.5) |
| [[SW480 (line)]] | alt | 16.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -17.4) |
| [[HEC-1-A (line)]] | alt | 15.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -18.8) |
| [[SW1417 (line)]] | alt | 21.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -15.8) |
| [[A498 (line)]] | wt | 28.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0626× (z -23.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.286× (z -10.5) |
| [[A549 (line)]] | wt | 23.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0483× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.301× (z -12.0) |
| [[COLO 205 (line)]] | alt | 39.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 25.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -21.7) |
| [[LS 180 (line)]] | wt | 22.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0572× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0813× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.115× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 19.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -11.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 5.55 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -13.2) |
| [[HT-29 (line)]] | alt | 14.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 14.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.363× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 22.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0965× (z -16.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 10.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0921× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.352× (z -11.8) |
| [[A-172 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -9.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0968× (z -9.9) |
| [[J82 (line)]] | alt | 7.58 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 9.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.3) |
| [[NCI-H2347 (line)]] | alt | 9.25 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0896× (z -12.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTX2]] | +0.78 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[ZNF816-ZNF321P]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.62 | +0.43 / +0.65 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TUBD1]] | +0.62 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[COX6B1]] | +0.60 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[COX6C]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ATP5MJ]] | +0.59 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[SNHG25]] | +0.59 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[RPS29]] | +0.59 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[LINC02976]] | +0.59 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[ROMO1]] | +0.58 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[COMMD6]] | +0.58 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[UBL5]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7C]] | -0.65 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[SCRN1]] | -0.65 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[TEX261]] | -0.63 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[GMFB]] | -0.63 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[PRKAR1A]] | -0.62 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[BACE1-AS]] | -0.62 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.62 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[ZBTB37]] | -0.61 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.61 | -0.37 / -0.67 | both halves | 8e-05 |  |
| [[ZNF664]] | -0.61 | -0.41 / -0.68 | both halves | 4e-05 |  |
| [[NRAS]] | -0.60 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[AKAP11]] | -0.60 | -0.53 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DTX2]] | C | DTX2P1-UPK3BP1-PMS2P11's natural level strengthens DTX2's drug response | DTX2P1-UPK3BP1-PMS2P11's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.34; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | DTX2P1-UPK3BP1-PMS2P11's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | DTX2P1-UPK3BP1-PMS2P11's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.56 | 0.514 over the table, 0.099 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.652). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-32.5, -19.8); signed map (-39.0, 5.4). **Vector** length 83.6, 16.9% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +5.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.3 | +1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | -0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +0.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.6 | +0.3 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | +1.5 | +0.9 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.3 | -9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.3 | -12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.2 | -13.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | -14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -21.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | DTX2P1-UPK3BP1-PMS2P11 readthrough, transcribed pseudogene |
| Locus type | readthrough (other) |
| Location | 7q11.23 — chr7:76,959,835-77,043,775 (+) |
| Ensembl biotype | lncRNA |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [441263](https://www.ncbi.nlm.nih.gov/gene/441263):

> This locus represents naturally-occurring readthrough transcription spanning multiple pseudogenes: DTX2P1 (DTX2 pseudogene 1), UPK3BP1 (uroplakin 3B pseudogene 1), PMS2P11 (PMS1 homolog 2, mismatch repair system component pseudogene 11). Some transcripts may also extend to PMS2P9 (PMS1 homolog 2, mismatch repair system component pseudogene 9). The readthrough transcripts likely do not encode functional proteins. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:42360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42360) · Entrez [441263](https://www.ncbi.nlm.nih.gov/gene/441263) · Ensembl [ENSG00000265479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000265479)

## Data

Gene col 15458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15458); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15458]; `tensor/DDL_lfc|DDL_z.npy` [15458]; `embed/gene_vectors.npy` [15458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15458 or target_col == 15458). Every well: [[DTX2P1-UPK3BP1-PMS2P11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTX2P1-UPK3BP1-PMS2P11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
