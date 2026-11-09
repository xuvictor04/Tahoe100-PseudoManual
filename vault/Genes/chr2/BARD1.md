---
symbol: "BARD1"
type: "gene"
col: 6161
ensembl_id: "ENSG00000138376"
name: "BRCA1 associated RING domain 1"
location: "2q35"
module: 67
arm: "+"
pooled_cpm: 72.48
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 29
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# BARD1

*BRCA1 associated RING domain 1* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.47× (z +7.2, q 3e-10, up in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~71% of this change. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 1.54× (z +4.2, q 0.002, up in 19 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H23 2.66×; ⚠ cell-cycle shift, explains ~65% of this change).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.644× (z -11.6, q 2e-28, down in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.645× (z -11.5, q 2e-28, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MELK]] (+0.88, fdr 7e-06), [[STIL]] (+0.86, fdr 7e-06), [[BLM]] (+0.85, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6161.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H23 2.66×; ⚠ cell-cycle shift, explains ~65% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.47×** | +7.2 | 3e-10 | 35/48 (hTERT-HPNE, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.37×** | +5.9 | 1e-06 | 27/48 (NCI-H23, H4, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.35×** | +5.6 | 5e-06 | 28/48 (NCI-H23, H4, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.33×** | +5.3 | 1e-05 | 26/48 (NCI-H23, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.29×** | +4.8 | 2e-04 | 20/48 (HT-29, hTERT-HPNE, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | **1.26×** | +4.3 | 0.002 | 23/47 (NCI-H23, H4, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +4.2 | 0.002 | 19/49 (LoVo, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.25×** | +4.2 | 0.002 | 23/47 (H4, NCI-H23, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.17× | +4.1 | 0.003 | 15/48 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.24×** | +4.0 | 0.004 | 20/48 (RKO, SW1417, …) | all doses, flat |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.15× | +3.8 | 0.008 | 14/48 (SW48, RKO, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.023 | 12/48 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.20×** | +3.4 | 0.029 | 15/48 (HT-29, SW1417, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.14× | +3.4 | 0.032 | 14/49 (HT-29, LS 180, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.18× | +3.1 | 0.070 | 12/48 (SW48, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6161.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.644×** | -11.6 | 2e-28 | 37/48 (A-172, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.645×** | -11.5 | 2e-28 | 33/48 (NCI-H1573, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.541×** | -11.5 | 4e-28 | 43/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.579×** | -10.2 | 4e-22 | 34/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.622×** | -8.4 | 7e-15 | 29/48 (SW48, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.657×** | -7.8 | 5e-13 | 33/48 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -6.8 | 7e-10 | 25/42 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.746×** | -5.5 | 3e-06 | 26/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.818×** | -5.3 | 8e-06 | 22/48 (HEC-1-A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.756×** | -5.2 | 1e-05 | 25/48 (SW48, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.595×** | -5.1 | 2e-05 | 28/46 (Panc 03.27, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.764×** | -5.0 | 3e-05 | 27/49 (J82, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.830×** | -4.9 | 4e-05 | 24/48 (A-427, A498, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.772×** | -4.8 | 6e-05 | 25/48 (SNU-1, Hs 766T, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.780×** | -4.6 | 1e-04 | 20/49 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.680×** | -3.8 | 0.005 | 22/49 (AsPC-1, SHP-77, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.820×** | -3.7 | 0.007 | 18/48 (KATO III, SHP-77, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.821×** | -3.7 | 0.007 | 17/48 (SW 1088, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.823×** | -3.6 | 0.008 | 21/48 (NCI-H1573, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 0.872× | -3.6 | 0.008 | 15/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.826×** | -3.6 | 0.009 | 19/47 (RKO, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6161. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 76.1 | 0 | 8 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.201× (z -17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.277× (z -10.1) |
| [[A498 (line)]] | wt | 73.2 | 0 | 6 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.302× (z -12.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 139 | 0 | 5 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.271× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 85.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -21.8) |
| [[NCI-H23 (line)]] | alt | 81.3 | 1 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +9.5) ⚠ cell-cycle shift, explains ~65% of this change | [[Dinaciclib (drug)]] 5 µM 0.147× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -10.3) |
| [[A-427 (line)]] | wt | 89.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.466× (z -9.8) |
| [[J82 (line)]] | alt | 166 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -8.9) |
| [[H4 (line)]] | wt | 55.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -13.1) |
| [[Hs 766T (line)]] | wt | 47.1 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.356× (z -11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.371× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 76.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -18.2) |
| [[SW48 (line)]] | wt | 57.3 | 0 | 3 | — | [[Bortezomib (drug)]] 0.05 µM 0.186× (z -10.9) |
| [[SW480 (line)]] | alt | 78.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -11.0) |
| [[AN3 CA (line)]] | alt | 100 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 61.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -8.8) |
| [[C-33 A (line)]] | alt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -8.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 95.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.361× (z -12.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.337× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 61.0 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.189× (z -11.4) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 89.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.417× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.453× (z -11.3) |
| [[LS 180 (line)]] | wt | 42.1 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.333× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.297× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 61.3 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.480× (z -9.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.401× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 82.2 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.337× (z -10.7) |
| [[COLO 205 (line)]] | alt | 46.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -11.3) |
| [[LoVo (line)]] | wt | 43.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -12.0) |
| [[NCI-H661 (line)]] | alt | 59.6 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0700× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 63.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.438× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 77.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.369× (z -9.6) |
| [[SNU-1 (line)]] | wt | 56.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.218× (z -12.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 80.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6161), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MELK]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[STIL]] | +0.86 | +0.82 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[BLM]] | +0.85 | +0.83 / +0.82 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 718 |
| [[SPC24]] | +0.84 | +0.82 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[TICRR]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[EXO1]] | +0.84 | +0.79 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 858 |
| [[NCAPD3]] | +0.84 | +0.79 / +0.83 | both halves | 7e-06 |  |
| [[DTL]] | +0.84 | +0.80 / +0.85 | both halves | 7e-06 |  |
| [[PBK]] | +0.84 | +0.84 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[ATAD2]] | +0.83 | +0.77 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[POLQ]] | +0.83 | +0.78 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[UBE2T]] | +0.83 | +0.80 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 655 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers BARD1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.867). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.3, -50.4); signed map (-43.1, -40.6). **Vector** length 152, 50.7% of its response variance represented; |z| ≥ 3 in 1,309 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.73 to 8); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.72 to 4); *Nucleosome assembly* (reactome, mean cos +0.72 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +6.2 | +7.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +5.0 | +5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.9 | +5.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | +4.7 | +4.2 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.5 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +4.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.6 | +1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.5 | +1.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +1.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -11.4 | -11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.2 | -10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.5 | -11.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -8.3 | -7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -5.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.7 | -2.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -3.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | BRCA1 associated RING domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:214,725,646-214,809,683 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ring finger proteins; Ankyrin repeat domain containing; BRCA1 B complex; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | KRAS_SIGNALING_DN, G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 35 pathways, smallest: Impaired BRCA2 binding to PALB2; Metalloprotease DUBs; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99728](https://www.uniprot.org/uniprotkb/Q99728) (BRCA1-associated RING domain protein 1):

> E3 ubiquitin-protein ligase. The BRCA1-BARD1 heterodimer specifically mediates the formation of 'Lys-6'-linked polyubiquitin chains and coordinates a diverse range of cellular pathways such as DNA damage repair, ubiquitination and transcriptional regulation to maintain genomic stability. Plays a central role in the control of the cell cycle in response to DNA damage. Acts by mediating ubiquitin E3 ligase activity that is required for its tumor suppressor function. Also forms a heterodimer with …

**Summary**, from NCBI Gene [580](https://www.ncbi.nlm.nih.gov/gene/580):

> This gene encodes a protein which interacts with the N-terminal region of BRCA1. In addition to its ability to bind BRCA1 in vivo and in vitro, it shares homology with the 2 most conserved regions of BRCA1: the N-terminal RING motif and the C-terminal BRCT domain. The RING motif is a cysteine-rich sequence found in a variety of proteins that regulate cell growth, including the products of tumor suppressor genes and dominant protooncogenes. This protein also contains 3 tandem ankyrin repeats. …

**Accessions** — [HGNC:952](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:952) · Entrez [580](https://www.ncbi.nlm.nih.gov/gene/580) · UniProt [Q99728](https://www.uniprot.org/uniprotkb/Q99728) · Ensembl [ENSG00000138376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138376)

## Data

Gene col 6161: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6161); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6161, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6161]; `tensor/DDL_lfc|DDL_z.npy` [6161]; `embed/gene_vectors.npy` [6161]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6161 or target_col == 6161). Every well: [[BARD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BARD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
