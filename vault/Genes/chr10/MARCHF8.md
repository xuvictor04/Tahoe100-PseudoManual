---
symbol: "MARCHF8"
type: "gene"
col: 9115
ensembl_id: "ENSG00000165406"
name: "membrane associated ring-CH-type finger 8"
location: "10q11.21-q11.22"
module: 76
arm: "+"
pooled_cpm: 47.2
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 34
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# MARCHF8

*membrane associated ring-CH-type finger 8* — 10q11.21-q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.30× (z +5.2, q 1e-04, up in 32 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 2.02×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.399× (z -12.9, q 5e-35, down in 39 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.470× (z -10.6, q 8e-24, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RALBP1]] (+0.72, fdr 7e-06), [[WIPI2]] (+0.67, fdr 7e-06), [[DNASE2]] (+0.64, fdr 7e-06); moves opposite to [[TNFRSF12A]] (-0.55, fdr 2e-05), [[ANAPC1P4]] (-0.51, fdr 2e-05), [[ZBTB38]] (-0.51, fdr 3e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9115.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 2.02×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +5.2 | 1e-04 | 32/48 (RKO, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +4.2 | 0.008 | 26/48 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.78× | +3.4 | 0.11 | 19/49 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.29× | +3.3 | 0.16 | 14/48 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.19 | 16/49 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.19 | 16/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 15 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9115.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.399×** | -12.9 | 5e-35 | 39/48 (H4, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.417×** | -11.3 | 3e-27 | 36/45 (RPMI-7951, SW 900, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.470×** | -10.6 | 8e-24 | 42/48 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.475×** | -10.4 | 3e-23 | 47/48 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.482×** | -10.2 | 2e-22 | 43/48 (SW480, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.488×** | -10.0 | 9e-22 | 43/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.474×** | -10.0 | 9e-22 | 33/40 (KATO III, A549, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.492×** | -9.9 | 2e-21 | 39/47 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.483×** | -9.8 | 7e-21 | 40/48 (A549, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.591×** | -7.3 | 1e-11 | 32/48 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.692×** | -7.3 | 2e-11 | 29/48 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.620×** | -6.7 | 1e-09 | 36/48 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.647×** | -6.1 | 5e-08 | 30/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **0.654×** | -5.7 | 5e-07 | 32/47 (SNU-423, HT-29, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.676×** | -5.3 | 5e-06 | 30/47 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.696×** | -5.1 | 1e-05 | 28/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.435×** | -4.9 | 3e-05 | 32/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.790×** | -4.7 | 1e-04 | 27/48 (LS 180, SW480, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.487×** | -4.3 | 6e-04 | 25/48 (NCI-H1792, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.824×** | -3.8 | 0.004 | 24/48 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.526×** | -3.8 | 0.004 | 25/48 (SW48, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.662×** | -3.5 | 0.011 | 24/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.765×** | -3.5 | 0.012 | 22/47 (SW48, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.781×** | -3.4 | 0.012 | 20/48 (CHP-212, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.774×** | -3.4 | 0.013 | 22/47 (HT-29, RKO, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.772×** | -3.4 | 0.013 | 22/48 (SW 900, SW48, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.686×** | -3.2 | 0.026 | 21/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 63.6 | 0 | 10 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -16.1) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.174× (z -15.5) |
| [[SW480 (line)]] | alt | 50.2 | 0 | 10 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.303× (z -11.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.320× (z -11.2) |
| [[SNU-423 (line)]] | alt | 90.7 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -15.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 60.9 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[HOP62 (line)]] | alt | 35.4 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -17.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 46.3 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.273× (z -10.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -8.8) |
| [[SW48 (line)]] | wt | 55.4 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.114× (z -13.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.216× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 44.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -10.8) |
| [[SNU-1 (line)]] | wt | 68.5 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.221× (z -10.6) |
| [[LoVo (line)]] | wt | 72.7 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.214× (z -13.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.344× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 43.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -16.1) |
| [[LS 180 (line)]] | wt | 75.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.360× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 34.0 | 1 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.312× (z -10.6) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.373× (z -8.9) |
| [[SW 900 (line)]] | alt | 56.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -10.5) |
| [[A-172 (line)]] | wt | 46.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.348× (z -8.6) |
| [[H4 (line)]] | wt | 43.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0723× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.233× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 43.3 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.355× (z -9.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HS-578T (line)]] | alt | 40.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -11.8) |
| [[HT-29 (line)]] | alt | 33.3 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.181× (z -11.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H2347 (line)]] | alt | 33.5 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 67.7 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.293× (z -12.6) |
| [[AN3 CA (line)]] | alt | 95.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0934× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[AsPC-1 (line)]] | alt | 46.9 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.209× (z -12.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -9.6) |
| [[C32 (line)]] | wt | 20.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.201× (z -8.6) |
| [[CHP-212 (line)]] | wt | 54.5 | 0 | 2 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0789× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 38.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 56.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H23 (line)]] | alt | 44.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 62.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SW1417 (line)]] | alt | 49.1 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.267× (z -11.8) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 73.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.246× (z -12.1) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 53.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0803× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HepG2_C3A (line)]] | wt | 74.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[KATO III (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0956× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H1573 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.243× (z -9.6) ⚠ toxic |
| [[RKO (line)]] | wt | 53.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[RPMI-7951 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0740× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SW 1271 (line)]] | alt | 47.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0579× (z -9.3) |
| [[BT-474 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALBP1]] | +0.72 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[WIPI2]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[DNASE2]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[COQ8A]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[MKRN1]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 | same gene group; pathway: HALLMARK_HEME_METABOLISM |
| [[FAM185BP]] | +0.63 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[LINC00674]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[KLHDC3]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TMEM183A]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.60 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[ALDH6A1]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[FAM174A]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF12A]] | -0.55 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[ANAPC1P4]] | -0.51 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ZBTB38]] | -0.51 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ERCC6L2]] | -0.51 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[METTL2B]] | -0.50 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[SSUH2]] | -0.50 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ST7L]] | -0.50 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[MIR4435-2HG]] | -0.50 | -0.56 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.6, -44.7); signed map (-19.4, 7.5). **Vector** length 95.6, 27.5% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.8 | +5.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.1 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +1.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.0 | +1.2 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.6 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -10.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -10.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | membrane associated ring-CH-type finger 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.21-q11.22 — chr10:45,454,585-45,594,906 (-) |
| Ensembl biotype | protein_coding |
| Also known as | c-MIR, CMIR, MARCH-VIII, RNF178; previously MIR, MARCH8 |
| Gene groups (HGNC) | Ring finger proteins; Membrane associated ring-CH-type fingers |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T0T0](https://www.uniprot.org/uniprotkb/Q5T0T0) (E3 ubiquitin-protein ligase MARCHF8):

> E3 ubiquitin-protein ligase that plays several important roles in innate immunity and adaptive immunity. Mediates ubiquitination of CD86 and MHC class II proteins, such as HLA-DR alpha and beta, and promotes their subsequent endocytosis and sorting to lysosomes via multivesicular bodies. Possesses a very broad antiviral activity by specifically inactivating different viral fusion proteins. Targets and ubiquitinates cytoplasmic lysine residues of viral envelope glycoproteins with single …

**Summary**, from NCBI Gene [220972](https://www.ncbi.nlm.nih.gov/gene/220972):

> MARCH8 is a member of the MARCH family of membrane-bound E3 ubiquitin ligases (EC 6.3.2.19). MARCH enzymes add ubiquitin (see MIM 191339) to target lysines in substrate proteins, thereby signaling their vesicular transport between membrane compartments. MARCH8 induces the internalization of several membrane glycoproteins (Goto et al., 2003 [PubMed 12582153]; Bartee et al., 2004 [PubMed 14722266]).[supplied by OMIM, Apr 2010]

**Accessions** — [HGNC:23356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23356) · Entrez [220972](https://www.ncbi.nlm.nih.gov/gene/220972) · UniProt [Q5T0T0](https://www.uniprot.org/uniprotkb/Q5T0T0) · Ensembl [ENSG00000165406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165406)

## Data

Gene col 9115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9115); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9115]; `tensor/DDL_lfc|DDL_z.npy` [9115]; `embed/gene_vectors.npy` [9115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9115 or target_col == 9115). Every well: [[MARCHF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARCHF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
