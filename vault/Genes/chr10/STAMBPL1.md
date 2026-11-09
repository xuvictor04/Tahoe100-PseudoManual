---
symbol: "STAMBPL1"
type: "gene"
col: 6131
ensembl_id: "ENSG00000138134"
name: "STAM binding protein like 1"
location: "10q23.31"
module: 92
arm: "+"
pooled_cpm: 30.47
n_lines_expressing: 44
n_dd_up: 4
n_dd_down: 43
n_dd_up_clean: 4
n_dd_down_clean: 40
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# STAMBPL1

*STAM binding protein like 1* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Bentamapimod (drug)]] 5 µM: 1.81× (z +3.9, q 0.028, up in 13 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.241× (z -18.0, q 0e+00, down in 40 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRED1]] (+0.71, fdr 7e-06), [[ETV1]] (+0.67, fdr 7e-06), [[B4GALT6]] (+0.66, fdr 7e-06); moves opposite to [[CRYAB]] (-0.57, fdr 1e-05), [[PLD3]] (-0.50, fdr 3e-05), [[RAB1A]] (-0.49, fdr 3e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[COL13A1]] → it (grade B ⚠); 7 go from it, the strongest it → [[EXTL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6131.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bentamapimod (drug)]] 5 µM |  | **1.81×** | +3.9 | 0.028 | 13/42 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | **1.80×** | +3.9 | 0.028 | 17/42 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.073 | 14/42 (A-172, NCI-H1792, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.087 | 10/42 (A549, HEC-1-A, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.29× | +3.3 | 0.12 | 10/42 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | 1.61× | +3.2 | 0.15 | 6/42 (NCI-H460, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6131.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.241×** | -18.0 | 0e+00 | 40/42 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.289×** | -15.7 | 0e+00 | 42/42 (LS 180, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.363×** | -12.8 | 3e-35 | 38/42 (LS 180, C32, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.469×** | -9.5 | 2e-19 | 33/42 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -8.2 | 3e-14 | 24/42 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.532×** | -7.5 | 6e-12 | 30/42 (C32, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.554×** | -7.2 | 7e-11 | 30/42 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.589×** | -7.1 | 1e-10 | 28/42 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.633×** | -6.5 | 5e-09 | 24/42 (C32, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.602×** | -6.4 | 1e-08 | 29/42 (PANC-1, C32, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.583×** | -6.2 | 2e-08 | 29/42 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.404×** | -6.0 | 1e-07 | 25/38 (NCI-H460, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.670×** | -5.9 | 1e-07 | 29/42 (C32, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.411×** | -5.9 | 2e-07 | 22/37 (C32, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.679×** | -5.8 | 3e-07 | 26/42 (C32, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.634×** | -5.7 | 4e-07 | 26/42 (C32, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.757×** | -4.9 | 3e-05 | 21/42 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6131. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 122 | 0 | 30 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0948× (z -22.0) |
| [[NCI-H460 (line)]] | wt | 49.4 | 0 | 18 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -19.3) |
| [[SK-MEL-2 (line)]] | alt | 30.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -15.6) |
| [[HCT15 (line)]] | alt | 59.7 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0759× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.202× (z -9.8) |
| [[PANC-1 (line)]] | alt | 41.0 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -14.1) |
| [[RKO (line)]] | wt | 53.5 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.191× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 32.4 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 29.2 | 0 | 5 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.125× (z -12.0) |
| [[LS 180 (line)]] | wt | 93.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0946× (z -18.6) |
| [[A549 (line)]] | wt | 33.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -11.0) |
| [[HOP62 (line)]] | alt | 22.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -10.3) |
| [[HT-29 (line)]] | alt | 18.5 | 2 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.77× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.263× (z -9.0) |
| [[LoVo (line)]] | wt | 26.6 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.248× (z -10.0) |
| [[SW480 (line)]] | alt | 35.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -15.0) |
| [[A-172 (line)]] | wt | 48.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -10.9) |
| [[COLO 205 (line)]] | alt | 49.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -10.0) |
| [[Hs 766T (line)]] | wt | 24.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -12.0) |
| [[KATO III (line)]] | alt | 17.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 64.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 24.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 34.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 24.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 31.9 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0843× (z -13.9) ⚠ transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.207× (z -8.9) |
| [[SW48 (line)]] | wt | 8.84 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0402× (z -11.0) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Rapamycin (drug)]] 0.5 µM 0.0808× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 26.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.264× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[SHP-77 (line)]] | alt | 20.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -11.3) |
| [[SNU-423 (line)]] | alt | 21.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -9.3) |
| [[A-427 (line)]] | wt | 5.74 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6131), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRED1]] | +0.71 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[ETV1]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[B4GALT6]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ETV4]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[ADGRL4]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[RASGRF1]] | +0.57 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[CCND1]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SPRY2]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[OSBPL10]] | +0.56 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[EXTL2]] | +0.56 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[SERTAD4]] | +0.55 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[ITGB5]] | +0.54 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYAB]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[PLD3]] | -0.50 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[RAB1A]] | -0.49 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[BLVRB]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[OSER1]] | -0.49 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[CALCOCO2]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[TBC1D23]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[KIF1B]] | -0.49 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[ULK1]] | -0.47 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[PEX16]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[TMEM208]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[RPS6KC1]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL13A1]] | B | COL13A1 activity raises STAMBPL1's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 2.59× lower at baseline in the lines without COL13A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[SH3TC2-DT]] | B | SH3TC2-DT activity raises STAMBPL1's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without SH3TC2-DT | 0.098 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G |
| [[KIFC3]] | C | KIFC3 activity raises STAMBPL1's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 5.15× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EXTL2]] | B | STAMBPL1 activity lowers EXTL2's level | lines that do not express STAMBPL1 (6) vs lines expressing it (44) | 1.87× higher at baseline in the lines without STAMBPL1 | 0.044 | ⚠ within organs, on part of the lines; also absent: CFAP45, PMAIP1, OCIAD2 |
| [[GLDC]] | B | STAMBPL1 activity lowers GLDC's level | lines that do not express STAMBPL1 (6) vs lines expressing it (44) | 6.52× higher at baseline in the lines without STAMBPL1 | 0.057 | ⚠ within organs, on part of the lines; also absent: CFAP45, PMAIP1, OCIAD2 |
| [[NHSL1]] | B | STAMBPL1 activity lowers NHSL1's level | lines that do not express STAMBPL1 (6) vs lines expressing it (44) | 1.67× higher at baseline in the lines without STAMBPL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CFAP45, PMAIP1, OCIAD2 |
| [[KIF1B]] | B | STAMBPL1 activity lowers KIF1B's level | lines that do not express STAMBPL1 (6) vs lines expressing it (44) | 1.68× higher at baseline in the lines without STAMBPL1 | 0.070 | ⚠ within organs, on part of the lines; also absent: CFAP45, PMAIP1, OCIAD2 |
| [[DUSP4]] | B | STAMBPL1 activity raises DUSP4's level | lines that do not express STAMBPL1 (6) vs lines expressing it (44) | 3.65× lower at baseline in the lines without STAMBPL1 | 0.081 | ⚠ within organs, on part of the lines; also absent: CFAP45, PMAIP1, OCIAD2 |
| [[COL13A1]] | B | STAMBPL1 activity raises COL13A1's level | lines that do not express STAMBPL1 (6) vs lines expressing it (44) | 3.61× lower at baseline in the lines without STAMBPL1 | 0.085 | ⚠ within organs, on part of the lines; also absent: CFAP45, PMAIP1, OCIAD2 |
| [[TLE6]] | C | STAMBPL1's natural level strengthens TLE6's drug response | STAMBPL1's natural level across 38 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.53; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.1, 7.6); signed map (9.5, 47.6). **Vector** length 120, 34.8% of its response variance represented; |z| ≥ 3 in 1,306 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MAPK output* (control, mean cos +0.57 to 8); *KRAS signaling up* (hallmark, mean cos +0.51 to 7); *MAPK family signaling cascades* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | -1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +0.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +2.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -7.4 | -7.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.1 | -5.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.4 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.9 | -6.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -5.9 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.8 | -7.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.2 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | STAM binding protein like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:88,879,734-88,975,153 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AMSH-LP, KIAA1373, AMSH-FP, FLJ31524, ALMalpha, bA399O19.2 |
| Gene groups (HGNC) | JAMM/MPN+ metallopeptidase family |
| Reactome | 2 pathways, smallest: Metalloprotease DUBs; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FJ0](https://www.uniprot.org/uniprotkb/Q96FJ0) (AMSH-like protease):

> Zinc metalloprotease that specifically cleaves 'Lys-63'-linked polyubiquitin chains. Acts as a positive regulator of the TORC1 signaling pathway by mediating 'Lys-63'-linked deubiquitination of SESN2, thereby inhibiting SESN2-interaction with the GATOR2 complex. Does not cleave 'Lys-48'-linked polyubiquitin chains.

**Summary**, from NCBI Gene [57559](https://www.ncbi.nlm.nih.gov/gene/57559):

> Enables K63-linked deubiquitinase activity. Involved in cellular response to L-leucine and positive regulation of TORC1 signaling. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24105](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24105) · Entrez [57559](https://www.ncbi.nlm.nih.gov/gene/57559) · UniProt [Q96FJ0](https://www.uniprot.org/uniprotkb/Q96FJ0) · Ensembl [ENSG00000138134](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138134)

## Data

Gene col 6131: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6131); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6131, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6131]; `tensor/DDL_lfc|DDL_z.npy` [6131]; `embed/gene_vectors.npy` [6131]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6131 or target_col == 6131). Every well: [[STAMBPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAMBPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
