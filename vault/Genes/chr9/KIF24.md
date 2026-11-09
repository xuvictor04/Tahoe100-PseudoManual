---
symbol: "KIF24"
type: "gene"
col: 11839
ensembl_id: "ENSG00000186638"
name: "kinesin family member 24"
location: "9p13.3"
module: 91
arm: "+"
pooled_cpm: 15.9
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 26
n_dd_up_clean: 9
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# KIF24

*kinesin family member 24* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (21 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.55× (z +14.2, q 4e-43, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.685× (z -8.4, q 2e-14, down in 26 of 47 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.778× (z -5.6, q 3e-06, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZGRF1]] (+0.87, fdr 7e-06), [[ESCO2]] (+0.83, fdr 7e-06), [[E2F8]] (+0.83, fdr 7e-06).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TLCD3B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 21 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11839.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.55×** | +14.2 | 4e-43 | 42/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +13.4 | 2e-38 | 32/45 (NCI-H2030, PANC-1, …) | top dose only | cell-cycle shift (explains ~25% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.85×** | +9.8 | 3e-20 | 32/47 (HOP62, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.82×** | +9.5 | 4e-19 | 29/46 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.78×** | +9.1 | 1e-17 | 33/46 (J82, SW480, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.70×** | +8.4 | 4e-15 | 31/46 (HOP62, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.69×** | +8.3 | 1e-14 | 30/47 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.66×** | +8.0 | 1e-13 | 27/46 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.63×** | +7.7 | 9e-13 | 26/45 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.35×** | +6.7 | 1e-09 | 23/45 (A549, NCI-H1792, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **1.51×** | +6.3 | 2e-08 | 20/41 (PANC-1, HT-29, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +5.9 | 1e-07 | 23/47 (A549, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.43×** | +5.6 | 9e-07 | 16/46 (A549, HS-578T, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.27×** | +5.3 | 4e-06 | 16/47 (SK-MEL-2, SW 900, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.37×** | +5.0 | 2e-05 | 13/47 (HT-29, SW48, …) | all doses, stronger at high dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.005 | 10/46 (SW480, HOP62, …) | top dose only | plate-row cell shift |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.019 | 6/47 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.028 | 7/46 (J82, SW480, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.038 | 2/46 (J82, HCT15) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.044 | 7/47 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.046 | 5/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.055 | 7/46 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11839.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.685×** | -8.4 | 2e-14 | 26/47 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.617×** | -7.6 | 8e-12 | 26/46 (RPMI-7951, A498, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.618×** | -7.3 | 6e-11 | 24/43 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.691×** | -5.8 | 9e-07 | 23/45 (SW480, SHP-77, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.778×** | -5.6 | 3e-06 | 24/47 (KATO III, SHP-77, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.518×** | -5.4 | 6e-06 | 19/35 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.725×** | -5.1 | 4e-05 | 19/46 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.805×** | -4.8 | 9e-05 | 20/47 (NCI-H661, SW480, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.723×** | -4.8 | 9e-05 | 23/46 (KATO III, LS 180, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.725×** | -4.7 | 2e-04 | 16/32 (J82, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.759×** | -4.3 | 7e-04 | 16/46 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -4.2 | 0.001 | 20/46 (HEC-1-A, C-33 A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.767×** | -4.2 | 0.001 | 12/47 (C-33 A, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.771×** | -4.1 | 0.002 | 18/44 (SNU-1, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.773×** | -4.0 | 0.002 | 11/47 (COLO 205, NCI-H460, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.660×** | -3.4 | 0.020 | 12/43 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.809×** | -3.3 | 0.024 | 7/46 (AsPC-1, SNU-423, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.809×** | -3.3 | 0.024 | 7/46 (A498, A-172, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.864× | -3.2 | 0.030 | 6/47 (PANC-1, SW 1088, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.869× | -3.1 | 0.044 | 10/47 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.869× | -3.1 | 0.044 | 5/47 (HT-29, NCI-H2347, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.759×** | -3.1 | 0.046 | 13/42 (Hs 766T, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.818×** | -3.0 | 0.052 | 11/46 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.826×** | -3.0 | 0.056 | 10/46 (COLO 205, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.78 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11839. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 25.5 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0427× (z -11.3) ⚠ toxic · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.385× (z -9.2) |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0392× (z -11.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0780× (z -8.6) |
| [[J82 (line)]] | alt | 36.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -10.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 20.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +13.5) | — |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0612× (z -10.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Cepharanthine (drug)]] 0.5 µM 0.106× (z -8.6) |
| [[SW480 (line)]] | alt | 27.1 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.75× (z +9.2) | [[Lonafarnib (drug)]] 5 µM 0.125× (z -10.3) ⚠ toxic |
| [[A-172 (line)]] | wt | 23.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.316× (z -9.2) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.203× (z -12.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A498 (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.240× (z -11.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A549 (line)]] | wt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.30× (z +9.1) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[LoVo (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -9.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.162× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 9.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +13.5) | — |
| [[NCI-H2347 (line)]] | alt | 4.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +9.4) | — |
| [[RKO (line)]] | wt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.21× (z +12.3) | — |
| [[SHP-77 (line)]] | alt | 29.7 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.370× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -10.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11839), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZGRF1]] | +0.87 | +0.79 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[ESCO2]] | +0.83 | +0.80 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[E2F8]] | +0.83 | +0.77 / +0.86 | both halves | 7e-06 |  |
| [[BRIP1]] | +0.81 | +0.81 / +0.81 | both halves | 7e-06 |  |
| [[PLK4]] | +0.81 | +0.71 / +0.83 | both halves | 7e-06 | pathway: Anchoring of the basal body to the plasma membrane; STRING 514 |
| [[SGO1]] | +0.80 | +0.83 / +0.79 | both halves | 7e-06 |  |
| [[KIF15]] | +0.79 | +0.79 / +0.80 | both halves | 7e-06 | same gene group |
| [[NCAPG]] | +0.79 | +0.78 / +0.80 | both halves | 7e-06 |  |
| [[BRCA1]] | +0.79 | +0.76 / +0.82 | both halves | 7e-06 |  |
| [[SKA3]] | +0.79 | +0.75 / +0.83 | both halves | 7e-06 |  |
| [[CENPN]] | +0.79 | +0.71 / +0.82 | both halves | 7e-06 |  |
| [[POLQ]] | +0.79 | +0.76 / +0.83 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLCD3B]] | B | TLCD3B activity raises KIF24's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without TLCD3B | 0.021 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises KIF24's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.92× lower at baseline in the lines without E2F2 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers KIF24's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[E2F8]] | B | E2F8 activity raises KIF24's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.11× lower at baseline in the lines without E2F8 | 0.086 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CENPP]] | C | CENPP activity raises KIF24's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.61× lower at baseline in the lines without CENPP | 0.016 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises KIF24's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.80× lower at baseline in the lines without NDC80 | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises KIF24's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.82× lower at baseline in the lines without AURKB | 0.052 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises KIF24's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without MCM10 | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[E2F1]] | C | E2F1 activity raises KIF24's level | lines that do not express E2F1 (3) vs lines expressing it (47) | 2.53× lower at baseline in the lines without E2F1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |
| [[C21orf58]], [[CDC45]], [[CENPM]], [[SKA3]] | C | C21orf58, CDC45, CENPM, SKA3 activity raises KIF24's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.94× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CLSPN]] | C | CLSPN activity raises KIF24's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.52× lower at baseline in the lines without CLSPN | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.812). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-39.0, -48.9); signed map (-43.0, -46.4). **Vector** length 118, 31.5% of its response variance represented; |z| ≥ 3 in 1,172 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.67 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.70 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.70 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +14.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.5 | +9.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.3 | +8.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | +4.9 | +7.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.4 | +8.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.1 | +3.3 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.7 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -7.9 | -8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.6 | -4.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -6.4 | -7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.0 | -5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | -5.0 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -5.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.2 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:34,252,380-34,329,268 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA571F15.4, FLJ10933, FLJ43884; previously C9orf48 |
| Gene groups (HGNC) | Kinesins; Sterile alpha motif domain containing; Small nucleolar RNA protein coding host genes |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T7B8](https://www.uniprot.org/uniprotkb/Q5T7B8) (Kinesin-like protein KIF24):

> Microtubule-dependent motor protein that acts as a negative regulator of ciliogenesis by mediating recruitment of CCP110 to mother centriole in cycling cells, leading to restrict nucleation of cilia at centrioles. Mediates depolymerization of microtubules of centriolar origin, possibly to suppress aberrant cilia formation. Following activation by NEK2 involved in disassembly of primary cilium during G2/M phase but does not disassemble fully formed ciliary axonemes. As cilium assembly and …

**Summary**, from NCBI Gene [347240](https://www.ncbi.nlm.nih.gov/gene/347240):

> This gene encodes a member of the kinesin superfamily of microtubule-based motor proteins which are involved in the intracellular transport of membranous organelles, protein complexes, and mRNAs. They also play critical roles in mitosis, morphogenesis, and signal transduction. The encoded protein contains an N-terminal sterile alpha motif (SAM) domain and an ATP-binding kinesin motor domain. It binds centriolar coiled coil protein 110 and centrosomal protein 97 and localizes to the mother …

**Accessions** — [HGNC:19916](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19916) · Entrez [347240](https://www.ncbi.nlm.nih.gov/gene/347240) · UniProt [Q5T7B8](https://www.uniprot.org/uniprotkb/Q5T7B8) · Ensembl [ENSG00000186638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186638)

## Data

Gene col 11839: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11839); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11839, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11839]; `tensor/DDL_lfc|DDL_z.npy` [11839]; `embed/gene_vectors.npy` [11839]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11839 or target_col == 11839). Every well: [[KIF24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
