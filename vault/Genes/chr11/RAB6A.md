---
symbol: "RAB6A"
type: "gene"
col: 10626
ensembl_id: "ENSG00000175582"
name: "RAB6A, member RAS oncogene family"
location: "11q13.4"
module: 40
arm: "+"
pooled_cpm: 297.39
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# RAB6A

*RAB6A, member RAS oncogene family* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.17× (z +4.5, q 0.004, up in 21 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 4 lines (NCI-H460 2.67×, PANC-1 1.80×, SW480 1.73×, NCI-H1792 2.08×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (PANC-1 2.18×, NCI-H460 2.42×, SW480 1.66×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H460 2.61×, PANC-1 1.56×; ⚠ cell-cycle shift, explains ~0% of this change); [[Chlorhexidine (diacetate) (drug)]] 5 µM in 1 line (SNU-1 1.91×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (PANC-1 1.61×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.484× (z -21.2, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIK3C2A]] (+0.83, fdr 7e-06), [[SRP54-AS1]] (+0.76, fdr 7e-06), [[FBXO42]] (+0.75, fdr 7e-06); moves opposite to [[CHTOP]] (-0.73, fdr 7e-06), [[TMEM185B]] (-0.73, fdr 7e-06), [[CSTF2T]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10626.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 4 lines (NCI-H460 2.67×, PANC-1 1.80×, SW480 1.73×, NCI-H1792 2.08×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (PANC-1 2.18×, NCI-H460 2.42×, SW480 1.66×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H460 2.61×, PANC-1 1.56×; ⚠ cell-cycle shift, explains ~0% of this change); [[Chlorhexidine (diacetate) (drug)]] 5 µM in 1 line (SNU-1 1.91×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (PANC-1 1.61×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.5 | 0.004 | 21/49 (COLO 205, LoVo, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.23×** | +4.3 | 0.004 | 29/49 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.047 | 23/48 (PANC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.092 | 22/48 (CFPAC-1, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.14 | 13/48 (HCT15, NCI-H23, …) | top dose only | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.17 | 17/48 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.17 | 18/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10626.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.484×** | -21.2 | 0e+00 | 47/48 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.467×** | -15.8 | 0e+00 | 47/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.514×** | -14.4 | 2e-44 | 46/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.551×** | -12.4 | 5e-33 | 41/44 (AsPC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.576×** | -11.9 | 2e-30 | 45/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.585×** | -11.6 | 5e-29 | 42/48 (BT-474, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.596×** | -10.7 | 7e-25 | 44/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.587×** | -10.6 | 2e-24 | 42/45 (C-33 A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.586×** | -10.1 | 2e-22 | 38/49 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.669×** | -8.7 | 3e-16 | 37/48 (AsPC-1, A-172, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.685×** | -7.9 | 2e-13 | 40/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.753×** | -6.1 | 4e-08 | 36/48 (hTERT-HPNE, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.728×** | -6.0 | 7e-08 | 41/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.735×** | -5.9 | 2e-07 | 35/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.822×** | -5.7 | 3e-07 | 27/48 (A-172, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.788×** | -5.1 | 1e-05 | 35/48 (KATO III, HS-578T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.814×** | -4.5 | 3e-04 | 27/48 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.817×** | -4.4 | 4e-04 | 27/48 (LoVo, SW48, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.836× | -3.9 | 0.003 | 20/49 (SW1417, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.885× | -3.6 | 0.007 | 13/48 (NCI-H2347, KATO III, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.847× | -3.6 | 0.007 | 19/48 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.844× | -3.5 | 0.012 | 17/47 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.857× | -3.4 | 0.017 | 18/49 (KATO III, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10626. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 363 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -21.3) |
| [[CFPAC-1 (line)]] | alt | 499 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.411× (z -14.4) |
| [[A-172 (line)]] | wt | 341 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -32.6) |
| [[HS-578T (line)]] | alt | 407 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -27.2) |
| [[AsPC-1 (line)]] | alt | 416 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.492× (z -12.9) |
| [[hTERT-HPNE (line)]] | wt | 291 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -16.8) |
| [[KATO III (line)]] | alt | 416 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 297 | 1 (1 ⚠) | 6 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.08× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -21.5) |
| [[NCI-H460 (line)]] | wt | 184 | 4 (4 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.67× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -12.4) |
| [[PANC-1 (line)]] | alt | 272 | 4 (3 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.61× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -22.2) |
| [[SNU-423 (line)]] | alt | 330 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -28.2) |
| [[HOP62 (line)]] | alt | 227 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -19.8) |
| [[LoVo (line)]] | wt | 295 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -15.1) |
| [[RPMI-7951 (line)]] | alt | 311 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -25.2) |
| [[C32 (line)]] | wt | 322 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -17.9) |
| [[J82 (line)]] | alt | 347 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -26.9) |
| [[SW 900 (line)]] | alt | 320 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -13.3) |
| [[A-427 (line)]] | wt | 265 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.443× (z -13.3) |
| [[A498 (line)]] | wt | 185 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.392× (z -12.8) |
| [[H4 (line)]] | wt | 282 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 315 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 262 | 2 (2 ⚠) | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -16.2) |
| [[A549 (line)]] | wt | 253 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -12.6) |
| [[BT-474 (line)]] | alt | 568 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.427× (z -14.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.614× (z -11.2) |
| [[COLO 205 (line)]] | alt | 279 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.24× (z +12.5) ⚠ toxic; cell-cycle shift, explains ~78% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.436× (z -8.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.566× (z -8.5) |
| [[Hs 766T (line)]] | wt | 368 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -17.7) |
| [[MIA PaCa-2 (line)]] | alt | 310 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 250 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -20.1) |
| [[Panc 03.27 (line)]] | alt | 338 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.551× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.662× (z -9.2) |
| [[SNU-1 (line)]] | wt | 310 | 1 | 2 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.91× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.536× (z -9.7) |
| [[SW480 (line)]] | alt | 307 | 2 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.73× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.569× (z -10.0) ⚠ toxic |
| [[HCT15 (line)]] | alt | 353 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 121 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.319× (z -11.1) |
| [[SW1417 (line)]] | alt | 323 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.529× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 247 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.2) |
| [[C-33 A (line)]] | alt | 220 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -15.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 195 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.605× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 253 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 280 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.455× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 224 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.417× (z -11.2) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 230 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 300 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 346 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10626), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3C2A]] | +0.83 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.76 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[FBXO42]] | +0.75 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[QPCTL]] | +0.73 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[TULP3]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[MAX]] | +0.73 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[KDELR1]] | +0.73 | +0.74 / +0.74 | both halves | 7e-06 | pathway: Golgi-to-ER retrograde transport |
| [[TBC1D20]] | +0.73 | +0.70 / +0.67 | both halves | 7e-06 | pathway: Rab regulation of trafficking; STRING 461 |
| [[HDAC3]] | +0.72 | +0.78 / +0.65 | both halves | 7e-06 | pathway: Signaling by NOTCH |
| [[MACO1]] | +0.72 | +0.80 / +0.62 | both halves | 7e-06 |  |
| [[DPM1]] | +0.71 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.71 | +0.76 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHTOP]] | -0.73 | -0.68 / -0.72 | both halves | 7e-06 |  |
| [[TMEM185B]] | -0.73 | -0.75 / -0.67 | both halves | 7e-06 |  |
| [[CSTF2T]] | -0.71 | -0.73 / -0.68 | both halves | 7e-06 |  |
| [[SRCAP]] | -0.70 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[PUF60]] | -0.69 | -0.64 / -0.68 | both halves | 7e-06 |  |
| [[SFPQ]] | -0.69 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[COA7]] | -0.69 | -0.75 / -0.60 | both halves | 7e-06 |  |
| [[ZNF507]] | -0.68 | -0.75 / -0.58 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.68 | -0.69 / -0.65 | both halves | 7e-06 |  |
| [[ZNF776]] | -0.67 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[ENC1]] | -0.67 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[VEZF1]] | -0.67 | -0.60 / -0.63 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDS1]] | B | CDS1 activity raises RAB6A's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.17× lower at baseline in the lines without CDS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.786). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (5.0, -18.5); signed map (-42.8, 13.2). **Vector** length 136, 55.3% of its response variance represented; |z| ≥ 3 in 1,291 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +9.8 | -1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.7 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.9 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.6 | +4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.5 | -8.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.8 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | -0.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.2 | -15.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.6 | -14.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.0 | -21.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.8 | -5.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.2 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.3 | -3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | RAB6A, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:73,675,638-73,761,137 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RAB6 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 15 pathways, smallest: Pre-NOTCH Processing in Golgi; TBC/RABGAPs; COPI-independent Golgi-to-ER retrograde traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [P20340](https://www.uniprot.org/uniprotkb/P20340) (Ras-related protein Rab-6A):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB6A acts as a regulator of COPI-independent retrograde transport from the Golgi apparatus towards the endoplasmic …

**Summary**, from NCBI Gene [5870](https://www.ncbi.nlm.nih.gov/gene/5870):

> This gene encodes a member of the RAB family, which belongs to the small GTPase superfamily. GTPases of the RAB family bind to various effectors to regulate the targeting and fusion of transport carriers to acceptor compartments. This protein is located at the Golgi apparatus, which regulates trafficking in both a retrograde (from early endosomes and Golgi to the endoplasmic reticulum) and an anterograde (from the Golgi to the plasma membrane) directions. Myosin II is an effector of this …

**Accessions** — [HGNC:9786](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9786) · Entrez [5870](https://www.ncbi.nlm.nih.gov/gene/5870) · UniProt [P20340](https://www.uniprot.org/uniprotkb/P20340) · Ensembl [ENSG00000175582](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175582)

## Data

Gene col 10626: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10626); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10626, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10626]; `tensor/DDL_lfc|DDL_z.npy` [10626]; `embed/gene_vectors.npy` [10626]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10626 or target_col == 10626). Every well: [[RAB6A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB6A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
