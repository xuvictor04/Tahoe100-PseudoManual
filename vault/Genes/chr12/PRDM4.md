---
symbol: "PRDM4"
type: "gene"
col: 3170
ensembl_id: "ENSG00000110851"
name: "PR/SET domain 4"
location: "12q23.3"
module: 12
arm: "+"
pooled_cpm: 44.77
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PRDM4

*PR/SET domain 4* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.21× (z +12.1, q 4e-31, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.435× (z -16.5, q 0e+00, down in 43 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.873× (z -3.8, q 0.007, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW48 0.0764×, NCI-H23 0.159×, C-33 A 0.104×, PANC-1 0.298×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (NCI-H2030 0.0499×, NCI-H1573 0.0610×, A549 0.119×, A-172 0.147×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (SNU-423 0.118×, HEC-1-A 0.205×, A549 0.215×, HCT15 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (A-172 0.529×, HOP62 0.544×); [[Doxycycline (monohydrate) (drug)]] 0.05 µM in 1 line (AN3 CA 0.154×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHAX]] (+0.66, fdr 7e-06), [[ZNF777]] (+0.66, fdr 1e-05), [[ASNSD1]] (+0.63, fdr 1e-05); moves opposite to [[TFRC]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3170.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.21×** | +12.1 | 4e-31 | 42/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.39×** | +9.3 | 5e-18 | 38/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +8.3 | 2e-14 | 34/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +8.3 | 2e-14 | 30/48 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.46×** | +6.9 | 5e-10 | 31/48 (LOX-IMVI, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +6.8 | 1e-09 | 26/48 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.34×** | +5.8 | 5e-07 | 32/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.5 | 2e-06 | 25/48 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +5.4 | 4e-06 | 23/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.30×** | +4.9 | 7e-05 | 25/48 (PANC-1, LS 180, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.8 | 1e-04 | 21/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +4.2 | 0.001 | 12/48 (SW 900, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +3.7 | 0.010 | 18/48 (J82, A498, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.010 | 13/48 (HT-29, J82, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.6 | 0.012 | 1/49 (SHP-77) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.015 | 16/48 (HT-29, A498, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.020 | 11/48 (SK-MEL-2, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.034 | 14/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.069 | 13/48 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Tadalafil (drug)]] 5 µM |  | 1.17× | +3.0 | 0.080 | 7/48 (SW480, NCI-H661, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +2.9 | 0.083 | 8/47 (SNU-423, C-33 A, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3170.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW48 0.0764×, NCI-H23 0.159×, C-33 A 0.104×, PANC-1 0.298×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (NCI-H2030 0.0499×, NCI-H1573 0.0610×, A549 0.119×, A-172 0.147×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (SNU-423 0.118×, HEC-1-A 0.205×, A549 0.215×, HCT15 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (A-172 0.529×, HOP62 0.544×); [[Doxycycline (monohydrate) (drug)]] 0.05 µM in 1 line (AN3 CA 0.154×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.435×** | -16.5 | 0e+00 | 43/47 (SW48, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.450×** | -15.3 | 0e+00 | 32/40 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.500×** | -12.8 | 5e-35 | 36/45 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.738×** | -8.6 | 1e-15 | 33/48 (A549, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.681×** | -7.6 | 2e-12 | 33/48 (J82, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.716×** | -6.4 | 2e-08 | 28/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.740×** | -6.0 | 2e-07 | 28/48 (SW480, NCI-H661, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.764×** | -5.4 | 6e-06 | 27/47 (HOP62, SNU-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.777×** | -5.0 | 3e-05 | 22/48 (A549, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.819×** | -4.0 | 0.004 | 19/48 (NCI-H2347, HOP62, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.873× | -3.8 | 0.007 | 17/48 (A-172, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.825×** | -3.7 | 0.011 | 20/48 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.821×** | -3.6 | 0.013 | 14/48 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.848× | -3.2 | 0.063 | 14/48 (HS-578T, LoVo, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.808×** | -3.0 | 0.093 | 12/48 (Hs 766T, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3170. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 51.7 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.529× (z -8.9) |
| [[HOP62 (line)]] | alt | 44.0 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.544× (z -8.6) |
| [[LoVo (line)]] | wt | 52.0 | 3 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.98× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[RKO (line)]] | wt | 53.8 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A549 (line)]] | wt | 56.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 54.4 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[MIA PaCa-2 (line)]] | alt | 51.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 42.3 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -9.7) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SW480 (line)]] | alt | 45.6 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.80× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 58.7 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.88× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -11.7) ⚠ cell-cycle shift, explains ~24% of this change |
| [[HEC-1-A (line)]] | alt | 38.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HS-578T (line)]] | alt | 42.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 52.7 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -10.7) ⚠ cell-cycle shift, explains ~24% of this change |
| [[PANC-1 (line)]] | alt | 52.5 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.82× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 46.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0764× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 55.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HCT15 (line)]] | alt | 53.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 30.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LS 180 (line)]] | wt | 43.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.8) | — |
| [[SNU-423 (line)]] | alt | 52.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW1417 (line)]] | alt | 52.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AN3 CA (line)]] | alt | 49.8 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.154× (z -8.8) |
| [[C-33 A (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[C32 (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[CFPAC-1 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.338× (z -9.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 55.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[KATO III (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H1573 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0610× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0499× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 49.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 45.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 45.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -12.8) ⚠ cell-cycle shift, explains ~68% of this change |
| [[SNU-1 (line)]] | wt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW 900 (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[BT-474 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3170), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHAX]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ZNF777]] | +0.66 | +0.73 / +0.53 | both halves | 1e-05 | same gene group |
| [[ASNSD1]] | +0.63 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[MSANTD4]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ZNF282]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 | same gene group |
| [[ABRAXAS2]] | +0.61 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[RDH14]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ZNF579]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 | same gene group |
| [[RRN3]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ZNF205]] | +0.60 | +0.62 / +0.62 | both halves | 7e-06 | same gene group |
| [[CBLL1]] | +0.60 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[RIOK2]] | +0.60 | +0.64 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFRC]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PRDM4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.591). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-45.3, 5.4); signed map (-6.5, -23.9). **Vector** length 101, 25.6% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +10.4 | +9.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +7.0 | +6.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.8 | +12.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +8.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +8.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +3.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.5 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.3 | +4.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | -5.6 | -4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | -5.4 | -5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -4.0 | -16.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.6 | +0.4 |
|  | [[Artemether (drug)]] 0.05 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | PR/SET domain 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:107,732,871-107,761,272 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PFM1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PR/SET domain family; Putative lysine methyltransferases |
| Hallmark sets | COMPLEMENT |
| Reactome | 3 pathways, smallest: p75NTR negatively regulates cell cycle via SC1; p75 NTR receptor-mediated signalling; Death Receptor Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKN5](https://www.uniprot.org/uniprotkb/Q9UKN5) (PR domain zinc finger protein 4):

> May function as a transcription factor involved in cell differentiation.

**Summary**, from NCBI Gene [11108](https://www.ncbi.nlm.nih.gov/gene/11108):

> The protein encoded by this gene is a transcription factor of the PR-domain protein family. It contains a PR-domain and multiple zinc finger motifs. Transcription factors of the PR-domain family are known to be involved in cell differentiation and tumorigenesis. An elevated expression level of this gene has been observed in PC12 cells treated with nerve growth factor, beta polypeptide (NGF). This gene is located in a chromosomal region that is thought to contain tumor suppressor genes. …

**Accessions** — [HGNC:9348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9348) · Entrez [11108](https://www.ncbi.nlm.nih.gov/gene/11108) · UniProt [Q9UKN5](https://www.uniprot.org/uniprotkb/Q9UKN5) · Ensembl [ENSG00000110851](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110851)

## Data

Gene col 3170: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3170); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3170, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3170]; `tensor/DDL_lfc|DDL_z.npy` [3170]; `embed/gene_vectors.npy` [3170]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3170 or target_col == 3170). Every well: [[PRDM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
