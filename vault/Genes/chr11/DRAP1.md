---
symbol: "DRAP1"
type: "gene"
col: 10620
ensembl_id: "ENSG00000175550"
name: "DR1 associated protein 1"
location: "11q13.1"
module: 206
arm: "+"
pooled_cpm: 72.7
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# DRAP1

*DR1 associated protein 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.85× (z +11.3, q 6e-27, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~59% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +4.8, q 1e-04, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.670× (z -4.3, q 0.008, down in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 0.386× (z -3.8, q 0.027, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGA1]] (+0.66, fdr 7e-06), [[STK10]] (+0.65, fdr 7e-06), [[N4BP3]] (+0.63, fdr 1e-05); moves opposite to [[TRMT11]] (-0.61, fdr 1e-05), [[RAVER2]] (-0.57, fdr 1e-05), [[PON2]] (-0.55, fdr 1e-05).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FRMD6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 14 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **2.85×** | +11.3 | 6e-27 | 40/48 (LOX-IMVI, SNU-423, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **4.63×** | +9.9 | 1e-20 | 46/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **3.82×** | +9.8 | 1e-20 | 39/39 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.89×** | +7.5 | 9e-12 | 41/43 (SNU-423, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.02×** | +5.4 | 1e-05 | 35/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **1.98×** | +5.2 | 2e-05 | 43/47 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.87×** | +4.8 | 1e-04 | 41/48 (NCI-H1573, AsPC-1, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.8 | 1e-04 | 34/48 (NCI-H1573, A549, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.89×** | +4.7 | 2e-04 | 32/48 (NCI-H460, LOX-IMVI, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.83×** | +4.6 | 2e-04 | 43/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.77×** | +4.4 | 7e-04 | 36/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +4.3 | 1e-03 | 31/48 (SW480, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.69×** | +4.0 | 0.003 | 34/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.65×** | +3.7 | 0.010 | 33/48 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.6 | 0.013 | 30/47 (CFPAC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10620.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.670×** | -4.3 | 0.008 | 45/48 (A-427, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.702×** | -3.8 | 0.027 | 32/48 (SW1417, LS 180, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.386×** | -3.8 | 0.027 | 38/47 (RKO, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.408×** | -3.6 | 0.047 | 38/48 (Hs 766T, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.592×** | -3.5 | 0.057 | 30/48 (AsPC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.648×** | -3.3 | 0.079 | 41/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.650×** | -3.3 | 0.079 | 29/48 (HOP62, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.641×** | -3.2 | 0.092 | 30/47 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.662×** | -3.2 | 0.099 | 31/48 (Panc 03.27, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.743× | -3.1 | 0.10 | 34/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.462× | -3.1 | 0.10 | 36/48 (H4, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.79 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.6 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.16× (z +17.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 7.95× (z +12.4) | — |
| [[A549 (line)]] | wt | 50.5 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +16.5) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 72.4 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +19.3) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[NCI-H1573 (line)]] | alt | 51.4 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +14.1) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 76.8 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +17.7) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[HOP62 (line)]] | alt | 75.1 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +14.8) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[HS-578T (line)]] | alt | 110 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +14.5) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[NCI-H1792 (line)]] | alt | 32.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +9.7) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[SNU-423 (line)]] | alt | 73.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.61× (z +17.9) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[A-172 (line)]] | wt | 87.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +16.4) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[AsPC-1 (line)]] | alt | 102 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +12.1) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[H4 (line)]] | wt | 69.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +10.2) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[KATO III (line)]] | alt | 46.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.08× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[PANC-1 (line)]] | alt | 203 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.62× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SW 1271 (line)]] | alt | 50.2 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +9.2) ⚠ cell-cycle shift, explains ~59% of this change | [[Tolmetin (drug)]] 5 µM 0.0494× (z -8.8) |
| [[SW 900 (line)]] | alt | 66.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +10.6) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[SW480 (line)]] | alt | 48.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-427 (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.0) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[AN3 CA (line)]] | alt | 52.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +9.1) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[C32 (line)]] | wt | 52.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +10.7) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[CFPAC-1 (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +12.5) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[CHP-212 (line)]] | wt | 29.4 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM 0.0509× (z -8.8) |
| [[COLO 205 (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +10.8) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[HCT15 (line)]] | alt | 39.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.87× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[HepG2_C3A (line)]] | wt | 31.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +10.9) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[Hs 766T (line)]] | wt | 97.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +13.7) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 79.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.41× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LoVo (line)]] | wt | 27.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +10.0) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[NCI-H23 (line)]] | alt | 57.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[Panc 03.27 (line)]] | alt | 99.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.4) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[RPMI-7951 (line)]] | alt | 93.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +14.2) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[SW48 (line)]] | wt | 51.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +10.2) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[A498 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 111 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 68.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGA1]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[STK10]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[N4BP3]] | +0.63 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PDLIM7]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[SMS]] | +0.61 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ZSWIM4]] | +0.58 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[SRSF9]] ⚠ | +0.58 | +0.50 / +0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DPF3]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[MYL12A]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[MEAK7]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[HIVEP3]] | +0.56 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[PIK3CD]] | +0.56 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[ADGRL1-AS1]] | +0.56 | +0.52 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT11]] | -0.61 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[RAVER2]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[PON2]] | -0.55 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[CIAO2A]] | -0.53 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[SPR]] | -0.53 | -0.53 / -0.29 | both halves | 3e-04 |  |
| [[PLBD1]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[FUCA2]] | -0.52 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[METTL25]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[MFSD14A]] | -0.51 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[PHB2]] | -0.51 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[ZNF148]] | -0.51 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[ZZZ3]] | -0.51 | -0.46 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD6]] | B | FRMD6 activity raises DRAP1's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without FRMD6 | 0.085 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.8, -1.6); signed map (-1.7, 43.1). **Vector** length 81.9, 32.0% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +6.2 | +11.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.7 | +5.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.6 | +1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | -0.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.2 | -3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.4 | +3.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -1.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.3 | -0.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | DR1 associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,919,274-65,921,563 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NC2-alpha |
| Reactome | 3 pathways, smallest: Signaling by NODAL; Signaling by Activin; Signaling by TGFB family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14919](https://www.uniprot.org/uniprotkb/Q14919) (Dr1-associated corepressor):

> The association of the DR1/DRAP1 heterodimer with TBP results in a functional repression of both activated and basal transcription of class II genes. This interaction precludes the formation of a transcription-competent complex by inhibiting the association of TFIIA and/or TFIIB with TBP. Can bind to DNA on its own.

**Summary**, from NCBI Gene [10589](https://www.ncbi.nlm.nih.gov/gene/10589):

> Transcriptional repression is a general mechanism for regulating transcriptional initiation in organisms ranging from yeast to humans. Accurate initiation of transcription from eukaryotic protein-encoding genes requires the assembly of a large multiprotein complex consisting of RNA polymerase II and general transcription factors such as TFIIA, TFIIB, and TFIID. DR1 is a repressor that interacts with the TATA-binding protein (TBP) of TFIID and prevents the formation of an active transcription …

**Accessions** — [HGNC:3019](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3019) · Entrez [10589](https://www.ncbi.nlm.nih.gov/gene/10589) · UniProt [Q14919](https://www.uniprot.org/uniprotkb/Q14919) · Ensembl [ENSG00000175550](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175550)

## Data

Gene col 10620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10620); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10620]; `tensor/DDL_lfc|DDL_z.npy` [10620]; `embed/gene_vectors.npy` [10620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10620 or target_col == 10620). Every well: [[DRAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DRAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
