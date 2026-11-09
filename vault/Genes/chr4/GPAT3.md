---
symbol: "GPAT3"
type: "gene"
col: 6213
ensembl_id: "ENSG00000138678"
name: "glycerol-3-phosphate acyltransferase 3"
location: "4q21.23"
module: 136
arm: "+"
pooled_cpm: 78.41
n_lines_expressing: 43
n_dd_up: 38
n_dd_down: 32
n_dd_up_clean: 31
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# GPAT3

*glycerol-3-phosphate acyltransferase 3* — 4q21.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.88× (z +9.5, q 8e-19, up in 29 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.596× (z -11.0, q 3e-25, down in 26 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX1A]] (+0.61, fdr 7e-06), [[S100A16]] (+0.60, fdr 1e-05), [[SH3KBP1]] (+0.59, fdr 1e-05); moves opposite to [[ZNF608]] (-0.58, fdr 1e-05), [[STAG2]] (-0.51, fdr 4e-05), [[HDGF]] (-0.50, fdr 4e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSD3]] → it (grade B ⚠); 2 go from it, the strongest it → [[LUCAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6213.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.88×** | +9.5 | 8e-19 | 29/41 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.81×** | +9.0 | 9e-17 | 31/41 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +8.3 | 2e-14 | 25/41 (COLO 205, AsPC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +8.1 | 8e-14 | 29/41 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +7.6 | 2e-12 | 31/41 (NCI-H1573, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +7.5 | 7e-12 | 26/41 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +7.5 | 7e-12 | 29/41 (NCI-H1573, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.39×** | +7.1 | 9e-11 | 25/42 (SW480, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.57×** | +6.5 | 5e-09 | 29/40 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.79×** | +6.3 | 2e-08 | 31/41 (PANC-1, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.46×** | +5.7 | 5e-07 | 26/40 (NCI-H460, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[EX229 (drug)]] 0.5 µM |  | **1.61×** | +5.1 | 1e-05 | 24/42 (PANC-1, LoVo, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +5.0 | 3e-05 | 23/40 (NCI-H1573, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +4.9 | 4e-05 | 24/40 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.8 | 5e-05 | 24/40 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.38×** | +4.7 | 7e-05 | 17/40 (COLO 205, KATO III, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.52×** | +4.5 | 2e-04 | 17/41 (PANC-1, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.77×** | +4.5 | 2e-04 | 20/41 (LoVo, HT-29, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6213.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.596×** | -11.0 | 3e-25 | 26/41 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.470×** | -10.9 | 3e-25 | 27/35 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -7.3 | 7e-11 | 26/42 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.618×** | -7.2 | 8e-11 | 28/39 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.685×** | -6.7 | 3e-09 | 31/41 (HOP62, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.730×** | -6.6 | 3e-09 | 27/41 (HT-29, A549, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.658×** | -6.6 | 4e-09 | 28/43 (HOP62, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.634×** | -6.6 | 4e-09 | 24/41 (SK-MEL-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.670×** | -6.0 | 1e-07 | 23/41 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -5.6 | 9e-07 | 6/43 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.690×** | -5.6 | 1e-06 | 26/41 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.715×** | -5.0 | 2e-05 | 24/42 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.710×** | -4.9 | 4e-05 | 27/41 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.758×** | -4.7 | 1e-04 | 21/42 (SW48, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.725×** | -4.6 | 1e-04 | 21/40 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.772×** | -4.6 | 2e-04 | 22/41 (SW48, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.806×** | -4.5 | 2e-04 | 19/41 (HOP62, AsPC-1, …) | all doses, stronger at high dose |  |
| [[IQ 1 (drug)]] 5 µM |  | **0.614×** | -3.8 | 0.004 | 15/40 (SHP-77, SW48, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6213. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 162 | 2 | 9 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.74× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -17.7) |
| [[SW48 (line)]] | wt | 147 | 6 (1 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 6.41× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 6.31× (z +10.3) | [[Trametinib (drug)]] 5 µM 0.190× (z -9.8) |
| [[C32 (line)]] | wt | 123 | 5 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.69× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -14.4) |
| [[HOP62 (line)]] | alt | 58.0 | 2 | 6 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.81× (z +9.2) | [[Adagrasib (drug)]] 0.05 µM 0.430× (z -21.5) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.8) |
| [[COLO 205 (line)]] | alt | 32.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 16.1× (z +14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 6.88× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 201 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.19× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 5.17× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 97.7 | 1 (1 ⚠) | 6 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.84× (z +8.8) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.173× (z -14.1) |
| [[HT-29 (line)]] | alt | 74.4 | 4 (1 ⚠) | 2 | [[Bortezomib (drug)]] 0.05 µM 4.09× (z +10.8) | [[Selinexor (drug)]] 5 µM 0.365× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 313 | 0 | 6 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.529× (z -19.9) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -19.2) |
| [[PANC-1 (line)]] | alt | 86.9 | 1 (1 ⚠) | 5 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.25× (z +9.0) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -16.0) |
| [[A498 (line)]] | wt | 110 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -13.1) |
| [[A549 (line)]] | wt | 90.0 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 98.9 | 3 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.60× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.368× (z -8.8) |
| [[H4 (line)]] | wt | 116 | 1 | 3 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.57× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -14.2) |
| [[KATO III (line)]] | alt | 62.1 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.57× (z +10.9) | — |
| [[LoVo (line)]] | wt | 84.3 | 4 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.48× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 79.9 | 1 (1 ⚠) | 3 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.34× (z +9.8) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.307× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.461× (z -9.3) |
| [[SW480 (line)]] | alt | 36.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.30× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 44.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 180 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -12.7) |
| [[LS 180 (line)]] | wt | 36.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.48× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 151 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 44.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.6) |
| [[SW 900 (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.408× (z -8.9) |
| [[A-427 (line)]] | wt | 45.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.23× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[BT-474 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0731× (z -10.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.12× (z +9.1) ⚠ unreliable plate only | — |
| [[HepG2_C3A (line)]] | wt | 61.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.66× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.623× (z -10.1) ⚠ position not correctable |
| [[SNU-423 (line)]] | alt | 36.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +8.5) | — |
| [[SW 1088 (line)]] | alt | 80.6 | 0 | 1 | — | [[Rucaparib (phosphate) (drug)]] 0.5 µM 0.0502× (z -9.5) |
| [[A-172 (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.08 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 68.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6213), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX1A]] | +0.61 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[S100A16]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[SH3KBP1]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PFDN2]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[UCHL3]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ARID3B]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.56 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[C6orf141]] | +0.56 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SH3BGRL3]] | +0.55 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[ZNF83]] | +0.55 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[BMERB1]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF608]] | -0.58 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[STAG2]] | -0.51 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[HDGF]] | -0.50 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[CPNE1]] | -0.50 | -0.60 / -0.38 | both halves | 7e-05 | pathway: Glycerophospholipid biosynthesis |
| [[MAT2B]] | -0.50 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[MUC1]] | -0.49 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[CILK1]] | -0.48 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[SLC39A1]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SHROOM3]] | -0.48 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[PCM1]] | -0.48 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[NFIX]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[JADE2]] | -0.48 | -0.48 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSD3]] | B | PSD3 activity raises GPAT3's level | lines that do not express PSD3 (13) vs lines expressing it (37) | 2.82× lower at baseline in the lines without PSD3 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| [[LUCAT1]] | B | LUCAT1 activity raises GPAT3's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 2.45× lower at baseline in the lines without LUCAT1 | 0.025 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LUCAT1]] | B | GPAT3 activity raises LUCAT1's level | lines that do not express GPAT3 (7) vs lines expressing it (43) | 2.51× lower at baseline in the lines without GPAT3 | 0.060 | ⚠ within organs, on part of the lines; also absent: HLA-H, ABCA5, ISG20; maybe low, not absent; its own permutation p |
| [[AMOTL1]] | B | GPAT3 activity lowers AMOTL1's level | lines that do not express GPAT3 (7) vs lines expressing it (43) | 1.47× higher at baseline in the lines without GPAT3 | 0.060 | ⚠ within organs, on part of the lines; also absent: HLA-H, ABCA5, ISG20; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.2, 4.1); signed map (-2.0, 47.5). **Vector** length 133, 42.1% of its response variance represented; |z| ≥ 3 in 1,623 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.1 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +8.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.6 | +5.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | +4.2 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.3 | -11.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -6.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -5.2 | -5.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.4 | -4.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.2 | -6.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -6.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -5.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.8 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | glycerol-3-phosphate acyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.23 — chr4:83,535,914-83,605,875 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11324, LPAAT-theta, MAG1, HMFN0839, AGPAT10; previously AGPAT9 |
| Gene groups (HGNC) | 1-acylglycerol-3-phosphate O-acyltransferases; Glycerol-3-phosphate acyltransferases |
| Reactome | 4 pathways, smallest: Synthesis of PA; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53EU6](https://www.uniprot.org/uniprotkb/Q53EU6) (Glycerol-3-phosphate acyltransferase 3):

> Converts glycerol-3-phosphate to 1-acyl-sn-glycerol-3-phosphate (lysophosphatidic acid or LPA) by incorporating an acyl moiety at the sn-1 position of the glycerol backbone. Also converts LPA into 1,2-diacyl-sn-glycerol-3-phosphate (phosphatidic acid or PA) by incorporating an acyl moiety at the sn-2 position of the glycerol backbone. Protects cells against lipotoxicity.

**Summary**, from NCBI Gene [84803](https://www.ncbi.nlm.nih.gov/gene/84803):

> This gene encodes a member of the lysophosphatidic acid acyltransferase protein family. The encoded protein is an enzyme which catalyzes the conversion of glycerol-3-phosphate to lysophosphatidic acid in the synthesis of triacylglycerol. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:28157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28157) · Entrez [84803](https://www.ncbi.nlm.nih.gov/gene/84803) · UniProt [Q53EU6](https://www.uniprot.org/uniprotkb/Q53EU6) · Ensembl [ENSG00000138678](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138678)

## Data

Gene col 6213: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6213); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6213, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6213]; `tensor/DDL_lfc|DDL_z.npy` [6213]; `embed/gene_vectors.npy` [6213]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6213 or target_col == 6213). Every well: [[GPAT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPAT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
