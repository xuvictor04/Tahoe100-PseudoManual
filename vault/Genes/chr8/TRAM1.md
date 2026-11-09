---
symbol: "TRAM1"
type: "gene"
col: 852
ensembl_id: "ENSG00000067167"
name: "translocation associated membrane protein 1"
location: "8q13.3"
module: 42
arm: "+"
pooled_cpm: 170.86
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# TRAM1

*translocation associated membrane protein 1* — 8q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.66× (z +9.6, q 6e-19, up in 39 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.31× (z +5.2, q 4e-05, up in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A549 7.17×, A498 3.39×, PANC-1 2.78×, CFPAC-1 2.19×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 7.55×, A498 3.68×, PANC-1 2.55×, CFPAC-1 2.22×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A549 4.32×, A498 2.40×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.673× (z -10.5, q 6e-23, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED2]] (+0.68, fdr 7e-06), [[UBE2J1]] (+0.66, fdr 1e-05), [[OSTC]] (+0.62, fdr 1e-05); moves opposite to [[ZC3H18]] (-0.50, fdr 2e-05), [[SMG9]] (-0.49, fdr 1e-04), [[ZNF274]] (-0.49, fdr 3e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 852.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A549 7.17×, A498 3.39×, PANC-1 2.78×, CFPAC-1 2.19×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 7.55×, A498 3.68×, PANC-1 2.55×, CFPAC-1 2.22×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A549 4.32×, A498 2.40×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +9.6 | 6e-19 | 39/49 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +8.5 | 4e-15 | 32/43 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +5.2 | 4e-05 | 34/47 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +5.2 | 4e-05 | 28/48 (SW48, HT-29, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +4.8 | 2e-04 | 21/49 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 2e-04 | 27/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.14× | +3.4 | 0.049 | 7/48 (SW480, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.12 | 16/48 (SW 900, C-33 A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.0 | 0.16 | 21/45 (A549, A498, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 852.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.673×** | -10.5 | 6e-23 | 36/48 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.583×** | -10.2 | 4e-22 | 38/48 (Hs 766T, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.615×** | -9.2 | 6e-18 | 36/48 (Hs 766T, A-172, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.804×** | -5.8 | 9e-07 | 28/48 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.745×** | -5.6 | 3e-06 | 30/48 (A-172, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.751×** | -5.4 | 5e-06 | 33/48 (Hs 766T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -4.7 | 2e-04 | 23/48 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.799×** | -4.2 | 0.002 | 26/48 (SW 900, NCI-H2347, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -4.1 | 0.003 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.812×** | -4.0 | 0.004 | 24/48 (HOP62, NCI-H2347, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.806×** | -3.9 | 0.004 | 26/48 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | 0.835× | -3.3 | 0.045 | 22/47 (HepG2/C3A, KATO III, …) | two highest doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.848× | -3.1 | 0.074 | 18/49 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.797×** | -3.1 | 0.086 | 23/48 (hTERT-HPNE, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 852. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 136 | 1 (1 ⚠) | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.412× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.591× (z -9.0) |
| [[A498 (line)]] | wt | 410 | 4 (4 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.68× (z +20.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.548× (z -10.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 148 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.427× (z -13.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.584× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 272 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -14.5) ⚠ cell-cycle shift, explains ~79% of this change |
| [[NCI-H2347 (line)]] | alt | 244 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -22.2) |
| [[A549 (line)]] | wt | 168 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.17× (z +24.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 221 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.446× (z -10.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.593× (z -9.7) |
| [[Hs 766T (line)]] | wt | 256 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -13.9) |
| [[J82 (line)]] | alt | 224 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.11× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.582× (z -10.9) |
| [[A-427 (line)]] | wt | 96.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 177 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -20.1) |
| [[HS-578T (line)]] | alt | 402 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -14.4) |
| [[KATO III (line)]] | alt | 259 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -12.5) |
| [[SW 900 (line)]] | alt | 246 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -11.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.506× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 183 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +11.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 162 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.96× (z +8.6) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -8.7) ⚠ cell-cycle shift, explains ~79% of this change |
| [[NCI-H2030 (line)]] | alt | 123 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.615× (z -8.6) |
| [[PANC-1 (line)]] | alt | 90.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +14.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 185 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -13.7) |
| [[SNU-1 (line)]] | wt | 140 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -8.5) |
| [[SNU-423 (line)]] | alt | 130 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +10.3) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 143 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.577× (z -9.8) |
| [[COLO 205 (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 192 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -10.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[hTERT-HPNE (line)]] | wt | 199 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.436× (z -9.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LOX-IMVI (line)]] | wt | 160 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 45.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +11.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 160 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -13.7) |
| [[RKO (line)]] | wt | 284 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 146 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -9.3) |
| [[AN3 CA (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 149 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 88.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 110 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 852), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED2]] | +0.68 | +0.69 / +0.72 | both halves | 7e-06 | STRING 534 |
| [[UBE2J1]] | +0.66 | +0.56 / +0.72 | both halves | 1e-05 | **novel candidate** |
| [[OSTC]] | +0.62 | +0.69 / +0.56 | both halves | 1e-05 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[STT3A]] | +0.60 | +0.59 / +0.64 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[RPN1]] | +0.59 | +0.60 / +0.64 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 819 |
| [[SH3GLB1]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CANX]] | +0.58 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[SEL1L]] | +0.56 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[DNAJC3]] | +0.56 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PCGF5]] | +0.55 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[TMED10]] | +0.55 | +0.57 / +0.59 | both halves | 9e-06 | STRING 453 |
| [[SSR3]] | +0.55 | +0.63 / +0.51 | both halves | 1e-05 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 699 |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H18]] | -0.50 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[SMG9]] | -0.49 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[ZNF274]] | -0.49 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[PWP2]] | -0.48 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[MAP3K14]] | -0.48 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[ARMC5]] | -0.47 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[PRPF38B]] | -0.47 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[HES1]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[NOP56]] | -0.46 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[ZNF43]] | -0.46 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[FBXO46]] | -0.45 | -0.34 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TRAM1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.543). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.1, -39.2); signed map (-57.0, 11.7). **Vector** length 131, 43.3% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.50 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.3 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.1 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.2 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +5.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.0 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.6 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.8 | +0.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.8 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -10.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.1 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +0.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.7 | -2.8 |
|  | [[Tirabrutinib (drug)]] 0.5 µM |  | -2.7 | -2.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.6 | -1.2 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | translocation associated membrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.3 — chr8:70,573,218-70,608,416 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRAM, TRAMP |
| Gene groups (HGNC) | TLC domain containing |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15629](https://www.uniprot.org/uniprotkb/Q15629) (Translocating chain-associated membrane protein 1):

> Involved in the translocation of nascent protein chains into or through the endoplasmic reticulum (ER) membrane by facilitating the proper chain positioning at the SEC61 channel. Regulates the exposure of nascent secretory protein chain to the cytosol during translocation into the ER. May affect the phospholipid bilayer in the vicinity of the lateral gate of the SEC61 channel, thereby facilitating ER protein transport. Intimately associates with transmembrane (TM) domain of nascent membrane …

**Summary**, from NCBI Gene [23471](https://www.ncbi.nlm.nih.gov/gene/23471):

> This gene encodes a multi-pass membrane protein that is part of the mammalian endoplasmic reticulum. The encoded protein influences glycosylation and facilitates the translocation of secretory proteins across the endoplasmic reticulum membrane by regulating which domains of the nascent polypeptide chain are visible to the cytosol during a translocational pause. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:20568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20568) · Entrez [23471](https://www.ncbi.nlm.nih.gov/gene/23471) · UniProt [Q15629](https://www.uniprot.org/uniprotkb/Q15629) · Ensembl [ENSG00000067167](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067167)

## Data

Gene col 852: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 852); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 852, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 852]; `tensor/DDL_lfc|DDL_z.npy` [852]; `embed/gene_vectors.npy` [852]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 852 or target_col == 852). Every well: [[TRAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
