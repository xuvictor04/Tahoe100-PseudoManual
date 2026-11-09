---
symbol: "BLTP1"
type: "gene"
col: 6216
ensembl_id: "ENSG00000138688"
name: "bridge-like lipid transfer protein family member 1"
location: "4q27"
module: 57
arm: "+"
pooled_cpm: 189.74
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 33
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# BLTP1

*bridge-like lipid transfer protein family member 1* — 4q27

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.432× (z -20.8, q 0e+00, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.451× (z -19.7, q 0e+00, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS35]] (+0.69, fdr 7e-06), [[ABITRAM]] (+0.65, fdr 1e-05), [[TMEM183A]] (+0.64, fdr 7e-06); moves opposite to [[ERF]] (-0.56, fdr 1e-05), [[IER5]] (-0.54, fdr 1e-05), [[TLNRD1]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6216.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 1.53× | +3.5 | 0.27 | 31/49 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.48× | +3.2 | 0.30 | 34/50 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.20× | +3.2 | 0.30 | 22/48 (LS 180, RKO, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.19× | +3.0 | 0.32 | 18/48 (A498, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 24 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6216.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.432×** | -20.8 | 0e+00 | 41/48 (SNU-423, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.451×** | -19.7 | 0e+00 | 48/49 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.448×** | -14.1 | 1e-42 | 47/48 (SW48, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.483×** | -12.8 | 4e-35 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.492×** | -11.9 | 9e-31 | 41/48 (NCI-H1792, SNU-423, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.503×** | -11.6 | 5e-29 | 47/47 (Panc 03.27, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.537×** | -10.9 | 1e-25 | 44/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.602×** | -8.9 | 4e-17 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.616×** | -8.1 | 2e-14 | 40/48 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.617×** | -8.1 | 2e-14 | 44/50 (HS-578T, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.628×** | -7.8 | 2e-13 | 36/44 (SNU-1, A-427, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.644×** | -7.7 | 7e-13 | 43/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | **0.661×** | -7.2 | 2e-11 | 41/49 (SNU-1, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.640×** | -7.2 | 2e-11 | 37/45 (LoVo, NCI-H23, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.668×** | -7.1 | 6e-11 | 34/48 (hTERT-HPNE, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.822×** | -4.8 | 4e-05 | 24/48 (LOX-IMVI, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.781×** | -4.3 | 4e-04 | 34/48 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.723×** | -4.0 | 0.001 | 37/48 (SHP-77, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.852× | -4.0 | 0.002 | 20/48 (SNU-1, A-172, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.747×** | -3.6 | 0.006 | 37/48 (MIA PaCa-2, HEC-1-A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.753×** | -3.5 | 0.008 | 34/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.828×** | -3.3 | 0.018 | 23/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.770×** | -3.3 | 0.020 | 26/48 (CHP-212, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.894× | -2.8 | 0.091 | 2/49 (SW 900, SW 1088) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.802×** | -2.8 | 0.091 | 23/48 (A498, LoVo, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.803×** | -2.7 | 0.092 | 21/49 (A498, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.856× | -2.7 | 0.100 | 15/47 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 161 | 0 | 18 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -19.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -17.8) |
| [[HOP62 (line)]] | alt | 204 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -21.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -17.5) |
| [[hTERT-HPNE (line)]] | wt | 217 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -29.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -19.5) |
| [[LOX-IMVI (line)]] | wt | 147 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -20.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 263 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -21.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -18.5) |
| [[A-172 (line)]] | wt | 201 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -18.9) |
| [[HS-578T (line)]] | alt | 158 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -21.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -17.8) |
| [[SW 900 (line)]] | alt | 174 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -21.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -14.4) |
| [[A549 (line)]] | wt | 169 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -23.2) |
| [[C32 (line)]] | wt | 161 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -21.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -18.1) |
| [[NCI-H1792 (line)]] | alt | 254 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -26.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -20.1) |
| [[SK-MEL-2 (line)]] | alt | 176 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -23.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -13.9) |
| [[SNU-423 (line)]] | alt | 193 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -31.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -18.5) |
| [[SW480 (line)]] | alt | 120 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.270× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -14.5) |
| [[PANC-1 (line)]] | alt | 145 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -16.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 176 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -27.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -15.0) |
| [[SNU-1 (line)]] | wt | 223 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 175 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -18.4) |
| [[COLO 205 (line)]] | alt | 157 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -24.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 138 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -15.0) |
| [[LoVo (line)]] | wt | 214 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -22.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 187 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -14.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 249 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -18.4) |
| [[SW1417 (line)]] | alt | 153 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -14.2) |
| [[BT-474 (line)]] | alt | 129 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.367× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 222 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -19.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -15.6) |
| [[H4 (line)]] | wt | 221 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -11.5) |
| [[J82 (line)]] | alt | 120 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -22.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -14.4) |
| [[LS 180 (line)]] | wt | 214 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -18.0) |
| [[NCI-H2347 (line)]] | alt | 256 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -11.9) |
| [[A498 (line)]] | wt | 202 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -17.9) |
| [[HEC-1-A (line)]] | alt | 285 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -21.8) |
| [[HT-29 (line)]] | alt | 213 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.360× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 265 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.434× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.511× (z -9.1) |
| [[A-427 (line)]] | wt | 211 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[CHP-212 (line)]] | wt | 189 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.2) |
| [[Hs 766T (line)]] | wt | 197 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -13.5) |
| [[KATO III (line)]] | alt | 164 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -14.7) |
| [[SHP-77 (line)]] | alt | 173 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.488× (z -9.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HCT15 (line)]] | alt | 280 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.365× (z -10.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -10.3) |
| [[SW48 (line)]] | wt | 219 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -11.7) |
| [[AN3 CA (line)]] | alt | 226 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.382× (z -8.5) |
| [[C-33 A (line)]] | alt | 234 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.446× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[NCI-H2030 (line)]] | alt | 117 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.8) |
| [[RKO (line)]] | wt | 196 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -13.4) |
| [[SW 1088 (line)]] | alt | 269 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 1271 (line)]] | alt | 187 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -8.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2122 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 259 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS35]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[ABITRAM]] | +0.65 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TMEM183A]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CPNE3]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PWP1]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[LONP2]] | +0.62 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[RNF20]] | +0.60 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[PHKB]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[TRAPPC11]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[GPS1]] | +0.60 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[THYN1]] | +0.59 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[EIF2AK1]] | +0.59 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERF]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[IER5]] | -0.54 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[TLNRD1]] | -0.53 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[DGUOK-AS1]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[CEACAM16-AS1]] | -0.52 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ZNF672]] | -0.50 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[SUZ12P1]] | -0.50 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[ISG20]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SPRED3]] | -0.49 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[CCDC71L]] | -0.49 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.4, -17.1); signed map (-31.0, -23.8). **Vector** length 82.3, 32.1% of its response variance represented; |z| ≥ 3 in 1,426 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.9 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.9 | -3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +3.8 | -4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | +3.3 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.8 | -0.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.7 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.6 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -19.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.4 | -11.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.2 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -10.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | bridge-like lipid transfer protein family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q27 — chr4:122,152,331-122,364,167 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21404, FSA, KIAA1371, Tweek; previously KIAA1109 |
| Gene groups (HGNC) | Bridge-like lipid transfer protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2LD37](https://www.uniprot.org/uniprotkb/Q2LD37) (Bridge-like lipid transfer protein family member 1):

> Bridge-like lipid transfer protein that functions as molecular bridges between endoplasmic reticulum and the membranes targeted for lipid delivery. Forms a tunnel with multiple beta-grooves that allows the transport of phospholipids (By similarity). Provides phosphatidylethanolamine for glycosylphosphatidylinositol (GPI) anchor synthesis in the endoplasmic reticulum. Plays a role in endosomal trafficking and endosome recycling. Also involved in the actin cytoskeleton and cilia structural …

**Summary**, from NCBI Gene [84162](https://www.ncbi.nlm.nih.gov/gene/84162):

> This gene is located on the long arm of chromosome 4 in a region that is associated with susceptibility to celiac disease. The encoded protein is similar to a Chinese hamster protein that is associated with spermatocyte and adipocyte differentiation. The C-terminus of the protein is also similar to a Caenorhabditis elegans protein that plays a role in lipid storage. In mammals, this protein is thought to function in the regulation of epithelial growth and differentiation, and in tumor …

**Accessions** — [HGNC:26953](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26953) · Entrez [84162](https://www.ncbi.nlm.nih.gov/gene/84162) · UniProt [Q2LD37](https://www.uniprot.org/uniprotkb/Q2LD37) · Ensembl [ENSG00000138688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138688)

## Data

Gene col 6216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6216); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6216]; `tensor/DDL_lfc|DDL_z.npy` [6216]; `embed/gene_vectors.npy` [6216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6216 or target_col == 6216). Every well: [[BLTP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLTP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
