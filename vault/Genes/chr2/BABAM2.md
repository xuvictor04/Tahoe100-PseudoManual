---
symbol: "BABAM2"
type: "gene"
col: 8123
ensembl_id: "ENSG00000158019"
name: "BRISC and BRCA1 A complex member 2"
location: "2p23.2"
module: 200
arm: "+"
pooled_cpm: 249.88
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 35
n_dd_up_clean: 9
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# BABAM2

*BRISC and BRCA1 A complex member 2* — 2p23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.44× (z +6.5, q 5e-08, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (18 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.271× (z -23.9, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FHIT]] (+0.66, fdr 7e-06), [[LINC01473]] (+0.65, fdr 7e-06), [[FGGY]] (+0.62, fdr 7e-06); moves opposite to [[CYP27C1]] (-0.51, fdr 3e-05), [[CCDC168]] (-0.50, fdr 6e-05), [[GMIP]] (-0.49, fdr 5e-05).
> It is in [[Module 200]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PRKN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8123.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +6.5 | 5e-08 | 40/47 (AsPC-1, HepG2/C3A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +5.0 | 1e-04 | 26/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.33×** | +5.0 | 1e-04 | 37/50 (A-172, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 4e-04 | 32/47 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.006 | 25/48 (A-172, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.23×** | +3.8 | 0.011 | 24/49 (NCI-H2347, HOP62, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.019 | 27/48 (A-172, LoVo, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.025 | 25/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.027 | 26/49 (MIA PaCa-2, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.028 | 33/50 (A-172, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.029 | 12/49 (NCI-H2347, LS 180, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.1 | 0.082 | 22/49 (J82, hTERT-HPNE, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.082 | 15/48 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.097 | 20/48 (LoVo, HOP62, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.097 | 20/49 (AsPC-1, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 22 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8123.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.271×** | -23.9 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.280×** | -23.3 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.419×** | -22.5 | 0e+00 | 48/49 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.375×** | -17.9 | 0e+00 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.386×** | -16.8 | 0e+00 | 42/44 (NCI-H23, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.537×** | -16.1 | 0e+00 | 38/48 (C32, NCI-H1792, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.421×** | -15.9 | 0e+00 | 45/49 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.430×** | -15.4 | 0e+00 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.424×** | -15.1 | 0e+00 | 46/48 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.428×** | -14.9 | 0e+00 | 44/47 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.453×** | -13.9 | 2e-42 | 46/48 (C32, A498, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.486×** | -12.7 | 2e-35 | 44/47 (LoVo, HCT15, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.488×** | -12.6 | 6e-35 | 43/50 (NCI-H23, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.534×** | -11.5 | 6e-29 | 44/48 (SK-MEL-2, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.516×** | -11.2 | 1e-27 | 40/45 (A-427, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.587×** | -9.8 | 5e-21 | 40/48 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.362×** | -9.7 | 7e-21 | 45/49 (C32, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.648×** | -7.9 | 5e-14 | 39/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.449×** | -7.7 | 4e-13 | 39/48 (MIA PaCa-2, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.664×** | -7.5 | 2e-12 | 37/48 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.676×** | -7.2 | 2e-11 | 42/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.715×** | -6.1 | 2e-08 | 40/48 (C32, C-33 A, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.776×** | -4.7 | 6e-05 | 32/48 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -4.6 | 7e-05 | 27/48 (SW1417, COLO 205, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.777×** | -4.6 | 7e-05 | 32/47 (CFPAC-1, NCI-H1792, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.774×** | -4.5 | 1e-04 | 30/48 (CFPAC-1, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8123. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 554 | 0 | 24 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -32.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -24.7) |
| [[SW480 (line)]] | alt | 218 | 0 | 24 (15 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -35.1) |
| [[PANC-1 (line)]] | alt | 330 | 0 | 22 (15 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -32.0) |
| [[NCI-H460 (line)]] | wt | 323 | 0 | 19 (13 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.201× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -21.1) |
| [[NCI-H1792 (line)]] | alt | 316 | 0 | 17 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -24.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -18.4) |
| [[CFPAC-1 (line)]] | alt | 296 | 0 | 16 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -11.8) |
| [[KATO III (line)]] | alt | 249 | 0 | 16 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -26.6) |
| [[MIA PaCa-2 (line)]] | alt | 404 | 0 | 16 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -21.0) |
| [[SW1417 (line)]] | alt | 223 | 0 | 16 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -23.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -22.2) |
| [[NCI-H23 (line)]] | alt | 453 | 0 | 15 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0306× (z -48.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -19.2) |
| [[SNU-1 (line)]] | wt | 291 | 0 | 15 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0564× (z -31.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -17.3) |
| [[SW 900 (line)]] | alt | 270 | 0 | 15 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -16.5) |
| [[HepG2_C3A (line)]] | wt | 296 | 0 | 14 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -21.2) |
| [[HT-29 (line)]] | alt | 189 | 0 | 14 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -22.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.238× (z -18.2) |
| [[LoVo (line)]] | wt | 198 | 0 | 14 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -24.0) |
| [[A549 (line)]] | wt | 364 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -21.7) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -19.2) |
| [[C-33 A (line)]] | alt | 267 | 0 | 13 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.175× (z -18.7) |
| [[LS 180 (line)]] | wt | 191 | 0 | 13 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -24.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -23.2) |
| [[SW48 (line)]] | wt | 192 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -18.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -17.7) |
| [[A-427 (line)]] | wt | 341 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0303× (z -46.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -16.7) |
| [[A498 (line)]] | wt | 272 | 0 | 12 (10 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.176× (z -21.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -19.4) |
| [[COLO 205 (line)]] | alt | 293 | 0 | 12 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -22.4) |
| [[LOX-IMVI (line)]] | wt | 195 | 0 | 12 (8 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -15.2) |
| [[RKO (line)]] | wt | 234 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -18.3) |
| [[H4 (line)]] | wt | 180 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -18.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 189 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -22.7) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -16.4) |
| [[J82 (line)]] | alt | 116 | 0 | 10 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -15.7) |
| [[SK-MEL-2 (line)]] | alt | 292 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -26.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -17.5) |
| [[SNU-423 (line)]] | alt | 283 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -22.5) |
| [[Hs 766T (line)]] | wt | 199 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 393 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.295× (z -12.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 144 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -14.7) |
| [[RPMI-7951 (line)]] | alt | 263 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -18.3) |
| [[HCT15 (line)]] | alt | 214 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -16.1) |
| [[HOP62 (line)]] | alt | 180 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.205× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -19.2) |
| [[BT-474 (line)]] | alt | 146 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -13.8) |
| [[CHP-212 (line)]] | wt | 224 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0931× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -15.4) |
| [[A-172 (line)]] | wt | 147 | 2 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +15.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.31× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -14.1) |
| [[HS-578T (line)]] | alt | 147 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 335 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SHP-77 (line)]] | alt | 125 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.225× (z -17.0) |
| [[AN3 CA (line)]] | alt | 169 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.136× (z -14.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 163 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.300× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -13.6) |
| [[SW 1271 (line)]] | alt | 357 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -15.0) |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.139× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 90.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -9.4) |
| [[SW 1088 (line)]] | alt | 252 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0589× (z -15.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 237 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8123), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHIT]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 | same gene group |
| [[LINC01473]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[FGGY]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[RAD51B]] | +0.60 | +0.64 / +0.56 | both halves | 1e-05 | pathway: DNA Double-Strand Break Repair |
| [[IMMP2L]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ATG10]] | +0.57 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[WWOX]] | +0.56 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[GMDS-DT]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ZNF608]] | +0.51 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[LYPLAL1]] | +0.51 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[PPP1R3C]] | +0.51 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[ARL4A]] | +0.50 | +0.39 / +0.44 | both halves | 5e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP27C1]] | -0.51 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[CCDC168]] | -0.50 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[GMIP]] | -0.49 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[LOXL1-AS1]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SLC22A20P]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[LOXL1]] | -0.47 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ZBTB34]] | -0.47 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[INPP5E]] | -0.47 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ANTXR2]] | -0.47 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[FLI1]] | -0.46 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[TWIST2]] | -0.46 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[MMP14]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKN]] | B | PRKN activity raises BABAM2's level | lines that do not express PRKN (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without PRKN | 0.013 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[MAP2K1]] | B | MAP2K1 activity lowers BABAM2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[WWOX]] | B | WWOX activity raises BABAM2's level | lines that do not express WWOX (5) vs lines expressing it (45) | 1.79× lower at baseline in the lines without WWOX | 0.035 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[ST6GALNAC2]] | B | ST6GALNAC2 activity raises BABAM2's level | lines that do not express ST6GALNAC2 (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without ST6GALNAC2 | 0.083 | ⚠ within organs, on part of the lines; also absent: CELSR1, CTSD, TRIM47; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity lowers BABAM2's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-25.5, 31.3); signed map (9.5, -12.3). **Vector** length 88.1, 37.7% of its response variance represented; |z| ≥ 3 in 2,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.5 | -16.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | -7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | -2.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.8 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.6 | -13.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.2 | +2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | +3.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -9.5 | -16.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -22.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.1 | -14.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | -6.8 | -15.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -15.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -1.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.7 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -4.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.6 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | BRISC and BRCA1 A complex member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.2 — chr2:27,889,941-28,338,901 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BRCC45, BRCC4; previously BRE |
| Gene groups (HGNC) | BRCA1 A complex; BRISC complex; MicroRNA protein coding host genes |
| Reactome | 14 pathways, smallest: Metalloprotease DUBs; Nonhomologous End-Joining (NHEJ); Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXR7](https://www.uniprot.org/uniprotkb/Q9NXR7) (BRISC and BRCA1-A complex member 2):

> Component of the BRCA1-A complex, a complex that specifically recognizes 'Lys-63'-linked ubiquitinated histones H2A and H2AX at DNA lesions sites, leading to target the BRCA1-BARD1 heterodimer to sites of DNA damage at double-strand breaks (DSBs). The BRCA1-A complex also possesses deubiquitinase activity that specifically removes 'Lys-63'-linked ubiquitin on histones H2A and H2AX. In the BRCA1-A complex, it acts as an adapter that bridges the interaction between BABAM1/NBA1 and the rest of the …

**Summary**, from NCBI Gene [9577](https://www.ncbi.nlm.nih.gov/gene/9577):

> This gene encodes an anti-apoptotic, death receptor-associated protein that interacts with tumor necrosis factor-receptor-1. The encoded protein acts as an adapter in several protein complexes, including the BRCA1-A complex and the BRISC complex. The BRCA1-A complex possesses ubiquitinase activity and targets sites of double strand DNA breaks, while the BRISC complex exhibits deubiquitinase activity and is involved in mitotic spindle assembly. This gene is upregulated in several types of …

**Accessions** — [HGNC:1106](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1106) · Entrez [9577](https://www.ncbi.nlm.nih.gov/gene/9577) · UniProt [Q9NXR7](https://www.uniprot.org/uniprotkb/Q9NXR7) · Ensembl [ENSG00000158019](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158019)

## Data

Gene col 8123: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8123); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8123, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8123]; `tensor/DDL_lfc|DDL_z.npy` [8123]; `embed/gene_vectors.npy` [8123]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8123 or target_col == 8123). Every well: [[BABAM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BABAM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
