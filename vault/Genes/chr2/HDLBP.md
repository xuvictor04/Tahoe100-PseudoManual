---
symbol: "HDLBP"
type: "gene"
col: 3709
ensembl_id: "ENSG00000115677"
name: "high density lipoprotein binding protein"
location: "2q37.3"
module: 42
arm: "+"
pooled_cpm: 398.58
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# HDLBP

*high density lipoprotein binding protein* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.86× (z +13.8, q 2e-40, up in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.22× (z +4.6, q 6e-04, up in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (PANC-1 2.60×, SHP-77 3.11×, A-427 2.43×, A549 2.60×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (PANC-1 2.57×, A-427 2.95×, SW480 2.41×, A549 2.70×, …; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (NCI-H1573 2.10×, PANC-1 1.66×, NCI-H460 1.69×); [[Auranofin (drug)]] 5 µM in 2 lines (Panc 03.27 1.81×, SHP-77 1.99×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.573× (z -12.3, q 4e-32, down in 38 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.627× (z -10.7, q 3e-24, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED2]] (+0.76, fdr 7e-06), [[CANX]] (+0.75, fdr 7e-06), [[COPG1]] (+0.74, fdr 7e-06); moves opposite to [[ZNF670]] (-0.59, fdr 2e-05), [[PPP1R35]] (-0.58, fdr 2e-05, ⚠ PPP1R35 in the vector space only through flagged drug-doses), [[OXLD1]] (-0.56, fdr 1e-04), [[IMP3]] (-0.55, fdr 2e-04).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SEC22B]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3709.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (PANC-1 2.60×, SHP-77 3.11×, A-427 2.43×, A549 2.60×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (PANC-1 2.57×, A-427 2.95×, SW480 2.41×, A549 2.70×, …; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (NCI-H1573 2.10×, PANC-1 1.66×, NCI-H460 1.69×); [[Auranofin (drug)]] 5 µM in 2 lines (Panc 03.27 1.81×, SHP-77 1.99×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +13.8 | 2e-40 | 43/44 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +13.5 | 2e-39 | 43/49 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +7.2 | 1e-10 | 33/45 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +4.6 | 6e-04 | 27/48 (Panc 03.27, SHP-77, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.6 | 6e-04 | 0/50 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +4.4 | 0.001 | 26/48 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.069 | 12/48 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.15× | +3.1 | 0.11 | 15/48 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.11 | 5/48 (LOX-IMVI, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 1.29× | +3.1 | 0.11 | 22/45 (SW480, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3709.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.573×** | -12.3 | 4e-32 | 38/47 (HT-29, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.627×** | -10.7 | 3e-24 | 42/48 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.706×** | -8.0 | 3e-13 | 38/48 (A498, SW 900, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.734×** | -7.1 | 2e-10 | 31/48 (A498, SW 900, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.748×** | -6.7 | 3e-09 | 37/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.818×** | -6.1 | 7e-08 | 29/49 (NCI-H2030, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.758×** | -6.1 | 7e-08 | 31/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.777×** | -5.8 | 5e-07 | 35/48 (RPMI-7951, HOP62, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.785×** | -5.5 | 2e-06 | 36/48 (SW 900, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.793×** | -5.3 | 6e-06 | 29/48 (A498, SW 900, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.805×** | -4.8 | 9e-05 | 28/48 (H4, C-33 A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.817×** | -4.6 | 2e-04 | 26/48 (NCI-H2347, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -4.5 | 2e-04 | 18/48 (HOP62, HS-578T, …) | top dose only | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **0.824×** | -4.4 | 4e-04 | 24/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -4.3 | 6e-04 | 16/48 (RPMI-7951, NCI-H2030, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.721×** | -3.9 | 0.003 | 24/49 (AsPC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.859× | -3.3 | 0.032 | 14/47 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | 0.868× | -3.2 | 0.035 | 9/48 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.822×** | -3.2 | 0.037 | 23/48 (SW 1271, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.870× | -3.2 | 0.038 | 16/48 (hTERT-HPNE, SW 900, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.873× | -3.1 | 0.047 | 19/48 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.898× | -3.1 | 0.048 | 4/48 (KATO III, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.866× | -3.1 | 0.054 | 11/47 (A-172, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.876× | -3.0 | 0.056 | 15/48 (LS 180, SW 900, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3709. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 420 | 2 (2 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.82× (z +11.6) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.472× (z -15.2) |
| [[HOP62 (line)]] | alt | 527 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +12.9) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.444× (z -12.9) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.555× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 381 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.69× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.629× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.582× (z -9.8) |
| [[A-172 (line)]] | wt | 448 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +11.4) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.535× (z -10.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.608× (z -8.5) |
| [[HS-578T (line)]] | alt | 455 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +13.7) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.479× (z -11.9) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.540× (z -10.4) |
| [[HT-29 (line)]] | alt | 555 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.395× (z -13.8) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.484× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 710 | 2 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +10.5) | [[Belinostat (drug)]] 5 µM 0.471× (z -10.7) |
| [[PANC-1 (line)]] | alt | 367 | 4 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.66× (z +10.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.596× (z -10.1) ⚠ toxic |
| [[SW 900 (line)]] | alt | 418 | 0 | 5 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.392× (z -13.7) |
| [[A549 (line)]] | wt | 369 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +16.2) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.577× (z -9.0) |
| [[J82 (line)]] | alt | 287 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +12.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.593× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 342 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +13.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -11.1) ⚠ cell-cycle shift, explains ~23% of this change |
| [[NCI-H23 (line)]] | alt | 328 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.94× (z +10.8) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.601× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 367 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.522× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 528 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.74× (z +8.6) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.548× (z -9.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.571× (z -8.7) |
| [[A-427 (line)]] | wt | 359 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +19.0) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.573× (z -9.5) ⚠ toxic |
| [[C-33 A (line)]] | alt | 329 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +15.4) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.551× (z -8.9) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 315 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +13.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 489 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +13.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 530 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.27× (z +12.3) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.518× (z -9.7) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 354 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.81× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.546× (z -10.6) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 229 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +16.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.99× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 243 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.05× (z +11.1) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.513× (z -10.3) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 322 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +14.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 271 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +16.9) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.504× (z -12.6) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 481 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.490× (z -12.0) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.522× (z -11.4) |
| [[C32 (line)]] | wt | 146 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +12.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 400 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.363× (z -10.1) ⚠ toxic |
| [[H4 (line)]] | wt | 545 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.440× (z -10.2) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.481× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 361 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 232 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +15.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 312 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.538× (z -8.6) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 406 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.615× (z -8.5) |
| [[HCT15 (line)]] | alt | 651 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.385× (z -11.4) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 394 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.532× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 585 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.485× (z -8.8) ⚠ toxic |
| [[KATO III (line)]] | alt | 387 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.406× (z -11.7) ⚠ toxic |
| [[LoVo (line)]] | wt | 510 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.441× (z -11.0) ⚠ toxic |
| [[LS 180 (line)]] | wt | 478 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.439× (z -9.9) ⚠ toxic |
| [[RKO (line)]] | wt | 331 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.77× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 503 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.430× (z -11.3) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 357 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 333 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 360 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 380 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 689 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 426 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 381 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3709), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED2]] | +0.76 | +0.77 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[CANX]] | +0.75 | +0.73 / +0.80 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication |
| [[COPG1]] | +0.74 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ARF1]] | +0.73 | +0.67 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[RPN1]] | +0.72 | +0.67 / +0.78 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication |
| [[HYOU1]] | +0.70 | +0.73 / +0.69 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication |
| [[USO1]] | +0.69 | +0.60 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SLC39A7]] | +0.68 | +0.77 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SEL1L]] | +0.68 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[SRPRA]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[GOLGA3]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[DAP]] | +0.66 | +0.56 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF670]] | -0.59 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[PPP1R35]] ⚠ | -0.58 | -0.47 / -0.61 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[OXLD1]] | -0.56 | -0.34 / -0.63 | both halves | 1e-04 |  |
| [[IMP3]] | -0.55 | -0.30 / -0.66 | both halves | 2e-04 |  |
| [[BLOC1S4]] | -0.55 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[RDH14]] | -0.55 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[MRPL46]] | -0.54 | -0.30 / -0.64 | both halves | 2e-04 |  |
| [[YTHDF2]] | -0.54 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[CELF1]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[DDX52]] | -0.54 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[EID2]] | -0.53 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[BMS1P1]] | -0.53 | -0.32 / -0.64 | both halves | 2e-04 |  |
| [[ZNF593]] | -0.53 | -0.32 / -0.64 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEC22B]] | C | SEC22B's natural level strengthens HDLBP's drug response | SEC22B's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.07; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.5, -18.4); signed map (-55.9, 8.1). **Vector** length 152, 57.6% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.57 to 11); *Asparagine N-linked glycosylation* (reactome, mean cos +0.55 to 23); *Maturation of DENV proteins* (reactome, mean cos +0.58 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +12.1 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.9 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.5 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +4.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.9 | +4.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +3.5 | +1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.5 | +1.3 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | +3.5 | +2.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +3.2 | +2.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.2 | -12.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -6.0 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.9 | -5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -5.1 | -6.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -5.0 | -5.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.7 | -3.3 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -3.7 | -3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | high density lipoprotein binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,227,264-241,317,061 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HBP; previously VGL |
| Hallmark sets | GLYCOLYSIS, HYPOXIA |
| Reactome | 7 pathways, smallest: HDL clearance; Plasma lipoprotein clearance; Plasma lipoprotein assembly, remodeling, and clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00341](https://www.uniprot.org/uniprotkb/Q00341) (Vigilin):

> Appears to play a role in cell sterol metabolism. It may function to protect cells from over-accumulation of cholesterol.

**Summary**, from NCBI Gene [3069](https://www.ncbi.nlm.nih.gov/gene/3069):

> The protein encoded by this gene binds high density lipoprotein (HDL) and may function to regulate excess cholesterol levels in cells. The encoded protein also binds RNA and can induce heterochromatin formation. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:4857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4857) · Entrez [3069](https://www.ncbi.nlm.nih.gov/gene/3069) · UniProt [Q00341](https://www.uniprot.org/uniprotkb/Q00341) · Ensembl [ENSG00000115677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115677)

## Data

Gene col 3709: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3709); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3709, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3709]; `tensor/DDL_lfc|DDL_z.npy` [3709]; `embed/gene_vectors.npy` [3709]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3709 or target_col == 3709). Every well: [[HDLBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDLBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
