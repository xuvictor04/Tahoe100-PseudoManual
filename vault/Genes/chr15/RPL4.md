---
symbol: "RPL4"
type: "gene"
col: 10493
ensembl_id: "ENSG00000174444"
name: "ribosomal protein L4"
location: "15q22.31"
module: 20
arm: "+"
pooled_cpm: 250.5
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# RPL4

*ribosomal protein L4* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.70× (z +13.6, q 2e-39, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.19× (z +5.6, q 2e-06, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Isocorydine (drug)]] 0.5 µM: 0.726× (z -4.4, q 0.004, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL3]] (+0.87, fdr 7e-06), [[EEF1A1P5]] (+0.84, fdr 7e-06), [[RPS18]] (+0.83, fdr 7e-06); moves opposite to [[ZNF503]] (-0.61, fdr 1e-05), [[CROCCP2-1]] (-0.57, fdr 1e-05), [[RBX1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LDHB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10493.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +13.6 | 2e-39 | 49/49 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +13.2 | 4e-37 | 43/44 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.29×** | +12.2 | 7e-32 | 47/50 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +9.4 | 1e-18 | 44/45 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.52×** | +5.7 | 1e-06 | 41/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.19×** | +5.6 | 2e-06 | 45/49 (COLO 205, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.47×** | +5.3 | 1e-05 | 41/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.2 | 2e-05 | 39/47 (COLO 205, Hs 766T, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +4.1 | 0.002 | 28/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.003 | 34/48 (RPMI-7951, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.005 | 35/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.21×** | +3.6 | 0.018 | 21/49 (NCI-H2347, HepG2/C3A, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.023 | 32/48 (HT-29, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.28×** | +3.4 | 0.023 | 31/48 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.28×** | +3.4 | 0.023 | 25/48 (NCI-H460, COLO 205, …) | rises with dose | position effect removed |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.023 | 34/48 (NCI-H460, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.039 | 35/47 (A-172, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.042 | 27/47 (NCI-H460, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.042 | 33/48 (KATO III, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Lucanthone (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.055 | 31/48 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10493.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Isocorydine (drug)]] 0.5 µM |  | **0.726×** | -4.4 | 0.004 | 41/48 (HT-29, HCT15, …) | inconsistent across doses | position effect removed |
| [[Sulfisoxazole (drug)]] 5 µM |  | **0.794×** | -4.4 | 0.004 | 41/48 (C-33 A, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **0.799×** | -3.8 | 0.023 | 40/48 (HT-29, LS 180, …) | rises with dose | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.764×** | -3.7 | 0.032 | 37/48 (KATO III, HT-29, …) | inconsistent across doses | position effect removed |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | **0.828×** | -3.4 | 0.074 | 27/48 (C-33 A, Panc 03.27, …) | rises with dose | position effect removed |
| [[Bergenin (drug)]] 5 µM |  | 0.838× | -3.2 | 0.13 | 17/49 (MIA PaCa-2, SHP-77, …) | rises with dose | position effect removed |
| [[Dorzolamide (hydrochloride) (drug)]] 5 µM |  | 0.788× | -3.1 | 0.14 | 30/48 (J82, NCI-H2030, …) | top dose only | position effect removed |
| [[Busulfan (drug)]] 0.5 µM |  | 0.802× | -3.0 | 0.14 | 29/49 (HOP62, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.832× | -3.0 | 0.14 | 24/48 (C-33 A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10493. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 199 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 225 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +13.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 280 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.46× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 282 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.2) |
| [[A-172 (line)]] | wt | 99.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +11.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 207 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.07× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -9.2) ⚠ cell-cycle shift, explains ~70% of this change |
| [[A498 (line)]] | wt | 166 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +13.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 379 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +14.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 299 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -10.5) |
| [[HOP62 (line)]] | alt | 190 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.46× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 339 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +12.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 589 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +14.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 180 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +14.3) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 330 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.76× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.419× (z -8.8) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SNU-423 (line)]] | alt | 192 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.67× (z +14.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 161 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 135 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 200 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 298 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 228 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 276 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +10.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 172 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 138 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +10.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 150 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 370 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 265 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +12.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 244 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +11.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 295 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +11.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 359 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 135 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 355 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +9.7) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 243 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +8.5) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.05× (z +13.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 226 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 240 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 228 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 312 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.5) ⚠ cell-cycle shift, explains ~9% of this change | — |
| [[SHP-77 (line)]] | alt | 276 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 193 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +10.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 255 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 288 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 368 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 192 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10493), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL3]] | +0.87 | +0.86 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[EEF1A1P5]] | +0.84 | +0.85 / +0.81 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation |
| [[RPS18]] | +0.83 | +0.79 / +0.81 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[EEF1A1]] | +0.82 | +0.81 / +0.84 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 997 |
| [[RPL10]] | +0.76 | +0.71 / +0.77 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[EEF1G]] | +0.75 | +0.75 / +0.73 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 983 |
| [[RPL14]] | +0.75 | +0.69 / +0.79 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3A]] | +0.74 | +0.70 / +0.73 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL29]] | +0.74 | +0.76 / +0.68 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[EEF2]] | +0.73 | +0.64 / +0.79 | both halves | 7e-06 | same gene group; pathway: Eukaryotic Translation Elongation; STRING 999 |
| [[RPL18A]] | +0.72 | +0.63 / +0.70 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[HNRNPA1]] | +0.71 | +0.69 / +0.76 | both halves | 7e-06 | STRING 623 |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF503]] | -0.61 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.57 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[RBX1]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 | pathway: Regulation of expression of SLITs and ROBOs |
| [[IRX5]] | -0.55 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ERVK3-1]] | -0.54 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[EID2]] | -0.53 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[DOHH]] | -0.53 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.52 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[MIDN]] | -0.51 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[EFNA2]] | -0.50 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ISG20L2]] | -0.50 | -0.45 / -0.51 | both halves | 3e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 418 |
| [[PIGBOS1]] | -0.49 | -0.54 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDHB]] | B | LDHB activity raises RPL4's level | lines that do not express LDHB (7) vs lines expressing it (43) | 1.30× lower at baseline in the lines without LDHB | 0.089 | ⚠ within organs, on part of the lines; also absent: E2F7, ANKRD44, TMOD2; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.634). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.4, -25.4); signed map (-21.9, -34.1). **Vector** length 105, 35.7% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosomal scanning and start codon recognition* (reactome, mean cos +0.65 to 6); *Translation initiation complex formation* (reactome, mean cos +0.65 to 6); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.65 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +0.7 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +3.4 | +0.9 |
|  | [[Erlotinib (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | -0.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.9 | +5.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.8 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.8 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.0 | -3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.5 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -4.1 | +1.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.8 | -1.5 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -3.0 | +0.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.8 | -0.3 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:66,498,015-66,524,532 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L4, uL4 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P36578](https://www.uniprot.org/uniprotkb/P36578) (Large ribosomal subunit protein uL4):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6124](https://www.ncbi.nlm.nih.gov/gene/6124):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L4E family of ribosomal proteins. It is located in the cytoplasm. As is typical for genes encoding ribosomal proteins, there are multiple processed pseudogenes of this gene …

**Accessions** — [HGNC:10353](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10353) · Entrez [6124](https://www.ncbi.nlm.nih.gov/gene/6124) · UniProt [P36578](https://www.uniprot.org/uniprotkb/P36578) · Ensembl [ENSG00000174444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174444)

## Data

Gene col 10493: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10493); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10493, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10493]; `tensor/DDL_lfc|DDL_z.npy` [10493]; `embed/gene_vectors.npy` [10493]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10493 or target_col == 10493). Every well: [[RPL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
