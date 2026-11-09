---
symbol: "MDC1"
type: "gene"
col: 6003
ensembl_id: "ENSG00000137337"
name: "mediator of DNA damage checkpoint 1"
location: "6p21.33"
module: 22
arm: "+"
pooled_cpm: 42.57
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# MDC1

*mediator of DNA damage checkpoint 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +16.6, q 0e+00, up in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.40× (z +6.2, q 5e-08, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.759× (z -7.2, q 4e-10, down in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.706× (z -6.2, q 2e-07, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DEPDC1]] (+0.74, fdr 7e-06), [[SGO1]] (+0.71, fdr 7e-06), [[HMMR]] (+0.70, fdr 7e-06); moves opposite to [[PPHLN1]] (-0.58, fdr 1e-05), [[NDUFAF7]] (-0.57, fdr 1e-05), [[DPM1]] (-0.56, fdr 3e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6003.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.89×** | +16.6 | 0e+00 | 41/48 (NCI-H2030, HS-578T, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.92×** | +11.6 | 1e-28 | 44/48 (RKO, A-427, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +7.2 | 1e-10 | 28/41 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.42×** | +6.5 | 9e-09 | 27/48 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +6.2 | 5e-08 | 32/48 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.5 | 5e-06 | 25/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.22×** | +5.3 | 1e-05 | 27/48 (SW480, NCI-H23, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.31×** | +5.0 | 5e-05 | 27/48 (J82, PANC-1, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.27×** | +4.5 | 5e-04 | 24/48 (RPMI-7951, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.1 | 0.002 | 0/48 | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.033 | 16/48 (A-427, BT-474, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.036 | 13/47 (NCI-H2030, SK-MEL-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6003.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.759×** | -7.2 | 4e-10 | 35/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.706×** | -6.2 | 2e-07 | 29/48 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.720×** | -6.1 | 3e-07 | 31/48 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.751×** | -5.3 | 2e-05 | 25/48 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.849× | -4.3 | 0.002 | 21/48 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.794×** | -4.1 | 0.004 | 23/48 (HOP62, SW 1271, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.802×** | -4.1 | 0.004 | 17/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.797×** | -3.9 | 0.005 | 22/48 (SHP-77, HS-578T, …) | all doses, flat |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.807×** | -3.9 | 0.005 | 19/48 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.770×** | -3.4 | 0.035 | 10/48 (HEC-1-A, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.714×** | -3.2 | 0.061 | 16/43 (A-427, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 0.5 µM |  | 0.841× | -3.2 | 0.069 | 7/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.847× | -3.0 | 0.10 | 20/47 (NCI-H460, CHP-212, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 36.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LoVo (line)]] | wt | 25.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LOX-IMVI (line)]] | wt | 38.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.8) ⚠ cell-cycle shift, explains ~33% of this change | [[Selinexor (drug)]] 5 µM 0.401× (z -10.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H460 (line)]] | wt | 28.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.4) ⚠ cell-cycle shift, explains ~33% of this change | [[Digitoxin (drug)]] 5 µM 0.299× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 26.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 5 µM 0.205× (z -11.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 51.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +14.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 49.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 38.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.02× (z +11.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A498 (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.421× (z -13.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A549 (line)]] | wt | 27.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[CFPAC-1 (line)]] | alt | 21.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[CHP-212 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0717× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 49.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 57.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +17.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HT-29 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.426× (z -9.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[J82 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +14.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LS 180 (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.335× (z -10.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H1573 (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +14.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2030 (line)]] | alt | 62.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +19.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H23 (line)]] | alt | 71.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +13.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[PANC-1 (line)]] | alt | 62.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SHP-77 (line)]] | alt | 85.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -12.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 52.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW 1271 (line)]] | alt | 71.5 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0716× (z -10.4) |
| [[SW48 (line)]] | wt | 50.3 | 1 | 0 | [[Filgotinib (drug)]] 5 µM 7.50× (z +10.8) | — |
| [[SW480 (line)]] | alt | 54.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.14× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DEPDC1]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[SGO1]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[HMMR]] | +0.70 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[PRC1]] | +0.70 | +0.63 / +0.71 | both halves | 7e-06 | STRING 539 |
| [[ASPM]] | +0.70 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[SMC4]] | +0.69 | +0.66 / +0.71 | both halves | 7e-06 | STRING 493 |
| [[PHF19]] | +0.69 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[SPDL1]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[MKI67]] | +0.68 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[ARHGAP11A]] | +0.67 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[C18orf54]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CENPE]] | +0.66 | +0.65 / +0.69 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPHLN1]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[NDUFAF7]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[DPM1]] | -0.56 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[HIGD2A]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[NENF]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ABHD17B]] | -0.54 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[RPS24]] | -0.54 | -0.64 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises MDC1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.5, -56.2); signed map (-49.8, -45.3). **Vector** length 113, 27.9% of its response variance represented; |z| ≥ 3 in 909 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.50 to 60); *DREAM G2/M down* (control, mean cos +0.57 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.51 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +11.3 | +16.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +8.6 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +7.8 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.0 | +6.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | +4.9 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +2.0 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +0.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -6.4 | -7.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.8 | -6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -3.8 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.4 | -5.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -3.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | mediator of DNA damage checkpoint 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:30,699,807-30,717,447 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NFBD1, KIAA0170, Em:AB023051.5 |
| Reactome | 17 pathways, smallest: Nonhomologous End-Joining (NHEJ); Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks; TP53 Regulates Transcription of DNA Repair Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14676](https://www.uniprot.org/uniprotkb/Q14676) (Mediator of DNA damage checkpoint protein 1):

> Histone reader protein required for checkpoint-mediated cell cycle arrest in response to DNA damage within both the S phase and G2/M phases of the cell cycle. Specifically recognizes and binds histone H2AX phosphorylated at 'Ser-139', a marker of DNA damage, serving as a scaffold for the recruitment of DNA repair and signal transduction proteins to discrete foci of DNA damage sites. Also required for downstream events subsequent to the recruitment of these proteins. These include …

**Summary**, from NCBI Gene [9656](https://www.ncbi.nlm.nih.gov/gene/9656):

> The protein encoded by this gene contains an N-terminal forkhead domain, two BRCA1 C-terminal (BRCT) motifs and a central domain with 13 repetitions of an approximately 41-amino acid sequence. The encoded protein is required to activate the intra-S phase and G2/M phase cell cycle checkpoints in response to DNA damage. This nuclear protein interacts with phosphorylated histone H2AX near sites of DNA double-strand breaks through its BRCT motifs, and facilitates recruitment of the ATM kinase and …

**Accessions** — [HGNC:21163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21163) · Entrez [9656](https://www.ncbi.nlm.nih.gov/gene/9656) · UniProt [Q14676](https://www.uniprot.org/uniprotkb/Q14676) · Ensembl [ENSG00000137337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137337)

## Data

Gene col 6003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6003); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6003]; `tensor/DDL_lfc|DDL_z.npy` [6003]; `embed/gene_vectors.npy` [6003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6003 or target_col == 6003). Every well: [[MDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
