---
symbol: "DDIT3"
type: "gene"
col: 10578
ensembl_id: "ENSG00000175197"
name: "DNA damage inducible transcript 3"
location: "12q13.3"
module: 63
arm: "+"
pooled_cpm: 100.52
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# DDIT3

*DNA damage inducible transcript 3* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.98× (z +10.2, q 2e-21, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.286× (z -12.6, q 8e-34, down in 38 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.05 µM: 0.650× (z -4.5, q 7e-04, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BUD31]] (+0.74, fdr 7e-06), [[SESN2]] (+0.71, fdr 7e-06), [[GOT1]] (+0.69, fdr 9e-06); moves opposite to [[BTBD1]] (-0.61, fdr 1e-05), [[TMEM33]] (-0.58, fdr 1e-05), [[VMA21]] (-0.55, fdr 1e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ERICH2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10578.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +10.2 | 2e-21 | 38/48 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.46×** | +9.5 | 1e-18 | 44/48 (HEC-1-A, SW 900, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **1.57×** | +6.7 | 4e-09 | 44/48 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +5.6 | 2e-06 | 31/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +5.6 | 3e-06 | 34/48 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.65×** | +5.3 | 1e-05 | 40/48 (C32, SNU-1, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.40×** | +5.1 | 4e-05 | 33/49 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.9 | 5e-05 | 31/47 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.59×** | +4.9 | 7e-05 | 44/48 (NCI-H2030, Hs 766T, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.50×** | +4.3 | 0.001 | 34/48 (C-33 A, Panc 03.27, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.004 | 33/48 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.009 | 27/49 (Panc 03.27, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.018 | 29/47 (C32, SHP-77, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.90×** | +3.5 | 0.018 | 27/49 (NCI-H460, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.020 | 31/48 (BT-474, CHP-212, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.021 | 30/49 (SW480, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10578.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.286×** | -12.6 | 8e-34 | 38/43 (HT-29, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.423×** | -9.0 | 5e-17 | 41/49 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.459×** | -7.6 | 7e-12 | 36/45 (SNU-423, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.630×** | -4.7 | 4e-04 | 28/47 (SW1417, CHP-212, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.650×** | -4.5 | 7e-04 | 35/47 (LoVo, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.692×** | -3.9 | 0.011 | 25/48 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.774×** | -3.8 | 0.012 | 25/48 (SW 900, PANC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.508×** | -3.7 | 0.015 | 24/38 (HT-29, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.719×** | -3.5 | 0.034 | 26/48 (HCT15, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.730×** | -3.3 | 0.055 | 26/48 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.733×** | -3.3 | 0.057 | 23/48 (HT-29, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.739×** | -3.2 | 0.073 | 25/48 (LoVo, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.744×** | -3.1 | 0.082 | 21/48 (NCI-H460, NCI-H1573, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 128 | 1 | 6 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.70× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.152× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.330× (z -10.3) |
| [[HT-29 (line)]] | alt | 214 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0691× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.341× (z -9.5) |
| [[KATO III (line)]] | alt | 146 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -18.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 75.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +15.5) | — |
| [[SNU-423 (line)]] | alt | 178 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -17.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 130 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -15.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 84.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 262 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -19.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 62.1 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.97× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -8.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 101 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -12.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 59.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +15.0) | — |
| [[NCI-H1573 (line)]] | alt | 85.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.31× (z +19.4) | — |
| [[NCI-H23 (line)]] | alt | 126 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 88.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -13.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 103 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -9.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 129 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -10.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 97.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -11.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 79.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -10.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 88.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.95× (z +23.2) | — |
| [[C32 (line)]] | wt | 82.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +11.6) | — |
| [[CHP-212 (line)]] | wt | 55.8 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0988× (z -9.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -8.8) |
| [[COLO 205 (line)]] | alt | 168 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +14.3) | — |
| [[HCT15 (line)]] | alt | 135 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -13.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 83.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 87.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0860× (z -14.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 78.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +15.1) | — |
| [[NCI-H1792 (line)]] | alt | 332 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -12.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 43.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +11.5) | — |
| [[SNU-1 (line)]] | wt | 81.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.65× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.190× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 86.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.9) | — |
| [[SW48 (line)]] | wt | 101 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.59× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 49.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 35.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.48× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 83.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +16.8) | — |
| [[LOX-IMVI (line)]] | wt | 58.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +9.5) | — |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0945× (z -8.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 89.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.19× (z +8.8) | — |
| [[SW 1088 (line)]] | alt | 75.2 | 0 | 1 | — | [[Lopinavir (drug)]] 0.05 µM 0.0618× (z -8.5) |
| [[AN3 CA (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BUD31]] | +0.74 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[SESN2]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 | pathway: Cellular response to starvation; STRING 451 |
| [[GOT1]] | +0.69 | +0.57 / +0.72 | both halves | 9e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[IFRD1]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[HERPUD1]] | +0.67 | +0.59 / +0.70 | both halves | 7e-06 | pathway: ATF4 activates genes in response to endoplasmic reticulum  stress; STRING 602 |
| [[FAM53C]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[XBP1]] | +0.64 | +0.68 / +0.63 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 988 |
| [[RPAIN]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[SPSB2]] | +0.63 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[CHAC1]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 | pathway: Response of EIF2AK1 (HRI) to heme deficiency; STRING 466 |
| [[NUPR1]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 421 |
| [[TRIB3]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 931 |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTBD1]] | -0.61 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[VMA21]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[NUP42]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ANKRD52]] | -0.54 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.53 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[IDH3A]] | -0.53 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[LMNB2]] | -0.52 | -0.39 / -0.58 | both halves | 5e-05 | same gene group |
| [[GFM1]] | -0.52 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[TUBGCP4]] | -0.52 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[CAPRIN1]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[PPP2R1B]] | -0.52 | -0.40 / -0.56 | both halves | 5e-05 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERICH2]] | B | ERICH2 activity raises DDIT3's level | lines that do not express ERICH2 (11) vs lines expressing it (39) | 1.35× lower at baseline in the lines without ERICH2 | 0.070 | ⚠ within organs, on part of the lines; also absent: ERICH2-DT, DMBX1, GAD1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.5, -8.2); signed map (-11.5, 25.5). **Vector** length 158, 57.5% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +9.5 |
|  | [[Artesunate (drug)]] 5 µM |  | +8.9 | +6.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +5.9 | +5.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +5.6 | +4.9 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +5.5 | +5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.3 | +4.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.8 | -7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.5 | -12.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.3 | -3.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -8.1 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -7.9 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.5 | -1.1 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | DNA damage inducible transcript 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,516,588-57,521,737 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CHOP10, GADD153, CHOP |
| Gene groups (HGNC) | Basic leucine zipper proteins; MicroRNA protein coding host genes |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, APOPTOSIS, HYPOXIA, P53_PATHWAY, MTORC1_SIGNALING |
| Reactome | 12 pathways, smallest: ATF6 (ATF6-alpha) activates chaperone genes; ATF6 (ATF6-alpha) activates chaperones; FOXO-mediated transcription of cell death genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DPQ6](https://www.uniprot.org/uniprotkb/P0DPQ6) (DDIT3 upstream open reading frame protein):

> [Isoform AltDDIT3]: Product of the upstream open reading frame (uORF) of DDIT3/CHOP that is specifically produced in absence of stress, thereby preventing translation of downstream stress effector DDIT3/CHOP.

**Summary**, from NCBI Gene [1649](https://www.ncbi.nlm.nih.gov/gene/1649):

> This gene encodes a member of the CCAAT/enhancer-binding protein (C/EBP) family of transcription factors. The protein functions as a dominant-negative inhibitor by forming heterodimers with other C/EBP members, such as C/EBP and LAP (liver activator protein), and preventing their DNA binding activity. The protein is implicated in adipogenesis and erythropoiesis, is activated by endoplasmic reticulum stress, and promotes apoptosis. Fusion of this gene and FUS on chromosome 16 or EWSR1 on …

**Accessions** — [HGNC:2726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2726) · Entrez [1649](https://www.ncbi.nlm.nih.gov/gene/1649) · UniProt [P0DPQ6](https://www.uniprot.org/uniprotkb/P0DPQ6) · Ensembl [ENSG00000175197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175197)

## Data

Gene col 10578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10578); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10578]; `tensor/DDL_lfc|DDL_z.npy` [10578]; `embed/gene_vectors.npy` [10578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10578 or target_col == 10578). Every well: [[DDIT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDIT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
