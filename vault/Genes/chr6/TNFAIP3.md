---
symbol: "TNFAIP3"
type: "gene"
col: 3995
ensembl_id: "ENSG00000118503"
name: "TNF alpha induced protein 3"
location: "6q23.3"
module: 14
arm: "+"
pooled_cpm: 113.64
n_lines_expressing: 47
n_dd_up: 25
n_dd_down: 9
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 8
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TNFAIP3

*TNF alpha induced protein 3* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 13.0× (z +39.9, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.461× (z -8.5, q 9e-15, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFKBIA]] (+0.85, fdr 7e-06), [[ZC3H12A]] (+0.75, fdr 7e-06), [[BIRC3]] (+0.75, fdr 7e-06); moves opposite to [[MBOAT7]] (-0.57, fdr 1e-05), [[ZCCHC17]] (-0.55, fdr 1e-05), [[SAP130]] (-0.55, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CCL20]] → it (grade B ⚠); 8 go from it, the strongest it → [[ARID5B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3995.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **13.0×** | +39.9 | 0e+00 | 45/45 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **12.9×** | +26.4 | 0e+00 | 45/45 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **83.5×** | +25.5 | 0e+00 | 46/46 (NCI-H2347, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.39×** | +20.4 | 0e+00 | 44/45 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **5.28×** | +18.3 | 0e+00 | 42/45 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **8.39×** | +12.2 | 2e-32 | 39/45 (NCI-H2347, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.66×** | +10.7 | 5e-25 | 41/45 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +9.1 | 7e-18 | 38/45 (HT-29, PANC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **2.31×** | +8.6 | 4e-16 | 38/45 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.18×** | +8.6 | 6e-16 | 40/45 (KATO III, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +8.5 | 1e-15 | 38/44 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 0.5 µM |  | **2.90×** | +8.4 | 3e-15 | 33/45 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +7.3 | 1e-11 | 29/41 (HS-578T, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +6.7 | 6e-10 | 33/46 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.82×** | +6.6 | 2e-09 | 34/45 (KATO III, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.84×** | +6.2 | 2e-08 | 34/44 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.71×** | +5.9 | 1e-07 | 32/45 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.53×** | +4.7 | 7e-05 | 29/46 (SW1417, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.004 | 26/45 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.021 | 22/46 (BT-474, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3995.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.461×** | -8.5 | 9e-15 | 39/45 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.594×** | -5.7 | 3e-06 | 37/46 (J82, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.614×** | -5.0 | 9e-05 | 23/40 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -4.7 | 4e-04 | 27/46 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.666×** | -4.2 | 0.003 | 26/45 (A549, COLO 205, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.681×** | -4.0 | 0.007 | 24/45 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.529×** | -3.7 | 0.020 | 25/44 (J82, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **0.717×** | -3.4 | 0.042 | 20/45 (HCT15, H4, …) | top dose only | plate-row cell shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.575×** | -3.2 | 0.091 | 22/42 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.753× | -3.1 | 0.10 | 17/45 (SW 1088, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3995. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 511 | 11 (4 ⚠) | 10 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 53.1× (z +20.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -20.7) |
| [[C32 (line)]] | wt | 77.2 | 10 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +25.7) | [[Auranofin (drug)]] 5 µM 0.227× (z -9.2) |
| [[BT-474 (line)]] | alt | 133 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 40.7× (z +26.9) | — |
| [[HS-578T (line)]] | alt | 176 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 29.6× (z +32.0) | — |
| [[KATO III (line)]] | alt | 28.5 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +26.4) | — |
| [[NCI-H1573 (line)]] | alt | 124 | 9 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 300× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -9.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 32.6 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 33.1× (z +40.2) | — |
| [[A498 (line)]] | wt | 165 | 6 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +27.7) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -8.9) |
| [[LoVo (line)]] | wt | 44.9 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +29.7) | — |
| [[LS 180 (line)]] | wt | 45.7 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +22.2) | — |
| [[hTERT-HPNE (line)]] | wt | 272 | 7 | 1 | [[Homoharringtonine (drug)]] 5 µM 29.8× (z +30.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 177 | 7 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 150× (z +24.5) | [[Dinaciclib (drug)]] 5 µM 0.362× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 82.1 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +23.1) | — |
| [[SW48 (line)]] | wt | 37.5 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +19.3) | — |
| [[A-172 (line)]] | wt | 99.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.6× (z +29.2) | — |
| [[A549 (line)]] | wt | 159 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +24.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 62.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +27.0) | — |
| [[NCI-H2030 (line)]] | alt | 63.2 | 7 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 38.4× (z +21.8) | — |
| [[NCI-H23 (line)]] | alt | 110 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 29.3× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -16.5) |
| [[Panc 03.27 (line)]] | alt | 111 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +26.7) | — |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +23.3) | — |
| [[SW1417 (line)]] | alt | 59.7 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +24.8) | — |
| [[SW480 (line)]] | alt | 40.8 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.05× (z +23.2) | [[Dinaciclib (drug)]] 5 µM 0.0514× (z -23.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 106 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +30.1) | [[Auranofin (drug)]] 5 µM 0.327× (z -8.5) |
| [[HOP62 (line)]] | alt | 99.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +25.5) | — |
| [[J82 (line)]] | alt | 246 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.84× (z +26.3) | [[Auranofin (drug)]] 5 µM 0.298× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 58.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.72× (z +20.2) | — |
| [[SNU-423 (line)]] | alt | 171 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.9× (z +28.4) | — |
| [[H4 (line)]] | wt | 61.5 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.87× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.0814× (z -11.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 334 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.267× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 32.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.4× (z +30.3) | — |
| [[NCI-H1792 (line)]] | alt | 145 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +17.7) | — |
| [[RPMI-7951 (line)]] | alt | 99.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +22.1) | — |
| [[SNU-1 (line)]] | wt | 30.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.8× (z +21.7) | — |
| [[AN3 CA (line)]] | alt | 84.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.23× (z +14.8) | — |
| [[CFPAC-1 (line)]] | alt | 148 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.91× (z +24.8) | — |
| [[HCT15 (line)]] | alt | 32.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.53× (z +15.8) | — |
| [[Hs 766T (line)]] | wt | 74.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +25.3) | — |
| [[HT-29 (line)]] | alt | 42.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +22.3) | — |
| [[COLO 205 (line)]] | alt | 122 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +16.9) | — |
| [[CHP-212 (line)]] | wt | 40.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.15× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 40.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +11.2) | — |
| [[SW 1088 (line)]] | alt | 151 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +9.9) | — |
| [[SW 1271 (line)]] | alt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +11.6) | — |
| [[A-427 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3995), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBIA]] | +0.85 | +0.84 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 870 |
| [[ZC3H12A]] | +0.75 | +0.68 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 708 |
| [[BIRC3]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 916 |
| [[CXCL2]] | +0.67 | +0.61 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 718 |
| [[SOD2]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 480 |
| [[EBI3]] | +0.64 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[NFKBIZ]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 | STRING 788 |
| [[CCL20]] | +0.63 | +0.58 / +0.62 | both halves | 8e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 698 |
| [[TIPARP]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[HIVEP2]] | +0.62 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[CSF1]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PLPP3]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT7]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.55 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[SAP130]] | -0.55 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[UFD1]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 | pathway: Deubiquitination |
| [[AAK1]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[VPS53]] | -0.53 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[DIP2A]] | -0.53 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TANGO2]] | -0.52 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[CERS5]] | -0.52 | -0.58 / -0.43 | both halves | 4e-05 |  |
| [[GDAP2]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[CAPN10]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[SGSM3]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCL20]] | B | CCL20 activity raises TNFAIP3's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.18× lower at baseline in the lines without CCL20 | 0.014 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[CXCL3]] | B | CXCL3 activity raises TNFAIP3's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 2.24× lower at baseline in the lines without CXCL3 | 0.018 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[NEDD9]] | B | NEDD9 activity raises TNFAIP3's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 2.12× lower at baseline in the lines without NEDD9 | 0.020 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[RHCG]] | B | RHCG activity raises TNFAIP3's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.43× lower at baseline in the lines without RHCG | 0.038 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[ETS2]] | B | ETS2 activity raises TNFAIP3's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.16× lower at baseline in the lines without ETS2 | 0.052 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[ZC3H12A]] | B | ZC3H12A activity raises TNFAIP3's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 3.41× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[NFATC2]] | B | NFATC2 activity raises TNFAIP3's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 2.15× lower at baseline in the lines without NFATC2 | 0.081 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[IL1R1]] | B | IL1R1 activity raises TNFAIP3's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 2.70× lower at baseline in the lines without IL1R1 | 0.084 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1 |
| [[ARID5B]] | C | ARID5B activity raises TNFAIP3's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 2.67× lower at baseline in the lines without ARID5B | 0.063 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARID5B]] | C | TNFAIP3 activity raises ARID5B's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 6.55× lower at baseline in the lines without TNFAIP3 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[KLF4]] | C | TNFAIP3 activity raises KLF4's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 4.59× lower at baseline in the lines without TNFAIP3 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[BCL3]] | C | TNFAIP3 activity raises BCL3's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 3.78× lower at baseline in the lines without TNFAIP3 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[FOSL2]] | C | TNFAIP3 activity raises FOSL2's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 1.71× lower at baseline in the lines without TNFAIP3 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent; its own permutation p |
| [[FAM20B]] | C | TNFAIP3 activity lowers FAM20B's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 1.67× higher at baseline in the lines without TNFAIP3 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent; its own permutation p |
| [[BIRC2]] | C | TNFAIP3 activity lowers BIRC2's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 1.40× higher at baseline in the lines without TNFAIP3 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent; its own permutation p |
| [[TXNIP]] | C | TNFAIP3 activity raises TXNIP's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 4.99× lower at baseline in the lines without TNFAIP3 | 0.087 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent |
| [[CERS5]] | C | TNFAIP3 activity lowers CERS5's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 1.33× higher at baseline in the lines without TNFAIP3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.4, 9.4); signed map (12.6, 28.8). **Vector** length 141, 49.5% of its response variance represented; |z| ≥ 3 in 1,574 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *IkBA variant leads to EDA-ID* (reactome, mean cos +0.54 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.6 | +9.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.9 | +18.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.9 | +6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.7 | +25.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.4 | +26.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.1 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +5.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.4 | +2.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.4 | +2.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.0 | -8.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | -9.5 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -9.1 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.7 | -2.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | -4.1 | -3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.5 | -0.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.3 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | TNF alpha induced protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3 — chr6:137,867,214-137,883,314 (+) |
| Ensembl biotype | protein_coding |
| Also known as | A20, OTUD7C |
| Gene groups (HGNC) | OTU domain containing; Zinc fingers A20-type; Atypical E3 ubiquitin ligases |
| Hallmark sets | COMPLEMENT, KRAS_SIGNALING_UP, INTERFERON_GAMMA_RESPONSE, HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 12 pathways, smallest: TNFR1-induced proapoptotic signaling; TNFR1-induced NF-kappa-B signaling pathway; NOD1/2 Signaling Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P21580](https://www.uniprot.org/uniprotkb/P21580) (Tumor necrosis factor alpha-induced protein 3):

> Ubiquitin-editing enzyme that contains both ubiquitin ligase and deubiquitinase activities. Involved in immune and inflammatory responses signaled by cytokines, such as TNF and IL-1 beta, or pathogens via Toll-like receptors (TLRs) through terminating NF-kappa-B activity. Essential component of a ubiquitin-editing protein complex, comprising also RNF11, ITCH and TAX1BP1, that ensures the transient nature of inflammatory signaling pathways. In cooperation with TAX1BP1 promotes disassembly of …

**Summary**, from NCBI Gene [7128](https://www.ncbi.nlm.nih.gov/gene/7128):

> This gene was identified as a gene whose expression is rapidly induced by the tumor necrosis factor (TNF). The protein encoded by this gene is a zinc finger protein and ubiqitin-editing enzyme, and has been shown to inhibit NF-kappa B activation as well as TNF-mediated apoptosis. The encoded protein, which has both ubiquitin ligase and deubiquitinase activities, is involved in the cytokine-mediated immune and inflammatory responses. Several transcript variants encoding the same protein have …

**Accessions** — [HGNC:11896](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11896) · Entrez [7128](https://www.ncbi.nlm.nih.gov/gene/7128) · UniProt [P21580](https://www.uniprot.org/uniprotkb/P21580) · Ensembl [ENSG00000118503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118503)

## Data

Gene col 3995: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3995); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3995, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3995]; `tensor/DDL_lfc|DDL_z.npy` [3995]; `embed/gene_vectors.npy` [3995]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3995 or target_col == 3995). Every well: [[TNFAIP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFAIP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
