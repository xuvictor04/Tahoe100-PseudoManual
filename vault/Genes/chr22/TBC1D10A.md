---
symbol: "TBC1D10A"
type: "gene"
col: 1839
ensembl_id: "ENSG00000099992"
name: "TBC1 domain family member 10A"
location: "22q12.2"
module: 161
arm: "+"
pooled_cpm: 32.0
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 23
n_dd_up_clean: 9
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# TBC1D10A

*TBC1 domain family member 10A* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +11.1, q 1e-25, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.639× (z -6.4, q 8e-08, down in 24 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.741× (z -6.0, q 4e-07, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATOSB]] (+0.65, fdr 3e-05), [[TYK2]] (+0.65, fdr 7e-06), [[CLIP2]] (+0.64, fdr 1e-05); moves opposite to [[MGST1]] (-0.60, fdr 4e-05), [[NSD1]] (-0.60, fdr 4e-05), [[ZFYVE9]] (-0.59, fdr 1e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1839.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +11.1 | 1e-25 | 37/47 (SNU-423, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.68×** | +7.7 | 4e-12 | 35/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +7.1 | 2e-10 | 29/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +6.5 | 1e-08 | 26/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +6.4 | 1e-08 | 28/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +5.7 | 1e-06 | 25/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +5.6 | 2e-06 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.1 | 2e-05 | 27/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.9 | 8e-05 | 22/44 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 0.001 | 23/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +4.2 | 0.001 | 20/45 (HS-578T, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1839.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.639×** | -6.4 | 8e-08 | 24/35 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.741×** | -6.0 | 4e-07 | 27/48 (A-172, HS-578T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -5.7 | 2e-06 | 26/46 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.673×** | -5.7 | 2e-06 | 26/43 (NCI-H2030, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -4.7 | 3e-04 | 22/47 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.722×** | -4.7 | 3e-04 | 24/48 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.734×** | -4.6 | 4e-04 | 25/48 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.741×** | -4.4 | 6e-04 | 24/48 (HT-29, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.736×** | -4.4 | 8e-04 | 24/47 (NCI-H1573, hTERT-HPNE, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.785×** | -4.2 | 0.001 | 23/48 (NCI-H23, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.764×** | -4.0 | 0.003 | 21/48 (SNU-423, HS-578T, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.757×** | -3.8 | 0.006 | 21/48 (SNU-423, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.773×** | -3.7 | 0.010 | 21/48 (NCI-H23, SW 900, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.783×** | -3.6 | 0.011 | 19/48 (hTERT-HPNE, H4, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.776×** | -3.6 | 0.011 | 15/46 (RKO, NCI-H23, …) | rises with dose |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.791×** | -3.5 | 0.017 | 13/47 (A-172, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.823×** | -3.3 | 0.030 | 12/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1839. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.4 | 10 (6 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.94× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.27× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.105× (z -15.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 19.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.5) | — |
| [[A498 (line)]] | wt | 90.1 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -11.7) |
| [[A-172 (line)]] | wt | 34.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0625× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.448× (z -8.5) |
| [[SW480 (line)]] | alt | 17.8 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 19.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 105 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 38.6 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 3.48× (z +8.9) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -9.0) |
| [[SNU-423 (line)]] | alt | 50.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.7) |
| [[C-33 A (line)]] | alt | 10.6 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0846× (z -9.8) |
| [[HCT15 (line)]] | alt | 30.4 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.159× (z -9.9) |
| [[Hs 766T (line)]] | wt | 45.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 48.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0432× (z -18.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -13.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 33.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.57× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 40.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -10.0) |
| [[NCI-H2122 (line)]] | alt | 28.8 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.231× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -9.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 57.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -8.8) |
| [[SHP-77 (line)]] | alt | 26.5 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.167× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +9.5) | — |
| [[SW 1088 (line)]] | alt | 72.5 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.0530× (z -8.7) |
| [[A-427 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1839), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATOSB]] | +0.65 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[TYK2]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[CLIP2]] | +0.64 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[PPARA]] | +0.62 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[CD82]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.62 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[ASMTL]] | +0.62 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[CASTOR1]] | +0.61 | +0.52 / +0.49 | both halves | 1e-05 | ⚠ **readthrough risk**: CASTOR1 lies 2.4 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[ECE1]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[FCHO1]] | +0.61 | +0.64 / +0.23 | both halves | 5e-04 |  |
| [[BAIAP3]] | +0.60 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[GNAI2]] | +0.60 | +0.60 / +0.30 | both halves | 2e-04 |  |
| [[TGFB1]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGST1]] | -0.60 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[NSD1]] | -0.60 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[ZFYVE9]] | -0.59 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[ZNF124]] | -0.59 | -0.59 / -0.37 | both halves | 9e-05 |  |
| [[RAB11FIP2]] | -0.58 | -0.58 / -0.29 | both halves | 2e-04 |  |
| [[QRSL1]] | -0.57 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[MLH3]] | -0.56 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[DERA]] | -0.55 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[LARP4]] | -0.55 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[ZMYND11]] | -0.55 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[EPM2A]] | -0.54 | -0.50 / -0.26 | both halves | 4e-04 |  |
| [[STXBP5]] | -0.54 | -0.54 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TBC1D10A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BDKRB2]] | B | BDKRB2 activity raises TBC1D10A's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 1.56× lower at baseline in the lines without BDKRB2 | 0.048 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[MGST1]] | B | MGST1 activity raises TBC1D10A's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without MGST1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[SMOX]] | B | SMOX activity raises TBC1D10A's level | lines that do not express SMOX (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without SMOX | 0.054 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[ADAM8]] | B | ADAM8 activity raises TBC1D10A's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.42× lower at baseline in the lines without ADAM8 | 0.059 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[BDKRB2]] | B | BDKRB2 activity weakens TBC1D10A's drug response | lines that do not express BDKRB2 (18) vs lines expressing it (30) | the lines without BDKRB2 respond 1.07× as strongly (z diff -0.30); strongest at Belinostat 5 µM: 1.92x vs 1.33x (z diff -2.1) | 0.068 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.9, -3.8); signed map (-21.7, 27.1). **Vector** length 101, 25.7% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +6.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +11.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | -0.1 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.8 | +1.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +0.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.1 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.2 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -6.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 10A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,291,990-30,326,947 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EPI64, AC004997.C22.2; previously TBC1D10 |
| Gene groups (HGNC) | TBC1 domain family members |
| Reactome | 4 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXI6](https://www.uniprot.org/uniprotkb/Q9BXI6) (TBC1 domain family member 10A):

> GTPase-activating protein (GAP) specific for RAB27A and RAB35. Does not show GAP activity for RAB2A, RAB3A and RAB4A.

**Summary**, from NCBI Gene [83874](https://www.ncbi.nlm.nih.gov/gene/83874):

> Enables GTPase activator activity and PDZ domain binding activity. Involved in positive regulation of proteolysis and retrograde transport, endosome to Golgi. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23609](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23609) · Entrez [83874](https://www.ncbi.nlm.nih.gov/gene/83874) · UniProt [Q9BXI6](https://www.uniprot.org/uniprotkb/Q9BXI6) · Ensembl [ENSG00000099992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099992)

## Data

Gene col 1839: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1839); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1839, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1839]; `tensor/DDL_lfc|DDL_z.npy` [1839]; `embed/gene_vectors.npy` [1839]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1839 or target_col == 1839). Every well: [[TBC1D10A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D10A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
