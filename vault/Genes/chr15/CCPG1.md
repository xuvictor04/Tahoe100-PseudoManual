---
symbol: "CCPG1"
type: "gene"
col: 15312
ensembl_id: "ENSG00000260916"
name: "cell cycle progression 1"
location: "15q21.3"
module: 63
arm: "+"
pooled_cpm: 105.42
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 28
n_dd_up_clean: 10
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# CCPG1

*cell cycle progression 1* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.88× (z +14.3, q 1e-43, up in 35 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.40× (z +7.7, q 2e-12, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.612× (z -15.8, q 0e+00, down in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.501× (z -15.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCEA1]] (+0.70, fdr 7e-06), [[CLGN]] (+0.67, fdr 7e-06), [[EPRS1]] (+0.65, fdr 7e-06); moves opposite to [[SNRPB]] (-0.54, fdr 1e-05), [[P2RY11]] (-0.52, fdr 3e-05), [[NOP56]] (-0.49, fdr 5e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LURAP1L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +14.3 | 1e-43 | 35/49 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +12.2 | 5e-32 | 31/43 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +8.5 | 3e-15 | 31/45 (SHP-77, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +7.7 | 2e-12 | 40/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.26×** | +7.4 | 2e-11 | 26/48 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.34×** | +6.7 | 1e-09 | 31/48 (BT-474, H4, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.23×** | +6.7 | 1e-09 | 24/48 (SNU-1, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.31×** | +6.1 | 7e-08 | 26/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +5.9 | 3e-07 | 25/48 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +5.0 | 3e-05 | 26/48 (A498, HEC-1-A, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +5.0 | 4e-05 | 14/48 (LoVo, NCI-H460, …) | two highest doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.24×** | +4.9 | 4e-05 | 21/48 (SNU-1, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.23×** | +4.7 | 1e-04 | 24/49 (C-33 A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.22×** | +4.6 | 2e-04 | 21/48 (LoVo, BT-474, …) | rises with dose |  |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **1.46×** | +4.5 | 2e-04 | 27/48 (RPMI-7951, A498, …) | top dose only | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.21×** | +4.3 | 6e-04 | 20/48 (C-33 A, BT-474, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.22×** | +4.3 | 6e-04 | 18/48 (HOP62, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +4.1 | 0.001 | 16/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.13× | +3.9 | 0.003 | 16/49 (SNU-1, NCI-H460, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.8 | 0.004 | 15/48 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +3.6 | 0.008 | 11/48 (AsPC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.008 | 14/49 (H4, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15312.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.612×** | -15.8 | 0e+00 | 35/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.501×** | -15.7 | 0e+00 | 47/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.505×** | -15.5 | 0e+00 | 43/48 (HT-29, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.513×** | -15.2 | 0e+00 | 36/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -13.9 | 5e-42 | 44/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.608×** | -11.3 | 1e-27 | 40/48 (SW 1088, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.609×** | -11.3 | 1e-27 | 44/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[EX229 (drug)]] 5 µM |  | **0.563×** | -6.8 | 5e-10 | 36/48 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.563×** | -6.8 | 5e-10 | 33/48 (A498, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.814×** | -6.6 | 3e-09 | 24/48 (SNU-1, PANC-1, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.601×** | -6.0 | 8e-08 | 33/47 (PANC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.608×** | -5.9 | 2e-07 | 25/49 (LoVo, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.771×** | -5.9 | 2e-07 | 27/48 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.763×** | -5.9 | 2e-07 | 26/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.708×** | -5.6 | 8e-07 | 27/48 (PANC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.627×** | -5.6 | 1e-06 | 26/48 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.818×** | -4.5 | 1e-04 | 23/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.804×** | -4.5 | 2e-04 | 24/48 (SW 900, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.687×** | -4.5 | 2e-04 | 22/48 (SW 900, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.709×** | -4.1 | 9e-04 | 21/48 (SW480, SHP-77, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 370 | 1 (1 ⚠) | 17 (10 ⚠) | [[Artesunate (drug)]] 5 µM 1.59× (z +9.2) ⚠ cell-cycle shift, explains ~14% of this change | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -18.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -17.3) |
| [[PANC-1 (line)]] | alt | 99.6 | 3 (3 ⚠) | 11 (7 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.84× (z +15.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -25.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -17.9) |
| [[HT-29 (line)]] | alt | 184 | 0 | 10 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 119 | 2 (1 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.52× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -20.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.333× (z -16.3) |
| [[NCI-H1792 (line)]] | alt | 205 | 1 (1 ⚠) | 8 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -20.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.488× (z -10.4) |
| [[SW480 (line)]] | alt | 58.9 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.36× (z +9.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.305× (z -13.4) |
| [[A498 (line)]] | wt | 134 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -20.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -17.9) |
| [[A549 (line)]] | wt | 112 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.57× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -17.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.369× (z -13.4) |
| [[KATO III (line)]] | alt | 145 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.170× (z -16.0) |
| [[SK-MEL-2 (line)]] | alt | 85.4 | 1 (1 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.67× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -16.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -9.8) |
| [[SNU-1 (line)]] | wt | 91.9 | 2 (1 ⚠) | 3 | [[Artesunate (drug)]] 5 µM 2.70× (z +11.6) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.52× (z +10.8) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.410× (z -10.3) |
| [[SW 900 (line)]] | alt | 134 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -11.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.481× (z -9.8) |
| [[SW1417 (line)]] | alt | 98.1 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.398× (z -9.4) |
| [[HOP62 (line)]] | alt | 39.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.70× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 99.9 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.53× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 66.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 223 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.29× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -25.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.411× (z -13.8) |
| [[RKO (line)]] | wt | 66.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -10.2) |
| [[A-172 (line)]] | wt | 118 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.457× (z -8.7) |
| [[C32 (line)]] | wt | 92.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -11.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -9.6) |
| [[J82 (line)]] | alt | 72.1 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.397× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 122 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H596 (line)]] | alt | 90.8 | 1 | 2 | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 2.25× (z +9.0) | [[Atazanavir (sulfate) (drug)]] 5 µM 0.153× (z -21.0) |
| [[SHP-77 (line)]] | alt | 58.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +15.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 176 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 67.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +10.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 56.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.364× (z -8.7) |
| [[LS 180 (line)]] | wt | 92.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 51.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.373× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 85.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -10.9) |
| [[SNU-423 (line)]] | alt | 67.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.53× (z +8.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.400× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 62.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +10.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 66.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.94× (z +9.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 99.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 61.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 44.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 49.0 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.02× (z +9.3) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[Panc 03.27 (line)]] | alt | 100 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.467× (z -8.5) |
| [[SW 1088 (line)]] | alt | 80.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0602× (z -9.9) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 117 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEA1]] | +0.70 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[CLGN]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[EPRS1]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[AARS1]] | +0.61 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ZFAND1]] | +0.59 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[MIA2]] | +0.58 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[RTN3]] | +0.57 | +0.50 / +0.60 | both halves | 1e-05 | STRING 794 |
| [[IDH1]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[AKTIP]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SARS1]] | +0.57 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ERP29]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CALCOCO2]] | +0.56 | +0.49 / +0.58 | both halves | 1e-05 | STRING 618 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[P2RY11]] | -0.52 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[NOP56]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 | same gene group |
| [[PRR7-AS1]] | -0.49 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[GEMIN4]] | -0.47 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[DUS2]] | -0.47 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[FBXW9]] | -0.45 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[POLR1C]] | -0.45 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[NIP7]] | -0.45 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[UBE2N]] | -0.45 | -0.32 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LURAP1L]] | B | LURAP1L activity raises CCPG1's level | lines that do not express LURAP1L (12) vs lines expressing it (38) | 1.65× lower at baseline in the lines without LURAP1L | 0.008 | ⚠ within organs, on part of the lines; also absent: KLF4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.8, 47.3); signed map (-15.0, 23.6). **Vector** length 136, 45.8% of its response variance represented; |z| ≥ 3 in 1,543 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.52 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.52 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +7.8 | +6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.2 | +7.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.9 | +6.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +5.7 | +4.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.6 | +7.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.5 | +5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.9 | +5.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +4.4 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -5.9 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -11.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | -5.2 | -6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -6.6 |
|  | [[EX229 (drug)]] 5 µM |  | -5.1 | -6.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -6.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | cell cycle progression 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:55,340,032-55,408,510 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1254, CPR8 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULG6](https://www.uniprot.org/uniprotkb/Q9ULG6) (Cell cycle progression protein 1):

> Acts as an assembly platform for Rho protein signaling complexes. Limits guanine nucleotide exchange activity of MCF2L toward RHOA, which results in an inhibition of both its transcriptional activation ability and its transforming activity. Does not inhibit activity of MCF2L toward CDC42, or activity of MCF2 toward either RHOA or CDC42 (By similarity). May be involved in cell cycle regulation.

**Summary**, from NCBI Gene [9236](https://www.ncbi.nlm.nih.gov/gene/9236):

> Involved in positive regulation of cell cycle and positive regulation of cell population proliferation. Acts upstream of or within reticulophagy. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24227](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24227) · Entrez [9236](https://www.ncbi.nlm.nih.gov/gene/9236) · UniProt [Q9ULG6](https://www.uniprot.org/uniprotkb/Q9ULG6) · Ensembl [ENSG00000260916](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260916)

## Data

Gene col 15312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15312); `tables/drug_effects.parquet` (79 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15312]; `tensor/DDL_lfc|DDL_z.npy` [15312]; `embed/gene_vectors.npy` [15312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15312 or target_col == 15312). Every well: [[CCPG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCPG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
