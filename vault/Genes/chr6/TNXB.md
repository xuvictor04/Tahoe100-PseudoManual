---
symbol: "TNXB"
type: "gene"
col: 9656
ensembl_id: "ENSG00000168477"
name: "tenascin XB"
location: "6p21.33-p21.32"
module: 37
arm: "+"
pooled_cpm: 18.73
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 27
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# TNXB

*tenascin XB* — 6p21.33-p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.66× (z +15.3, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.407× (z -9.9, q 2e-20, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BNIPL]] (+0.74, fdr 7e-06), [[TMEM269]] (+0.72, fdr 7e-06), [[DNHD1]] (+0.71, fdr 7e-06); moves opposite to [[COMMD8]] (-0.64, fdr 1e-05), [[AGPS]] (-0.63, fdr 7e-06), [[TIGD2]] (-0.60, fdr 4e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9656.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +15.3 | 0e+00 | 42/48 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +8.9 | 1e-16 | 36/47 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +6.1 | 2e-07 | 30/48 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.55×** | +5.4 | 9e-06 | 27/47 (A-427, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +5.2 | 2e-05 | 26/48 (NCI-H2030, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +5.0 | 5e-05 | 28/48 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.7 | 2e-04 | 6/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.019 | 20/48 (SW1417, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9656.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.407×** | -9.9 | 2e-20 | 39/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.404×** | -9.6 | 2e-19 | 35/47 (COLO 205, RKO, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.467×** | -8.4 | 7e-15 | 38/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.484×** | -7.7 | 2e-12 | 34/46 (LOX-IMVI, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.664×** | -6.4 | 2e-08 | 29/48 (Hs 766T, SW 1271, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.591×** | -5.6 | 2e-06 | 29/48 (PANC-1, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.606×** | -5.3 | 9e-06 | 18/29 (HCT15, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.645×** | -4.8 | 9e-05 | 23/47 (KATO III, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.650×** | -4.8 | 1e-04 | 25/48 (H4, SNU-1, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.669×** | -4.4 | 5e-04 | 27/48 (LoVo, AN3 CA, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **0.673×** | -4.4 | 6e-04 | 21/41 (HCT15, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.472×** | -4.3 | 7e-04 | 20/46 (Hs 766T, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.480×** | -4.2 | 1e-03 | 18/45 (H4, C32, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.685×** | -4.2 | 0.001 | 23/47 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.491×** | -4.1 | 0.001 | 21/46 (C32, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.521×** | -3.8 | 0.006 | 21/46 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.729×** | -3.5 | 0.014 | 18/48 (SW 1088, hTERT-HPNE, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.557×** | -3.4 | 0.020 | 15/45 (AsPC-1, C-33 A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.653×** | -3.4 | 0.021 | 13/48 (SW 900, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.731×** | -3.3 | 0.022 | 16/47 (HT-29, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.740×** | -3.3 | 0.022 | 14/48 (HT-29, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.725×** | -3.3 | 0.024 | 17/46 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9656. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.1 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.210× (z -10.7) |
| [[C32 (line)]] | wt | 9.73 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +10.2) | [[Captopril (drug)]] 0.05 µM 0.131× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 23.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.189× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 9.56 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Pemetrexed (drug)]] 5 µM 0.138× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 25.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0864× (z -15.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[H4 (line)]] | wt | 56.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0978× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.182× (z -9.4) |
| [[HCT15 (line)]] | alt | 77.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0608× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[A-427 (line)]] | wt | 30.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.248× (z -8.7) |
| [[A498 (line)]] | wt | 16.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 13.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.0953× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[LOX-IMVI (line)]] | wt | 12.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -10.0) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 11.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 19.6 | 0 | 2 (1 ⚠) | — | [[venetoclax (drug)]] 5 µM 0.0510× (z -9.3) |
| [[SW 900 (line)]] | alt | 15.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +8.7) | [[Docetaxel (drug)]] 0.05 µM 0.0867× (z -11.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[A549 (line)]] | wt | 19.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.179× (z -9.8) |
| [[COLO 205 (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.132× (z -11.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 19.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 18.0 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.113× (z -8.6) |
| [[Hs 766T (line)]] | wt | 18.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.225× (z -9.6) |
| [[HS-578T (line)]] | alt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +9.8) | — |
| [[J82 (line)]] | alt | 21.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 5.90 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0826× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 67.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[Panc 03.27 (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +15.5) | — |
| [[RKO (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0643× (z -10.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 6.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 9.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +9.2) | — |
| [[SW 1271 (line)]] | alt | 28.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.0269× (z -9.3) |
| [[SW1417 (line)]] | alt | 5.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.90× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9656), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BNIPL]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.72 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[DNHD1]] | +0.71 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[EFCAB12]] | +0.70 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[SPACDR]] | +0.69 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[WDR49]] | +0.69 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[ECT2L]] | +0.68 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[PHKG1]] | +0.68 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.67 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[PPP1R32]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[MUC20-OT1]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[HYPK]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD8]] | -0.64 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[AGPS]] | -0.63 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[TIGD2]] | -0.60 | -0.40 / -0.61 | both halves | 4e-05 |  |
| [[N6AMT1]] | -0.59 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[DHX9]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[B3GALT9]] | -0.58 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[MPHOSPH6]] | -0.58 | -0.46 / -0.60 | both halves | 2e-05 |  |
| [[ATIC]] | -0.57 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[SLX4IP]] | -0.57 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[ZDHHC21]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[AADAT]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TNXB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 1.7% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers TNXB's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.6, -19.6); signed map (10.4, 6.8). **Vector** length 112, 30.4% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +15.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +8.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +6.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.7 | +4.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.2 | +0.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.8 | -9.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.5 | -9.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.6 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -8.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.3 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -4.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -4.0 | -4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -1.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.5 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | tenascin XB |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33-p21.32 — chr6:32,041,153-32,115,334 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TNXBS, XBS, XB, HXBL, TN-X, TNX; previously TNXB1, TNXB2 |
| Gene groups (HGNC) | Tenascins |
| Reactome | 2 pathways, smallest: ECM proteoglycans; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P22105](https://www.uniprot.org/uniprotkb/P22105) (Tenascin-X):

> Appears to mediate interactions between cells and the extracellular matrix. Substrate-adhesion molecule that appears to inhibit cell migration. Accelerates collagen fibril formation. May play a role in supporting the growth of epithelial tumors.

**Summary**, from NCBI Gene [7148](https://www.ncbi.nlm.nih.gov/gene/7148):

> This gene encodes a member of the tenascin family of extracellular matrix glycoproteins. The tenascins have anti-adhesive effects, as opposed to fibronectin which is adhesive. This protein is thought to function in matrix maturation during wound healing, and its deficiency has been associated with the connective tissue disorder Ehlers-Danlos syndrome. This gene localizes to the major histocompatibility complex (MHC) class III region on chromosome 6. It is one of four genes in this cluster which …

**Accessions** — [HGNC:11976](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11976) · Entrez [7148](https://www.ncbi.nlm.nih.gov/gene/7148) · UniProt [P22105](https://www.uniprot.org/uniprotkb/P22105) · Ensembl [ENSG00000168477](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168477)

## Data

Gene col 9656: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9656); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9656, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9656]; `tensor/DDL_lfc|DDL_z.npy` [9656]; `embed/gene_vectors.npy` [9656]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9656 or target_col == 9656). Every well: [[TNXB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNXB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
