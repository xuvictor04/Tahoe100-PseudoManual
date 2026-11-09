---
symbol: "LMNB2"
type: "gene"
col: 10735
ensembl_id: "ENSG00000176619"
name: "lamin B2"
location: "19p13.3"
module: 22
arm: "+"
pooled_cpm: 35.0
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# LMNB2

*lamin B2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (21 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.81× (z +19.2, q 0e+00, up in 45 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.13× (z +8.6, q 1e-15, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.662× (z -5.9, q 2e-06, down in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~84% of this change. The strongest without an alert is [[Temsirolimus (drug)]] 0.5 µM: 0.781× (z -3.6, q 0.032, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMNB1]] (+0.76, fdr 7e-06), [[FOXM1]] (+0.75, fdr 7e-06), [[DNMT1]] (+0.74, fdr 7e-06); moves opposite to [[RNF181]] (-0.66, fdr 1e-05), [[NACA4P]] (-0.65, fdr 7e-06, ⚠ NACA4P in the vector space only through flagged drug-doses), [[SMIM26]] (-0.65, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[SELENOK]] (-0.64, fdr 1e-05), [[SYF2]] (-0.63, fdr 1e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LAMA5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10735.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.81×** | +19.2 | 0e+00 | 45/45 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.62×** | +17.8 | 0e+00 | 38/40 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.23×** | +15.6 | 0e+00 | 41/42 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.69×** | +10.6 | 3e-24 | 31/47 (A549, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.85×** | +8.9 | 9e-17 | 40/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.13×** | +8.6 | 1e-15 | 43/48 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.82×** | +8.3 | 9e-15 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.76×** | +8.1 | 3e-14 | 38/48 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.64×** | +7.1 | 7e-11 | 40/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.59×** | +6.6 | 2e-09 | 36/46 (NCI-H2030, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.53×** | +6.1 | 6e-08 | 35/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.48×** | +5.6 | 9e-07 | 27/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | **1.50×** | +5.6 | 9e-07 | 30/47 (C32, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.30×** | +5.3 | 4e-06 | 30/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 1e-04 | 27/47 (A549, NCI-H2030, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +4.4 | 5e-04 | 20/48 (HEC-1-A, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.78×** | +4.3 | 5e-04 | 25/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.004 | 16/48 (HEC-1-A, LS 180, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.012 | 13/48 (A498, AsPC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.013 | 10/46 (SW1417, NCI-H1792, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.019 | 16/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.022 | 14/47 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.027 | 14/48 (A498, NCI-H1792, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.49×** | +3.0 | 0.053 | 7/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10735.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.662×** | -5.9 | 2e-06 | 29/48 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.761×** | -5.6 | 7e-06 | 27/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.831×** | -3.8 | 0.030 | 18/48 (MIA PaCa-2, KATO III, …) | rises with dose | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.778×** | -3.6 | 0.032 | 15/48 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.781×** | -3.6 | 0.032 | 20/47 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.763×** | -3.5 | 0.032 | 14/48 (KATO III, A-427, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **0.784×** | -3.5 | 0.032 | 15/47 (KATO III, A-172, …) | top dose only | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.628×** | -3.5 | 0.032 | 18/48 (LoVo, Hs 766T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.796×** | -3.3 | 0.063 | 15/48 (SW 1088, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.729×** | -3.3 | 0.064 | 18/48 (RPMI-7951, Hs 766T, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.734×** | -3.2 | 0.071 | 16/48 (A498, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.804×** | -3.2 | 0.071 | 15/48 (Hs 766T, A-172, …) | all doses, stronger at high dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.804×** | -3.1 | 0.071 | 14/48 (HepG2/C3A, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10735. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 41.6 | 4 (4 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.376× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 42.1 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +14.6) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[A498 (line)]] | wt | 33.9 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +13.6) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[A549 (line)]] | wt | 24.4 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +16.1) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[LoVo (line)]] | wt | 27.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H460 (line)]] | wt | 21.7 | 4 (4 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.18× (z +11.6) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[SNU-423 (line)]] | alt | 22.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.36× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-427 (line)]] | wt | 55.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.302× (z -14.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 64.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.4) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[HOP62 (line)]] | alt | 26.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.01× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[J82 (line)]] | alt | 39.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LOX-IMVI (line)]] | wt | 49.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.69× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Selinexor (drug)]] 5 µM 0.305× (z -14.4) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 53.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1792 (line)]] | alt | 16.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.08× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2347 (line)]] | alt | 33.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +13.0) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[SW1417 (line)]] | alt | 40.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW480 (line)]] | alt | 43.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 72.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[H4 (line)]] | wt | 40.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.241× (z -10.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.152× (z -9.8) |
| [[HS-578T (line)]] | alt | 32.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.9) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[HT-29 (line)]] | alt | 21.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[KATO III (line)]] | alt | 21.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.03× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2030 (line)]] | alt | 27.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.35× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[Panc 03.27 (line)]] | alt | 34.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[RPMI-7951 (line)]] | alt | 30.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HCT15 (line)]] | alt | 52.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HepG2_C3A (line)]] | wt | 32.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.0) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[Hs 766T (line)]] | wt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[RKO (line)]] | wt | 44.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10735), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMNB1]] | +0.76 | +0.72 / +0.76 | both halves | 7e-06 | same gene group; STRING 999 |
| [[FOXM1]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 | STRING 443 |
| [[DNMT1]] | +0.74 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[TFDP1]] | +0.74 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[NUP188]] | +0.73 | +0.61 / +0.80 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.71 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[BUB1B]] | +0.71 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[ARHGAP11A]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[TMPO]] | +0.70 | +0.71 / +0.74 | both halves | 7e-06 | STRING 796 |
| [[MAD2L1]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[CBX5]] | +0.69 | +0.58 / +0.75 | both halves | 7e-06 | same gene group; STRING 444 |

## Genes that move opposite

*19 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF181]] | -0.66 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[NACA4P]] ⚠ | -0.65 | -0.61 / -0.67 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SMIM26]] ⚠ | -0.65 | -0.59 / -0.67 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SELENOK]] | -0.64 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[SYF2]] | -0.63 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[WDR83OS]] ⚠ | -0.63 | -0.53 / -0.64 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CDC37L1]] | -0.63 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[TRAPPC2B]] | -0.62 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[PCF11-AS1]] | -0.62 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[FTL]] | -0.62 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[MED10]] | -0.62 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | -0.61 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.61 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[ADPRM]] | -0.61 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[NKAP]] | -0.61 | -0.49 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA5]] | B | LAMA5 activity raises LMNB2's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.45× lower at baseline in the lines without LAMA5 | 0.049 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises LMNB2's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.68× lower at baseline in the lines without MYBL1 | 0.050 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[PBK]] | C | PBK activity raises LMNB2's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.19× lower at baseline in the lines without PBK | 0.033 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MCM3]] | C | MCM3 activity raises LMNB2's level | lines that do not express MCM3 (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.6, -35.5); signed map (-33.8, -48.1). **Vector** length 113, 33.4% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.51 to 8); *Kinesins* (reactome, mean cos +0.51 to 10); *Initiation of Nuclear Envelope (NE) Reformation* (reactome, mean cos +0.57 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +9.3 | +17.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +8.5 | +19.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +7.7 | +15.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +7.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | +3.6 | +6.6 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.7 | +0.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +4.3 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +3.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.9 | -5.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -4.6 | -5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.4 | -1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -0.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.0 | -3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | lamin B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,427,638-2,456,959 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LMN2 |
| Gene groups (HGNC) | Lamins; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03252](https://www.uniprot.org/uniprotkb/Q03252) (Lamin-B2):

> Lamins are intermediate filament proteins that assemble into a filamentous meshwork, and which constitute the major components of the nuclear lamina, a fibrous layer on the nucleoplasmic side of the inner nuclear membrane. Lamins provide a framework for the nuclear envelope, bridging the nuclear envelope and chromatin, thereby playing an important role in nuclear assembly, chromatin organization, nuclear membrane and telomere dynamics. The structural integrity of the lamina is strictly …

**Summary**, from NCBI Gene [84823](https://www.ncbi.nlm.nih.gov/gene/84823):

> This gene encodes a B type nuclear lamin. The nuclear lamina consists of a two-dimensional matrix of proteins located next to the inner nuclear membrane. The lamin family of proteins make up the matrix and are highly conserved in evolution. During mitosis, the lamina matrix is reversibly disassembled as the lamin proteins are phosphorylated. Lamin proteins are thought to be involved in nuclear stability, chromatin structure and gene expression. Vertebrate lamins consist of two types, A and B. …

**Accessions** — [HGNC:6638](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6638) · Entrez [84823](https://www.ncbi.nlm.nih.gov/gene/84823) · UniProt [Q03252](https://www.uniprot.org/uniprotkb/Q03252) · Ensembl [ENSG00000176619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176619)

## Data

Gene col 10735: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10735); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10735, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10735]; `tensor/DDL_lfc|DDL_z.npy` [10735]; `embed/gene_vectors.npy` [10735]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10735 or target_col == 10735). Every well: [[LMNB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMNB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
