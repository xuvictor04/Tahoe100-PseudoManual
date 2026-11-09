---
symbol: "RCN1"
type: "gene"
col: 551
ensembl_id: "ENSG00000049449"
name: "reticulocalbin 1"
location: "11p13"
module: 25
arm: "+"
pooled_cpm: 57.7
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# RCN1

*reticulocalbin 1* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.75× (z +15.5, q 0e+00, up in 43 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.53× (z +6.5, q 8e-09, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.231× (z -22.5, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TARDBP]] (+0.74, fdr 7e-06), [[MOB1A]] (+0.73, fdr 7e-06), [[ERAP1]] (+0.72, fdr 1e-05); moves opposite to [[ETHE1]] (-0.70, fdr 7e-06), [[ARID3A]] (-0.69, fdr 3e-05), [[CDKN2D]] (-0.68, fdr 4e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HLA-H]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 551.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +15.5 | 0e+00 | 43/45 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +14.1 | 1e-42 | 38/39 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +12.0 | 4e-31 | 38/42 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +6.5 | 8e-09 | 32/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +5.1 | 4e-05 | 30/47 (NCI-H460, HOP62, …) | two highest doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.3 | 0.002 | 0/47 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 0.002 | 27/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.020 | 23/47 (HOP62, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.3 | 0.070 | 20/46 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.076 | 16/47 (C32, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.1 | 0.095 | 15/47 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.097 | 13/47 (HOP62, A-172, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 551.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.231×** | -22.5 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.240×** | -21.8 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.266×** | -20.3 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.343×** | -16.4 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.387×** | -14.5 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.549×** | -13.0 | 2e-36 | 41/47 (SNU-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.369×** | -8.0 | 1e-13 | 43/47 (SW480, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.797×** | -4.9 | 7e-05 | 26/47 (LoVo, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.645×** | -4.8 | 1e-04 | 30/47 (Hs 766T, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.734×** | -4.7 | 1e-04 | 27/47 (SW1417, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.754×** | -4.2 | 0.002 | 26/47 (A498, HS-578T, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.832×** | -4.0 | 0.003 | 17/47 (NCI-H2347, SW480, …) | top dose only | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.779×** | -3.8 | 0.006 | 24/47 (HCT15, SW48, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.773×** | -3.8 | 0.006 | 20/46 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **0.781×** | -3.8 | 0.006 | 23/47 (SW 1088, A-172, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.751×** | -3.1 | 0.055 | 17/47 (NCI-H661, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 551. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 57.7 | 5 (3 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +9.1) | [[Belinostat (drug)]] 5 µM 0.129× (z -21.4) |
| [[SW480 (line)]] | alt | 88.0 | 3 (3 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.25× (z +13.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.0897× (z -28.9) |
| [[HOP62 (line)]] | alt | 55.5 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +14.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -11.2) |
| [[KATO III (line)]] | alt | 29.8 | 1 (1 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +10.0) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.0936× (z -18.8) |
| [[LS 180 (line)]] | wt | 36.2 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +12.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -15.4) |
| [[NCI-H1792 (line)]] | alt | 47.4 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +11.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.235× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 80.1 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +11.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -10.8) |
| [[HS-578T (line)]] | alt | 67.8 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +12.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.05 µM 0.304× (z -10.1) |
| [[LoVo (line)]] | wt | 58.6 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 0.05 µM 2.44× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.0813× (z -27.2) |
| [[LOX-IMVI (line)]] | wt | 35.3 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.0) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.232× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 60.5 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -22.1) |
| [[PANC-1 (line)]] | alt | 48.4 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.245× (z -14.4) |
| [[RKO (line)]] | wt | 42.9 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +8.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.117× (z -16.2) |
| [[SNU-423 (line)]] | alt | 90.6 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 4.04× (z +12.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.291× (z -11.4) |
| [[A498 (line)]] | wt | 161 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.294× (z -13.6) |
| [[A549 (line)]] | wt | 43.9 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +11.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -11.9) |
| [[H4 (line)]] | wt | 88.9 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.05 µM 0.150× (z -14.2) |
| [[J82 (line)]] | alt | 87.4 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.59× (z +8.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.164× (z -17.6) |
| [[SK-MEL-2 (line)]] | alt | 42.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -20.7) |
| [[SNU-1 (line)]] | wt | 97.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -25.4) |
| [[SW1417 (line)]] | alt | 116 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.234× (z -14.8) |
| [[SW48 (line)]] | wt | 54.7 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.164× (z -12.3) |
| [[C32 (line)]] | wt | 35.8 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.226× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 24.0 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +12.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -9.5) |
| [[A-172 (line)]] | wt | 77.0 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.240× (z -13.8) |
| [[A-427 (line)]] | wt | 37.0 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 3.25× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -14.7) |
| [[HCT15 (line)]] | alt | 62.3 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -16.8) |
| [[Hs 766T (line)]] | wt | 28.8 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.27× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.177× (z -11.8) |
| [[HT-29 (line)]] | alt | 24.4 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +9.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.266× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 70.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -15.6) |
| [[SW 900 (line)]] | alt | 44.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -12.5) |
| [[BT-474 (line)]] | alt | 35.5 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.219× (z -11.6) |
| [[C-33 A (line)]] | alt | 56.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.151× (z -14.3) |
| [[COLO 205 (line)]] | alt | 28.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0739× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 32.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -16.0) |
| [[Panc 03.27 (line)]] | alt | 55.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -12.5) |
| [[AN3 CA (line)]] | alt | 63.1 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.132× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 32.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.157× (z -12.9) |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 43.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -10.4) |
| [[SW 1088 (line)]] | alt | 83.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0328× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 69.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.28× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 62.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 48.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 551), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TARDBP]] | +0.74 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[ERAP1]] | +0.72 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[UBQLN4]] | +0.71 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[CAPRIN1]] | +0.70 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[FUCA2]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation |
| [[PDIA3P1]] | +0.68 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[U2AF2]] | +0.68 | +0.38 / +0.64 | both halves | 7e-05 |  |
| [[ZMPSTE24]] | +0.68 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[ANKRD40]] | +0.67 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[HCFC1]] | +0.67 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.67 | +0.37 / +0.66 | both halves | 8e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETHE1]] | -0.70 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[ARID3A]] | -0.69 | -0.46 / -0.68 | both halves | 3e-05 |  |
| [[CDKN2D]] | -0.68 | -0.42 / -0.67 | both halves | 4e-05 |  |
| [[CIB1]] | -0.67 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[SIRT6]] | -0.65 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[FAM89B]] | -0.65 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[MARCHF9]] | -0.64 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[NUDT22]] | -0.64 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[TMEM191A-1]] | -0.64 | -0.33 / -0.62 | both halves | 1e-04 |  |
| [[PIGH]] | -0.64 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[POLD4]] | -0.63 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[LIN7B]] | -0.63 | -0.41 / -0.61 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-H]] | B | HLA-H activity raises RCN1's level | lines that do not express HLA-H (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without HLA-H | 0.020 | ⚠ within organs, on part of the lines; also absent: GPAT3, S100A6, ENSG00000290574; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.2, -23.1); signed map (-13.6, -36.9). **Vector** length 121, 36.3% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.6 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.2 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.1 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +3.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +4.2 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.5 | +1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +0.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.1 | -14.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.7 | -16.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.9 | -22.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.5 | -4.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.6 | -3.1 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -3.4 | -3.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.0 | -2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | reticulocalbin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:32,091,074-32,105,722 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Rcal, PIG20, FLJ37041; previously RCN |
| Gene groups (HGNC) | CREC family |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15293](https://www.uniprot.org/uniprotkb/Q15293) (Reticulocalbin-1):

> May regulate calcium-dependent activities in the endoplasmic reticulum lumen or post-ER compartment.

**Summary**, from NCBI Gene [5954](https://www.ncbi.nlm.nih.gov/gene/5954):

> Reticulocalbin 1 is a calcium-binding protein located in the lumen of the ER. The protein contains six conserved regions with similarity to a high affinity Ca(+2)-binding motif, the EF-hand. High conservation of amino acid residues outside of these motifs, in comparison to mouse reticulocalbin, is consistent with a possible biochemical function besides that of calcium binding. In human endothelial and prostate cancer cell lines this protein localizes to the plasma membrane.[provided by RefSeq, …

**Accessions** — [HGNC:9934](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9934) · Entrez [5954](https://www.ncbi.nlm.nih.gov/gene/5954) · UniProt [Q15293](https://www.uniprot.org/uniprotkb/Q15293) · Ensembl [ENSG00000049449](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049449)

## Data

Gene col 551: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 551); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 551, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 551]; `tensor/DDL_lfc|DDL_z.npy` [551]; `embed/gene_vectors.npy` [551]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 551 or target_col == 551). Every well: [[RCN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
