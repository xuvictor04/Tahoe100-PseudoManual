---
symbol: "SAMHD1"
type: "gene"
col: 2121
ensembl_id: "ENSG00000101347"
name: "SAM and HD domain containing deoxynucleoside triphosphate triphosphohydrolase 1"
location: "20q11.23"
module: 32
arm: "+"
pooled_cpm: 56.25
n_lines_expressing: 47
n_dd_up: 34
n_dd_down: 25
n_dd_up_clean: 25
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 60
direction_downstream: 12
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# SAMHD1

*SAM and HD domain containing deoxynucleoside triphosphate triphosphohydrolase 1* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.98× (z +8.2, q 1e-13, up in 21 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.59× (z +5.8, q 2e-06, up in 21 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.503× (z -12.1, q 5e-31, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OAS2]] (+0.90, fdr 7e-06), [[OAS3]] (+0.89, fdr 7e-06), [[PARP9]] (+0.89, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 60 arrows point to it, the strongest [[IFI6]] → it (grade B ⚠); 12 go from it, the strongest it → [[ADAR]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2121.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.98×** | +8.2 | 1e-13 | 21/34 (SW480, J82, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.8 | 2e-06 | 21/44 (HS-578T, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.3 | 2e-05 | 29/45 (LoVo, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.52×** | +5.2 | 3e-05 | 23/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +5.1 | 4e-05 | 26/44 (A549, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **1.50×** | +5.0 | 4e-05 | 22/44 (J82, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.48×** | +4.9 | 7e-05 | 21/45 (SW480, PANC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 7e-04 | 21/44 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.43×** | +4.3 | 9e-04 | 26/45 (CFPAC-1, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.42×** | +4.2 | 0.002 | 22/44 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.38×** | +4.0 | 0.003 | 20/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.003 | 22/45 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.38×** | +3.9 | 0.004 | 24/45 (hTERT-HPNE, Hs 766T, …) | top dose only |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.39×** | +3.9 | 0.004 | 22/45 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.004 | 25/45 (Hs 766T, CFPAC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.004 | 20/45 (HS-578T, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.004 | 22/45 (CFPAC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.009 | 18/45 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.009 | 18/45 (KATO III, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.35×** | +3.5 | 0.012 | 15/45 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.012 | 17/45 (CFPAC-1, SW1417, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2121.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.503×** | -12.1 | 5e-31 | 31/45 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.528×** | -11.3 | 6e-27 | 31/45 (SNU-423, COLO 205, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.432×** | -10.5 | 2e-23 | 32/45 (NCI-H23, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.553×** | -10.4 | 2e-23 | 34/45 (COLO 205, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.491×** | -8.9 | 9e-17 | 30/45 (SNU-423, RPMI-7951, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.488×** | -8.5 | 3e-15 | 36/45 (MIA PaCa-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.618×** | -6.0 | 2e-07 | 31/45 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | **0.435×** | -5.4 | 4e-06 | 26/44 (A549, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.651×** | -5.3 | 6e-06 | 25/45 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.659×** | -5.2 | 1e-05 | 25/45 (SNU-423, HS-578T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.771×** | -4.6 | 2e-04 | 26/45 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.695×** | -4.5 | 3e-04 | 25/45 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.697×** | -4.5 | 3e-04 | 28/45 (BT-474, RKO, …) | rises with dose |  |
| [[Ciclopirox (drug)]] 5 µM |  | **0.804×** | -3.8 | 0.005 | 24/45 (SK-MEL-2, COLO 205, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.728×** | -3.8 | 0.005 | 21/44 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.742×** | -3.7 | 0.007 | 19/45 (COLO 205, Hs 766T, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.744×** | -3.7 | 0.008 | 22/45 (RPMI-7951, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 51.3 | 0 | 9 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.290× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 115 | 0 | 9 | — | [[Tofacitinib (drug)]] 5 µM 0.182× (z -17.3) |
| [[RPMI-7951 (line)]] | alt | 178 | 1 (1 ⚠) | 8 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.41× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Tofacitinib (drug)]] 5 µM 0.282× (z -16.2) |
| [[SNU-423 (line)]] | alt | 138 | 0 | 9 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.243× (z -16.4) |
| [[A498 (line)]] | wt | 102 | 0 | 7 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.305× (z -12.5) |
| [[COLO 205 (line)]] | alt | 148 | 0 | 7 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.168× (z -14.9) |
| [[HS-578T (line)]] | alt | 62.2 | 3 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 8.23× (z +18.4) | [[Tofacitinib (drug)]] 5 µM 0.376× (z -12.1) |
| [[LoVo (line)]] | wt | 62.6 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +8.7) | [[Tofacitinib (drug)]] 5 µM 0.377× (z -10.8) |
| [[SW480 (line)]] | alt | 31.4 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A-172 (line)]] | wt | 130 | 0 | 5 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.261× (z -15.0) |
| [[KATO III (line)]] | alt | 98.0 | 0 | 5 | — | [[Tofacitinib (drug)]] 5 µM 0.304× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 92.1 | 0 | 5 | — | [[Tofacitinib (drug)]] 5 µM 0.373× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 88.5 | 0 | 5 | — | [[Tofacitinib (drug)]] 5 µM 0.230× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 79.6 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +8.6) | [[Tofacitinib (drug)]] 5 µM 0.260× (z -13.8) |
| [[J82 (line)]] | alt | 93.0 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 8.10× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 95.3 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.302× (z -14.2) |
| [[Hs 766T (line)]] | wt | 110 | 0 | 3 | — | [[Bortezomib (drug)]] 0.05 µM 0.258× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 86.9 | 1 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +10.0) | [[Tofacitinib (drug)]] 5 µM 0.406× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 26.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.27× (z +9.3) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[HepG2_C3A (line)]] | wt | 58.8 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.289× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 15.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[PANC-1 (line)]] | alt | 22.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.07× (z +9.4) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[RKO (line)]] | wt | 83.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change · without an alert: [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.266× (z -8.9) |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.71× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | — |
| [[LS 180 (line)]] | wt | 17.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | — |
| [[NCI-H2030 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | — |
| [[SNU-1 (line)]] | wt | 43.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.123× (z -10.8) |
| [[A-427 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OAS2]] | +0.90 | +0.86 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 727 |
| [[OAS3]] | +0.89 | +0.84 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 692 |
| [[PARP9]] | +0.89 | +0.85 / +0.91 | both halves | 7e-06 | STRING 454 |
| [[CMPK2]] | +0.88 | +0.82 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TRIM14]] | +0.88 | +0.80 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 423 |
| [[MX1]] | +0.88 | +0.83 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 765 |
| [[USP18]] | +0.88 | +0.84 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 585 |
| [[OAS1]] | +0.87 | +0.86 / +0.87 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 710 |
| [[XAF1]] | +0.86 | +0.83 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 630 |
| [[STAT1]] | +0.86 | +0.80 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 746 |
| [[IFIT1]] | +0.86 | +0.80 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 825 |
| [[IFI44L]] | +0.86 | +0.77 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*60 arrows, 60 of them with an alert ⚠; grade A 0, B 31, C 29. Shown: the 12 strongest; 48 more arrows (48 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI6]] | B | IFI6 activity raises SAMHD1's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.32× lower at baseline in the lines without IFI6 | 0.006 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[SLC15A3]] | B | SLC15A3 activity strengthens SAMHD1's drug response | lines that do not express SLC15A3 (16) vs lines expressing it (29) | the lines without SLC15A3 respond 0.43× as strongly (z diff +2.11); strongest at Selinexor 5 µM: 0.74x vs 0.49x (z diff +4.2) | 0.008 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4; target measured in part of the lines; artifact flags |
| [[OAS2]] | B | OAS2 activity strengthens SAMHD1's drug response | lines that do not express OAS2 (13) vs lines expressing it (32) | the lines without OAS2 respond 0.34× as strongly (z diff +2.04); strongest at Bortezomib 0.05 µM: 0.65x vs 0.37x (z diff +3.6) | 0.014 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; the reference differs; artifact flags |
| [[RASGRP3]] | B | RASGRP3 activity raises SAMHD1's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 1.92× lower at baseline in the lines without RASGRP3 | 0.018 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity raises SAMHD1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.99× lower at baseline in the lines without OAS2 | 0.018 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[OAS1]] | B | OAS1 activity raises SAMHD1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.25× lower at baseline in the lines without OAS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[BATF2]] | B | BATF2 activity raises SAMHD1's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.01× lower at baseline in the lines without BATF2 | 0.023 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[EPSTI1]] | B | EPSTI1 activity raises SAMHD1's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without EPSTI1 | 0.027 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[SAMD9]] | B | SAMD9 activity raises SAMHD1's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without SAMD9 | 0.030 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[LMO2]] | B | LMO2 activity raises SAMHD1's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 1.86× lower at baseline in the lines without LMO2 | 0.032 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity strengthens SAMHD1's drug response | lines that do not express IFI6 (12) vs lines expressing it (33) | the lines without IFI6 respond 0.28× as strongly (z diff +2.32); strongest at Bortezomib 0.05 µM: 0.66x vs 0.38x (z diff +4.0) | 0.033 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |
| [[OAS1]] | B | OAS1 activity strengthens SAMHD1's drug response | lines that do not express OAS1 (12) vs lines expressing it (33) | the lines without OAS1 respond 0.34× as strongly (z diff +2.02); strongest at Bortezomib 0.05 µM: 0.67x vs 0.37x (z diff +4.2) | 0.036 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAR]] | C | SAMHD1's natural level strengthens ADAR's drug response | SAMHD1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.71; direction not clear | 0.017 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP10]] | C | SAMHD1's natural level strengthens PARP10's drug response | SAMHD1's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.71; direction not clear | 0.020 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HERC6]] | C | SAMHD1's natural level strengthens HERC6's drug response | SAMHD1's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.78; direction not clear | 0.022 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | SAMHD1's natural level strengthens USP18's drug response | SAMHD1's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.75; direction not clear | 0.025 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF9]] | C | SAMHD1's natural level strengthens IRF9's drug response | SAMHD1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.77; direction not clear | 0.025 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | SAMHD1's natural level strengthens PARP12's drug response | SAMHD1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.83; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | SAMHD1's natural level strengthens HELZ2's drug response | SAMHD1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.80; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[STAT1]] | C | SAMHD1's natural level strengthens STAT1's drug response | SAMHD1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.79; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PSMB9]] | C | SAMHD1's natural level strengthens PSMB9's drug response | SAMHD1's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.60; direction not clear | 0.079 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[IFIT1]] | C | SAMHD1's natural level strengthens IFIT1's drug response | SAMHD1's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.48; direction not clear | 0.083 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIH1]] | C | SAMHD1 activity raises IFIH1's level | lines that do not express SAMHD1 (3) vs lines expressing it (47) | 2.26× lower at baseline in the lines without SAMHD1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM2, IL27RA, SLC38A1; maybe low, not absent; its own permutation p |
| [[TAP2]] | C | SAMHD1 activity raises TAP2's level | lines that do not express SAMHD1 (3) vs lines expressing it (47) | 1.90× lower at baseline in the lines without SAMHD1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM2, IL27RA, SLC38A1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.887). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.2, 54.4); signed map (65.5, 32.3). **Vector** length 146, 50.1% of its response variance represented; |z| ≥ 3 in 1,376 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.75 to 56); *interferon* (control, mean cos +0.83 to 23); *Interferon gamma signaling* (reactome, mean cos +0.74 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +5.8 | +5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.4 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +5.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.6 | +2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.6 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | -1.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.8 | -10.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -10.3 | -12.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -9.2 | -11.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.5 | -10.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -8.3 | -8.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.6 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | SAM and HD domain containing deoxynucleoside triphosphate triphosphohydrolase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:36,890,229-36,951,893 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SBBI88, Mg11, HDDC1, MOP-5, AGS5 |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 5 pathways, smallest: Nucleotide catabolism; Interferon alpha/beta signaling; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3Z3](https://www.uniprot.org/uniprotkb/Q9Y3Z3) (Deoxynucleoside triphosphate triphosphohydrolase SAMHD1):

> Protein that acts both as a host restriction factor involved in defense response to virus and as a regulator of DNA end resection at stalled replication forks. Has deoxynucleoside triphosphate (dNTPase) activity, which is required to restrict infection by viruses, such as HIV-1: dNTPase activity reduces cellular dNTP levels to levels too low for retroviral reverse transcription to occur, blocking early-stage virus replication in dendritic and other myeloid cells. Likewise, suppresses LINE-1 …

**Summary**, from NCBI Gene [25939](https://www.ncbi.nlm.nih.gov/gene/25939):

> This gene may play a role in regulation of the innate immune response. The encoded protein is upregulated in response to viral infection and may be involved in mediation of tumor necrosis factor-alpha proinflammatory responses. Mutations in this gene have been associated with Aicardi-Goutieres syndrome. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:15925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15925) · Entrez [25939](https://www.ncbi.nlm.nih.gov/gene/25939) · UniProt [Q9Y3Z3](https://www.uniprot.org/uniprotkb/Q9Y3Z3) · Ensembl [ENSG00000101347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101347)

## Data

Gene col 2121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2121); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2121]; `tensor/DDL_lfc|DDL_z.npy` [2121]; `embed/gene_vectors.npy` [2121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2121 or target_col == 2121). Every well: [[SAMHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
