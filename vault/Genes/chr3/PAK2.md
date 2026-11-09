---
symbol: "PAK2"
type: "gene"
col: 11103
ensembl_id: "ENSG00000180370"
name: "p21 (RAC1) activated kinase 2"
location: "3q29"
module: 54
arm: "-"
pooled_cpm: 199.56
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# PAK2

*p21 (RAC1) activated kinase 2* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.00× (z +20.6, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.26× (z +6.9, q 6e-10, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.597× (z -15.2, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GSPT1]] (+0.66, fdr 9e-06), [[FLII]] (+0.61, fdr 3e-05), [[SBDS]] (+0.60, fdr 2e-05); moves opposite to [[PELO]] (-0.57, fdr 6e-05), [[OSBPL7]] (-0.56, fdr 2e-05), [[RNF114]] (-0.56, fdr 6e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +20.6 | 0e+00 | 47/49 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +17.5 | 0e+00 | 39/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +13.7 | 3e-40 | 40/45 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +9.5 | 5e-19 | 38/48 (COLO 205, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +7.4 | 2e-11 | 31/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +6.9 | 6e-10 | 31/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +6.6 | 3e-09 | 27/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.23×** | +6.3 | 3e-08 | 25/47 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +6.1 | 7e-08 | 17/49 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.23×** | +6.1 | 7e-08 | 23/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.22×** | +6.0 | 1e-07 | 25/48 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +5.8 | 3e-07 | 24/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.21×** | +5.5 | 2e-06 | 27/47 (HT-29, COLO 205, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.17× | +4.6 | 2e-04 | 19/47 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.16× | +4.4 | 3e-04 | 15/48 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.10× | +3.0 | 0.085 | 7/48 (A498, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11103.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.597×** | -15.2 | 0e+00 | 45/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.606×** | -14.8 | 0e+00 | 46/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.636×** | -13.4 | 1e-38 | 45/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.739×** | -8.9 | 7e-17 | 41/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.789×** | -7.0 | 3e-10 | 29/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.801×** | -6.5 | 6e-09 | 31/49 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.864× | -6.1 | 9e-08 | 13/48 (SW480, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.899× | -4.4 | 6e-04 | 16/48 (A-427, LOX-IMVI, …) | top dose only | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.956× | -4.4 | 6e-04 | 0/50 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.752×** | -4.4 | 6e-04 | 22/49 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.867× | -4.2 | 0.002 | 14/48 (BT-474, A-427, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.769×** | -4.0 | 0.002 | 24/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tadalafil (drug)]] 5 µM |  | 0.871× | -3.9 | 0.004 | 6/48 (NCI-H1573, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.874× | -3.8 | 0.006 | 8/48 (LS 180, J82, …) | rises with dose |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 0.881× | -3.7 | 0.008 | 14/48 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.844× | -3.6 | 0.013 | 22/48 (KATO III, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.885× | -3.4 | 0.018 | 16/47 (NCI-H23, AsPC-1, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.889× | -3.4 | 0.018 | 11/47 (NCI-H23, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Baicalin (drug)]] 5 µM |  | 0.920× | -3.4 | 0.018 | 1/49 (CHP-212) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 264 | 5 (5 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +18.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.440× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 382 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +13.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.392× (z -15.5) |
| [[PANC-1 (line)]] | alt | 306 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +20.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.516× (z -15.3) |
| [[A-427 (line)]] | wt | 221 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -22.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.559× (z -10.1) |
| [[A549 (line)]] | wt | 123 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +15.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.427× (z -12.8) |
| [[HOP62 (line)]] | alt | 227 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +13.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.497× (z -11.9) |
| [[KATO III (line)]] | alt | 200 | 3 (3 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +12.0) ⚠ cell-cycle shift, explains ~22% of this change | [[Panobinostat (drug)]] 0.5 µM 0.499× (z -12.5) |
| [[LoVo (line)]] | wt | 141 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +11.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.580× (z -9.0) |
| [[COLO 205 (line)]] | alt | 212 | 4 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +13.3) ⚠ cell-cycle shift, explains ~22% of this change | [[Panobinostat (drug)]] 0.5 µM 0.460× (z -10.7) |
| [[HS-578T (line)]] | alt | 225 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +14.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.536× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 212 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.08× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.392× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 150 | 3 (3 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +11.6) ⚠ cell-cycle shift, explains ~22% of this change | [[Panobinostat (drug)]] 0.5 µM 0.540× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 210 | 1 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +10.2) ⚠ cell-cycle shift, explains ~22% of this change | [[Panobinostat (drug)]] 0.5 µM 0.470× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 254 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +8.5) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.409× (z -12.7) |
| [[LS 180 (line)]] | wt | 178 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.522× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 223 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +13.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.591× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 249 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +12.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.588× (z -9.5) |
| [[RKO (line)]] | wt | 244 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.486× (z -11.2) |
| [[SNU-1 (line)]] | wt | 263 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.379× (z -10.6) |
| [[A498 (line)]] | wt | 158 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +16.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 153 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +12.7) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 146 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +11.3) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 243 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +13.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.636× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 123 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +15.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 166 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +15.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 171 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +15.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 218 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +11.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.613× (z -8.9) |
| [[A-172 (line)]] | wt | 223 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +10.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 116 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +11.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 122 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 223 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +10.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 150 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 145 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +14.5) ⚠ toxic; transcription drop | [[TAK-901 (drug)]] 5 µM 0.348× (z -9.1) |
| [[BT-474 (line)]] | alt | 192 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.559× (z -9.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[C32 (line)]] | wt | 142 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.94× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 192 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +15.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 169 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 76.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 269 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.589× (z -8.7) |
| [[SW 900 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 133 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +12.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 232 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 171 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 228 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSPT1]] | +0.66 | +0.57 / +0.67 | both halves | 9e-06 | pathway: Signaling by ROBO receptors |
| [[FLII]] | +0.61 | +0.43 / +0.70 | both halves | 3e-05 |  |
| [[SBDS]] | +0.60 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[ZMYND11]] | +0.60 | +0.37 / +0.65 | both halves | 7e-05 |  |
| [[NPIPB5]] | +0.60 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[REEP3]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ZC3H14]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ADSS2]] | +0.57 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[USP45]] | +0.57 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[SLC39A10]] | +0.56 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[WWC3]] | +0.56 | +0.36 / +0.56 | both halves | 9e-05 |  |
| [[VPS4A]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 | pathway: HIV Infection |

## Genes that move opposite

*43 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PELO]] | -0.57 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[OSBPL7]] | -0.56 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[RNF114]] | -0.56 | -0.39 / -0.62 | both halves | 6e-05 |  |
| [[DBP]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SCRN2]] | -0.54 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[DTX2]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[NECAP1]] | -0.52 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[FAM104A]] | -0.52 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[FBXO46]] | -0.52 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ARL4D]] | -0.51 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[MRPL14]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[LINC01273]] | -0.51 | -0.38 / -0.57 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PAK2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PAK2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GNE]] | C | GNE activity raises PAK2's level | lines that do not express GNE (3) vs lines expressing it (47) | 1.41× lower at baseline in the lines without GNE | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF222, ATL3; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.442). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.1, -18.5); signed map (9.4, -8.8). **Vector** length 109, 33.3% of its response variance represented; |z| ≥ 3 in 1,304 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +20.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.9 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +6.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.6 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +6.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.8 | +5.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.9 | -4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.0 | -3.6 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | -4.2 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.1 | -6.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.5 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -0.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.1 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | p21 (RAC1) activated kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,739,857-196,832,647 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAK65, PAKgamma |
| Gene groups (HGNC) | p21 (RAC1) activated kinase family |
| Reactome | 57 pathways, smallest: Nef and signal transduction; CD28 dependent Vav1 pathway; Activation of RAC1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13177](https://www.uniprot.org/uniprotkb/Q13177) (Serine/threonine-protein kinase PAK 2):

> Serine/threonine protein kinase that plays a role in a variety of different signaling pathways including cytoskeleton regulation, cell motility, cell cycle progression, apoptosis or proliferation. Acts as a downstream effector of the small GTPases CDC42 and RAC1. Activation by the binding of active CDC42 and RAC1 results in a conformational change and a subsequent autophosphorylation on several serine and/or threonine residues. Full-length PAK2 stimulates cell survival and cell growth. …

**Summary**, from NCBI Gene [5062](https://www.ncbi.nlm.nih.gov/gene/5062):

> The p21 activated kinases (PAK) are critical effectors that link Rho GTPases to cytoskeleton reorganization and nuclear signaling. The PAK proteins are a family of serine/threonine kinases that serve as targets for the small GTP binding proteins, CDC42 and RAC1, and have been implicated in a wide range of biological activities. The protein encoded by this gene is activated by proteolytic cleavage during caspase-mediated apoptosis, and may play a role in regulating the apoptotic events in the …

**Accessions** — [HGNC:8591](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8591) · Entrez [5062](https://www.ncbi.nlm.nih.gov/gene/5062) · UniProt [Q13177](https://www.uniprot.org/uniprotkb/Q13177) · Ensembl [ENSG00000180370](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180370)

## Data

Gene col 11103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11103); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11103]; `tensor/DDL_lfc|DDL_z.npy` [11103]; `embed/gene_vectors.npy` [11103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11103 or target_col == 11103). Every well: [[PAK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
