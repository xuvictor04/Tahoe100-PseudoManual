---
symbol: "EEA1"
type: "gene"
col: 2225
ensembl_id: "ENSG00000102189"
name: "early endosome antigen 1"
location: "12q22"
module: 179
arm: "-"
pooled_cpm: 125.05
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# EEA1

*early endosome antigen 1* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.96× (z +34.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.704× (z -7.6, q 2e-11, down in 33 of 47 measured lines) ⚠ toxic. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 10 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (KATO III 0.450×, J82 0.457×, RKO 0.435×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 2 lines (LoVo 0.486×, HT-29 0.463×); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (J82 0.448×, HT-29 0.499×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ROCK2]] (+0.59, fdr 1e-05), [[SMC6]] (+0.58, fdr 1e-05), [[KTN1]] (+0.58, fdr 7e-06); moves opposite to [[KHDC4]] (-0.62, fdr 7e-06), [[EDRF1]] (-0.61, fdr 1e-05), [[RBM14]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 179]] (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2225.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.96×** | +34.7 | 0e+00 | 47/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.63×** | +21.8 | 0e+00 | 48/48 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.52×** | +20.1 | 0e+00 | 47/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +13.4 | 1e-38 | 42/48 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +12.3 | 6e-33 | 37/49 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.63×** | +11.1 | 2e-26 | 35/49 (SNU-423, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +8.8 | 1e-16 | 41/48 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.50×** | +8.8 | 1e-16 | 32/44 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +8.2 | 2e-14 | 37/50 (LS 180, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.42×** | +7.9 | 2e-13 | 34/48 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +6.0 | 8e-08 | 28/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.27×** | +5.0 | 2e-05 | 24/45 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +5.0 | 3e-05 | 21/48 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.24×** | +4.9 | 4e-05 | 27/48 (HepG2/C3A, A549, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.24×** | +4.8 | 6e-05 | 26/47 (SNU-1, CFPAC-1, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.004 | 22/49 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.18× | +3.6 | 0.008 | 19/47 (H4, CFPAC-1, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 1.10× | +3.2 | 0.034 | 4/48 (HCT15, SW 1088, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.038 | 12/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | 1.10× | +3.0 | 0.059 | 4/49 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.14× | +3.0 | 0.063 | 17/47 (A498, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2225.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 10 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (KATO III 0.450×, J82 0.457×, RKO 0.435×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 2 lines (LoVo 0.486×, HT-29 0.463×); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (J82 0.448×, HT-29 0.499×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -7.6 | 2e-11 | 33/47 (KATO III, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -4.2 | 0.007 | 2/50 (NCI-H23, HOP62) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.879× | -4.1 | 0.007 | 4/48 (SHP-77, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.734×** | -3.7 | 0.037 | 25/45 (SNU-1, A549, …) | rises with dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.871× | -3.1 | 0.22 | 11/48 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2225. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 150 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +29.5) | — |
| [[NCI-H460 (line)]] | wt | 142 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +25.9) | [[Dinaciclib (drug)]] 0.05 µM 0.399× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[hTERT-HPNE (line)]] | wt | 112 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +23.2) | — |
| [[PANC-1 (line)]] | alt | 84.6 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +38.3) | — |
| [[A498 (line)]] | wt | 164 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +20.7) | — |
| [[C32 (line)]] | wt | 92.8 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +19.9) | — |
| [[HT-29 (line)]] | alt | 96.8 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +22.9) | [[Auranofin (drug)]] 5 µM 0.463× (z -10.3) |
| [[LoVo (line)]] | wt | 188 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +21.2) | [[Auranofin (drug)]] 5 µM 0.486× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 202 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +25.5) | — |
| [[NCI-H1573 (line)]] | alt | 43.8 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +20.3) | — |
| [[NCI-H23 (line)]] | alt | 59.9 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +20.4) | [[Adagrasib (drug)]] 0.05 µM 0.602× (z -15.6) ⚠ position not correctable |
| [[RKO (line)]] | wt | 238 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +28.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.435× (z -11.0) ⚠ toxic |
| [[SW 900 (line)]] | alt | 101 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +17.8) | — |
| [[A549 (line)]] | wt | 173 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.491× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 77.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +25.2) | — |
| [[HOP62 (line)]] | alt | 89.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +28.0) | — |
| [[LS 180 (line)]] | wt | 110 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +14.8) | [[Digitoxin (drug)]] 5 µM 0.488× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[SNU-423 (line)]] | alt | 209 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +21.6) | — |
| [[A-172 (line)]] | wt | 208 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +22.0) | — |
| [[A-427 (line)]] | wt | 90.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +24.8) | — |
| [[C-33 A (line)]] | alt | 54.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +13.9) | — |
| [[J82 (line)]] | alt | 200 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +18.0) | [[Ixazomib citrate (drug)]] 5 µM 0.443× (z -12.0) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.448× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 64.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +22.7) | — |
| [[SNU-1 (line)]] | wt | 124 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.5) | [[Bortezomib (drug)]] 5 µM 0.0774× (z -12.8) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 59.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +17.9) | — |
| [[HepG2_C3A (line)]] | wt | 191 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 110 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +20.0) | — |
| [[HS-578T (line)]] | alt | 111 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.3) | — |
| [[KATO III (line)]] | alt | 109 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +18.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.450× (z -11.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 114 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +18.3) | — |
| [[Panc 03.27 (line)]] | alt | 67.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.2) | — |
| [[RPMI-7951 (line)]] | alt | 122 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +16.2) | — |
| [[SK-MEL-2 (line)]] | alt | 225 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +19.5) | — |
| [[SW480 (line)]] | alt | 160 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +24.4) | — |
| [[H4 (line)]] | wt | 124 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 191 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +21.6) | — |
| [[BT-474 (line)]] | alt | 77.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.6) | [[Lonafarnib (drug)]] 5 µM 0.171× (z -9.4) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 60.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +16.6) | — |
| [[HCT15 (line)]] | alt | 131 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.5) | — |
| [[SW 1088 (line)]] | alt | 140 | 0 | 2 (2 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0911× (z -10.1) ⚠ toxic |
| [[SW1417 (line)]] | alt | 118 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +16.5) | — |
| [[HEC-1-A (line)]] | alt | 82.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 80.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 135 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 171 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 96.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2225), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROCK2]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[SMC6]] | +0.58 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[KTN1]] | +0.58 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[FER]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[PPP1R12A]] | +0.57 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[NOTCH2NLB]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[CCAR1]] | +0.57 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[VPS13C]] | +0.56 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[LRRC37A2]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[RO60]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ERCC6L2]] | +0.54 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[RAD50]] | +0.54 | +0.62 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KHDC4]] | -0.62 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[EDRF1]] | -0.61 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[RBM14]] | -0.60 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[LSM12]] | -0.58 | -0.69 / -0.46 | both halves | 3e-05 |  |
| [[USPL1]] | -0.57 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ATPAF2]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[ZNF589]] | -0.56 | -0.34 / -0.55 | both halves | 1e-04 | same gene group |
| [[SHQ1]] | -0.55 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[PPT2]] | -0.54 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.53 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[KLHDC3]] | -0.52 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[PMPCA]] | -0.52 | -0.56 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EEA1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **-** arm (projection on the module's main direction -0.651). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-1.3, -17.9); signed map (10.6, -10.4). **Vector** length 133, 42.5% of its response variance represented; |z| ≥ 3 in 1,329 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.4 | +21.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.2 | +20.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +34.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.5 | +13.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +6.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.5 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | +3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +0.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.8 | -7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.1 | -2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.7 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -4.4 | +3.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.4 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | +0.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.0 | -2.4 |
|  | [[Diphenhydramine (drug)]] 5 µM |  | -2.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | early endosome antigen 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:92,770,637-92,929,331 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZFYVE2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Zinc fingers FYVE-type |
| Reactome | 3 pathways, smallest: Toll Like Receptor 9 (TLR9) Cascade; Toll-like Receptor Cascades; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15075](https://www.uniprot.org/uniprotkb/Q15075) (Early endosome antigen 1):

> Binds phospholipid vesicles containing phosphatidylinositol 3-phosphate and participates in endosomal trafficking.

**Summary**, from NCBI Gene [8411](https://www.ncbi.nlm.nih.gov/gene/8411):

> Enables 1-phosphatidylinositol binding activity; GTP-dependent protein binding activity; and protein homodimerization activity. Involved in endocytosis and vesicle fusion. Located in cytosol and early endosome membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3185) · Entrez [8411](https://www.ncbi.nlm.nih.gov/gene/8411) · UniProt [Q15075](https://www.uniprot.org/uniprotkb/Q15075) · Ensembl [ENSG00000102189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102189)

## Data

Gene col 2225: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2225); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2225, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2225]; `tensor/DDL_lfc|DDL_z.npy` [2225]; `embed/gene_vectors.npy` [2225]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2225 or target_col == 2225). Every well: [[EEA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
