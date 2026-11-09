---
symbol: "ISG20"
type: "gene"
col: 10222
ensembl_id: "ENSG00000172183"
name: "interferon stimulated exonuclease gene 20"
location: "15q26.1"
module: 70
arm: "+"
pooled_cpm: 39.18
n_lines_expressing: 46
n_dd_up: 17
n_dd_down: 39
n_dd_up_clean: 14
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 22
direction_downstream: 32
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# ISG20

*interferon stimulated exonuclease gene 20* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.09× (z +10.2, q 2e-21, up in 33 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.476× (z -10.2, q 9e-22, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OASL]] (+0.70, fdr 7e-06), [[HELZ2]] (+0.69, fdr 7e-06), [[ISG15]] (+0.69, fdr 7e-06); moves opposite to [[MRPS35]] (-0.58, fdr 1e-05), [[OPA1]] (-0.57, fdr 3e-05), [[NUDT21]] (-0.56, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[IFI44]] → it (grade B ⚠); 32 go from it, the strongest it → cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10222.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +10.2 | 2e-21 | 33/43 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.01×** | +9.6 | 2e-19 | 34/44 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.48×** | +7.0 | 4e-10 | 26/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +5.7 | 2e-06 | 30/44 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.51×** | +5.4 | 7e-06 | 23/44 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +5.0 | 5e-05 | 25/43 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +4.0 | 0.004 | 18/43 (A549, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +4.0 | 0.004 | 18/44 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.50×** | +4.0 | 0.004 | 22/44 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.029 | 17/43 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.3 | 0.052 | 16/42 (BT-474, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.92×** | +3.2 | 0.055 | 10/43 (SW480, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.057 | 14/44 (SNU-1, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.062 | 15/43 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Rimonabant (drug)]] 5 µM |  | 1.19× | +3.1 | 0.071 | 11/44 (KATO III, SW 900, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.084 | 15/43 (NCI-H2030, LS 180, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.084 | 8/44 (BT-474, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.084 | 8/43 (SK-MEL-2, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10222.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.476×** | -10.2 | 9e-22 | 38/44 (HT-29, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.497×** | -9.6 | 2e-19 | 35/44 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.557×** | -8.1 | 2e-13 | 33/44 (HT-29, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.639×** | -8.0 | 2e-13 | 31/44 (A549, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.563×** | -7.9 | 3e-13 | 24/41 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.571×** | -7.4 | 1e-11 | 20/33 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.635×** | -6.2 | 4e-08 | 29/44 (HT-29, A549, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.641×** | -6.1 | 7e-08 | 26/44 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.691×** | -5.1 | 2e-05 | 28/44 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.705×** | -4.8 | 9e-05 | 24/43 (A549, NCI-H460, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.693×** | -4.7 | 2e-04 | 25/43 (A549, SW 1271, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.716×** | -4.6 | 2e-04 | 23/43 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.725×** | -4.4 | 4e-04 | 21/44 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.725×** | -4.4 | 4e-04 | 22/43 (A-172, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.727×** | -4.4 | 5e-04 | 20/44 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.733×** | -4.3 | 7e-04 | 21/43 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.737×** | -4.2 | 9e-04 | 22/43 (A549, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.739×** | -4.2 | 1e-03 | 22/44 (A549, NCI-H1573, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.742×** | -4.1 | 0.001 | 21/45 (A-172, HT-29, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.748×** | -4.0 | 0.002 | 22/43 (A549, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10222. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 98.3 | 7 (4 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +15.0) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.98× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.339× (z -9.3) |
| [[A549 (line)]] | wt | 94.9 | 0 | 6 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.273× (z -10.4) ⚠ toxic · without an alert: [[Budesonide (drug)]] 0.05 µM 0.334× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 106 | 3 (2 ⚠) | 3 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.96× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.298× (z -9.5) |
| [[HT-29 (line)]] | alt | 88.6 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -15.5) |
| [[A-172 (line)]] | wt | 56.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -13.2) |
| [[LoVo (line)]] | wt | 30.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +17.9) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 61.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.235× (z -10.7) |
| [[A498 (line)]] | wt | 50.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 29.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +13.3) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.02× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 21.4 | 0 | 3 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.124× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 33.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.4) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.54× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 62.6 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.78× (z +8.6) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[COLO 205 (line)]] | alt | 81.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.10× (z +8.6) | — |
| [[H4 (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.139× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 30.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.202× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 38.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -8.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 17.5 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.92× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 96.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -8.6) |
| [[A-427 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.21 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.29 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.38 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10222), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OASL]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 794 |
| [[HELZ2]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 628 |
| [[ISG15]] | +0.69 | +0.61 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 893 |
| [[HLA-B]] | +0.68 | +0.59 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 540 |
| [[IRF7]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 823 |
| [[RIGI]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 717 |
| [[IFI27]] | +0.66 | +0.51 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 622 |
| [[ZNFX1]] | +0.65 | +0.57 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TRIM5]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[HLA-F]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[PMAIP1]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS |
| [[RASGRP3]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS35]] | -0.58 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[OPA1]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[NUDT21]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[SKP2]] | -0.56 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[IARS2]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CHPT1]] | -0.54 | -0.58 / -0.53 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 20, C 2. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI44]] | B | IFI44 activity raises ISG20's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.36× lower at baseline in the lines without IFI44 | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[SERPINB7]] | B | SERPINB7 activity raises ISG20's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 1.98× lower at baseline in the lines without SERPINB7 | 0.005 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[RSAD2]] | B | RSAD2 activity raises ISG20's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.11× lower at baseline in the lines without RSAD2 | 0.009 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[HMGN2P46]] | B | HMGN2P46 activity raises ISG20's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 1.96× lower at baseline in the lines without HMGN2P46 | 0.010 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[SAMD9]] | B | SAMD9 activity raises ISG20's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without SAMD9 | 0.013 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[NLRC5]] | B | NLRC5 activity raises ISG20's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 2.00× lower at baseline in the lines without NLRC5 | 0.015 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises ISG20's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.82× lower at baseline in the lines without OAS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[C15orf48]] | B | C15orf48 activity raises ISG20's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 1.85× lower at baseline in the lines without C15orf48 | 0.036 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[APOL3]] | B | APOL3 activity raises ISG20's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without APOL3 | 0.044 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[CTSS]] | B | CTSS activity raises ISG20's level | lines that do not express CTSS (15) vs lines expressing it (35) | 1.55× lower at baseline in the lines without CTSS | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[GBP4]] | B | GBP4 activity raises ISG20's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.58× lower at baseline in the lines without GBP4 | 0.059 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[OVOL1]] | B | OVOL1 activity raises ISG20's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.48× lower at baseline in the lines without OVOL1 | 0.062 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 0, C 32. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | C | ISG20 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 0.65× the cells of the other lines | 0.004 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| cells under [[Methylprednisolone succinate (drug)]] 0.5 µM | C | ISG20 activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 1.56× the cells of the other lines | 0.004 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| cells under [[Ponatinib (drug)]] 0.05 µM | C | ISG20 activity raises the cells' numbers under Ponatinib 0.05 µM (protects the cells) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 0.72× the cells of the other lines | 0.008 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | ISG20 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 0.72× the cells of the other lines | 0.008 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| cells under [[olaparib (drug)]] 5 µM | C | ISG20 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 1.64× the cells of the other lines | 0.011 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| cells under [[Methylprednisolone succinate (drug)]] 5 µM | C | ISG20 activity lowers the cells' numbers under Methylprednisolone succinate 5 µM (makes them more sensitive) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 1.43× the cells of the other lines | 0.017 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| cells under [[Cyclosporin A (drug)]] 0.05 µM | C | ISG20 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 0.68× the cells of the other lines | 0.025 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| cells under [[Tolcapone (drug)]] 5 µM | C | ISG20 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 0.78× the cells of the other lines | 0.026 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM | C | ISG20 activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 0.78× the cells of the other lines | 0.030 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| cells under [[TAK-733 (drug)]] 0.05 µM | C | ISG20 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 1.30× the cells of the other lines | 0.031 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| cells under [[Pioglitazone (drug)]] 0.5 µM | C | ISG20 activity lowers the cells' numbers under Pioglitazone 0.5 µM (makes them more sensitive) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 1.33× the cells of the other lines | 0.033 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| cells under [[HI-TOPK-032 (drug)]] 5 µM | C | ISG20 activity lowers the cells' numbers under HI-TOPK-032 5 µM (makes them more sensitive) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 1.39× the cells of the other lines | 0.039 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.2, 51.0); signed map (65.0, 28.6). **Vector** length 140, 44.6% of its response variance represented; |z| ≥ 3 in 1,274 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon gamma signaling* (reactome, mean cos +0.53 to 13); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.53 to 8); *SARS-CoV-2 activates/modulates innate and adaptive immune responses* (reactome, mean cos +0.54 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.4 | +2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.7 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +6.0 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +4.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.5 | +4.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +3.2 |
| fall | [[NG25 (drug)]] 5 µM |  | -6.5 | -2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -6.5 | -8.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -5.2 | -6.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -5.0 | -4.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.8 | -4.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -4.8 | -4.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.8 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | interferon stimulated exonuclease gene 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:88,635,670-88,656,483 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HEM45, CD25 |
| Gene groups (HGNC) | Exonucleases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, APOPTOSIS, INTERFERON_GAMMA_RESPONSE, ESTROGEN_RESPONSE_LATE, GLYCOLYSIS, HYPOXIA |
| Reactome | 3 pathways, smallest: Interferon alpha/beta signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AZ6](https://www.uniprot.org/uniprotkb/Q96AZ6) (Interferon-stimulated gene 20 kDa protein):

> Interferon-induced antiviral exoribonuclease that acts mainly on single-stranded RNA. Exhibits antiviral activity against RNA viruses including hepatitis C virus (HCV), hepatitis A virus (HAV) and yellow fever virus (YFV). Inhibition of several viruses such as chikungunya virus (CHIKV) does not involve the degradation of viral RNAs, but rather the inhibition of translation of viral proteins (By similarity). Exerts a translational control over a large panel of non-self RNA substrates while …

**Summary**, from NCBI Gene [3669](https://www.ncbi.nlm.nih.gov/gene/3669):

> Enables 3'-5' exonuclease activity and RNA binding activity. Involved in several processes, including DNA catabolic process; defense response to virus; and negative regulation of viral genome replication. Located in cytoplasm and nuclear lumen. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6130](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6130) · Entrez [3669](https://www.ncbi.nlm.nih.gov/gene/3669) · UniProt [Q96AZ6](https://www.uniprot.org/uniprotkb/Q96AZ6) · Ensembl [ENSG00000172183](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172183)

## Data

Gene col 10222: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10222); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10222, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10222]; `tensor/DDL_lfc|DDL_z.npy` [10222]; `embed/gene_vectors.npy` [10222]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10222 or target_col == 10222). Every well: [[ISG20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ISG20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
