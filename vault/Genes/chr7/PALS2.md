---
symbol: "PALS2"
type: "gene"
col: 2687
ensembl_id: "ENSG00000105926"
name: "protein associated with LIN7 2, MAGUK p55 family member"
location: "7p15.3"
module: 18
arm: "+"
pooled_cpm: 128.71
n_lines_expressing: 47
n_dd_up: 25
n_dd_down: 7
n_dd_up_clean: 19
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 13
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PALS2

*protein associated with LIN7 2, MAGUK p55 family member* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.60× (z +7.9, q 1e-12, up in 37 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.56× (z +7.6, q 8e-12, up in 31 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.602× (z -12.2, q 2e-31, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METAP1]] (+0.78, fdr 7e-06), [[UCK2]] (+0.73, fdr 7e-06), [[PACC1]] (+0.70, fdr 7e-06); moves opposite to [[RBM23]] (-0.67, fdr 1e-05), [[COQ7]] (-0.64, fdr 1e-05), [[LARP7]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CENPV]] → it (grade B ⚠); 13 go from it, the strongest it → [[MOB1B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2687.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +7.9 | 1e-12 | 37/45 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +7.6 | 8e-12 | 35/44 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +7.6 | 8e-12 | 31/45 (H4, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +7.4 | 2e-11 | 37/45 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +7.1 | 2e-10 | 32/45 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +6.8 | 7e-10 | 32/45 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +6.8 | 9e-10 | 34/45 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +6.6 | 3e-09 | 34/45 (LoVo, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.5 | 5e-09 | 34/45 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.87×** | +5.5 | 2e-06 | 34/46 (LoVo, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +5.4 | 3e-06 | 29/46 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +5.2 | 9e-06 | 23/45 (RKO, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +4.8 | 7e-05 | 23/45 (LoVo, CFPAC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.7 | 1e-04 | 31/42 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 4e-04 | 29/45 (NCI-H460, AsPC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 7e-04 | 29/45 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.002 | 23/44 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.0 | 0.002 | 20/46 (NCI-H460, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.26×** | +3.9 | 0.004 | 25/45 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[EX229 (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.005 | 23/45 (Hs 766T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2687.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.602×** | -12.2 | 2e-31 | 34/45 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.686×** | -6.4 | 3e-08 | 27/46 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.676×** | -6.4 | 3e-08 | 28/42 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.698×** | -6.1 | 1e-07 | 26/45 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.803×** | -3.7 | 0.021 | 25/45 (Hs 766T, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.821×** | -3.4 | 0.070 | 20/45 (RPMI-7951, PANC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.764×** | -3.2 | 0.095 | 21/45 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.827× | -3.1 | 0.11 | 19/44 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -3.1 | 0.11 | 5/47 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.880× | -3.1 | 0.11 | 13/45 (RKO, Panc 03.27, …) | top dose only | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.876× | -3.1 | 0.11 | 14/46 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.837× | -3.0 | 0.11 | 16/45 (SW480, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2687. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 309 | 1 | 8 (6 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.91× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -17.8) |
| [[H4 (line)]] | wt | 188 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.12× (z +10.5) | — |
| [[LoVo (line)]] | wt | 96.7 | 4 (1 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 2.27× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -12.4) |
| [[SW480 (line)]] | alt | 277 | 1 | 4 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.79× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 40.0 | 2 (1 ⚠) | 2 | [[Belinostat (drug)]] 5 µM 2.60× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 122 | 2 (2 ⚠) | 2 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.62× (z +10.9) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -10.2) |
| [[RKO (line)]] | wt | 192 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -17.8) |
| [[A-427 (line)]] | wt | 123 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.411× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 170 | 0 | 3 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.640× (z -16.9) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.529× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 211 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.445× (z -11.1) |
| [[A-172 (line)]] | wt | 97.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.6) |
| [[Hs 766T (line)]] | wt | 67.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.36× (z +11.1) ⚠ unreliable plate only | [[Docetaxel (drug)]] 0.05 µM 0.372× (z -9.0) ⚠ transcription drop |
| [[HS-578T (line)]] | alt | 122 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 126 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.46× (z +9.4) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -8.8) |
| [[PANC-1 (line)]] | alt | 150 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 1.97× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -12.9) |
| [[SNU-1 (line)]] | wt | 157 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.490× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 93.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -9.5) |
| [[C-33 A (line)]] | alt | 193 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 37.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.85× (z +8.6) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HCT15 (line)]] | alt | 89.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -8.5) |
| [[HT-29 (line)]] | alt | 78.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 115 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 170 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 96.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 99.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 211 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +9.4) | — |
| [[A498 (line)]] | wt | 275 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 181 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 80.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.5 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 129 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.59 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 66.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 220 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2687), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | +0.78 | +0.85 / +0.68 | both halves | 7e-06 |  |
| [[UCK2]] | +0.73 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[PACC1]] | +0.70 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[PPARGC1B]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[TBC1D4]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[POLR3G]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[TMTC4]] | +0.65 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[PPAT]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[DKC1]] | +0.65 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[ADAT2]] | +0.65 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[GARNL3]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ANKRD13B]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM23]] | -0.67 | -0.75 / -0.54 | both halves | 1e-05 |  |
| [[COQ7]] | -0.64 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[LARP7]] | -0.62 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[RBM42]] | -0.62 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[XRN1]] | -0.62 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[ZNF764]] | -0.62 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.62 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[ZNF776]] | -0.61 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[SCAF1]] | -0.61 | -0.70 / -0.46 | both halves | 2e-05 |  |
| [[FAM200A]] | -0.61 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[HNRNPH2]] | -0.60 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[LINC00174]] | -0.60 | -0.69 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CENPV]] | B | CENPV activity raises PALS2's level | lines that do not express CENPV (9) vs lines expressing it (41) | 1.18× lower at baseline in the lines without CENPV | 0.051 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PPARGC1B]] | C | PPARGC1B activity raises PALS2's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without PPARGC1B | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent; its own permutation p |
| [[GARNL3]] | C | GARNL3 activity raises PALS2's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without GARNL3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MOB1B]] | C | PALS2 activity raises MOB1B's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 3.43× lower at baseline in the lines without PALS2 | 0.002 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |
| [[BMP2K]] | C | PALS2 activity raises BMP2K's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 3.89× lower at baseline in the lines without PALS2 | 0.010 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |
| [[DDHD1]] | C | PALS2 activity raises DDHD1's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 3.63× lower at baseline in the lines without PALS2 | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |
| [[NBPF15]] | C | PALS2 activity raises NBPF15's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 2.47× lower at baseline in the lines without PALS2 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |
| [[FAM200A]] | C | PALS2 activity raises FAM200A's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 2.03× lower at baseline in the lines without PALS2 | 0.031 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |
| [[FMNL2]] | C | PALS2 activity raises FMNL2's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 3.87× lower at baseline in the lines without PALS2 | 0.032 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |
| [[ADCY3]] | C | PALS2 activity raises ADCY3's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 4.10× lower at baseline in the lines without PALS2 | 0.050 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |
| [[NBPF9]] | C | PALS2 activity strengthens NBPF9's drug response | lines that do not express PALS2 (3) vs lines expressing it (45) | the lines without PALS2 respond the other way (z diff +2.34); strongest at Ouabain (Octahydrate) 5 µM: 0.71x vs 1.54x (z diff +4.7) | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PRKCQ]] | C | PALS2 activity strengthens PRKCQ's drug response | lines that do not express PALS2 (3) vs lines expressing it (41) | the lines without PALS2 respond 0.69× as strongly (z diff +0.46); strongest at Panobinostat 0.5 µM: 0.70x vs 1.78x (z diff +3.8) | 0.073 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[EPS15]] | C | PALS2 activity raises EPS15's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 1.56× lower at baseline in the lines without PALS2 | 0.074 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |
| cells under [[Lonafarnib (drug)]] 5 µM | C | PALS2 activity raises the cells' numbers under Lonafarnib 5 µM (protects the cells) | lines that do not express PALS2 (3) vs lines expressing it (45) | the lines without PALS2: 0.13× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |
| [[PAQR3]] | C | PALS2 activity raises PAQR3's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 2.18× lower at baseline in the lines without PALS2 | 0.087 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.717). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.3, -37.9); signed map (-5.4, -54.5). **Vector** length 136, 47.3% of its response variance represented; |z| ≥ 3 in 1,214 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.6 | +7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.2 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +5.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.7 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.7 | +5.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -13.6 | -12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.1 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.0 | -1.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | protein associated with LIN7 2, MAGUK p55 family member |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:24,573,268-24,694,193 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VAM-1, p55T; previously MPP6 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing; SH3 domain containing |
| Matched by | ensembl_id |

UniProt [Q9NZW5](https://www.uniprot.org/uniprotkb/Q9NZW5) carries no function annotation.

**Summary**, from NCBI Gene [51678](https://www.ncbi.nlm.nih.gov/gene/51678):

> Members of the peripheral membrane-associated guanylate kinase (MAGUK) family function in tumor suppression and receptor clustering by forming multiprotein complexes containing distinct sets of transmembrane, cytoskeletal, and cytoplasmic signaling proteins. All MAGUKs contain a PDZ-SH3-GUK core and are divided into 4 subfamilies, DLG-like (see DLG1; MIM 601014), ZO1-like (see TJP1; MIM 601009), p55-like (see MPP1; MIM 305360), and LIN2-like (see CASK; MIM 300172), based on their size and the …

**Accessions** — [HGNC:18167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18167) · Entrez [51678](https://www.ncbi.nlm.nih.gov/gene/51678) · UniProt [Q9NZW5](https://www.uniprot.org/uniprotkb/Q9NZW5) · Ensembl [ENSG00000105926](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105926)

## Data

Gene col 2687: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2687); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2687, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2687]; `tensor/DDL_lfc|DDL_z.npy` [2687]; `embed/gene_vectors.npy` [2687]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2687 or target_col == 2687). Every well: [[PALS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PALS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
