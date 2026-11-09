---
symbol: "HNRNPK"
type: "gene"
col: 9072
ensembl_id: "ENSG00000165119"
name: "heterogeneous nuclear ribonucleoprotein K"
location: "9q21.32"
module: 3
arm: "-"
pooled_cpm: 227.4
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# HNRNPK

*heterogeneous nuclear ribonucleoprotein K* — 9q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.39× (z +17.5, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.63× (z +9.8, q 1e-20, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.500× (z -13.9, q 3e-41, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YWHAE]] (+0.82, fdr 7e-06), [[EIF4G2]] (+0.75, fdr 7e-06), [[HNRNPL]] (+0.73, fdr 7e-06); moves opposite to [[SDHAP2]] (-0.81, fdr 7e-06), [[ATP5MJ]] (-0.75, fdr 7e-06), [[MPG]] (-0.75, fdr 2e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9072.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.39×** | +17.5 | 0e+00 | 49/49 (SNU-423, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +16.0 | 0e+00 | 44/44 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.06×** | +14.5 | 1e-45 | 47/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +12.2 | 5e-32 | 44/45 (SNU-423, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.71×** | +10.8 | 4e-25 | 45/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.72×** | +10.5 | 1e-23 | 42/48 (A549, A498, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.63×** | +9.8 | 1e-20 | 45/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.37×** | +8.8 | 6e-17 | 36/48 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.52×** | +8.4 | 3e-15 | 39/48 (A-172, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.50×** | +8.1 | 3e-14 | 42/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.48×** | +7.9 | 2e-13 | 45/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.40×** | +6.5 | 3e-09 | 38/47 (NCI-H1792, COLO 205, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.38×** | +6.4 | 5e-09 | 42/48 (SW 900, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.65×** | +5.3 | 6e-06 | 34/49 (NCI-H1573, J82, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.006 | 23/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.021 | 26/48 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.024 | 20/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.039 | 20/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.039 | 17/48 (SHP-77, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9072.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.500×** | -13.9 | 3e-41 | 48/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.516×** | -13.3 | 6e-38 | 48/48 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.560×** | -11.7 | 4e-29 | 47/48 (AsPC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.708×** | -6.9 | 6e-10 | 44/48 (HepG2/C3A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.632×** | -4.8 | 2e-04 | 37/49 (A-427, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.800×** | -4.3 | 0.002 | 27/47 (HCT15, HT-29, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.821×** | -4.0 | 0.006 | 27/48 (Panc 03.27, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.878× | -3.6 | 0.024 | 10/48 (SK-MEL-2, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9072. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 142 | 14 (12 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +20.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.75× (z +13.0) | — |
| [[NCI-H460 (line)]] | wt | 222 | 13 (11 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +19.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.45× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.510× (z -9.7) |
| [[A549 (line)]] | wt | 228 | 9 (7 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +21.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.76× (z +14.6) | [[Panobinostat (drug)]] 0.5 µM 0.422× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 195 | 8 (8 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +16.1) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.382× (z -15.3) |
| [[HOP62 (line)]] | alt | 240 | 8 (7 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.06× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.400× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 180 | 8 (7 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.94× (z +17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.42× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.394× (z -12.1) |
| [[SW480 (line)]] | alt | 255 | 8 (7 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +18.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.78× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.399× (z -14.0) |
| [[A-172 (line)]] | wt | 199 | 10 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +15.9) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.39× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 270 | 7 (6 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +14.0) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.95× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.422× (z -13.4) |
| [[PANC-1 (line)]] | alt | 232 | 7 (6 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +19.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.96× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.400× (z -14.4) |
| [[J82 (line)]] | alt | 314 | 7 (6 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.84× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.505× (z -10.7) |
| [[KATO III (line)]] | alt | 240 | 6 (6 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.56× (z +17.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.430× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 308 | 6 (6 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +14.6) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 0.5 µM 0.394× (z -14.6) |
| [[HT-29 (line)]] | alt | 201 | 6 (6 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +16.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.457× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 260 | 6 (5 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +19.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.95× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.445× (z -11.0) |
| [[SNU-423 (line)]] | alt | 202 | 8 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +21.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 237 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +18.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.28× (z +11.8) | — |
| [[COLO 205 (line)]] | alt | 160 | 7 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +13.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HepG2_C3A (line)]] | wt | 209 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +13.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.345× (z -14.9) |
| [[Hs 766T (line)]] | wt | 180 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +13.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 212 | 4 (4 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +11.7) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.438× (z -12.8) |
| [[LS 180 (line)]] | wt | 255 | 4 (4 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +15.4) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.428× (z -10.9) |
| [[SW 900 (line)]] | alt | 185 | 4 (4 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +11.3) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 0.5 µM 0.449× (z -11.2) |
| [[A-427 (line)]] | wt | 224 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.11× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.494× (z -9.9) |
| [[HS-578T (line)]] | alt | 167 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.26× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 203 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +11.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.435× (z -12.6) |
| [[C-33 A (line)]] | alt | 295 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +11.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.437× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 169 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +12.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.433× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 193 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.19× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.435× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 210 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +11.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.504× (z -9.9) |
| [[SW48 (line)]] | wt | 240 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +10.8) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.428× (z -9.2) |
| [[C32 (line)]] | wt | 167 | 4 (3 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.50× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 287 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +13.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.471× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 200 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 216 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +13.2) ⚠ cell-cycle shift, explains ~90% of this change | — |
| [[H4 (line)]] | wt | 232 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 323 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +13.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.507× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 210 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +10.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SHP-77 (line)]] | alt | 158 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +12.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.514× (z -8.6) |
| [[CHP-212 (line)]] | wt | 272 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.423× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 266 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.81× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.523× (z -9.5) |
| [[SNU-1 (line)]] | wt | 279 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.63× (z +9.0) | — |
| [[RKO (line)]] | wt | 325 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.494× (z -10.1) |
| [[AN3 CA (line)]] | alt | 292 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 279 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9072), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAE]] | +0.82 | +0.72 / +0.83 | both halves | 7e-06 | STRING 403 |
| [[EIF4G2]] | +0.75 | +0.68 / +0.76 | both halves | 7e-06 | STRING 632 |
| [[HNRNPL]] | +0.73 | +0.59 / +0.70 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 990 |
| [[DDX3X]] | +0.72 | +0.62 / +0.62 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 757 |
| [[DDX6]] | +0.72 | +0.48 / +0.65 | both halves | 2e-05 | STRING 748 |
| [[TUG1]] | +0.71 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[PRKAR1A]] | +0.70 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[TASOR]] | +0.69 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[CPNE1]] | +0.69 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[HNRNPH3]] | +0.68 | +0.49 / +0.63 | both halves | 1e-05 | same gene group; STRING 809 |
| [[CHRAC1]] | +0.68 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[IL6ST]] | +0.68 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP2]] | -0.81 | -0.69 / -0.74 | both halves | 7e-06 |  |
| [[ATP5MJ]] | -0.75 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[MPG]] | -0.75 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[CAMLG]] | -0.75 | -0.70 / -0.68 | both halves | 7e-06 |  |
| [[LCMT1]] | -0.74 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[SDHAP1]] | -0.73 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[ANKS3]] | -0.72 | -0.62 / -0.67 | both halves | 7e-06 |  |
| [[COMMD6]] | -0.72 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[TMEM120B]] | -0.71 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[MRPL55]] | -0.71 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[SLC17A5]] | -0.70 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | -0.70 | -0.63 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises HNRNPK's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[C5]] | C | C5 activity raises HNRNPK's level | lines that do not express C5 (4) vs lines expressing it (46) | 1.20× lower at baseline in the lines without C5 | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLSPN, PRDM6, TCF19; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.825). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (0.4, -14.7); signed map (17.2, -33.2). **Vector** length 107, 41.4% of its response variance represented; |z| ≥ 3 in 1,331 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.53 to 10); *MYC targets v1* (hallmark, mean cos +0.60 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +7.8 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +7.3 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +16.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.4 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.5 | +1.6 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +2.7 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +3.8 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.9 | -11.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | -5.5 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | -13.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -13.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | +0.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.4 | +0.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.2 | -1.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.2 | -2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.32 — chr9:83,968,083-83,980,631 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSBP, TUNP; previously HNRPK |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Heterogeneous nuclear ribonucleoproteins |
| Reactome | 14 pathways, smallest: SUMOylation of RNA binding proteins; HCMV Late Events; HCMV Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [P61978](https://www.uniprot.org/uniprotkb/P61978) (Heterogeneous nuclear ribonucleoprotein K):

> One of the major pre-mRNA-binding proteins. Binds tenaciously to poly(C) sequences. Likely to play a role in the nuclear metabolism of hnRNAs, particularly for pre-mRNAs that contain cytidine-rich sequences. Can also bind poly(C) single-stranded DNA. Plays an important role in p53/TP53 response to DNA damage, acting at the level of both transcription activation and repression. When sumoylated, acts as a transcriptional coactivator of p53/TP53, playing a role in p21/CDKN1A and 14-3-3 sigma/SFN …

**Summary**, from NCBI Gene [3190](https://www.ncbi.nlm.nih.gov/gene/3190):

> This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the nucleus, some seem to shuttle between the nucleus and the cytoplasm. The hnRNP proteins have …

**Accessions** — [HGNC:5044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5044) · Entrez [3190](https://www.ncbi.nlm.nih.gov/gene/3190) · UniProt [P61978](https://www.uniprot.org/uniprotkb/P61978) · Ensembl [ENSG00000165119](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165119)

## Data

Gene col 9072: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9072); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9072, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9072]; `tensor/DDL_lfc|DDL_z.npy` [9072]; `embed/gene_vectors.npy` [9072]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9072 or target_col == 9072). Every well: [[HNRNPK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
