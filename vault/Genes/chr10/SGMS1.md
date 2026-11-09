---
symbol: "SGMS1"
type: "gene"
col: 12760
ensembl_id: "ENSG00000198964"
name: "sphingomyelin synthase 1"
location: "10q11.23"
module: 143
arm: "+"
pooled_cpm: 135.05
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# SGMS1

*sphingomyelin synthase 1* — 10q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +13.0, q 8e-36, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.428× (z -16.4, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SK-MEL-2 0.135×, NCI-H460 0.207×, NCI-H23 0.168×, A498 0.235×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.0997×, NCI-H460 0.217×, A498 0.255×, LoVo 0.290×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.139×, RKO 0.0912×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.376×, A-172 0.488×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.475×); [[Idoxuridine (drug)]] 0.5 µM in 1 line (SW 1088 0.0786×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COBLL1]] (+0.59, fdr 1e-05), [[JADE3]] (+0.57, fdr 3e-05), [[USP25]] (+0.56, fdr 1e-05); moves opposite to [[HIF1AN]] (-0.54, fdr 9e-05), [[EXOC3]] (-0.47, fdr 6e-05), [[PLCH2]] (-0.46, fdr 1e-04).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HLA-DRA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12760.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +13.0 | 8e-36 | 36/49 (hTERT-HPNE, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +6.6 | 1e-08 | 34/48 (HOP62, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.9 | 6e-07 | 28/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +5.0 | 1e-04 | 21/48 (hTERT-HPNE, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +4.7 | 3e-04 | 31/49 (NCI-H2030, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.6 | 4e-04 | 25/49 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +4.4 | 9e-04 | 27/50 (NCI-H1573, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +4.4 | 1e-03 | 24/48 (CFPAC-1, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +4.2 | 0.002 | 19/48 (Hs 766T, CFPAC-1, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.002 | 25/48 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.8 | 0.006 | 23/48 (CFPAC-1, HT-29, …) | two highest doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.006 | 22/50 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.20× | +3.7 | 0.009 | 22/48 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.011 | 19/48 (Hs 766T, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.011 | 20/48 (HOP62, COLO 205, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.034 | 18/50 (HepG2/C3A, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.17× | +3.2 | 0.046 | 14/48 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.083 | 14/48 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.083 | 17/47 (Hs 766T, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12760.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SK-MEL-2 0.135×, NCI-H460 0.207×, NCI-H23 0.168×, A498 0.235×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.0997×, NCI-H460 0.217×, A498 0.255×, LoVo 0.290×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.139×, RKO 0.0912×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.376×, A-172 0.488×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.475×); [[Idoxuridine (drug)]] 0.5 µM in 1 line (SW 1088 0.0786×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.428×** | -16.4 | 0e+00 | 40/44 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.483×** | -14.9 | 0e+00 | 42/49 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.581×** | -10.3 | 1e-22 | 41/45 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.726×** | -6.6 | 7e-09 | 33/48 (HT-29, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.721×** | -3.5 | 0.051 | 18/38 (SNU-423, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.843× | -3.3 | 0.091 | 15/49 (H4, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | 0.858× | -3.1 | 0.14 | 18/48 (NCI-H1573, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 95.3 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +15.6) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.488× (z -8.8) |
| [[A498 (line)]] | wt | 153 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -19.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 146 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -13.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 130 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -14.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 161 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0997× (z -29.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 97.4 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +10.7) | — |
| [[H4 (line)]] | wt | 107 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -17.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 209 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -9.1) |
| [[LoVo (line)]] | wt | 148 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -18.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 86.0 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -19.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 179 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -12.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 248 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -10.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 90.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -12.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 164 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -13.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 45.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +16.2) | — |
| [[HepG2_C3A (line)]] | wt | 173 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -12.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 77.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.268× (z -14.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 213 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -16.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 54.4 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.351× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 126 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.334× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.376× (z -10.0) |
| [[PANC-1 (line)]] | alt | 119 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -15.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 140 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0912× (z -23.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 120 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -13.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 146 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -12.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 89.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Docetaxel (drug)]] 0.05 µM 0.426× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~35% of this change |
| [[hTERT-HPNE (line)]] | wt | 83.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +18.4) | — |
| [[NCI-H2030 (line)]] | alt | 137 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -23.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 98.3 | 2 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.2× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 261 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -20.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 97.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -20.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 266 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 95.6 | 0 | 2 (1 ⚠) | — | [[Idoxuridine (drug)]] 0.5 µM 0.0786× (z -9.5) |
| [[AN3 CA (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -9.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 271 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.5) |
| [[HOP62 (line)]] | alt | 73.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +13.5) | — |
| [[Hs 766T (line)]] | wt | 103 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +13.5) | — |
| [[J82 (line)]] | alt | 95.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -9.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 82.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +12.6) | — |
| [[SW1417 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -15.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 90.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 100.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 151 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COBLL1]] | +0.59 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[JADE3]] | +0.57 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[USP25]] | +0.56 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[RIMKLB]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[NTN4]] | +0.49 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[FAM135A]] | +0.48 | +0.40 / +0.49 | both halves | 4e-05 |  |
| [[LINC02057]] | +0.48 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[NFIB]] | +0.47 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[GNAQ]] | +0.47 | +0.40 / +0.31 | both halves | 2e-04 |  |
| [[ZBTB8A]] | +0.46 | +0.43 / +0.35 | both halves | 1e-04 |  |
| [[ATXN2]] | +0.46 | +0.46 / +0.35 | both halves | 1e-04 |  |
| [[MAGI3]] | +0.45 | +0.39 / +0.50 | both halves | 5e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIF1AN]] | -0.54 | -0.55 / -0.37 | both halves | 9e-05 |  |
| [[EXOC3]] | -0.47 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[PLCH2]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[ARAP1]] | -0.45 | -0.49 / -0.34 | both halves | 1e-04 | same gene group |
| [[PRPF38A]] | -0.45 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[TUBGCP2]] | -0.44 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[ODAD4]] | -0.44 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[ZNF177]] | -0.43 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[LINC01237]] | -0.42 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[GSTM2]] | -0.42 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[ACOX3]] | -0.42 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[AGO1]] | -0.42 | -0.31 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-DRA]] | B | HLA-DRA activity weakens SGMS1's drug response | lines that do not express HLA-DRA (39) vs lines expressing it (10) | the lines without HLA-DRA respond 1.26× as strongly (z diff -0.55); strongest at Dinaciclib 0.5 µM: 0.41x vs 0.77x (z diff -4.5) | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530; target measured in part of the lines; both ways; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers SGMS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CSF1R]] | B | CSF1R activity lowers SGMS1's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 1.30× higher at baseline in the lines without CSF1R | 0.074 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.444). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.4, -24.9); signed map (9.2, -3.7). **Vector** length 98.7, 27.0% of its response variance represented; |z| ≥ 3 in 1,280 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.5 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +2.9 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | -1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -16.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | -14.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | sphingomyelin synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.23 — chr10:50,305,586-50,625,163 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MOB, MGC17342, SMS1; previously TMEM23 |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VZ5](https://www.uniprot.org/uniprotkb/Q86VZ5) (Phosphatidylcholine:ceramide cholinephosphotransferase 1):

> Major sphingomyelin synthase at the Golgi apparatus. Catalyzes the reversible transfer of phosphocholine moiety in sphingomyelin biosynthesis: in the forward reaction transfers phosphocholine head group of phosphatidylcholine (PC) on to ceramide (CER) to form ceramide phosphocholine (sphingomyelin, SM) and diacylglycerol (DAG) as by-product, and in the reverse reaction transfers phosphocholine from SM to DAG to form PC and CER. The direction of the reaction depends on the levels of CER and DAG …

**Summary**, from NCBI Gene [259230](https://www.ncbi.nlm.nih.gov/gene/259230):

> The protein encoded by this gene is predicted to be a five-pass transmembrane protein. This gene may be predominately expressed in brain. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:29799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29799) · Entrez [259230](https://www.ncbi.nlm.nih.gov/gene/259230) · UniProt [Q86VZ5](https://www.uniprot.org/uniprotkb/Q86VZ5) · Ensembl [ENSG00000198964](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198964)

## Data

Gene col 12760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12760); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12760]; `tensor/DDL_lfc|DDL_z.npy` [12760]; `embed/gene_vectors.npy` [12760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12760 or target_col == 12760). Every well: [[SGMS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGMS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
