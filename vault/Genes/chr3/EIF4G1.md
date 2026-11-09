---
symbol: "EIF4G1"
type: "gene"
col: 3599
ensembl_id: "ENSG00000114867"
name: "eukaryotic translation initiation factor 4 gamma 1"
location: "3q27.1"
module: 4
arm: "+"
pooled_cpm: 218.86
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# EIF4G1

*eukaryotic translation initiation factor 4 gamma 1* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.27× (z +14.2, q 3e-43, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.63× (z +8.5, q 2e-15, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.793× (z -3.9, q 0.054, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOLC1]] (+0.77, fdr 7e-06), [[PSME3]] (+0.75, fdr 7e-06), [[EIF2S1]] (+0.75, fdr 7e-06); moves opposite to [[DCTN6-DT]] (-0.75, fdr 7e-06), [[RPS29]] (-0.71, fdr 7e-06), [[SNHG25]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ME3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3599.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.27×** | +14.2 | 3e-43 | 49/49 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.07×** | +12.2 | 7e-32 | 41/44 (A498, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.47×** | +9.5 | 5e-19 | 36/48 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.77×** | +9.2 | 7e-18 | 41/45 (A498, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +8.5 | 2e-15 | 40/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.47×** | +8.2 | 1e-14 | 45/48 (RKO, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +7.9 | 1e-13 | 47/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +7.9 | 1e-13 | 47/49 (COLO 205, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.57×** | +7.6 | 2e-12 | 41/47 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +7.2 | 4e-11 | 39/48 (SW480, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +6.3 | 2e-08 | 40/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.40×** | +5.9 | 2e-07 | 37/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.81×** | +5.4 | 3e-06 | 40/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.35×** | +5.3 | 5e-06 | 34/48 (AsPC-1, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.36×** | +5.2 | 8e-06 | 31/48 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.2 | 8e-06 | 33/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.72×** | +4.9 | 2e-05 | 42/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +4.8 | 6e-05 | 33/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.63×** | +4.5 | 2e-04 | 41/48 (NCI-H460, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.63×** | +4.4 | 2e-04 | 38/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.001 | 28/48 (NCI-H1573, MIA PaCa-2, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.003 | 20/48 (MIA PaCa-2, NCI-H1573, …) | top dose only |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.004 | 11/48 (NCI-H2030, SW480, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.035 | 26/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3599.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.793×** | -3.9 | 0.054 | 31/49 (J82, SW 1271, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.813×** | -3.6 | 0.081 | 29/48 (KATO III, A-427, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.755×** | -3.5 | 0.084 | 30/48 (SHP-77, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.825× | -3.4 | 0.11 | 26/49 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.877× | -3.3 | 0.13 | 13/48 (HT-29, LOX-IMVI, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.838× | -3.1 | 0.19 | 20/48 (KATO III, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3599. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 102 | 10 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.89× (z +15.0) | — |
| [[A549 (line)]] | wt | 108 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 128 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +9.4) | — |
| [[C32 (line)]] | wt | 148 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.8) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +10.0) | [[Cobimetinib (drug)]] 0.05 µM 0.389× (z -9.8) |
| [[HS-578T (line)]] | alt | 237 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.5) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.21× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 259 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +11.5) | — |
| [[RPMI-7951 (line)]] | alt | 202 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +10.4) | — |
| [[A-172 (line)]] | wt | 196 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.06× (z +9.5) | — |
| [[A498 (line)]] | wt | 308 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[CFPAC-1 (line)]] | alt | 136 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 172 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.5) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.68× (z +10.3) | — |
| [[HepG2_C3A (line)]] | wt | 146 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.3) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[HOP62 (line)]] | alt | 175 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +13.3) | — |
| [[LOX-IMVI (line)]] | wt | 210 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 330 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.30× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 190 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 133 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW480 (line)]] | alt | 211 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.01× (z +9.7) | — |
| [[H4 (line)]] | wt | 237 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.0) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[J82 (line)]] | alt | 353 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 294 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.1) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.92× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 130 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +10.5) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.29× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 136 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HT-29 (line)]] | alt | 215 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 187 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LS 180 (line)]] | wt | 200 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2030 (line)]] | alt | 220 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 287 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW 900 (line)]] | alt | 156 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[AN3 CA (line)]] | alt | 207 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.22× (z +9.4) | — |
| [[KATO III (line)]] | alt | 262 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 235 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2347 (line)]] | alt | 253 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RKO (line)]] | wt | 229 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.96× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 179 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW1417 (line)]] | alt | 221 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.03× (z +8.9) ⚠ unreliable plate only | — |
| [[A-427 (line)]] | wt | 454 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 242 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 169 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 239 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 181 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 288 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3599), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOLC1]] | +0.77 | +0.80 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 418 |
| [[PSME3]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[EIF2S1]] | +0.75 | +0.72 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 986 |
| [[VARS1]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[WDR77]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.74 | +0.70 / +0.75 | both halves | 7e-06 | STRING 475 |
| [[GRWD1]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 | STRING 410 |
| [[SYNCRIP]] | +0.73 | +0.68 / +0.75 | both halves | 7e-06 | STRING 758 |
| [[PUF60]] | +0.72 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[IPO4]] | +0.72 | +0.72 / +0.69 | both halves | 7e-06 | STRING 431 |
| [[EBNA1BP2]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[MAK16]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN6-DT]] | -0.75 | -0.69 / -0.73 | both halves | 7e-06 |  |
| [[RPS29]] | -0.71 | -0.67 / -0.68 | both halves | 7e-06 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 856 |
| [[SNHG25]] | -0.71 | -0.67 / -0.70 | both halves | 7e-06 |  |
| [[CNNM2]] | -0.70 | -0.66 / -0.70 | both halves | 7e-06 |  |
| [[GABARAPL2]] | -0.70 | -0.58 / -0.71 | both halves | 8e-06 |  |
| [[DPM3]] | -0.70 | -0.64 / -0.67 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication |
| [[COMMD6]] | -0.69 | -0.68 / -0.66 | both halves | 7e-06 |  |
| [[RNF181]] | -0.69 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[UQCRB]] ⚠ | -0.69 | -0.63 / -0.67 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | -0.68 | -0.62 / -0.65 | both halves | 7e-06 | pathway: MTOR signalling |
| [[LMBR1L]] | -0.68 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[LIN7B]] | -0.68 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[SIRT2]] | -0.68 | -0.59 / -0.69 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ME3]] | B | ME3 activity lowers EIF4G1's level | lines that do not express ME3 (13) vs lines expressing it (37) | 1.27× higher at baseline in the lines without ME3 | 0.044 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[PRR5L]] | B | PRR5L activity lowers EIF4G1's level | lines that do not express PRR5L (10) vs lines expressing it (40) | 1.14× higher at baseline in the lines without PRR5L | 0.053 | ⚠ within organs, on part of the lines; also absent: RASA3, DUSP5-DT, HOXA13; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.680). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.7, -33.2); signed map (-6.7, -44.2). **Vector** length 135, 52.7% of its response variance represented; |z| ≥ 3 in 1,447 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.51 to 21); *Folding of actin by CCT/TriC* (reactome, mean cos +0.58 to 4); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +7.7 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +6.7 | +9.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.7 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +6.5 | +14.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +7.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.7 | +2.2 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -4.8 | -3.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | -4.8 | +3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.2 | -3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4 gamma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:184,314,495-184,335,358 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p220, PARK18; previously EIF4G, EIF4F |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; MIF4G domain containing proteins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 32 pathways, smallest: Z-decay: degradation of maternal mRNAs by zygotically expressed factors; mTORC1-mediated signalling; Deadenylation of mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04637](https://www.uniprot.org/uniprotkb/Q04637) (Eukaryotic translation initiation factor 4 gamma 1):

> Component of the protein complex eIF4F, which is involved in the recognition of the mRNA cap, ATP-dependent unwinding of 5'-terminal secondary structure and recruitment of mRNA to the ribosome. Exists in two complexes, either with EIF1 or with EIF4E (mutually exclusive). Together with EIF1, is required for leaky scanning, in particular for avoiding cap-proximal start codon. Together with EIF4E, antagonizes the scanning promoted by EIF1-EIF4G1 and locates the start codon (through a TISU element) …

**Summary**, from NCBI Gene [1981](https://www.ncbi.nlm.nih.gov/gene/1981):

> The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by this gene is a large scaffolding protein that contains binding sites for other members of the …

**Accessions** — [HGNC:3296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3296) · Entrez [1981](https://www.ncbi.nlm.nih.gov/gene/1981) · UniProt [Q04637](https://www.uniprot.org/uniprotkb/Q04637) · Ensembl [ENSG00000114867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114867)

## Data

Gene col 3599: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3599); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3599, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3599]; `tensor/DDL_lfc|DDL_z.npy` [3599]; `embed/gene_vectors.npy` [3599]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3599 or target_col == 3599). Every well: [[EIF4G1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4G1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
