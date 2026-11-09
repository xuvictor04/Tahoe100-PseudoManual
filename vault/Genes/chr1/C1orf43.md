---
symbol: "C1orf43"
type: "gene"
col: 6778
ensembl_id: "ENSG00000143612"
name: "lipid transport auxiliary protein 1"
location: "1q21.3"
module: 23
arm: "+"
pooled_cpm: 83.19
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# C1orf43

*lipid transport auxiliary protein 1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.02× (z +11.4, q 3e-27, up in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.42× (z +3.4, q 0.057, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HS-578T 3.24×, HEC-1-A 2.74×, PANC-1 2.22×, J82 2.54×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H460 5.22×, A-172 3.53×, Hs 766T 2.18×, J82 1.98×; ⚠ cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 2.92×, HEC-1-A 2.83×, PANC-1 2.28×, NCI-H460 2.28×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 2.08×).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.421× (z -14.0, q 1e-41, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2H1]] (+0.72, fdr 7e-06), [[TP53]] (+0.69, fdr 1e-05), [[N4BP2L2]] (+0.69, fdr 7e-06); moves opposite to [[TBC1D24]] (-0.63, fdr 7e-05), [[PAQR4]] (-0.62, fdr 3e-05), [[EHD4]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GFOD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6778.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HS-578T 3.24×, HEC-1-A 2.74×, PANC-1 2.22×, J82 2.54×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H460 5.22×, A-172 3.53×, Hs 766T 2.18×, J82 1.98×; ⚠ cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 2.92×, HEC-1-A 2.83×, PANC-1 2.28×, NCI-H460 2.28×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 2.08×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +11.4 | 3e-27 | 43/49 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +9.1 | 4e-17 | 37/43 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.35×** | +6.9 | 1e-09 | 34/48 (NCI-H460, A-172, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.9 | 6e-07 | 0/50 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **1.37×** | +5.0 | 6e-05 | 32/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +4.5 | 6e-04 | 28/45 (A-427, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.057 | 26/48 (LoVo, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.057 | 16/48 (Hs 766T, C32, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.22×** | +3.2 | 0.084 | 22/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.38× | +3.1 | 0.11 | 17/48 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | 1.43× | +3.0 | 0.13 | 19/47 (A498, A-427, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6778.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.421×** | -14.0 | 1e-41 | 47/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.482×** | -11.8 | 1e-29 | 47/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.497×** | -11.3 | 2e-27 | 47/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.662×** | -6.7 | 3e-09 | 44/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.795×** | -5.2 | 2e-05 | 30/48 (KATO III, A-427, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.546×** | -5.1 | 3e-05 | 42/49 (AN3 CA, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.734×** | -5.0 | 5e-05 | 32/48 (SW48, A-427, …) | rises with dose | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6778. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 110 | 5 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +28.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.08× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.372× (z -12.1) |
| [[KATO III (line)]] | alt | 77.9 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.1) ⚠ cell-cycle shift, explains ~42% of this change | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -14.3) |
| [[PANC-1 (line)]] | alt | 89.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +10.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.363× (z -13.0) |
| [[A-172 (line)]] | wt | 82.8 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +19.7) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H23 (line)]] | alt | 153 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +9.9) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.427× (z -10.4) |
| [[A-427 (line)]] | wt | 110 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.383× (z -10.9) |
| [[A498 (line)]] | wt | 84.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.481× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 70.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +10.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.420× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 119 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 141 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -11.8) |
| [[SW1417 (line)]] | alt | 65.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -10.5) |
| [[SW480 (line)]] | alt | 74.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -13.2) |
| [[A549 (line)]] | wt | 79.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.404× (z -9.1) |
| [[HOP62 (line)]] | alt | 71.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -10.2) |
| [[Hs 766T (line)]] | wt | 81.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.3) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HT-29 (line)]] | alt | 89.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.370× (z -10.2) |
| [[J82 (line)]] | alt | 61.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.2) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H1792 (line)]] | alt | 63.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 102 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.418× (z -10.9) |
| [[SNU-423 (line)]] | alt | 60.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.6) ⚠ cell-cycle shift, explains ~42% of this change | [[Panobinostat (drug)]] 5 µM 0.341× (z -10.1) |
| [[BT-474 (line)]] | alt | 87.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.309× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 74.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.447× (z -9.0) |
| [[HCT15 (line)]] | alt | 81.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.319× (z -9.8) |
| [[HS-578T (line)]] | alt | 48.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +11.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 69.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -9.5) |
| [[LoVo (line)]] | wt | 82.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.459× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 69.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +8.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 69.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.411× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 72.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.374× (z -9.5) |
| [[SHP-77 (line)]] | alt | 93.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 65.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 63.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.298× (z -9.2) |
| [[SW 1088 (line)]] | alt | 65.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0743× (z -8.8) |
| [[SW 900 (line)]] | alt | 101 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.407× (z -8.8) |
| [[AN3 CA (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 79.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6778), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H1]] | +0.72 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[TP53]] | +0.69 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[N4BP2L2]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[AIMP1]] | +0.68 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[TMEM192]] | +0.68 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[N4BP2L1]] | +0.68 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[TMEM260]] | +0.67 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[HPS1]] | +0.67 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[ANAPC16]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[RRAGB]] | +0.65 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[UFC1]] | +0.65 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[OCIAD1]] | +0.64 | +0.63 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D24]] | -0.63 | -0.63 / -0.37 | both halves | 7e-05 |  |
| [[PAQR4]] | -0.62 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[EHD4]] | -0.61 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[LPCAT4]] | -0.61 | -0.65 / -0.38 | both halves | 6e-05 |  |
| [[METAP1]] | -0.60 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[NUP93]] | -0.59 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TPM3]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 | ⚠ same locus (12.0 kb, same strand: neighbours can correlate without regulation) |
| [[AP3M2]] | -0.59 | -0.62 / -0.38 | both halves | 7e-05 |  |
| [[LSM4]] | -0.59 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[USB1]] | -0.59 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[SPTLC2]] | -0.58 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[STIMATE]] | -0.57 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[GNA12]] | -0.56 | -0.59 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GFOD1]] | B | GFOD1 activity lowers C1orf43's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.34× higher at baseline in the lines without GFOD1 | 0.028 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises C1orf43's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises C1orf43's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-19.7, 15.9); signed map (9.4, -21.9). **Vector** length 108, 33.8% of its response variance represented; |z| ≥ 3 in 819 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +10.9 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +8.8 | +3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.8 | -0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.6 | +1.0 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.5 | -0.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.4 | -11.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.2 | -14.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | -11.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.7 | -6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -5.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | lipid transport auxiliary protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,206,696-154,220,637 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NICE-3, DKFZp586G1722; previously C1orf43 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWL3](https://www.uniprot.org/uniprotkb/Q9BWL3) (Lipid transport auxiliary protein 1):

> Required for the formation of endoplasmic reticulum-plasma membrane junctions and functions as an accessory protein for bridge-like lipid transfer protein BLTP1, participating in lipid delivery between endoplasmic reticulum and cell membranes. Regulates the phagocytosis of Gram-negative bacteria like L. pneumophila and E. coli, as well as Gram-positive bacteria such as S. aureus.

**Summary**, from NCBI Gene [25912](https://www.ncbi.nlm.nih.gov/gene/25912):

> Involved in phagocytosis. Located in Golgi apparatus; endoplasmic reticulum-plasma membrane contact site; and mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29876) · Entrez [25912](https://www.ncbi.nlm.nih.gov/gene/25912) · UniProt [Q9BWL3](https://www.uniprot.org/uniprotkb/Q9BWL3) · Ensembl [ENSG00000143612](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143612)

## Data

Gene col 6778: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6778); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6778, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6778]; `tensor/DDL_lfc|DDL_z.npy` [6778]; `embed/gene_vectors.npy` [6778]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6778 or target_col == 6778). Every well: [[C1orf43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1orf43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
