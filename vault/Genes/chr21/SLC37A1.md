---
symbol: "SLC37A1"
type: "gene"
col: 8311
ensembl_id: "ENSG00000160190"
name: "solute carrier family 37 member 1"
location: "21q22.3"
module: 8
arm: "+"
pooled_cpm: 35.27
n_lines_expressing: 41
n_dd_up: 8
n_dd_down: 22
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 45
direction_downstream: 2
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SLC37A1

*solute carrier family 37 member 1* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.52× (z +7.8, q 5e-12, up in 22 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.362× (z -19.4, q 0e+00, down in 36 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMPRSS2]] (+0.61, fdr 7e-06), [[TMCO4]] (+0.61, fdr 3e-05), [[NPNT]] (+0.60, fdr 3e-05); moves opposite to [[TANC2]] (-0.55, fdr 3e-05), [[ZNF559]] (-0.51, fdr 1e-04), [[DNAAF9]] (-0.51, fdr 2e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 45 arrows point to it, the strongest [[TOX3]] → it (grade B ⚠); 2 go from it, the strongest it → [[TRAM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8311.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +7.8 | 5e-12 | 22/37 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 9e-04 | 13/38 (AsPC-1, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.6 | 9e-04 | 17/38 (NCI-H460, SW48, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.4 | 0.001 | 15/37 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.003 | 13/40 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.23×** | +3.8 | 0.011 | 10/38 (AsPC-1, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.17× | +3.8 | 0.011 | 8/39 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.22×** | +3.8 | 0.011 | 14/38 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.019 | 11/38 (A498, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.6 | 0.021 | 9/39 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.022 | 16/39 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.17× | +3.5 | 0.022 | 12/40 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.036 | 10/39 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8311.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.362×** | -19.4 | 0e+00 | 36/39 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.366×** | -19.2 | 0e+00 | 35/39 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.428×** | -16.2 | 0e+00 | 34/38 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.554×** | -11.2 | 4e-27 | 26/38 (LoVo, CHP-212, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.584×** | -10.2 | 2e-22 | 22/38 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.615×** | -9.3 | 2e-18 | 24/39 (SW1417, SW480, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.479×** | -7.3 | 2e-11 | 25/40 (A-172, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.690×** | -6.5 | 6e-09 | 19/28 (RKO, KATO III, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.739×** | -5.7 | 6e-07 | 22/39 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.741×** | -5.7 | 7e-07 | 17/37 (SW1417, NCI-H2030, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.744×** | -5.4 | 4e-06 | 20/35 (NCI-H2030, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.763×** | -5.1 | 1e-05 | 19/39 (LS 180, NCI-H1573, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.771×** | -4.9 | 4e-05 | 17/40 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.623×** | -4.7 | 1e-04 | 16/35 (Panc 03.27, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.784×** | -4.6 | 2e-04 | 19/37 (LoVo, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.804×** | -4.1 | 0.001 | 18/38 (NCI-H1573, A498, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.832×** | -3.5 | 0.013 | 12/38 (AsPC-1, A498, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.712×** | -3.4 | 0.019 | 11/36 (SNU-1, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.847× | -3.1 | 0.037 | 6/39 (AsPC-1, BT-474, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.850× | -3.1 | 0.045 | 9/38 (SW1417, Panc 03.27, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.852× | -3.0 | 0.049 | 3/39 (SK-MEL-2, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 102 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -22.8) |
| [[LS 180 (line)]] | wt | 151 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0941× (z -27.7) |
| [[SW1417 (line)]] | alt | 50.8 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -15.9) |
| [[SW480 (line)]] | alt | 32.3 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -11.9) |
| [[COLO 205 (line)]] | alt | 140 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -18.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.183× (z -13.1) |
| [[HT-29 (line)]] | alt | 132 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -15.1) |
| [[A549 (line)]] | wt | 26.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.271× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 82.9 | 2 | 3 | [[Cobimetinib (drug)]] 5 µM 3.26× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.155× (z -16.4) |
| [[KATO III (line)]] | alt | 39.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0918× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.172× (z -16.0) |
| [[NCI-H1573 (line)]] | alt | 56.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 59.6 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -13.5) |
| [[RKO (line)]] | wt | 53.0 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.284× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 33.2 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.8) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -12.4) |
| [[Hs 766T (line)]] | wt | 49.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 23.7 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.160× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 21.7 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.171× (z -11.9) |
| [[A-427 (line)]] | wt | 19.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 19.1 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.363× (z -8.6) |
| [[PANC-1 (line)]] | alt | 11.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 29.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0902× (z -13.4) |
| [[A498 (line)]] | wt | 49.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.147× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -13.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 9.70 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 26.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.364× (z -9.0) |
| [[AN3 CA (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.62 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.90 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.56 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.25 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMPRSS2]] | +0.61 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[TMCO4]] | +0.61 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[NPNT]] | +0.60 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[HNF4G]] | +0.59 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[CTSS]] | +0.57 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[HNF1B]] | +0.57 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[SLCO3A1]] | +0.56 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[CLIC5]] | +0.56 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[PLCH1]] | +0.55 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[MUC13]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PKDCC]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[SLC44A3-AS1]] | +0.54 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TANC2]] | -0.55 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[ZNF559]] | -0.51 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[DNAAF9]] | -0.51 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[SMIM8]] | -0.48 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[DYNC2H1]] | -0.48 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[OGG1]] | -0.48 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[ELL2]] | -0.47 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[SMYD3]] | -0.46 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[TRAM2]] | -0.46 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[ZNF891]] | -0.46 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[ZNF790-AS1]] | -0.45 | -0.37 / -0.39 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 45, C 0. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOX3]] | B | TOX3 activity raises SLC37A1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.95× lower at baseline in the lines without TOX3 | 8e-04 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[TMPRSS2]] | B | TMPRSS2 activity raises SLC37A1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.88× lower at baseline in the lines without TMPRSS2 | 1e-03 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[ADGRF1]] | B | ADGRF1 activity raises SLC37A1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.71× lower at baseline in the lines without ADGRF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[TSPAN8]] | B | TSPAN8 activity raises SLC37A1's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 3.35× lower at baseline in the lines without TSPAN8 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[GCNT3]] | B | GCNT3 activity raises SLC37A1's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.08× lower at baseline in the lines without GCNT3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[ANO9]] | B | ANO9 activity raises SLC37A1's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 2.47× lower at baseline in the lines without ANO9 | 0.006 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[SYK]] | B | SYK activity raises SLC37A1's level | lines that do not express SYK (30) vs lines expressing it (20) | 3.96× lower at baseline in the lines without SYK | 0.007 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[MUC13]] | B | MUC13 activity raises SLC37A1's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.95× lower at baseline in the lines without MUC13 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[TRIM31]] | B | TRIM31 activity raises SLC37A1's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 3.76× lower at baseline in the lines without TRIM31 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[ST14]] | B | ST14 activity raises SLC37A1's level | lines that do not express ST14 (32) vs lines expressing it (18) | 3.72× lower at baseline in the lines without ST14 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[RBM47]] | B | RBM47 activity raises SLC37A1's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 3.11× lower at baseline in the lines without RBM47 | 0.011 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[LINC01559]] | B | LINC01559 activity raises SLC37A1's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 3.63× lower at baseline in the lines without LINC01559 | 0.011 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAM2]] | B | SLC37A1 activity lowers TRAM2's level | lines that do not express SLC37A1 (9) vs lines expressing it (41) | 3.41× higher at baseline in the lines without SLC37A1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RSPH1, GRTP1, ABCA3; its own permutation p |
| [[PSME2]] | B | SLC37A1 activity raises PSME2's level | lines that do not express SLC37A1 (9) vs lines expressing it (41) | 1.38× lower at baseline in the lines without SLC37A1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RSPH1, GRTP1, ABCA3; its own permutation p |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.525). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.8, 53.0); signed map (56.4, 0.5). **Vector** length 105, 26.7% of its response variance represented; |z| ≥ 3 in 1,092 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.7 | +4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.0 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.4 | +3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +7.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +0.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.3 | +3.3 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | +2.2 | +3.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -19.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.5 | -19.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -16.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -11.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 37 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:42,496,008-42,581,440 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPX1 |
| Gene groups (HGNC) | Solute carrier family 37 |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: Gluconeogenesis; Glucose metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P57057](https://www.uniprot.org/uniprotkb/P57057) (Glucose-6-phosphate exchanger SLC37A1):

> Inorganic phosphate and glucose-6-phosphate antiporter. May transport cytoplasmic glucose-6-phosphate into the lumen of the endoplasmic reticulum and translocate inorganic phosphate into the opposite direction. Independent of a lumenal glucose-6-phosphatase. May not play a role in homeostatic regulation of blood glucose levels.

**Summary**, from NCBI Gene [54020](https://www.ncbi.nlm.nih.gov/gene/54020):

> The protein encoded by this gene localizes to the endoplasmic reticulum (ER) membrane. This protein translocates glucose-6-phosphate from the cytoplasm into the lumen of the ER for hydrolysis into glucose by another ER membrane protein. This gene is a member of the solute carrier 37 gene family. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:11024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11024) · Entrez [54020](https://www.ncbi.nlm.nih.gov/gene/54020) · UniProt [P57057](https://www.uniprot.org/uniprotkb/P57057) · Ensembl [ENSG00000160190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160190)

## Data

Gene col 8311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8311); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8311]; `tensor/DDL_lfc|DDL_z.npy` [8311]; `embed/gene_vectors.npy` [8311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8311 or target_col == 8311). Every well: [[SLC37A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC37A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
