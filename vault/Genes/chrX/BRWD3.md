---
symbol: "BRWD3"
type: "gene"
col: 9103
ensembl_id: "ENSG00000165288"
name: "bromodomain and WD repeat domain containing 3"
location: "Xq21.1"
module: 79
arm: "+"
pooled_cpm: 207.34
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 26
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# BRWD3

*bromodomain and WD repeat domain containing 3* — Xq21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[PF-06260933 (drug)]] 5 µM: 1.62× (z +4.5, q 0.005, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.428× (z -13.8, q 7e-41, down in 43 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.472× (z -13.2, q 9e-38, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P4HA1]] (+0.70, fdr 7e-06), [[PDK3]] (+0.66, fdr 1e-05), [[FAM162A]] (+0.65, fdr 3e-05); moves opposite to [[POGK]] (-0.55, fdr 3e-05), [[ACOT9]] (-0.55, fdr 2e-05), [[PTPN21]] (-0.54, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CA9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | **1.62×** | +4.5 | 0.005 | 37/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.035 | 24/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Minodronic acid (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.047 | 34/48 (NCI-H2347, PANC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9103.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.428×** | -13.8 | 7e-41 | 43/45 (RPMI-7951, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.466×** | -13.5 | 7e-39 | 44/49 (SK-MEL-2, SW480, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.472×** | -13.2 | 9e-38 | 47/48 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.460×** | -13.2 | 2e-37 | 45/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.496×** | -12.4 | 5e-33 | 47/48 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.491×** | -12.0 | 2e-31 | 39/44 (A-427, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.512×** | -11.8 | 3e-30 | 42/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.642×** | -11.0 | 2e-26 | 38/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.549×** | -10.2 | 2e-22 | 44/47 (NCI-H1573, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.616×** | -8.5 | 7e-16 | 45/48 (RPMI-7951, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -8.2 | 9e-15 | 39/49 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.705×** | -6.2 | 3e-08 | 39/48 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.732×** | -5.3 | 5e-06 | 37/48 (SNU-423, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.741×** | -5.3 | 5e-06 | 39/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.832×** | -4.6 | 2e-04 | 23/48 (NCI-H23, PANC-1, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.731×** | -3.9 | 0.003 | 33/48 (NCI-H23, A-427, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.811×** | -3.7 | 0.007 | 24/47 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.755×** | -3.5 | 0.013 | 33/48 (NCI-H661, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.765×** | -3.4 | 0.021 | 24/48 (C32, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.831×** | -3.3 | 0.028 | 23/48 (RPMI-7951, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.833×** | -3.2 | 0.032 | 23/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.881× | -3.1 | 0.039 | 15/48 (CFPAC-1, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.846× | -2.9 | 0.069 | 21/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 454 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -27.7) |
| [[CFPAC-1 (line)]] | alt | 265 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.325× (z -13.0) |
| [[C32 (line)]] | wt | 191 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 271 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 287 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.366× (z -12.7) |
| [[SNU-423 (line)]] | alt | 328 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.9) |
| [[KATO III (line)]] | alt | 186 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -20.2) |
| [[NCI-H2347 (line)]] | alt | 211 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.303× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 380 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.322× (z -14.0) |
| [[H4 (line)]] | wt | 230 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 191 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -19.2) |
| [[SK-MEL-2 (line)]] | alt | 294 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.432× (z -10.1) |
| [[SW480 (line)]] | alt | 279 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -17.3) |
| [[HCT15 (line)]] | alt | 302 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 166 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -10.0) |
| [[Hs 766T (line)]] | wt | 218 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.422× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 232 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -10.9) |
| [[PANC-1 (line)]] | alt | 248 | 1 | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.451× (z -11.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.531× (z -9.6) |
| [[A549 (line)]] | wt | 173 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 136 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -15.2) |
| [[HOP62 (line)]] | alt | 167 | 1 | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -11.6) |
| [[HT-29 (line)]] | alt | 195 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.493× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 156 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 266 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -18.2) |
| [[SW 900 (line)]] | alt | 172 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.339× (z -13.1) |
| [[SW1417 (line)]] | alt | 164 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.328× (z -13.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.482× (z -9.1) |
| [[AN3 CA (line)]] | alt | 228 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -13.5) |
| [[AsPC-1 (line)]] | alt | 241 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -12.1) |
| [[C-33 A (line)]] | alt | 240 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.453× (z -8.7) |
| [[HS-578T (line)]] | alt | 114 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -14.8) |
| [[LS 180 (line)]] | wt | 157 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -13.6) |
| [[A-427 (line)]] | wt | 216 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[COLO 205 (line)]] | alt | 214 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -20.4) |
| [[LoVo (line)]] | wt | 141 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -28.0) |
| [[Panc 03.27 (line)]] | alt | 193 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.482× (z -9.9) |
| [[SW48 (line)]] | wt | 185 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.501× (z -9.1) |
| [[BT-474 (line)]] | alt | 96.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.0) |
| [[CHP-212 (line)]] | wt | 193 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -10.4) |
| [[RKO (line)]] | wt | 219 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.293× (z -12.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 75.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.486× (z -8.7) |
| [[A498 (line)]] | wt | 98.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.0) | — |
| [[J82 (line)]] | alt | 125 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.509× (z -8.5) |
| [[SHP-77 (line)]] | alt | 167 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 91.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P4HA1]] | +0.70 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[PDK3]] | +0.66 | +0.80 / +0.56 | both halves | 1e-05 |  |
| [[FAM162A]] | +0.65 | +0.84 / +0.45 | both halves | 3e-05 |  |
| [[RBPJ]] | +0.64 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[FAM13A]] | +0.64 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[KDM3A]] | +0.62 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[NDUFB8]] | +0.61 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[PIK3C2A]] | +0.61 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[C4orf3]] | +0.60 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[WDR45B]] | +0.59 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[CFAP36]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[PIAS2]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGK]] | -0.55 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ACOT9]] | -0.55 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PTPN21]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[TTLL11]] | -0.53 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TXNRD3]] | -0.51 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[GHRLOS]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[AVEN]] | -0.50 | -0.65 / -0.46 | both halves | 2e-05 |  |
| [[BCAR3]] | -0.49 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[PUS1]] | -0.49 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[EXOSC6]] | -0.48 | -0.66 / -0.39 | both halves | 5e-05 |  |
| [[SHLD2]] | -0.48 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[ZBTB45]] | -0.47 | -0.49 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA9]] | B | CA9 activity raises BRWD3's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.25× lower at baseline in the lines without CA9 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[MLLT3]] | B | MLLT3 activity strengthens BRWD3's drug response | lines that do not express MLLT3 (6) vs lines expressing it (43) | the lines without MLLT3 respond 0.85× as strongly (z diff +0.93); strongest at Homoharringtonine 5 µM: 0.97x vs 0.56x (z diff +5.6) | 0.077 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN; target measured in part of the lines; artifact flags |
| [[SAP30-DT]] | C | SAP30-DT's natural level strengthens BRWD3's drug response | SAP30-DT's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.11; direction clear | 0.074 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.7, -17.3); signed map (-35.5, 23.8). **Vector** length 97.9, 35.2% of its response variance represented; |z| ≥ 3 in 1,318 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | -8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.4 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +1.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.1 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -11.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -11.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.1 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.1 | -2.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain and WD repeat domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.1 — chrX:80,669,503-80,809,877 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BRODL, MRX93, FLJ38568 |
| Gene groups (HGNC) | Bromodomain and WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6RI45](https://www.uniprot.org/uniprotkb/Q6RI45) (Bromodomain and WD repeat-containing protein 3):

> Required for regulation of cell morphology and cytoskeletal organization.

**Summary**, from NCBI Gene [254065](https://www.ncbi.nlm.nih.gov/gene/254065):

> The protein encoded by this gene contains a bromodomain and several WD repeats. It is thought to have a chromatin-modifying function, and may thus play a role in transcription. Mutations in this gene are associated with a spectrum of cognitive disabilities and X-linked macrocephaly. This gene is also associated with translocations in patients with B-cell chronic lymphocytic leukemia. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:17342](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17342) · Entrez [254065](https://www.ncbi.nlm.nih.gov/gene/254065) · UniProt [Q6RI45](https://www.uniprot.org/uniprotkb/Q6RI45) · Ensembl [ENSG00000165288](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165288)

## Data

Gene col 9103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9103); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9103]; `tensor/DDL_lfc|DDL_z.npy` [9103]; `embed/gene_vectors.npy` [9103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9103 or target_col == 9103). Every well: [[BRWD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRWD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
