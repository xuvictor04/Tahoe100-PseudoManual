---
symbol: "MARS1"
type: "gene"
col: 9400
ensembl_id: "ENSG00000166986"
name: "methionyl-tRNA synthetase 1"
location: "12q13.3"
module: 63
arm: "+"
pooled_cpm: 98.34
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 21
n_dd_up_clean: 32
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# MARS1

*methionyl-tRNA synthetase 1* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (10 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 2.33× (z +13.8, q 9e-41, up in 44 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Neratinib (maleate) (drug)]] 0.5 µM: 1.88× (z +10.7, q 3e-24, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.631× (z -11.2, q 3e-26, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AARS1]] (+0.90, fdr 7e-06), [[YARS1]] (+0.88, fdr 7e-06), [[PSAT1]] (+0.87, fdr 7e-06); moves opposite to [[IFNAR1]] (-0.48, fdr 3e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.33×** | +13.8 | 9e-41 | 44/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.88×** | +10.7 | 3e-24 | 47/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.54×** | +10.4 | 6e-23 | 45/48 (C32, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.83×** | +10.0 | 2e-21 | 43/48 (LOX-IMVI, SW 900, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +8.8 | 1e-16 | 40/48 (LOX-IMVI, C32, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.40×** | +8.1 | 6e-14 | 35/49 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.61×** | +8.0 | 8e-14 | 42/48 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.39×** | +7.9 | 1e-13 | 38/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.33×** | +6.9 | 3e-10 | 32/49 (SNU-1, Hs 766T, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **2.15×** | +6.8 | 6e-10 | 41/48 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.49×** | +6.7 | 8e-10 | 35/48 (C32, SNU-1, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.42×** | +5.9 | 1e-07 | 30/47 (C32, SNU-1, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.41×** | +5.8 | 2e-07 | 28/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.40×** | +5.7 | 4e-07 | 31/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +5.7 | 4e-07 | 36/49 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.39×** | +5.6 | 6e-07 | 29/48 (Hs 766T, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.83×** | +5.3 | 3e-06 | 29/48 (SW480, LOX-IMVI, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9400.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.631×** | -11.2 | 3e-26 | 38/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.786×** | -5.8 | 1e-06 | 24/48 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.723×** | -5.6 | 5e-06 | 33/47 (SW 1271, H4, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.707×** | -5.5 | 5e-06 | 31/47 (LoVo, H4, …) | all doses, flat | low cells (technical?) |
| [[AZD-8055 (drug)]] 5 µM |  | **0.559×** | -5.2 | 2e-05 | 36/49 (J82, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.742×** | -5.1 | 3e-05 | 24/48 (HS-578T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **0.747×** | -5.0 | 5e-05 | 32/49 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.672×** | -4.9 | 9e-05 | 31/48 (J82, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.823×** | -4.8 | 1e-04 | 25/48 (KATO III, HS-578T, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.762×** | -4.7 | 2e-04 | 24/48 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.789×** | -4.1 | 0.002 | 23/49 (RPMI-7951, SW480, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.849× | -4.0 | 0.003 | 26/49 (SNU-1, PANC-1, …) | top dose only |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.799×** | -3.9 | 0.005 | 19/48 (HS-578T, SNU-423, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.800×** | -3.8 | 0.005 | 21/49 (NCI-H2030, RKO, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.806×** | -3.7 | 0.008 | 21/48 (HT-29, A-427, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.685×** | -3.4 | 0.023 | 17/50 (HS-578T, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.023 | 16/48 (RKO, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 199 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -19.6) |
| [[A-427 (line)]] | wt | 233 | 1 | 9 (5 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.59× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -18.0) |
| [[LoVo (line)]] | wt | 167 | 1 (1 ⚠) | 8 (5 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.17× (z +14.0) ⚠ toxic | [[Harringtonine (drug)]] 0.5 µM 0.306× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.443× (z -14.6) |
| [[SNU-1 (line)]] | wt | 149 | 2 | 5 (3 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.50× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.0917× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.249× (z -16.0) |
| [[SW1417 (line)]] | alt | 111 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -14.3) |
| [[HT-29 (line)]] | alt | 143 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -19.6) |
| [[LOX-IMVI (line)]] | wt | 71.1 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.06× (z +10.9) | — |
| [[C32 (line)]] | wt | 44.7 | 4 (1 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 2.91× (z +11.0) | — |
| [[H4 (line)]] | wt | 94.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 72.7 | 4 (1 ⚠) | 0 | [[Neratinib (maleate) (drug)]] 5 µM 2.13× (z +9.8) | — |
| [[SW480 (line)]] | alt | 108 | 3 (1 ⚠) | 1 | [[PH-797804 (drug)]] 5 µM 4.40× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.635× (z -8.5) |
| [[A498 (line)]] | wt | 118 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.493× (z -12.8) |
| [[SW48 (line)]] | wt | 203 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.445× (z -9.3) |
| [[A-172 (line)]] | wt | 70.3 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.496× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 58.1 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 5.29× (z +13.0) ⚠ toxic | [[Selinexor (drug)]] 5 µM 0.457× (z -9.0) |
| [[Hs 766T (line)]] | wt | 44.0 | 2 (1 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.59× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 89.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 146 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.44× (z +9.0) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 69.9 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.30× (z +10.0) ⚠ toxic · without an alert: [[5-Azacytidine (drug)]] 5 µM 3.00× (z +9.5) | — |
| [[A549 (line)]] | wt | 62.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[C-33 A (line)]] | alt | 106 | 1 | 0 | [[5-Azacytidine (drug)]] 5 µM 2.84× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 49.9 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 9.89× (z +15.1) ⚠ toxic | — |
| [[HCT15 (line)]] | alt | 63.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.69× (z +9.4) ⚠ toxic | — |
| [[HepG2_C3A (line)]] | wt | 103 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.98× (z +10.6) ⚠ toxic | — |
| [[HOP62 (line)]] | alt | 34.8 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.18× (z +11.1) ⚠ toxic | — |
| [[J82 (line)]] | alt | 82.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.562× (z -10.2) |
| [[KATO III (line)]] | alt | 77.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.344× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 96.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.397× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 54.7 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.39× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 138 | 1 | 0 | [[Neratinib (maleate) (drug)]] 0.5 µM 2.72× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 172 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.9) |
| [[RKO (line)]] | wt | 127 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.61× (z +8.5) ⚠ toxic | — |
| [[SNU-423 (line)]] | alt | 39.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[SW 1271 (line)]] | alt | 99.6 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0735× (z -11.3) |
| [[SW 900 (line)]] | alt | 75.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.88× (z +9.0) ⚠ unreliable plate only | — |
| [[AN3 CA (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AARS1]] | +0.90 | +0.89 / +0.88 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 913 |
| [[YARS1]] | +0.88 | +0.88 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 999 |
| [[PSAT1]] | +0.87 | +0.89 / +0.85 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 520 |
| [[CARS1]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 890 |
| [[ASNS]] | +0.86 | +0.85 / +0.84 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 653 |
| [[IARS1]] | +0.85 | +0.86 / +0.83 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 999 |
| [[GARS1]] | +0.84 | +0.84 / +0.82 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 927 |
| [[XPOT]] | +0.84 | +0.84 / +0.82 | both halves | 7e-06 | STRING 655 |
| [[CHAC1]] | +0.83 | +0.79 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[SARS1]] | +0.83 | +0.84 / +0.79 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 895 |
| [[PHGDH]] | +0.82 | +0.83 / +0.79 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives |
| [[TARS1]] | +0.82 | +0.83 / +0.80 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 881 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFNAR1]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises MARS1's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds |
| [[ASNSP1]] | B | ASNSP1 activity raises MARS1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.45× lower at baseline in the lines without ASNSP1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[ANK2]] | B | ANK2 activity raises MARS1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.34× lower at baseline in the lines without ANK2 | 0.075 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[TRIB3]] | C | TRIB3's natural level weakens MARS1's drug response | TRIB3's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.24; direction not clear | 0.061 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.888). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.2, 47.8); signed map (-13.4, 24.3). **Vector** length 160, 58.7% of its response variance represented; |z| ≥ 3 in 1,661 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.75 to 16); *mTORC1 signaling* (hallmark, mean cos +0.66 to 20); *unfolded protein response* (hallmark, mean cos +0.77 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.8 | +10.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +9.6 | +8.0 |
|  | [[Artesunate (drug)]] 5 µM |  | +9.2 | +10.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +9.2 | +13.8 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +9.2 | +10.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +8.7 | +7.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +6.8 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.7 | +4.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +6.6 | +6.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.2 | -11.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.3 | -2.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.9 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -5.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.4 | -5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -6.2 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -3.7 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -3.6 | -4.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.5 | -5.6 |
|  | [[4EGI-1 (drug)]] 5 µM |  | -3.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | methionyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,475,445-57,517,569 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MetRS, SPG70, CMT2U; previously MARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I; MicroRNA protein coding host genes |
| Reactome | 7 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Transcriptional and post-translational regulation of MITF-M expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [P56192](https://www.uniprot.org/uniprotkb/P56192) (Methionine--tRNA ligase, cytoplasmic):

> Catalyzes the specific attachment of L-methionine to its cognate tRNA in a 2 step reaction: the amino acid (AA) is first activated by ATP to form AA-AMP and then transferred to the acceptor end of the tRNA. Plays a role in the synthesis of ribosomal RNA in the nucleolus. In addition, can prevent the misincorporation of homocysteine into tRNA and protein by catalyzing a tRNA-independent hydrolysis of the misactivated homocysteinyl-AMP intermediate. The homocysteinyl-AMP intermediate undergoes an …

**Summary**, from NCBI Gene [4141](https://www.ncbi.nlm.nih.gov/gene/4141):

> This gene encodes a member of the class I family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. The encoded protein is a component of the multi-tRNA synthetase complex and catalyzes the ligation of methionine to tRNA molecules. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:6898](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6898) · Entrez [4141](https://www.ncbi.nlm.nih.gov/gene/4141) · UniProt [P56192](https://www.uniprot.org/uniprotkb/P56192) · Ensembl [ENSG00000166986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166986)

## Data

Gene col 9400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9400); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9400]; `tensor/DDL_lfc|DDL_z.npy` [9400]; `embed/gene_vectors.npy` [9400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9400 or target_col == 9400). Every well: [[MARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
