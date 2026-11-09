---
symbol: "LMO7"
type: "gene"
col: 5823
ensembl_id: "ENSG00000136153"
name: "LIM domain 7"
location: "13q22.2"
module: 31
arm: "+"
pooled_cpm: 534.91
n_lines_expressing: 39
n_dd_up: 6
n_dd_down: 25
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 44
direction_downstream: 39
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# LMO7

*LIM domain 7* — 13q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.47× (z +22.8, q 0e+00, up in 25 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Peretinoin (drug)]] 0.5 µM: 1.20× (z +4.5, q 7e-04, up in 16 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (J82 4.91×, HOP62 3.82×, HEC-1-A 3.96×, NCI-H460 4.46×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (J82 4.34×, HOP62 3.88×, SW 900 4.34×, HEC-1-A 3.78×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (J82 4.04×, SW 900 4.31×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 2.49×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 1.71×).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.560× (z -14.6, q 1e-45, down in 35 of 37 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.725× (z -8.1, q 3e-14, down in 28 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EZR]] (+0.63, fdr 7e-06), [[LMO7DN]] (+0.62, fdr 9e-06, ⚠ read-through risk), [[CD55]] (+0.59, fdr 2e-05), [[C1orf116]] (+0.57, fdr 7e-06); moves opposite to [[HDHD5]] (-0.47, fdr 2e-04), [[XYLT2]] (-0.47, fdr 2e-04), [[LINC02985]] (-0.46, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 44 arrows point to it, the strongest [[C1orf116]] → it (grade B ⚠); 39 go from it, the strongest it → [[DSG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5823.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (J82 4.91×, HOP62 3.82×, HEC-1-A 3.96×, NCI-H460 4.46×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (J82 4.34×, HOP62 3.88×, SW 900 4.34×, HEC-1-A 3.78×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (J82 4.04×, SW 900 4.31×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 2.49×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 1.71×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.47×** | +22.8 | 0e+00 | 25/38 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +22.7 | 0e+00 | 21/33 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +18.4 | 0e+00 | 23/34 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.25×** | +5.7 | 2e-06 | 23/37 (COLO 205, A-172, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.20× | +4.5 | 7e-04 | 16/36 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.20×** | +4.5 | 8e-04 | 20/36 (COLO 205, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.15× | +3.5 | 0.033 | 12/38 (RKO, J82, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.036 | 11/38 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.18× | +3.4 | 0.036 | 16/36 (A-172, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.15× | +3.4 | 0.036 | 11/37 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.14× | +3.3 | 0.048 | 10/36 (HepG2/C3A, HOP62, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.26× | +3.1 | 0.11 | 12/29 (HOP62, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5823.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.560×** | -14.6 | 1e-45 | 35/37 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.571×** | -14.2 | 4e-43 | 33/37 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.610×** | -12.5 | 1e-33 | 31/37 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.723×** | -11.6 | 6e-29 | 28/38 (SW48, AsPC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.639×** | -11.3 | 1e-27 | 30/37 (SW48, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.673×** | -9.6 | 6e-20 | 24/36 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.691×** | -9.3 | 9e-19 | 31/37 (SW48, SW1417, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.725×** | -8.1 | 3e-14 | 28/37 (SW48, NCI-H2347, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.744×** | -7.1 | 1e-10 | 27/37 (SW48, HT-29, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.591×** | -6.9 | 2e-10 | 28/37 (SW48, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.592×** | -6.9 | 2e-10 | 27/37 (SW48, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.754×** | -6.9 | 3e-10 | 24/37 (SW48, Panc 03.27, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.827×** | -6.8 | 5e-10 | 21/37 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.793×** | -5.9 | 2e-07 | 26/37 (CFPAC-1, A-427, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.644×** | -5.8 | 2e-07 | 26/37 (SW48, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.664×** | -5.4 | 2e-06 | 25/37 (SW48, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.810×** | -5.3 | 3e-06 | 20/37 (A-427, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.676×** | -5.2 | 6e-06 | 23/37 (SW48, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.875× | -4.8 | 5e-05 | 10/37 (HOP62, HCT15, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.718×** | -4.4 | 3e-04 | 19/38 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.903× | -3.7 | 0.005 | 10/38 (CFPAC-1, A549, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.823×** | -3.5 | 0.009 | 14/37 (SW48, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.866× | -3.4 | 0.012 | 10/37 (SW48, LoVo, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | 0.874× | -3.4 | 0.013 | 11/37 (CFPAC-1, A549, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | 0.876× | -3.3 | 0.018 | 10/38 (SW48, LoVo, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 1,814 | 0 | 19 (14 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -24.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.196× (z -16.0) |
| [[CFPAC-1 (line)]] | alt | 818 | 0 | 16 (13 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0988× (z -25.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.326× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 1,290 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0739× (z -27.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.369× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 1,658 | 0 | 10 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -25.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2347 (line)]] | alt | 1,005 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -19.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.290× (z -13.2) |
| [[HT-29 (line)]] | alt | 1,712 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -19.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.295× (z -10.0) |
| [[LoVo (line)]] | wt | 1,829 | 1 (1 ⚠) | 8 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 5.24× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.114× (z -21.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.327× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 1,254 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -19.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.309× (z -11.3) |
| [[A-427 (line)]] | wt | 545 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.278× (z -16.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.489× (z -9.1) |
| [[Hs 766T (line)]] | wt | 1,208 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -15.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.376× (z -8.8) |
| [[KATO III (line)]] | alt | 1,410 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -18.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.444× (z -8.5) |
| [[SW1417 (line)]] | alt | 315 | 3 (3 ⚠) | 5 (5 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.07× (z +10.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -15.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HCT15 (line)]] | alt | 293 | 2 (2 ⚠) | 5 (5 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.67× (z +14.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.340× (z -12.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H460 (line)]] | wt | 141 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.49× (z +11.0) | — |
| [[SW480 (line)]] | alt | 766 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -16.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HOP62 (line)]] | alt | 213 | 4 (4 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +19.6) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.482× (z -10.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 227 | 3 (3 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +19.1) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.497× (z -9.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[hTERT-HPNE (line)]] | wt | 210 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +12.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 1,271 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -17.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HS-578T (line)]] | alt | 172 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +13.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 313 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.91× (z +23.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.634× (z -9.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 228 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +12.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 135 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +15.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 256 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.95× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -13.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[COLO 205 (line)]] | alt | 1,839 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -11.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 149 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +18.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 171 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +13.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 195 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +15.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 148 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.369× (z -10.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[BT-474 (line)]] | alt | 137 | 0 | 2 | — | [[Osimertinib (mesylate) (drug)]] 5 µM 0.323× (z -8.7) |
| [[H4 (line)]] | wt | 205 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +14.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 162 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +10.9) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 144 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 140 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 286 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.71× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 99.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 55.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 117 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 120 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1,153 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 73.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 534 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.3 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 94.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 119 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 91.0 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 124 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 389 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EZR]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[LMO7DN]] | +0.62 | +0.57 / +0.62 | both halves | 9e-06 | ⚠ **readthrough risk**: LMO7DN lies 10.7 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[CD55]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[C1orf116]] | +0.57 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ANXA3]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[YWHAZ]] | +0.55 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[DIAPH1]] | +0.55 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[C4BPB]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[LSMEM2]] | +0.54 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[MISP]] | +0.54 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[JUP]] | +0.53 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[GPRC5A]] | +0.53 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[KLF5]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDHD5]] | -0.47 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[XYLT2]] | -0.47 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[LINC02985]] | -0.46 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[PGAP2]] | -0.46 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[GLMN]] | -0.45 | -0.35 / -0.49 | both halves | 1e-04 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[CCDC107]] | -0.45 | -0.36 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 43, C 1. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1orf116]] | B | C1orf116 activity raises LMO7's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 5.54× lower at baseline in the lines without C1orf116 | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[COL17A1]] | B | COL17A1 activity raises LMO7's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 5.71× lower at baseline in the lines without COL17A1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[ITGB4]] | B | ITGB4 activity raises LMO7's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 4.75× lower at baseline in the lines without ITGB4 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[CDH1]] | B | CDH1 activity raises LMO7's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 4.90× lower at baseline in the lines without CDH1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[MPZL2]] | B | MPZL2 activity raises LMO7's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 5.09× lower at baseline in the lines without MPZL2 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[MROH3P]] | B | MROH3P activity raises LMO7's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 4.45× lower at baseline in the lines without MROH3P | 4e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[HS3ST1]] | B | HS3ST1 activity raises LMO7's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 5.03× lower at baseline in the lines without HS3ST1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[ST14]] | B | ST14 activity raises LMO7's level | lines that do not express ST14 (32) vs lines expressing it (18) | 5.09× lower at baseline in the lines without ST14 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[ITGB6]] | B | ITGB6 activity raises LMO7's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 4.76× lower at baseline in the lines without ITGB6 | 8e-04 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[KIAA0040]] | B | KIAA0040 activity raises LMO7's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 3.81× lower at baseline in the lines without KIAA0040 | 1e-03 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[CATSPERB]] | B | CATSPERB activity raises LMO7's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 4.32× lower at baseline in the lines without CATSPERB | 0.001 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises LMO7's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.88× lower at baseline in the lines without TMPRSS4 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 38, C 1. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSG2]] | B | LMO7 activity raises DSG2's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 3.50× lower at baseline in the lines without LMO7 | 0.007 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[GLMN]] | B | LMO7 activity lowers GLMN's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 1.70× higher at baseline in the lines without LMO7 | 0.008 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[MFSD6]] | B | LMO7 activity raises MFSD6's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.22× lower at baseline in the lines without LMO7 | 0.010 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[MYO5B]] | B | LMO7 activity raises MYO5B's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 4.24× lower at baseline in the lines without LMO7 | 0.016 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[MPZL2]] | B | LMO7 activity raises MPZL2's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 4.02× lower at baseline in the lines without LMO7 | 0.017 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[TJP2]] | B | LMO7 activity raises TJP2's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.99× lower at baseline in the lines without LMO7 | 0.018 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[KLF5]] | B | LMO7 activity raises KLF5's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 3.39× lower at baseline in the lines without LMO7 | 0.019 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[TES]] | B | LMO7 activity raises TES's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.96× lower at baseline in the lines without LMO7 | 0.022 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[ANXA3]] | B | LMO7 activity raises ANXA3's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 3.27× lower at baseline in the lines without LMO7 | 0.022 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[CDH1]] | B | LMO7 activity raises CDH1's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 4.68× lower at baseline in the lines without LMO7 | 0.032 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[HS3ST1]] | B | LMO7 activity raises HS3ST1's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 3.04× lower at baseline in the lines without LMO7 | 0.033 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[MROH3P]] | B | LMO7 activity raises MROH3P's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.69× lower at baseline in the lines without LMO7 | 0.036 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.536). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.1, 57.9); signed map (6.8, 34.1). **Vector** length 135, 44.0% of its response variance represented; |z| ≥ 3 in 1,422 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.8 | +22.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.2 | +22.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +11.2 | +18.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.2 | +4.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.9 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.5 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.8 | -9.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.0 | -11.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.9 | -5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.8 | -6.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.3 | -7.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.3 | -6.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.1 | -5.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | LIM domain 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q22.2 — chr13:75,620,434-75,859,870 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBX20, KIAA0858; previously FBXO20 |
| Gene groups (HGNC) | LIM domain containing; PDZ domain containing |
| Reactome | 7 pathways, smallest: Signaling by ALK fusions and activated point mutants; Signaling by ALK in cancer; Neddylation |
| Matched by | ensembl_id |

UniProt [Q8WWI1](https://www.uniprot.org/uniprotkb/Q8WWI1) carries no function annotation.

**Summary**, from NCBI Gene [4008](https://www.ncbi.nlm.nih.gov/gene/4008):

> This gene encodes a protein containing a calponin homology (CH) domain, a PDZ domain, and a LIM domain, and may be involved in protein-protein interactions. Several alternatively spliced transcript variants encoding different isoforms have been found for this gene, however, the full-length nature of some variants is not known. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:6646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6646) · Entrez [4008](https://www.ncbi.nlm.nih.gov/gene/4008) · UniProt [Q8WWI1](https://www.uniprot.org/uniprotkb/Q8WWI1) · Ensembl [ENSG00000136153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136153)

## Data

Gene col 5823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5823); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5823]; `tensor/DDL_lfc|DDL_z.npy` [5823]; `embed/gene_vectors.npy` [5823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5823 or target_col == 5823). Every well: [[LMO7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMO7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
