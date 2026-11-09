---
symbol: "TRIM44"
type: "gene"
col: 9284
ensembl_id: "ENSG00000166326"
name: "TRIM family member 44"
location: "11p13"
module: 1
arm: "+"
pooled_cpm: 156.58
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TRIM44

*TRIM family member 44* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.81× (z +12.2, q 1e-31, up in 36 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.67× (z +11.0, q 8e-26, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.638× (z -9.7, q 2e-19, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TASOR]] (+0.71, fdr 7e-06), [[UTP20]] (+0.70, fdr 7e-06), [[SFPQ]] (+0.69, fdr 7e-06); moves opposite to [[KLHL7]] (-0.74, fdr 7e-06), [[LMBR1L]] (-0.74, fdr 7e-06), [[TULP3]] (-0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9284.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +12.2 | 1e-31 | 36/43 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +11.4 | 2e-27 | 42/48 (A-427, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +11.0 | 8e-26 | 37/47 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +8.5 | 3e-15 | 38/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +8.4 | 5e-15 | 35/44 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.07×** | +8.2 | 2e-14 | 38/47 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +7.9 | 3e-13 | 31/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +6.7 | 1e-09 | 0/49 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +5.9 | 2e-07 | 38/47 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +5.7 | 6e-07 | 31/47 (NCI-H2347, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.33×** | +5.6 | 1e-06 | 38/46 (HS-578T, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +5.1 | 2e-05 | 31/47 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.6 | 2e-04 | 27/47 (NCI-H2347, HT-29, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.3 | 8e-04 | 24/46 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +4.2 | 9e-04 | 25/47 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.001 | 27/47 (NCI-H2347, SHP-77, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +4.0 | 0.002 | 13/47 (NCI-H2347, AsPC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.013 | 22/47 (NCI-H2347, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.022 | 21/47 (NCI-H2347, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.073 | 8/47 (J82, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9284.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.638×** | -9.7 | 2e-19 | 42/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.648×** | -9.4 | 2e-18 | 39/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.758×** | -8.5 | 4e-15 | 31/48 (SW48, RKO, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.705×** | -7.6 | 6e-12 | 36/47 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.736×** | -6.6 | 4e-09 | 32/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.768×** | -5.5 | 4e-06 | 27/46 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.815× | -3.2 | 0.13 | 19/47 (SW 1271, SW 1088, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.868× | -3.1 | 0.15 | 19/47 (A498, KATO III, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9284. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 123 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +16.0) | — |
| [[NCI-H460 (line)]] | wt | 114 | 7 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +20.7) | [[Panobinostat (drug)]] 0.5 µM 0.542× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 186 | 4 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.05× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 3.37× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.535× (z -10.7) |
| [[HT-29 (line)]] | alt | 238 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +14.2) | [[Panobinostat (drug)]] 0.5 µM 0.501× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 143 | 4 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.95× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.547× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[NCI-H23 (line)]] | alt | 179 | 0 | 5 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.434× (z -11.6) |
| [[PANC-1 (line)]] | alt | 186 | 1 (1 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.78× (z +10.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.544× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 198 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 1.99× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.650× (z -8.6) |
| [[A-172 (line)]] | wt | 150 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +11.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -11.5) |
| [[HOP62 (line)]] | alt | 116 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 356 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 147 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +9.9) | [[Belinostat (drug)]] 5 µM 0.297× (z -15.8) |
| [[RKO (line)]] | wt | 315 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -12.1) |
| [[A498 (line)]] | wt | 198 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.478× (z -11.6) |
| [[J82 (line)]] | alt | 206 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.95× (z +9.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -8.9) |
| [[LoVo (line)]] | wt | 131 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.96× (z +8.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.372× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.510× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 111 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +11.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 159 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 151 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 4.21× (z +9.2) | — |
| [[A-427 (line)]] | wt | 68.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +12.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.424× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 77.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 138 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +15.5) | — |
| [[C32 (line)]] | wt | 164 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 2.19× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -8.8) |
| [[HS-578T (line)]] | alt | 108 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +9.3) | — |
| [[KATO III (line)]] | alt | 123 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.339× (z -11.0) |
| [[SW48 (line)]] | wt | 127 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -15.4) |
| [[SW480 (line)]] | alt | 176 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.502× (z -11.1) |
| [[A549 (line)]] | wt | 130 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.0) |
| [[Hs 766T (line)]] | wt | 147 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +19.3) | — |
| [[NCI-H2030 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[SK-MEL-2 (line)]] | alt | 254 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.90× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 304 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 70.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 125 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 77.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 121 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 114 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 190 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9284), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TASOR]] | +0.71 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[UTP20]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[SFPQ]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[EWSR1]] | +0.69 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[ABCE1]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[EIF4G1]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[TMEM185B]] | +0.69 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[COMMD10]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[SRFBP1]] | +0.67 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[YWHAE]] | +0.67 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SNX19]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.66 | +0.65 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL7]] | -0.74 | -0.60 / -0.72 | both halves | 7e-06 |  |
| [[LMBR1L]] | -0.74 | -0.71 / -0.69 | both halves | 7e-06 |  |
| [[TULP3]] | -0.72 | -0.70 / -0.69 | both halves | 7e-06 |  |
| [[SDHAP2]] | -0.70 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[VKORC1]] | -0.70 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[CBFA2T2]] | -0.70 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[MPG]] | -0.70 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.69 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[RAB40C]] | -0.69 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[CARD19]] | -0.68 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | -0.67 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[QPCTL]] | -0.67 | -0.63 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TRIM44's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TBCEL]] | C | TBCEL activity raises TRIM44's level | lines that do not express TBCEL (4) vs lines expressing it (46) | 1.99× lower at baseline in the lines without TBCEL | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: C2orf92, HHAT, RUNDC3A-AS1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.652). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.9, -15.5); signed map (14.3, -39.3). **Vector** length 151, 49.7% of its response variance represented; |z| ≥ 3 in 1,164 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.1 | +12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.1 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.9 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.2 | +8.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +7.4 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.7 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.3 | +8.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.9 | +5.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.8 | -9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | -5.5 | -5.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.5 | -6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -7.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.0 | -0.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.6 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.6 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | TRIM family member 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:35,662,775-35,818,007 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DIPB, MC7 |
| Gene groups (HGNC) | Tripartite motif family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DX7](https://www.uniprot.org/uniprotkb/Q96DX7) (Tripartite motif-containing protein 44):

> May play a role in the process of differentiation and maturation of neuronal cells (By similarity). May regulate the activity of TRIM17. Is a negative regulator of PAX6 expression.

**Summary**, from NCBI Gene [54765](https://www.ncbi.nlm.nih.gov/gene/54765):

> This gene encodes a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, namely a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19016](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19016) · Entrez [54765](https://www.ncbi.nlm.nih.gov/gene/54765) · UniProt [Q96DX7](https://www.uniprot.org/uniprotkb/Q96DX7) · Ensembl [ENSG00000166326](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166326)

## Data

Gene col 9284: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9284); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9284, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9284]; `tensor/DDL_lfc|DDL_z.npy` [9284]; `embed/gene_vectors.npy` [9284]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9284 or target_col == 9284). Every well: [[TRIM44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
