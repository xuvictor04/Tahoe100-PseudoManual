---
symbol: "ARHGDIA"
type: "gene"
col: 6535
ensembl_id: "ENSG00000141522"
name: "Rho GDP dissociation inhibitor alpha"
location: "17q25.3"
module: 78
arm: "+"
pooled_cpm: 62.61
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 13
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# ARHGDIA

*Rho GDP dissociation inhibitor alpha* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.54× (z +12.1, q 5e-31, up in 44 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.90× (z +8.3, q 2e-14, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.690× (z -4.9, q 6e-04, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEC]] (+0.79, fdr 7e-06), [[FAAP100]] (+0.72, fdr 7e-06), [[ARFRP1]] (+0.69, fdr 7e-06); moves opposite to [[ATP6V0D1-DT]] (-0.57, fdr 2e-05), [[NUDT2]] (-0.57, fdr 1e-05), [[UBE4B]] (-0.55, fdr 1e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6535.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.54×** | +12.1 | 5e-31 | 44/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +11.2 | 1e-26 | 37/42 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.90×** | +8.3 | 2e-14 | 43/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.84×** | +7.6 | 6e-12 | 40/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +7.3 | 4e-11 | 34/45 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.68×** | +6.7 | 2e-09 | 39/47 (PANC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.43×** | +6.5 | 7e-09 | 33/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +6.2 | 3e-08 | 4/49 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.48×** | +4.9 | 6e-05 | 35/47 (A549, A-427, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.45×** | +4.8 | 9e-05 | 34/47 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +4.7 | 1e-04 | 29/48 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.37×** | +4.0 | 0.002 | 30/48 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.36×** | +4.0 | 0.003 | 26/47 (NCI-H460, HT-29, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.003 | 25/49 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.35×** | +3.9 | 0.004 | 27/48 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.006 | 29/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.006 | 31/48 (HT-29, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.5 | 0.012 | 27/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.023 | 22/48 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.029 | 21/47 (NCI-H460, C32, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.58×** | +3.1 | 0.047 | 20/48 (NCI-H460, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.057 | 20/48 (NCI-H1792, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 5 µM |  | **1.56×** | +3.0 | 0.058 | 23/46 (HT-29, SW480, …) | two highest doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6535.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.690×** | -4.9 | 6e-04 | 35/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.686×** | -4.7 | 7e-04 | 32/50 (SW480, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~24% here); noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.786×** | -4.5 | 0.001 | 27/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.779×** | -4.1 | 0.005 | 26/48 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.789×** | -4.1 | 0.005 | 28/48 (SW480, LoVo, …) | all doses, flat | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.726×** | -4.1 | 0.005 | 28/47 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Afatinib (drug)]] 0.5 µM |  | **0.806×** | -3.8 | 0.011 | 31/49 (BT-474, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.745×** | -3.7 | 0.013 | 26/48 (J82, SW48, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.776×** | -3.4 | 0.049 | 21/48 (KATO III, HCT15, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.792×** | -3.3 | 0.057 | 25/48 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.819×** | -3.2 | 0.066 | 20/48 (HEC-1-A, SW480, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.771×** | -3.1 | 0.085 | 21/48 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.793×** | -3.1 | 0.093 | 20/47 (SW480, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6535. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 49.3 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.9) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.10× (z +10.9) | — |
| [[A498 (line)]] | wt | 41.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 55.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A549 (line)]] | wt | 68.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.89× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 56.1 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +15.0) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[SNU-423 (line)]] | alt | 75.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HOP62 (line)]] | alt | 79.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +10.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 55.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +11.7) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[J82 (line)]] | alt | 92.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 68.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 31.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.14× (z +12.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 97.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 38.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -11.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 69.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[C32 (line)]] | wt | 49.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +9.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 43.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.1) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[H4 (line)]] | wt | 68.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 72.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 91.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 79.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 55.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 61.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 63.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[RPMI-7951 (line)]] | alt | 63.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 69.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 68.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.376× (z -10.0) |
| [[SW 900 (line)]] | alt | 52.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 95.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 71.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6535), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEC]] | +0.79 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[FAAP100]] | +0.72 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[ARFRP1]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[CLIC1]] | +0.68 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[C15orf39]] | +0.68 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[CSRP1]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[RNF123]] | +0.64 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[APEH]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[TMEM185B]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ITPR3]] | +0.62 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[R3HDM4]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[LRWD1]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V0D1-DT]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[NUDT2]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[UBE4B]] | -0.55 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[ZCCHC8]] | -0.55 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[HIGD2A]] | -0.55 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[SOS1]] | -0.55 | -0.50 / -0.44 | both halves | 3e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ARID4B]] | -0.54 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[HINT1]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[NSD3]] | -0.54 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[RPRD2]] | -0.53 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[C14orf93]] | -0.53 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[HOXA5]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ARHGDIA's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises ARHGDIA's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PLP2]] | C | PLP2 activity raises ARHGDIA's level | lines that do not express PLP2 (4) vs lines expressing it (46) | 1.38× lower at baseline in the lines without PLP2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OTULINL, C12orf75; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.2, -25.5); signed map (-7.1, 30.6). **Vector** length 98.0, 29.0% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.1 | +12.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.9 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +4.4 | +6.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.9 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +4.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.1 | +4.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -4.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.8 | -3.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.5 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | Rho GDP dissociation inhibitor alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,867,721-81,871,378 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RHOGDI; previously GDIA1 |
| Gene groups (HGNC) | Rho GDP dissociation inhibitor family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, MITOTIC_SPINDLE |
| Reactome | 15 pathways, smallest: Axonal growth stimulation; Axonal growth inhibition (RHOA activation); p75NTR regulates axonogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P52565](https://www.uniprot.org/uniprotkb/P52565) (Rho GDP-dissociation inhibitor 1):

> Controls Rho proteins homeostasis. Regulates the GDP/GTP exchange reaction of the Rho proteins by inhibiting the dissociation of GDP from them, and the subsequent binding of GTP to them. Retains Rho proteins such as CDC42, RAC1 and RHOA in an inactive cytosolic pool, regulating their stability and protecting them from degradation. Actively involved in the recycling and distribution of activated Rho GTPases in the cell, mediates extraction from membranes of both inactive and activated molecules …

**Summary**, from NCBI Gene [396](https://www.ncbi.nlm.nih.gov/gene/396):

> This gene encodes a protein that plays a key role in the regulation of signaling through Rho GTPases. The encoded protein inhibits the disassociation of Rho family members from GDP (guanine diphosphate), thereby maintaining these factors in an inactive state. Activity of this protein is important in a variety of cellular processes, and expression of this gene may be altered in tumors. Mutations in this gene have been found in individuals with nephrotic syndrome, type 8. Alternate splicing …

**Accessions** — [HGNC:678](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:678) · Entrez [396](https://www.ncbi.nlm.nih.gov/gene/396) · UniProt [P52565](https://www.uniprot.org/uniprotkb/P52565) · Ensembl [ENSG00000141522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141522)

## Data

Gene col 6535: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6535); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6535, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6535]; `tensor/DDL_lfc|DDL_z.npy` [6535]; `embed/gene_vectors.npy` [6535]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6535 or target_col == 6535). Every well: [[ARHGDIA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGDIA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
