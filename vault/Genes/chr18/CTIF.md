---
symbol: "CTIF"
type: "gene"
col: 5500
ensembl_id: "ENSG00000134030"
name: "cap binding complex dependent translation initiation factor"
location: "18q21.1"
module: 211
arm: "+"
pooled_cpm: 103.81
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/211"]
generated_by: "tahoemap"
---

# CTIF

*cap binding complex dependent translation initiation factor* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.35× (z +6.8, q 2e-09, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.486× (z -11.2, q 2e-26, down in 38 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.789× (z -5.4, q 5e-06, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NLN]] (+0.55, fdr 3e-05), [[RHOQ]] (+0.55, fdr 1e-05), [[RUSC2]] (+0.54, fdr 1e-05); moves opposite to [[IFNGR2]] (-0.48, fdr 4e-05), [[PRPF38A]] (-0.48, fdr 4e-05), [[LINC03015]] (-0.47, fdr 8e-05).
> It is in [[Module 211]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LDLRAD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5500.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.8 | 2e-09 | 34/48 (NCI-H2347, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +6.8 | 2e-09 | 38/48 (NCI-H2347, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +6.2 | 8e-08 | 38/48 (NCI-H2347, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +6.1 | 1e-07 | 38/49 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +4.3 | 0.002 | 28/49 (LS 180, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +4.3 | 0.002 | 30/48 (HCT15, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.25×** | +3.4 | 0.056 | 24/48 (SHP-77, BT-474, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +3.3 | 0.058 | 21/48 (NCI-H1573, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.23×** | +3.3 | 0.062 | 22/48 (SHP-77, H4, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.080 | 17/48 (SNU-423, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.23×** | +3.2 | 0.083 | 23/50 (SNU-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5500.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.486×** | -11.2 | 2e-26 | 38/44 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.509×** | -10.1 | 2e-21 | 41/49 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.548×** | -9.4 | 2e-18 | 36/48 (A549, A498, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.552×** | -9.2 | 4e-18 | 39/47 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.560×** | -8.7 | 5e-16 | 36/45 (KATO III, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.759×** | -6.3 | 3e-08 | 29/48 (Panc 03.27, A549, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.789×** | -5.4 | 5e-06 | 29/48 (RKO, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.731×** | -5.1 | 3e-05 | 31/48 (A549, HS-578T, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.740×** | -4.9 | 7e-05 | 27/48 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | **0.763×** | -4.4 | 7e-04 | 26/48 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.757×** | -4.2 | 0.002 | 26/48 (C32, A498, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.615×** | -4.1 | 0.002 | 24/49 (LoVo, SW48, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.839× | -4.0 | 0.003 | 20/49 (A-427, RKO, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | **0.778×** | -3.9 | 0.004 | 25/48 (A498, C32, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.652×** | -3.6 | 0.011 | 20/38 (HEC-1-A, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.825×** | -3.1 | 0.061 | 23/48 (HS-578T, KATO III, …) | all doses, stronger at high dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.824×** | -3.0 | 0.082 | 19/49 (NCI-H1573, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5500. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 179 | 0 | 9 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[PANC-1 (line)]] | alt | 82.1 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 223 | 1 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +13.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 98.3 | 0 | 5 (5 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0490× (z -16.8) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 98.0 | 4 (2 ⚠) | 1 (1 ⚠) | [[Peretinoin (drug)]] 5 µM 2.99× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H460 (line)]] | wt | 369 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A549 (line)]] | wt | 74.1 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -14.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 137 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 76.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H23 (line)]] | alt | 132 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0644× (z -26.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 90.1 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 49.9 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.309× (z -11.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[J82 (line)]] | alt | 142 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.491× (z -11.2) |
| [[KATO III (line)]] | alt | 83.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0463× (z -24.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 175 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.286× (z -11.6) ⚠ toxic |
| [[RKO (line)]] | wt | 227 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.430× (z -12.5) |
| [[SHP-77 (line)]] | alt | 99.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.62× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[Panc 03.27 (line)]] | alt | 61.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -15.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 65.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 87.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[AN3 CA (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0985× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[C32 (line)]] | wt | 65.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.270× (z -9.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[CFPAC-1 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 96.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[COLO 205 (line)]] | alt | 55.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HCT15 (line)]] | alt | 101 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.369× (z -8.5) |
| [[LS 180 (line)]] | wt | 91.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 29.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.20× (z +8.5) | — |
| [[NCI-H661 (line)]] | alt | 50.5 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0667× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 82.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Cytarabine (hydrochloride) (drug)]] 5 µM 0.0754× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW480 (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 91.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 108 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5500), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLN]] | +0.55 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[RHOQ]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[RUSC2]] | +0.54 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[EXOC6B]] | +0.52 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[AGTPBP1]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[MAP4]] | +0.51 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[ERC1]] | +0.50 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[EPS15]] | +0.50 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[KLHL29]] | +0.49 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[CMTM8]] | +0.48 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[GARNL3]] | +0.48 | +0.45 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFNGR2]] | -0.48 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[PRPF38A]] | -0.48 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[LINC03015]] | -0.47 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[CASC9]] | -0.45 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[DPY19L2P2-1]] | -0.45 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[COQ6]] | -0.44 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ZBED8]] | -0.44 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[AMACR]] | -0.43 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[XRCC1]] | -0.42 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[ZC3H7A]] | -0.42 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[PLEKHF2]] | -0.42 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[BCLAF1]] | -0.42 | -0.45 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDLRAD3]] | B | LDLRAD3 activity raises CTIF's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.97× lower at baseline in the lines without LDLRAD3 | 0.045 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 211]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.4, -9.0); signed map (-12.2, 19.2). **Vector** length 109, 33.8% of its response variance represented; |z| ≥ 3 in 1,216 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | +7.1 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.7 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.7 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.6 | +2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.7 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.1 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.8 | -5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.7 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.8 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.5 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.6 | -5.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.9 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -3.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.0 | +0.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.9 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | cap binding complex dependent translation initiation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:48,539,031-48,863,217 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0427 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; MIF4G domain containing proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O43310](https://www.uniprot.org/uniprotkb/O43310) (CBP80/20-dependent translation initiation factor):

> Specifically required for the pioneer round of mRNA translation mediated by the cap-binding complex (CBC), that takes place during or right after mRNA export via the nuclear pore complex (NPC). Acts via its interaction with the NCBP1/CBP80 component of the CBC complex and recruits the 40S small subunit of the ribosome via eIF3. In contrast, it is not involved in steady state translation, that takes place when the CBC complex is replaced by cytoplasmic cap-binding protein eIF4E. Also required …

**Summary**, from NCBI Gene [9811](https://www.ncbi.nlm.nih.gov/gene/9811):

> CTIF is a component of the CBP80 (NCBP1; MIM 600469)/CBP20 (NCBP2; MIM 605133) translation initiation complex that binds cotranscriptionally to the cap end of nascent mRNA. The CBP80/CBP20 complex is involved in a simultaneous editing and translation step that recognizes premature termination codons (PTCs) in mRNAs and directs PTC-containing mRNAs toward nonsense-mediated decay (NMD). On mRNAs without PTCs, the CBP80/CBP20 complex is replaced with cytoplasmic mRNA cap-binding proteins, …

**Accessions** — [HGNC:23925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23925) · Entrez [9811](https://www.ncbi.nlm.nih.gov/gene/9811) · UniProt [O43310](https://www.uniprot.org/uniprotkb/O43310) · Ensembl [ENSG00000134030](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134030)

## Data

Gene col 5500: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5500); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5500, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5500]; `tensor/DDL_lfc|DDL_z.npy` [5500]; `embed/gene_vectors.npy` [5500]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5500 or target_col == 5500). Every well: [[CTIF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTIF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
