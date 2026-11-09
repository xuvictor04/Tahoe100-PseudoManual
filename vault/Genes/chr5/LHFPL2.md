---
symbol: "LHFPL2"
type: "gene"
col: 7011
ensembl_id: "ENSG00000145685"
name: "LHFPL tetraspan subfamily member 2"
location: "5q14.1"
module: 72
arm: "+"
pooled_cpm: 157.76
n_lines_expressing: 46
n_dd_up: 11
n_dd_down: 26
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# LHFPL2

*LHFPL tetraspan subfamily member 2* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.69× (z +9.2, q 3e-17, up in 36 of 44 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.41× (z +6.0, q 4e-07, up in 30 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.190× (z -28.8, q 0e+00, down in 41 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SFN]] (+0.55, fdr 2e-05), [[MICALL1]] (+0.53, fdr 1e-05), [[TANGO2]] (+0.52, fdr 2e-05); moves opposite to [[YY1AP1]] (-0.53, fdr 4e-05), [[NFIX]] (-0.49, fdr 7e-05), [[CEP135]] (-0.48, fdr 4e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC01705]] → it (grade B ⚠); 2 go from it, the strongest it → [[SESTD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7011.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +9.2 | 3e-17 | 36/44 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.56×** | +7.3 | 6e-11 | 30/44 (SW480, HT-29, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +6.0 | 4e-07 | 30/44 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.41×** | +5.8 | 9e-07 | 30/43 (SW 900, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +5.5 | 4e-06 | 26/44 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 8e-04 | 25/43 (SW 900, H4, …) | rises with dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.27×** | +4.2 | 0.002 | 21/44 (BT-474, COLO 205, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.048 | 19/43 (BT-474, C32, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.060 | 16/44 (HOP62, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.063 | 15/44 (SK-MEL-2, NCI-H460, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.096 | 14/45 (BT-474, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7011.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.190×** | -28.8 | 0e+00 | 41/44 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.201×** | -27.8 | 0e+00 | 42/44 (A549, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.286×** | -21.7 | 0e+00 | 39/44 (A549, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.417×** | -21.4 | 0e+00 | 42/44 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.401×** | -15.8 | 0e+00 | 40/45 (KATO III, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.394×** | -15.5 | 0e+00 | 34/39 (A549, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.465×** | -12.8 | 2e-35 | 39/44 (NCI-H1792, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.504×** | -11.0 | 3e-26 | 32/41 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.534×** | -10.9 | 9e-26 | 36/44 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -10.1 | 3e-22 | 31/45 (NCI-H1792, A-172, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.565×** | -9.9 | 3e-21 | 35/44 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.615×** | -8.1 | 2e-14 | 31/46 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.640×** | -7.4 | 4e-12 | 30/44 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.655×** | -7.3 | 9e-12 | 30/44 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **0.692×** | -6.4 | 7e-09 | 31/43 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.785×** | -5.9 | 1e-07 | 25/44 (SK-MEL-2, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.777×** | -4.4 | 4e-04 | 24/44 (SW48, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.841× | -4.2 | 6e-04 | 22/44 (NCI-H2347, CHP-212, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.633×** | -4.1 | 8e-04 | 23/45 (A549, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.788×** | -4.1 | 9e-04 | 21/45 (HOP62, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.016 | 20/44 (KATO III, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7011. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 375 | 0 | 16 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0820× (z -27.6) |
| [[RPMI-7951 (line)]] | alt | 297 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -23.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.154× (z -17.8) |
| [[HOP62 (line)]] | alt | 286 | 0 | 14 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0760× (z -25.6) |
| [[HS-578T (line)]] | alt | 391 | 0 | 14 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0622× (z -26.0) |
| [[NCI-H1792 (line)]] | alt | 607 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0630× (z -36.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0572× (z -26.5) |
| [[SW480 (line)]] | alt | 77.9 | 8 (6 ⚠) | 6 (3 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.36× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.17× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.193× (z -22.7) |
| [[A549 (line)]] | wt | 240 | 1 | 11 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.31× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.0800× (z -27.2) |
| [[A498 (line)]] | wt | 271 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -21.0) |
| [[hTERT-HPNE (line)]] | wt | 252 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0993× (z -15.4) |
| [[LS 180 (line)]] | wt | 111 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -21.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.167× (z -19.1) |
| [[NCI-H2347 (line)]] | alt | 189 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -16.8) |
| [[C32 (line)]] | wt | 253 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -18.2) |
| [[KATO III (line)]] | alt | 214 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0835× (z -26.9) |
| [[SNU-423 (line)]] | alt | 186 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -20.2) |
| [[SW 900 (line)]] | alt | 209 | 1 | 8 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.62× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -16.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.190× (z -15.9) |
| [[J82 (line)]] | alt | 166 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -22.0) |
| [[SW1417 (line)]] | alt | 115 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -21.9) |
| [[Hs 766T (line)]] | wt | 58.3 | 3 | 4 (1 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 3.15× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.195× (z -12.6) |
| [[HT-29 (line)]] | alt | 99.3 | 2 (1 ⚠) | 5 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.84× (z +9.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.57× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -19.2) |
| [[RKO (line)]] | wt | 93.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -18.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.254× (z -12.8) |
| [[SW48 (line)]] | wt | 103 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -16.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.147× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 378 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0873× (z -25.3) |
| [[COLO 205 (line)]] | alt | 172 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0968× (z -20.1) |
| [[LOX-IMVI (line)]] | wt | 62.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -17.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 42.9 | 5 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.78× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.364× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 97.4 | 2 | 4 (2 ⚠) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 3.15× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 162 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -19.3) |
| [[BT-474 (line)]] | alt | 157 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -14.5) |
| [[LoVo (line)]] | wt | 256 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0981× (z -24.9) |
| [[CHP-212 (line)]] | wt | 111 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -12.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.106× (z -12.3) |
| [[H4 (line)]] | wt | 120 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.162× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 147 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -16.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.300× (z -11.2) |
| [[PANC-1 (line)]] | alt | 85.2 | 1 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.43× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.424× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 91.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.291× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -10.9) |
| [[SHP-77 (line)]] | alt | 74.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -12.2) |
| [[A-427 (line)]] | wt | 58.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[C-33 A (line)]] | alt | 65.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -10.2) |
| [[SW 1088 (line)]] | alt | 263 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.118× (z -9.3) |
| [[AN3 CA (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW 1271 (line)]] | alt | 56.1 | 0 | 1 | — | [[NG25 (drug)]] 0.05 µM 0.0568× (z -9.4) |
| [[HCT15 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 53.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7011), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFN]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[MICALL1]] | +0.53 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.52 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[LINC01564]] | +0.52 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[AAK1]] | +0.51 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[RAB5IF]] | +0.50 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[CDR2L]] | +0.49 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[SLC35C1]] | +0.48 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[KRT16]] | +0.48 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[STRIP2]] | +0.47 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[SNX29]] | +0.47 | +0.53 / +0.31 | both halves | 2e-04 |  |
| [[VTI1A]] | +0.47 | +0.55 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YY1AP1]] | -0.53 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[NFIX]] | -0.49 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[CEP135]] | -0.48 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[DLEU1]] | -0.47 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[KLHL32]] | -0.46 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[ARHGAP12]] | -0.46 | -0.34 / -0.45 | both halves | 1e-04 | STRING 416 |
| [[KPNA5]] | -0.46 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[NUAK2]] | -0.45 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ZBTB25]] | -0.45 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[DBP]] | -0.44 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[SLC35E2B]] | -0.44 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[ANO9]] | -0.44 | -0.44 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01705]] | B | LINC01705 activity raises LHFPL2's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without LINC01705 | 0.003 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[ST3GAL1]] | B | ST3GAL1 activity raises LHFPL2's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.69× lower at baseline in the lines without ST3GAL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[LINC02257]] | B | LINC02257 activity raises LHFPL2's level | lines that do not express LINC02257 (15) vs lines expressing it (35) | 2.03× lower at baseline in the lines without LINC02257 | 0.028 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent |
| [[PLXNA2]] | B | PLXNA2 activity raises LHFPL2's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 2.14× lower at baseline in the lines without PLXNA2 | 0.033 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[NAV1]] | B | NAV1 activity raises LHFPL2's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without NAV1 | 0.069 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[KLRC4-KLRK1]] | B | KLRC4-KLRK1 activity weakens LHFPL2's drug response | lines that do not express KLRC4-KLRK1 (26) vs lines expressing it (19) | the lines without KLRC4-KLRK1 respond 1.71× as strongly (z diff -2.58); strongest at Homoharringtonine 0.5 µM: 0.39x vs 0.71x (z diff -4.0) | 0.093 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KLRC3, KLRC2, PIP5K1B; target measured in part of the lines; artifact flags |
| [[SESTD1]] | C | SESTD1 activity raises LHFPL2's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 3.71× lower at baseline in the lines without SESTD1 | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SESTD1]] | C | LHFPL2 activity raises SESTD1's level | lines that do not express LHFPL2 (4) vs lines expressing it (46) | 4.25× lower at baseline in the lines without LHFPL2 | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, SESTD1, HIPK2; maybe low, not absent; co-absent with the target |
| [[NPC1]] | C | LHFPL2 activity raises NPC1's level | lines that do not express LHFPL2 (4) vs lines expressing it (46) | 1.84× lower at baseline in the lines without LHFPL2 | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, SESTD1, HIPK2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.441). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.3, -10.8); signed map (-7.2, 25.6). **Vector** length 113, 37.3% of its response variance represented; |z| ≥ 3 in 1,834 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.0 | +6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | +8.6 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.7 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.7 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | -10.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.6 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +1.3 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.8 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.8 | -12.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.6 | -4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.2 | -21.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.2 | -2.5 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -2.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | LHFPL tetraspan subfamily member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:78,485,215-78,770,021 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0206 |
| Gene groups (HGNC) | LHFPL tetraspan proteins |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZUX7](https://www.uniprot.org/uniprotkb/Q6ZUX7) (LHFPL tetraspan subfamily member 2 protein):

> Plays a role in female and male fertility. Involved in distal reproductive tract development.

**Summary**, from NCBI Gene [10184](https://www.ncbi.nlm.nih.gov/gene/10184):

> This gene is a member of the lipoma HMGIC fusion partner (LHFP) gene family, which is a subset of the superfamily of tetraspan transmembrane protein encoding genes. Mutations in one LHFP-like gene result in deafness in humans and mice, and a second LHFP-like gene is fused to a high-mobility group gene in a translocation-associated lipoma. Alternatively spliced transcript variants have been found, but their biological validity has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6588](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6588) · Entrez [10184](https://www.ncbi.nlm.nih.gov/gene/10184) · UniProt [Q6ZUX7](https://www.uniprot.org/uniprotkb/Q6ZUX7) · Ensembl [ENSG00000145685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145685)

## Data

Gene col 7011: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7011); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7011, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7011]; `tensor/DDL_lfc|DDL_z.npy` [7011]; `embed/gene_vectors.npy` [7011]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7011 or target_col == 7011). Every well: [[LHFPL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LHFPL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
