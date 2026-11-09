---
symbol: "RUFY2"
type: "gene"
col: 12816
ensembl_id: "ENSG00000204130"
name: "RUN and FYVE domain containing 2"
location: "10q21.3"
module: 30
arm: "+"
pooled_cpm: 94.35
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# RUFY2

*RUN and FYVE domain containing 2* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.52× (z +9.5, q 1e-18, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.579× (z -12.4, q 1e-32, down in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.726× (z -7.3, q 2e-11, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYZL1]] (+0.71, fdr 7e-06), [[ABCD4]] (+0.68, fdr 7e-06), [[RTCA]] (+0.68, fdr 7e-06); moves opposite to [[FAT1]] (-0.64, fdr 7e-06), [[CSRNP1]] (-0.60, fdr 1e-05), [[CFL1]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12816.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +9.5 | 1e-18 | 42/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +7.8 | 1e-12 | 41/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +6.4 | 4e-08 | 30/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.005 | 25/49 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.1 | 0.006 | 22/45 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.2 | 0.11 | 10/49 (A-427, HT-29, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.2 | 0.11 | 3/48 (BT-474, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 1.15× | +3.2 | 0.11 | 15/48 (SNU-1, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 21 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12816.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.579×** | -12.4 | 1e-32 | 47/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.612×** | -11.2 | 2e-26 | 43/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.751×** | -8.8 | 2e-16 | 31/49 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.696×** | -7.6 | 4e-12 | 32/45 (RKO, A-172, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.719×** | -7.5 | 7e-12 | 35/48 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.786×** | -7.4 | 1e-11 | 24/48 (SNU-423, CFPAC-1, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.726×** | -7.3 | 2e-11 | 31/48 (A-172, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -7.1 | 1e-10 | 33/48 (A-172, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.726×** | -7.0 | 1e-10 | 25/44 (HCT15, CFPAC-1, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.805×** | -6.8 | 7e-10 | 26/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.735×** | -6.7 | 8e-10 | 35/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.751×** | -6.5 | 4e-09 | 35/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | **0.755×** | -6.4 | 7e-09 | 31/49 (SNU-1, A549, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.794×** | -5.0 | 2e-05 | 28/50 (HOP62, Hs 766T, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.679×** | -4.6 | 2e-04 | 22/49 (SK-MEL-2, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.842× | -3.9 | 0.003 | 16/48 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.859× | -3.2 | 0.033 | 18/47 (HEC-1-A, SNU-1, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **0.781×** | -2.9 | 0.068 | 20/47 (SW 1088, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12816. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 108 | 0 | 10 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.410× (z -13.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.534× (z -9.4) |
| [[A-172 (line)]] | wt | 170 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -16.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.485× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 111 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -13.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.621× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 111 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -13.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.494× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 95.5 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.437× (z -11.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.638× (z -8.9) |
| [[SNU-423 (line)]] | alt | 160 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -16.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 125 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.391× (z -11.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HCT15 (line)]] | alt | 123 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[Hs 766T (line)]] | wt | 118 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.442× (z -10.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H460 (line)]] | wt | 109 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -13.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[PANC-1 (line)]] | alt | 105 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.83× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.604× (z -8.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HEC-1-A (line)]] | alt | 108 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.487× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.516× (z -8.6) |
| [[HS-578T (line)]] | alt | 83.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -10.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[hTERT-HPNE (line)]] | wt | 91.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0853× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[SW480 (line)]] | alt | 89.9 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.80× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.564× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[A-427 (line)]] | wt | 96.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.509× (z -9.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 78.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.501× (z -9.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[AsPC-1 (line)]] | alt | 85.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.455× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[C-33 A (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -10.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[H4 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.397× (z -8.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[J82 (line)]] | alt | 68.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.511× (z -8.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[LOX-IMVI (line)]] | wt | 81.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[NCI-H1792 (line)]] | alt | 85.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.488× (z -8.5) ⚠ cell-cycle shift, explains ~58% of this change |
| [[Panc 03.27 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.507× (z -8.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[RKO (line)]] | wt | 91.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SNU-1 (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[AN3 CA (line)]] | alt | 145 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12816), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYZL1]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[ABCD4]] | +0.68 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[RTCA]] | +0.68 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[ACTR10]] | +0.66 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[EZH1]] | +0.66 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[MRPS5]] | +0.64 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[FLYWCH1]] | +0.64 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[UBE2Q2P1]] | +0.64 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[SNX4]] | +0.64 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[FHIP2A]] | +0.63 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[CASP6]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SHARPIN]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAT1]] | -0.64 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[CSRNP1]] | -0.60 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[CFL1]] | -0.57 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[SNRPB]] | -0.56 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[HIVEP2]] | -0.55 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[THOC6]] | -0.55 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[RASGRF1]] | -0.55 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[HNRNPF]] | -0.54 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ARL5B]] | -0.53 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[PKP4]] | -0.53 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SLC12A2]] | -0.52 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[PURB]] | -0.52 | -0.57 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RUFY2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers RUFY2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NCEH1]] | B | NCEH1 activity raises RUFY2's level | lines that do not express NCEH1 (6) vs lines expressing it (44) | 1.20× lower at baseline in the lines without NCEH1 | 0.080 | ⚠ within organs, on part of the lines; also absent: KCNK6, SMCO2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.634). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-4.7, -11.8); signed map (-32.4, -4.1). **Vector** length 109, 31.4% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.4 | +9.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.5 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.4 | +6.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.6 | +4.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.2 | +4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +0.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +3.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.4 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -7.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +0.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | RUN and FYVE domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:68,341,107-68,407,294 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RABIP4R, FLJ10063, KIAA1537, ZFYVE13 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; RUN domain containing |
| Matched by | ensembl_id |

UniProt [Q8WXA3](https://www.uniprot.org/uniprotkb/Q8WXA3) carries no function annotation.

**Summary**, from NCBI Gene [55680](https://www.ncbi.nlm.nih.gov/gene/55680):

> Enables SH3 domain binding activity. Predicted to be involved in regulation of endocytosis. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19761) · Entrez [55680](https://www.ncbi.nlm.nih.gov/gene/55680) · UniProt [Q8WXA3](https://www.uniprot.org/uniprotkb/Q8WXA3) · Ensembl [ENSG00000204130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204130)

## Data

Gene col 12816: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12816); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12816, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12816]; `tensor/DDL_lfc|DDL_z.npy` [12816]; `embed/gene_vectors.npy` [12816]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12816 or target_col == 12816). Every well: [[RUFY2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUFY2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
