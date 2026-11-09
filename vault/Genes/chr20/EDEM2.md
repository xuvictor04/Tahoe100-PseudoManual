---
symbol: "EDEM2"
type: "gene"
col: 1526
ensembl_id: "ENSG00000088298"
name: "ER degradation enhancing alpha-mannosidase like protein 2"
location: "20q11.22"
module: 65
arm: "+"
pooled_cpm: 19.23
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# EDEM2

*ER degradation enhancing alpha-mannosidase like protein 2* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.49× (z +6.3, q 1e-07, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.365× (z -22.5, q 0e+00, down in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.802× (z -4.9, q 6e-05, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRS2]] (+0.65, fdr 1e-05), [[PLA2G12A]] (+0.64, fdr 1e-05), [[RTCA]] (+0.64, fdr 7e-06); moves opposite to [[HIVEP1]] (-0.60, fdr 2e-05), [[ERF]] (-0.58, fdr 3e-05), [[ZHX2]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +6.3 | 1e-07 | 25/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +5.8 | 2e-06 | 26/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +5.5 | 9e-06 | 25/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.21×** | +4.3 | 0.002 | 13/48 (AsPC-1, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.21×** | +4.2 | 0.002 | 19/48 (A-427, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +4.2 | 0.002 | 19/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +3.6 | 0.023 | 13/47 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.095 | 14/48 (A-427, KATO III, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.44× | +3.1 | 0.14 | 9/46 (BT-474, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.14 | 9/48 (SW480, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1526.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.365×** | -22.5 | 0e+00 | 42/47 (NCI-H1792, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.432×** | -13.2 | 1e-37 | 41/48 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.453×** | -12.5 | 1e-33 | 38/47 (SW480, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.525×** | -9.8 | 2e-20 | 34/47 (HS-578T, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.610×** | -7.8 | 7e-13 | 31/48 (SW480, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.621×** | -7.5 | 6e-12 | 32/47 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.636×** | -7.1 | 8e-11 | 30/47 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.629×** | -7.0 | 1e-10 | 30/43 (SW48, BT-474, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -5.4 | 4e-06 | 6/48 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -4.9 | 6e-05 | 26/47 (BT-474, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.581×** | -4.5 | 4e-04 | 19/48 (BT-474, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.754×** | -4.4 | 4e-04 | 18/41 (C32, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.774×** | -3.7 | 0.009 | 18/37 (NCI-H2030, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.815×** | -3.2 | 0.054 | 16/48 (KATO III, Hs 766T, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.680×** | -3.2 | 0.054 | 11/45 (J82, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.823×** | -3.0 | 0.078 | 9/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 59.2 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -9.7) |
| [[SW480 (line)]] | alt | 21.7 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.232× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 14.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -12.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HS-578T (line)]] | alt | 16.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0321× (z -21.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HEC-1-A (line)]] | alt | 16.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -14.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 42.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -14.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AsPC-1 (line)]] | alt | 10.4 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.108× (z -11.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 13.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0929× (z -11.7) |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 2 (1 ⚠) | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0762× (z -11.2) |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -10.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Hs 766T (line)]] | wt | 39.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -12.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HT-29 (line)]] | alt | 22.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0678× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 22.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -17.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H23 (line)]] | alt | 30.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[NCI-H460 (line)]] | wt | 17.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -13.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW48 (line)]] | wt | 14.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0537× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0781× (z -9.1) |
| [[A-427 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[A498 (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -11.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -14.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[CFPAC-1 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[COLO 205 (line)]] | alt | 29.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -9.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[H4 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.117× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -11.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[J82 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -15.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -8.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H2030 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -8.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -11.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RKO (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -8.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -15.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRS2]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PLA2G12A]] | +0.64 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[RTCA]] | +0.64 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.64 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[ALG9]] | +0.64 | +0.70 / +0.48 | both halves | 2e-05 | pathway: Asparagine N-linked glycosylation |
| [[MFSD9]] | +0.63 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[VPS33B]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[TMEM182]] | +0.63 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[MBD2]] | +0.62 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[MINDY3]] | +0.62 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[JKAMP]] | +0.62 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ZDHHC16]] | +0.61 | +0.60 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP1]] | -0.60 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[ERF]] | -0.58 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[ZHX2]] | -0.57 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[NFATC1]] | -0.56 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[CUX1]] | -0.56 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[NR2F1-AS1]] | -0.55 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[TSC22D1]] | -0.55 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[BAZ2B]] | -0.55 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[SON]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[NLGN3]] | -0.55 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[ZNF335]] | -0.55 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[KDSR]] | -0.54 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers EDEM2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.651). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-4.4, -11.4); signed map (-32.3, -12.5). **Vector** length 80.6, 15.8% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.0 | +6.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.8 | +2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.5 | -22.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -3.5 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.1 | -7.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -1.6 | -0.9 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ER degradation enhancing alpha-mannosidase like protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:35,115,364-35,147,336 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10783, bA4204.1; previously C20orf49, C20orf31 |
| Gene groups (HGNC) | Mannosidases alpha class 1 |
| Reactome | 10 pathways, smallest: ER Quality Control Compartment (ERQC); Calnexin/calreticulin cycle; N-glycan trimming in the ER and Calnexin/Calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BV94](https://www.uniprot.org/uniprotkb/Q9BV94) (ER degradation-enhancing alpha-mannosidase-like protein 2):

> Involved in the endoplasmic reticulum-associated degradation (ERAD) pathway that targets misfolded glycoproteins for degradation in an N-glycan-dependent manner. May initiate ERAD by promoting the first mannose trimming step of ERAD substrates, from Man9GlcNAc2 to Man8GlcNAc2. Seems to recognize and bind to exposed hydrophobic regions in target proteins (By similarity).

**Summary**, from NCBI Gene [55741](https://www.ncbi.nlm.nih.gov/gene/55741):

> In the endoplasmic reticulum (ER), misfolded proteins are retrotranslocated to the cytosol and degraded by the proteasome in a process known as ER-associated degradation (ERAD). EDEM2 belongs to a family of proteins involved in ERAD of glycoproteins (Mast et al., 2005 [PubMed 15537790]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:15877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15877) · Entrez [55741](https://www.ncbi.nlm.nih.gov/gene/55741) · UniProt [Q9BV94](https://www.uniprot.org/uniprotkb/Q9BV94) · Ensembl [ENSG00000088298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088298)

## Data

Gene col 1526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1526); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1526]; `tensor/DDL_lfc|DDL_z.npy` [1526]; `embed/gene_vectors.npy` [1526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1526 or target_col == 1526). Every well: [[EDEM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDEM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
