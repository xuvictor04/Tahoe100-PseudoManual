---
symbol: "NDUFS1"
type: "gene"
col: 341
ensembl_id: "ENSG00000023228"
name: "NADH:ubiquinone oxidoreductase core subunit S1"
location: "2q33.3"
module: 194
arm: "+"
pooled_cpm: 95.44
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# NDUFS1

*NADH:ubiquinone oxidoreductase core subunit S1* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.07× (z +23.6, q 0e+00, up in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.51× (z +19.0, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.693× (z -11.9, q 7e-30, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPP8]] (+0.68, fdr 7e-06), [[PSME3IP1]] (+0.68, fdr 1e-05), [[RC3H2]] (+0.65, fdr 1e-05); moves opposite to [[RALGDS]] (-0.64, fdr 1e-05), [[OCEL1]] (-0.64, fdr 4e-04), [[CARHSP1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 194]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 341.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +23.6 | 0e+00 | 46/49 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +19.7 | 0e+00 | 42/44 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +19.0 | 0e+00 | 42/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +14.6 | 0e+00 | 38/45 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +13.7 | 6e-41 | 40/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +9.6 | 7e-20 | 30/48 (HEC-1-A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.31×** | +8.5 | 1e-15 | 33/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.21×** | +6.3 | 2e-08 | 24/48 (HEC-1-A, LOX-IMVI, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +6.3 | 3e-08 | 22/48 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.5 | 2e-06 | 21/50 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.15× | +4.5 | 4e-04 | 18/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.14× | +4.1 | 0.002 | 10/48 (A498, SHP-77, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.13× | +4.0 | 0.002 | 10/47 (PANC-1, J82, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.09× | +3.9 | 0.003 | 6/48 (SW1417, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | 1.13× | +3.9 | 0.004 | 21/48 (HEC-1-A, LOX-IMVI, …) | all doses, flat |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 1.10× | +3.2 | 0.053 | 9/45 (HT-29, SNU-423, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 341.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.693×** | -11.9 | 7e-30 | 35/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.738×** | -9.9 | 1e-20 | 31/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.747×** | -9.5 | 5e-19 | 30/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -8.2 | 5e-14 | 22/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.789×** | -7.7 | 2e-12 | 29/48 (AsPC-1, SW480, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.836× | -5.8 | 6e-07 | 19/49 (SW 900, H4, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.886× | -5.6 | 2e-06 | 13/48 (AsPC-1, NCI-H23, …) | all doses, flat | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -5.0 | 4e-05 | 14/48 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.861× | -4.8 | 9e-05 | 16/49 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.888× | -3.9 | 0.007 | 7/48 (RKO, LS 180, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.889× | -3.8 | 0.007 | 11/48 (SW 1088, Panc 03.27, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.902× | -3.3 | 0.042 | 13/48 (H4, NCI-H1573, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.868× | -3.3 | 0.044 | 10/48 (SW1417, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.970× | -3.3 | 0.045 | 0/50 | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.903× | -3.1 | 0.063 | 8/48 (AsPC-1, RKO, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.839× | -3.0 | 0.099 | 9/48 (AsPC-1, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 341. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 118 | 4 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +17.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.53× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.626× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 71.7 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 115 | 5 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.46× (z +21.4) | [[Panobinostat (drug)]] 5 µM 0.607× (z -8.5) |
| [[C-33 A (line)]] | alt | 105 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +9.7) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.242× (z -14.5) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 99.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +11.9) | — |
| [[KATO III (line)]] | alt | 80.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 89.3 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +17.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.75× (z +15.0) | — |
| [[SNU-423 (line)]] | alt | 70.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 62.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.44× (z +11.1) ⚠ toxic; transcription drop | [[AZD2858 (drug)]] 0.5 µM 0.359× (z -9.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 96.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.53× (z +8.8) | — |
| [[LoVo (line)]] | wt | 81.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +17.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 91.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +14.0) | — |
| [[SK-MEL-2 (line)]] | alt | 69.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 121 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.58× (z +10.4) | — |
| [[A-427 (line)]] | wt | 94.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +14.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 126 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.81× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 83.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +15.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 108 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.467× (z -10.8) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 0.550× (z -8.5) |
| [[BT-474 (line)]] | alt | 83.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.7) | — |
| [[C32 (line)]] | wt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +11.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 89.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 74.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +13.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 119 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.4) | — |
| [[SW 900 (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 109 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.472× (z -11.4) |
| [[COLO 205 (line)]] | alt | 79.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +10.0) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 87.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 87.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.82× (z +9.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 84.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.29× (z +9.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 67.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 65.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +9.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 72.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +8.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 98.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 133 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.87× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 104 | 0 | 1 | — | [[Sulfatinib (drug)]] 0.5 µM 0.0813× (z -10.2) |
| [[SW48 (line)]] | wt | 81.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 85.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 125 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 82.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 93.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 341), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP8]] | +0.68 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PSME3IP1]] | +0.68 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[RC3H2]] | +0.65 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[TIA1]] | +0.65 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CPSF2]] | +0.65 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[TRMT13]] | +0.62 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[MCTS1]] | +0.62 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.62 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[ZMPSTE24]] | +0.61 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[PPWD1]] | +0.61 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[COPZ1]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[DNAJB14]] | +0.60 | +0.65 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALGDS]] | -0.64 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[OCEL1]] | -0.64 | -0.26 / -0.63 | both halves | 4e-04 |  |
| [[CARHSP1]] | -0.64 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[AMD1]] | -0.62 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[EIF4A3]] | -0.62 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[PHAF1]] | -0.61 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[NEIL2]] | -0.59 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[KHDRBS3]] | -0.59 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[SMG1P2]] | -0.59 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[BMP8B]] | -0.57 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[RBM38]] | -0.57 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[IGSF8]] | -0.56 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises NDUFS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-5.9, 3.2); signed map (16.8, -28.5). **Vector** length 123, 33.4% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +19.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +23.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.0 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +19.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +6.5 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +2.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.1 | +2.6 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.8 | -11.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.5 | -9.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.7 | -5.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.7 | -9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -8.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.9 | -0.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase core subunit S1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:206,114,817-206,159,509 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CI-75k |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase core subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Complex I biogenesis; Mitochondrial protein degradation; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P28331](https://www.uniprot.org/uniprotkb/P28331) (NADH-ubiquinone oxidoreductase 75 kDa subunit, mitochondrial):

> Core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which catalyzes electron transfer from NADH through the respiratory chain, using ubiquinone as an electron acceptor. Essential for catalysing the entry and efficient transfer of electrons within complex I. Plays a key role in the assembly and stability of complex I and participates in the association of complex I with ubiquinol-cytochrome reductase complex (Complex III) to form supercomplexes.

**Summary**, from NCBI Gene [4719](https://www.ncbi.nlm.nih.gov/gene/4719):

> The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. This protein is the largest subunit of complex I and it is a component of the iron-sulfur (IP) …

**Accessions** — [HGNC:7707](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7707) · Entrez [4719](https://www.ncbi.nlm.nih.gov/gene/4719) · UniProt [P28331](https://www.uniprot.org/uniprotkb/P28331) · Ensembl [ENSG00000023228](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023228)

## Data

Gene col 341: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 341); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 341, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 341]; `tensor/DDL_lfc|DDL_z.npy` [341]; `embed/gene_vectors.npy` [341]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 341 or target_col == 341). Every well: [[NDUFS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
