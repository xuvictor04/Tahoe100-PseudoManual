---
symbol: "ANP32E"
type: "gene"
col: 6737
ensembl_id: "ENSG00000143401"
name: "acidic nuclear phosphoprotein 32 family member E"
location: "1q21.2"
module: 22
arm: "+"
pooled_cpm: 95.15
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# ANP32E

*acidic nuclear phosphoprotein 32 family member E* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.79× (z +19.5, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.57× (z +5.6, q 2e-06, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.669× (z -5.0, q 3e-04, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRC1]] (+0.66, fdr 7e-06), [[KIF11]] (+0.65, fdr 7e-06), [[HNRNPA2B1]] (+0.63, fdr 7e-06); moves opposite to [[BRI3]] (-0.61, fdr 7e-06), [[FAU]] (-0.56, fdr 1e-05), [[DNLZ]] (-0.54, fdr 3e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6737.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.79×** | +19.5 | 0e+00 | 49/49 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.82×** | +18.8 | 0e+00 | 44/44 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.41×** | +14.1 | 6e-43 | 45/45 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +6.9 | 8e-10 | 10/50 (HOP62, J82, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +5.6 | 2e-06 | 40/48 (COLO 205, NCI-H1573, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **1.55×** | +5.4 | 5e-06 | 40/47 (HT-29, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +5.1 | 3e-05 | 37/48 (COLO 205, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.21×** | +3.4 | 0.046 | 20/48 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.31×** | +3.3 | 0.052 | 27/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.076 | 25/48 (SW 900, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6737.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.669×** | -5.0 | 3e-04 | 30/48 (AN3 CA, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **0.759×** | -4.9 | 3e-04 | 29/48 (A-427, LS 180, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **0.703×** | -4.4 | 0.002 | 30/48 (SW 900, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.724×** | -4.0 | 0.006 | 30/48 (SW 900, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.724×** | -4.0 | 0.006 | 30/48 (SW 900, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.572×** | -3.6 | 0.026 | 33/49 (SNU-1, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.826×** | -3.4 | 0.060 | 21/48 (MIA PaCa-2, HCT15, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.766×** | -3.3 | 0.064 | 29/48 (A498, A-427, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.843× | -3.0 | 0.17 | 18/49 (NCI-H1573, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6737. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 175 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +14.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.370× (z -10.2) |
| [[A-172 (line)]] | wt | 68.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.40× (z +19.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 64.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.0× (z +18.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 115 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +17.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 88.7 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +17.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 130 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 66.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +15.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 81.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +14.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 122 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.35× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 129 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +17.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 82.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.83× (z +17.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 56.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +13.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 62.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +16.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 81.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +12.8) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 73.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +13.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 97.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +17.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 64.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +15.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 55.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.24× (z +14.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 74.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.31× (z +15.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 104 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +14.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 116 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.18× (z +16.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 56.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.68× (z +15.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 70.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.9× (z +19.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 135 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +14.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 129 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +12.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 50.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.71× (z +15.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 66.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +13.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 49.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +14.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 158 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 52.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.80× (z +12.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 185 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +10.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 88.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.93× (z +14.0) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 134 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +9.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 81.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.11× (z +8.9) | — |
| [[H4 (line)]] | wt | 81.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 140 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.64× (z +16.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 206 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.00× (z +12.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 64.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.86× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 53.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 111 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 239 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +11.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 104 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +15.6) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 72.6 | 0 | 1 | — | [[Ranolazine (drug)]] 0.05 µM 0.0822× (z -8.5) |
| [[BT-474 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6737), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRC1]] | +0.66 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[KIF11]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[HNRNPA2B1]] | +0.63 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[INCENP]] | +0.62 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[BUB1B]] | +0.62 | +0.54 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[ARHGAP11A]] | +0.61 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[TMPO]] | +0.61 | +0.53 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[KIF14]] | +0.61 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[NCAPG]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[CIP2A]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[RRM1]] | +0.59 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[NUSAP1]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRI3]] | -0.61 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[FAU]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[DNLZ]] | -0.54 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ASTN2]] | -0.53 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[GAS5]] | -0.53 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[SNHG25]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ZFAS1]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[CIAO2B]] | -0.50 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[ZBTB43]] | -0.50 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[COMMD6]] | -0.50 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[NOP10]] ⚠ | -0.50 | -0.35 / -0.53 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS13]] ⚠ | -0.50 | -0.47 / -0.49 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RRAGC]] | -0.50 | -0.46 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ANP32E's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.2, -54.0); signed map (-48.3, -45.2). **Vector** length 109, 37.2% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.53 to 8); *Kinesins* (reactome, mean cos +0.51 to 10); *Initiation of Nuclear Envelope (NE) Reformation* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +5.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +1.2 |
|  | [[Furosemide (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Decitabine (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.0 | +1.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | -5.2 | -4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.6 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.4 | -1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -4.4 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.8 | -3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.7 | +0.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | acidic nuclear phosphoprotein 32 family member E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:150,218,417-150,236,156 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LANPL, MGC5350, LANP-L |
| Gene groups (HGNC) | ANP32 acidic nuclear phosphoproteins |
| Hallmark sets | PROTEIN_SECRETION, E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTT0](https://www.uniprot.org/uniprotkb/Q9BTT0) (Acidic leucine-rich nuclear phosphoprotein 32 family member E):

> Histone chaperone that specifically mediates the genome-wide removal of histone H2A.Z/H2AZ1 from the nucleosome: removes H2A.Z/H2AZ1 from its normal sites of deposition, especially from enhancer and insulator regions. Not involved in deposition of H2A.Z/H2AZ1 in the nucleosome. May stabilize the evicted H2A.Z/H2AZ1-H2B dimer, thus shifting the equilibrium towards dissociation and the off-chromatin state. Inhibits activity of protein phosphatase 2A (PP2A). Does not inhibit protein phosphatase 1. …

**Summary**, from NCBI Gene [81611](https://www.ncbi.nlm.nih.gov/gene/81611):

> Enables histone binding activity; histone chaperone activity; and protein folding chaperone. Predicted to be involved in regulation of apoptotic process. Located in nucleus. Part of Swr1 complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16673](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16673) · Entrez [81611](https://www.ncbi.nlm.nih.gov/gene/81611) · UniProt [Q9BTT0](https://www.uniprot.org/uniprotkb/Q9BTT0) · Ensembl [ENSG00000143401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143401)

## Data

Gene col 6737: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6737); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6737, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6737]; `tensor/DDL_lfc|DDL_z.npy` [6737]; `embed/gene_vectors.npy` [6737]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6737 or target_col == 6737). Every well: [[ANP32E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANP32E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
