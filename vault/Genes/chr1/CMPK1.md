---
symbol: "CMPK1"
type: "gene"
col: 8503
ensembl_id: "ENSG00000162368"
name: "cytidine/uridine monophosphate kinase 1"
location: "1p33"
module: 29
arm: "+"
pooled_cpm: 100.43
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CMPK1

*cytidine/uridine monophosphate kinase 1* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.37× (z +21.3, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.22× (z +4.9, q 1e-04, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 13 lines (NCI-H460 3.06×, HOP62 3.33×, SW480 2.89×, NCI-H1573 3.83×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HOP62 3.31×, SNU-423 4.00×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.443× (z -28.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPN1]] (+0.77, fdr 7e-06), [[TXNDC5]] (+0.71, fdr 7e-06), [[PGRMC1]] (+0.70, fdr 7e-06); moves opposite to [[PPP1R35]] (-0.67, fdr 1e-05, ⚠ PPP1R35 in the vector space only through flagged drug-doses), [[ZNF316]] (-0.66, fdr 7e-06), [[SURF6]] (-0.65, fdr 7e-06), [[MTRES1]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8503.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 13 lines (NCI-H460 3.06×, HOP62 3.33×, SW480 2.89×, NCI-H1573 3.83×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HOP62 3.31×, SNU-423 4.00×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +21.3 | 0e+00 | 47/49 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.24×** | +18.6 | 0e+00 | 40/50 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +18.1 | 0e+00 | 38/43 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +10.9 | 1e-25 | 39/44 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +4.9 | 1e-04 | 23/48 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +4.6 | 5e-04 | 23/48 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.5 | 6e-04 | 20/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM | ⚠ unreliable plate only; position correction uncertain | 1.19× | +4.4 | 8e-04 | 20/49 (RKO, KATO III, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.008 | 19/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.039 | 15/48 (PANC-1, NCI-H460, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8503.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.443×** | -28.4 | 0e+00 | 47/48 (HT-29, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.401×** | -22.6 | 0e+00 | 47/48 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.457×** | -19.3 | 0e+00 | 45/48 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.466×** | -18.8 | 0e+00 | 47/48 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.487×** | -17.7 | 0e+00 | 47/48 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.565×** | -13.5 | 9e-40 | 42/48 (COLO 205, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.684×** | -9.4 | 7e-19 | 45/48 (A498, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.717×** | -8.2 | 1e-14 | 40/48 (C-33 A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.772×** | -6.4 | 1e-08 | 29/48 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -6.1 | 6e-08 | 23/48 (A498, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.785×** | -6.0 | 1e-07 | 27/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -5.4 | 3e-06 | 20/48 (CFPAC-1, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.674×** | -5.1 | 2e-05 | 28/49 (A498, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | 0.897× | -3.8 | 0.006 | 8/48 (A498, RPMI-7951, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.906× | -3.4 | 0.023 | 14/48 (SNU-1, A498, …) | top dose only |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.876× | -3.1 | 0.062 | 11/49 (SNU-1, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8503. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 162 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -24.5) |
| [[PANC-1 (line)]] | alt | 99.5 | 5 (5 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +15.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -14.4) |
| [[COLO 205 (line)]] | alt | 270 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -23.5) |
| [[NCI-H460 (line)]] | wt | 72.0 | 3 (3 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +17.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -16.7) |
| [[HOP62 (line)]] | alt | 116 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +17.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -24.7) |
| [[HS-578T (line)]] | alt | 147 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -19.0) |
| [[NCI-H2030 (line)]] | alt | 101 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -21.3) |
| [[Hs 766T (line)]] | wt | 139 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -16.9) |
| [[KATO III (line)]] | alt | 113 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +12.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -15.6) |
| [[LS 180 (line)]] | wt | 109 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -17.2) |
| [[MIA PaCa-2 (line)]] | alt | 113 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +14.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 51.5 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +15.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -19.4) |
| [[A-172 (line)]] | wt | 69.4 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -17.7) |
| [[AsPC-1 (line)]] | alt | 102 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -22.7) |
| [[CFPAC-1 (line)]] | alt | 189 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -22.5) |
| [[HT-29 (line)]] | alt | 160 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -24.9) |
| [[J82 (line)]] | alt | 126 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -17.8) |
| [[LoVo (line)]] | wt | 105 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -19.9) |
| [[Panc 03.27 (line)]] | alt | 81.2 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -16.5) |
| [[SW1417 (line)]] | alt | 71.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -12.5) |
| [[SW480 (line)]] | alt | 65.7 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +15.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -15.3) |
| [[C32 (line)]] | wt | 89.9 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 78.3 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -24.0) |
| [[NCI-H1792 (line)]] | alt | 85.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +13.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -9.4) |
| [[RKO (line)]] | wt | 97.4 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -16.2) |
| [[A549 (line)]] | wt | 88.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +14.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.469× (z -9.0) |
| [[H4 (line)]] | wt | 112 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -13.0) |
| [[HCT15 (line)]] | alt | 99.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 83.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.465× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 84.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -17.5) |
| [[SNU-1 (line)]] | wt | 93.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -14.3) |
| [[SNU-423 (line)]] | alt | 77.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.00× (z +15.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -11.2) |
| [[C-33 A (line)]] | alt | 82.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.34× (z +10.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.360× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 90.6 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -13.7) |
| [[SHP-77 (line)]] | alt | 70.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +13.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.380× (z -10.6) |
| [[SW 900 (line)]] | alt | 82.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -14.8) |
| [[SW48 (line)]] | wt | 66.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -14.3) |
| [[A-427 (line)]] | wt | 74.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.38× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -20.3) |
| [[AN3 CA (line)]] | alt | 105 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -15.0) |
| [[NCI-H23 (line)]] | alt | 89.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.13× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 98.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -16.1) |
| [[SW 1088 (line)]] | alt | 105 | 0 | 2 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.111× (z -8.6) ⚠ toxic · without an alert: [[Decitabine (drug)]] 0.5 µM 0.115× (z -8.5) |
| [[BT-474 (line)]] | alt | 95.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 91.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 83.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.0) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8503), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPN1]] | +0.77 | +0.70 / +0.79 | both halves | 7e-06 |  |
| [[TXNDC5]] | +0.71 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[PGRMC1]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[CRTAP]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ADAM15]] | +0.68 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.67 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[FKBP9]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ATP2A2]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[HIPK1]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[STT3B]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[TMEM30A]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[DHFR]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R35]] ⚠ | -0.67 | -0.55 / -0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF316]] | -0.66 | -0.70 / -0.64 | both halves | 7e-06 |  |
| [[SURF6]] | -0.65 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[MTRES1]] | -0.64 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[ZNF23]] | -0.63 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[SURF2]] | -0.63 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[PITPNA-AS1]] | -0.62 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[SNHG11]] | -0.62 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[ESF1]] | -0.61 | -0.68 / -0.57 | both halves | 9e-06 |  |
| [[MRPL46]] | -0.61 | -0.46 / -0.66 | both halves | 2e-05 |  |
| [[METTL23]] | -0.61 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[NT5C]] | -0.61 | -0.45 / -0.63 | both halves | 3e-05 | pathway: Metabolism of nucleotides; STRING 496 |
| [[BTG1]] | -0.61 | -0.46 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CMPK1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.728). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.1, -21.8); signed map (-23.3, -39.3). **Vector** length 121, 37.0% of its response variance represented; |z| ≥ 3 in 1,261 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +18.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +21.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.8 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.3 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.5 | +1.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +3.2 | +1.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +3.1 | +1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.0 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -22.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -28.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -13.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.2 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -6.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.7 | -2.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cytidine/uridine monophosphate kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p33 — chr1:47,333,790-47,394,866 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UMP-CMPK; previously CMPK |
| Gene groups (HGNC) | Cytidine/uridine monophosphate kinases |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P30085](https://www.uniprot.org/uniprotkb/P30085) (UMP-CMP kinase):

> Catalyzes the phosphorylation of pyrimidine nucleoside monophosphates at the expense of ATP. Plays an important role in de novo pyrimidine nucleotide biosynthesis. Has preference for UMP and CMP as phosphate acceptors. Also displays broad nucleoside diphosphate kinase activity.

**Summary**, from NCBI Gene [51727](https://www.ncbi.nlm.nih.gov/gene/51727):

> This gene encodes one of the enzymes required for cellular nucleic acid biosynthesis. This enzyme catalyzes the transfer of a phosphate group from ATP to CMP, UMP, or dCMP, to form the corresponding diphosphate nucleotide. Alternate splicing results in both coding and non-coding transcript variants. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:18170](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18170) · Entrez [51727](https://www.ncbi.nlm.nih.gov/gene/51727) · UniProt [P30085](https://www.uniprot.org/uniprotkb/P30085) · Ensembl [ENSG00000162368](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162368)

## Data

Gene col 8503: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8503); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8503, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8503]; `tensor/DDL_lfc|DDL_z.npy` [8503]; `embed/gene_vectors.npy` [8503]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8503 or target_col == 8503). Every well: [[CMPK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMPK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
