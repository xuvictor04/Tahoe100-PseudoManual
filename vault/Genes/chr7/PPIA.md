---
symbol: "PPIA"
type: "gene"
col: 12165
ensembl_id: "ENSG00000196262"
name: "peptidylprolyl isomerase A"
location: "7p13"
module: 50
arm: "+"
pooled_cpm: 89.23
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# PPIA

*peptidylprolyl isomerase A* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.20× (z +18.1, q 0e+00, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Acetohexamide (drug)]] 5 µM: 0.779× (z -5.7, q 6e-06, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUMO3]] (+0.64, fdr 1e-05), [[CFL1]] (+0.63, fdr 7e-06), [[RPSA]] (+0.61, fdr 7e-06); moves opposite to [[RBMX2]] (-0.70, fdr 1e-05), [[TIPRL]] (-0.68, fdr 1e-05), [[UBE2B]] (-0.66, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12165.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +18.1 | 0e+00 | 46/49 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +16.9 | 0e+00 | 46/49 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +14.4 | 7e-45 | 43/44 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +11.1 | 1e-26 | 41/45 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.2 | 7e-11 | 40/48 (A-172, HOP62, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.44×** | +5.9 | 3e-07 | 35/48 (HS-578T, CFPAC-1, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.42×** | +5.5 | 4e-06 | 37/50 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.38×** | +5.1 | 3e-05 | 35/48 (SNU-423, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.35×** | +4.9 | 7e-05 | 36/48 (HOP62, NCI-H2347, …) | all doses, flat | low cells (technical?); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.71×** | +4.6 | 3e-04 | 32/49 (C32, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +4.5 | 3e-04 | 26/48 (MIA PaCa-2, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 0.05 µM |  | **1.31×** | +4.1 | 0.002 | 27/48 (A498, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Acetohexamide (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.005 | 23/48 (A498, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.010 | 24/48 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Valdecoxib (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.010 | 25/48 (PANC-1, A498, …) | inconsistent across doses | position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.015 | 25/48 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Menadione (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.077 | 17/48 (A498, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Olanzapine (drug)]] 5 µM |  | 1.14× | +2.9 | 0.091 | 4/48 (KATO III, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12165.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Acetohexamide (drug)]] 5 µM |  | **0.779×** | -5.7 | 6e-06 | 35/48 (SW480, HEC-1-A, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.796×** | -5.2 | 4e-05 | 26/48 (BT-474, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.803×** | -3.6 | 0.069 | 24/48 (HEC-1-A, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.810×** | -3.4 | 0.086 | 23/48 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.793×** | -3.3 | 0.098 | 22/50 (LoVo, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.867× | -3.3 | 0.098 | 18/48 (LoVo, RKO, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -3.1 | 0.16 | 0/50 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12165. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 120 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +8.5) | — |
| [[A549 (line)]] | wt | 80.1 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +14.7) | — |
| [[C32 (line)]] | wt | 50.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +13.9) | — |
| [[CFPAC-1 (line)]] | alt | 60.7 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +13.3) | — |
| [[HOP62 (line)]] | alt | 62.3 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +16.0) | — |
| [[HS-578T (line)]] | alt | 63.9 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +14.5) | — |
| [[NCI-H1792 (line)]] | alt | 47.2 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 110 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +15.2) | — |
| [[A-172 (line)]] | wt | 104 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +12.4) | — |
| [[A-427 (line)]] | wt | 107 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 78.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +13.6) | — |
| [[H4 (line)]] | wt | 137 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 151 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +13.6) | — |
| [[Hs 766T (line)]] | wt | 73.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 77.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +11.3) | — |
| [[J82 (line)]] | alt | 78.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 121 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 95.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 67.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +14.4) | — |
| [[SW 900 (line)]] | alt | 68.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.7) | — |
| [[SW480 (line)]] | alt | 112 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 126 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +17.4) | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 62.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +10.8) | — |
| [[KATO III (line)]] | alt | 131 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +10.0) | — |
| [[LoVo (line)]] | wt | 108 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 71.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 74.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 39.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +12.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 92.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 79.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +13.9) | — |
| [[Panc 03.27 (line)]] | alt | 84.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +13.9) | — |
| [[RKO (line)]] | wt | 66.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 80.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +11.6) | — |
| [[SW 1088 (line)]] | alt | 119 | 0 | 2 | — | [[Verapamil (drug)]] 0.5 µM 0.0678× (z -11.2) |
| [[C-33 A (line)]] | alt | 68.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 94.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 43.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 84.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 91.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.78× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 82.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +12.5) | — |
| [[SW48 (line)]] | wt | 108 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -10.1) |
| [[AN3 CA (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 75.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12165), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUMO3]] | +0.64 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CFL1]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 | pathway: Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; STRING 880 |
| [[RPSA]] | +0.61 | +0.62 / +0.58 | both halves | 7e-06 | pathway: SARS-CoV-1 Infection; STRING 451 |
| [[NIPBL-DT]] | +0.60 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[FADS2]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[GANAB]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 | pathway: SARS-CoV-1 Infection |
| [[RNPS1]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[ACLY]] | +0.59 | +0.53 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[U2AF2]] | +0.58 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[CTSZ]] | +0.58 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[SUV39H2]] | +0.58 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[HCFC1]] | +0.58 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBMX2]] | -0.70 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[TIPRL]] | -0.68 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.66 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.65 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[LIN7B]] | -0.64 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.62 | -0.55 / -0.58 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CAPN7]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[SEC62]] | -0.59 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[SAT2]] | -0.59 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[GPATCH11]] | -0.59 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[RP9]] | -0.59 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[NKAP]] | -0.59 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[ATF4]] | -0.58 | -0.45 / -0.63 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PPIA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.472). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.4, -11.9); signed map (-28.4, -41.1). **Vector** length 101, 27.8% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +18.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.8 | +4.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.6 | +5.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.2 | -0.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.6 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +0.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.4 | -5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.8 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -1.6 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl isomerase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,796,680-44,824,564 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CYPA |
| Gene groups (HGNC) | Cyclophilin peptidylprolyl isomerases |
| Hallmark sets | GLYCOLYSIS, MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 31 pathways, smallest: APOBEC3G mediated resistance to HIV-1 infection; Calcineurin activates NFAT; Integration of provirus |
| Matched by | ensembl_id |

**Function**, from UniProt [P62937](https://www.uniprot.org/uniprotkb/P62937) (Peptidyl-prolyl cis-trans isomerase A):

> Catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides. Exerts a strong chemotactic effect on leukocytes partly through activation of one of its membrane receptors BSG/CD147, initiating a signaling cascade that culminates in MAPK/ERK activation. Activates endothelial cells (ECs) in a pro-inflammatory manner by stimulating activation of NF-kappa-B and ERK, JNK and p38 MAP-kinases and by inducing expression of adhesion molecules including SELE and VCAM1. Induces …

**Summary**, from NCBI Gene [5478](https://www.ncbi.nlm.nih.gov/gene/5478):

> This gene encodes a member of the peptidyl-prolyl cis-trans isomerase (PPIase) family. PPIases catalyze the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and accelerate the folding of proteins. The encoded protein is a cyclosporin binding-protein and may play a role in cyclosporin A-mediated immunosuppression. The protein can also interact with several HIV proteins, including p55 gag, Vpr, and capsid protein, and has been shown to be necessary for the formation of …

**Accessions** — [HGNC:9253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9253) · Entrez [5478](https://www.ncbi.nlm.nih.gov/gene/5478) · UniProt [P62937](https://www.uniprot.org/uniprotkb/P62937) · Ensembl [ENSG00000196262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196262)

## Data

Gene col 12165: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12165); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12165, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12165]; `tensor/DDL_lfc|DDL_z.npy` [12165]; `embed/gene_vectors.npy` [12165]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12165 or target_col == 12165). Every well: [[PPIA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
