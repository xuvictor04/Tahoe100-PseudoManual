---
symbol: "PYCR1"
type: "gene"
col: 11355
ensembl_id: "ENSG00000183010"
name: "pyrroline-5-carboxylate reductase 1"
location: "17q25.3"
module: 63
arm: "+"
pooled_cpm: 18.88
n_lines_expressing: 48
n_dd_up: 22
n_dd_down: 23
n_dd_up_clean: 15
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# PYCR1

*pyrroline-5-carboxylate reductase 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.27× (z +18.1, q 0e+00, up in 27 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 2.65× (z +5.8, q 8e-07, up in 31 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.555× (z -9.4, q 3e-18, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XPOT]] (+0.75, fdr 7e-06), [[IARS1]] (+0.73, fdr 7e-06), [[AARS1]] (+0.70, fdr 7e-06); moves opposite to [[TOPORS]] (-0.56, fdr 2e-05), [[WBP4]] (-0.52, fdr 8e-05), [[IFNAR1]] (-0.49, fdr 5e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CTH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11355.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.27×** | +18.1 | 0e+00 | 27/27 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.85×** | +17.9 | 0e+00 | 36/37 (KATO III, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +9.7 | 4e-20 | 31/34 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.74×** | +6.0 | 2e-07 | 33/45 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.65×** | +5.8 | 8e-07 | 31/45 (SW480, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +5.7 | 1e-06 | 8/46 (A-172, C-33 A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.2 | 2e-05 | 24/42 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **2.23×** | +4.8 | 1e-04 | 23/42 (NCI-H2030, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +4.5 | 5e-04 | 24/42 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[TAK-733 (drug)]] 5 µM |  | **2.05×** | +4.3 | 0.001 | 21/44 (MIA PaCa-2, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.001 | 22/46 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.03×** | +4.2 | 0.001 | 17/43 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 0.001 | 21/44 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.001 | 19/44 (NCI-H460, SHP-77, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.014 | 18/46 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.49×** | +3.2 | 0.043 | 14/45 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +3.2 | 0.043 | 11/44 (HCT15, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.053 | 12/45 (LoVo, HEC-1-A, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.060 | 12/44 (MIA PaCa-2, NCI-H1573, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.068 | 10/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.077 | 12/41 (PANC-1, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **1.64×** | +2.9 | 0.085 | 8/43 (LS 180, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11355.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.555×** | -9.4 | 3e-18 | 32/45 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.497×** | -7.9 | 7e-13 | 30/45 (KATO III, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.565×** | -6.4 | 2e-08 | 31/46 (A-172, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.618×** | -5.4 | 8e-06 | 24/44 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.642×** | -5.0 | 6e-05 | 23/44 (SW48, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.668×** | -4.6 | 5e-04 | 25/46 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.675×** | -4.3 | 0.002 | 22/45 (LoVo, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -4.0 | 0.004 | 22/45 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.783×** | -3.9 | 0.006 | 23/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.680×** | -3.7 | 0.010 | 20/43 (hTERT-HPNE, LS 180, …) | all doses, flat | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.705×** | -3.7 | 0.010 | 24/45 (BT-474, RPMI-7951, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.726×** | -3.5 | 0.023 | 16/44 (HOP62, A549, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.805×** | -3.5 | 0.023 | 22/46 (hTERT-HPNE, KATO III, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.560×** | -3.4 | 0.024 | 13/43 (SNU-1, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.565×** | -3.4 | 0.028 | 16/46 (RKO, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.816×** | -3.2 | 0.039 | 18/46 (KATO III, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.754×** | -3.2 | 0.047 | 14/44 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 48.7 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -20.9) |
| [[LoVo (line)]] | wt | 20.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +10.2) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.142× (z -12.1) |
| [[PANC-1 (line)]] | alt | 43.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -13.2) |
| [[A498 (line)]] | wt | 45.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.333× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 17.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.54× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 30.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.06× (z +12.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 23.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.01× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -12.0) |
| [[SW48 (line)]] | wt | 25.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0868× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -10.5) |
| [[SW480 (line)]] | alt | 18.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.41× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 11.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 26.6× (z +13.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 28.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.19× (z +10.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 15.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 18.7× (z +14.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 17.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -14.9) |
| [[NCI-H2030 (line)]] | alt | 19.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 21.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.06× (z +11.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 24.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -9.4) |
| [[BT-474 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -13.6) |
| [[H4 (line)]] | wt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -11.1) |
| [[HOP62 (line)]] | alt | 6.75 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0382× (z -12.9) |
| [[J82 (line)]] | alt | 9.48 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 6.02 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.5× (z +9.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 9.81 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.64× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 10.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.33× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -14.7) |
| [[Panc 03.27 (line)]] | alt | 8.46 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.3× (z +10.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 9.78 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0729× (z -8.5) |
| [[SHP-77 (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 21.3× (z +13.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 25.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPOT]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[IARS1]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives |
| [[AARS1]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[MTHFD2]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 | STRING 489 |
| [[SLC1A5]] | +0.69 | +0.75 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_XENOBIOTIC_METABOLISM; STRING 406 |
| [[PSAT1]] | +0.69 | +0.68 / +0.64 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 596 |
| [[ASNS]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 543 |
| [[GARS1]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[PHGDH]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 489 |
| [[EPRS1]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 421 |
| [[MARS1]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives |
| [[GFPT1]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOPORS]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[WBP4]] | -0.52 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[IFNAR1]] | -0.49 | -0.40 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTH]] | B | CTH activity raises PYCR1's level | lines that do not express CTH (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without CTH | 0.015 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |
| [[CHAC1]] | B | CHAC1 activity raises PYCR1's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 2.55× lower at baseline in the lines without CHAC1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.0, 47.8); signed map (-14.2, 25.0). **Vector** length 99.3, 25.2% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.58 to 16); *mTORC1 signaling* (hallmark, mean cos +0.56 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.64 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.5 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +18.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.8 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +17.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +9.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.1 | +5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.6 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.3 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -3.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | pyrroline-5-carboxylate reductase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,932,384-81,942,412 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P5C |
| Gene groups (HGNC) | Pyrroline-5-carboxylate reductase family |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 2 pathways, smallest: Glutamate and glutamine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P32322](https://www.uniprot.org/uniprotkb/P32322) (Pyrroline-5-carboxylate reductase 1, mitochondrial):

> Oxidoreductase that catalyzes the last step in proline biosynthesis, which corresponds to the reduction of pyrroline-5-carboxylate to L-proline using NAD(P)H. At physiologic concentrations, has higher specific activity in the presence of NADH. Involved in the cellular response to oxidative stress.

**Summary**, from NCBI Gene [5831](https://www.ncbi.nlm.nih.gov/gene/5831):

> This gene encodes an enzyme that catalyzes the NAD(P)H-dependent conversion of pyrroline-5-carboxylate to proline. This enzyme may also play a physiologic role in the generation of NADP(+) in some cell types. The protein forms a homopolymer and localizes to the mitochondrion. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:9721](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9721) · Entrez [5831](https://www.ncbi.nlm.nih.gov/gene/5831) · UniProt [P32322](https://www.uniprot.org/uniprotkb/P32322) · Ensembl [ENSG00000183010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183010)

## Data

Gene col 11355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11355); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11355]; `tensor/DDL_lfc|DDL_z.npy` [11355]; `embed/gene_vectors.npy` [11355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11355 or target_col == 11355). Every well: [[PYCR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PYCR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
