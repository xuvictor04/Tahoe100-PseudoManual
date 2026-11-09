---
symbol: "DDX60"
type: "gene"
col: 6041
ensembl_id: "ENSG00000137628"
name: "DExD/H-box helicase 60"
location: "4q32.3"
module: 32
arm: "+"
pooled_cpm: 125.0
n_lines_expressing: 44
n_dd_up: 17
n_dd_down: 57
n_dd_up_clean: 15
n_dd_down_clean: 44
in_vector_space: true
direction_upstream: 65
direction_downstream: 45
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# DDX60

*DExD/H-box helicase 60* — 4q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.22× (z +8.8, q 5e-16, up in 37 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 57 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.147× (z -21.3, q 0e+00, down in 42 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARP14]] (+0.92, fdr 7e-06), [[DDX60L]] (+0.92, fdr 7e-06, ⚠ same locus), [[IFIT3]] (+0.90, fdr 7e-06), [[IFIH1]] (+0.90, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 65 arrows point to it, the strongest [[SAMD9L]] → it (grade B ⚠); 45 go from it, the strongest it → [[DDX60L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6041.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.22×** | +8.8 | 5e-16 | 37/42 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +8.8 | 5e-16 | 29/41 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.74×** | +5.9 | 6e-07 | 31/41 (NCI-H2347, RKO, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.53×** | +4.7 | 4e-04 | 29/41 (AsPC-1, RKO, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +4.6 | 6e-04 | 25/42 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.51×** | +4.4 | 9e-04 | 26/42 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.35×** | +4.3 | 0.002 | 28/42 (AsPC-1, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.39×** | +4.0 | 0.005 | 27/44 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.006 | 27/43 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.017 | 25/42 (MIA PaCa-2, SW1417, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.024 | 22/43 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.39×** | +3.5 | 0.024 | 25/42 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.39×** | +3.5 | 0.024 | 25/43 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.024 | 24/42 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.024 | 26/42 (AsPC-1, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.38×** | +3.3 | 0.033 | 24/42 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 57 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6041.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.147×** | -21.3 | 0e+00 | 42/42 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.168×** | -19.8 | 0e+00 | 42/42 (RKO, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.171×** | -19.6 | 0e+00 | 42/42 (RKO, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.288×** | -13.8 | 2e-41 | 42/42 (LoVo, RKO, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.295×** | -13.6 | 9e-40 | 36/43 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.308×** | -13.1 | 5e-37 | 40/42 (RKO, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.447×** | -12.6 | 1e-34 | 31/43 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.319×** | -12.2 | 2e-32 | 37/41 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.362×** | -11.3 | 1e-27 | 42/42 (RKO, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.363×** | -11.3 | 1e-27 | 37/42 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.375×** | -10.9 | 6e-26 | 40/42 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.383×** | -10.7 | 8e-25 | 37/42 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.515×** | -10.4 | 9e-24 | 37/42 (COLO 205, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.541×** | -9.6 | 2e-20 | 28/43 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.390×** | -9.6 | 4e-20 | 40/42 (RKO, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.206×** | -9.2 | 2e-18 | 36/43 (KATO III, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.477×** | -8.2 | 6e-15 | 38/42 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 111 | 0 | 32 (10 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0462× (z -23.9) |
| [[BT-474 (line)]] | alt | 139 | 0 | 24 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0659× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.171× (z -18.5) |
| [[LoVo (line)]] | wt | 248 | 2 | 22 (6 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.85× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.0754× (z -22.4) |
| [[NCI-H1573 (line)]] | alt | 171 | 1 | 22 (7 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.51× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.0653× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0759× (z -22.2) |
| [[SNU-423 (line)]] | alt | 121 | 0 | 23 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0722× (z -21.4) |
| [[A549 (line)]] | wt | 137 | 0 | 20 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -24.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0921× (z -20.2) |
| [[KATO III (line)]] | alt | 232 | 0 | 19 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0808× (z -18.0) |
| [[MIA PaCa-2 (line)]] | alt | 128 | 0 | 19 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0696× (z -19.7) |
| [[CFPAC-1 (line)]] | alt | 212 | 2 (1 ⚠) | 16 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.05× (z +9.3) | [[Tofacitinib (drug)]] 5 µM 0.250× (z -16.5) |
| [[NCI-H1792 (line)]] | alt | 121 | 0 | 18 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.105× (z -18.2) |
| [[NCI-H23 (line)]] | alt | 57.5 | 0 | 16 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0736× (z -18.5) |
| [[COLO 205 (line)]] | alt | 366 | 0 | 15 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0526× (z -20.1) |
| [[NCI-H2347 (line)]] | alt | 281 | 3 (1 ⚠) | 11 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 4.01× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.27× (z +9.8) | [[Tofacitinib (drug)]] 5 µM 0.292× (z -14.4) |
| [[PANC-1 (line)]] | alt | 55.8 | 1 | 13 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.81× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.214× (z -15.1) |
| [[A498 (line)]] | wt | 163 | 0 | 13 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -16.7) |
| [[AsPC-1 (line)]] | alt | 197 | 1 (1 ⚠) | 12 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.0890× (z -18.3) |
| [[HS-578T (line)]] | alt | 93.0 | 0 | 13 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0985× (z -17.5) |
| [[RPMI-7951 (line)]] | alt | 165 | 0 | 13 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0687× (z -22.1) |
| [[SHP-77 (line)]] | alt | 68.0 | 0 | 13 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0894× (z -14.1) |
| [[A-172 (line)]] | wt | 197 | 0 | 11 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.117× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 232 | 3 (2 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.75× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.245× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 228 | 2 (2 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 117 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -18.8) |
| [[HEC-1-A (line)]] | alt | 55.2 | 4 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +17.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.12× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -15.1) |
| [[LS 180 (line)]] | wt | 158 | 1 (1 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.262× (z -11.1) |
| [[Hs 766T (line)]] | wt | 240 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 66.7 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.115× (z -15.0) |
| [[C-33 A (line)]] | alt | 45.6 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.0942× (z -13.1) |
| [[CHP-212 (line)]] | wt | 91.4 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.0534× (z -13.1) |
| [[H4 (line)]] | wt | 141 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -12.0) |
| [[HOP62 (line)]] | alt | 61.5 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +17.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.44× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 87.8 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.189× (z -10.4) |
| [[SW1417 (line)]] | alt | 77.2 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.181× (z -12.8) |
| [[C32 (line)]] | wt | 60.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -10.8) |
| [[SW 900 (line)]] | alt | 125 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.166× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 33.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +21.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.52× (z +13.0) | — |
| [[HCT15 (line)]] | alt | 50.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -9.4) |
| [[SW 1088 (line)]] | alt | 167 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0872× (z -8.8) |
| [[A-427 (line)]] | wt | 17.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 18.2 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.5 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARP14]] | +0.92 | +0.88 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 667 |
| [[DDX60L]] | +0.92 | +0.90 / +0.93 | both halves | 7e-06 | same gene group; STRING 773; ⚠ same locus (37.9 kb, same strand: neighbours can correlate without regulation) |
| [[IFIT3]] | +0.90 | +0.83 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 936 |
| [[IFIH1]] | +0.90 | +0.84 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 987 |
| [[SAMD9L]] | +0.89 | +0.82 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 872 |
| [[XAF1]] | +0.89 | +0.82 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 850 |
| [[OAS2]] | +0.89 | +0.80 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 907 |
| [[RSAD2]] | +0.89 | +0.81 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 911 |
| [[SAMD9]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 893 |
| [[RIGI]] | +0.88 | +0.80 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 992 |
| [[IFIT1]] | +0.87 | +0.79 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 944 |
| [[DTX3L]] | +0.87 | +0.81 / +0.88 | both halves | 7e-06 | STRING 562 |
| [[PARP9]] | +0.87 | +0.78 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 883 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*65 arrows, 65 of them with an alert ⚠; grade A 0, B 52, C 13. Shown: the 12 strongest; 53 more arrows (53 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD9L]] | B | SAMD9L activity raises DDX60's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 3.27× lower at baseline in the lines without SAMD9L | 3e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[GBP4]] | B | GBP4 activity raises DDX60's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 3.20× lower at baseline in the lines without GBP4 | 6e-04 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[OAS2]] | B | OAS2 activity raises DDX60's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 3.27× lower at baseline in the lines without OAS2 | 7e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[PLAAT4]] | B | PLAAT4 activity raises DDX60's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.81× lower at baseline in the lines without PLAAT4 | 7e-04 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[RSAD2]] | B | RSAD2 activity raises DDX60's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.21× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[TRIM22]] | B | TRIM22 activity raises DDX60's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.65× lower at baseline in the lines without TRIM22 | 0.001 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[DDX60L]] | B | DDX60L activity raises DDX60's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 4.19× lower at baseline in the lines without DDX60L | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[IFI16]] | B | IFI16 activity raises DDX60's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.72× lower at baseline in the lines without IFI16 | 0.001 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[MX1]] | B | MX1 activity raises DDX60's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.28× lower at baseline in the lines without MX1 | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[OAS1]] | B | OAS1 activity raises DDX60's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.47× lower at baseline in the lines without OAS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IFIT3]] | B | IFIT3 activity raises DDX60's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 3.10× lower at baseline in the lines without IFIT3 | 0.004 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[EPSTI1]] | B | EPSTI1 activity raises DDX60's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.51× lower at baseline in the lines without EPSTI1 | 0.005 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |

### Downstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 42, C 3. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX60L]] | B | DDX60 activity raises DDX60L's level | lines that do not express DDX60 (6) vs lines expressing it (44) | 5.04× lower at baseline in the lines without DDX60 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, RNASEL, SAMD9; maybe low, not absent |
| [[PARP14]] | B | DDX60 activity raises PARP14's level | lines that do not express DDX60 (6) vs lines expressing it (44) | 2.45× lower at baseline in the lines without DDX60 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, RNASEL, SAMD9; maybe low, not absent |
| [[SP100]] | B | DDX60 activity raises SP100's level | lines that do not express DDX60 (6) vs lines expressing it (44) | 2.46× lower at baseline in the lines without DDX60 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, RNASEL, SAMD9; maybe low, not absent |
| [[IFIT3]] | B | DDX60 activity raises IFIT3's level | lines that do not express DDX60 (6) vs lines expressing it (44) | 4.39× lower at baseline in the lines without DDX60 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, RNASEL, SAMD9; maybe low, not absent |
| [[IFIT1]] | B | DDX60 activity raises IFIT1's level | lines that do not express DDX60 (6) vs lines expressing it (44) | 3.19× lower at baseline in the lines without DDX60 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, RNASEL, SAMD9; maybe low, not absent |
| [[RSAD2]] | B | DDX60 activity raises RSAD2's level | lines that do not express DDX60 (6) vs lines expressing it (44) | 4.11× lower at baseline in the lines without DDX60 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, RNASEL, SAMD9; maybe low, not absent |
| [[PLSCR1]] | B | DDX60 activity raises PLSCR1's level | lines that do not express DDX60 (6) vs lines expressing it (44) | 2.81× lower at baseline in the lines without DDX60 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, RNASEL, SAMD9; maybe low, not absent |
| [[GBP3]] | B | DDX60 activity raises GBP3's level | lines that do not express DDX60 (6) vs lines expressing it (44) | 4.60× lower at baseline in the lines without DDX60 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, RNASEL, SAMD9; maybe low, not absent |
| [[OAS2]] | B | DDX60 activity raises OAS2's level | lines that do not express DDX60 (6) vs lines expressing it (44) | 4.30× lower at baseline in the lines without DDX60 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, RNASEL, SAMD9; maybe low, not absent |
| [[MYD88]] | B | DDX60 activity raises MYD88's level | lines that do not express DDX60 (6) vs lines expressing it (44) | 1.80× lower at baseline in the lines without DDX60 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, RNASEL, SAMD9; maybe low, not absent |
| [[OAS1]] | B | DDX60 activity raises OAS1's level | lines that do not express DDX60 (6) vs lines expressing it (44) | 3.01× lower at baseline in the lines without DDX60 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, RNASEL, SAMD9; maybe low, not absent |
| [[CASP8]] | B | DDX60 activity raises CASP8's level | lines that do not express DDX60 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without DDX60 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, RNASEL, SAMD9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.904). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.5, 53.6); signed map (63.7, 31.7). **Vector** length 150, 61.3% of its response variance represented; |z| ≥ 3 in 2,000 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.84 to 23); *Interferon Signaling* (reactome, mean cos +0.77 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.80 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +15.6 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +15.2 | +8.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +12.3 | +1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.9 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.2 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.9 | +5.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.3 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.3 | +1.6 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -9.9 | -12.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.7 | -10.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.5 | -7.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -8.5 | -9.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -7.8 | -7.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.7 | -13.6 |

## What is on record

|  |  |
|---|---|
| Name | DExD/H-box helicase 60 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.3 — chr4:168,216,291-168,318,883 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20035 |
| Gene groups (HGNC) | Ski2 like RNA helicases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY21](https://www.uniprot.org/uniprotkb/Q8IY21) (Probable ATP-dependent RNA helicase DDX60):

> Positively regulates RIGI- and IFIH1/MDA5-dependent type I interferon and interferon inducible gene expression in response to viral infection. Binds ssRNA, dsRNA and dsDNA and can promote the binding of RIGI to dsRNA. Exhibits antiviral activity against hepatitis C virus and vesicular stomatitis virus (VSV). Selectively reduces infectious titers of viruses that depend on type II IRES-mediated translation by modulating ribosome occupancy on type II IRES-containing viral mRNAs, without affecting …

**Summary**, from NCBI Gene [55601](https://www.ncbi.nlm.nih.gov/gene/55601):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases which are implicated in a number of cellular procsses involving RNA binding and alteration of RNA secondary structure. This gene encodes a DEXD/H box RNA helicase that functions as an antiviral factor and promotes RIG-I-like receptor-mediated signaling. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:25942](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25942) · Entrez [55601](https://www.ncbi.nlm.nih.gov/gene/55601) · UniProt [Q8IY21](https://www.uniprot.org/uniprotkb/Q8IY21) · Ensembl [ENSG00000137628](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137628)

## Data

Gene col 6041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6041); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6041]; `tensor/DDL_lfc|DDL_z.npy` [6041]; `embed/gene_vectors.npy` [6041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6041 or target_col == 6041). Every well: [[DDX60 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX60.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
