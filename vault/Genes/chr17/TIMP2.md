---
symbol: "TIMP2"
type: "gene"
col: 433
ensembl_id: "ENSG00000035862"
name: "TIMP metallopeptidase inhibitor 2"
location: "17q25.3"
module: 50
arm: "+"
pooled_cpm: 171.82
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# TIMP2

*TIMP metallopeptidase inhibitor 2* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.60× (z +16.0, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.479× (z -24.8, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP295NL]] (+0.71, fdr 7e-06, ⚠ read-through risk), [[GM2A]] (+0.63, fdr 1e-05), [[CYB5R3]] (+0.61, fdr 1e-05), [[ITM2C]] (+0.61, fdr 7e-06); moves opposite to [[AFG1L]] (-0.60, fdr 1e-05), [[TRIP11]] (-0.59, fdr 1e-05), [[MCPH1]] (-0.58, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[COL18A1]] → it (grade B ⚠); 5 go from it, the strongest it → [[CASTOR2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 433.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +16.0 | 0e+00 | 40/44 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +14.4 | 2e-44 | 36/45 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +14.3 | 5e-44 | 33/39 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +9.9 | 8e-21 | 39/45 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +8.8 | 1e-16 | 29/44 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +8.4 | 5e-15 | 32/42 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +6.1 | 7e-08 | 22/44 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +5.7 | 1e-06 | 17/44 (LOX-IMVI, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.18× | +5.6 | 2e-06 | 19/44 (SW 900, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.24×** | +5.2 | 1e-05 | 23/44 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.24×** | +5.2 | 1e-05 | 23/44 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +4.6 | 2e-04 | 24/45 (LOX-IMVI, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.30×** | +4.5 | 3e-04 | 25/44 (SHP-77, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.20×** | +4.4 | 5e-04 | 22/44 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | 1.16× | +3.4 | 0.028 | 17/43 (BT-474, HT-29, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.066 | 7/44 (KATO III, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 433.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.479×** | -24.8 | 0e+00 | 42/44 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.364×** | -24.0 | 0e+00 | 44/44 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.398×** | -21.1 | 0e+00 | 41/44 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.532×** | -15.0 | 0e+00 | 43/44 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.624×** | -11.2 | 3e-27 | 41/44 (MIA PaCa-2, A549, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.650×** | -10.3 | 1e-22 | 30/44 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.745×** | -7.0 | 2e-10 | 28/44 (BT-474, LoVo, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.745×** | -7.0 | 2e-10 | 28/43 (NCI-H2030, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.738×** | -7.0 | 2e-10 | 35/45 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.578×** | -6.8 | 5e-10 | 34/44 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.755×** | -6.7 | 1e-09 | 27/44 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.758×** | -6.6 | 2e-09 | 28/44 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -6.6 | 2e-09 | 28/44 (SW 900, SK-MEL-2, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.611×** | -6.1 | 3e-08 | 30/44 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.776×** | -6.0 | 7e-08 | 27/44 (A549, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.698×** | -4.5 | 3e-04 | 19/44 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.705×** | -4.4 | 4e-04 | 24/44 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.824×** | -4.3 | 4e-04 | 22/44 (SNU-423, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 433. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 177 | 2 | 10 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.94× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -30.6) |
| [[PANC-1 (line)]] | alt | 49.3 | 8 (2 ⚠) | 4 | [[Panobinostat (drug)]] 0.05 µM 3.55× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -15.1) |
| [[BT-474 (line)]] | alt | 87.0 | 3 (1 ⚠) | 6 (3 ⚠) | [[Peretinoin (drug)]] 5 µM 4.09× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -15.8) |
| [[HOP62 (line)]] | alt | 280 | 6 (3 ⚠) | 2 | [[Tucidinostat (drug)]] 5 µM 2.07× (z +15.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.356× (z -15.0) |
| [[MIA PaCa-2 (line)]] | alt | 285 | 2 (1 ⚠) | 6 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.92× (z +12.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -21.5) |
| [[NCI-H460 (line)]] | wt | 65.9 | 1 | 6 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.49× (z +15.0) | [[Harringtonine (drug)]] 0.5 µM 0.320× (z -13.2) |
| [[A-427 (line)]] | wt | 113 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -26.0) |
| [[HEC-1-A (line)]] | alt | 198 | 2 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 1.94× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.56× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -24.2) |
| [[KATO III (line)]] | alt | 75.0 | 4 (1 ⚠) | 2 | [[Tucidinostat (drug)]] 5 µM 2.47× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 81.6 | 6 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.76× (z +13.7) | — |
| [[SK-MEL-2 (line)]] | alt | 268 | 2 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.69× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -16.9) |
| [[SNU-1 (line)]] | wt | 55.1 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.05 µM 0.224× (z -10.4) |
| [[SNU-423 (line)]] | alt | 388 | 2 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.84× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.51× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -24.3) |
| [[SW480 (line)]] | alt | 202 | 1 | 5 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.90× (z +12.1) | [[Harringtonine (drug)]] 5 µM 0.285× (z -16.0) |
| [[A498 (line)]] | wt | 272 | 4 (3 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.61× (z +9.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.561× (z -8.5) |
| [[LoVo (line)]] | wt | 67.3 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.228× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 106 | 2 | 3 | [[Panobinostat (drug)]] 5 µM 2.22× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -13.9) |
| [[A-172 (line)]] | wt | 558 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 273 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -25.1) |
| [[C32 (line)]] | wt | 254 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -11.7) |
| [[H4 (line)]] | wt | 133 | 2 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.91× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -15.4) |
| [[HCT15 (line)]] | alt | 121 | 4 | 0 | [[Belinostat (drug)]] 5 µM 4.25× (z +12.2) | — |
| [[Hs 766T (line)]] | wt | 94.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 263 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -15.0) |
| [[SW 900 (line)]] | alt | 107 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.264× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 223 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -15.7) |
| [[CHP-212 (line)]] | wt | 360 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -19.1) |
| [[NCI-H2347 (line)]] | alt | 229 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -23.3) |
| [[SHP-77 (line)]] | alt | 73.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -8.8) |
| [[SW1417 (line)]] | alt | 309 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 1.64× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -13.8) |
| [[AN3 CA (line)]] | alt | 164 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 197 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.43× (z +10.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -9.0) |
| [[HS-578T (line)]] | alt | 143 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 123 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.07× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 532 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.437× (z -9.8) |
| [[J82 (line)]] | alt | 242 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.84× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 139 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 49.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.196× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 209 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -10.7) |
| [[SW48 (line)]] | wt | 71.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -9.7) |
| [[C-33 A (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 34.8 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 40.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 191 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 433), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP295NL]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 | ⚠ **readthrough risk**: CEP295NL lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[GM2A]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[CYB5R3]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ITM2C]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[IGSF3]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[F11R]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[TNK2]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[LPCAT2]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[PSAP]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CLSTN1]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[VAT1]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[CTSB]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT; STRING 477 |
| [[PDZD7]] | +0.57 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AFG1L]] | -0.60 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.59 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[MCPH1]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[ERCC4]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[RPP38]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[NME6]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ARL14EP]] | -0.57 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[RPAP2]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TP53RK]] | -0.56 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[CCDC137]] | -0.56 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[C1orf131]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[BRIX1]] | -0.55 | -0.51 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL18A1]] | B | COL18A1 activity raises TIMP2's level | lines that do not express COL18A1 (18) vs lines expressing it (32) | 2.61× lower at baseline in the lines without COL18A1 | 0.008 | ⚠ within organs, on part of the lines; also absent: NGFR, CX3CL1, PPP2R2B |
| [[MMP2]] | B | MMP2 activity weakens TIMP2's drug response | lines that do not express MMP2 (30) vs lines expressing it (15) | the lines without MMP2 respond 1.03× as strongly (z diff -0.20); strongest at Harringtonine 5 µM: 0.35x vs 0.54x (z diff -2.3) | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; target measured in part of the lines; both ways; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TIMP2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TIMP2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[VSIR]] | B | VSIR activity raises TIMP2's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without VSIR | 0.086 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASTOR2]] | C | TIMP2 activity raises CASTOR2's level | lines that do not express TIMP2 (4) vs lines expressing it (46) | 1.86× lower at baseline in the lines without TIMP2 | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CNTNAP1, P3H1, RDX; maybe low, not absent |
| [[BCAM]] | C | TIMP2 activity raises BCAM's level | lines that do not express TIMP2 (4) vs lines expressing it (46) | 2.04× lower at baseline in the lines without TIMP2 | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CNTNAP1, P3H1, RDX; maybe low, not absent |
| [[CEP295NL]] | C | TIMP2 activity raises CEP295NL's level | lines that do not express TIMP2 (4) vs lines expressing it (46) | 1.96× lower at baseline in the lines without TIMP2 | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CNTNAP1, P3H1, RDX; maybe low, not absent |
| [[MFGE8]] | C | TIMP2 activity raises MFGE8's level | lines that do not express TIMP2 (4) vs lines expressing it (46) | 3.28× lower at baseline in the lines without TIMP2 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CNTNAP1, P3H1, RDX; maybe low, not absent |
| [[PDZD7]] | C | TIMP2 activity raises PDZD7's level | lines that do not express TIMP2 (4) vs lines expressing it (46) | 1.72× lower at baseline in the lines without TIMP2 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CNTNAP1, P3H1, RDX; maybe low, not absent |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, 0.4); signed map (-13.4, 36.6). **Vector** length 134, 42.6% of its response variance represented; |z| ≥ 3 in 1,434 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.2 | +16.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.6 | +9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.6 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +14.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.9 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.3 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.9 | -24.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.7 | -15.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.7 | -21.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.2 | -10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.2 | -24.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.1 | -6.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.0 | -6.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.6 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.3 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | TIMP metallopeptidase inhibitor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:78,852,977-78,925,387 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSC-21K |
| Gene groups (HGNC) | Tissue inhibitor of metallopeptidases |
| Hallmark sets | APOPTOSIS, COMPLEMENT |
| Reactome | 8 pathways, smallest: TGFBR3 PTM regulation; Activation of Matrix Metalloproteinases; Signaling by TGFBR3 |
| Matched by | ensembl_id |

**Function**, from UniProt [P16035](https://www.uniprot.org/uniprotkb/P16035) (Metalloproteinase inhibitor 2):

> Complexes with metalloproteinases (such as collagenases) and irreversibly inactivates them by binding to their catalytic zinc cofactor. Known to act on MMP-1, MMP-2, MMP-3, MMP-7, MMP-8, MMP-9, MMP-10, MMP-13, MMP-14, MMP-15, MMP-16 and MMP-19.

**Summary**, from NCBI Gene [7077](https://www.ncbi.nlm.nih.gov/gene/7077):

> This gene is a member of the TIMP gene family. The proteins encoded by this gene family are natural inhibitors of the matrix metalloproteinases, a group of peptidases involved in degradation of the extracellular matrix. In addition to an inhibitory role against metalloproteinases, the encoded protein has a unique role among TIMP family members in its ability to directly suppress the proliferation of endothelial cells. As a result, the encoded protein may be critical to the maintenance of tissue …

**Accessions** — [HGNC:11821](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11821) · Entrez [7077](https://www.ncbi.nlm.nih.gov/gene/7077) · UniProt [P16035](https://www.uniprot.org/uniprotkb/P16035) · Ensembl [ENSG00000035862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000035862)

## Data

Gene col 433: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 433); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 433, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 433]; `tensor/DDL_lfc|DDL_z.npy` [433]; `embed/gene_vectors.npy` [433]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 433 or target_col == 433). Every well: [[TIMP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
