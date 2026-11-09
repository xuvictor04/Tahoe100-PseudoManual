---
symbol: "PPP2R3A"
type: "gene"
col: 1056
ensembl_id: "ENSG00000073711"
name: "protein phosphatase 2 regulatory subunit B''alpha"
location: "3q22.2-q22.3"
module: 1
arm: "-"
pooled_cpm: 97.84
n_lines_expressing: 46
n_dd_up: 5
n_dd_down: 21
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PPP2R3A

*protein phosphatase 2 regulatory subunit B''alpha* — 3q22.2-q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.21× (z +6.2, q 4e-07, up in 19 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.655× (z -13.6, q 1e-39, down in 31 of 44 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.406× (z -10.8, q 8e-25, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPST2]] (+0.60, fdr 1e-05), [[CBL]] (+0.57, fdr 1e-05), [[MYO9B]] (+0.57, fdr 1e-05); moves opposite to [[MCCC2]] (-0.56, fdr 3e-05), [[UTP15]] (-0.56, fdr 2e-05), [[TRUB1]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[DTNA]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GPR161]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1056.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +6.2 | 4e-07 | 19/44 (PANC-1, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.24×** | +4.8 | 4e-04 | 24/45 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +4.6 | 7e-04 | 19/44 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +4.0 | 0.008 | 15/43 (SK-MEL-2, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.39×** | +4.0 | 0.008 | 21/41 (NCI-H460, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.19× | +3.8 | 0.016 | 16/43 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.047 | 12/46 (A-172, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Rifaximin (drug)]] 5 µM |  | 1.16× | +3.3 | 0.061 | 6/44 (A549, Panc 03.27, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.16× | +3.3 | 0.061 | 13/46 (C32, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.10× | +3.1 | 0.10 | 3/44 (AN3 CA, LoVo, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.15× | +3.1 | 0.11 | 7/44 (A-427, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1056.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.655×** | -13.6 | 1e-39 | 31/44 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.587×** | -12.2 | 1e-31 | 36/45 (NCI-H23, H4, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.581×** | -11.9 | 2e-30 | 37/44 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.406×** | -10.8 | 8e-25 | 38/45 (A-427, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -9.2 | 3e-18 | 34/44 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.672×** | -9.1 | 1e-17 | 31/44 (LOX-IMVI, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.662×** | -8.7 | 2e-16 | 28/42 (RPMI-7951, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.675×** | -8.6 | 5e-16 | 31/41 (HS-578T, C32, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.680×** | -8.5 | 2e-15 | 33/43 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.698×** | -7.9 | 2e-13 | 30/43 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.812×** | -6.7 | 1e-09 | 26/44 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.582×** | -6.5 | 5e-09 | 28/44 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.597×** | -6.2 | 3e-08 | 26/37 (LOX-IMVI, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.771×** | -5.9 | 1e-07 | 24/44 (LOX-IMVI, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.772×** | -5.9 | 1e-07 | 27/44 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.796×** | -5.2 | 7e-06 | 23/44 (A-172, RPMI-7951, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.863× | -4.8 | 6e-05 | 15/44 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.829×** | -4.3 | 5e-04 | 20/44 (LOX-IMVI, A549, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.829×** | -4.3 | 5e-04 | 22/44 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.838× | -4.0 | 0.001 | 19/44 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.841× | -3.8 | 0.004 | 18/45 (HOP62, HS-578T, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.843× | -3.8 | 0.004 | 19/44 (NCI-H1792, C32, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.850× | -3.7 | 0.005 | 18/44 (NCI-H460, SW 1088, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.860× | -3.2 | 0.033 | 16/43 (SNU-1, AN3 CA, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.907× | -3.1 | 0.036 | 10/44 (NCI-H2347, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1056. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 239 | 0 | 16 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -23.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.311× (z -14.4) |
| [[HOP62 (line)]] | alt | 110 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.212× (z -10.7) |
| [[PANC-1 (line)]] | alt | 62.6 | 1 (1 ⚠) | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.03× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -16.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.457× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 92.3 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.303× (z -12.1) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.428× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 192 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.242× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 161 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.393× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 327 | 1 | 4 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 1.91× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 133 | 0 | 4 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.149× (z -13.4) |
| [[C-33 A (line)]] | alt | 105 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.418× (z -8.5) |
| [[HS-578T (line)]] | alt | 249 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[J82 (line)]] | alt | 99.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 176 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.447× (z -10.5) |
| [[AN3 CA (line)]] | alt | 138 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[C32 (line)]] | wt | 123 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[H4 (line)]] | wt | 183 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.433× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 65.7 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.443× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.464× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 43.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.313× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[A549 (line)]] | wt | 72.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -16.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.399× (z -10.2) |
| [[Hs 766T (line)]] | wt | 61.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[LoVo (line)]] | wt | 45.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.347× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 85.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H23 (line)]] | alt | 77.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -25.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[RKO (line)]] | wt | 92.3 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.312× (z -11.9) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.194× (z -9.1) |
| [[SNU-423 (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -9.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW1417 (line)]] | alt | 131 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.464× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~44% of this change |
| [[A498 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.532× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[CFPAC-1 (line)]] | alt | 99.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.430× (z -9.2) ⚠ toxic |
| [[HCT15 (line)]] | alt | 70.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[hTERT-HPNE (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 223 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 90.8 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.135× (z -12.3) |
| [[SW 1088 (line)]] | alt | 91.9 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.102× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.72 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 84.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 55.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1056), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST2]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CBL]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[NMB]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[KLC3]] | +0.55 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[FBXL2]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[PLIN3]] | +0.54 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[TMOD1]] | +0.54 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[EXOC6B]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[SH3PXD2B]] | +0.53 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[WDR44]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[F11R]] | +0.52 | +0.52 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCCC2]] | -0.56 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[UTP15]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TRUB1]] | -0.55 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[MRRF]] | -0.53 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[POMK]] | -0.53 | -0.49 / -0.49 | both halves | 2e-05 |  |
| [[PYM1]] | -0.53 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[CAVIN2]] | -0.52 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[COG4]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[DIS3L]] | -0.52 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[NELFCD]] | -0.51 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[GUF1]] | -0.51 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[SAFB]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DTNA]] | B | DTNA activity raises PPP2R3A's level | lines that do not express DTNA (22) vs lines expressing it (28) | 1.96× lower at baseline in the lines without DTNA | 0.041 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PPP2R3A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[AKT3]] | B | AKT3 activity raises PPP2R3A's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without AKT3 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[PLEKHO1]] | B | PLEKHO1 activity raises PPP2R3A's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 1.96× lower at baseline in the lines without PLEKHO1 | 0.075 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[GPR161]] | C | GPR161 activity raises PPP2R3A's level | lines that do not express GPR161 (6) vs lines expressing it (44) | 4.44× lower at baseline in the lines without GPR161 | 0.041 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PPP2R3A, NKAIN1; co-absent with the target |
| [[SPIRE1]] | C | SPIRE1 activity raises PPP2R3A's level | lines that do not express SPIRE1 (3) vs lines expressing it (47) | 3.65× lower at baseline in the lines without SPIRE1 | 0.069 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR161]] | C | PPP2R3A activity raises GPR161's level | lines that do not express PPP2R3A (4) vs lines expressing it (46) | 6.05× lower at baseline in the lines without PPP2R3A | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: CCDC102A, DMXL2, FSD1L; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.402). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-1.5, 3.7); signed map (-23.8, 19.9). **Vector** length 107, 30.5% of its response variance represented; |z| ≥ 3 in 1,291 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.7 | +4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +0.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.1 | +2.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +4.1 | +4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +2.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -10.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | -6.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.5 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.3 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -9.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -3.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.0 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 regulatory subunit B''alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.2-q22.3 — chr3:135,965,728-136,147,894 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PR130, PR72; previously PPP2R3 |
| Gene groups (HGNC) | Protein phosphatase 2 regulatory subunits; EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06190](https://www.uniprot.org/uniprotkb/Q06190) (Serine/threonine-protein phosphatase 2A regulatory subunit B'' subunit alpha):

> The B regulatory subunit might modulate substrate selectivity and catalytic activity, and might also direct the localization of the catalytic enzyme to a particular subcellular compartment.

**Summary**, from NCBI Gene [5523](https://www.ncbi.nlm.nih.gov/gene/5523):

> This gene encodes one of the regulatory subunits of the protein phosphatase 2. Protein phosphatase 2 (formerly named type 2A) is one of the four major Ser/Thr phosphatases and is implicated in the negative control of cell growth and division. Protein phosphatase 2 holoenzymes are heterotrimeric proteins composed of a structural subunit A, a catalytic subunit C, and a regulatory subunit B. The regulatory subunit is encoded by a diverse set of genes that have been grouped into the B/PR55, …

**Accessions** — [HGNC:9307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9307) · Entrez [5523](https://www.ncbi.nlm.nih.gov/gene/5523) · UniProt [Q06190](https://www.uniprot.org/uniprotkb/Q06190) · Ensembl [ENSG00000073711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073711)

## Data

Gene col 1056: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1056); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1056, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1056]; `tensor/DDL_lfc|DDL_z.npy` [1056]; `embed/gene_vectors.npy` [1056]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1056 or target_col == 1056). Every well: [[PPP2R3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2R3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
