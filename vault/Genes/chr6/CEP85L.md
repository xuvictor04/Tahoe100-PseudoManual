---
symbol: "CEP85L"
type: "gene"
col: 3295
ensembl_id: "ENSG00000111860"
name: "centrosomal protein 85L"
location: "6q22.31"
module: 62
arm: "+"
pooled_cpm: 95.69
n_lines_expressing: 46
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# CEP85L

*centrosomal protein 85L* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.42× (z +8.7, q 1e-15, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.373× (z -24.6, q 0e+00, down in 40 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.686× (z -9.4, q 8e-19, down in 29 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 9 lines (C32 0.276×, A498 0.411×, SHP-77 0.455×, SW48 0.300×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (A549 0.0972×, A-427 0.0894×, LOX-IMVI 0.181×, C32 0.183×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (PANC-1 0.285×, LOX-IMVI 0.191×, NCI-H460 0.300×, HOP62 0.217×, …; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (C32 0.480×); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.189×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK1]] (+0.53, fdr 4e-05), [[GLTP]] (+0.52, fdr 2e-05), [[TIGAR]] (+0.52, fdr 2e-05); moves opposite to [[MANBAL]] (-0.42, fdr 1e-04), [[JAKMIP3]] (-0.42, fdr 1e-04), [[GATB]] (-0.41, fdr 1e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FZD1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[IKBIP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3295.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +8.7 | 1e-15 | 33/44 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +8.7 | 1e-15 | 30/44 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +7.7 | 2e-12 | 27/44 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +5.9 | 6e-07 | 21/43 (SHP-77, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +5.4 | 9e-06 | 23/44 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.3 | 9e-06 | 19/44 (SW480, LoVo, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.24×** | +5.3 | 9e-06 | 22/44 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.21×** | +4.9 | 8e-05 | 21/44 (SW1417, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.5 | 4e-04 | 17/43 (SW 900, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.19× | +4.4 | 6e-04 | 22/44 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.4 | 6e-04 | 19/44 (A498, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +4.3 | 8e-04 | 18/45 (SW480, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.3 | 8e-04 | 14/44 (SW480, SW1417, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.16× | +3.6 | 0.015 | 16/44 (NCI-H460, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.14× | +3.4 | 0.029 | 12/45 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.031 | 12/43 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.087 | 16/45 (NCI-H460, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3295.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 9 lines (C32 0.276×, A498 0.411×, SHP-77 0.455×, SW48 0.300×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (A549 0.0972×, A-427 0.0894×, LOX-IMVI 0.181×, C32 0.183×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (PANC-1 0.285×, LOX-IMVI 0.191×, NCI-H460 0.300×, HOP62 0.217×, …; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (C32 0.480×); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.189×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.373×** | -24.6 | 0e+00 | 40/45 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.387×** | -22.8 | 0e+00 | 37/40 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.559×** | -13.4 | 7e-39 | 33/42 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.686×** | -9.4 | 8e-19 | 29/44 (C32, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.745×** | -7.4 | 2e-11 | 29/44 (J82, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.804×** | -5.2 | 2e-05 | 21/43 (J82, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.856× | -3.9 | 0.008 | 17/44 (C32, NCI-H460, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.867× | -3.5 | 0.028 | 15/44 (C32, A-172, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.868× | -3.4 | 0.044 | 17/44 (LoVo, PANC-1, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.870× | -3.3 | 0.049 | 10/45 (HOP62, RPMI-7951, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.819×** | -3.2 | 0.071 | 9/43 (J82, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.880× | -3.2 | 0.071 | 6/44 (LoVo, SW 900, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3295. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 153 | 7 (3 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.228× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.411× (z -12.0) |
| [[C32 (line)]] | wt | 254 | 1 | 9 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 5.58× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.276× (z -15.9) |
| [[J82 (line)]] | alt | 105 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.534× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 148 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.469× (z -8.8) |
| [[SW48 (line)]] | wt | 125 | 3 | 3 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 8.88× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.300× (z -9.6) |
| [[SW480 (line)]] | alt | 46.1 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +19.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.67× (z +9.4) | — |
| [[A-427 (line)]] | wt | 82.3 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.57× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0894× (z -25.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 77.6 | 2 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +15.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.296× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.426× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 234 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -20.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 76.5 | 2 (2 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +8.9) ⚠ cell-cycle shift, explains ~47% of this change | [[Dinaciclib (drug)]] 5 µM 0.340× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 194 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -17.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 49.2 | 3 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.41× (z +9.2) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 5 µM 0.304× (z -12.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 135 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -18.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 193 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.525× (z -9.4) |
| [[HOP62 (line)]] | alt | 139 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -18.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 132 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 83.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -17.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 139 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.25× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -18.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 121 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -20.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 108 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.63× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -11.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 151 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.65× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -13.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 106 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0972× (z -27.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 142 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -9.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 25.1 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +9.8) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[HS-578T (line)]] | alt | 90.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -13.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 48.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.357× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 54.7 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.339× (z -10.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 38.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.298× (z -11.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 35.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -10.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 158 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.455× (z -9.8) |
| [[SW 900 (line)]] | alt | 117 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.375× (z -10.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.439× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 49.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -9.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 56.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 93.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 78.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 43.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +11.4) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.189× (z -9.0) |
| [[NCI-H661 (line)]] | alt | 87.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -8.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -11.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 116 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3295), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK1]] | +0.53 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[GLTP]] | +0.52 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[TIGAR]] | +0.52 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[PDE7A]] | +0.51 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[POLH]] | +0.51 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[CYFIP2]] | +0.50 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ACER2]] | +0.50 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[PRKY]] | +0.49 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[IKBIP]] | +0.49 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[FDXR]] | +0.48 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[SESN1]] | +0.48 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ACER3]] | +0.47 | +0.46 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MANBAL]] | -0.42 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[JAKMIP3]] | -0.42 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[GATB]] | -0.41 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[CLCN6]] | -0.40 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[MTERF4]] | -0.40 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[PISD]] | -0.40 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[TRIM16]] | -0.40 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[PATJ]] | -0.39 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[EXOC3]] | -0.39 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[POLR2M]] | -0.39 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[GTF2H3]] | -0.38 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[BROX]] | -0.38 | -0.38 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FZD1]] | B | FZD1 activity raises CEP85L's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 3.05× lower at baseline in the lines without FZD1 | 0.032 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[GLS2]] | B | GLS2 activity lowers CEP85L's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 2.08× higher at baseline in the lines without GLS2 | 0.042 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| [[ADAM12]] | B | ADAM12 activity raises CEP85L's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 2.20× lower at baseline in the lines without ADAM12 | 0.048 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[PATJ]] | B | PATJ activity lowers CEP85L's level | lines that do not express PATJ (9) vs lines expressing it (41) | 2.15× higher at baseline in the lines without PATJ | 0.089 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers CEP85L's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[IKBIP]] | C | IKBIP activity raises CEP85L's level | lines that do not express IKBIP (4) vs lines expressing it (46) | 5.34× lower at baseline in the lines without IKBIP | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SOAT1, NKAIN1, CEP85L; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IKBIP]] | C | CEP85L activity raises IKBIP's level | lines that do not express CEP85L (4) vs lines expressing it (46) | 3.97× lower at baseline in the lines without CEP85L | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17; co-absent with the target |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.7, 37.4); signed map (43.8, -25.7). **Vector** length 104, 28.0% of its response variance represented; |z| ≥ 3 in 1,157 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.3 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | -1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.7 | -9.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.3 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -0.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.8 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 85L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31 — chr6:118,460,772-118,710,075 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-BR-15, bA57K17.2; previously C6orf204 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SZL2](https://www.uniprot.org/uniprotkb/Q5SZL2) (Centrosomal protein of 85 kDa-like):

> Plays an essential role in neuronal cell migration.

**Summary**, from NCBI Gene [387119](https://www.ncbi.nlm.nih.gov/gene/387119):

> The protein encoded by this gene was identified as a breast cancer antigen. Nothing more is known of its function at this time. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:21638](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21638) · Entrez [387119](https://www.ncbi.nlm.nih.gov/gene/387119) · UniProt [Q5SZL2](https://www.uniprot.org/uniprotkb/Q5SZL2) · Ensembl [ENSG00000111860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111860)

## Data

Gene col 3295: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3295); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3295, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3295]; `tensor/DDL_lfc|DDL_z.npy` [3295]; `embed/gene_vectors.npy` [3295]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3295 or target_col == 3295). Every well: [[CEP85L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP85L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
