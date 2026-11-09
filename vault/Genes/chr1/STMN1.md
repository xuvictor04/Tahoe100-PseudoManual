---
symbol: "STMN1"
type: "gene"
col: 3936
ensembl_id: "ENSG00000117632"
name: "stathmin 1"
location: "1p36.11"
module: 22
arm: "+"
pooled_cpm: 85.92
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# STMN1

*stathmin 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.90× (z +19.3, q 0e+00, up in 46 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +6.6, q 5e-09, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.543× (z -5.8, q 5e-06, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.756× (z -4.0, q 0.011, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUSAP1]] (+0.82, fdr 7e-06), [[NCAPG]] (+0.81, fdr 7e-06), [[KIF11]] (+0.78, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MYBL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3936.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **6.90×** | +19.3 | 0e+00 | 46/46 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **5.73×** | +16.7 | 0e+00 | 41/41 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.85×** | +12.4 | 4e-33 | 44/44 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.00×** | +6.7 | 4e-09 | 39/47 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.6 | 5e-09 | 34/47 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~73% of this change | **1.81×** | +5.9 | 3e-07 | 39/47 (HT-29, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.84×** | +5.9 | 4e-07 | 37/46 (C32, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.49×** | +5.6 | 1e-06 | 27/47 (NCI-H1792, C32, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **1.74×** | +5.5 | 2e-06 | 37/47 (hTERT-HPNE, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.2 | 1e-05 | 32/46 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.52×** | +4.2 | 0.002 | 28/47 (hTERT-HPNE, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.34×** | +4.1 | 0.002 | 36/47 (SW 900, CFPAC-1, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.003 | 29/47 (A-172, J82, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.51×** | +4.0 | 0.003 | 29/47 (HOP62, A-172, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.44×** | +3.6 | 0.010 | 28/46 (HOP62, A549, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.82×** | +3.6 | 0.013 | 31/47 (HOP62, SW480, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.020 | 24/46 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **1.91×** | +3.3 | 0.026 | 24/44 (HOP62, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.40×** | +3.3 | 0.026 | 24/47 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.035 | 24/47 (J82, LOX-IMVI, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.37×** | +2.9 | 0.090 | 20/47 (NCI-H460, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3936.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.543×** | -5.8 | 5e-06 | 39/47 (SNU-1, LS 180, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.567×** | -5.6 | 6e-06 | 36/47 (HEC-1-A, NCI-H2030, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.449×** | -4.1 | 0.007 | 29/44 (NCI-H23, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.756×** | -4.0 | 0.011 | 33/47 (SK-MEL-2, SW48, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.473×** | -3.9 | 0.012 | 31/47 (HEC-1-A, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.537×** | -3.7 | 0.020 | 28/47 (KATO III, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **0.780×** | -3.5 | 0.036 | 27/47 (HT-29, COLO 205, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.714×** | -3.4 | 0.054 | 26/47 (KATO III, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.78 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3936. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 53.2 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.5× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.59× (z +9.3) | — |
| [[A-172 (line)]] | wt | 89.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.04× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 89.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.20× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[H4 (line)]] | wt | 101 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 8.11× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.153× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 52.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.4× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LOX-IMVI (line)]] | wt | 84.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.03× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 94.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.44× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RPMI-7951 (line)]] | alt | 71.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.22× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 121 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.63× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-423 (line)]] | alt | 71.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.31× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +10.9) | — |
| [[A-427 (line)]] | wt | 174 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 52.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.31× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 31.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.3× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 44.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.81× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 143 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HOP62 (line)]] | alt | 100 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HS-578T (line)]] | alt | 48.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.29× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HT-29 (line)]] | alt | 56.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.29× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[J82 (line)]] | alt | 191 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.1) | — |
| [[KATO III (line)]] | alt | 62.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.81× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 24.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.7× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LS 180 (line)]] | wt | 45.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Selinexor (drug)]] 5 µM 0.264× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 21.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +21.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 77.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 38.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.11× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Panc 03.27 (line)]] | alt | 45.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 129 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.14× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW1417 (line)]] | alt | 81.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW48 (line)]] | wt | 98.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.87× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.203× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 138 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HCT15 (line)]] | alt | 106 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.12× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 53.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.77× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2030 (line)]] | alt | 169 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 157 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Bortezomib (drug)]] 5 µM 0.128× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[RKO (line)]] | wt | 79.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SHP-77 (line)]] | alt | 189 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-1 (line)]] | wt | 62.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 7.05× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Bortezomib (drug)]] 0.05 µM 0.130× (z -10.4) ⚠ cell-cycle shift, explains ~63% of this change |
| [[SW 900 (line)]] | alt | 62.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.06× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW480 (line)]] | alt | 130 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[BT-474 (line)]] | alt | 63.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HepG2_C3A (line)]] | wt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.6× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[AN3 CA (line)]] | alt | 149 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3936), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUSAP1]] | +0.82 | +0.84 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 455 |
| [[NCAPG]] | +0.81 | +0.85 / +0.76 | both halves | 7e-06 |  |
| [[KIF11]] | +0.78 | +0.83 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 460 |
| [[FOXM1]] | +0.77 | +0.80 / +0.69 | both halves | 7e-06 | STRING 409 |
| [[NCAPD2]] | +0.77 | +0.79 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[H2AZ2]] | +0.77 | +0.79 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[BIRC5]] | +0.76 | +0.84 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 643 |
| [[SKA2]] | +0.76 | +0.71 / +0.72 | both halves | 7e-06 | same gene group |
| [[CDK1]] | +0.75 | +0.80 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 600 |
| [[SPC25]] | +0.75 | +0.73 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[TPX2]] | +0.75 | +0.80 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[PRC1]] | +0.75 | +0.81 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 406 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | B | MYBL1 activity raises STMN1's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 2.31× lower at baseline in the lines without MYBL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers STMN1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises STMN1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[AURKB]] | C | AURKB activity raises STMN1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.05× lower at baseline in the lines without AURKB | 0.028 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises STMN1's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.03× lower at baseline in the lines without PBK | 0.030 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises STMN1's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.82× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.8, -53.6); signed map (-47.7, -44.9). **Vector** length 113, 47.1% of its response variance represented; |z| ≥ 3 in 1,143 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.64 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.58 to 48); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.57 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | +4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | +3.7 | +5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.6 | +3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.1 | +5.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.0 | -0.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +1.7 | -0.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | -8.6 | -5.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.1 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -6.4 | -3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -6.1 | -3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.6 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | stathmin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:25,884,181-25,906,991 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMN, OP18, PR22, PP19, PP17, Lag, FLJ32206; previously LAP18, C1orf215 |
| Gene groups (HGNC) | Stathmins; MicroRNA protein coding host genes |
| Hallmark sets | GLYCOLYSIS, G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 3 pathways, smallest: Nuclear signaling by ERBB4; Signaling by ERBB4; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [P16949](https://www.uniprot.org/uniprotkb/P16949) (Stathmin):

> Involved in the regulation of the microtubule (MT) filament system by destabilizing microtubules. Prevents assembly and promotes disassembly of microtubules. Phosphorylation at Ser-16 may be required for axon formation during neurogenesis. Involved in the control of the learned and innate fear (By similarity).

**Summary**, from NCBI Gene [3925](https://www.ncbi.nlm.nih.gov/gene/3925):

> This gene belongs to the stathmin family of genes. It encodes a ubiquitous cytosolic phosphoprotein proposed to function as an intracellular relay integrating regulatory signals of the cellular environment. The encoded protein is involved in the regulation of the microtubule filament system by destabilizing microtubules. It prevents assembly and promotes disassembly of microtubules. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb …

**Accessions** — [HGNC:6510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6510) · Entrez [3925](https://www.ncbi.nlm.nih.gov/gene/3925) · UniProt [P16949](https://www.uniprot.org/uniprotkb/P16949) · Ensembl [ENSG00000117632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117632)

## Data

Gene col 3936: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3936); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3936, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3936]; `tensor/DDL_lfc|DDL_z.npy` [3936]; `embed/gene_vectors.npy` [3936]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3936 or target_col == 3936). Every well: [[STMN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STMN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
