---
symbol: "TET1"
type: "gene"
col: 6155
ensembl_id: "ENSG00000138336"
name: "tet methylcytosine dioxygenase 1"
location: "10q21.3"
module: 103
arm: "+"
pooled_cpm: 36.67
n_lines_expressing: 38
n_dd_up: 15
n_dd_down: 38
n_dd_up_clean: 13
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 15
direction_downstream: 6
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# TET1

*tet methylcytosine dioxygenase 1* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.58× (z +7.4, q 7e-11, up in 24 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.534× (z -14.3, q 2e-43, down in 31 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TF]] (+0.63, fdr 1e-05), [[SMAD9]] (+0.59, fdr 1e-05), [[SDC2]] (+0.59, fdr 1e-05); moves opposite to [[MGLL]] (-0.46, fdr 7e-05), [[XDH]] (-0.45, fdr 4e-05), [[PCED1B]] (-0.42, fdr 6e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[SMIM10]] → it (grade B ⚠); 6 go from it, the strongest it → [[RFX7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6155.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +7.4 | 7e-11 | 24/36 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.3 | 9e-08 | 10/30 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.42×** | +5.7 | 2e-06 | 20/36 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +5.4 | 1e-05 | 18/35 (NCI-H460, A-172, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +4.8 | 1e-04 | 18/36 (RPMI-7951, SNU-423, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.76×** | +4.8 | 2e-04 | 12/34 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.005 | 9/36 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.008 | 10/35 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.26×** | +3.8 | 0.009 | 14/36 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.016 | 9/36 (HOP62, NCI-H460, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.018 | 9/36 (A-172, AN3 CA, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.24×** | +3.5 | 0.021 | 12/33 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.029 | 4/36 (hTERT-HPNE, A-172, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.4 | 0.029 | 8/36 (A-172, SNU-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.052 | 9/36 (NCI-H460, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.059 | 3/36 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.071 | 2/36 (SNU-423, H4) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6155.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -14.3 | 2e-43 | 31/36 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.451×** | -12.8 | 3e-35 | 32/36 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.470×** | -11.7 | 2e-29 | 27/36 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.565×** | -9.2 | 5e-18 | 24/36 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.587×** | -8.6 | 1e-15 | 22/36 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.588×** | -8.5 | 1e-15 | 24/36 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.602×** | -8.2 | 3e-14 | 26/36 (NCI-H1792, C32, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.624×** | -7.6 | 2e-12 | 23/36 (C32, SK-MEL-2, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.634×** | -7.3 | 1e-11 | 22/36 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.641×** | -7.2 | 5e-11 | 23/36 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.649×** | -7.0 | 2e-10 | 26/35 (C32, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.650×** | -6.9 | 2e-10 | 21/36 (C32, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.652×** | -6.9 | 3e-10 | 21/35 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.664×** | -6.6 | 2e-09 | 22/36 (C32, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.670×** | -6.4 | 4e-09 | 21/36 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -6.2 | 2e-08 | 20/36 (C32, SNU-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6155. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 244 | 0 | 24 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0259× (z -49.8) |
| [[SK-MEL-2 (line)]] | alt | 48.2 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0115× (z -30.1) |
| [[NCI-H1792 (line)]] | alt | 74.5 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -26.4) |
| [[NCI-H460 (line)]] | wt | 67.4 | 1 | 10 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.72× (z +9.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -16.3) |
| [[AN3 CA (line)]] | alt | 448 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -18.1) |
| [[SNU-1 (line)]] | wt | 68.2 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -13.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.268× (z -12.5) |
| [[SW480 (line)]] | alt | 103 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.272× (z -13.1) |
| [[A-172 (line)]] | wt | 71.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -26.5) |
| [[CHP-212 (line)]] | wt | 220 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0228× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.221× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 80.6 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.1) |
| [[SNU-423 (line)]] | alt | 41.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -16.8) |
| [[PANC-1 (line)]] | alt | 35.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -14.4) |
| [[C-33 A (line)]] | alt | 108 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0418× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.318× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 96.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0775× (z -19.1) |
| [[H4 (line)]] | wt | 23.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0608× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 75.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 22.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.9) |
| [[SHP-77 (line)]] | alt | 55.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.266× (z -9.0) |
| [[SW 900 (line)]] | alt | 18.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.78× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.123× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 33.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 12.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 6.43 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.33 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.61 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.28 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.15 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6155), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TF]] | +0.63 | +0.55 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[SMAD9]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[SDC2]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PIAS2]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[LOXL3]] | +0.56 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[A2M]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[NRN1]] | +0.55 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TMEM45A]] | +0.55 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[LHFPL3-AS1]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[MEOX2]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[EPHA3]] | +0.54 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[NREP]] | +0.53 | +0.50 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGLL]] | -0.46 | -0.55 / -0.38 | both halves | 7e-05 | pathway: Epigenetic regulation of gene expression |
| [[XDH]] | -0.45 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[PCED1B]] | -0.42 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[SRGAP1]] | -0.41 | -0.40 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMIM10]] | B | SMIM10 activity raises TET1's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 2.22× lower at baseline in the lines without SMIM10 | 0.007 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[COL1A2]] | B | COL1A2 activity raises TET1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 3.53× lower at baseline in the lines without COL1A2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[LOXL3]] | B | LOXL3 activity raises TET1's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 3.53× lower at baseline in the lines without LOXL3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent |
| [[MGLL]] | B | MGLL activity lowers TET1's level | lines that do not express MGLL (14) vs lines expressing it (36) | 3.98× higher at baseline in the lines without MGLL | 0.033 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[COL8A1]] | B | COL8A1 activity raises TET1's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 1.95× lower at baseline in the lines without COL8A1 | 0.045 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1 |
| [[XDH]] | B | XDH activity lowers TET1's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.96× higher at baseline in the lines without XDH | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[FAM13C]] | B | FAM13C activity raises TET1's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 2.92× lower at baseline in the lines without FAM13C | 0.060 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[SYNGR1]] | B | SYNGR1 activity raises TET1's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 3.01× lower at baseline in the lines without SYNGR1 | 0.064 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers TET1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[LINC00461]] | B | LINC00461 activity raises TET1's level | lines that do not express LINC00461 (22) vs lines expressing it (28) | 1.83× lower at baseline in the lines without LINC00461 | 0.071 | ⚠ within organs, on part of the lines; also absent: NPTX2, EYA1, CELF4; maybe low, not absent |
| [[LINC02428]] | B | LINC02428 activity raises TET1's level | lines that do not express LINC02428 (32) vs lines expressing it (18) | 2.05× lower at baseline in the lines without LINC02428 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ENSG00000287598, ENSG00000287474 |
| [[CFI]] | B | CFI activity raises TET1's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.36× lower at baseline in the lines without CFI | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFX7]] | B | TET1 activity raises RFX7's level | lines that do not express TET1 (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without TET1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PLEKHO1, MCAM, KCNK13; maybe low, not absent |
| [[SMIM10]] | B | TET1 activity raises SMIM10's level | lines that do not express TET1 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without TET1 | 0.021 | ⚠ within organs, on part of the lines; also absent: PLEKHO1, MCAM, KCNK13; maybe low, not absent |
| [[KDM2B]] | B | TET1 activity raises KDM2B's level | lines that do not express TET1 (12) vs lines expressing it (38) | 1.73× lower at baseline in the lines without TET1 | 0.042 | ⚠ within organs, on part of the lines; also absent: PLEKHO1, MCAM, KCNK13; maybe low, not absent |
| [[EPHA3]] | B | TET1 activity raises EPHA3's level | lines that do not express TET1 (12) vs lines expressing it (38) | 2.89× lower at baseline in the lines without TET1 | 0.071 | ⚠ within organs, on part of the lines; also absent: PLEKHO1, MCAM, KCNK13; maybe low, not absent |
| [[PIAS2]] | B | TET1 activity raises PIAS2's level | lines that do not express TET1 (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without TET1 | 0.072 | ⚠ within organs, on part of the lines; also absent: PLEKHO1, MCAM, KCNK13; maybe low, not absent |
| [[NDUFB8]] | B | TET1 activity raises NDUFB8's level | lines that do not express TET1 (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without TET1 | 0.098 | ⚠ within organs, on part of the lines; also absent: PLEKHO1, MCAM, KCNK13; maybe low, not absent |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.540). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.8, 29.8); signed map (28.6, 41.3). **Vector** length 106, 28.9% of its response variance represented; |z| ≥ 3 in 1,100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.3 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +7.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +5.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -3.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -12.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -5.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.1 | -6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -5.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -5.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | tet methylcytosine dioxygenase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:68,560,337-68,694,487 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LCX, KIAA1676, bA119F7.1; previously CXXC6 |
| Gene groups (HGNC) | Zinc fingers CXXC-type; Tet methylcytosine dioxygenase family |
| Reactome | 2 pathways, smallest: TET1,2,3 and TDG demethylate DNA; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFU7](https://www.uniprot.org/uniprotkb/Q8NFU7) (Methylcytosine dioxygenase TET1):

> Dioxygenase that plays a key role in active DNA demethylation, by catalyzing the sequential oxidation of the modified genomic base 5-methylcytosine (5mC) into 5-hydroxymethylcytosine (5hmC), 5-formylcytosine (5fC), and 5-carboxylcytosine (5caC). In addition to its role in DNA demethylation, plays a more general role in chromatin regulation by recruiting histone modifying protein complexes to alter histone marks and chromatin accessibility, leading to both activation and repression of gene …

**Summary**, from NCBI Gene [80312](https://www.ncbi.nlm.nih.gov/gene/80312):

> DNA methylation is an epigenetic mechanism that is important for controlling gene expression. The protein encoded by this gene is a demethylase that belongs to the TET (ten-eleven translocation) family. Members of the TET protein family play a role in the DNA methylation process and gene activation. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:29484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29484) · Entrez [80312](https://www.ncbi.nlm.nih.gov/gene/80312) · UniProt [Q8NFU7](https://www.uniprot.org/uniprotkb/Q8NFU7) · Ensembl [ENSG00000138336](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138336)

## Data

Gene col 6155: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6155); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6155, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6155]; `tensor/DDL_lfc|DDL_z.npy` [6155]; `embed/gene_vectors.npy` [6155]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6155 or target_col == 6155). Every well: [[TET1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TET1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
