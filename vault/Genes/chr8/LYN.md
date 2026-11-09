---
symbol: "LYN"
type: "gene"
col: 14854
ensembl_id: "ENSG00000254087"
name: "LYN proto-oncogene, Src family tyrosine kinase"
location: "8q12.1"
module: 8
arm: "+"
pooled_cpm: 80.65
n_lines_expressing: 42
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 12
direction_downstream: 1
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# LYN

*LYN proto-oncogene, Src family tyrosine kinase* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.55× (z +16.2, q 0e+00, up in 33 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.762× (z -6.8, q 6e-09, down in 21 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tofacitinib (citrate) (drug)]] 0.5 µM: 0.800× (z -5.8, q 8e-07, down in 18 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H2347 0.252×, Panc 03.27 0.200×, BT-474 0.117×, SW480 0.445×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.0612×, NCI-H2347 0.336×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.272×, NCI-H2347 0.271×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RKO 0.410×, LoVo 0.475×); [[Auranofin (drug)]] 5 µM in 2 lines (NCI-H2347 0.422×, BT-474 0.237×); [[Budesonide (drug)]] 0.5 µM in 1 line (NCI-H1573 0.252×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NT5C3A]] (+0.61, fdr 1e-05), [[LYSMD2]] (+0.61, fdr 3e-05), [[PRRG4]] (+0.55, fdr 1e-05); moves opposite to [[CYTH2]] (-0.46, fdr 5e-05), [[TUBGCP2]] (-0.45, fdr 9e-05), [[HMGA2]] (-0.45, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[GBP4]] → it (grade B ⚠); 1 goes from it, the strongest it → [[IL15RA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14854.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +16.2 | 0e+00 | 33/40 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +9.7 | 1e-19 | 26/40 (J82, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +8.8 | 4e-16 | 23/41 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.26×** | +8.6 | 1e-15 | 23/40 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +8.4 | 4e-15 | 28/40 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +8.2 | 2e-14 | 21/40 (NCI-H460, RKO, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +6.9 | 3e-10 | 17/39 (J82, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +6.2 | 3e-08 | 15/35 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +6.2 | 3e-08 | 23/40 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +5.6 | 1e-06 | 18/41 (CFPAC-1, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.22×** | +5.1 | 2e-05 | 14/39 (SNU-423, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +5.1 | 2e-05 | 19/39 (PANC-1, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.45×** | +5.0 | 3e-05 | 15/38 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.9 | 4e-05 | 18/40 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 8e-05 | 13/41 (NCI-H460, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +4.7 | 8e-05 | 15/40 (CFPAC-1, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +4.4 | 3e-04 | 16/41 (NCI-H1792, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.38×** | +4.2 | 7e-04 | 7/40 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +4.2 | 7e-04 | 17/39 (A549, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14854.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H2347 0.252×, Panc 03.27 0.200×, BT-474 0.117×, SW480 0.445×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.0612×, NCI-H2347 0.336×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.272×, NCI-H2347 0.271×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RKO 0.410×, LoVo 0.475×); [[Auranofin (drug)]] 5 µM in 2 lines (NCI-H2347 0.422×, BT-474 0.237×); [[Budesonide (drug)]] 0.5 µM in 1 line (NCI-H1573 0.252×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.762×** | -6.8 | 6e-09 | 21/35 (NCI-H2347, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.757×** | -6.7 | 6e-09 | 22/37 (RKO, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.779×** | -6.5 | 2e-08 | 23/39 (RKO, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.800×** | -5.8 | 8e-07 | 18/40 (CFPAC-1, A498, …) | two highest doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.885× | -4.5 | 7e-04 | 10/41 (COLO 205, CFPAC-1, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.858× | -4.0 | 0.005 | 19/40 (NCI-H2347, BT-474, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.858× | -4.0 | 0.005 | 13/41 (BT-474, A498, …) | two highest doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.914× | -3.3 | 0.054 | 13/41 (CFPAC-1, BT-474, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.964× | -3.3 | 0.054 | 0/41 | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.883× | -3.3 | 0.063 | 9/39 (CFPAC-1, BT-474, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.888× | -3.1 | 0.100 | 6/39 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14854. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 75.0 | 6 (5 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +15.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.75× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.237× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 100 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +17.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.87× (z +13.3) | — |
| [[A549 (line)]] | wt | 62.8 | 5 (1 ⚠) | 1 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 3.38× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 170 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0612× (z -33.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.410× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 352 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.422× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 165 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.88× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -15.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 53.3 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.78× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -11.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 83.0 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.446× (z -13.4) ⚠ cell-cycle shift, explains ~20% of this change |
| [[J82 (line)]] | alt | 86.1 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.77× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +8.9) | — |
| [[KATO III (line)]] | alt | 115 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.412× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 66.4 | 1 (1 ⚠) | 2 | [[Trametinib (drug)]] 5 µM 3.05× (z +8.8) ⚠ cell-cycle shift, explains ~7% of this change | [[Budesonide (drug)]] 0.5 µM 0.252× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 38.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 3.61× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 216 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.273× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 40.7 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.74× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 114 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 1.97× (z +9.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.475× (z -11.1) |
| [[PANC-1 (line)]] | alt | 68.3 | 2 | 0 | [[Panobinostat (drug)]] 0.05 µM 1.94× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 33.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 42.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 197 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.92× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 64.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 31.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 91.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.68× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 91.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.96× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 41.8 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.65× (z +12.3) ⚠ unreliable plate only | — |
| [[NCI-H661 (line)]] | alt | 38.1 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0698× (z -8.7) |
| [[SNU-1 (line)]] | wt | 89.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.299× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 94.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -11.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.75 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.66 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14854), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NT5C3A]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[LYSMD2]] | +0.61 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[PRRG4]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[HDHD3]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[DAPP1]] | +0.54 | +0.43 / +0.48 | both halves | 3e-05 | same gene group; pathway: Antigen activates B Cell Receptor (BCR) leading to generation of second messengers; STRING 964 |
| [[C4orf19]] | +0.54 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[ELF3]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[MAP3K8]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 | pathway: Co-stimulation by CD28 |
| [[FRK]] | +0.53 | +0.44 / +0.56 | both halves | 3e-05 | same gene group; STRING 430 |
| [[PIK3C2B]] | +0.51 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CFB]] | +0.51 | +0.43 / +0.56 | both halves | 3e-05 | pathway: HALLMARK_COMPLEMENT |
| [[IL15RA]] | +0.50 | +0.44 / +0.46 | both halves | 3e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYTH2]] | -0.46 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[TUBGCP2]] | -0.45 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[HMGA2]] | -0.45 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[SLC25A16]] | -0.44 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[SLC37A2]] | -0.44 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[SLC30A9]] | -0.43 | -0.34 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP4]] | B | GBP4 activity raises LYN's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.53× lower at baseline in the lines without GBP4 | 0.010 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[IL15RA]] | B | IL15RA activity raises LYN's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 3.66× lower at baseline in the lines without IL15RA | 0.011 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[TSPAN15]] | B | TSPAN15 activity raises LYN's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 2.61× lower at baseline in the lines without TSPAN15 | 0.026 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[RBM47]] | B | RBM47 activity raises LYN's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without RBM47 | 0.032 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[FRK]] | B | FRK activity raises LYN's level | lines that do not express FRK (22) vs lines expressing it (28) | 2.00× lower at baseline in the lines without FRK | 0.038 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[COBL]] | B | COBL activity raises LYN's level | lines that do not express COBL (23) vs lines expressing it (27) | 2.13× lower at baseline in the lines without COBL | 0.054 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[PRRG4]] | B | PRRG4 activity raises LYN's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 2.46× lower at baseline in the lines without PRRG4 | 0.056 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[CD5L]] | B | CD5L activity raises LYN's level | lines that do not express CD5L (23) vs lines expressing it (27) | 1.45× lower at baseline in the lines without CD5L | 0.060 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[CASP10]] | B | CASP10 activity raises LYN's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.27× lower at baseline in the lines without CASP10 | 0.080 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[RASGRP3]] | B | RASGRP3 activity raises LYN's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 1.42× lower at baseline in the lines without RASGRP3 | 0.087 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[TNFSF10]] | B | TNFSF10 activity raises LYN's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 2.04× lower at baseline in the lines without TNFSF10 | 0.089 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[ST14]] | B | ST14 activity raises LYN's level | lines that do not express ST14 (32) vs lines expressing it (18) | 2.30× lower at baseline in the lines without ST14 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL15RA]] | B | LYN activity raises IL15RA's level | lines that do not express LYN (8) vs lines expressing it (42) | 2.40× lower at baseline in the lines without LYN | 0.046 | ⚠ within organs, on part of the lines; also absent: SLC12A7, NGEF, ENSG00000289862; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.446). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.5, 53.6); signed map (52.4, -2.0). **Vector** length 119, 31.7% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.5 | +16.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.1 | +8.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +5.3 | +8.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.2 | +4.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.2 | +6.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.7 | +4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.6 | +5.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.4 | +5.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.7 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.7 | -0.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.3 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.8 | -4.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.7 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | LYN proto-oncogene, Src family tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:55,879,835-56,014,169 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JTK8 |
| Gene groups (HGNC) | SH2 domain containing; Src family tyrosine kinases; SH3 domain containing |
| Hallmark sets | APICAL_SURFACE, ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, UV_RESPONSE_UP, COMPLEMENT |
| Reactome | 65 pathways, smallest: CD22 mediated BCR regulation; Erythropoietin activates Phospholipase C gamma (PLCG); Erythropoietin activates STAT5 |
| Matched by | ensembl_id |

**Function**, from UniProt [P07948](https://www.uniprot.org/uniprotkb/P07948) (Tyrosine-protein kinase Lyn):

> Non-receptor tyrosine-protein kinase that transmits signals from cell surface receptors and plays an important role in the regulation of innate and adaptive immune responses, hematopoiesis, responses to growth factors and cytokines, integrin signaling, but also responses to DNA damage and genotoxic agents. Functions primarily as negative regulator, but can also function as activator, depending on the context. Required for the initiation of the B-cell response, but also for its down-regulation …

**Summary**, from NCBI Gene [4067](https://www.ncbi.nlm.nih.gov/gene/4067):

> This gene encodes a tyrosine protein kinase, which maybe involved in the regulation of mast cell degranulation, and erythroid differentiation. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2011]

**Accessions** — [HGNC:6735](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6735) · Entrez [4067](https://www.ncbi.nlm.nih.gov/gene/4067) · UniProt [P07948](https://www.uniprot.org/uniprotkb/P07948) · Ensembl [ENSG00000254087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254087)

## Data

Gene col 14854: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14854); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14854, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14854]; `tensor/DDL_lfc|DDL_z.npy` [14854]; `embed/gene_vectors.npy` [14854]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14854 or target_col == 14854). Every well: [[LYN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
