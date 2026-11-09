---
symbol: "ARFGEF1"
type: "gene"
col: 839
ensembl_id: "ENSG00000066777"
name: "ARF guanine nucleotide exchange factor 1"
location: "8q13.2"
module: 76
arm: "+"
pooled_cpm: 235.73
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 26
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# ARFGEF1

*ARF guanine nucleotide exchange factor 1* — 8q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 1.44× (z +4.2, q 0.018, up in 29 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.419× (z -22.6, q 0e+00, down in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.614× (z -17.5, q 0e+00, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (74 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3GLB1]] (+0.53, fdr 1e-05), [[AKAP9]] (+0.51, fdr 1e-04), [[GOLGB1]] (+0.50, fdr 2e-04); moves opposite to [[POLR3G]] (-0.46, fdr 1e-04), [[TNFAIP8]] (-0.45, fdr 5e-05), [[LIMD1]] (-0.44, fdr 3e-04).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 839.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.018 | 29/49 (A498, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 1.35× | +3.5 | 0.11 | 22/49 (HEC-1-A, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.14× | +3.4 | 0.11 | 11/48 (HS-578T, C32, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.34× | +3.3 | 0.11 | 22/50 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.14× | +3.3 | 0.11 | 7/47 (RPMI-7951, A-172, …) | rises with dose |  |
| [[Rifaximin (drug)]] 5 µM |  | 1.14× | +3.2 | 0.13 | 5/48 (J82, A-172, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.31× | +3.1 | 0.15 | 19/48 (BT-474, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 839.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.419×** | -22.6 | 0e+00 | 47/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.420×** | -22.5 | 0e+00 | 47/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.509×** | -17.6 | 0e+00 | 46/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.614×** | -17.5 | 0e+00 | 43/49 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.566×** | -14.8 | 0e+00 | 45/49 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.568×** | -14.2 | 2e-43 | 43/47 (CFPAC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.584×** | -13.4 | 3e-39 | 41/44 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.526×** | -10.7 | 1e-24 | 42/45 (A-427, NCI-H1792, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.680×** | -10.0 | 7e-22 | 38/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.688×** | -9.4 | 4e-19 | 38/50 (HS-578T, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.800×** | -7.9 | 1e-13 | 30/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.740×** | -7.8 | 2e-13 | 36/48 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.747×** | -7.3 | 1e-11 | 28/48 (HS-578T, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.785×** | -6.3 | 1e-08 | 34/48 (KATO III, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.792×** | -6.1 | 5e-08 | 28/48 (SNU-423, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.793×** | -6.0 | 6e-08 | 27/48 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -6.0 | 7e-08 | 23/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.794×** | -3.8 | 0.004 | 25/48 (HT-29, SNU-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.725×** | -3.7 | 0.005 | 24/49 (CFPAC-1, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.867× | -3.7 | 0.005 | 14/49 (SW 1088, SW480, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.864× | -3.7 | 0.005 | 20/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.915× | -3.2 | 0.026 | 1/48 (NCI-H2030) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.759×** | -3.2 | 0.029 | 19/48 (BT-474, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.827×** | -3.1 | 0.036 | 15/48 (HepG2/C3A, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.828×** | -3.1 | 0.036 | 20/47 (SK-MEL-2, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.765×** | -3.1 | 0.036 | 20/46 (C32, CHP-212, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 839. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 289 | 0 | 14 (11 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -22.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -14.8) |
| [[HS-578T (line)]] | alt | 385 | 0 | 13 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -22.6) |
| [[SNU-423 (line)]] | alt | 172 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -18.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 274 | 0 | 11 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -22.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -15.8) |
| [[SW480 (line)]] | alt | 203 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -24.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 363 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -23.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -17.9) |
| [[LOX-IMVI (line)]] | wt | 312 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 245 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -19.6) |
| [[SW 900 (line)]] | alt | 281 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.373× (z -15.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 294 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -15.6) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -9.6) |
| [[J82 (line)]] | alt | 190 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -18.1) |
| [[COLO 205 (line)]] | alt | 300 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -17.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -10.2) |
| [[KATO III (line)]] | alt | 260 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.341× (z -17.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -15.3) |
| [[Panc 03.27 (line)]] | alt | 275 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.292× (z -19.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -11.6) |
| [[A498 (line)]] | wt | 357 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.422× (z -16.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -11.4) |
| [[H4 (line)]] | wt | 264 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.485× (z -8.6) |
| [[HCT15 (line)]] | alt | 299 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -11.1) |
| [[HT-29 (line)]] | alt | 255 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -19.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 263 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -15.7) |
| [[NCI-H2347 (line)]] | alt | 287 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -19.5) |
| [[A-172 (line)]] | wt | 141 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -11.4) |
| [[A549 (line)]] | wt | 256 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.276× (z -20.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -17.6) |
| [[C-33 A (line)]] | alt | 181 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[LoVo (line)]] | wt | 231 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -17.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 134 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.303× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[RPMI-7951 (line)]] | alt | 269 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.606× (z -9.8) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 253 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.481× (z -13.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -13.5) |
| [[Hs 766T (line)]] | wt | 249 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -17.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 330 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.328× (z -17.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 233 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.615× (z -10.8) ⚠ cell-cycle shift, explains ~62% of this change |
| [[HepG2_C3A (line)]] | wt | 171 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.318× (z -15.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LS 180 (line)]] | wt | 236 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.487× (z -10.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 145 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.534× (z -11.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 162 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.458× (z -12.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 182 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.352× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW48 (line)]] | wt | 190 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[BT-474 (line)]] | alt | 229 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.531× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -12.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H661 (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 183 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.635× (z -9.1) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 281 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 194 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.529× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SW 1088 (line)]] | alt | 231 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.134× (z -11.1) |
| [[SW 1271 (line)]] | alt | 245 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.228× (z -10.5) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 194 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 216 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 198 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 839), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3GLB1]] | +0.53 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[AKAP9]] | +0.51 | +0.36 / +0.45 | both halves | 1e-04 |  |
| [[GOLGB1]] | +0.50 | +0.29 / +0.54 | both halves | 2e-04 |  |
| [[TNKS]] | +0.48 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[MBD5]] | +0.48 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[COA8]] | +0.47 | +0.36 / +0.45 | both halves | 9e-05 |  |
| [[ROCK1]] | +0.46 | +0.44 / +0.51 | both halves | 3e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[BBS9]] | +0.46 | +0.38 / +0.38 | both halves | 7e-05 |  |
| [[NIPBL]] | +0.45 | +0.23 / +0.50 | both halves | 5e-04 | same gene group; STRING 539 |
| [[RAB3GAP2]] | +0.45 | +0.38 / +0.42 | both halves | 7e-05 |  |
| [[ARF5]] | +0.44 | +0.45 / +0.37 | both halves | 8e-05 | STRING 487 |
| [[CCNDBP1]] | +0.44 | +0.59 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3G]] | -0.46 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[TNFAIP8]] | -0.45 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[LIMD1]] | -0.44 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[PLEKHH1]] | -0.43 | -0.24 / -0.39 | both halves | 5e-04 |  |
| [[EXTL3]] | -0.43 | -0.16 / -0.51 | ⚠ one half (not replicated) | 0.001 |  |
| [[SHB]] | -0.43 | -0.24 / -0.36 | both halves | 5e-04 |  |
| [[CTSC]] | -0.43 | -0.46 / -0.47 | both halves | 2e-05 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[STAMBPL1]] | -0.43 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[ARSJ]] | -0.42 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[FAM86DP]] | -0.42 | -0.24 / -0.41 | both halves | 4e-04 |  |
| [[CHSY1]] | -0.42 | -0.19 / -0.41 | ⚠ not reproduced | 8e-04 |  |
| [[MIR155HG]] | -0.42 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[FAM86DP-1]] | -0.41 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[CPNE5]] | -0.41 | -0.27 / -0.42 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARFGEF1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MIR155HG]] | B | MIR155HG activity raises ARFGEF1's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 1.25× lower at baseline in the lines without MIR155HG | 0.036 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.277). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.7, -48.3); signed map (-10.6, -4.5). **Vector** length 70.6, 22.3% of its response variance represented; |z| ≥ 3 in 1,212 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | +4.7 | -13.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +4.6 | -14.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +2.7 | -10.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +0.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | -0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | +4.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | +0.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.3 | -14.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | +0.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ARF guanine nucleotide exchange factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.2 — chr8:67,173,511-67,343,781 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434L057, BIG1, ARFGEP1, p200 |
| Gene groups (HGNC) | Armadillo like helical domain containing; ArfGEF family |
| Hallmark sets | PROTEIN_SECRETION, MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6D6](https://www.uniprot.org/uniprotkb/Q9Y6D6) (Brefeldin A-inhibited guanine nucleotide-exchange protein 1):

> Promotes guanine-nucleotide exchange on ARF1 and ARF3. Promotes the activation of ARF1/ARF3 through replacement of GDP with GTP. Involved in vesicular trafficking. Required for the maintenance of Golgi structure; the function may be independent of its GEF activity. Required for the maturation of integrin beta-1 in the Golgi. Involved in the establishment and persistence of cell polarity during directed cell movement in wound healing. Proposed to act as A kinase-anchoring protein (AKAP) and may …

**Summary**, from NCBI Gene [10565](https://www.ncbi.nlm.nih.gov/gene/10565):

> ADP-ribosylation factors (ARFs) play an important role in intracellular vesicular trafficking. The protein encoded by this gene is involved in the activation of ARFs by accelerating replacement of bound GDP with GTP. It contains a Sec7 domain, which may be responsible for guanine-nucleotide exchange activity and also brefeldin A inhibition. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:15772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15772) · Entrez [10565](https://www.ncbi.nlm.nih.gov/gene/10565) · UniProt [Q9Y6D6](https://www.uniprot.org/uniprotkb/Q9Y6D6) · Ensembl [ENSG00000066777](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066777)

## Data

Gene col 839: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 839); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 839, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 839]; `tensor/DDL_lfc|DDL_z.npy` [839]; `embed/gene_vectors.npy` [839]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 839 or target_col == 839). Every well: [[ARFGEF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARFGEF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
