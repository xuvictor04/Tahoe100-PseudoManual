---
symbol: "TMEM63A"
type: "gene"
col: 12149
ensembl_id: "ENSG00000196187"
name: "transmembrane protein 63A"
location: "1q42.12"
module: 135
arm: "-"
pooled_cpm: 48.84
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 42
n_dd_up_clean: 0
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# TMEM63A

*transmembrane protein 63A* — 1q42.12

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (COLO 205 1.91×).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.255× (z -39.1, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CKLF]] (+0.56, fdr 8e-05), [[RPS6KA1]] (+0.55, fdr 4e-05), [[RGL3]] (+0.55, fdr 3e-05); moves opposite to [[DIO2]] (-0.51, fdr 1e-05), [[SEMA6A-AS1]] (-0.50, fdr 3e-05), [[CLIP1]] (-0.48, fdr 7e-05).
> It sits in the **-** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CLMN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12149.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (COLO 205 1.91×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adenosine (drug)]] 5 µM |  | 1.11× | +3.2 | 0.45 | 6/47 (Panc 03.27, MIA PaCa-2, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.11× | +3.2 | 0.45 | 6/47 (NCI-H2030, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 24 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12149.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.255×** | -39.1 | 0e+00 | 45/47 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.275×** | -26.2 | 0e+00 | 43/46 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.375×** | -19.1 | 0e+00 | 43/47 (MIA PaCa-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.506×** | -13.8 | 4e-41 | 44/47 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.515×** | -13.5 | 3e-39 | 42/47 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.539×** | -12.5 | 6e-34 | 41/47 (A-172, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.655×** | -12.1 | 8e-32 | 32/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.545×** | -11.8 | 2e-30 | 33/46 (COLO 205, SNU-423, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.577×** | -11.1 | 5e-27 | 35/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.587×** | -10.8 | 3e-25 | 40/47 (LS 180, COLO 205, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.409×** | -9.5 | 2e-19 | 42/48 (MIA PaCa-2, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.655×** | -8.6 | 5e-16 | 35/47 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.659×** | -8.4 | 2e-15 | 31/46 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.664×** | -8.3 | 5e-15 | 35/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.669×** | -8.1 | 2e-14 | 29/47 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.498×** | -7.4 | 5e-12 | 37/47 (SK-MEL-2, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.713×** | -6.8 | 2e-10 | 31/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.831×** | -5.3 | 3e-06 | 21/47 (CFPAC-1, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.783×** | -4.9 | 2e-05 | 24/47 (CFPAC-1, NCI-H1573, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.793×** | -4.7 | 6e-05 | 22/47 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.644×** | -4.7 | 6e-05 | 22/47 (H4, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.783×** | -4.7 | 6e-05 | 22/47 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.645×** | -4.6 | 7e-05 | 22/47 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12149. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.4 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -22.4) |
| [[SW480 (line)]] | alt | 40.2 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -20.5) |
| [[A-172 (line)]] | wt | 48.2 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -24.8) |
| [[COLO 205 (line)]] | alt | 124 | 1 | 8 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.91× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -28.6) |
| [[NCI-H1573 (line)]] | alt | 72.0 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -34.8) |
| [[A549 (line)]] | wt | 37.4 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0520× (z -24.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.160× (z -22.8) |
| [[HOP62 (line)]] | alt | 47.2 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -23.2) |
| [[MIA PaCa-2 (line)]] | alt | 65.6 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0691× (z -34.1) |
| [[SW 900 (line)]] | alt | 96.7 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -30.0) |
| [[PANC-1 (line)]] | alt | 40.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -22.4) |
| [[SNU-423 (line)]] | alt | 49.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -23.1) |
| [[HT-29 (line)]] | alt | 78.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -19.0) |
| [[KATO III (line)]] | alt | 50.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -20.9) |
| [[LS 180 (line)]] | wt | 99.8 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -16.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 50.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0994× (z -28.9) |
| [[SW1417 (line)]] | alt | 72.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -16.3) |
| [[CFPAC-1 (line)]] | alt | 72.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -25.6) |
| [[HEC-1-A (line)]] | alt | 54.8 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -12.4) |
| [[LoVo (line)]] | wt | 50.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -20.8) |
| [[Panc 03.27 (line)]] | alt | 77.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -17.9) |
| [[SK-MEL-2 (line)]] | alt | 50.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -27.1) |
| [[HS-578T (line)]] | alt | 29.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 32.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -16.3) |
| [[A-427 (line)]] | wt | 25.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -12.9) |
| [[A498 (line)]] | wt | 30.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -20.5) |
| [[AsPC-1 (line)]] | alt | 26.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.4) |
| [[BT-474 (line)]] | alt | 98.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -13.6) |
| [[C32 (line)]] | wt | 37.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -13.7) |
| [[H4 (line)]] | wt | 45.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0423× (z -20.1) |
| [[HCT15 (line)]] | alt | 59.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 31.6 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.124× (z -11.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.5) |
| [[CHP-212 (line)]] | wt | 39.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0803× (z -10.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 42.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -17.1) |
| [[LOX-IMVI (line)]] | wt | 20.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 39.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -21.2) |
| [[NCI-H2347 (line)]] | alt | 54.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -19.3) |
| [[RKO (line)]] | wt | 34.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -15.4) |
| [[RPMI-7951 (line)]] | alt | 38.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 31.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -8.9) |
| [[J82 (line)]] | alt | 31.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -14.0) |
| [[SNU-1 (line)]] | wt | 36.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -12.7) |
| [[SW48 (line)]] | wt | 47.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[AN3 CA (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.43 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12149), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CKLF]] | +0.56 | +0.67 / +0.37 | both halves | 8e-05 |  |
| [[RPS6KA1]] | +0.55 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[RGL3]] | +0.55 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[MRI1]] | +0.50 | +0.42 / +0.39 | both halves | 5e-05 |  |
| [[ABCD4]] | +0.48 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[RNASET2]] | +0.48 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[CCDC134]] | +0.48 | +0.52 / +0.27 | both halves | 3e-04 |  |
| [[KYAT1]] | +0.48 | +0.61 / +0.28 | both halves | 3e-04 |  |
| [[RAD9A]] | +0.47 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[TUBGCP2]] | +0.47 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[FHOD1]] | +0.47 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[PHLDB3]] | +0.46 | +0.47 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIO2]] | -0.51 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SEMA6A-AS1]] | -0.50 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[CLIP1]] | -0.48 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[ZNF518B]] | -0.47 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[RBM15B]] | -0.47 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[CENPBD1P]] | -0.47 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[LINC00907]] | -0.47 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[LURAP1L-AS1]] | -0.46 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[ZNF644]] | -0.46 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[PDCD6IP-DT]] | -0.46 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[DPY19L1P2]] | -0.46 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[CEP112]] | -0.45 | -0.49 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLMN]] | B | CLMN activity raises TMEM63A's level | lines that do not express CLMN (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without CLMN | 0.005 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[CPLANE1]] | B | CPLANE1 activity lowers TMEM63A's level | lines that do not express CPLANE1 (5) vs lines expressing it (45) | 1.80× higher at baseline in the lines without CPLANE1 | 0.060 | ⚠ within organs, on part of the lines; also absent: NKAIN1, SIX4, TPST1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **-** arm (projection on the module's main direction -0.392). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (14.6, -23.2); signed map (-25.8, 20.9). **Vector** length 66.0, 14.6% of its response variance represented; |z| ≥ 3 in 1,348 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.2 | -4.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +1.9 | -3.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +1.8 | -8.4 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +1.7 | +1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | -1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -26.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -12.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -39.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 63A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.12 — chr1:225,845,536-225,882,380 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0792 |
| Gene groups (HGNC) | TMEM63 family |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O94886](https://www.uniprot.org/uniprotkb/O94886) (Mechanosensitive cation channel TMEM63A):

> Mechanosensitive cation channel with low conductance and high activation threshold. In contrast to TMEM63B, does not show phospholipid scramblase activity. Acts as a regulator of lysosomal morphology by mediating lysosomal mechanosensitivity (By similarity). Important for the baby's first breath and respiration throughout life. Upon lung inflation conducts cation currents in alveolar type 1 and 2 cells triggering lamellar body exocytosis and surfactant secretion into airspace. Also acts as an …

**Summary**, from NCBI Gene [9725](https://www.ncbi.nlm.nih.gov/gene/9725):

> Enables mechanosensitive monoatomic ion channel activity. Predicted to be involved in lysosome organization and surfactant secretion. Located in bounding membrane of organelle; centriolar satellite; and plasma membrane. Implicated in hypomyelinating leukodystrophy 19. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29118) · Entrez [9725](https://www.ncbi.nlm.nih.gov/gene/9725) · UniProt [O94886](https://www.uniprot.org/uniprotkb/O94886) · Ensembl [ENSG00000196187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196187)

## Data

Gene col 12149: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12149); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12149, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12149]; `tensor/DDL_lfc|DDL_z.npy` [12149]; `embed/gene_vectors.npy` [12149]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12149 or target_col == 12149). Every well: [[TMEM63A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM63A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
