---
symbol: "CHD7"
type: "gene"
col: 10092
ensembl_id: "ENSG00000171316"
name: "chromodomain helicase DNA binding protein 7"
location: "8q12.2"
module: 18
arm: "+"
pooled_cpm: 176.97
n_lines_expressing: 47
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CHD7

*chromodomain helicase DNA binding protein 7* — 8q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.98× (z +15.5, q 0e+00, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.481× (z -16.0, q 0e+00, down in 35 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.759× (z -6.3, q 4e-08, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCF20]] (+0.63, fdr 1e-05), [[PALS2]] (+0.63, fdr 1e-05), [[UCK2]] (+0.63, fdr 7e-06); moves opposite to [[SENP2]] (-0.56, fdr 1e-05), [[ZNF490]] (-0.54, fdr 1e-05), [[OSCP1]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[CAMKMT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10092.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.98×** | +15.5 | 0e+00 | 41/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.78×** | +13.1 | 1e-36 | 42/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +12.3 | 3e-32 | 39/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +10.4 | 3e-23 | 36/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +7.5 | 8e-12 | 36/45 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +6.2 | 6e-08 | 25/45 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.31×** | +6.1 | 8e-08 | 31/44 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.30×** | +5.9 | 2e-07 | 25/45 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +5.8 | 4e-07 | 32/45 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +5.7 | 8e-07 | 28/45 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +5.3 | 5e-06 | 24/45 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +5.2 | 8e-06 | 32/41 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.8 | 8e-05 | 16/45 (A498, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +4.7 | 1e-04 | 24/44 (NCI-H1792, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.22×** | +4.5 | 3e-04 | 21/46 (A498, RPMI-7951, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +4.0 | 0.002 | 19/45 (A498, LOX-IMVI, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.020 | 18/45 (PANC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.057 | 17/45 (LOX-IMVI, C32, …) | top dose only | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.082 | 7/45 (J82, SW 900, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.089 | 8/44 (NCI-H23, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10092.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.481×** | -16.0 | 0e+00 | 35/41 (A-427, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.514×** | -15.1 | 0e+00 | 39/46 (C-33 A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.566×** | -12.0 | 9e-31 | 32/42 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.671×** | -8.7 | 3e-16 | 33/44 (RKO, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.759×** | -6.3 | 4e-08 | 25/45 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.764×** | -6.1 | 8e-08 | 25/45 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -5.6 | 2e-06 | 18/45 (RKO, J82, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 0.856× | -3.5 | 0.029 | 13/45 (KATO III, NCI-H23, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.804×** | -3.5 | 0.032 | 21/45 (HEC-1-A, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~3% of this change | 0.859× | -3.5 | 0.032 | 14/45 (KATO III, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.808×** | -3.4 | 0.037 | 21/45 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.906× | -3.2 | 0.067 | 6/45 (NCI-H2030, SHP-77, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.860× | -3.2 | 0.067 | 12/44 (NCI-H2030, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10092. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 197 | 10 (2 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +20.6) | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.568× (z -10.0) |
| [[H4 (line)]] | wt | 95.2 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 3.71× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 140 | 5 (2 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.32× (z +10.1) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.17× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -20.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 165 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 111 | 3 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +10.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -13.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 211 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.441× (z -13.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 183 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.31× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -30.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 217 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -8.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 113 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.418× (z -9.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 245 | 3 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 241 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.70× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.428× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 65.7 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +10.6) | — |
| [[COLO 205 (line)]] | alt | 108 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +12.0) | — |
| [[J82 (line)]] | alt | 212 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -20.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 210 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +16.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 222 | 3 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.34× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.356× (z -11.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 595 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.542× (z -9.2) |
| [[SW 900 (line)]] | alt | 211 | 4 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.29× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.490× (z -9.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 194 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 214 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -10.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 353 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.387× (z -10.9) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 317 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.43× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -14.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 340 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -17.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 207 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.471× (z -10.0) |
| [[SNU-1 (line)]] | wt | 265 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -15.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 209 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 372 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.467× (z -8.5) |
| [[HOP62 (line)]] | alt | 123 | 2 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.29× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 89.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 179 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -22.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 121 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.05 µM 2.04× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.616× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 171 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.502× (z -9.0) ⚠ toxic |
| [[A498 (line)]] | wt | 69.7 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 168 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.427× (z -9.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 220 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -15.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 175 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 178 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.537× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -9.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 18.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 325 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 136 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10092), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF20]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[PALS2]] | +0.63 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[UCK2]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SFMBT1]] | +0.63 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[KANK1]] | +0.61 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[ADCY3]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[MEMO1]] | +0.57 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[CAMKMT]] | +0.56 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[TBC1D4]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ARHGEF11]] | +0.56 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[XPO5]] | +0.55 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[TMTC4]] | +0.55 | +0.66 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP2]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[ZNF490]] | -0.54 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[OSCP1]] | -0.51 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[PI4KB]] | -0.50 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[BTN3A1]] | -0.50 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[NDUFA5]] | -0.50 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[TP53BP1]] | -0.48 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[BBOF1]] | -0.48 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TMCO1]] | -0.48 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[MMUT]] | -0.48 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[YME1L1]] | -0.48 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[TBC1D23]] | -0.48 | -0.42 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMKMT]] | C | CHD7 activity raises CAMKMT's level | lines that do not express CHD7 (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without CHD7 | 0.058 | ⚠ few lines (3 vs 47); across organs; also absent: GDPD1, ENSG00000287975, PIM2 |
| [[CCDC88C]] | C | CHD7 activity raises CCDC88C's level | lines that do not express CHD7 (3) vs lines expressing it (47) | 3.61× lower at baseline in the lines without CHD7 | 0.099 | ⚠ few lines (3 vs 47); across organs; also absent: GDPD1, ENSG00000287975, PIM2 |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.4, -37.4); signed map (7.9, -2.8). **Vector** length 117, 40.4% of its response variance represented; |z| ≥ 3 in 1,363 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.6 | +4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.6 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +7.6 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.4 | +5.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.6 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.5 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -2.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.8 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +0.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.9 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -0.6 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | chromodomain helicase DNA binding protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.2 — chr8:60,678,740-60,868,028 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1416, FLJ20357, FLJ20361; previously CRG |
| Gene groups (HGNC) | Myb/SANT domain containing; Helicases; SNF2 related family |
| Reactome | 4 pathways, smallest: CHD6, CHD7, CHD8, CHD9 subfamily; CHD chromatin remodelers; ATP-dependent chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2D1](https://www.uniprot.org/uniprotkb/Q9P2D1) (ATP-dependent chromatin remodeler CHD7):

> ATP-dependent chromatin-remodeling factor, slides nucleosomes along DNA; nucleosome sliding requires ATP. Probable transcription regulator. May be involved in the in 45S precursor rRNA production.

**Summary**, from NCBI Gene [55636](https://www.ncbi.nlm.nih.gov/gene/55636):

> This gene encodes a protein that contains several helicase family domains. Mutations in this gene have been found in some patients with the CHARGE syndrome. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2015]

**Accessions** — [HGNC:20626](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20626) · Entrez [55636](https://www.ncbi.nlm.nih.gov/gene/55636) · UniProt [Q9P2D1](https://www.uniprot.org/uniprotkb/Q9P2D1) · Ensembl [ENSG00000171316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171316)

## Data

Gene col 10092: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10092); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10092, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10092]; `tensor/DDL_lfc|DDL_z.npy` [10092]; `embed/gene_vectors.npy` [10092]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10092 or target_col == 10092). Every well: [[CHD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
