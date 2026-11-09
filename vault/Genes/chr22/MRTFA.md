---
symbol: "MRTFA"
type: "gene"
col: 12244
ensembl_id: "ENSG00000196588"
name: "myocardin related transcription factor A"
location: "22q13.1-q13.2"
module: 214
arm: "+"
pooled_cpm: 183.44
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 5
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/214"]
generated_by: "tahoemap"
---

# MRTFA

*myocardin related transcription factor A* — 22q13.1-q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.00× (z +18.6, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.356× (z -19.6, q 0e+00, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.803× (z -5.9, q 4e-07, down in 26 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (HepG2/C3A 0.125×, A498 0.173×, SNU-1 0.145×, A-172 0.241×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (NCI-H2347 0.506×, HepG2/C3A 0.415×, SW480 0.626×, NCI-H2030 0.505×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (Panc 03.27 0.120×, hTERT-HPNE 0.121×, SK-MEL-2 0.138×, A498 0.185×, …; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP17]] (+0.62, fdr 1e-05), [[RHOB]] (+0.62, fdr 1e-05), [[DENND5A]] (+0.56, fdr 1e-05); moves opposite to [[ITPKB]] (-0.56, fdr 6e-05), [[KIAA0753]] (-0.54, fdr 2e-05), [[MIR30DHG]] (-0.50, fdr 1e-04).
> It is in [[Module 214]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +18.6 | 0e+00 | 44/48 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.48×** | +17.2 | 0e+00 | 46/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.06×** | +13.7 | 1e-40 | 47/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +13.6 | 5e-40 | 46/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +11.5 | 9e-29 | 44/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +11.2 | 2e-27 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +8.5 | 1e-15 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +8.5 | 2e-15 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +8.2 | 2e-14 | 42/48 (KATO III, C-33 A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +8.0 | 7e-14 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +6.1 | 4e-08 | 31/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +5.6 | 9e-07 | 34/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +5.3 | 5e-06 | 28/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.79×** | +5.2 | 1e-05 | 28/49 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.8 | 6e-05 | 30/48 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.5 | 2e-04 | 28/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.4 | 3e-04 | 21/48 (HT-29, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12244.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (HepG2/C3A 0.125×, A498 0.173×, SNU-1 0.145×, A-172 0.241×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (NCI-H2347 0.506×, HepG2/C3A 0.415×, SW480 0.626×, NCI-H2030 0.505×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (Panc 03.27 0.120×, hTERT-HPNE 0.121×, SK-MEL-2 0.138×, A498 0.185×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.356×** | -19.6 | 0e+00 | 44/49 (HepG2/C3A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.363×** | -18.5 | 0e+00 | 43/44 (Panc 03.27, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.659×** | -7.9 | 5e-13 | 40/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.638×** | -7.9 | 5e-13 | 31/45 (A-427, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.803×** | -5.9 | 4e-07 | 26/49 (NCI-H2347, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.844× | -3.2 | 0.12 | 20/48 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.794× | -3.1 | 0.14 | 21/47 (CHP-212, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.852× | -3.0 | 0.15 | 21/48 (A-172, SNU-423, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.852× | -3.0 | 0.15 | 13/48 (KATO III, HEC-1-A, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 127 | 13 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +21.3) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -11.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 199 | 11 (2 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.06× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 155 | 6 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.76× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 124 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +20.9) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -11.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 145 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.439× (z -9.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 151 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +13.7) | — |
| [[NCI-H1573 (line)]] | alt | 184 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 179 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.29× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -13.6) |
| [[A498 (line)]] | wt | 323 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -9.5) |
| [[HOP62 (line)]] | alt | 111 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 134 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -24.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 149 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -14.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 104 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -13.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 143 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +17.9) | [[Selinexor (drug)]] 5 µM 0.524× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 161 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +16.3) | — |
| [[hTERT-HPNE (line)]] | wt | 167 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -21.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 162 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -10.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 150 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 203 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.30× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -13.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 156 | 3 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -15.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 193 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -19.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 173 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.71× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -13.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 158 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -18.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 186 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.50× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -10.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 154 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -14.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 137 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -9.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 155 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.9) | — |
| [[HepG2_C3A (line)]] | wt | 484 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -13.2) |
| [[Hs 766T (line)]] | wt | 192 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.30× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -13.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 119 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +17.7) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -9.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 206 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +20.0) | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -16.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 102 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.25× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -10.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 237 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -16.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 145 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -18.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 191 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 2.98× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -10.4) |
| [[HS-578T (line)]] | alt | 444 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 335 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 85.3 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -19.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 168 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 258 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -10.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 376 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -12.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 285 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -14.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 131 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +11.6) | — |
| [[NCI-H661 (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -9.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -9.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 198 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP17]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[RHOB]] | +0.62 | +0.50 / +0.64 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[DENND5A]] | +0.56 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[OSBPL9]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TMEM179B]] | +0.55 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[LRRFIP2]] | +0.55 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[HES4]] | +0.54 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[AGFG1]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[MFSD12]] | +0.53 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[PAFAH1B1]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 | pathway: RHO GTPase Effectors |
| [[FERMT2]] | +0.52 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[JUND]] | +0.52 | +0.38 / +0.55 | both halves | 7e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPKB]] | -0.56 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[KIAA0753]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[MIR30DHG]] | -0.50 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[ZCCHC4]] | -0.49 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[SMG1P6]] | -0.48 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[HSPA14]] | -0.46 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[PRIMPOL]] | -0.46 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[LNP1]] | -0.45 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[CYB5D1]] | -0.45 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[SLC43A1]] | -0.45 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[INTS2]] | -0.45 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[IVNS1ABP]] | -0.45 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 214]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.9, -0.5); signed map (-0.8, 22.9). **Vector** length 104, 38.7% of its response variance represented; |z| ≥ 3 in 1,484 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 0.5 µM |  | +5.5 | +2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.0 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +5.0 | +1.9 |
|  | [[Trametinib (drug)]] 5 µM |  | +4.7 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.6 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +4.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -5.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.0 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.4 | -1.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.2 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | myocardin related transcription factor A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1-q13.2 — chr22:40,410,281-40,636,719 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1438, MAL, MRTF-A, BSAC, MKL; previously MKL1 |
| Gene groups (HGNC) | Myocardin family |
| Reactome | 7 pathways, smallest: SUMOylation of transcription cofactors; RHO GTPases Activate Formins; SUMO E3 ligases SUMOylate target proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969V6](https://www.uniprot.org/uniprotkb/Q969V6) (Myocardin-related transcription factor A):

> Transcription coactivator that associates with the serum response factor (SRF) transcription factor to control expression of genes regulating the cytoskeleton during development, morphogenesis and cell migration. The SRF-MRTFA complex activity responds to Rho GTPase-induced changes in cellular globular actin (G-actin) concentration, thereby coupling cytoskeletal gene expression to cytoskeletal dynamics. MRTFA binds G-actin via its RPEL repeats, regulating activity of the MRTFA-SRF complex. …

**Summary**, from NCBI Gene [57591](https://www.ncbi.nlm.nih.gov/gene/57591):

> The protein encoded by this gene interacts with the transcription factor myocardin, a key regulator of smooth muscle cell differentiation. The encoded protein is predominantly nuclear and may help transduce signals from the cytoskeleton to the nucleus. This gene is involved in a specific translocation event that creates a fusion of this gene and the RNA-binding motif protein-15 gene. This translocation has been associated with acute megakaryocytic leukemia. Alternative splicing results in …

**Accessions** — [HGNC:14334](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14334) · Entrez [57591](https://www.ncbi.nlm.nih.gov/gene/57591) · UniProt [Q969V6](https://www.uniprot.org/uniprotkb/Q969V6) · Ensembl [ENSG00000196588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196588)

## Data

Gene col 12244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12244); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12244]; `tensor/DDL_lfc|DDL_z.npy` [12244]; `embed/gene_vectors.npy` [12244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12244 or target_col == 12244). Every well: [[MRTFA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRTFA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
