---
symbol: "ZC3H12A-DT"
type: "gene"
col: 13914
ensembl_id: "ENSG00000233621"
name: "lncRNA induced by TGF-beta and antagonizes TGF-beta signaling 1"
location: "1p34.3"
module: 139
arm: "+"
pooled_cpm: 15.48
n_lines_expressing: 49
n_dd_up: 36
n_dd_down: 31
n_dd_up_clean: 31
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# ZC3H12A-DT

*lncRNA induced by TGF-beta and antagonizes TGF-beta signaling 1* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.07× (z +19.8, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.449× (z -11.2, q 2e-26, down in 38 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.545× (z -8.5, q 4e-15, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEACAM22P-1]] (+0.59, fdr 1e-05), [[ZC3H12A]] (+0.56, fdr 1e-05, ⚠ same locus), [[EBI3]] (+0.56, fdr 1e-05), [[SAA4]] (+0.55, fdr 2e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ENOX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.07×** | +19.8 | 0e+00 | 41/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.48×** | +18.1 | 0e+00 | 41/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.57×** | +17.9 | 0e+00 | 44/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.34×** | +17.0 | 0e+00 | 41/46 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.71×** | +14.0 | 1e-42 | 38/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +13.0 | 8e-37 | 34/43 (LOX-IMVI, AsPC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.42×** | +12.5 | 1e-33 | 39/45 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +11.0 | 2e-26 | 26/44 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.59×** | +9.4 | 4e-19 | 37/45 (A498, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +5.9 | 2e-07 | 25/43 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.51×** | +5.9 | 2e-07 | 20/44 (A549, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.51×** | +5.8 | 3e-07 | 25/47 (PANC-1, HT-29, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.47×** | +5.5 | 2e-06 | 19/45 (BT-474, PANC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +4.7 | 1e-04 | 12/46 (MIA PaCa-2, NCI-H2030, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.25×** | +4.6 | 2e-04 | 16/46 (LS 180, AsPC-1, …) | all doses, flat | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.35×** | +4.3 | 6e-04 | 11/46 (BT-474, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.003 | 17/46 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.005 | 13/45 (A549, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13914.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.449×** | -11.2 | 2e-26 | 38/47 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.518×** | -9.2 | 9e-18 | 28/47 (H4, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.545×** | -8.5 | 4e-15 | 30/47 (H4, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.552×** | -8.3 | 2e-14 | 29/46 (H4, SW480, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.583×** | -7.6 | 5e-12 | 26/46 (H4, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.630×** | -6.4 | 1e-08 | 26/42 (H4, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.639×** | -6.3 | 3e-08 | 24/46 (H4, SW480, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.676×** | -5.2 | 1e-05 | 18/45 (A-172, CFPAC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.500×** | -5.1 | 3e-05 | 19/40 (HepG2/C3A, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.693×** | -4.9 | 5e-05 | 19/40 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.514×** | -4.9 | 6e-05 | 22/45 (Panc 03.27, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.520×** | -4.8 | 8e-05 | 17/44 (CFPAC-1, A549, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.715×** | -4.7 | 1e-04 | 16/47 (CFPAC-1, SW 1088, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.722×** | -4.5 | 2e-04 | 14/47 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.724×** | -4.5 | 3e-04 | 19/46 (SW480, A498, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.814×** | -4.0 | 0.002 | 17/45 (CFPAC-1, SNU-423, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.585×** | -3.9 | 0.003 | 9/42 (COLO 205, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.757×** | -3.9 | 0.003 | 16/46 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.593×** | -3.8 | 0.004 | 14/44 (RPMI-7951, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.615×** | -3.5 | 0.011 | 14/43 (SW 900, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.632×** | -3.4 | 0.021 | 13/43 (A498, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.784×** | -3.3 | 0.028 | 6/47 (SNU-423, LoVo, …) | top dose only | plate-row cell shift |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.795×** | -3.2 | 0.034 | 9/47 (SK-MEL-2, BT-474, …) | inconsistent across doses |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -3.1 | 0.049 | 5/47 (SW 1088, NCI-H661, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 54.1 | 0 | 10 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0622× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.107× (z -12.4) |
| [[PANC-1 (line)]] | alt | 9.08 | 8 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +18.0) | [[Digitoxin (drug)]] 0.5 µM 0.261× (z -8.7) |
| [[A-172 (line)]] | wt | 11.5 | 7 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 6.87× (z +10.1) | [[Hydroxyurea (drug)]] 0.05 µM 0.159× (z -8.8) |
| [[A498 (line)]] | wt | 41.0 | 4 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.89× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.6) |
| [[HOP62 (line)]] | alt | 13.6 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +14.2) | — |
| [[SW480 (line)]] | alt | 10.5 | 2 | 5 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.91× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.245× (z -8.7) |
| [[COLO 205 (line)]] | alt | 32.1 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.1) |
| [[KATO III (line)]] | alt | 22.1 | 2 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.99× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0662× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[CFPAC-1 (line)]] | alt | 29.4 | 3 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.61× (z +8.8) | [[Daptomycin (drug)]] 0.5 µM 0.231× (z -9.5) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 11.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +13.8) | — |
| [[A549 (line)]] | wt | 47.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0854× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 5.16 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.49× (z +10.7) | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0773× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 21.9 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.90× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 19.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +10.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0988× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 7.34 | 2 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.65× (z +12.7) ⚠ position not correctable · without an alert: [[Tucidinostat (drug)]] 5 µM 5.00× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 21.3 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.05× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.262× (z -9.1) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 7.80 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +13.2) | — |
| [[A-427 (line)]] | wt | 7.90 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0968× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 5.25 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.05 µM 0.0647× (z -8.8) |
| [[HS-578T (line)]] | alt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +10.9) | — |
| [[J82 (line)]] | alt | 7.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +10.7) | — |
| [[LoVo (line)]] | wt | 7.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 6.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.91× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 7.55 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0721× (z -11.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 33.4 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.66× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0786× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0943× (z -9.8) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEACAM22P-1]] | +0.59 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[ZC3H12A]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[EBI3]] | +0.56 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[SAA4]] | +0.55 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[SAA2-SAA4]] | +0.54 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SAA2]] | +0.53 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[PER1]] | +0.53 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[BIRC3]] | +0.52 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[UGCG]] | +0.52 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[IL3RA]] | +0.52 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SETD5]] | +0.51 | +0.22 / +0.50 | both halves | 6e-04 |  |
| [[SBNO2]] | +0.51 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[NFKBIA]] | +0.50 | +0.62 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENOX1]] | B | ENOX1 activity raises ZC3H12A-DT's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without ENOX1 | 0.005 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[CCL20]] | B | CCL20 activity raises ZC3H12A-DT's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.55× lower at baseline in the lines without CCL20 | 0.015 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[LINC02036]] | B | LINC02036 activity raises ZC3H12A-DT's level | lines that do not express LINC02036 (11) vs lines expressing it (39) | 1.85× lower at baseline in the lines without LINC02036 | 0.031 | ⚠ within organs, on part of the lines; also absent: LINC00887, ENSG00000256982, SIPA1L2; maybe low, not absent |
| [[C3]] | B | C3 activity raises ZC3H12A-DT's level | lines that do not express C3 (32) vs lines expressing it (18) | 1.84× lower at baseline in the lines without C3 | 0.069 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11 |
| [[SGPP2]] | B | SGPP2 activity raises ZC3H12A-DT's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 1.30× lower at baseline in the lines without SGPP2 | 0.070 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[TNFSF14]] | B | TNFSF14 activity raises ZC3H12A-DT's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.90× lower at baseline in the lines without TNFSF14 | 0.087 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[SQOR]] | B | SQOR activity raises ZC3H12A-DT's level | lines that do not express SQOR (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without SQOR | 0.087 | ⚠ within organs, on part of the lines; also absent: SAT1, ITPR3, LRRC8E |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.9, 8.9); signed map (13.5, 28.3). **Vector** length 90.7, 21.9% of its response variance represented; |z| ≥ 3 in 1,441 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.1 | +18.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.3 | +12.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +11.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +4.1 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +4.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.4 | +5.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.2 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.2 | -11.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -0.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.6 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -8.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -3.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -7.6 |

## What is on record

|  |  |
|---|---|
| Name | lncRNA induced by TGF-beta and antagonizes TGF-beta signaling 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p34.3 — chr1:37,350,934-37,474,432 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LOC728431; previously LINC01137, ZC3H12A-DT |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49453) · Entrez [728431](https://www.ncbi.nlm.nih.gov/gene/728431) · Ensembl [ENSG00000233621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233621)

## Data

Gene col 13914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13914); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13914]; `tensor/DDL_lfc|DDL_z.npy` [13914]; `embed/gene_vectors.npy` [13914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13914 or target_col == 13914). Every well: [[ZC3H12A-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC3H12A-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
