---
symbol: "SCMH1"
type: "gene"
col: 215
ensembl_id: "ENSG00000010803"
name: "Scm polycomb group protein homolog 1"
location: "1p34.2"
module: 1
arm: "+"
pooled_cpm: 140.31
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 29
n_dd_up_clean: 4
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SCMH1

*Scm polycomb group protein homolog 1* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.33× (z +5.5, q 2e-05, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.190× (z -32.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMC6]] (+0.64, fdr 1e-05), [[SLC25A13]] (+0.64, fdr 1e-05), [[TTC27]] (+0.60, fdr 1e-05); moves opposite to [[MLF2]] (-0.57, fdr 2e-05), [[GRB2]] (-0.57, fdr 2e-05), [[ALKBH5]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TTYH2]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Bendamustine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 215.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +5.5 | 2e-05 | 30/48 (HepG2/C3A, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +4.3 | 0.005 | 12/48 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.26×** | +4.2 | 0.005 | 30/48 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +3.8 | 0.017 | 23/48 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.017 | 25/48 (Hs 766T, A498, …) | all doses, flat |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.7 | 0.021 | 16/48 (BT-474, J82, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.031 | 21/48 (CFPAC-1, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | 1.12× | +3.1 | 0.15 | 4/48 (SW48, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 215.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.190×** | -32.1 | 0e+00 | 48/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.216×** | -29.6 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.373×** | -26.9 | 0e+00 | 48/49 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.265×** | -25.6 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.228×** | -14.9 | 0e+00 | 48/49 (NCI-H23, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.465×** | -14.2 | 8e-44 | 41/48 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.476×** | -13.8 | 3e-41 | 37/44 (KATO III, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.481×** | -13.1 | 3e-37 | 41/45 (SW480, A-427, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.494×** | -13.1 | 3e-37 | 42/50 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.284×** | -12.7 | 3e-35 | 42/48 (A-427, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.534×** | -11.6 | 1e-29 | 42/49 (MIA PaCa-2, RKO, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.583×** | -10.0 | 5e-22 | 43/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.626×** | -9.1 | 6e-18 | 38/48 (SW48, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.726×** | -8.7 | 1e-16 | 27/48 (NCI-H1792, C32, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.656×** | -8.1 | 1e-14 | 34/48 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.770×** | -7.1 | 3e-11 | 34/48 (RKO, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.712×** | -6.5 | 2e-09 | 35/49 (HOP62, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.787×** | -6.5 | 2e-09 | 34/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.533×** | -6.4 | 5e-09 | 37/49 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 215. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 209 | 0 | 19 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -31.1) |
| [[MIA PaCa-2 (line)]] | alt | 204 | 0 | 17 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0831× (z -34.2) |
| [[NCI-H23 (line)]] | alt | 186 | 0 | 16 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -27.0) |
| [[PANC-1 (line)]] | alt | 192 | 0 | 16 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -28.8) |
| [[RKO (line)]] | wt | 289 | 0 | 14 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -29.5) |
| [[SK-MEL-2 (line)]] | alt | 167 | 0 | 14 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -28.6) |
| [[SW480 (line)]] | alt | 158 | 0 | 14 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -33.7) |
| [[HOP62 (line)]] | alt | 154 | 0 | 13 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -21.8) |
| [[LOX-IMVI (line)]] | wt | 167 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -23.0) |
| [[NCI-H460 (line)]] | wt | 128 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -25.1) |
| [[SNU-1 (line)]] | wt | 194 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -18.2) |
| [[SW48 (line)]] | wt | 171 | 0 | 13 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -19.8) |
| [[C-33 A (line)]] | alt | 222 | 0 | 12 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -22.0) |
| [[SNU-423 (line)]] | alt | 120 | 0 | 12 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -21.6) |
| [[J82 (line)]] | alt | 129 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.203× (z -18.3) |
| [[LoVo (line)]] | wt | 138 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -27.1) |
| [[LS 180 (line)]] | wt | 162 | 0 | 11 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -21.5) |
| [[A-172 (line)]] | wt | 122 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -27.0) |
| [[C32 (line)]] | wt | 102 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -19.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.225× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 131 | 0 | 9 | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -22.0) |
| [[HCT15 (line)]] | alt | 204 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -17.8) |
| [[SHP-77 (line)]] | alt | 165 | 1 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +8.6) ⚠ cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 5 µM 0.294× (z -16.5) |
| [[A549 (line)]] | wt | 159 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -22.7) |
| [[AN3 CA (line)]] | alt | 233 | 0 | 7 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -15.3) |
| [[H4 (line)]] | wt | 247 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -20.5) |
| [[HS-578T (line)]] | alt | 120 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -17.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -15.4) |
| [[A498 (line)]] | wt | 149 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -16.5) |
| [[BT-474 (line)]] | alt | 140 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -17.3) |
| [[CFPAC-1 (line)]] | alt | 92.2 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -14.0) |
| [[HT-29 (line)]] | alt | 122 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -19.5) |
| [[KATO III (line)]] | alt | 114 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -26.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.182× (z -21.2) |
| [[NCI-H1792 (line)]] | alt | 130 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -21.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.222× (z -17.7) |
| [[NCI-H2030 (line)]] | alt | 144 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -13.9) |
| [[A-427 (line)]] | wt | 117 | 0 | 5 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0514× (z -19.8) |
| [[Hs 766T (line)]] | wt | 94.9 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -19.1) |
| [[hTERT-HPNE (line)]] | wt | 131 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 92.5 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -15.2) |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -17.3) |
| [[SW 900 (line)]] | alt | 85.1 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -10.9) |
| [[SW1417 (line)]] | alt | 81.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -17.4) |
| [[COLO 205 (line)]] | alt | 103 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -19.7) |
| [[NCI-H2347 (line)]] | alt | 49.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.4) ⚠ cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 49.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.341× (z -8.7) |
| [[CHP-212 (line)]] | wt | 90.7 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.176× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 50.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.7) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SW 1271 (line)]] | alt | 117 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.273× (z -8.5) |
| [[NCI-H2122 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 215), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC6]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[SLC25A13]] | +0.64 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[TTC27]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CEP83]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CUX1]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[DOCK1]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[FAF1]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TMEM168]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[NDUFAF2]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ABCE1]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ATR]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[MECR]] | +0.58 | +0.62 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLF2]] | -0.57 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[GRB2]] | -0.57 | -0.54 / -0.48 | both halves | 2e-05 | pathway: Intracellular signaling by second messengers |
| [[ALKBH5]] | -0.57 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[PBXIP1]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[MXD1]] | -0.55 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[LMBRD1]] | -0.54 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[SUMO1]] | -0.54 | -0.42 / -0.56 | both halves | 4e-05 | pathway: SUMO E3 ligases SUMOylate target proteins; STRING 425 |
| [[RAB11A]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[APAF1]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[TM9SF2]] | -0.53 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[SAR1A]] | -0.53 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[SPINT2]] | -0.53 | -0.51 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTYH2]] | B | TTYH2 activity raises SCMH1's level | lines that do not express TTYH2 (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without TTYH2 | 0.012 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, DUXAP9; maybe low, not absent |
| [[TTYH2]] | B | TTYH2 activity strengthens SCMH1's drug response | lines that do not express TTYH2 (9) vs lines expressing it (41) | the lines without TTYH2 respond 0.79× as strongly (z diff +1.96); strongest at Dinaciclib 5 µM: 0.67x vs 0.46x (z diff +4.3) | 0.068 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, DUXAP9; maybe low, not absent; artifact flags |
| [[LDLRAD3]] | B | LDLRAD3 activity raises SCMH1's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.67× lower at baseline in the lines without LDLRAD3 | 0.091 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CENPP]] | C | CENPP activity raises SCMH1's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.05× lower at baseline in the lines without CENPP | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[CENPP]] | C | CENPP activity strengthens SCMH1's drug response | lines that do not express CENPP (4) vs lines expressing it (46) | the lines without CENPP respond 0.63× as strongly (z diff +2.98); strongest at Dinaciclib 5 µM: 1.07x vs 0.46x (z diff +7.7) | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bendamustine (drug)]] 0.5 µM | C | SCMH1's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | SCMH1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.361 over the table, 0.040 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.506). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (3.5, -32.1); signed map (7.0, -46.3). **Vector** length 118, 45.4% of its response variance represented; |z| ≥ 3 in 1,557 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +9.7 | +5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +8.6 | +3.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.6 | +0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.0 | +1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.0 | +3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.6 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +1.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.3 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | -0.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.2 | -14.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.8 | -12.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -6.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.6 | -7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | Scm polycomb group protein homolog 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:41,027,202-41,242,306 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Scml3 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; MBT domain containing |
| Reactome | 19 pathways, smallest: SUMOylation of DNA methylation proteins; RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known; SUMOylation of transcription cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GD3](https://www.uniprot.org/uniprotkb/Q96GD3) (Polycomb protein SCMH1):

> Associates with Polycomb group (PcG) multiprotein complexes; the complex class is required to maintain the transcriptionally repressive state of some genes.

**Summary**, from NCBI Gene [22955](https://www.ncbi.nlm.nih.gov/gene/22955):

> Predicted to enable chromatin binding activity and histone binding activity. Predicted to be involved in heterochromatin formation and negative regulation of DNA-templated transcription. Predicted to act upstream of or within anterior/posterior pattern specification; chromatin remodeling; and spermatogenesis. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19003](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19003) · Entrez [22955](https://www.ncbi.nlm.nih.gov/gene/22955) · UniProt [Q96GD3](https://www.uniprot.org/uniprotkb/Q96GD3) · Ensembl [ENSG00000010803](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010803)

## Data

Gene col 215: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 215); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 215, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 215]; `tensor/DDL_lfc|DDL_z.npy` [215]; `embed/gene_vectors.npy` [215]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 215 or target_col == 215). Every well: [[SCMH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCMH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
