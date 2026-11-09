---
symbol: "LCOR"
type: "gene"
col: 12161
ensembl_id: "ENSG00000196233"
name: "ligand dependent nuclear receptor corepressor"
location: "10q24.1"
module: 60
arm: "-"
pooled_cpm: 272.72
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# LCOR

*ligand dependent nuclear receptor corepressor* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.61× (z +4.3, q 0.010, up in 30 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (A549 2.64×, NCI-H23 1.81×, A-427 1.64×, A498 1.72×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (SW480 1.77×, A549 1.88×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A549 2.07×; ⚠ cell-cycle shift, explains ~7% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SW480 3.67×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 2.06×).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.494× (z -15.5, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOP1A]] (+0.63, fdr 7e-06), [[EBAG9]] (+0.61, fdr 2e-05), [[MAP3K1]] (+0.59, fdr 1e-05); moves opposite to [[PWWP3A]] (-0.57, fdr 2e-05), [[DAP3]] (-0.57, fdr 1e-05), [[UFD1]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12161.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (A549 2.64×, NCI-H23 1.81×, A-427 1.64×, A498 1.72×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (SW480 1.77×, A549 1.88×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A549 2.07×; ⚠ cell-cycle shift, explains ~7% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SW480 3.67×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 2.06×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +4.3 | 0.010 | 30/49 (SW480, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.20× | +4.0 | 0.019 | 21/48 (SW1417, SW 900, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.2 | 0.23 | 20/48 (A549, NCI-H23, …) | all doses, flat | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.26 | 13/48 (HOP62, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.0 | 0.26 | 23/48 (SW480, A549, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 18 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12161.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.494×** | -15.5 | 0e+00 | 47/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.532×** | -12.8 | 4e-35 | 43/45 (H4, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.561×** | -12.7 | 1e-34 | 47/49 (A-172, H4, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.593×** | -11.0 | 4e-26 | 46/47 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.665×** | -8.9 | 5e-17 | 43/48 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.660×** | -8.8 | 2e-16 | 35/44 (A-427, A549, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.673×** | -8.4 | 5e-15 | 32/47 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.704×** | -7.7 | 9e-13 | 41/48 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.713×** | -7.4 | 7e-12 | 36/48 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.723×** | -7.1 | 7e-11 | 36/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.733×** | -6.8 | 5e-10 | 34/48 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.725×** | -6.7 | 1e-09 | 41/48 (HT-29, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.815×** | -6.3 | 9e-09 | 26/49 (NCI-H1792, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.766×** | -5.8 | 2e-07 | 36/48 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.566×** | -5.1 | 1e-05 | 36/45 (NCI-H1792, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.873× | -4.2 | 9e-04 | 13/48 (A-172, BT-474, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.874× | -2.9 | 0.076 | 14/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.5 µM |  | 0.876× | -2.9 | 0.087 | 9/48 (A-427, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12161. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 220 | 0 | 12 (9 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.338× (z -18.4) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.558× (z -9.9) |
| [[HOP62 (line)]] | alt | 324 | 0 | 8 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.350× (z -15.7) |
| [[NCI-H1573 (line)]] | alt | 203 | 0 | 8 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.384× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 303 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -17.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 339 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.477× (z -10.0) |
| [[A549 (line)]] | wt | 254 | 3 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +19.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.298× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[CFPAC-1 (line)]] | alt | 369 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.411× (z -13.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.449× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 647 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.323× (z -13.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.478× (z -8.9) |
| [[HT-29 (line)]] | alt | 416 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Auranofin (drug)]] 5 µM 0.435× (z -11.0) |
| [[SNU-423 (line)]] | alt | 374 | 0 | 6 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -12.5) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.444× (z -11.9) |
| [[BT-474 (line)]] | alt | 278 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Lonafarnib (drug)]] 5 µM 0.0536× (z -14.9) ⚠ toxic |
| [[C32 (line)]] | wt | 226 | 1 | 4 (3 ⚠) | [[Ponatinib (drug)]] 5 µM 2.06× (z +9.1) | [[Auranofin (drug)]] 5 µM 0.308× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 286 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.390× (z -15.9) |
| [[Hs 766T (line)]] | wt | 223 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.354× (z -13.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.467× (z -9.9) |
| [[LS 180 (line)]] | wt | 313 | 0 | 5 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.490× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 224 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.361× (z -13.8) |
| [[A498 (line)]] | wt | 234 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.450× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.496× (z -9.9) |
| [[H4 (line)]] | wt | 232 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.377× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 212 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.460× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.501× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 227 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Auranofin (drug)]] 5 µM 0.491× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 272 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -10.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.500× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 296 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.443× (z -13.1) |
| [[PANC-1 (line)]] | alt | 304 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.510× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.571× (z -10.0) |
| [[SW 900 (line)]] | alt | 341 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.454× (z -11.5) |
| [[A-427 (line)]] | wt | 215 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.300× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.560× (z -9.0) |
| [[LoVo (line)]] | wt | 315 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.540× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 207 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.346× (z -13.0) |
| [[SHP-77 (line)]] | alt | 326 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.411× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.492× (z -9.5) |
| [[SW48 (line)]] | wt | 199 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.451× (z -9.2) |
| [[SW480 (line)]] | alt | 265 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 1.77× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.67× (z +9.8) | [[Auranofin (drug)]] 5 µM 0.616× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 237 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.409× (z -10.6) |
| [[C-33 A (line)]] | alt | 302 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.431× (z -11.2) |
| [[COLO 205 (line)]] | alt | 256 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.483× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.505× (z -9.8) |
| [[HS-578T (line)]] | alt | 169 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.438× (z -10.0) |
| [[KATO III (line)]] | alt | 284 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.478× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SK-MEL-2 (line)]] | alt | 192 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.374× (z -14.3) |
| [[SNU-1 (line)]] | wt | 239 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.476× (z -9.0) |
| [[SW1417 (line)]] | alt | 344 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.455× (z -12.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.511× (z -11.1) |
| [[AN3 CA (line)]] | alt | 312 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.280× (z -12.0) |
| [[CHP-212 (line)]] | wt | 240 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HCT15 (line)]] | alt | 441 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[J82 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.454× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 174 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.534× (z -8.5) ⚠ toxic |
| [[RKO (line)]] | wt | 258 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.531× (z -8.8) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 212 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.191× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 164 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 181 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12161), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOP1A]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.61 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[MAP3K1]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ACBD5]] | +0.59 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[NUDCD2]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[AGL]] | +0.57 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[CDKN1B]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[BHLHE41]] | +0.57 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[TRMT1L]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SUPT20H]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CCDC148]] | +0.56 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[CETN3]] | +0.56 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PWWP3A]] | -0.57 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[DAP3]] | -0.57 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[UFD1]] | -0.57 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | -0.55 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[MBOAT7]] | -0.55 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ANKRD23]] | -0.55 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[NPIPB11]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CCDC32]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[HERC2P3]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[HSPE1]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[PPP1R32]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[TANGO2]] | -0.52 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **-** arm (projection on the module's main direction -0.465). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-30.2, 2.9); signed map (11.5, -14.1). **Vector** length 100, 35.0% of its response variance represented; |z| ≥ 3 in 1,175 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.6 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +9.1 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +7.9 | +2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.3 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +1.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.1 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.3 | -15.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -8.2 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -8.1 | -8.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.5 | -7.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -6.1 | -5.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.2 | -2.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.2 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ligand dependent nuclear receptor corepressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:96,832,254-96,995,956 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MLR2, FLJ38026, KIAA1795, DKFZP564P1916, FLJ13022; previously C10orf12 |
| Gene groups (HGNC) | Helix-turn-helix motif Psq family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JN0](https://www.uniprot.org/uniprotkb/Q96JN0) (Ligand-dependent corepressor):

> May act as transcription activator that binds DNA elements with the sequence 5'-CCCTATCGATCGATCTCTACCT-3' (By similarity). Repressor of ligand-dependent transcription activation by target nuclear receptors. Repressor of ligand-dependent transcription activation by ESR1, ESR2, NR3C1, PGR, RARA, RARB, RARG, RXRA and VDR.

**Summary**, from NCBI Gene [84458](https://www.ncbi.nlm.nih.gov/gene/84458):

> LCOR is a transcriptional corepressor widely expressed in fetal and adult tissues that is recruited to agonist-bound nuclear receptors through a single LxxLL motif, also referred to as a nuclear receptor (NR) box (Fernandes et al., 2003 [PubMed 12535528]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29503](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29503) · Entrez [84458](https://www.ncbi.nlm.nih.gov/gene/84458) · UniProt [Q96JN0](https://www.uniprot.org/uniprotkb/Q96JN0) · Ensembl [ENSG00000196233](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196233)

## Data

Gene col 12161: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12161); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12161, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12161]; `tensor/DDL_lfc|DDL_z.npy` [12161]; `embed/gene_vectors.npy` [12161]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12161 or target_col == 12161). Every well: [[LCOR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LCOR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
