---
symbol: "ZBTB1"
type: "gene"
col: 4769
ensembl_id: "ENSG00000126804"
name: "zinc finger and BTB domain containing 1"
location: "14q23.3"
module: 95
arm: "+"
pooled_cpm: 95.18
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# ZBTB1

*zinc finger and BTB domain containing 1* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +17.1, q 0e+00, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.198× (z -33.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX6]] (+0.72, fdr 1e-05), [[THAP2]] (+0.71, fdr 1e-05), [[PCNX4-DT]] (+0.70, fdr 4e-05); moves opposite to [[GTF2E2]] (-0.65, fdr 4e-05), [[COG5]] (-0.64, fdr 6e-05), [[PACC1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[JAM2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4769.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +17.1 | 0e+00 | 36/48 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +12.4 | 6e-33 | 44/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +10.9 | 3e-25 | 38/48 (SW480, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +10.3 | 1e-22 | 35/48 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +8.0 | 1e-13 | 33/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +6.5 | 8e-09 | 32/49 (NCI-H460, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +5.2 | 1e-05 | 27/48 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +5.1 | 3e-05 | 32/48 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +4.9 | 6e-05 | 29/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.003 | 24/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +3.7 | 0.010 | 19/48 (RPMI-7951, A-172, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +3.4 | 0.032 | 7/48 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.17× | +3.3 | 0.043 | 14/49 (MIA PaCa-2, SW1417, …) | all doses, flat |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.057 | 14/48 (AsPC-1, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4769.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.198×** | -33.1 | 0e+00 | 48/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.217×** | -31.3 | 0e+00 | 48/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.217×** | -31.2 | 0e+00 | 48/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.450×** | -16.3 | 0e+00 | 48/48 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.528×** | -13.0 | 1e-36 | 45/48 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.707×** | -10.0 | 2e-21 | 38/48 (LS 180, NCI-H23, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.434×** | -8.9 | 4e-17 | 45/49 (SW480, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.700×** | -7.3 | 3e-11 | 36/48 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.773×** | -5.2 | 1e-05 | 31/49 (A-427, NCI-H1573, …) | two highest doses | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.764×** | -5.2 | 1e-05 | 25/48 (H4, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.789×** | -4.8 | 7e-05 | 29/48 (NCI-H1792, A-172, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.784×** | -4.8 | 9e-05 | 25/48 (A-172, AsPC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.793×** | -4.7 | 1e-04 | 29/48 (HOP62, A-172, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.809×** | -4.1 | 0.001 | 27/47 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.870× | -4.0 | 0.003 | 12/49 (MIA PaCa-2, H4, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.828×** | -3.8 | 0.004 | 22/48 (A-172, SW48, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.841× | -3.5 | 0.013 | 21/48 (A-172, RKO, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.844× | -3.5 | 0.015 | 16/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.752×** | -3.0 | 0.058 | 15/46 (RKO, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4769. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 115 | 8 (3 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +17.9) | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -21.2) |
| [[NCI-H460 (line)]] | wt | 88.0 | 8 (3 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.35× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.153× (z -22.1) |
| [[HEC-1-A (line)]] | alt | 87.4 | 5 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -22.4) |
| [[NCI-H1792 (line)]] | alt | 183 | 1 | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.111× (z -27.1) |
| [[NCI-H2347 (line)]] | alt | 76.5 | 6 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +15.9) | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -20.5) |
| [[J82 (line)]] | alt | 74.1 | 3 | 5 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +20.1) | [[Panobinostat (drug)]] 5 µM 0.203× (z -19.8) |
| [[KATO III (line)]] | alt | 61.1 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +21.9) | [[Panobinostat (drug)]] 5 µM 0.156× (z -20.1) |
| [[LoVo (line)]] | wt | 65.4 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +22.5) | [[Belinostat (drug)]] 5 µM 0.212× (z -18.9) |
| [[SW480 (line)]] | alt | 80.4 | 3 | 5 | [[Auranofin (drug)]] 5 µM 2.42× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.146× (z -29.4) |
| [[A-427 (line)]] | wt | 73.4 | 1 | 6 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.39× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -15.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.297× (z -13.8) |
| [[LS 180 (line)]] | wt | 79.3 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -24.2) |
| [[NCI-H1573 (line)]] | alt | 197 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -22.2) |
| [[SK-MEL-2 (line)]] | alt | 78.6 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.321× (z -11.4) |
| [[SW48 (line)]] | wt | 123 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.136× (z -17.5) |
| [[A-172 (line)]] | wt | 115 | 2 | 4 | [[Harringtonine (drug)]] 0.5 µM 2.01× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.172× (z -21.9) |
| [[A549 (line)]] | wt | 101 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.122× (z -22.7) |
| [[COLO 205 (line)]] | alt | 86.7 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.5) | [[Panobinostat (drug)]] 0.5 µM 0.101× (z -22.2) |
| [[HepG2_C3A (line)]] | wt | 78.0 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.185× (z -15.4) |
| [[Hs 766T (line)]] | wt | 93.5 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +21.9) | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -17.7) |
| [[HT-29 (line)]] | alt | 62.8 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +14.5) | [[Belinostat (drug)]] 5 µM 0.160× (z -19.3) |
| [[MIA PaCa-2 (line)]] | alt | 127 | 3 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 3.28× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.125× (z -21.3) |
| [[Panc 03.27 (line)]] | alt | 71.1 | 3 | 3 | [[Auranofin (drug)]] 5 µM 2.47× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -17.3) |
| [[RPMI-7951 (line)]] | alt | 117 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +14.9) | [[Belinostat (drug)]] 5 µM 0.195× (z -16.8) |
| [[SW1417 (line)]] | alt | 63.4 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.8) | [[Belinostat (drug)]] 5 µM 0.255× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 87.6 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.1) | [[Belinostat (drug)]] 5 µM 0.139× (z -18.6) |
| [[CFPAC-1 (line)]] | alt | 128 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.220× (z -18.8) |
| [[H4 (line)]] | wt | 143 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0755× (z -21.3) |
| [[hTERT-HPNE (line)]] | wt | 135 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0876× (z -23.8) |
| [[LOX-IMVI (line)]] | wt | 61.9 | 1 | 4 | [[Auranofin (drug)]] 5 µM 2.24× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -19.0) |
| [[NCI-H23 (line)]] | alt | 230 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.230× (z -18.7) |
| [[PANC-1 (line)]] | alt | 96.5 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -22.5) |
| [[SNU-423 (line)]] | alt | 77.8 | 2 | 3 | [[Auranofin (drug)]] 5 µM 2.83× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.204× (z -16.6) |
| [[SW 900 (line)]] | alt | 138 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.179× (z -17.9) |
| [[C-33 A (line)]] | alt | 128 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -14.0) |
| [[HCT15 (line)]] | alt | 121 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.172× (z -15.2) |
| [[HS-578T (line)]] | alt | 59.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -20.0) |
| [[RKO (line)]] | wt | 67.1 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.29× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -15.0) |
| [[A498 (line)]] | wt | 45.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -11.9) |
| [[AN3 CA (line)]] | alt | 93.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -10.7) |
| [[C32 (line)]] | wt | 93.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -16.5) |
| [[CHP-212 (line)]] | wt | 126 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.165× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 107 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -14.1) |
| [[SNU-1 (line)]] | wt | 118 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.130× (z -18.9) |
| [[SHP-77 (line)]] | alt | 52.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.348× (z -9.6) |
| [[BT-474 (line)]] | alt | 49.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -11.4) |
| [[SW 1088 (line)]] | alt | 121 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0945× (z -8.8) |
| [[SW 1271 (line)]] | alt | 208 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -10.9) |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4769), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX6]] | +0.72 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[THAP2]] | +0.71 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.70 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[GGPS1]] | +0.70 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[ZNF24]] | +0.70 | +0.60 / +0.55 | both halves | 1e-05 | same gene group; STRING 414 |
| [[OXA1L-DT]] | +0.70 | +0.63 / +0.40 | both halves | 4e-05 |  |
| [[INO80D]] | +0.70 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[GTF2H1]] | +0.69 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SUCLG2-DT]] | +0.69 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ZBTB2]] | +0.69 | +0.53 / +0.53 | both halves | 1e-05 | same gene group; STRING 406 |
| [[TMEM202-AS1]] | +0.69 | +0.59 / +0.37 | both halves | 9e-05 |  |
| [[AKT1S1]] | +0.68 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2E2]] | -0.65 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[COG5]] | -0.64 | -0.63 / -0.38 | both halves | 6e-05 |  |
| [[PACC1]] | -0.64 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[SPTLC2]] | -0.63 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[LPCAT4]] | -0.62 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[TOMM5]] | -0.61 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.61 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[CCNY]] | -0.60 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[SLC37A3]] | -0.60 | -0.62 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAM2]] | B | JAM2 activity raises ZBTB1's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 1.35× lower at baseline in the lines without JAM2 | 0.041 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[SUCLG2-DT]] | B | SUCLG2-DT activity raises ZBTB1's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without SUCLG2-DT | 0.050 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ZBTB1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.738). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (4.2, 11.1); signed map (19.2, -21.0). **Vector** length 136, 44.2% of its response variance represented; |z| ≥ 3 in 1,437 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +13.1 | +12.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +13.0 | +17.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +12.5 | +10.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.2 | +10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.6 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.8 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.6 | +5.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.1 | +5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +4.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.0 | -13.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.4 | -31.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.4 | -16.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -10.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.8 | -7.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.6 | -4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.6 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.6 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:64,503,712-64,533,690 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0997, ZNF909 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2K1](https://www.uniprot.org/uniprotkb/Q9Y2K1) (Zinc finger and BTB domain-containing protein 1):

> Acts as a transcriptional repressor. Represses cAMP-responsive element (CRE)-mediated transcriptional activation. In addition, has a role in translesion DNA synthesis. Requires for UV-inducible RAD18 loading, PCNA monoubiquitination, POLH recruitment to replication factories and efficient translesion DNA synthesis. Plays a key role in the transcriptional regulation of T lymphocyte development (By similarity).

**Summary**, from NCBI Gene [22890](https://www.ncbi.nlm.nih.gov/gene/22890):

> Enables K63-linked polyubiquitin modification-dependent protein binding activity; protein heterodimerization activity; and protein homodimerization activity. Involved in several processes, including DNA metabolic process; mRNA transcription by RNA polymerase II; and protein homooligomerization. Located in nuclear body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20259) · Entrez [22890](https://www.ncbi.nlm.nih.gov/gene/22890) · UniProt [Q9Y2K1](https://www.uniprot.org/uniprotkb/Q9Y2K1) · Ensembl [ENSG00000126804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126804)

## Data

Gene col 4769: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4769); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4769, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4769]; `tensor/DDL_lfc|DDL_z.npy` [4769]; `embed/gene_vectors.npy` [4769]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4769 or target_col == 4769). Every well: [[ZBTB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
