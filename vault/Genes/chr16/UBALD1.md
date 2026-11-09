---
symbol: "UBALD1"
type: "gene"
col: 7722
ensembl_id: "ENSG00000153443"
name: "UBA like domain containing 1"
location: "16p13.3"
module: 145
arm: "+"
pooled_cpm: 15.92
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 26
n_dd_up_clean: 17
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# UBALD1

*UBA like domain containing 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +11.1, q 5e-26, up in 28 of 46 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.06× (z +10.7, q 4e-24, up in 35 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.267× (z -19.5, q 0e+00, down in 43 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.241× (z -11.0, q 1e-25, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRAT2]] (+0.67, fdr 1e-05), [[MOB2]] (+0.62, fdr 1e-04), [[UBALD2]] (+0.58, fdr 2e-04); moves opposite to [[VDAC2]] (-0.51, fdr 2e-05), [[HBS1L]] (-0.47, fdr 3e-05), [[FRRS1]] (-0.44, fdr 3e-05).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7722.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.70×** | +11.1 | 5e-26 | 28/46 (A549, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +10.7 | 4e-24 | 35/45 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +9.7 | 7e-20 | 34/45 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +8.4 | 5e-15 | 32/47 (A549, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +7.9 | 2e-13 | 31/47 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +7.9 | 3e-13 | 31/46 (AsPC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +7.0 | 3e-10 | 23/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +6.8 | 7e-10 | 25/46 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +6.5 | 7e-09 | 25/47 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.4 | 1e-08 | 4/48 (C-33 A, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +6.1 | 4e-08 | 23/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +6.0 | 1e-07 | 25/47 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.4 | 3e-06 | 24/43 (NCI-H1792, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.1 | 1e-05 | 19/46 (Hs 766T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 0.002 | 14/45 (LOX-IMVI, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.003 | 12/47 (C-33 A, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.010 | 18/47 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.031 | 15/46 (LoVo, KATO III, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.031 | 11/47 (SW480, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7722.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.267×** | -19.5 | 0e+00 | 43/47 (AsPC-1, HT-29, …) | all doses, flat | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.241×** | -11.0 | 1e-25 | 38/45 (SK-MEL-2, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.245×** | -10.9 | 4e-25 | 41/45 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.250×** | -10.7 | 1e-24 | 38/45 (HT-29, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.268×** | -10.2 | 3e-22 | 34/42 (HT-29, A-427, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.288×** | -9.6 | 6e-20 | 35/44 (A498, HEC-1-A, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **0.550×** | -8.3 | 7e-15 | 35/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.475×** | -7.8 | 3e-13 | 34/48 (NCI-H2030, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.493×** | -5.5 | 3e-06 | 23/43 (LoVo, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.605×** | -5.3 | 7e-06 | 24/47 (A498, AsPC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.610×** | -5.2 | 1e-05 | 25/46 (HT-29, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.783×** | -5.1 | 1e-05 | 19/48 (A-427, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.723×** | -4.6 | 2e-04 | 16/46 (NCI-H23, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.732×** | -4.6 | 2e-04 | 19/45 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.579×** | -4.2 | 9e-04 | 19/47 (LoVo, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.754×** | -4.0 | 0.002 | 18/46 (A498, H4, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.757×** | -3.9 | 0.003 | 14/45 (SNU-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.776×** | -3.5 | 0.013 | 8/48 (SW48, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7722. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 26.9 | 3 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.34× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0863× (z -16.3) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0767× (z -9.0) |
| [[A549 (line)]] | wt | 21.8 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +18.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 9.64× (z +14.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.219× (z -10.1) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 28.5 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +12.7) ⚠ cell-cycle shift, explains ~33% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.111× (z -16.0) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0692× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 25.1 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +16.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.54× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.153× (z -10.2) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0374× (z -9.3) |
| [[A-427 (line)]] | wt | 21.9 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0786× (z -17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[venetoclax (drug)]] 5 µM 0.0909× (z -8.9) |
| [[A498 (line)]] | wt | 16.2 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.183× (z -12.2) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0926× (z -8.9) |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.105× (z -10.7) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0263× (z -9.1) |
| [[KATO III (line)]] | alt | 14.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +13.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.18× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.121× (z -11.4) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 18.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[EX229 (drug)]] 0.05 µM 0.276× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-733 (drug)]] 5 µM 0.0473× (z -9.3) |
| [[Hs 766T (line)]] | wt | 11.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +9.7) ⚠ cell-cycle shift, explains ~33% of this change | [[Sulfisoxazole (drug)]] 0.5 µM 0.0597× (z -13.6) |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[EX229 (drug)]] 5 µM 0.0446× (z -9.5) |
| [[BT-474 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[C-33 A (line)]] | alt | 30.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.136× (z -10.5) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.173× (z -9.5) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 5.04 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +8.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[COLO 205 (line)]] | alt | 9.26 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.201× (z -11.8) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.143× (z -10.3) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 14.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2030 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0878× (z -14.7) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.165× (z -10.3) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.209× (z -9.1) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.131× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.166× (z -12.4) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 26.2 | 0 | 1 | — | [[TAK-733 (drug)]] 5 µM 0.0332× (z -8.6) |
| [[A-172 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7722), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 21 of them with an alert (⚠; 20 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRAT2]] | +0.67 | +0.52 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[MOB2]] | +0.62 | +0.34 / +0.69 | both halves | 1e-04 |  |
| [[UBALD2]] | +0.58 | +0.30 / +0.67 | both halves | 2e-04 |  |
| [[ZFTRAF1]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[GATAD2B]] | +0.56 | +0.20 / +0.67 | ⚠ one half (not replicated) | 8e-04 |  |
| [[GARRE1]] | +0.56 | +0.32 / +0.63 | both halves | 2e-04 |  |
| [[CYTH2]] | +0.53 | +0.40 / +0.56 | both halves | 4e-05 |  |
| [[NATD1]] | +0.53 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[MAFF]] | +0.52 | +0.32 / +0.65 | both halves | 2e-04 |  |
| [[WDR48]] | +0.52 | +0.03 / +0.65 | ⚠ one half (not replicated) | 0.006 |  |
| [[BRD3]] | +0.52 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[PNPLA2]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ATG2A]] | +0.51 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[YAF2]] | +0.51 | +0.33 / +0.60 | both halves | 1e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VDAC2]] | -0.51 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[HBS1L]] | -0.47 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[FRRS1]] | -0.44 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[OPA1]] | -0.44 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[EIF2A]] | -0.44 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[ATP6V1A]] | -0.43 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[STEAP2]] | -0.43 | -0.22 / -0.54 | both halves | 6e-04 |  |
| [[PECR]] | -0.43 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[CRYZ]] | -0.43 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[EDEM2]] | -0.43 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[GNPDA2]] | -0.43 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[SLC18B1]] | -0.43 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises UBALD1's level | compounds that target MAP2K1: 3 of 4 lower it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.8, -43.3); signed map (-19.1, 12.4). **Vector** length 109, 27.0% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.5 | +8.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +1.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.2 | +9.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.2 | +2.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +6.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.8 | +1.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.7 | +3.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.7 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.7 | -19.5 |
|  | [[EX229 (drug)]] 5 µM |  | -8.5 | -10.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.2 | -11.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.1 | -10.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -7.5 | -7.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.4 | -9.6 |

## What is on record

|  |  |
|---|---|
| Name | UBA like domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,608,883-4,615,027 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FAM100A |
| Matched by | ensembl_id |

UniProt [Q8TB05](https://www.uniprot.org/uniprotkb/Q8TB05) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29576) · Entrez [124402](https://www.ncbi.nlm.nih.gov/gene/124402) · UniProt [Q8TB05](https://www.uniprot.org/uniprotkb/Q8TB05) · Ensembl [ENSG00000153443](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153443)

## Data

Gene col 7722: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7722); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7722, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7722]; `tensor/DDL_lfc|DDL_z.npy` [7722]; `embed/gene_vectors.npy` [7722]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7722 or target_col == 7722). Every well: [[UBALD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBALD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
