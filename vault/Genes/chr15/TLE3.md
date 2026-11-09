---
symbol: "TLE3"
type: "gene"
col: 6392
ensembl_id: "ENSG00000140332"
name: "TLE family member 3, transcriptional corepressor"
location: "15q23"
module: 192
arm: "+"
pooled_cpm: 64.81
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# TLE3

*TLE family member 3, transcriptional corepressor* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +10.3, q 3e-22, up in 29 of 46 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.33× (z +7.0, q 4e-10, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.455× (z -13.2, q 3e-37, down in 31 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.629× (z -4.2, q 0.002, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOX13]] (+0.62, fdr 7e-06), [[CDC42EP4]] (+0.61, fdr 3e-05), [[ZMIZ1]] (+0.58, fdr 3e-05); moves opposite to [[DPY19L4]] (-0.56, fdr 3e-04), [[UHMK1]] (-0.50, fdr 1e-04), [[APOOL]] (-0.49, fdr 5e-05).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6392.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.52×** | +10.3 | 3e-22 | 29/46 (A498, HT-29, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.52×** | +7.0 | 4e-10 | 30/46 (PANC-1, A498, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.0 | 4e-10 | 28/47 (HT-29, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.38×** | +5.4 | 1e-05 | 28/45 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.3 | 1e-05 | 25/46 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.33×** | +5.0 | 5e-05 | 23/46 (A498, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 3e-04 | 23/46 (NCI-H2030, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.26×** | +4.0 | 0.004 | 20/46 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.26×** | +4.0 | 0.004 | 19/46 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.008 | 17/46 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.23×** | +3.6 | 0.015 | 19/46 (SW48, LoVo, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.059 | 20/47 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.1 | 0.089 | 17/43 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6392.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.455×** | -13.2 | 3e-37 | 31/38 (A549, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.525×** | -11.3 | 4e-27 | 34/47 (HOP62, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.577×** | -8.9 | 1e-16 | 31/40 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.741×** | -5.3 | 2e-05 | 25/46 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 0.840× | -4.3 | 0.002 | 20/46 (A498, RKO, …) | rises with dose | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.629×** | -4.2 | 0.002 | 23/46 (Hs 766T, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.844× | -4.2 | 0.002 | 15/46 (LoVo, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.789×** | -4.1 | 0.002 | 22/46 (RKO, Hs 766T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.651×** | -3.9 | 0.005 | 22/46 (LoVo, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.785×** | -3.9 | 0.005 | 17/46 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.658×** | -3.8 | 0.007 | 16/46 (A498, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.662×** | -3.8 | 0.008 | 20/46 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.693×** | -3.4 | 0.034 | 22/46 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.822×** | -3.3 | 0.038 | 18/46 (SW480, SNU-423, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.832×** | -3.1 | 0.072 | 20/45 (A549, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6392. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 92.8 | 3 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +16.9) ⚠ cell-cycle shift, explains ~53% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -11.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 69.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -14.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 92.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -17.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 60.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.63× (z +8.8) ⚠ cell-cycle shift, explains ~45% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 52.7 | 1 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.72× (z +14.7) ⚠ toxic; cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -11.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 104 | 2 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.19× (z +13.3) ⚠ cell-cycle shift, explains ~45% of this change | [[Dinaciclib (drug)]] 5 µM 0.398× (z -10.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 70.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -16.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 37.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.106× (z -16.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 98.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -12.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 68.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +13.5) ⚠ cell-cycle shift, explains ~53% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -8.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 34.1 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0808× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0932× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 51.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.5) ⚠ cell-cycle shift, explains ~53% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -10.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 55.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +15.8) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +12.6) | — |
| [[KATO III (line)]] | alt | 64.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +8.6) | — |
| [[LoVo (line)]] | wt | 86.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -10.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 47.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.9) ⚠ cell-cycle shift, explains ~53% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 85.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.5) ⚠ cell-cycle shift, explains ~53% of this change | [[Dinaciclib (drug)]] 5 µM 0.263× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 49.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.00× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 71.2 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.112× (z -10.6) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 78.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -16.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 73.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -14.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -14.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -9.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[C32 (line)]] | wt | 72.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[COLO 205 (line)]] | alt | 67.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +13.9) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[H4 (line)]] | wt | 65.5 | 0 | 1 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0717× (z -9.6) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 50.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.5) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[Hs 766T (line)]] | wt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 37.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 56.1 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.26× (z +9.0) ⚠ toxic; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 45.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.367× (z -9.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 76.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.2) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SNU-423 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -12.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.36 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6392), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOX13]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 | pathway: Deactivation of the beta-catenin transactivating complex |
| [[CDC42EP4]] | +0.61 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[ZMIZ1]] | +0.58 | +0.46 / +0.54 | both halves | 3e-05 | STRING 471 |
| [[RUNX3]] | +0.58 | +0.44 / +0.61 | both halves | 3e-05 | same gene group; pathway: Formation of the beta-catenin:TCF transactivating complex; STRING 597 |
| [[SEMA4C]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ST3GAL2]] | +0.57 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[VDR]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[FOXA2]] | +0.56 | +0.34 / +0.62 | both halves | 1e-04 | STRING 412 |
| [[ZBTB7A]] | +0.55 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[MIDN]] | +0.55 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[SOX4]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 | pathway: Deactivation of the beta-catenin transactivating complex |
| [[SYNJ2]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L4]] | -0.56 | -0.28 / -0.64 | both halves | 3e-04 |  |
| [[UHMK1]] | -0.50 | -0.34 / -0.53 | both halves | 1e-04 | pathway: ESR-mediated signaling |
| [[APOOL]] | -0.49 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[DNAJC13]] | -0.48 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[CHMP3]] | -0.47 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[VTI1B]] | -0.46 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[RAB11FIP2]] | -0.46 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[EDEM2]] | -0.46 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[PTPN11]] | -0.46 | -0.20 / -0.56 | both halves | 7e-04 |  |
| [[ATPAF1]] | -0.46 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[VAMP7]] | -0.46 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[ARPP19]] | -0.46 | -0.24 / -0.54 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises TLE3's level | compounds that target MAP2K1: 3 of 4 lower it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[PIM2]] | C | PIM2 activity raises TLE3's level | lines that do not express PIM2 (3) vs lines expressing it (47) | 2.40× lower at baseline in the lines without PIM2 | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: JMJD8, CHD7, CYP2R1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.432). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.9, 31.9); signed map (-4.1, 27.0). **Vector** length 118, 30.4% of its response variance represented; |z| ≥ 3 in 1,145 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +3.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.3 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | +4.2 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.0 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.5 | -8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | -11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -13.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -5.0 | -4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.6 | -3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.3 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | TLE family member 3, transcriptional corepressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:70,047,790-70,098,176 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ESG, ESG3, KIAA1547, HsT18976, GRG3 |
| Gene groups (HGNC) | WD repeat domain containing; Wnt enhanceosome complex; TLE family; MicroRNA protein coding host genes |
| Hallmark sets | HEDGEHOG_SIGNALING, G2M_CHECKPOINT |
| Reactome | 12 pathways, smallest: Repression of WNT target genes; Deactivation of the beta-catenin transactivating complex; NOTCH1 Intracellular Domain Regulates Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04726](https://www.uniprot.org/uniprotkb/Q04726) (Transducin-like enhancer protein 3):

> Transcriptional coregulator that binds to a number of transcription factors. Acts as a regulator of adipogenesis both by acting as a corepressor of Wnt signaling and coactivator for PPARG. Inhibits the transcriptional activation mediated by CTNNB1 and TCF family members in Wnt signaling. Promotes diffentiation of white adipocytes by acting as a coactivator for PPARG and preventing the association between PRDM16 and PPARG, thereby preventing browning of white adipocytes (By similarity).

**Summary**, from NCBI Gene [7090](https://www.ncbi.nlm.nih.gov/gene/7090):

> This gene encodes a transcriptional co-repressor protein that belongs to the transducin-like enhancer family of proteins. The members of this family function in the Notch signaling pathway that regulates determination of cell fate during development. Expression of this gene has been associated with a favorable outcome to chemotherapy with taxanes for ovarian carcinoma. Alternate splicing results in multiple transcript variants. Additional alternatively spliced transcript variants of this gene …

**Accessions** — [HGNC:11839](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11839) · Entrez [7090](https://www.ncbi.nlm.nih.gov/gene/7090) · UniProt [Q04726](https://www.uniprot.org/uniprotkb/Q04726) · Ensembl [ENSG00000140332](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140332)

## Data

Gene col 6392: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6392); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6392, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6392]; `tensor/DDL_lfc|DDL_z.npy` [6392]; `embed/gene_vectors.npy` [6392]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6392 or target_col == 6392). Every well: [[TLE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
