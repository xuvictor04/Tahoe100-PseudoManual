---
symbol: "GMFB"
type: "gene"
col: 12329
ensembl_id: "ENSG00000197045"
name: "glia maturation factor beta"
location: "14q22.2"
module: 25
arm: "+"
pooled_cpm: 32.45
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# GMFB

*glia maturation factor beta* — 14q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.57× (z +14.7, q 0e+00, up in 36 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +13.8, q 9e-41, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.594× (z -10.6, q 3e-23, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OCRL]] (+0.77, fdr 7e-06), [[LIN7C]] (+0.75, fdr 1e-05), [[NRAS]] (+0.72, fdr 1e-05); moves opposite to [[DRD4]] (-0.68, fdr 7e-06), [[COG7]] (-0.68, fdr 7e-06), [[RAB40C]] (-0.68, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SFT2D2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12329.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +14.7 | 0e+00 | 36/39 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +13.8 | 9e-41 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +11.5 | 1e-28 | 36/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +11.5 | 1e-28 | 43/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.85×** | +9.6 | 1e-19 | 40/48 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +8.0 | 9e-14 | 36/48 (PANC-1, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +7.8 | 7e-13 | 31/43 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +6.5 | 5e-09 | 34/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +6.3 | 1e-08 | 31/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +5.4 | 3e-06 | 30/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +5.1 | 2e-05 | 24/48 (PANC-1, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.2 | 0.001 | 13/33 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.2 | 0.001 | 23/47 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.016 | 16/48 (NCI-H1792, H4, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.017 | 14/48 (Panc 03.27, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.039 | 9/48 (A-427, NCI-H1573, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.069 | 14/48 (COLO 205, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.071 | 15/48 (KATO III, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.16× | +2.9 | 0.090 | 10/48 (HEC-1-A, HCT15, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +2.9 | 0.090 | 13/47 (SW48, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12329.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.594×** | -10.6 | 3e-23 | 40/48 (HT-29, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.690×** | -6.1 | 4e-07 | 29/48 (NCI-H2030, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.731×** | -5.1 | 6e-05 | 25/48 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.672×** | -4.6 | 5e-04 | 28/47 (HCT15, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -4.3 | 0.002 | 23/47 (SW 1271, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.780×** | -4.1 | 0.005 | 20/48 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.720×** | -3.8 | 0.010 | 21/48 (KATO III, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -3.4 | 0.054 | 18/48 (SNU-1, SW480, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.817×** | -3.3 | 0.059 | 18/48 (NCI-H2030, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12329. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.9 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -9.0) |
| [[LS 180 (line)]] | wt | 33.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +9.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -8.9) |
| [[PANC-1 (line)]] | alt | 29.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 21.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +8.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -10.1) |
| [[KATO III (line)]] | alt | 23.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.64× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 41.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 28.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +12.8) | — |
| [[SW 900 (line)]] | alt | 33.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.83× (z +8.9) | — |
| [[A-427 (line)]] | wt | 52.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.94× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 24.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +8.6) | — |
| [[C32 (line)]] | wt | 25.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +11.4) | — |
| [[H4 (line)]] | wt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 36.9 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0895× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 22.4 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0815× (z -11.1) |
| [[HOP62 (line)]] | alt | 21.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 19.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +9.0) | — |
| [[J82 (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0883× (z -10.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 21.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 39.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 25.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 32.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 27.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.24× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 30.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12329), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCRL]] | +0.77 | +0.62 / +0.82 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.75 | +0.57 / +0.81 | both halves | 1e-05 |  |
| [[NRAS]] | +0.72 | +0.54 / +0.77 | both halves | 1e-05 |  |
| [[GUF1]] | +0.72 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[SLC25A24]] | +0.71 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[ALG10B]] | +0.70 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[ZDHHC21]] | +0.69 | +0.48 / +0.79 | both halves | 2e-05 |  |
| [[HUS1]] | +0.69 | +0.57 / +0.75 | both halves | 9e-06 |  |
| [[TEX261]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[HDHD2]] | +0.68 | +0.39 / +0.75 | both halves | 5e-05 |  |
| [[TAF9]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ZNF260]] | +0.68 | +0.59 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRD4]] | -0.68 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[COG7]] | -0.68 | -0.64 / -0.69 | both halves | 7e-06 |  |
| [[RAB40C]] | -0.68 | -0.48 / -0.78 | both halves | 2e-05 |  |
| [[QPCTL]] | -0.67 | -0.47 / -0.71 | both halves | 2e-05 |  |
| [[COX6B1]] | -0.66 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[MARK4]] | -0.66 | -0.48 / -0.72 | both halves | 2e-05 |  |
| [[SDHAF1]] | -0.66 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[CSNK1G2]] | -0.65 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[RPS29]] | -0.65 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[NARF]] | -0.64 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[MIR4458HG]] | -0.64 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[PRKRIP1]] | -0.64 | -0.56 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GMFB's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises GMFB's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SFT2D2]] | C | GMFB's natural level weakens SFT2D2's drug response | GMFB's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse +0.14; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.1, -19.0); signed map (-15.3, -38.2). **Vector** length 108, 28.0% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.6 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +11.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.1 | +1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +3.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -10.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -1.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.3 | -2.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.2 | -3.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | glia maturation factor beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.2 — chr14:54,474,484-54,489,025 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GMF |
| Gene groups (HGNC) | Glia maturation factor family |
| Hallmark sets | COMPLEMENT |
| Matched by | ensembl_id |

**Function**, from UniProt [P60983](https://www.uniprot.org/uniprotkb/P60983) (Glia maturation factor beta):

> This protein causes differentiation of brain cells, stimulation of neural regeneration, and inhibition of proliferation of tumor cells.

**Summary**, from NCBI Gene [2764](https://www.ncbi.nlm.nih.gov/gene/2764):

> Predicted to enable Arp2/3 complex binding activity. Predicted to be involved in actin filament debranching and negative regulation of Arp2/3 complex-mediated actin nucleation. Predicted to act upstream of or within learning and locomotory behavior. Predicted to be active in cortical actin cytoskeleton. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4373](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4373) · Entrez [2764](https://www.ncbi.nlm.nih.gov/gene/2764) · UniProt [P60983](https://www.uniprot.org/uniprotkb/P60983) · Ensembl [ENSG00000197045](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197045)

## Data

Gene col 12329: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12329); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12329, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12329]; `tensor/DDL_lfc|DDL_z.npy` [12329]; `embed/gene_vectors.npy` [12329]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12329 or target_col == 12329). Every well: [[GMFB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GMFB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
