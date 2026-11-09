---
symbol: "GTF2IRD1"
type: "gene"
col: 124
ensembl_id: "ENSG00000006704"
name: "GTF2I repeat domain containing 1"
location: "7q11.23"
module: 20
arm: "-"
pooled_cpm: 117.01
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 31
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# GTF2IRD1

*GTF2I repeat domain containing 1* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.33× (z +6.5, q 6e-08, up in 34 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.27× (z +5.6, q 5e-06, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.336× (z -35.8, q 0e+00, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC18]] (+0.60, fdr 1e-05), [[PWWP2B]] (+0.58, fdr 1e-05), [[ZNF579]] (+0.50, fdr 3e-05); moves opposite to [[TMEM30A]] (-0.57, fdr 2e-05), [[PRKAR1A]] (-0.55, fdr 5e-05), [[FSTL1]] (-0.52, fdr 9e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 124.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.33×** | +6.5 | 6e-08 | 34/47 (LoVo, H4, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +5.6 | 5e-06 | 29/47 (LoVo, H4, …) | rises with dose | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **1.42×** | +4.3 | 0.004 | 22/48 (PANC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.8 | 0.018 | 10/48 (HOP62, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.8 | 0.018 | 19/48 (PANC-1, BT-474, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.045 | 17/48 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.067 | 16/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.15× | +3.3 | 0.067 | 12/48 (HOP62, AsPC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.072 | 17/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | 1.15× | +3.2 | 0.074 | 10/48 (AsPC-1, Panc 03.27, …) | top dose only | plate-row cell shift |
| [[venetoclax (drug)]] 5 µM |  | 1.29× | +3.1 | 0.11 | 14/48 (PANC-1, HT-29, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 124.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.336×** | -35.8 | 0e+00 | 48/49 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.347×** | -23.7 | 0e+00 | 44/48 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.379×** | -22.6 | 0e+00 | 43/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.412×** | -20.6 | 0e+00 | 44/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.480×** | -17.1 | 0e+00 | 38/49 (COLO 205, LoVo, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.469×** | -16.9 | 0e+00 | 43/50 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.485×** | -16.8 | 0e+00 | 43/48 (PANC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.513×** | -15.5 | 0e+00 | 42/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.514×** | -15.5 | 0e+00 | 39/48 (SW1417, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.517×** | -15.3 | 0e+00 | 42/48 (NCI-H1792, A-427, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.507×** | -15.2 | 0e+00 | 34/43 (LS 180, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.501×** | -14.9 | 0e+00 | 36/45 (MIA PaCa-2, A-172, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.343×** | -13.0 | 6e-37 | 40/49 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.578×** | -12.7 | 2e-35 | 37/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.610×** | -11.5 | 5e-29 | 38/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.640×** | -10.4 | 1e-23 | 29/48 (A-427, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.757×** | -9.1 | 2e-18 | 32/48 (A-172, Hs 766T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.722×** | -7.6 | 1e-12 | 37/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.544×** | -7.4 | 4e-12 | 28/48 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.731×** | -7.3 | 8e-12 | 30/48 (PANC-1, RKO, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.804×** | -7.2 | 2e-11 | 26/48 (SW480, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 124. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 215 | 0 | 20 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -28.3) |
| [[MIA PaCa-2 (line)]] | alt | 155 | 0 | 19 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -30.0) |
| [[PANC-1 (line)]] | alt | 94.8 | 0 | 18 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -24.8) |
| [[SW480 (line)]] | alt | 174 | 0 | 16 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -31.1) |
| [[A-427 (line)]] | wt | 76.9 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -22.8) |
| [[SW1417 (line)]] | alt | 226 | 0 | 15 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0696× (z -44.2) |
| [[NCI-H1792 (line)]] | alt | 93.2 | 1 (1 ⚠) | 13 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.7) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -27.6) |
| [[NCI-H460 (line)]] | wt | 116 | 4 (1 ⚠) | 10 (3 ⚠) | [[Trametinib (drug)]] 0.05 µM 1.83× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -26.7) |
| [[SW48 (line)]] | wt | 214 | 0 | 14 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -25.1) |
| [[HS-578T (line)]] | alt | 105 | 0 | 13 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -19.2) |
| [[A-172 (line)]] | wt | 246 | 1 (1 ⚠) | 10 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -25.9) |
| [[H4 (line)]] | wt | 105 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -20.7) |
| [[KATO III (line)]] | alt | 145 | 1 | 10 (4 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.60× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.122× (z -26.8) |
| [[Panc 03.27 (line)]] | alt | 119 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -23.2) |
| [[AsPC-1 (line)]] | alt | 101 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -20.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -14.4) |
| [[C32 (line)]] | wt | 88.9 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -18.5) |
| [[LOX-IMVI (line)]] | wt | 80.7 | 0 | 10 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.169× (z -18.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -13.7) |
| [[C-33 A (line)]] | alt | 112 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -16.5) |
| [[CFPAC-1 (line)]] | alt | 67.4 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -15.9) |
| [[LoVo (line)]] | wt | 182 | 1 (1 ⚠) | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +13.5) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -25.1) |
| [[SNU-423 (line)]] | alt | 119 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -21.5) |
| [[HEC-1-A (line)]] | alt | 150 | 0 | 8 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -20.3) |
| [[HOP62 (line)]] | alt | 93.6 | 1 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.9) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -17.4) |
| [[Hs 766T (line)]] | wt | 47.8 | 1 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -16.1) |
| [[HT-29 (line)]] | alt | 128 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -24.2) |
| [[NCI-H2030 (line)]] | alt | 54.5 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -20.1) |
| [[RKO (line)]] | wt | 121 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -15.0) |
| [[SNU-1 (line)]] | wt | 73.0 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.196× (z -13.4) |
| [[BT-474 (line)]] | alt | 144 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -20.1) |
| [[COLO 205 (line)]] | alt | 215 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0534× (z -28.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0768× (z -25.0) |
| [[NCI-H23 (line)]] | alt | 45.1 | 1 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -14.7) |
| [[A498 (line)]] | wt | 145 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -18.8) |
| [[AN3 CA (line)]] | alt | 272 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -17.0) |
| [[HepG2_C3A (line)]] | wt | 139 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -14.7) |
| [[SK-MEL-2 (line)]] | alt | 80.0 | 0 | 6 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -20.2) |
| [[SW 900 (line)]] | alt | 96.6 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -20.0) |
| [[NCI-H2347 (line)]] | alt | 70.5 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -15.5) |
| [[J82 (line)]] | alt | 117 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -10.4) |
| [[SHP-77 (line)]] | alt | 65.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -15.0) |
| [[HCT15 (line)]] | alt | 139 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -16.7) |
| [[RPMI-7951 (line)]] | alt | 50.0 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -10.8) |
| [[SW 1088 (line)]] | alt | 151 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0695× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 53.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 38.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -10.0) |
| [[A549 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 85.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 124), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC18]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PWWP2B]] | +0.58 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ZNF579]] | +0.50 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[TRIM16]] | +0.50 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[FPGS]] | +0.49 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[BCAT2]] | +0.48 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[EIF5B]] | +0.47 | +0.29 / +0.46 | both halves | 3e-04 |  |
| [[CARMIL2]] | +0.47 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[GPR153]] | +0.47 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[ATP9B]] | +0.47 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[LRRC8E]] | +0.47 | +0.37 / +0.47 | both halves | 8e-05 |  |
| [[SLC25A33]] | +0.46 | +0.34 / +0.45 | both halves | 1e-04 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM30A]] | -0.57 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[PRKAR1A]] | -0.55 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[FSTL1]] | -0.52 | -0.50 / -0.37 | both halves | 9e-05 |  |
| [[ERAP1]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[MSL3]] | -0.51 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[BPNT2]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[LINC01232]] | -0.50 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[ITM2C]] | -0.50 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[ITM2B]] | -0.50 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[USF1]] | -0.49 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[CMTM6]] | -0.47 | -0.28 / -0.56 | both halves | 3e-04 |  |
| [[CTSO]] | -0.47 | -0.44 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GTF2IRD1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.360). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-46.4, 16.2); signed map (-0.6, -12.0). **Vector** length 112, 36.3% of its response variance represented; |z| ≥ 3 in 1,747 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +11.6 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.7 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +7.4 | -0.5 |
|  | [[EX229 (drug)]] 5 µM |  | +6.3 | +4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.7 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | -3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +5.1 | +3.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.9 | +2.6 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -16.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -23.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.4 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -11.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -3.1 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -9.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | GTF2I repeat domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:74,453,790-74,602,605 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MusTRD1, RBAP2, GTF3, WBSCR12, BEN, Cream1; previously WBSCR11 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHL9](https://www.uniprot.org/uniprotkb/Q9UHL9) (General transcription factor II-I repeat domain-containing protein 1):

> May be a transcription regulator involved in cell-cycle progression and skeletal muscle differentiation. May repress GTF2I transcriptional functions, by preventing its nuclear residency, or by inhibiting its transcriptional activation. May contribute to slow-twitch fiber type specificity during myogenesis and in regenerating muscles. Binds troponin I slow-muscle fiber enhancer (USE B1). Binds specifically and with high affinity to the EFG sequences derived from the early enhancer of HOXC8 (By …

**Summary**, from NCBI Gene [9569](https://www.ncbi.nlm.nih.gov/gene/9569):

> The protein encoded by this gene contains five GTF2I-like repeats and each repeat possesses a potential helix-loop-helix (HLH) motif. It may have the ability to interact with other HLH-proteins and function as a transcription factor or as a positive transcriptional regulator under the control of Retinoblastoma protein. This gene plays a role in craniofacial and cognitive development and mutations have been associated with Williams-Beuren syndrome, a multisystem developmental disorder caused by …

**Accessions** — [HGNC:4661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4661) · Entrez [9569](https://www.ncbi.nlm.nih.gov/gene/9569) · UniProt [Q9UHL9](https://www.uniprot.org/uniprotkb/Q9UHL9) · Ensembl [ENSG00000006704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006704)

## Data

Gene col 124: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 124); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 124, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 124]; `tensor/DDL_lfc|DDL_z.npy` [124]; `embed/gene_vectors.npy` [124]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 124 or target_col == 124). Every well: [[GTF2IRD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2IRD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
