---
symbol: "UBR1"
type: "gene"
col: 8257
ensembl_id: "ENSG00000159459"
name: "ubiquitin protein ligase E3 component n-recognin 1"
location: "15q15.2"
module: 12
arm: "+"
pooled_cpm: 139.92
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# UBR1

*ubiquitin protein ligase E3 component n-recognin 1* — 15q15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.34× (z +8.7, q 3e-15, up in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~23% of this change. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.35× (z +8.5, q 7e-15, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.532× (z -18.6, q 0e+00, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.789× (z -9.8, q 1e-20, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POMP]] (+0.64, fdr 1e-05), [[ARFIP1]] (+0.56, fdr 1e-05), [[HIBCH]] (+0.56, fdr 1e-05); moves opposite to [[PMS2P1]] (-0.50, fdr 3e-05), [[PTPN18]] (-0.50, fdr 2e-05), [[CASC3]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8257.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.34×** | +8.7 | 3e-15 | 31/48 (HEC-1-A, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +8.5 | 7e-15 | 31/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +8.1 | 2e-13 | 33/49 (SW480, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +6.7 | 2e-09 | 27/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +5.7 | 1e-06 | 17/48 (A-172, SNU-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.21×** | +5.7 | 1e-06 | 23/49 (SW 900, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +4.8 | 1e-04 | 11/48 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.12× | +4.8 | 1e-04 | 10/48 (NCI-H23, LS 180, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.7 | 1e-04 | 21/48 (NCI-H2347, PANC-1, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +4.4 | 7e-04 | 20/48 (PANC-1, NCI-H23, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +4.3 | 7e-04 | 21/48 (C32, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.7 | 0.009 | 17/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.12× | +3.3 | 0.038 | 7/48 (RKO, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.12× | +3.3 | 0.040 | 14/48 (BT-474, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.061 | 11/49 (LOX-IMVI, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.076 | 14/48 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.076 | 2/48 (SNU-423, C-33 A) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.11× | +3.0 | 0.076 | 6/48 (NCI-H1792, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8257.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.532×** | -18.6 | 0e+00 | 44/49 (COLO 205, A-427, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.617×** | -13.6 | 6e-40 | 36/44 (NCI-H23, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.609×** | -13.5 | 4e-39 | 36/45 (NCI-H460, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.702×** | -10.0 | 3e-21 | 32/47 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.789×** | -9.8 | 1e-20 | 31/49 (HOP62, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.734×** | -9.0 | 1e-17 | 36/48 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.740×** | -8.8 | 8e-17 | 31/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.776×** | -7.4 | 7e-12 | 28/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.825×** | -5.6 | 1e-06 | 24/47 (HT-29, LS 180, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.827×** | -5.5 | 2e-06 | 24/48 (PANC-1, KATO III, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.842× | -5.0 | 3e-05 | 22/48 (PANC-1, NCI-H460, …) | two highest doses | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.902× | -4.2 | 0.001 | 10/49 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.871× | -4.0 | 0.003 | 19/48 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.7 | 0.007 | 16/50 (NCI-H23, HOP62, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.836× | -3.7 | 0.007 | 18/47 (hTERT-HPNE, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | 0.886× | -3.5 | 0.014 | 6/48 (hTERT-HPNE, SW48, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.883× | -3.5 | 0.014 | 15/47 (LS 180, LoVo, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 0.923× | -3.3 | 0.030 | 5/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.912× | -3.2 | 0.034 | 10/48 (SW480, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.892× | -3.1 | 0.052 | 8/48 (NCI-H23, COLO 205, …) | all doses, flat |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.901× | -2.9 | 0.085 | 11/47 (A-427, SW48, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.903× | -2.8 | 0.094 | 10/48 (LoVo, NCI-H2030, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.830×** | -2.8 | 0.094 | 13/46 (CHP-212, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8257. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 130 | 4 (3 ⚠) | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 1.64× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.433× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.498× (z -13.6) |
| [[HOP62 (line)]] | alt | 124 | 1 | 9 (7 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.69× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -20.5) |
| [[NCI-H460 (line)]] | wt | 124 | 1 (1 ⚠) | 9 (8 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 0.5 µM 0.454× (z -14.3) |
| [[HT-29 (line)]] | alt | 269 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.470× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 150 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.78× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.391× (z -16.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 123 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.445× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.521× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 151 | 2 (1 ⚠) | 3 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.00× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 123 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.122× (z -30.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 156 | 2 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.50× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -14.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 351 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.604× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 159 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.385× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 159 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -18.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -12.8) |
| [[A-172 (line)]] | wt | 103 | 2 | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.52× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.516× (z -9.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 103 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -14.6) |
| [[C-33 A (line)]] | alt | 135 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -13.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 196 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.425× (z -11.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 145 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.274× (z -12.9) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 150 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -12.3) |
| [[LoVo (line)]] | wt | 244 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 218 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -10.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.462× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 192 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -9.2) |
| [[A498 (line)]] | wt | 115 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.508× (z -11.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 130 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.28× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -9.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 119 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -13.2) |
| [[LS 180 (line)]] | wt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.522× (z -10.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 148 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.13× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.423× (z -10.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 135 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -15.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -10.7) |
| [[SW1417 (line)]] | alt | 119 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.490× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -9.2) |
| [[A-427 (line)]] | wt | 89.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -20.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 196 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -10.5) |
| [[HCT15 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 87.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -10.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 76.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 76.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -14.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 93.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 147 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8257), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POMP]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ARFIP1]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[HIBCH]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[PSMC1]] | +0.55 | +0.64 / +0.37 | both halves | 9e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[AP1G1]] | +0.52 | +0.59 / +0.38 | both halves | 7e-05 |  |
| [[USP8]] | +0.52 | +0.58 / +0.44 | both halves | 3e-05 | STRING 443 |
| [[ATF1]] | +0.51 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[DHX36]] | +0.50 | +0.50 / +0.46 | both halves | 3e-05 | STRING 441 |
| [[SAP30BP]] | +0.50 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[BIN3]] | +0.50 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[SLC10A7]] | +0.50 | +0.57 / +0.37 | both halves | 8e-05 |  |
| [[MRPL27]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P1]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[PTPN18]] | -0.50 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[CASC3]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[CRNDE]] | -0.47 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[SEC61A2]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[SEC22C]] | -0.46 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[SNHG22]] | -0.46 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[ABCB10]] | -0.46 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[UBQLN4]] | -0.46 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[PSMG4]] | -0.46 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[PCGF5]] | -0.45 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[CAMKK2]] | -0.45 | -0.46 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers UBR1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.348). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.9, -7.1); signed map (-7.9, -6.8). **Vector** length 118, 33.9% of its response variance represented; |z| ≥ 3 in 1,310 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.6 | +8.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +6.6 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.2 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +4.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +4.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.0 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -6.3 | -7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -9.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.2 | -4.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.9 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.8 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.0 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin protein ligase E3 component n-recognin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.2 — chr15:42,942,897-43,106,113 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ubiquitin protein ligase E3 component n-recognins; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWV7](https://www.uniprot.org/uniprotkb/Q8IWV7) (E3 ubiquitin-protein ligase UBR1):

> E3 ubiquitin-protein ligase which is a component of the N-end rule pathway. Recognizes and binds proteins bearing specific N-terminal residues that are destabilizing according to the N-end rule, leading to their ubiquitination and subsequent degradation. Recognizes both type-1 and type-2 N-degrons, containing positively charged amino acids (Arg, Lys and His) and bulky and hydrophobic amino acids, respectively. Does not ubiquitinate proteins that are acetylated at the N-terminus. In contrast, it …

**Summary**, from NCBI Gene [197131](https://www.ncbi.nlm.nih.gov/gene/197131):

> The N-end rule pathway is one proteolytic pathway of the ubiquitin system. The recognition component of this pathway, encoded by this gene, binds to a destabilizing N-terminal residue of a substrate protein and participates in the formation of a substrate-linked multiubiquitin chain. This leads to the eventual degradation of the substrate protein. The protein described in this record has a RING-type zinc finger and a UBR-type zinc finger. Mutations in this gene have been associated with …

**Accessions** — [HGNC:16808](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16808) · Entrez [197131](https://www.ncbi.nlm.nih.gov/gene/197131) · UniProt [Q8IWV7](https://www.uniprot.org/uniprotkb/Q8IWV7) · Ensembl [ENSG00000159459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159459)

## Data

Gene col 8257: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8257); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8257, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8257]; `tensor/DDL_lfc|DDL_z.npy` [8257]; `embed/gene_vectors.npy` [8257]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8257 or target_col == 8257). Every well: [[UBR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
