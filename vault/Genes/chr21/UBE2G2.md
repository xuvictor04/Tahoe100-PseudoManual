---
symbol: "UBE2G2"
type: "gene"
col: 11576
ensembl_id: "ENSG00000184787"
name: "ubiquitin conjugating enzyme E2 G2"
location: "21q22.3"
module: 18
arm: "+"
pooled_cpm: 72.27
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# UBE2G2

*ubiquitin conjugating enzyme E2 G2* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (18 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.96× (z +14.0, q 5e-42, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.805× (z -4.6, q 0.003, down in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~21% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.556×, RKO 0.625×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.188×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.377×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XPO5]] (+0.76, fdr 7e-06), [[ADAT2]] (+0.74, fdr 7e-06), [[MRPS25]] (+0.73, fdr 7e-06); moves opposite to [[CIR1]] (-0.72, fdr 7e-06), [[FRG1]] (-0.68, fdr 7e-06), [[TCEAL8]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 20 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11576.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +14.0 | 5e-42 | 46/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.00×** | +13.3 | 3e-38 | 38/45 (A498, Panc 03.27, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.89×** | +13.3 | 6e-38 | 47/48 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.88×** | +13.2 | 2e-37 | 39/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.87×** | +13.1 | 5e-37 | 39/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.82×** | +12.5 | 6e-34 | 42/48 (A498, KATO III, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.67×** | +10.7 | 9e-25 | 43/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.65×** | +10.4 | 2e-23 | 36/48 (HOP62, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +10.3 | 4e-23 | 38/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +10.2 | 1e-22 | 41/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.66×** | +10.2 | 2e-22 | 39/47 (CFPAC-1, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.65×** | +10.1 | 3e-22 | 33/44 (A498, SW1417, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +9.6 | 3e-20 | 38/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.38×** | +9.5 | 7e-20 | 31/49 (CFPAC-1, NCI-H2347, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +8.6 | 3e-16 | 38/47 (H4, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.80×** | +6.4 | 4e-09 | 35/48 (NCI-H460, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.79×** | +6.3 | 8e-09 | 40/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.32×** | +5.8 | 2e-07 | 29/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.68×** | +5.6 | 4e-07 | 34/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.67×** | +5.6 | 6e-07 | 38/48 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +5.5 | 1e-06 | 21/48 (CFPAC-1, HEC-1-A, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 5e-04 | 23/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.47×** | +4.2 | 6e-04 | 23/48 (A498, CFPAC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.1 | 8e-04 | 24/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 1e-03 | 22/48 (AsPC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.003 | 19/47 (NCI-H23, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11576.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.556×, RKO 0.625×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.188×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.377×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.805×** | -4.6 | 0.003 | 24/48 (LoVo, A498, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.849× | -3.5 | 0.15 | 15/48 (KATO III, A498, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.809× | -3.2 | 0.26 | 18/48 (HEC-1-A, A498, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 83.8 | 10 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +12.4) | — |
| [[A498 (line)]] | wt | 62.6 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HOP62 (line)]] | alt | 57.2 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +12.8) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[LS 180 (line)]] | wt | 69.7 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 34.0 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +10.4) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[HS-578T (line)]] | alt | 58.0 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.53× (z +10.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 52.6 | 4 (4 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.89× (z +10.5) ⚠ unreliable plate only | — |
| [[Panc 03.27 (line)]] | alt | 46.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.14× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.56× (z +8.6) | — |
| [[H4 (line)]] | wt | 70.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.59× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +9.3) | — |
| [[KATO III (line)]] | alt | 38.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[RKO (line)]] | wt | 135 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.625× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 40.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[SW1417 (line)]] | alt | 65.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[AsPC-1 (line)]] | alt | 32.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[HEC-1-A (line)]] | alt | 76.5 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[Hs 766T (line)]] | wt | 48.7 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[HT-29 (line)]] | alt | 35.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[LoVo (line)]] | wt | 85.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 122 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.68× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 73.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 82.3 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 36.5 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.3) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 91.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 80.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 51.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[COLO 205 (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.00× (z +9.5) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[HCT15 (line)]] | alt | 71.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 63.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.28× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LOX-IMVI (line)]] | wt | 106 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.31× (z +9.0) ⚠ unreliable plate only | — |
| [[NCI-H2030 (line)]] | alt | 103 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 79.6 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.69× (z +11.9) ⚠ unreliable plate only | — |
| [[SNU-1 (line)]] | wt | 95.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[A-172 (line)]] | wt | 75.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 157 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 74.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 80.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 73.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPO5]] | +0.76 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[MRPS25]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 | STRING 478 |
| [[LETM1]] | +0.72 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[URB1]] | +0.70 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[SEH1L]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[CHID1]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[GART]] | +0.69 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.68 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[QSOX2]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[MDN1]] | +0.68 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[CAD]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIR1]] | -0.72 | -0.67 / -0.74 | both halves | 7e-06 |  |
| [[FRG1]] | -0.68 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[TCEAL8]] | -0.66 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[MED19]] | -0.66 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[IFI27L2]] | -0.65 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.65 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[SECISBP2L]] | -0.65 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[ASB8]] | -0.64 | -0.57 / -0.65 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[TRAPPC2B]] | -0.64 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[AKAP9]] | -0.64 | -0.58 / -0.65 | both halves | 8e-06 |  |
| [[SAP18]] | -0.64 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[EAPP]] | -0.64 | -0.56 / -0.70 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UBE2G2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MTHFD1L]] | C | MTHFD1L activity raises UBE2G2's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.29× lower at baseline in the lines without MTHFD1L | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.747). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.9, -36.6); signed map (-3.4, -51.7). **Vector** length 114, 34.8% of its response variance represented; |z| ≥ 3 in 1,346 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.54 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.4 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +6.9 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +6.9 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +6.6 | +13.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.0 | +10.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.2 | +6.4 |
|  | [[EX229 (drug)]] 5 µM |  | +5.0 | +6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.5 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +9.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.5 | +5.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -10.5 | -0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.9 | +0.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | +4.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +0.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.0 | -3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.3 | -0.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 G2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:44,768,580-44,801,826 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UBC7 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 5 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Protein ubiquitination; Antigen processing: Ubiquitination & Proteasome degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P60604](https://www.uniprot.org/uniprotkb/P60604) (Ubiquitin-conjugating enzyme E2 G2):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. In vitro catalyzes 'Lys-48'-linked polyubiquitination. Involved in endoplasmic reticulum-associated degradation (ERAD). Required for sterol-induced ubiquitination of 3-hydroxy-3-methylglutaryl coenzyme A reductase and its subsequent proteasomal degradation.

**Summary**, from NCBI Gene [7327](https://www.ncbi.nlm.nih.gov/gene/7327):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. The encoded protein shares 100% sequence identity with the mouse counterpart. This gene is ubiquitously …

**Accessions** — [HGNC:12483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12483) · Entrez [7327](https://www.ncbi.nlm.nih.gov/gene/7327) · UniProt [P60604](https://www.uniprot.org/uniprotkb/P60604) · Ensembl [ENSG00000184787](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184787)

## Data

Gene col 11576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11576); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11576]; `tensor/DDL_lfc|DDL_z.npy` [11576]; `embed/gene_vectors.npy` [11576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11576 or target_col == 11576). Every well: [[UBE2G2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2G2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
