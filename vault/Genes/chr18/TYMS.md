---
symbol: "TYMS"
type: "gene"
col: 10760
ensembl_id: "ENSG00000176890"
name: "thymidylate synthetase"
location: "18p11.32"
module: 6
arm: "+"
pooled_cpm: 35.93
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 37
n_dd_up_clean: 3
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TYMS

*thymidylate synthetase* — 18p11.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.36× (z +17.8, q 0e+00, up in 43 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.39× (z +3.5, q 0.021, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.359× (z -15.3, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HELLS]] (+0.87, fdr 7e-06), [[MCM4]] (+0.84, fdr 7e-06), [[TIMELESS]] (+0.82, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 13 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10760.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **5.36×** | +17.8 | 0e+00 | 43/43 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **5.12×** | +16.6 | 0e+00 | 39/39 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **3.60×** | +12.5 | 8e-34 | 39/42 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.68×** | +5.3 | 2e-05 | 32/45 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.66×** | +5.2 | 2e-05 | 34/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.39×** | +4.9 | 8e-05 | 31/47 (NCI-H23, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **1.55×** | +4.6 | 3e-04 | 30/45 (RPMI-7951, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.49×** | +4.0 | 0.004 | 24/46 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~81% of this change | **1.43×** | +3.7 | 0.014 | 21/43 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.41×** | +3.7 | 0.014 | 20/47 (HOP62, A498, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.39×** | +3.5 | 0.021 | 23/47 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.24×** | +3.2 | 0.057 | 21/47 (SW48, LOX-IMVI, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.24×** | +3.2 | 0.057 | 19/47 (RKO, HT-29, …) | rises with dose |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.057 | 17/47 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Flutamide (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.088 | 16/46 (PANC-1, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10760.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.359×** | -15.3 | 0e+00 | 42/47 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.306×** | -12.5 | 2e-33 | 46/47 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.313×** | -12.3 | 3e-32 | 43/47 (J82, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.364×** | -10.7 | 2e-24 | 40/47 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.404×** | -9.6 | 1e-19 | 40/47 (J82, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.449×** | -8.5 | 3e-15 | 42/47 (J82, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.563×** | -6.1 | 1e-07 | 34/47 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.688×** | -5.6 | 2e-06 | 34/47 (HT-29, HCT15, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.600×** | -5.4 | 4e-06 | 36/46 (J82, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.534×** | -5.2 | 1e-05 | 30/47 (A-427, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.719×** | -4.9 | 5e-05 | 29/47 (HOP62, LS 180, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.415×** | -4.7 | 1e-04 | 29/47 (A-427, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **0.736×** | -4.6 | 2e-04 | 23/47 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.562×** | -4.3 | 7e-04 | 22/47 (A-427, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.661×** | -4.2 | 0.001 | 25/47 (Panc 03.27, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.705×** | -3.7 | 0.007 | 22/46 (A-427, KATO III, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.791×** | -3.5 | 0.014 | 24/47 (KATO III, A-427, …) | top dose only |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.637×** | -3.4 | 0.022 | 17/47 (SW480, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.735×** | -3.3 | 0.026 | 19/46 (KATO III, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.08 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 125 | 2 (2 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.0806× (z -28.5) |
| [[LS 180 (line)]] | wt | 36.8 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 7.46× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -14.7) |
| [[SW480 (line)]] | alt | 41.6 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -19.2) |
| [[HCT15 (line)]] | alt | 51.1 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 6.23× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -13.0) |
| [[J82 (line)]] | alt | 89.0 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 80.5 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -18.0) |
| [[C32 (line)]] | wt | 55.6 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Panobinostat (drug)]] 5 µM 0.220× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 44.7 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 8.75× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -19.8) |
| [[PANC-1 (line)]] | alt | 45.7 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 7.60× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -10.3) |
| [[A-172 (line)]] | wt | 48.2 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Selinexor (drug)]] 5 µM 0.322× (z -10.0) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.209× (z -9.8) |
| [[A498 (line)]] | wt | 38.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.8) |
| [[A549 (line)]] | wt | 25.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.78× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[HOP62 (line)]] | alt | 46.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.34× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -13.6) |
| [[HT-29 (line)]] | alt | 22.6 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 10.9× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -14.8) |
| [[KATO III (line)]] | alt | 24.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 7.05× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -9.6) |
| [[LoVo (line)]] | wt | 18.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.72× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 24.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 8.24× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -9.8) |
| [[C-33 A (line)]] | alt | 65.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 48.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -12.7) |
| [[Hs 766T (line)]] | wt | 19.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.23× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -11.5) |
| [[HS-578T (line)]] | alt | 16.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.79× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[LOX-IMVI (line)]] | wt | 32.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.04× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 24.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.7× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H2030 (line)]] | alt | 32.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 31.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[Panc 03.27 (line)]] | alt | 28.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.14× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -12.8) |
| [[SHP-77 (line)]] | alt | 32.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 42.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 5.20× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -12.8) |
| [[SW48 (line)]] | wt | 37.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -12.7) |
| [[BT-474 (line)]] | alt | 37.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 11.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.97× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[H4 (line)]] | wt | 33.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0602× (z -18.1) |
| [[NCI-H1573 (line)]] | alt | 14.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -8.6) |
| [[RKO (line)]] | wt | 29.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 18.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.42× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -8.7) |
| [[SNU-1 (line)]] | wt | 43.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -15.8) |
| [[SNU-423 (line)]] | alt | 15.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.96× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[AN3 CA (line)]] | alt | 54.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 17.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.57× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HELLS]] | +0.87 | +0.85 / +0.83 | both halves | 7e-06 | STRING 552 |
| [[MCM4]] | +0.84 | +0.86 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 938 |
| [[TIMELESS]] | +0.82 | +0.86 / +0.78 | both halves | 7e-06 | STRING 450 |
| [[MYBL2]] | +0.81 | +0.87 / +0.78 | both halves | 7e-06 | pathway: Mitotic G1 phase and G1/S transition; STRING 616 |
| [[RAD51AP1]] | +0.80 | +0.78 / +0.82 | both halves | 7e-06 | STRING 513 |
| [[RRM1]] | +0.79 | +0.81 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 976 |
| [[CSE1L]] | +0.79 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[CENPH]] | +0.78 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[KNTC1]] | +0.78 | +0.82 / +0.78 | both halves | 7e-06 | STRING 521 |
| [[PCNA]] | +0.78 | +0.81 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR; STRING 913 |
| [[CLSPN]] | +0.78 | +0.79 / +0.77 | both halves | 7e-06 |  |
| [[PCLAF]] | +0.77 | +0.83 / +0.79 | both halves | 7e-06 | STRING 859 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises TYMS's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 7.8% of all compounds | 0.062 | ⚠ off-target possible; 5 compounds |
| [[CDC25A]] | B | CDC25A activity raises TYMS's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.31× lower at baseline in the lines without CDC25A | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises TYMS's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.50× lower at baseline in the lines without DSCC1 | 0.036 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.802). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.9, -44.3); signed map (-37.8, -47.1). **Vector** length 121, 44.2% of its response variance represented; |z| ≥ 3 in 1,281 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.62 to 65); *DNA strand elongation* (reactome, mean cos +0.65 to 28); *DNA Replication* (reactome, mean cos +0.63 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +8.0 | +5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +6.9 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.0 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +2.9 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.7 | +2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.6 | +2.1 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.7 | +0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.7 | +1.8 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -4.8 | -6.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -4.7 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.5 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.5 | -5.2 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -4.2 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.6 | -5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | thymidylate synthetase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.32 — chr18:657,653-673,578 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Tsase, TMS, HsT422; previously TS |
| Gene groups (HGNC) | Small molecule methyltransferases; Methyltransferases with unique structures |
| Hallmark sets | DNA_REPAIR, MYC_TARGETS_V1 |
| Reactome | 7 pathways, smallest: G1/S-Specific Transcription; Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P04818](https://www.uniprot.org/uniprotkb/P04818) (Thymidylate synthase):

> Catalyzes the reductive methylation of 2'-deoxyuridine 5'-monophosphate (dUMP) to thymidine 5'-monophosphate (dTMP), using the cosubstrate, 5,10- methylenetetrahydrofolate (CH2H4folate) as a 1-carbon donor and reductant and contributes to the mitochondrial and nuclear de novo thymidylate biosynthesis pathway.

**Summary**, from NCBI Gene [7298](https://www.ncbi.nlm.nih.gov/gene/7298):

> Thymidylate synthase catalyzes the methylation of deoxyuridylate to deoxythymidylate using, 10-methylenetetrahydrofolate (methylene-THF) as a cofactor. This function maintains the dTMP (thymidine-5-prime monophosphate) pool critical for DNA replication and repair. The enzyme has been of interest as a target for cancer chemotherapeutic agents. It is considered to be the primary site of action for 5-fluorouracil, 5-fluoro-2-prime-deoxyuridine, and some folate analogs. Expression of this gene and …

**Accessions** — [HGNC:12441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12441) · Entrez [7298](https://www.ncbi.nlm.nih.gov/gene/7298) · UniProt [P04818](https://www.uniprot.org/uniprotkb/P04818) · Ensembl [ENSG00000176890](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176890)

## Data

Gene col 10760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10760); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10760]; `tensor/DDL_lfc|DDL_z.npy` [10760]; `embed/gene_vectors.npy` [10760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10760 or target_col == 10760). Every well: [[TYMS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TYMS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
