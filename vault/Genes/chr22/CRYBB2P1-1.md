---
symbol: "CRYBB2P1-1"
type: "gene"
col: 16576
ensembl_id: "ENSG00000291087"
name: ""
location: ""
module: 105
arm: "+"
pooled_cpm: 54.99
n_lines_expressing: 46
n_dd_up: 14
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# CRYBB2P1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.39× (z +5.7, q 8e-06, up in 28 of 44 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.37× (z +5.5, q 1e-05, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.499× (z -17.1, q 0e+00, down in 37 of 44 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.434× (z -13.9, q 1e-41, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYBB2P1]] (+0.72, fdr 7e-06, ⚠ read-through risk), [[TMED7-TICAM2]] (+0.70, fdr 7e-06), [[BTAF1]] (+0.69, fdr 9e-06), [[C9orf153]] (+0.69, fdr 1e-05); moves opposite to [[KLF11]] (-0.55, fdr 1e-05), [[PABIR1]] (-0.54, fdr 1e-05), [[ZFP36L2]] (-0.53, fdr 1e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GRK3]] → it (grade C ⚠); 1 goes from it, the strongest it → [[GRK3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16576.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +5.7 | 8e-06 | 28/44 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +5.5 | 1e-05 | 25/44 (LoVo, SHP-77, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.28×** | +4.3 | 0.003 | 21/44 (CFPAC-1, LOX-IMVI, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.24×** | +3.5 | 0.053 | 20/44 (LS 180, Hs 766T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.46×** | +3.4 | 0.053 | 16/41 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.053 | 18/44 (SNU-423, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.053 | 14/44 (CFPAC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.14× | +3.3 | 0.053 | 21/44 (NCI-H1573, Hs 766T, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.053 | 18/45 (HS-578T, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.053 | 9/44 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.054 | 18/44 (SHP-77, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.067 | 19/44 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.2 | 0.067 | 13/34 (HEC-1-A, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.067 | 15/44 (LOX-IMVI, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.21×** | +3.1 | 0.067 | 16/44 (HEC-1-A, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16576.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.499×** | -17.1 | 0e+00 | 37/44 (NCI-H460, C32, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.434×** | -13.9 | 1e-41 | 40/44 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.480×** | -12.2 | 3e-32 | 29/38 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.498×** | -12.1 | 2e-31 | 39/44 (SK-MEL-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.595×** | -8.6 | 6e-16 | 34/43 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.632×** | -8.0 | 2e-13 | 28/44 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.733×** | -5.2 | 2e-05 | 23/44 (C32, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **0.770×** | -4.5 | 4e-04 | 24/43 (HCT15, NCI-H1792, …) | all doses, flat | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.773×** | -4.5 | 5e-04 | 24/44 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.784×** | -4.2 | 0.001 | 26/44 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.784×** | -4.2 | 0.001 | 22/44 (A498, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.811×** | -3.6 | 0.014 | 18/44 (SK-MEL-2, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.672×** | -3.6 | 0.014 | 15/44 (J82, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.870× | -3.4 | 0.028 | 9/44 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.824×** | -3.4 | 0.030 | 16/44 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.836× | -3.1 | 0.064 | 11/44 (SW48, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 75.8 | 1 (1 ⚠) | 5 (3 ⚠) | [[Lonafarnib (drug)]] 5 µM 4.19× (z +8.6) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -15.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.431× (z -9.4) |
| [[A498 (line)]] | wt | 70.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -22.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.184× (z -16.3) |
| [[C32 (line)]] | wt | 104 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -26.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -15.6) |
| [[CFPAC-1 (line)]] | alt | 89.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -17.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.405× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 64.1 | 1 (1 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +12.9) ⚠ cell-cycle shift, explains ~17% of this change | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -18.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.126× (z -16.6) |
| [[NCI-H460 (line)]] | wt | 76.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -30.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -19.1) |
| [[SK-MEL-2 (line)]] | alt | 119 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0442× (z -32.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.364× (z -10.2) |
| [[A549 (line)]] | wt | 48.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0831× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.172× (z -13.4) |
| [[C-33 A (line)]] | alt | 131 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0955× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.327× (z -9.0) |
| [[HOP62 (line)]] | alt | 72.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -19.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.399× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 83.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -25.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 35.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -22.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.159× (z -14.5) |
| [[SNU-423 (line)]] | alt | 76.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -13.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.368× (z -9.2) |
| [[A-427 (line)]] | wt | 32.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.225× (z -11.7) ⚠ toxic |
| [[HCT15 (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -11.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 65.0 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.56× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -13.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 51.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -16.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.161× (z -13.9) |
| [[LS 180 (line)]] | wt | 56.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0863× (z -21.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 47.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -10.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.314× (z -10.4) |
| [[PANC-1 (line)]] | alt | 37.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -13.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.380× (z -10.1) |
| [[A-172 (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -19.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 57.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0974× (z -11.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 48.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -11.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 57.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -13.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 56.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.3) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[HS-578T (line)]] | alt | 68.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -10.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.531× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 49.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 52.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.8) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[Panc 03.27 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -10.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 61.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW1417 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.347× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 88.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -15.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 7.86 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 96.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.40 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYBB2P1]] | +0.72 | +0.75 / +0.65 | both halves | 7e-06 | ⚠ **readthrough risk**: CRYBB2P1 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[TMED7-TICAM2]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[BTAF1]] | +0.69 | +0.75 / +0.57 | both halves | 9e-06 |  |
| [[C9orf153]] | +0.69 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[FAM210A]] | +0.69 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[POM121]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[POM121C]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[CTDP1]] | +0.67 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[LONP1]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[PRKRIP1]] | +0.65 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[AK2]] | +0.65 | +0.72 / +0.57 | both halves | 8e-06 |  |
| [[TSNAX-DISC1]] | +0.64 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[EEF1AKMT4]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF11]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PABIR1]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[ZFP36L2]] | -0.53 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[POGZ]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ROCK2]] | -0.52 | -0.52 / -0.43 | both halves | 4e-05 |  |
| [[CPLANE1]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[BCL7B]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRK3]] | C | GRK3 activity raises CRYBB2P1-1's level | lines that do not express GRK3 (3) vs lines expressing it (47) | 4.41× lower at baseline in the lines without GRK3 | 0.006 | ⚠ few lines (3 vs 47); across organs; also absent: PALS2, PAM; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRK3]] | C | CRYBB2P1-1 activity raises GRK3's level | lines that do not express CRYBB2P1-1 (4) vs lines expressing it (46) | 3.65× lower at baseline in the lines without CRYBB2P1-1 | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes |

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.816). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.8, -21.0); signed map (-40.7, 24.0). **Vector** length 117, 31.7% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.7 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.4 | +2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +3.8 | +3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +3.3 | +3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.7 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.7 | -13.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -11.0 | -17.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -8.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -8.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.8 | -5.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.9 | -4.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.9 | -3.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.6 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -4.5 |

## What is on record

> [!warning] No registry record
> CRYBB2P1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16576); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16576]; `tensor/DDL_lfc|DDL_z.npy` [16576]; `embed/gene_vectors.npy` [16576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16576 or target_col == 16576). Every well: [[CRYBB2P1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRYBB2P1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
