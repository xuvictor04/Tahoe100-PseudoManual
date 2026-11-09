---
symbol: "INSIG2"
type: "gene"
col: 4633
ensembl_id: "ENSG00000125629"
name: "insulin induced gene 2"
location: "2q14.1-q14.2"
module: 99
arm: "+"
pooled_cpm: 171.6
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 33
n_dd_up_clean: 5
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# INSIG2

*insulin induced gene 2* — 2q14.1-q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Pravastatin (sodium) (drug)]] 5 µM: 1.41× (z +4.8, q 9e-04, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.130× (z -41.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR45B]] (+0.85, fdr 7e-06), [[FAM162A]] (+0.83, fdr 7e-06), [[PDK3]] (+0.83, fdr 7e-06); moves opposite to [[CPLANE1]] (-0.66, fdr 7e-06), [[ITPA]] (-0.65, fdr 3e-05), [[PARVA]] (-0.65, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RAB20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4633.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.41×** | +4.8 | 9e-04 | 39/48 (HEC-1-A, SW 900, …) | rises with dose | plate-row cell shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +4.5 | 0.002 | 29/49 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.35×** | +4.2 | 0.006 | 34/49 (HEC-1-A, HT-29, …) | top dose only | plate-row cell shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.70×** | +4.0 | 0.009 | 32/48 (SNU-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.095 | 27/49 (HEC-1-A, SHP-77, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4633.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.130×** | -41.8 | 0e+00 | 48/48 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.165×** | -25.0 | 0e+00 | 48/48 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.219×** | -21.9 | 0e+00 | 48/48 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.329×** | -16.1 | 0e+00 | 46/49 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.326×** | -15.6 | 0e+00 | 44/44 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.423×** | -11.9 | 7e-31 | 46/47 (HepG2/C3A, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.438×** | -11.5 | 2e-28 | 45/47 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.581×** | -11.1 | 1e-26 | 41/49 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.571×** | -8.1 | 3e-14 | 38/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.576×** | -8.0 | 9e-14 | 36/48 (HEC-1-A, AsPC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.607×** | -7.2 | 3e-11 | 46/48 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.586×** | -7.1 | 4e-11 | 37/45 (A-172, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.724×** | -6.6 | 2e-09 | 40/48 (HepG2/C3A, SNU-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.638×** | -6.2 | 2e-08 | 37/48 (C32, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.737×** | -6.2 | 2e-08 | 36/48 (SNU-423, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.702×** | -5.1 | 1e-05 | 44/48 (Hs 766T, A549, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -4.9 | 3e-05 | 32/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.724×** | -4.7 | 1e-04 | 34/48 (C32, PANC-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.765×** | -3.9 | 0.003 | 33/48 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.767×** | -3.8 | 0.003 | 30/48 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.775×** | -3.7 | 0.005 | 30/49 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.772×** | -3.5 | 0.009 | 27/48 (SNU-423, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.787×** | -3.4 | 0.012 | 26/49 (HT-29, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.788×** | -3.4 | 0.012 | 28/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4633. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 267 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -37.4) |
| [[CFPAC-1 (line)]] | alt | 335 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0978× (z -41.4) |
| [[HepG2_C3A (line)]] | wt | 387 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0684× (z -35.2) |
| [[A-172 (line)]] | wt | 247 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0627× (z -40.8) |
| [[C32 (line)]] | wt | 289 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0503× (z -44.6) |
| [[AsPC-1 (line)]] | alt | 219 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0459× (z -46.4) |
| [[Hs 766T (line)]] | wt | 220 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -32.1) |
| [[NCI-H1792 (line)]] | alt | 188 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -35.6) |
| [[NCI-H2347 (line)]] | alt | 170 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0884× (z -40.7) |
| [[RPMI-7951 (line)]] | alt | 303 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0672× (z -36.8) |
| [[SW 900 (line)]] | alt | 274 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -32.5) |
| [[H4 (line)]] | wt | 297 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0494× (z -35.9) |
| [[LOX-IMVI (line)]] | wt | 147 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0886× (z -34.5) |
| [[NCI-H1573 (line)]] | alt | 162 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0491× (z -25.4) |
| [[SK-MEL-2 (line)]] | alt | 154 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -27.9) |
| [[A549 (line)]] | wt | 159 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -22.8) |
| [[BT-474 (line)]] | alt | 88.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.2) |
| [[HCT15 (line)]] | alt | 325 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -25.5) |
| [[LS 180 (line)]] | wt | 176 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -27.5) |
| [[NCI-H460 (line)]] | wt | 148 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0841× (z -38.3) |
| [[SNU-1 (line)]] | wt | 212 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0474× (z -39.5) |
| [[SNU-423 (line)]] | alt | 173 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -34.9) |
| [[SW480 (line)]] | alt | 154 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -25.2) |
| [[HOP62 (line)]] | alt | 304 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0639× (z -33.7) |
| [[HS-578T (line)]] | alt | 192 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0998× (z -32.7) |
| [[NCI-H23 (line)]] | alt | 82.0 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.00× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0974× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.249× (z -20.9) |
| [[Panc 03.27 (line)]] | alt | 152 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -28.5) |
| [[PANC-1 (line)]] | alt | 99.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -30.8) |
| [[HT-29 (line)]] | alt | 116 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -21.0) |
| [[J82 (line)]] | alt | 171 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -28.8) |
| [[LoVo (line)]] | wt | 133 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -27.6) |
| [[MIA PaCa-2 (line)]] | alt | 154 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -25.6) |
| [[RKO (line)]] | wt | 114 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -23.3) |
| [[SW48 (line)]] | wt | 174 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -19.8) |
| [[A-427 (line)]] | wt | 65.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -14.1) |
| [[C-33 A (line)]] | alt | 212 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -16.2) |
| [[CHP-212 (line)]] | wt | 213 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -13.4) |
| [[COLO 205 (line)]] | alt | 104 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -25.0) |
| [[hTERT-HPNE (line)]] | wt | 115 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.0) |
| [[KATO III (line)]] | alt | 94.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -23.5) |
| [[A498 (line)]] | wt | 105 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -22.2) |
| [[AN3 CA (line)]] | alt | 148 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0906× (z -14.2) |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -23.1) |
| [[SW 1088 (line)]] | alt | 297 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0665× (z -18.9) |
| [[SW1417 (line)]] | alt | 104 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -23.5) |
| [[SHP-77 (line)]] | alt | 106 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.4) |
| [[SW 1271 (line)]] | alt | 163 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0757× (z -18.5) |
| [[NCI-H661 (line)]] | alt | 77.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -12.2) |
| [[NCI-H2122 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 193 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4633), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR45B]] | +0.85 | +0.88 / +0.80 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.83 | +0.85 / +0.78 | both halves | 7e-06 |  |
| [[PDK3]] | +0.83 | +0.86 / +0.75 | both halves | 7e-06 |  |
| [[ERO1A]] | +0.81 | +0.87 / +0.69 | both halves | 7e-06 |  |
| [[PFKFB4]] | +0.81 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[HK2]] | +0.80 | +0.84 / +0.71 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.79 | +0.85 / +0.65 | both halves | 7e-06 |  |
| [[MXI1]] | +0.79 | +0.86 / +0.71 | both halves | 7e-06 |  |
| [[HERC3]] | +0.77 | +0.83 / +0.63 | both halves | 7e-06 |  |
| [[FAM210A]] | +0.77 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[PDK1]] | +0.77 | +0.85 / +0.67 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.76 | +0.75 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPLANE1]] | -0.66 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[ITPA]] | -0.65 | -0.68 / -0.46 | both halves | 3e-05 |  |
| [[PARVA]] | -0.65 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[UTP20]] | -0.65 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[AVEN]] | -0.63 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[TCF12]] | -0.63 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[INO80]] | -0.61 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[DLG5]] | -0.61 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[FKRP]] | -0.61 | -0.65 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB20]] | B | RAB20 activity raises INSIG2's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without RAB20 | 0.032 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[LIMCH1]] | B | LIMCH1 activity raises INSIG2's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.28× lower at baseline in the lines without LIMCH1 | 0.045 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[LINC02575]] | B | LINC02575 activity lowers INSIG2's level | lines that do not express LINC02575 (32) vs lines expressing it (18) | 1.26× higher at baseline in the lines without LINC02575 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000289309, LINC01205, MSRB3-AS1 |
| [[TOP2A]] | B | TOP2A activity raises INSIG2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NDRG1]] | B | NDRG1 activity raises INSIG2's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without NDRG1 | 0.098 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.902). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.4, -16.5); signed map (-36.0, 24.1). **Vector** length 138, 56.1% of its response variance represented; |z| ≥ 3 in 1,470 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.61 to 17); *mTORC1 signaling* (hallmark, mean cos +0.57 to 15); *Glycolysis* (reactome, mean cos +0.58 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +9.0 | -4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +8.0 | -1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +7.6 | -8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +6.9 | -8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.5 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.1 | +4.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +3.5 | +4.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.9 | -25.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.5 | -7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -41.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.2 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.0 | -11.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.9 | -3.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.7 | -5.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.2 | -3.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.9 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | insulin induced gene 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1-q14.2 — chr2:118,088,452-118,110,997 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 3 pathways, smallest: Regulation of cholesterol biosynthesis by SREBP (SREBF); Metabolism of steroids; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5U4](https://www.uniprot.org/uniprotkb/Q9Y5U4) (Insulin-induced gene 2 protein):

> Oxysterol-binding protein that mediates feedback control of cholesterol synthesis by controlling both endoplasmic reticulum to Golgi transport of SCAP and degradation of HMGCR. Acts as a negative regulator of cholesterol biosynthesis by mediating the retention of the SCAP-SREBP complex in the endoplasmic reticulum, thereby blocking the processing of sterol regulatory element-binding proteins (SREBPs) SREBF1/SREBP1 and SREBF2/SREBP2. Binds oxysterol, including 22-hydroxycholesterol, …

**Summary**, from NCBI Gene [51141](https://www.ncbi.nlm.nih.gov/gene/51141):

> The protein encoded by this gene is highly similar to the protein product encoded by gene INSIG1. Both INSIG1 protein and this protein are endoplasmic reticulum proteins that block the processing of sterol regulatory element binding proteins (SREBPs) by binding to SREBP cleavage-activating protein (SCAP), and thus prevent SCAP from escorting SREBPs to the Golgi. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20452) · Entrez [51141](https://www.ncbi.nlm.nih.gov/gene/51141) · UniProt [Q9Y5U4](https://www.uniprot.org/uniprotkb/Q9Y5U4) · Ensembl [ENSG00000125629](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125629)

## Data

Gene col 4633: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4633); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4633, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4633]; `tensor/DDL_lfc|DDL_z.npy` [4633]; `embed/gene_vectors.npy` [4633]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4633 or target_col == 4633). Every well: [[INSIG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INSIG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
