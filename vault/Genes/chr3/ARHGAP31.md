---
symbol: "ARHGAP31"
type: "gene"
col: 400
ensembl_id: "ENSG00000031081"
name: "Rho GTPase activating protein 31"
location: "3q13.32-q13.33"
module: 147
arm: "+"
pooled_cpm: 33.75
n_lines_expressing: 40
n_dd_up: 7
n_dd_down: 37
n_dd_up_clean: 7
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 28
direction_downstream: 13
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# ARHGAP31

*Rho GTPase activating protein 31* — 3q13.32-q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +9.9, q 3e-20, up in 25 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.170× (z -24.1, q 0e+00, down in 37 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LTBP2]] (+0.65, fdr 1e-05), [[LINC02454]] (+0.64, fdr 7e-06), [[TMEM156]] (+0.63, fdr 7e-06); moves opposite to [[AVPI1]] (-0.56, fdr 1e-05), [[CFD]] (-0.53, fdr 9e-05), [[KRAS]] (-0.53, fdr 3e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[FRMD4A]] → it (grade B ⚠); 13 go from it, the strongest it → [[ARHGAP22]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +9.9 | 3e-20 | 25/35 (NCI-H1792, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +6.2 | 2e-07 | 20/38 (PANC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.7 | 5e-04 | 19/38 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Ferulic acid (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.012 | 16/37 (A498, SNU-423, …) | two highest doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.019 | 13/38 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.037 | 13/37 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.081 | 12/38 (RKO, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.28× | +3.1 | 0.13 | 10/31 (LoVo, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[BAY1125976 (drug)]] 5 µM |  | 1.61× | +3.0 | 0.16 | 9/38 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 400.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.170×** | -24.1 | 0e+00 | 37/38 (Hs 766T, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.191×** | -22.5 | 0e+00 | 36/38 (Hs 766T, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.283×** | -17.2 | 0e+00 | 35/38 (Hs 766T, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.553×** | -8.3 | 1e-14 | 26/38 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.627×** | -7.7 | 2e-12 | 27/38 (RKO, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.547×** | -7.5 | 5e-12 | 30/38 (Hs 766T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.638×** | -6.2 | 4e-08 | 23/38 (NCI-H1573, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.659×** | -5.7 | 1e-06 | 19/37 (HEC-1-A, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.647×** | -5.5 | 2e-06 | 20/38 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.428×** | -5.4 | 5e-06 | 20/36 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.670×** | -5.2 | 9e-06 | 19/38 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.685×** | -4.9 | 4e-05 | 18/27 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.466×** | -4.8 | 6e-05 | 17/36 (RKO, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.732×** | -4.7 | 8e-05 | 16/38 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.698×** | -4.6 | 1e-04 | 14/37 (RKO, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.703×** | -4.6 | 1e-04 | 18/37 (NCI-H1573, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 49.5 | 1 | 9 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -12.2) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0969× (z -12.1) |
| [[RKO (line)]] | wt | 112 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0754× (z -18.2) |
| [[HEC-1-A (line)]] | alt | 29.4 | 0 | 8 | — | [[Belinostat (drug)]] 5 µM 0.0822× (z -14.4) |
| [[C32 (line)]] | wt | 67.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -14.6) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.184× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 80.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -16.2) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.110× (z -14.9) |
| [[H4 (line)]] | wt | 96.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.104× (z -15.1) |
| [[Hs 766T (line)]] | wt | 72.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0759× (z -20.8) |
| [[LoVo (line)]] | wt | 13.7 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 20.1 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.87× (z +11.5) | [[Adagrasib (drug)]] 0.05 µM 0.349× (z -15.3) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.109× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 28.3 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.125× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 23.9 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.131× (z -15.8) |
| [[PANC-1 (line)]] | alt | 36.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -14.0) |
| [[A-172 (line)]] | wt | 44.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.150× (z -14.6) |
| [[A498 (line)]] | wt | 42.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.189× (z -13.8) |
| [[A549 (line)]] | wt | 16.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -11.4) |
| [[HS-578T (line)]] | alt | 71.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -14.2) |
| [[J82 (line)]] | alt | 88.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.114× (z -15.1) |
| [[NCI-H2030 (line)]] | alt | 40.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -16.9) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.224× (z -10.0) |
| [[SW 1271 (line)]] | alt | 65.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0375× (z -10.8) |
| [[AN3 CA (line)]] | alt | 57.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0928× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 21.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -8.9) |
| [[HCT15 (line)]] | alt | 32.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -10.9) |
| [[HOP62 (line)]] | alt | 53.4 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.507× (z -10.7) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.101× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 17.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 81.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -12.2) |
| [[SNU-423 (line)]] | alt | 42.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -11.6) |
| [[SW 900 (line)]] | alt | 33.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 102 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0972× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.517× (z -12.4) ⚠ position not correctable |
| [[SW48 (line)]] | wt | 28.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +11.3) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[A-427 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.19 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTBP2]] | +0.65 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[LINC02454]] | +0.64 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[TMEM156]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[EVA1A]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ELK3]] | +0.63 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[KIAA1549L]] | +0.62 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[RPSAP52]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[C2orf92]] | +0.61 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ROBO4]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[COL27A1]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[B4GALT6]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[MARCHF4]] | +0.59 | +0.60 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVPI1]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[CFD]] | -0.53 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[KRAS]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[RHPN2]] | -0.52 | -0.44 / -0.35 | both halves | 1e-04 | pathway: RHOA GTPase cycle |
| [[EFNA4]] | -0.52 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[ARNT]] | -0.52 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[KIF16B]] | -0.49 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[PPP1R12B]] | -0.49 | -0.32 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 25, C 3. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD4A]] | B | FRMD4A activity raises ARHGAP31's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 3.57× lower at baseline in the lines without FRMD4A | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[ESM1]] | B | ESM1 activity raises ARHGAP31's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 3.23× lower at baseline in the lines without ESM1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| [[ROBO4]] | B | ROBO4 activity raises ARHGAP31's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 3.48× lower at baseline in the lines without ROBO4 | 0.006 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[LNCOG]] | B | LNCOG activity raises ARHGAP31's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 3.60× lower at baseline in the lines without LNCOG | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[LINC02454]] | B | LINC02454 activity raises ARHGAP31's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 4.08× lower at baseline in the lines without LINC02454 | 0.015 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[PRDM5]] | B | PRDM5 activity raises ARHGAP31's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 2.73× lower at baseline in the lines without PRDM5 | 0.015 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[FLI1]] | B | FLI1 activity raises ARHGAP31's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 3.01× lower at baseline in the lines without FLI1 | 0.020 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[BCL2A1]] | B | BCL2A1 activity raises ARHGAP31's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.60× lower at baseline in the lines without BCL2A1 | 0.022 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[COL27A1]] | B | COL27A1 activity raises ARHGAP31's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 3.30× lower at baseline in the lines without COL27A1 | 0.032 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[SPHK1]] | B | SPHK1 activity raises ARHGAP31's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 3.51× lower at baseline in the lines without SPHK1 | 0.042 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[CFAP58]] | B | CFAP58 activity raises ARHGAP31's level | lines that do not express CFAP58 (6) vs lines expressing it (44) | 1.90× lower at baseline in the lines without CFAP58 | 0.042 | ⚠ within organs, on part of the lines; also absent: MINDY4, ENSG00000286162, MPP4; maybe low, not absent |
| [[ESM1]] | B | ESM1 activity strengthens ARHGAP31's drug response | lines that do not express ESM1 (27) vs lines expressing it (11) | the lines without ESM1 respond 0.81× as strongly (z diff +1.28); strongest at Trametinib 5 µM: 0.56x vs 0.43x (z diff +2.6) | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; target measured in part of the lines; artifact flags |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP22]] | B | ARHGAP31 activity raises ARHGAP22's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 5.92× lower at baseline in the lines without ARHGAP31 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[CFAP58]] | B | ARHGAP31 activity raises CFAP58's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 1.58× lower at baseline in the lines without ARHGAP31 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[IL27RA]] | B | ARHGAP31 activity raises IL27RA's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 2.02× lower at baseline in the lines without ARHGAP31 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[LRRC8C]] | B | ARHGAP31 activity raises LRRC8C's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 2.63× lower at baseline in the lines without ARHGAP31 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[LINC02454]] | B | ARHGAP31 activity raises LINC02454's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 2.41× lower at baseline in the lines without ARHGAP31 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[FMNL3]] | B | ARHGAP31 activity raises FMNL3's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 3.05× lower at baseline in the lines without ARHGAP31 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[BNC2]] | B | ARHGAP31 activity raises BNC2's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 3.93× lower at baseline in the lines without ARHGAP31 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[SPHK1]] | B | ARHGAP31 activity raises SPHK1's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 2.63× lower at baseline in the lines without ARHGAP31 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[WNT5B]] | B | ARHGAP31 activity raises WNT5B's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 3.00× lower at baseline in the lines without ARHGAP31 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[MAMLD1]] | B | ARHGAP31 activity raises MAMLD1's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 3.57× lower at baseline in the lines without ARHGAP31 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[PRDM5]] | B | ARHGAP31 activity raises PRDM5's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 2.39× lower at baseline in the lines without ARHGAP31 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[NT5E]] | C | ARHGAP31 activity raises NT5E's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 4.56× lower at baseline in the lines without ARHGAP31 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1; co-absent with the target |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.7, 8.9); signed map (12.1, 47.3). **Vector** length 129, 37.9% of its response variance represented; |z| ≥ 3 in 1,151 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.9 | +9.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | -0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | -3.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +3.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.1 | -8.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.9 | -7.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.6 | -5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.3 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -22.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.8 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.32-q13.33 — chr3:119,294,383-119,420,714 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDGAP |
| Gene groups (HGNC) | Rho GTPase activating proteins |
| Reactome | 7 pathways, smallest: RHOU GTPase cycle; RHOA GTPase cycle; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2M1Z3](https://www.uniprot.org/uniprotkb/Q2M1Z3) (Rho GTPase-activating protein 31):

> Functions as a GTPase-activating protein (GAP) for RAC1 and CDC42. Required for cell spreading, polarized lamellipodia formation and cell migration.

**Summary**, from NCBI Gene [57514](https://www.ncbi.nlm.nih.gov/gene/57514):

> This gene encodes a GTPase-activating protein (GAP). A variety of cellular processes are regulated by Rho GTPases which cycle between an inactive form bound to GDP and an active form bound to GTP. This cycling between inactive and active forms is regulated by guanine nucleotide exchange factors and GAPs. The encoded protein is a GAP shown to regulate two GTPases involved in protein trafficking and cell growth. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:29216](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29216) · Entrez [57514](https://www.ncbi.nlm.nih.gov/gene/57514) · UniProt [Q2M1Z3](https://www.uniprot.org/uniprotkb/Q2M1Z3) · Ensembl [ENSG00000031081](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000031081)

## Data

Gene col 400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 400); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 400]; `tensor/DDL_lfc|DDL_z.npy` [400]; `embed/gene_vectors.npy` [400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 400 or target_col == 400). Every well: [[ARHGAP31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
