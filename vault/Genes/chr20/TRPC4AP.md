---
symbol: "TRPC4AP"
type: "gene"
col: 2054
ensembl_id: "ENSG00000100991"
name: "transient receptor potential cation channel subfamily C member 4 associated protein"
location: "20q11.22"
module: 131
arm: "+"
pooled_cpm: 214.31
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# TRPC4AP

*transient receptor potential cation channel subfamily C member 4 associated protein* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.65× (z +8.7, q 1e-15, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.373× (z -17.3, q 0e+00, down in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.838× (z -4.4, q 7e-04, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (RKO 0.146×, RPMI-7951 0.203×, NCI-H2347 0.316×, A-172 0.257×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (SNU-1 0.0607×, A549 0.199×, AN3 CA 0.0531×, NCI-H460 0.279×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HS-578T 0.475×, A-172 0.544×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.604×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB6A]] (+0.69, fdr 7e-06), [[WDR20]] (+0.67, fdr 7e-06), [[RNF149]] (+0.66, fdr 1e-05); moves opposite to [[CYB5D1]] (-0.65, fdr 1e-05), [[PUF60]] (-0.60, fdr 1e-05), [[ZNF816]] (-0.60, fdr 1e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTNR1A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SNHG25]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2054.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +8.7 | 1e-15 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +7.3 | 8e-11 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +7.1 | 3e-10 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.01×** | +6.4 | 3e-08 | 44/48 (NCI-H1573, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +5.6 | 2e-06 | 39/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.79×** | +5.3 | 1e-05 | 36/49 (A498, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +4.6 | 4e-04 | 32/48 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.1 | 0.003 | 20/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.8 | 0.010 | 29/47 (COLO 205, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.068 | 26/49 (A-427, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.22×** | +3.2 | 0.068 | 26/48 (A498, HT-29, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.068 | 25/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2054.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (RKO 0.146×, RPMI-7951 0.203×, NCI-H2347 0.316×, A-172 0.257×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (SNU-1 0.0607×, A549 0.199×, AN3 CA 0.0531×, NCI-H460 0.279×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HS-578T 0.475×, A-172 0.544×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.604×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.373×** | -17.3 | 0e+00 | 49/49 (RKO, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.382×** | -16.2 | 0e+00 | 43/44 (SNU-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.441×** | -13.2 | 1e-37 | 44/45 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.606×** | -8.6 | 8e-16 | 47/48 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.718×** | -8.2 | 3e-14 | 32/48 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.648×** | -7.6 | 3e-12 | 45/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.780×** | -6.2 | 6e-08 | 29/49 (A549, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.709×** | -6.0 | 1e-07 | 40/48 (HOP62, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.838× | -4.4 | 7e-04 | 17/48 (A-172, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.779×** | -4.4 | 7e-04 | 27/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.793×** | -3.9 | 0.005 | 25/47 (NCI-H2347, NCI-H2030, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.802×** | -3.9 | 0.005 | 30/48 (SW 1271, SW 1088, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.804×** | -3.8 | 0.005 | 30/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.858× | -3.8 | 0.006 | 4/48 (Hs 766T, CHP-212, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.830×** | -3.3 | 0.039 | 21/48 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.841× | -3.0 | 0.082 | 21/48 (HOP62, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2054. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 193 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.604× (z -10.0) |
| [[PANC-1 (line)]] | alt | 149 | 3 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -13.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 222 | 3 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 198 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -19.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 257 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -18.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 206 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.475× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 184 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -18.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 268 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -15.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 211 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.29× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -12.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 201 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -22.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 175 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 320 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -24.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 293 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -17.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 192 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -15.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 203 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -18.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 222 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 257 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -15.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 264 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -19.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 207 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -18.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 223 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0607× (z -29.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 212 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -16.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 250 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -16.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 878 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -16.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 143 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.413× (z -10.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 338 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -16.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 143 | 1 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.18× (z +8.8) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -10.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 200 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -12.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 153 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.401× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 150 | 1 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 1.98× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -12.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 244 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -17.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 243 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -15.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 166 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -11.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 141 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -11.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 301 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -21.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 500 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -15.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -12.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0531× (z -21.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -9.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -13.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 243 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -11.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.440× (z -8.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 115 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 252 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2054), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB6A]] | +0.69 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[WDR20]] | +0.67 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[RNF149]] | +0.66 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[ABHD18]] | +0.66 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[HINT1]] | +0.65 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[GAPVD1]] | +0.65 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[SLC37A3]] | +0.65 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[NENF]] | +0.65 | +0.76 / +0.50 | both halves | 1e-05 |  |
| [[CCT6P3-1]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[MZT2B]] | +0.64 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[ATOX1]] | +0.63 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[DENND10]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5D1]] | -0.65 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[PUF60]] | -0.60 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[ZNF816]] | -0.60 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[JUNB]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SLC35A4]] | -0.57 | -0.77 / -0.35 | both halves | 1e-04 |  |
| [[NAB1]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.56 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[THOC6]] | -0.56 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[CELSR3]] | -0.56 | -0.71 / -0.37 | both halves | 9e-05 |  |
| [[DCLRE1A]] | -0.55 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[ZXDB]] | -0.55 | -0.67 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTNR1A]] | B | MTNR1A activity lowers TRPC4AP's level | lines that do not express MTNR1A (7) vs lines expressing it (43) | 1.14× higher at baseline in the lines without MTNR1A | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG25]] | C | TRPC4AP's natural level weakens SNHG25's drug response | TRPC4AP's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.67, reverse +0.01; direction clear | 0.040 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.640). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-11.0, -8.8); signed map (-39.6, 7.1). **Vector** length 97.4, 36.6% of its response variance represented; |z| ≥ 3 in 1,165 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Termination* (reactome, mean cos +0.53 to 20); *Peptide chain elongation* (reactome, mean cos +0.54 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.54 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.5 | +1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.5 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | -2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +3.5 | -6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.9 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | -0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -9.4 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -4.6 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.4 | -0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | transient receptor potential cation channel subfamily C member 4 associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:35,002,404-35,092,807 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP727M231, DKFZp586C1223, dJ756N5.2, TRRP4AP, PPP1R158; previously C20orf188 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Armadillo like helical domain containing |
| Reactome | 4 pathways, smallest: TRP channels; Stimuli-sensing channels; Ion channel transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEL6](https://www.uniprot.org/uniprotkb/Q8TEL6) (Short transient receptor potential channel 4-associated protein):

> Substrate-recognition component of a DCX (DDB1-CUL4-X-box) E3 ubiquitin-protein ligase complex required for cell cycle control. The DCX(TRPC4AP) complex specifically mediates the polyubiquitination and subsequent degradation of MYC as part of the DesCEND (destruction via C-end degrons) pathway. The DesCEND (destruction via C-end degrons) pathway recognizes a C-degron located at the extreme C terminus of target proteins, leading to their ubiquitination and degradation. The DCX(TRPC4AP) complex …

**Summary**, from NCBI Gene [26133](https://www.ncbi.nlm.nih.gov/gene/26133):

> Enables phosphatase binding activity and ubiquitin-like ligase-substrate adaptor activity. Involved in protein ubiquitination and ubiquitin-dependent protein catabolic process via the C-end degron rule pathway. Located in cytosol. Part of Cul4A-RING E3 ubiquitin ligase complex. Is active in Cul4-RING E3 ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16181) · Entrez [26133](https://www.ncbi.nlm.nih.gov/gene/26133) · UniProt [Q8TEL6](https://www.uniprot.org/uniprotkb/Q8TEL6) · Ensembl [ENSG00000100991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100991)

## Data

Gene col 2054: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2054); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2054, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2054]; `tensor/DDL_lfc|DDL_z.npy` [2054]; `embed/gene_vectors.npy` [2054]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2054 or target_col == 2054). Every well: [[TRPC4AP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPC4AP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
