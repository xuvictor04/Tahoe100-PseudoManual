---
symbol: "SVIL"
type: "gene"
col: 12380
ensembl_id: "ENSG00000197321"
name: "supervillin"
location: "10p11.23"
module: 151
arm: "+"
pooled_cpm: 307.81
n_lines_expressing: 47
n_dd_up: 7
n_dd_down: 32
n_dd_up_clean: 6
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# SVIL

*supervillin* — 10p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.28× (z +4.7, q 0.002, up in 28 of 45 measured lines) ⚠ cell-cycle shift, explains ~20% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.26× (z +4.4, q 0.003, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.391× (z -18.5, q 0e+00, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BACH1]] (+0.64, fdr 1e-05), [[PMEPA1]] (+0.63, fdr 7e-06), [[IGF2BP2]] (+0.63, fdr 1e-05); moves opposite to [[ATPAF1]] (-0.61, fdr 1e-05), [[TRIT1]] (-0.59, fdr 1e-05), [[ALG9]] (-0.58, fdr 1e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BCAN-AS1]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Busulfan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12380.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +4.7 | 0.002 | 28/45 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +4.4 | 0.003 | 24/45 (PANC-1, SK-MEL-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.003 | 23/45 (SK-MEL-2, SW48, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.15× | +3.9 | 0.011 | 21/45 (SW48, HOP62, …) | rises with dose | composition shift |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.029 | 21/45 (RPMI-7951, CFPAC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.19× | +3.5 | 0.048 | 22/45 (SW48, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.19× | +3.4 | 0.049 | 19/45 (HT-29, LoVo, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.19× | +3.4 | 0.050 | 20/45 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.054 | 21/45 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.13× | +3.3 | 0.054 | 15/46 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.19× | +3.3 | 0.054 | 17/45 (LoVo, NCI-H23, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.056 | 21/45 (NCI-H1792, A498, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.2 | 0.056 | 10/45 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.056 | 20/45 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.056 | 18/45 (SW48, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.062 | 20/46 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.091 | 9/45 (NCI-H2347, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12380.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.391×** | -18.5 | 0e+00 | 44/45 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.545×** | -16.9 | 0e+00 | 38/46 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.427×** | -16.7 | 0e+00 | 44/45 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.484×** | -14.3 | 5e-44 | 42/45 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.545×** | -11.5 | 2e-28 | 34/43 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.591×** | -10.0 | 2e-21 | 41/45 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.610×** | -8.2 | 2e-14 | 38/46 (HepG2/C3A, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.643×** | -8.0 | 7e-14 | 33/44 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.671×** | -7.6 | 3e-12 | 36/47 (Panc 03.27, HEC-1-A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.691×** | -7.3 | 2e-11 | 28/45 (HEC-1-A, RPMI-7951, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.782×** | -6.9 | 3e-10 | 29/45 (J82, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.708×** | -6.8 | 4e-10 | 32/45 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.698×** | -6.8 | 4e-10 | 32/45 (J82, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.756×** | -6.3 | 1e-08 | 25/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.721×** | -6.2 | 2e-08 | 32/45 (HEC-1-A, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.731×** | -6.2 | 2e-08 | 32/45 (A-172, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.730×** | -6.0 | 8e-08 | 24/45 (J82, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.809×** | -5.3 | 3e-06 | 25/45 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.727×** | -5.3 | 3e-06 | 29/46 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.615×** | -5.0 | 1e-05 | 30/45 (NCI-H1573, C32, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.786×** | -4.8 | 5e-05 | 27/45 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12380. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 747 | 0 | 21 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -23.9) |
| [[NCI-H460 (line)]] | wt | 221 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -14.8) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.377× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 346 | 2 (1 ⚠) | 9 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.65× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.338× (z -14.1) |
| [[J82 (line)]] | alt | 185 | 2 (1 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.1) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.93× (z +8.7) | [[Selinexor (drug)]] 5 µM 0.437× (z -16.0) |
| [[LoVo (line)]] | wt | 321 | 2 (1 ⚠) | 8 (4 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.80× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 673 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -24.0) |
| [[A-172 (line)]] | wt | 257 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -17.4) |
| [[HT-29 (line)]] | alt | 171 | 6 (3 ⚠) | 3 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.79× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.453× (z -10.5) |
| [[LS 180 (line)]] | wt | 411 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.253× (z -15.7) |
| [[AsPC-1 (line)]] | alt | 490 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -23.1) |
| [[HepG2_C3A (line)]] | wt | 1,009 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -16.3) |
| [[HOP62 (line)]] | alt | 272 | 2 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +18.0) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.68× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.434× (z -10.8) |
| [[PANC-1 (line)]] | alt | 235 | 2 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.98× (z +10.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.80× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 272 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 452 | 1 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.0) ⚠ cell-cycle shift, explains ~24% of this change | [[Panobinostat (drug)]] 5 µM 0.360× (z -10.0) |
| [[SNU-423 (line)]] | alt | 340 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -16.9) |
| [[SW48 (line)]] | wt | 241 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +22.4) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.51× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 396 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.2) ⚠ cell-cycle shift, explains ~24% of this change | [[Panobinostat (drug)]] 5 µM 0.362× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 297 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -13.1) |
| [[SW1417 (line)]] | alt | 413 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -17.7) |
| [[SW480 (line)]] | alt | 274 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -11.3) |
| [[A549 (line)]] | wt | 259 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -14.5) |
| [[Hs 766T (line)]] | wt | 236 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.332× (z -11.2) |
| [[KATO III (line)]] | alt | 166 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.441× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 911 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.261× (z -13.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 298 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -15.6) |
| [[NCI-H2347 (line)]] | alt | 362 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -14.0) |
| [[RKO (line)]] | wt | 156 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.518× (z -11.8) |
| [[SHP-77 (line)]] | alt | 245 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -15.3) |
| [[A-427 (line)]] | wt | 107 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +13.5) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 5 µM 0.101× (z -27.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.422× (z -10.6) |
| [[C32 (line)]] | wt | 317 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -14.9) |
| [[MIA PaCa-2 (line)]] | alt | 236 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +16.1) ⚠ cell-cycle shift, explains ~24% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.295× (z -12.0) ⚠ toxic |
| [[SW 900 (line)]] | alt | 356 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -10.6) |
| [[A498 (line)]] | wt | 150 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -11.0) |
| [[BT-474 (line)]] | alt | 238 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -14.1) |
| [[HS-578T (line)]] | alt | 248 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.2) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[H4 (line)]] | wt | 135 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.321× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 116 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +12.2) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[AN3 CA (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 240 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 70.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 154 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 535 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 75.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 561 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12380), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BACH1]] | +0.64 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[PMEPA1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[IGF2BP2]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 | same gene group |
| [[AGO2]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ZBTB38]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PLPP4]] | +0.61 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[LINC02930]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[FJX1]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ADGRL4]] | +0.59 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[MACF1]] | +0.59 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[SPRY2]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[DUSP4]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATPAF1]] | -0.61 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[TRIT1]] | -0.59 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[ALG9]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[NAPB]] | -0.58 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[PMS2P3-1]] | -0.58 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SRP54-AS1]] | -0.57 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[C20orf96]] | -0.57 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[DNASE2]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[LAPTM4A]] | -0.56 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[IER3IP1]] | -0.55 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PMS2P3]] | -0.54 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[EEF1AKMT3]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAN-AS1]] | B | BCAN-AS1 activity raises SVIL's level | lines that do not express BCAN-AS1 (11) vs lines expressing it (39) | 2.14× lower at baseline in the lines without BCAN-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS2, ETV7; maybe low, not absent |
| [[KIFC3]] | C | KIFC3 activity raises SVIL's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 2.40× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Busulfan (drug)]] 5 µM | C | SVIL activity lowers the cells' numbers under Busulfan 5 µM (makes them more sensitive) | lines that do not express SVIL (3) vs lines expressing it (45) | the lines without SVIL: 1.30× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: DBN1, LAMC1, PLEC; maybe low, not absent |
| cells under [[EX229 (drug)]] 0.5 µM | C | SVIL activity raises the cells' numbers under EX229 0.5 µM (protects the cells) | lines that do not express SVIL (3) vs lines expressing it (45) | the lines without SVIL: 0.67× the cells of the other lines | 0.038 | ⚠ few lines (3 vs 47); across organs; also absent: DBN1, LAMC1, PLEC; maybe low, not absent |
| cells under [[Neratinib (maleate) (drug)]] 5 µM | C | SVIL activity raises the cells' numbers under Neratinib (maleate) 5 µM (protects the cells) | lines that do not express SVIL (3) vs lines expressing it (45) | the lines without SVIL: 0.83× the cells of the other lines | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: DBN1, LAMC1, PLEC; maybe low, not absent |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.3, 12.1); signed map (16.4, 40.3). **Vector** length 125, 43.0% of its response variance represented; |z| ≥ 3 in 1,918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +9.9 | +3.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.5 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +9.2 | +3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.3 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.3 | +4.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.8 | +3.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +4.6 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +0.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -7.3 | -6.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.3 | -6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.1 | -5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.1 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.1 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.1 | -6.8 |

## What is on record

|  |  |
|---|---|
| Name | supervillin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.23 — chr10:29,457,338-29,736,959 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Gelsolin/villins; MicroRNA protein coding host genes |
| Hallmark sets | MYOGENESIS, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [O95425](https://www.uniprot.org/uniprotkb/O95425) (Supervillin):

> [Isoform 1]: Forms a high-affinity link between the actin cytoskeleton and the membrane. Is among the first costameric proteins to assemble during myogenesis and it contributes to myogenic membrane structure and differentiation. Appears to be involved in myosin II assembly. May modulate myosin II regulation through MLCK during cell spreading, an initial step in cell migration. May play a role in invadopodial function. In addition to its cytoskeletal activities, acts as a cofactor or scaffold …

**Summary**, from NCBI Gene [6840](https://www.ncbi.nlm.nih.gov/gene/6840):

> This gene encodes a bipartite protein with distinct amino- and carboxy-terminal domains. The amino-terminus contains nuclear localization signals and the carboxy-terminus contains numerous consecutive sequences with extensive similarity to proteins in the gelsolin family of actin-binding proteins, which cap, nucleate, and/or sever actin filaments. The gene product is tightly associated with both actin filaments and plasma membranes, suggesting a role as a high-affinity link between the actin …

**Accessions** — [HGNC:11480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11480) · Entrez [6840](https://www.ncbi.nlm.nih.gov/gene/6840) · UniProt [O95425](https://www.uniprot.org/uniprotkb/O95425) · Ensembl [ENSG00000197321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197321)

## Data

Gene col 12380: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12380); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12380, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12380]; `tensor/DDL_lfc|DDL_z.npy` [12380]; `embed/gene_vectors.npy` [12380]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12380 or target_col == 12380). Every well: [[SVIL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SVIL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
