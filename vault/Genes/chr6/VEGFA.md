---
symbol: "VEGFA"
type: "gene"
col: 3399
ensembl_id: "ENSG00000112715"
name: "vascular endothelial growth factor A"
location: "6p21.1"
module: 180
arm: "+"
pooled_cpm: 282.27
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 35
n_dd_up_clean: 3
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# VEGFA

*vascular endothelial growth factor A* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.35× (z +15.3, q 0e+00, up in 46 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Dihydroartemisinin (drug)]] 0.5 µM: 1.32× (z +4.2, q 0.005, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.371× (z -20.7, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENO2]] (+0.59, fdr 1e-05), [[SH3D21]] (+0.59, fdr 1e-05), [[NDRG1]] (+0.58, fdr 1e-05); moves opposite to [[ADGRG6]] (-0.56, fdr 4e-05), [[TMX3]] (-0.49, fdr 5e-05), [[ABCE1]] (-0.48, fdr 3e-05).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PLOD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3399.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.35×** | +15.3 | 0e+00 | 46/48 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +6.4 | 5e-08 | 38/46 (SNU-1, SW48, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +4.9 | 2e-04 | 30/46 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.005 | 35/46 (SNU-1, PANC-1, …) | two highest doses | position effect removed |
| [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM | ⚠ unreliable plate only; position correction uncertain | **1.29×** | +3.8 | 0.019 | 29/47 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.048 | 25/46 (COLO 205, CFPAC-1, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.048 | 23/46 (Hs 766T, SNU-1, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | 1.50× | +3.2 | 0.11 | 21/46 (Hs 766T, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.11 | 22/45 (J82, H4, …) | rises with dose | low cells (technical?) |
| [[Bicalutamide (drug)]] 0.05 µM |  | 1.23× | +3.1 | 0.11 | 21/46 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3399.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.371×** | -20.7 | 0e+00 | 41/46 (SW 900, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.343×** | -15.8 | 0e+00 | 46/46 (SW 900, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.352×** | -14.9 | 0e+00 | 33/42 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.368×** | -14.8 | 0e+00 | 45/46 (SW 900, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.402×** | -13.5 | 3e-39 | 37/47 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.430×** | -12.5 | 1e-33 | 44/46 (AN3 CA, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.420×** | -12.3 | 5e-33 | 38/45 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.466×** | -11.3 | 1e-27 | 45/46 (SW 900, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.559×** | -8.3 | 9e-15 | 31/46 (SW 900, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.589×** | -7.8 | 3e-13 | 44/46 (SW 900, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.564×** | -7.8 | 3e-13 | 32/43 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.694×** | -7.6 | 1e-12 | 32/47 (HS-578T, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.615×** | -7.2 | 3e-11 | 39/46 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.623×** | -6.7 | 7e-10 | 29/45 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.647×** | -6.1 | 5e-08 | 31/46 (HOP62, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.764×** | -5.6 | 7e-07 | 34/46 (HS-578T, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.526×** | -5.0 | 2e-05 | 32/47 (SW 900, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.716×** | -4.9 | 2e-05 | 35/46 (RPMI-7951, A549, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[vincristine (drug)]] 0.05 µM |  | **0.735×** | -4.3 | 4e-04 | 34/46 (MIA PaCa-2, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.820×** | -4.1 | 9e-04 | 24/46 (PANC-1, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.781×** | -3.5 | 0.010 | 27/45 (CFPAC-1, NCI-H1573, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.660×** | -3.2 | 0.028 | 25/47 (HOP62, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.806×** | -3.2 | 0.030 | 20/46 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Cilostazol (drug)]] 5 µM |  | **0.800×** | -3.2 | 0.030 | 22/46 (SHP-77, A-172, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 529 | 0 | 23 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -31.8) |
| [[HOP62 (line)]] | alt | 521 | 1 (1 ⚠) | 16 (10 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.80× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -22.0) |
| [[RPMI-7951 (line)]] | alt | 664 | 0 | 17 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -28.4) |
| [[HS-578T (line)]] | alt | 1,164 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -30.9) |
| [[SNU-423 (line)]] | alt | 815 | 0 | 14 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -24.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.275× (z -18.9) |
| [[hTERT-HPNE (line)]] | wt | 456 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -13.3) |
| [[BT-474 (line)]] | alt | 335 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -22.2) |
| [[H4 (line)]] | wt | 464 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -21.5) |
| [[KATO III (line)]] | alt | 450 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -18.1) |
| [[A-172 (line)]] | wt | 287 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0784× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.229× (z -13.6) |
| [[A498 (line)]] | wt | 340 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -18.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.229× (z -15.5) |
| [[AN3 CA (line)]] | alt | 673 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0573× (z -28.8) |
| [[HT-29 (line)]] | alt | 357 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -15.9) |
| [[NCI-H1792 (line)]] | alt | 415 | 1 (1 ⚠) | 9 (6 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.38× (z +9.4) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -24.0) |
| [[J82 (line)]] | alt | 273 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -11.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.465× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 444 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -19.6) |
| [[CFPAC-1 (line)]] | alt | 470 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.315× (z -12.5) |
| [[PANC-1 (line)]] | alt | 179 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -19.8) |
| [[LS 180 (line)]] | wt | 496 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -16.0) |
| [[NCI-H1573 (line)]] | alt | 136 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -12.0) |
| [[A549 (line)]] | wt | 145 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -15.8) |
| [[CHP-212 (line)]] | wt | 308 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -13.9) |
| [[COLO 205 (line)]] | alt | 248 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.314× (z -11.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.335× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 506 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.322× (z -9.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.368× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 170 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -13.7) |
| [[C32 (line)]] | wt | 226 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -13.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.254× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 380 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.573× (z -9.0) |
| [[SHP-77 (line)]] | alt | 204 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -17.5) |
| [[SW 1088 (line)]] | alt | 709 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -10.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 166 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.381× (z -9.1) |
| [[LoVo (line)]] | wt | 160 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.371× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 148 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.51× (z +12.0) ⚠ position not correctable | [[Panobinostat (drug)]] 5 µM 0.363× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 89.9 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.20× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 143 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -10.1) |
| [[SW480 (line)]] | alt | 90.7 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.95× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -8.9) |
| [[C-33 A (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -8.6) |
| [[HCT15 (line)]] | alt | 281 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -17.4) |
| [[LOX-IMVI (line)]] | wt | 149 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -19.8) |
| [[NCI-H2122 (line)]] | alt | 302 | 0 | 1 | — | [[Roxadustat (drug)]] 0.5 µM 0.0539× (z -9.5) |
| [[NCI-H661 (line)]] | alt | 100 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -8.8) |
| [[SNU-1 (line)]] | wt | 117 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.13× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 40.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 162 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 68.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENO2]] | +0.59 | +0.66 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[SH3D21]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.58 | +0.68 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[ADM]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[SNAI1]] | +0.57 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[CLK3]] | +0.55 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[FUT11]] | +0.55 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[DDIT4]] | +0.55 | +0.53 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[HILPDA]] | +0.55 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[PKD1]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[MKNK2]] | +0.54 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[KDM3A]] | +0.54 | +0.59 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_HYPOXIA |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRG6]] | -0.56 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[TMX3]] | -0.49 | -0.39 / -0.50 | both halves | 5e-05 | pathway: Platelet activation, signaling and aggregation |
| [[ABCE1]] | -0.48 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[SH3D19]] | -0.48 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[SLC25A24]] | -0.48 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[CSE1L]] | -0.46 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[LARP4]] | -0.45 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[NAA25]] | -0.45 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[NUP155]] | -0.45 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[TMEM33]] | -0.44 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[UTP20]] | -0.44 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[ATE1]] | -0.44 | -0.37 / -0.41 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLOD2]] | B | PLOD2 activity raises VEGFA's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.43× lower at baseline in the lines without PLOD2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[DEPP1]] | B | DEPP1 activity raises VEGFA's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 2.37× lower at baseline in the lines without DEPP1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[NDRG1]] | B | NDRG1 activity raises VEGFA's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 2.96× lower at baseline in the lines without NDRG1 | 0.039 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[TOP2A]] | B | TOP2A activity raises VEGFA's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SH3D21]] | C | SH3D21 activity raises VEGFA's level | lines that do not express SH3D21 (4) vs lines expressing it (46) | 2.43× lower at baseline in the lines without SH3D21 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000286677; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.1, -14.2); signed map (-33.9, 29.0). **Vector** length 128, 48.3% of its response variance represented; |z| ≥ 3 in 1,500 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +6.6 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.0 | -7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | -14.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.7 | -15.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.0 | +3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | -2.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -5.4 | -13.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.3 | -6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -14.9 |
|  | [[NG25 (drug)]] 5 µM |  | -4.9 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.7 | -7.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.6 | -3.5 |
|  | [[vincristine (drug)]] 0.05 µM |  | -3.4 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -2.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | vascular endothelial growth factor A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,770,184-43,786,487 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VEGF-A, VPF; previously VEGF |
| Gene groups (HGNC) | VEGF family |
| Hallmark sets | ANGIOGENESIS, HEDGEHOG_SIGNALING, UNFOLDED_PROTEIN_RESPONSE, GLYCOLYSIS, HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 23 pathways, smallest: VEGF binds to VEGFR leading to receptor dimerization; VEGF ligand-receptor interactions; Regulation of gene expression by Hypoxia-inducible Factor |
| Matched by | ensembl_id |

**Function**, from UniProt [P15692](https://www.uniprot.org/uniprotkb/P15692) (Vascular endothelial growth factor A, long form):

> [N-VEGF]: Participates in the induction of key genes involved in the response to hypoxia and in the induction of angiogenesis such as HIF1A. Involved in protecting cells from hypoxia-mediated cell death (By similarity).; [VEGFA]: Growth factor active in angiogenesis, vasculogenesis and endothelial cell growth. Induces endothelial cell proliferation, promotes cell migration, inhibits apoptosis and induces permeabilization of blood vessels. Binds to the FLT1/VEGFR1 and KDR/VEGFR2 receptors, …

**Summary**, from NCBI Gene [7422](https://www.ncbi.nlm.nih.gov/gene/7422):

> This gene is a member of the PDGF/VEGF growth factor family. It encodes a heparin-binding protein, which exists as a disulfide-linked homodimer. This growth factor induces proliferation and migration of vascular endothelial cells, and is essential for both physiological and pathological angiogenesis. Disruption of this gene in mice resulted in abnormal embryonic blood vessel formation. This gene is upregulated in many known tumors and its expression is correlated with tumor stage and …

**Accessions** — [HGNC:12680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12680) · Entrez [7422](https://www.ncbi.nlm.nih.gov/gene/7422) · UniProt [P15692](https://www.uniprot.org/uniprotkb/P15692) · Ensembl [ENSG00000112715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112715)

## Data

Gene col 3399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3399); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3399]; `tensor/DDL_lfc|DDL_z.npy` [3399]; `embed/gene_vectors.npy` [3399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3399 or target_col == 3399). Every well: [[VEGFA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VEGFA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
