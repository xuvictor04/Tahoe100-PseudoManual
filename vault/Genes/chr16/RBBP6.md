---
symbol: "RBBP6"
type: "gene"
col: 4326
ensembl_id: "ENSG00000122257"
name: "RB binding protein 6, ubiquitin ligase"
location: "16p12.1"
module: 188
arm: "+"
pooled_cpm: 168.79
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# RBBP6

*RB binding protein 6, ubiquitin ligase* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +16.3, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.653× (z -8.1, q 4e-13, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.742× (z -5.9, q 6e-07, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SON]] (+0.80, fdr 7e-06), [[MZF1-AS1]] (+0.74, fdr 1e-05), [[ARMC5]] (+0.71, fdr 7e-06); moves opposite to [[NDRG3]] (-0.72, fdr 7e-06), [[AKTIP]] (-0.68, fdr 1e-05), [[GPD1L]] (-0.68, fdr 7e-06).
> It is in [[Module 188]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4326.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +16.3 | 0e+00 | 43/48 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +13.3 | 4e-38 | 43/49 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +9.2 | 1e-17 | 39/48 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +5.7 | 1e-06 | 34/48 (A-172, RKO, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.20×** | +3.6 | 0.040 | 24/48 (A-172, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.4 | 0.057 | 21/48 (KATO III, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.3 | 0.081 | 13/48 (SW1417, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.18× | +3.0 | 0.18 | 21/48 (A549, SK-MEL-2, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4326.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.653×** | -8.1 | 4e-13 | 36/44 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.676×** | -7.7 | 4e-12 | 36/49 (NCI-H23, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.707×** | -6.3 | 5e-08 | 28/45 (C-33 A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.742×** | -5.9 | 6e-07 | 30/48 (LoVo, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.755×** | -5.5 | 3e-06 | 28/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.803×** | -4.3 | 0.001 | 26/48 (RKO, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -4.3 | 0.002 | 18/48 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.809×** | -4.2 | 0.002 | 25/48 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Folic acid (drug)]] 5 µM |  | 0.875× | -3.7 | 0.012 | 7/48 (NCI-H460, NCI-H1573, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.3 | 0.062 | 16/49 (SW480, KATO III, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.851× | -3.1 | 0.12 | 17/49 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 218 | 5 (3 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +23.2) | [[Panobinostat (drug)]] 0.5 µM 0.473× (z -11.6) |
| [[PANC-1 (line)]] | alt | 169 | 2 | 6 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +16.4) | [[Digitoxin (drug)]] 5 µM 0.465× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 165 | 4 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.494× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 217 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +25.0) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -19.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 109 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +22.0) | — |
| [[KATO III (line)]] | alt | 223 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.443× (z -12.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 202 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 172 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +21.6) | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 197 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -13.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 172 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.367× (z -12.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 124 | 2 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.65× (z +11.2) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.47× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -10.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 215 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.404× (z -10.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 175 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +21.3) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -13.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 150 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +18.5) | — |
| [[LS 180 (line)]] | wt | 182 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.1) | [[Harringtonine (drug)]] 5 µM 0.515× (z -9.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H2030 (line)]] | alt | 171 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +16.5) | — |
| [[NCI-H2347 (line)]] | alt | 64.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +11.1) | — |
| [[RKO (line)]] | wt | 236 | 2 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 1.94× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.538× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 155 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.2) | — |
| [[SK-MEL-2 (line)]] | alt | 139 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +24.9) | — |
| [[SNU-1 (line)]] | wt | 166 | 2 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.09× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -12.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 154 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -11.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 173 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -14.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 224 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.56× (z +15.0) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.8) | — |
| [[BT-474 (line)]] | alt | 188 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.409× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.447× (z -8.6) |
| [[C32 (line)]] | wt | 138 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +23.3) | — |
| [[CFPAC-1 (line)]] | alt | 154 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.1) | — |
| [[COLO 205 (line)]] | alt | 201 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.6) | — |
| [[H4 (line)]] | wt | 164 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -9.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 283 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.499× (z -9.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 165 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -22.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 223 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +13.3) | — |
| [[HOP62 (line)]] | alt | 112 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +17.9) | — |
| [[J82 (line)]] | alt | 164 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +12.1) | — |
| [[NCI-H460 (line)]] | wt | 177 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.500× (z -10.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 154 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +16.4) | — |
| [[C-33 A (line)]] | alt | 274 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -15.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 188 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.294× (z -9.3) |
| [[Hs 766T (line)]] | wt | 199 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +12.5) | — |
| [[Panc 03.27 (line)]] | alt | 111 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +12.9) | — |
| [[SW1417 (line)]] | alt | 142 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +15.6) | — |
| [[SW48 (line)]] | wt | 116 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +8.6) | — |
| [[A-427 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SON]] | +0.80 | +0.78 / +0.69 | both halves | 7e-06 | STRING 872 |
| [[MZF1-AS1]] | +0.74 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[ARMC5]] | +0.71 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ANKHD1-EIF4EBP3]] | +0.71 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[TOPORS]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 | same gene group |
| [[TRIP11]] | +0.70 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[BPTF]] | +0.70 | +0.83 / +0.53 | both halves | 1e-05 |  |
| [[BOLA1]] | +0.70 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[C6orf62]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ASH1L]] | +0.68 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[PCF11]] | +0.68 | +0.77 / +0.43 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 917 |
| [[CFAP53]] | +0.67 | +0.72 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | -0.72 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[AKTIP]] | -0.68 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[GPD1L]] | -0.68 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[FAR1]] | -0.67 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[GCSH]] | -0.67 | -0.73 / -0.44 | both halves | 3e-05 |  |
| [[HDAC1]] | -0.66 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[CTC1]] | -0.66 | -0.66 / -0.68 | both halves | 7e-06 |  |
| [[RPA1]] | -0.65 | -0.71 / -0.49 | both halves | 1e-05 |  |
| [[STX7]] | -0.64 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[NDFIP1]] | -0.63 | -0.70 / -0.60 | both halves | 7e-06 |  |
| [[SKIC3]] | -0.62 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[MRS2]] | -0.61 | -0.51 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RBBP6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction -0.764). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.0, -5.6); signed map (20.6, -9.0). **Vector** length 153, 50.9% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +16.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.9 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +13.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +1.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -11.4 | -7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -10.8 | -8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.5 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.1 | -5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.7 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.9 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.6 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.0 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | RB binding protein 6, ubiquitin ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.1 — chr16:24,537,693-24,572,863 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P2P-R, PACT, SNAMA |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 12 pathways, smallest: RHOBTB1 GTPase cycle; RHOBTB GTPase Cycle; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6E9](https://www.uniprot.org/uniprotkb/Q7Z6E9) (E3 ubiquitin-protein ligase RBBP6):

> E3 ubiquitin-protein ligase which promotes ubiquitination of YBX1, leading to its degradation by the proteasome. May play a role as a scaffold protein to promote the assembly of the p53/TP53-MDM2 complex, resulting in increase of MDM2-mediated ubiquitination and degradation of p53/TP53; may function as negative regulator of p53/TP53, leading to both apoptosis and cell growth (By similarity). Regulates DNA-replication and the stability of chromosomal common fragile sites (CFSs) in a ZBTB38- and …

**Summary**, from NCBI Gene [5930](https://www.ncbi.nlm.nih.gov/gene/5930):

> The retinoblastoma tumor suppressor (pRB) protein binds with many other proteins. In various human cancers, pRB suppresses cellular proliferation and is inactivated. Cell cycle-dependent phosphorylation regulates the activity of pRB. This gene encodes a protein which binds to underphosphorylated but not phosphorylated pRB. Multiple alternatively spliced transcript variants that encode different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9889](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9889) · Entrez [5930](https://www.ncbi.nlm.nih.gov/gene/5930) · UniProt [Q7Z6E9](https://www.uniprot.org/uniprotkb/Q7Z6E9) · Ensembl [ENSG00000122257](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122257)

## Data

Gene col 4326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4326); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4326]; `tensor/DDL_lfc|DDL_z.npy` [4326]; `embed/gene_vectors.npy` [4326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4326 or target_col == 4326). Every well: [[RBBP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBBP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
