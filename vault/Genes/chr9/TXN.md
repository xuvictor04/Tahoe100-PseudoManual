---
symbol: "TXN"
type: "gene"
col: 5905
ensembl_id: "ENSG00000136810"
name: "thioredoxin"
location: "9q31.3"
module: 60
arm: "+"
pooled_cpm: 136.24
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 7
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# TXN

*thioredoxin* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.21× (z +10.3, q 3e-22, up in 43 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.53× (z +8.5, q 2e-15, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.503× (z -8.9, q 3e-16, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H23 0.124×, LoVo 0.203×, HT-29 0.257×, SW48 0.272×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.294×, RKO 0.326×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRDX1]] (+0.70, fdr 7e-06), [[HSPE1]] (+0.68, fdr 7e-06), [[LRP8]] (+0.64, fdr 7e-06); moves opposite to [[MKS1]] (-0.62, fdr 1e-05), [[DNAL4]] (-0.62, fdr 4e-05), [[XRCC1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 7 go from it, the strongest it → [[TXNRD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5905.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.21×** | +10.3 | 3e-22 | 43/44 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.94×** | +9.9 | 2e-20 | 48/49 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.53×** | +8.5 | 2e-15 | 45/48 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.63×** | +8.3 | 2e-14 | 43/45 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **2.00×** | +6.2 | 9e-08 | 45/47 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.84×** | +5.6 | 2e-06 | 41/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +5.1 | 2e-05 | 41/48 (COLO 205, HEC-1-A, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.70×** | +4.9 | 6e-05 | 42/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +4.3 | 0.001 | 37/48 (HEC-1-A, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.4 | 0.039 | 25/47 (CFPAC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.43×** | +3.3 | 0.048 | 32/48 (COLO 205, SW480, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.28×** | +3.2 | 0.057 | 34/48 (HT-29, Hs 766T, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +3.2 | 0.057 | 28/48 (HEC-1-A, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.40×** | +3.1 | 0.068 | 30/48 (NCI-H1573, SW480, …) | all doses, flat | composition shift |
| [[Arbutin (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.069 | 31/48 (SNU-423, A498, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5905.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H23 0.124×, LoVo 0.203×, HT-29 0.257×, SW48 0.272×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.294×, RKO 0.326×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.503×** | -8.9 | 3e-16 | 39/48 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.629×** | -4.2 | 0.006 | 36/48 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.677×** | -3.6 | 0.067 | 40/48 (KATO III, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.645× | -3.2 | 0.19 | 29/50 (LoVo, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.717× | -3.0 | 0.27 | 27/48 (SW48, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5905. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 259 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.55× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.1) |
| [[A549 (line)]] | wt | 151 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.87× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[COLO 205 (line)]] | alt | 121 | 2 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 4.44× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -8.9) |
| [[HOP62 (line)]] | alt | 86.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.60× (z +9.4) | — |
| [[KATO III (line)]] | alt | 241 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.37× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -13.0) |
| [[LoVo (line)]] | wt | 155 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.37× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -16.5) |
| [[LOX-IMVI (line)]] | wt | 101 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 66.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.57× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 106 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 152 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.0) |
| [[A498 (line)]] | wt | 250 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AsPC-1 (line)]] | alt | 106 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.49× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -10.4) |
| [[C32 (line)]] | wt | 54.0 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.59× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 131 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -11.2) |
| [[HT-29 (line)]] | alt | 197 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 110 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.60× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 93.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 199 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.27× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[RKO (line)]] | wt | 174 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -11.5) |
| [[A-427 (line)]] | wt | 111 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.294× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 72.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HS-578T (line)]] | alt | 97.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 88.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 168 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -22.5) |
| [[Panc 03.27 (line)]] | alt | 96.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-1 (line)]] | wt | 122 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -8.5) |
| [[SW 900 (line)]] | alt | 75.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW1417 (line)]] | alt | 145 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.78× (z +8.9) | — |
| [[SW48 (line)]] | wt | 229 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -13.0) |
| [[A-172 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 194 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 184 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5905), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDX1]] | +0.70 | +0.73 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY; STRING 990 |
| [[HSPE1]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 | STRING 810 |
| [[LRP8]] | +0.64 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[AHSA1]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[SEL1L3]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[HSPD1]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 | STRING 552 |
| [[TXNRD1]] | +0.59 | +0.62 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY; STRING 999 |
| [[GCLM]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY; STRING 670 |
| [[PTGES3]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[KTN1-AS1]] | +0.57 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[NAA50]] | +0.57 | +0.70 / +0.38 | both halves | 6e-05 |  |
| [[CCT3]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKS1]] | -0.62 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[DNAL4]] | -0.62 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[XRCC1]] | -0.62 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[SNHG11]] | -0.61 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[ACTR1B]] | -0.59 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[OSGEP]] | -0.59 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[FAM161B]] | -0.58 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[DXO]] | -0.58 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[COQ6]] | -0.58 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[YY1AP1]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[PRR14]] | -0.57 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[PPIL4]] | -0.57 | -0.62 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TXNRD1]] | C | TXN's natural level weakens TXNRD1's drug response | TXN's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.12; direction not clear | 0.041 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM | C | TXN's natural level raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | TXN's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.75 | 0.162 over the table, 0.003 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | TXN's natural level raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | TXN's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.310 over the table, 0.028 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | TXN's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | TXN's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.406 over the table, 0.052 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Adagrasib (drug)]] 0.5 µM | C | TXN's natural level lowers the cells' numbers under Adagrasib 0.5 µM (makes them more sensitive) | TXN's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.437 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | TXN's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | TXN's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.471 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | TXN's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | TXN's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.086 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.584). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-20.4, -10.3); signed map (-25.2, -30.0). **Vector** length 81.2, 33.5% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.7 | +8.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -8.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -2.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | -3.0 | +4.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.5 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | +0.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.1 | +1.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -2.0 | +0.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.9 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:110,243,810-110,256,507 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRX, Trx80, TXN1 |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, GLYCOLYSIS |
| Reactome | 24 pathways, smallest: Protein repair; Regulation of FOXO transcriptional activity by acetylation; The NLRP3 inflammasome |
| Matched by | ensembl_id |

**Function**, from UniProt [P10599](https://www.uniprot.org/uniprotkb/P10599) (Thioredoxin):

> Participates in various redox reactions through the reversible oxidation of its active center dithiol to a disulfide and catalyzes dithiol-disulfide exchange reactions. Plays a role in the reversible S-nitrosylation of cysteine residues in target proteins, and thereby contributes to the response to intracellular nitric oxide. Nitrosylates the active site Cys of CASP3 in response to nitric oxide (NO), and thereby inhibits caspase-3 activity. Induces the FOS/JUN AP-1 DNA-binding activity in …

**Summary**, from NCBI Gene [7295](https://www.ncbi.nlm.nih.gov/gene/7295):

> The protein encoded by this gene acts as a homodimer and is involved in many redox reactions. The encoded protein is active in the reversible S-nitrosylation of cysteines in certain proteins, which is part of the response to intracellular nitric oxide. This protein is found in the cytoplasm. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:12435](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12435) · Entrez [7295](https://www.ncbi.nlm.nih.gov/gene/7295) · UniProt [P10599](https://www.uniprot.org/uniprotkb/P10599) · Ensembl [ENSG00000136810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136810)

## Data

Gene col 5905: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5905); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5905, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5905]; `tensor/DDL_lfc|DDL_z.npy` [5905]; `embed/gene_vectors.npy` [5905]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5905 or target_col == 5905). Every well: [[TXN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
