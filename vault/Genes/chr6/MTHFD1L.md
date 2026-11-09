---
symbol: "MTHFD1L"
type: "gene"
col: 4170
ensembl_id: "ENSG00000120254"
name: "methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 1 like"
location: "6q25.1"
module: 5
arm: "+"
pooled_cpm: 230.5
n_lines_expressing: 47
n_dd_up: 17
n_dd_down: 27
n_dd_up_clean: 14
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 30
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MTHFD1L

*methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 1 like* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.83× (z +14.7, q 0e+00, up in 41 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 1.41× (z +8.3, q 2e-14, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.423× (z -29.7, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX21]] (+0.66, fdr 7e-06), [[RHBDD1]] (+0.66, fdr 7e-06), [[MOCOS]] (+0.64, fdr 7e-06); moves opposite to [[FAM8A1]] (-0.60, fdr 2e-05), [[BPNT1]] (-0.58, fdr 1e-05), [[DBP]] (-0.57, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BMF]] → it (grade C ⚠); 30 go from it, the strongest it → [[TTL]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4170.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.83×** | +14.7 | 0e+00 | 41/45 (HT-29, HEC-1-A, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.41×** | +8.3 | 2e-14 | 32/45 (SHP-77, Panc 03.27, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.33×** | +7.0 | 6e-10 | 34/45 (HEC-1-A, LoVo, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +6.4 | 3e-08 | 21/46 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +6.3 | 4e-08 | 27/45 (SHP-77, BT-474, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.29×** | +6.2 | 7e-08 | 27/45 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.62×** | +6.1 | 7e-08 | 29/45 (HEC-1-A, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +6.1 | 8e-08 | 21/45 (HEC-1-A, LoVo, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +5.7 | 7e-07 | 28/45 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.54×** | +5.5 | 2e-06 | 24/45 (HEC-1-A, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.53×** | +5.5 | 3e-06 | 25/45 (AsPC-1, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +5.4 | 3e-06 | 24/45 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.26×** | +5.4 | 3e-06 | 25/44 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +4.9 | 4e-05 | 21/45 (A-172, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.46×** | +4.8 | 6e-05 | 25/45 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.42×** | +4.5 | 3e-04 | 22/45 (AsPC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.13× | +4.2 | 7e-04 | 11/45 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Neratinib (drug)]] 0.5 µM |  | 1.19× | +4.2 | 9e-04 | 17/46 (HEC-1-A, RKO, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4170.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.423×** | -29.7 | 0e+00 | 42/45 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.317×** | -28.0 | 0e+00 | 44/45 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.344×** | -26.0 | 0e+00 | 43/45 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.360×** | -24.9 | 0e+00 | 42/45 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.595×** | -17.9 | 0e+00 | 42/45 (C32, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.509×** | -15.9 | 0e+00 | 35/45 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.575×** | -12.2 | 4e-32 | 40/45 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.598×** | -12.0 | 1e-31 | 30/42 (SW48, C32, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.611×** | -11.5 | 5e-29 | 36/44 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.634×** | -11.1 | 6e-27 | 39/45 (SW48, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[NG25 (drug)]] 5 µM |  | **0.421×** | -11.0 | 1e-26 | 42/44 (RKO, KATO III, …) | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.772×** | -8.9 | 2e-17 | 29/45 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.694×** | -8.9 | 2e-17 | 32/45 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.517×** | -8.4 | 2e-15 | 38/46 (PANC-1, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.697×** | -8.1 | 1e-14 | 27/43 (C32, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.719×** | -8.1 | 3e-14 | 33/45 (J82, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.719×** | -8.1 | 3e-14 | 33/45 (C32, SW48, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.770×** | -6.4 | 5e-09 | 28/46 (C32, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4170. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 406 | 0 | 20 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -53.2) |
| [[RKO (line)]] | wt | 373 | 0 | 19 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -41.0) |
| [[SW48 (line)]] | wt | 470 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -28.1) |
| [[C32 (line)]] | wt | 477 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -24.8) |
| [[NCI-H460 (line)]] | wt | 262 | 1 (1 ⚠) | 16 (5 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.89× (z +10.0) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -36.1) |
| [[MIA PaCa-2 (line)]] | alt | 236 | 3 (2 ⚠) | 12 (6 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.94× (z +11.9) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.84× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.203× (z -17.7) |
| [[A-172 (line)]] | wt | 194 | 3 (1 ⚠) | 10 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.49× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -14.8) |
| [[J82 (line)]] | alt | 246 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -28.3) |
| [[KATO III (line)]] | alt | 213 | 1 (1 ⚠) | 11 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.98× (z +8.5) ⚠ unreliable plate only | [[Digitoxin (drug)]] 5 µM 0.302× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.434× (z -14.7) |
| [[NCI-H2030 (line)]] | alt | 506 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -34.9) |
| [[A-427 (line)]] | wt | 216 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -20.6) |
| [[A549 (line)]] | wt | 328 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -35.2) |
| [[LoVo (line)]] | wt | 303 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -20.2) |
| [[SK-MEL-2 (line)]] | alt | 259 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -39.8) |
| [[LOX-IMVI (line)]] | wt | 272 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -32.6) |
| [[NCI-H23 (line)]] | alt | 677 | 1 (1 ⚠) | 9 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.99× (z +10.1) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -40.9) |
| [[SNU-1 (line)]] | wt | 502 | 2 (1 ⚠) | 8 (2 ⚠) | [[Trametinib (drug)]] 5 µM 2.39× (z +9.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 1.92× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.131× (z -22.4) |
| [[HEC-1-A (line)]] | alt | 211 | 1 (1 ⚠) | 8 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.17× (z +12.0) ⚠ unreliable plate only | [[Panobinostat (drug)]] 5 µM 0.328× (z -17.2) |
| [[LS 180 (line)]] | wt | 179 | 2 (2 ⚠) | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +11.3) ⚠ cell-cycle shift, explains ~5% of this change | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -11.5) |
| [[HOP62 (line)]] | alt | 163 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -16.1) |
| [[NCI-H1792 (line)]] | alt | 239 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -22.4) |
| [[SW1417 (line)]] | alt | 151 | 1 (1 ⚠) | 6 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.36× (z +10.7) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -19.7) |
| [[SW480 (line)]] | alt | 272 | 2 (2 ⚠) | 5 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.38× (z +10.9) ⚠ unreliable plate only | [[Panobinostat (drug)]] 5 µM 0.280× (z -16.0) |
| [[HS-578T (line)]] | alt | 141 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -19.6) |
| [[NCI-H1573 (line)]] | alt | 172 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -22.5) |
| [[CHP-212 (line)]] | wt | 263 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -12.2) |
| [[HT-29 (line)]] | alt | 165 | 1 (1 ⚠) | 4 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.63× (z +12.6) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -14.5) |
| [[SHP-77 (line)]] | alt | 150 | 1 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Belinostat (drug)]] 5 µM 0.287× (z -15.9) |
| [[A498 (line)]] | wt | 135 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -13.5) |
| [[C-33 A (line)]] | alt | 255 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.204× (z -15.8) |
| [[H4 (line)]] | wt | 196 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.266× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 293 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -16.0) |
| [[AN3 CA (line)]] | alt | 283 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 87.7 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.31× (z +11.0) ⚠ unreliable plate only | — |
| [[BT-474 (line)]] | alt | 61.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 149 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.1) |
| [[SNU-423 (line)]] | alt | 98.3 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.62× (z +9.3) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -8.7) |
| [[SW 1271 (line)]] | alt | 317 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.151× (z -11.4) ⚠ transcription drop; cell-cycle shift, explains ~54% of this change |
| [[HCT15 (line)]] | alt | 193 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.406× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 84.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.89× (z +9.9) ⚠ unreliable plate only | — |
| [[RPMI-7951 (line)]] | alt | 146 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.35× (z +8.8) ⚠ unreliable plate only | — |
| [[SW 900 (line)]] | alt | 81.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.75× (z +11.7) ⚠ unreliable plate only | — |
| [[CFPAC-1 (line)]] | alt | 45.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 57.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 55.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4170), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX21]] | +0.66 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[RHBDD1]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MOCOS]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 | pathway: Metabolism of vitamins and cofactors |
| [[PUS7]] | +0.64 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[HLCS]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 | pathway: Metabolism of vitamins and cofactors |
| [[PRMT3]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[LETM1]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[SLFNL1-AS1]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ENOX2]] | +0.60 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[PTPRG]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[SPOPL-DT]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ATR]] | +0.59 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM8A1]] | -0.60 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[BPNT1]] | -0.58 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[DBP]] | -0.57 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[RAB11A]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[MAGED2]] | -0.50 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[LRP1]] | -0.50 | -0.44 / -0.38 | both halves | 7e-05 | pathway: Metabolism of vitamins and cofactors |
| [[SECISBP2L]] | -0.49 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[MTMR11]] | -0.49 | -0.49 / -0.37 | both halves | 7e-05 |  |
| [[BAZ2A]] | -0.49 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[FAM229B]] | -0.48 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[BMF]] | -0.48 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[KLHL32]] | -0.48 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMF]] | C | BMF activity lowers MTHFD1L's level | lines that do not express BMF (4) vs lines expressing it (46) | 2.27× higher at baseline in the lines without BMF | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent; its own permutation p |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 0, C 30. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTL]] | C | MTHFD1L activity raises TTL's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 3.79× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ADCY3]] | C | MTHFD1L, [[USP31]] activity raises ADCY3's level | lines that do not express MTHFD1L, USP31 (3) vs lines expressing them (47) | 3.19× lower at baseline in the lines without MTHFD1L, USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p; co-absent genes |
| [[STXBP5]] | C | MTHFD1L activity raises STXBP5's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.88× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[MTMR11]] | C | MTHFD1L activity lowers MTMR11's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.76× higher at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[MDN1]] | C | MTHFD1L, [[USP31]] activity raises MDN1's level | lines that do not express MTHFD1L, USP31 (3) vs lines expressing them (47) | 2.58× lower at baseline in the lines without MTHFD1L, USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p; co-absent genes |
| [[PKP4]] | C | MTHFD1L activity raises PKP4's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.32× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[MACROD1]] | C | MTHFD1L activity raises MACROD1's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.22× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[XXYLT1]] | C | MTHFD1L activity raises XXYLT1's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.13× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[TULP4]] | C | MTHFD1L activity raises TULP4's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[AGAP6]] | C | MTHFD1L activity raises AGAP6's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[EHMT1]] | C | MTHFD1L activity raises EHMT1's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 1.87× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[TIMM23B-AGAP6]] | C | MTHFD1L activity raises TIMM23B-AGAP6's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 1.82× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.9, -33.1); signed map (2.5, -51.9). **Vector** length 147, 54.1% of its response variance represented; |z| ≥ 3 in 2,043 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +13.7 | +14.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +9.6 | +8.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +7.0 | +6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.8 | +6.3 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +6.5 | +7.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +6.3 | +6.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.3 | +5.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -11.0 | -17.9 |
|  | [[NG25 (drug)]] 5 µM |  | -8.2 | -11.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.2 | -8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -15.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.4 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -8.9 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -3.6 | -0.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.5 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.3 | -2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.3 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:150,865,679-151,101,887 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586G1517, FLJ21145; previously FTHFSDC1 |
| Gene groups (HGNC) | MTHFD family; Formyltetrahydrofolate synthetases |
| Reactome | 3 pathways, smallest: Metabolism of folate and pterines; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UB35](https://www.uniprot.org/uniprotkb/Q6UB35) (Monofunctional C1-tetrahydrofolate synthase, mitochondrial):

> May provide the missing metabolic reaction required to link the mitochondria and the cytoplasm in the mammalian model of one-carbon folate metabolism complementing thus the enzymatic activities of MTHFD2.

**Summary**, from NCBI Gene [25902](https://www.ncbi.nlm.nih.gov/gene/25902):

> The protein encoded by this gene is involved in the synthesis of tetrahydrofolate (THF) in the mitochondrion. THF is important in the de novo synthesis of purines and thymidylate and in the regeneration of methionine from homocysteine. Several transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:21055](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21055) · Entrez [25902](https://www.ncbi.nlm.nih.gov/gene/25902) · UniProt [Q6UB35](https://www.uniprot.org/uniprotkb/Q6UB35) · Ensembl [ENSG00000120254](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120254)

## Data

Gene col 4170: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4170); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4170, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4170]; `tensor/DDL_lfc|DDL_z.npy` [4170]; `embed/gene_vectors.npy` [4170]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4170 or target_col == 4170). Every well: [[MTHFD1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTHFD1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
