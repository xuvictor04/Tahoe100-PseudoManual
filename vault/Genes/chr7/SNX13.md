---
symbol: "SNX13"
type: "gene"
col: 978
ensembl_id: "ENSG00000071189"
name: "sorting nexin 13"
location: "7p21.1"
module: 72
arm: "+"
pooled_cpm: 168.49
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# SNX13

*sorting nexin 13* — 7p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.87× (z +11.5, q 1e-27, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.391× (z -16.5, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.650× (z -7.9, q 5e-13, down in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (SW48 0.133×, NCI-H23 0.245×, A-427 0.266×, KATO III 0.247×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 5 lines (SW480 0.431×, MIA PaCa-2 0.385×, SK-MEL-2 0.412×, A-172 0.467×, …); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-1 0.155×, H4 0.186×, NCI-H1573 0.249×, LoVo 0.355×; ⚠ toxic; transcription drop); [[Monocrotaline (drug)]] 0.05 µM in 1 line (SW 1271 0.240×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFB5]] (+0.63, fdr 9e-05), [[QRSL1]] (+0.61, fdr 3e-05), [[UBE4B]] (+0.60, fdr 7e-06); moves opposite to [[SEMA7A]] (-0.65, fdr 1e-05), [[EHD1]] (-0.60, fdr 1e-05), [[CSRP1]] (-0.58, fdr 6e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 978.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.87×** | +11.5 | 1e-27 | 46/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +8.6 | 3e-15 | 47/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.60×** | +8.4 | 8e-15 | 42/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +8.1 | 1e-13 | 44/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +6.9 | 4e-10 | 38/48 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +6.5 | 5e-09 | 41/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.05×** | +6.3 | 2e-08 | 39/48 (SW480, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +6.3 | 2e-08 | 38/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +6.1 | 9e-08 | 31/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.5 | 4e-04 | 24/48 (RKO, AsPC-1, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +4.2 | 0.002 | 28/47 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.14× | +3.4 | 0.032 | 4/48 (BT-474, J82, …) | rises with dose | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.049 | 20/48 (RKO, COLO 205, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.066 | 21/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.19× | +3.1 | 0.067 | 16/48 (J82, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 978.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (SW48 0.133×, NCI-H23 0.245×, A-427 0.266×, KATO III 0.247×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 5 lines (SW480 0.431×, MIA PaCa-2 0.385×, SK-MEL-2 0.412×, A-172 0.467×, …); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-1 0.155×, H4 0.186×, NCI-H1573 0.249×, LoVo 0.355×; ⚠ toxic; transcription drop); [[Monocrotaline (drug)]] 0.05 µM in 1 line (SW 1271 0.240×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.391×** | -16.5 | 0e+00 | 41/44 (SW48, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.421×** | -15.8 | 0e+00 | 49/49 (SNU-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.424×** | -14.5 | 1e-45 | 44/45 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -7.9 | 5e-13 | 41/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.655×** | -7.4 | 1e-11 | 40/47 (RKO, SW1417, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.679×** | -7.1 | 2e-10 | 40/48 (SW1417, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.709×** | -6.3 | 2e-08 | 36/48 (SW1417, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.719×** | -6.0 | 1e-07 | 37/48 (AN3 CA, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.751×** | -5.2 | 1e-05 | 37/48 (NCI-H2347, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -5.0 | 3e-05 | 25/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.870× | -3.6 | 0.018 | 15/48 (HOP62, BT-474, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.831×** | -3.4 | 0.035 | 22/48 (Panc 03.27, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.843× | -3.1 | 0.078 | 23/48 (BT-474, NCI-H2030, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.848× | -3.0 | 0.11 | 19/47 (NCI-H1792, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 195 | 7 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +15.7) | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -14.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 154 | 3 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.04× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -16.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 224 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -14.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 173 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.72× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.385× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 124 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -14.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 185 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.97× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.431× (z -11.7) |
| [[H4 (line)]] | wt | 355 | 2 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.33× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -17.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 166 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.467× (z -9.7) |
| [[C32 (line)]] | wt | 205 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 192 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -14.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 172 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 181 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.60× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -14.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 173 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +10.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.350× (z -12.7) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 215 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -12.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 221 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -14.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 197 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.392× (z -12.1) ⚠ toxic |
| [[A498 (line)]] | wt | 211 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -13.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 125 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.375× (z -11.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 201 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -10.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 180 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 148 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -13.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 156 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -10.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 143 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -10.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 279 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -15.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 149 | 1 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.50× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.468× (z -9.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 186 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 159 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -17.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 218 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -14.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 160 | 1 | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.19× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.412× (z -10.4) |
| [[SNU-423 (line)]] | alt | 164 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -13.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 222 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -12.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 123 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.478× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 147 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -13.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 163 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -18.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 216 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Monocrotaline (drug)]] 0.05 µM 0.240× (z -8.6) |
| [[SW48 (line)]] | wt | 190 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -19.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[BT-474 (line)]] | alt | 174 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.101× (z -13.9) ⚠ toxic |
| [[J82 (line)]] | alt | 98.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.450× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -9.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 125 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 242 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFB5]] | +0.63 | +0.36 / +0.67 | both halves | 9e-05 |  |
| [[QRSL1]] | +0.61 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[UBE4B]] | +0.60 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[MAP2K5]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[INTU]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[TNKS]] | +0.59 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[TENT2]] | +0.59 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[UBR3]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[MRPL37]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[MRPS15]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ZNF148]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CEP126]] | +0.56 | +0.48 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA7A]] | -0.65 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[EHD1]] | -0.60 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[CSRP1]] | -0.58 | -0.62 / -0.38 | both halves | 6e-05 |  |
| [[MAP2K3]] | -0.57 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[COTL1]] | -0.56 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[DUSP7]] | -0.55 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[CSRNP1]] | -0.54 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[PLEC]] | -0.52 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[SOWAHC]] | -0.52 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[R3HDM4]] | -0.52 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[FOSL1]] | -0.52 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ACTN1]] | -0.52 | -0.44 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers SNX13's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SNX13's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SNX13's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | SNX13's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | SNX13's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.58 | 0.491 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.375). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.3, 17.2); signed map (-20.8, -23.0). **Vector** length 92.3, 34.2% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.7 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.1 | +6.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +0.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.2 | -7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -5.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.3 | -1.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.9 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.1 — chr7:17,790,761-17,940,501 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RGS-PX1, KIAA0713 |
| Gene groups (HGNC) | Sorting nexins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5W8](https://www.uniprot.org/uniprotkb/Q9Y5W8) (Sorting nexin-13):

> May be involved in several stages of intracellular trafficking. May play a role in endosome homeostasis (By similarity). Acts as a GAP for Galphas.

**Summary**, from NCBI Gene [23161](https://www.ncbi.nlm.nih.gov/gene/23161):

> This gene encodes a PHOX domain- and RGS domain-containing protein that belongs to the sorting nexin (SNX) family and the regulator of G protein signaling (RGS) family. The PHOX domain is a phosphoinositide binding domain, and the SNX family members are involved in intracellular trafficking. The RGS family members are regulatory molecules that act as GTPase activating proteins for G alpha subunits of heterotrimeric G proteins. The RGS domain of this protein interacts with G alpha(s), …

**Accessions** — [HGNC:21335](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21335) · Entrez [23161](https://www.ncbi.nlm.nih.gov/gene/23161) · UniProt [Q9Y5W8](https://www.uniprot.org/uniprotkb/Q9Y5W8) · Ensembl [ENSG00000071189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071189)

## Data

Gene col 978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 978); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 978]; `tensor/DDL_lfc|DDL_z.npy` [978]; `embed/gene_vectors.npy` [978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 978 or target_col == 978). Every well: [[SNX13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
