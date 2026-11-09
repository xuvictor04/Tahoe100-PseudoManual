---
symbol: "TMEM91"
type: "gene"
col: 6592
ensembl_id: "ENSG00000142046"
name: "transmembrane protein 91"
location: "19q13.2"
module: 23
arm: "+"
pooled_cpm: 35.39
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 38
n_dd_up_clean: 4
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# TMEM91

*transmembrane protein 91* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.34× (z +5.0, q 4e-04, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (14 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.420× (z -14.7, q 0e+00, down in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.486× (z -11.8, q 8e-30, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP5D1P-1]] (+0.65, fdr 8e-06), [[PNISR]] (+0.64, fdr 2e-05), [[TRNAU1AP]] (+0.64, fdr 7e-06); moves opposite to [[RGS19]] (-0.64, fdr 2e-05), [[PRELID3B]] (-0.61, fdr 7e-06), [[PHB1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[B9D2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6592.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +5.0 | 4e-04 | 26/47 (SW480, LoVo, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +4.7 | 7e-04 | 19/46 (A549, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.28×** | +3.9 | 0.016 | 14/47 (SW480, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.24×** | +3.7 | 0.025 | 15/47 (A-427, NCI-H460, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.025 | 12/46 (C-33 A, A549, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.7 | 0.025 | 14/47 (SW480, NCI-H1792, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.039 | 18/47 (A-172, LoVo, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.11 | 7/47 (HOP62, NCI-H2030, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.13 | 18/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.20× | +3.1 | 0.13 | 13/47 (A549, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6592.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.420×** | -14.7 | 0e+00 | 45/47 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.421×** | -14.6 | 0e+00 | 46/47 (A549, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.455×** | -13.3 | 3e-38 | 43/47 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.457×** | -12.8 | 4e-35 | 35/45 (C-33 A, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.486×** | -11.8 | 8e-30 | 39/46 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.508×** | -11.4 | 2e-28 | 40/47 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.667×** | -9.6 | 7e-20 | 34/47 (SNU-423, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.568×** | -9.6 | 8e-20 | 36/47 (A549, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.582×** | -9.1 | 4e-18 | 33/47 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.592×** | -8.9 | 4e-17 | 38/47 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.386×** | -8.4 | 2e-15 | 36/46 (A-172, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.632×** | -7.7 | 5e-13 | 35/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.422×** | -7.6 | 1e-12 | 29/47 (A-427, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.629×** | -7.4 | 6e-12 | 31/47 (HT-29, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.656×** | -7.1 | 4e-11 | 28/47 (HT-29, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.656×** | -7.1 | 4e-11 | 27/46 (A549, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.776×** | -6.0 | 7e-08 | 26/47 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.581×** | -4.8 | 4e-05 | 25/47 (PANC-1, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -4.6 | 1e-04 | 22/47 (A498, hTERT-HPNE, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.783×** | -4.1 | 9e-04 | 21/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6592. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 90.0 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -17.9) |
| [[HS-578T (line)]] | alt | 77.6 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.285× (z -10.7) |
| [[H4 (line)]] | wt | 68.0 | 0 | 9 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.218× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~87% of this change |
| [[NCI-H1792 (line)]] | alt | 63.5 | 0 | 9 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.233× (z -13.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -11.5) |
| [[SW480 (line)]] | alt | 41.5 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.339× (z -11.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.367× (z -10.3) |
| [[HOP62 (line)]] | alt | 79.7 | 0 | 6 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.262× (z -14.4) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.363× (z -10.9) |
| [[HT-29 (line)]] | alt | 68.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -16.9) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 47.8 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -12.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.326× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 69.6 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.78× (z +11.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.294× (z -10.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.333× (z -9.3) |
| [[SNU-423 (line)]] | alt | 35.1 | 0 | 5 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.292× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 29.1 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.310× (z -10.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.356× (z -8.9) |
| [[PANC-1 (line)]] | alt | 32.3 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.330× (z -11.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.435× (z -8.7) |
| [[A-172 (line)]] | wt | 64.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0978× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 29.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0579× (z -11.5) |
| [[A498 (line)]] | wt | 34.8 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.249× (z -11.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -10.3) |
| [[HCT15 (line)]] | alt | 67.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change · without an alert: [[OTS514 (drug)]] 5 µM 0.0986× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 50.7 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.265× (z -9.4) |
| [[C-33 A (line)]] | alt | 48.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.115× (z -14.6) ⚠ toxic |
| [[J82 (line)]] | alt | 25.9 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.308× (z -8.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.315× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 36.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -13.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -8.9) |
| [[LoVo (line)]] | wt | 13.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +13.2) ⚠ cell-cycle shift, explains ~80% of this change | — |
| [[NCI-H460 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.368× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW 1088 (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0565× (z -8.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6592), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP5D1P-1]] | +0.65 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[PNISR]] | +0.64 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[TRNAU1AP]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[LAMB2P1]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[TCF25]] | +0.61 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[ZSCAN16-AS1]] | +0.61 | +0.68 / +0.37 | both halves | 8e-05 |  |
| [[KPNB1-DT]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[NDUFA6-DT]] | +0.61 | +0.49 / +0.38 | both halves | 7e-05 |  |
| [[GTF2IRD2B]] | +0.61 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[GTF2IRD2]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ZCWPW2]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[BORCS7-ASMT]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS19]] | -0.64 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[PRELID3B]] | -0.61 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[PHB1]] | -0.61 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[RITA1]] | -0.58 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[AGPS]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[ICMT]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[GLO1]] | -0.54 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[MINPP1]] | -0.53 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[CDYL2]] | -0.53 | -0.55 / -0.37 | both halves | 7e-05 |  |
| [[PHF6]] | -0.53 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[GOT2]] | -0.53 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[MLX]] | -0.53 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B9D2]] | C | B9D2's natural level strengthens TMEM91's drug response | B9D2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.18; direction not clear | 0.010 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MZF1]] | C | MZF1's natural level strengthens TMEM91's drug response | MZF1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.48; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PROSER3]] | C | PROSER3's natural level strengthens TMEM91's drug response | PROSER3's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.20; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.604). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-8.1, 28.0); signed map (-4.1, 1.7). **Vector** length 95.0, 24.9% of its response variance represented; |z| ≥ 3 in 1,273 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +7.7 | -3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | -0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +3.5 | -3.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | +3.5 | -3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.8 | +3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | -1.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +3.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -11.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.3 | -9.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.9 | -12.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.3 | -8.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -8.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | +0.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 91 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,350,911-41,384,083 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ27310, IFITMD6, DSPC3, SynDIG3 |
| Gene groups (HGNC) | Dispanins |
| Matched by | ensembl_id |

UniProt [Q6ZNR0](https://www.uniprot.org/uniprotkb/Q6ZNR0) carries no function annotation.

**Summary**, from NCBI Gene [641649](https://www.ncbi.nlm.nih.gov/gene/641649):

> Predicted to act upstream of or within hematopoietic progenitor cell differentiation. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32393) · Entrez [641649](https://www.ncbi.nlm.nih.gov/gene/641649) · UniProt [Q6ZNR0](https://www.uniprot.org/uniprotkb/Q6ZNR0) · Ensembl [ENSG00000142046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142046)

## Data

Gene col 6592: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6592); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6592, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6592]; `tensor/DDL_lfc|DDL_z.npy` [6592]; `embed/gene_vectors.npy` [6592]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6592 or target_col == 6592). Every well: [[TMEM91 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM91.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
