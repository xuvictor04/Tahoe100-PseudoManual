---
symbol: "DDX46"
type: "gene"
col: 7032
ensembl_id: "ENSG00000145833"
name: "DEAD-box helicase 46"
location: "5q31.1"
module: 36
arm: "+"
pooled_cpm: 188.98
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# DDX46

*DEAD-box helicase 46* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.17× (z +15.3, q 0e+00, up in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.44× (z +7.6, q 2e-12, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.869× (z -4.1, q 0.016, down in 19 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM: 0.823× (z -4.0, q 0.016, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARN]] (+0.59, fdr 1e-05), [[MTOR]] (+0.55, fdr 3e-05), [[CDK11B]] (+0.54, fdr 1e-05); moves opposite to [[SDCBP]] (-0.49, fdr 6e-05), [[POLR2M]] (-0.48, fdr 6e-04), [[PLEKHF2]] (-0.48, fdr 5e-04).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCN3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 22 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7032.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.17×** | +15.3 | 0e+00 | 46/49 (SNU-423, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.05×** | +14.3 | 9e-44 | 42/44 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.82×** | +12.3 | 1e-32 | 48/48 (LoVo, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.81×** | +12.3 | 2e-32 | 45/48 (LoVo, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.67×** | +10.7 | 2e-24 | 46/48 (LoVo, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.62×** | +10.0 | 1e-21 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.39×** | +9.6 | 6e-20 | 38/48 (NCI-H1792, SNU-423, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.58×** | +9.5 | 2e-19 | 43/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.59×** | +8.8 | 7e-17 | 39/45 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +7.6 | 2e-12 | 37/48 (H4, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +7.3 | 1e-11 | 41/49 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.39×** | +6.7 | 7e-10 | 42/48 (A-172, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.38×** | +6.7 | 9e-10 | 39/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.40×** | +6.7 | 1e-09 | 37/47 (SNU-423, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.33×** | +5.9 | 1e-07 | 36/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +5.3 | 4e-06 | 34/48 (BT-474, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +5.2 | 9e-06 | 27/48 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.001 | 25/48 (A-172, SNU-423, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.010 | 20/48 (H4, HOP62, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.4 | 0.013 | 14/49 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.017 | 23/48 (NCI-H460, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.020 | 2/49 (RPMI-7951, SW 900) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.053 | 20/47 (H4, HOP62, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.15× | +2.9 | 0.059 | 11/49 (BT-474, COLO 205, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.061 | 12/48 (CFPAC-1, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7032.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.869× | -4.1 | 0.016 | 19/48 (A-427, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.823×** | -4.0 | 0.016 | 28/48 (LoVo, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7032. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 152 | 10 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.89× (z +8.8) | — |
| [[SW480 (line)]] | alt | 213 | 10 (10 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[SNU-423 (line)]] | alt | 126 | 9 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 181 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 128 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[LoVo (line)]] | wt | 254 | 7 (7 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.26× (z +12.7) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A-172 (line)]] | wt | 140 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.08× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 188 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +10.2) | — |
| [[A549 (line)]] | wt | 164 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.07× (z +9.1) | — |
| [[H4 (line)]] | wt | 161 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 141 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +10.3) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[HS-578T (line)]] | alt | 158 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 178 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1792 (line)]] | alt | 136 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.5) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.49× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 142 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.27× (z +11.1) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.62× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 232 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[RPMI-7951 (line)]] | alt | 147 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[HEC-1-A (line)]] | alt | 239 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.19× (z +10.8) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[HT-29 (line)]] | alt | 185 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H2347 (line)]] | alt | 132 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H460 (line)]] | wt | 191 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[A498 (line)]] | wt | 204 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[BT-474 (line)]] | alt | 148 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.11× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[C32 (line)]] | wt | 125 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[KATO III (line)]] | alt | 155 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[LOX-IMVI (line)]] | wt | 220 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.18× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1573 (line)]] | alt | 181 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.3) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.89× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 224 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[SNU-1 (line)]] | wt | 187 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.21× (z +9.0) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SW48 (line)]] | wt | 195 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.42× (z +10.1) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A-427 (line)]] | wt | 286 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[HCT15 (line)]] | alt | 210 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[HepG2_C3A (line)]] | wt | 194 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H2030 (line)]] | alt | 234 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.84× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[RKO (line)]] | wt | 221 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.95× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[SW 900 (line)]] | alt | 159 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[SW1417 (line)]] | alt | 132 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[AN3 CA (line)]] | alt | 288 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 263 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 187 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 141 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 330 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7032), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARN]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[MTOR]] | +0.55 | +0.46 / +0.59 | both halves | 3e-05 | pathway: Dengue Virus-Host Interactions |
| [[CDK11B]] | +0.54 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[RSKR]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[PPM1G]] | +0.53 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ARIH2]] | +0.52 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[KPNB1]] | +0.52 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[EP400]] | +0.51 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[PPP2R3B]] | +0.50 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[ATAD3A]] | +0.50 | +0.29 / +0.49 | both halves | 2e-04 |  |
| [[CDK11A]] | +0.50 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[PNN]] | +0.49 | +0.47 / +0.56 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 418 |

## Genes that move opposite

*31 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP]] | -0.49 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[POLR2M]] | -0.48 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[PLEKHF2]] | -0.48 | -0.23 / -0.43 | both halves | 5e-04 |  |
| [[PGAP4]] | -0.46 | -0.19 / -0.46 | ⚠ not reproduced | 9e-04 |  |
| [[TBPL1]] | -0.46 | -0.29 / -0.29 | both halves | 2e-04 |  |
| [[MAD2L1BP]] | -0.46 | -0.05 / -0.49 | ⚠ not reproduced | 0.005 |  |
| [[TRAPPC2L]] | -0.45 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[CCN3]] | -0.45 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[RIT1]] | -0.45 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[RTCA-AS1]] | -0.45 | -0.23 / -0.24 | both halves | 5e-04 |  |
| [[STBD1]] | -0.44 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[GNA13]] | -0.44 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[LAMTOR3]] | -0.44 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[DIPK2A]] | -0.44 | -0.25 / -0.38 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCN3]] | B | CCN3 activity lowers DDX46's level | lines that do not express CCN3 (20) vs lines expressing it (30) | 1.25× higher at baseline in the lines without CCN3 | 0.019 | ⚠ within organs, on part of the lines; also absent: SNAI2, FAR2, ENSG00000228033 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.464). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-25.1, -42.2); signed map (-19.1, -54.2). **Vector** length 90.5, 32.4% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +3.0 | +15.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.9 | +6.7 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.6 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +2.3 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +2.3 | +14.3 |
|  | [[Trimetrexate (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | +1.7 | +0.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.9 | -4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.0 | -0.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -4.8 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | -3.7 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -1.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[Adenine (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 46 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:134,758,771-134,855,133 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0801, FLJ25329, PRPF5, Prp5 |
| Gene groups (HGNC) | DEAD-box helicases; Spliceosomal A complex |
| Reactome | 13 pathways, smallest: CHD1 and CHD2 subfamily; CHD chromatin remodelers; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L014](https://www.uniprot.org/uniprotkb/Q7L014) (Probable ATP-dependent RNA helicase DDX46):

> Component of the 17S U2 SnRNP complex of the spliceosome, a large ribonucleoprotein complex that removes introns from transcribed pre-mRNAs. The 17S U2 SnRNP complex (1) directly participates in early spliceosome assembly and (2) mediates recognition of the intron branch site during pre-mRNA splicing by promoting the selection of the pre-mRNA branch-site adenosine, the nucleophile for the first step of splicing. Within the 17S U2 SnRNP complex, DDX46 plays essential roles during assembly of …

**Summary**, from NCBI Gene [9879](https://www.ncbi.nlm.nih.gov/gene/9879):

> This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, …

**Accessions** — [HGNC:18681](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18681) · Entrez [9879](https://www.ncbi.nlm.nih.gov/gene/9879) · UniProt [Q7L014](https://www.uniprot.org/uniprotkb/Q7L014) · Ensembl [ENSG00000145833](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145833)

## Data

Gene col 7032: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7032); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7032, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7032]; `tensor/DDL_lfc|DDL_z.npy` [7032]; `embed/gene_vectors.npy` [7032]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7032 or target_col == 7032). Every well: [[DDX46 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX46.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
