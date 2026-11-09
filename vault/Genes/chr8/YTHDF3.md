---
symbol: "YTHDF3"
type: "gene"
col: 11722
ensembl_id: "ENSG00000185728"
name: "YTH N6-methyladenosine RNA binding protein F3"
location: "8q12.3"
module: 35
arm: "+"
pooled_cpm: 155.14
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 11
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# YTHDF3

*YTH N6-methyladenosine RNA binding protein F3* — 8q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.71× (z +18.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.403× (z -16.5, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.623× (z -8.9, q 8e-17, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (64 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 36 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMC5-DT]] (+0.65, fdr 4e-04), [[C2orf49-DT]] (+0.64, fdr 0.001, ⚠ one half only (not replicated)), [[NGDN]] (+0.62, fdr 4e-05), [[UBE2D3]] (+0.62, fdr 7e-06); moves opposite to [[EPS15]] (-0.54, fdr 5e-04), [[TBCD]] (-0.54, fdr 4e-04), [[DOP1B]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11722.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.71×** | +18.8 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.95×** | +17.6 | 0e+00 | 48/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +14.5 | 4e-45 | 46/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.82×** | +13.2 | 1e-37 | 47/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.95×** | +12.6 | 3e-34 | 46/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +12.4 | 2e-33 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.80×** | +11.0 | 2e-26 | 43/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +8.4 | 4e-15 | 40/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +7.7 | 1e-12 | 44/48 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +6.2 | 4e-08 | 36/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +5.8 | 5e-07 | 43/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +5.7 | 5e-07 | 37/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +5.4 | 3e-06 | 31/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.002 | 29/48 (HT-29, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.9 | 0.003 | 18/48 (SNU-1, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +3.8 | 0.004 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.016 | 24/49 (PANC-1, C32, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11722.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.403×** | -16.5 | 0e+00 | 44/44 (SHP-77, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.439×** | -15.5 | 0e+00 | 47/49 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.623×** | -8.9 | 8e-17 | 44/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.624×** | -8.9 | 8e-17 | 44/48 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.674×** | -7.4 | 1e-11 | 42/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.765×** | -5.1 | 4e-05 | 36/48 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.769×** | -4.6 | 4e-04 | 25/45 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.800×** | -4.0 | 0.004 | 26/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.815×** | -3.8 | 0.007 | 32/48 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.814×** | -3.7 | 0.010 | 26/50 (NCI-H2347, RPMI-7951, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.826×** | -3.6 | 0.017 | 23/48 (PANC-1, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.884× | -3.3 | 0.046 | 13/48 (A498, BT-474, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.841× | -3.3 | 0.046 | 20/47 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.842× | -3.2 | 0.046 | 21/48 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.837× | -3.2 | 0.046 | 18/47 (NCI-H1573, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11722. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 111 | 13 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.95× (z +26.4) | — |
| [[PANC-1 (line)]] | alt | 143 | 9 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +21.2) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.567× (z -8.5) |
| [[LoVo (line)]] | wt | 120 | 8 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -16.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 210 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -14.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 139 | 7 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +18.6) | [[Panobinostat (drug)]] 0.5 µM 0.568× (z -8.8) |
| [[HOP62 (line)]] | alt | 183 | 4 (1 ⚠) | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.53× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.463× (z -10.0) |
| [[HT-29 (line)]] | alt | 128 | 6 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.454× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.485× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 103 | 6 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.466× (z -8.6) |
| [[A498 (line)]] | wt | 274 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.461× (z -10.7) |
| [[BT-474 (line)]] | alt | 148 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.454× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[HEC-1-A (line)]] | alt | 129 | 5 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.27× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -13.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 174 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +19.8) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -13.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 135 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.10× (z +18.4) | — |
| [[LS 180 (line)]] | wt | 148 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.51× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 142 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -9.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 119 | 4 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.10× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -19.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 122 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 200 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -10.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 126 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 146 | 3 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.45× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.485× (z -8.9) |
| [[COLO 205 (line)]] | alt | 134 | 5 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 13.1× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.421× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 241 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.92× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 182 | 2 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.549× (z -9.5) |
| [[A-172 (line)]] | wt | 111 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +15.9) | — |
| [[A-427 (line)]] | wt | 128 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.34× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -21.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 134 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -17.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 244 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -14.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 138 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 122 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -10.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 216 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.5× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0446× (z -36.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 188 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.83× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -12.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 159 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.37× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -12.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 127 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 175 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.52× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -10.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 138 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.86× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -12.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 175 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -23.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 147 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.50× (z +11.1) | — |
| [[SW48 (line)]] | wt | 143 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 4.80× (z +13.4) | — |
| [[C32 (line)]] | wt | 184 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 9.00× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -11.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 146 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -14.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 130 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.89× (z +13.6) | — |
| [[SK-MEL-2 (line)]] | alt | 154 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +14.6) | — |
| [[C-33 A (line)]] | alt | 123 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.60× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -11.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 120 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.136× (z -8.5) |
| [[CHP-212 (line)]] | wt | 175 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11722), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 31 of them with an alert (⚠; 31 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC5-DT]] | +0.65 | +0.26 / +0.56 | both halves | 4e-04 |  |
| [[C2orf49-DT]] | +0.64 | +0.15 / +0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[NGDN]] | +0.62 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[UBE2D3]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[SRRM2-AS1]] | +0.61 | +0.26 / +0.43 | both halves | 4e-04 |  |
| [[POLR2M]] | +0.61 | +0.30 / +0.51 | both halves | 2e-04 |  |
| [[CCNT2]] | +0.61 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[TRMO]] | +0.61 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[PJVK]] | +0.60 | +0.20 / +0.42 | both halves | 7e-04 |  |
| [[PGBD4]] | +0.60 | +0.09 / +0.56 | ⚠ one half (not replicated) | 0.003 |  |
| [[KRBA2]] | +0.60 | +0.15 / +0.54 | ⚠ one half (not replicated) | 0.001 |  |
| [[RAE1]] | +0.59 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[LANCL2]] | +0.58 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[KCTD21-AS1]] | +0.58 | +0.23 / +0.37 | both halves | 5e-04 |  |
| [[GPRASP3]] | +0.58 | +0.32 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPS15]] | -0.54 | -0.24 / -0.40 | both halves | 5e-04 |  |
| [[TBCD]] | -0.54 | -0.29 / -0.24 | both halves | 4e-04 |  |
| [[DOP1B]] | -0.53 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[PACS2]] | -0.53 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[AFDN]] | -0.52 | -0.16 / -0.39 | ⚠ not reproduced | 0.001 |  |
| [[STX2]] | -0.51 | -0.18 / -0.30 | ⚠ not reproduced | 0.001 |  |
| [[TNK2]] | -0.51 | +0.01 / -0.37 | ⚠ not reproduced | 1.00 |  |
| [[HABP4]] | -0.50 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[SUN1]] | -0.50 | -0.29 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[FN3KRP]] | -0.49 | -0.11 / -0.18 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises YTHDF3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (6.2, 23.3); signed map (32.4, -13.9). **Vector** length 63.4, 20.4% of its response variance represented; |z| ≥ 3 in 1,326 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.5 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.1 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | +4.1 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | -1.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.3 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | -3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | -1.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.9 | -7.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -8.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -8.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.7 | +0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | +12.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | +1.8 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -1.5 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | YTH N6-methyladenosine RNA binding protein F3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.3 — chr8:63,168,553-63,212,786 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31657 |
| Gene groups (HGNC) | YTH domain containing N6-methyladenosine readers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z739](https://www.uniprot.org/uniprotkb/Q7Z739) (YTH domain-containing family protein 3):

> Specifically recognizes and binds N6-methyladenosine (m6A)-containing RNAs, and regulates their stability. M6A is a modification present at internal sites of mRNAs and some non-coding RNAs and plays a role in mRNA stability and processing. Acts as a regulator of mRNA stability by promoting degradation of m6A-containing mRNAs via interaction with the CCR4-NOT complex or PAN3. The YTHDF paralogs (YTHDF1, YTHDF2 and YTHDF3) share m6A-containing mRNAs targets and act redundantly to mediate mRNA …

**Summary**, from NCBI Gene [253943](https://www.ncbi.nlm.nih.gov/gene/253943):

> This gene encodes a member of the YTH (YT521-B homology) domain protein family. The YTH domain is common in eukaryotes, is often found in the middle of the protein sequence, and may function in binding to RNA. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2013]

**Accessions** — [HGNC:26465](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26465) · Entrez [253943](https://www.ncbi.nlm.nih.gov/gene/253943) · UniProt [Q7Z739](https://www.uniprot.org/uniprotkb/Q7Z739) · Ensembl [ENSG00000185728](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185728)

## Data

Gene col 11722: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11722); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11722, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11722]; `tensor/DDL_lfc|DDL_z.npy` [11722]; `embed/gene_vectors.npy` [11722]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11722 or target_col == 11722). Every well: [[YTHDF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YTHDF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
