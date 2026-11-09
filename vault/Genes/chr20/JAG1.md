---
symbol: "JAG1"
type: "gene"
col: 2128
ensembl_id: "ENSG00000101384"
name: "jagged canonical Notch ligand 1"
location: "20p12.2"
module: 141
arm: "+"
pooled_cpm: 73.27
n_lines_expressing: 44
n_dd_up: 11
n_dd_down: 28
n_dd_up_clean: 8
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# JAG1

*jagged canonical Notch ligand 1* — 20p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.50× (z +18.1, q 0e+00, up in 31 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.629× (z -6.3, q 2e-07, down in 20 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Binimetinib (drug)]] 0.5 µM: 0.740× (z -5.1, q 1e-04, down in 22 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMEPA1]] (+0.64, fdr 7e-06), [[F2RL1]] (+0.62, fdr 8e-06), [[MAP2K3]] (+0.60, fdr 7e-06); moves opposite to [[RAB6A]] (-0.53, fdr 2e-05), [[FBXO42]] (-0.51, fdr 2e-05), [[SOS1]] (-0.49, fdr 2e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ARHGAP26]] → it (grade B ⚠); 6 go from it, the strongest it → [[F2RL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2128.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.50×** | +18.1 | 0e+00 | 31/42 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.46×** | +16.7 | 0e+00 | 38/42 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +8.1 | 9e-14 | 33/41 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +7.8 | 1e-12 | 27/42 (A498, SW48, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.52×** | +6.7 | 2e-09 | 29/43 (SW48, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +6.0 | 2e-07 | 25/42 (NCI-H460, SW1417, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +5.0 | 4e-05 | 24/42 (SW48, SW1417, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.43×** | +5.0 | 4e-05 | 23/42 (COLO 205, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +4.7 | 1e-04 | 25/42 (SW48, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.012 | 20/42 (NCI-H1573, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.27×** | +3.4 | 0.040 | 17/42 (SK-MEL-2, J82, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.11 | 13/42 (LoVo, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2128.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.629×** | -6.3 | 2e-07 | 20/35 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.740×** | -5.1 | 1e-04 | 22/42 (SW480, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -4.6 | 9e-04 | 24/42 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.748×** | -4.5 | 9e-04 | 19/44 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.749×** | -4.5 | 9e-04 | 21/43 (SW480, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | **0.806×** | -4.3 | 0.001 | 20/42 (A-172, A549, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.738×** | -4.3 | 0.001 | 22/43 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -4.2 | 0.001 | 4/44 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.740×** | -4.2 | 0.001 | 19/42 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.786×** | -4.1 | 0.003 | 20/42 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.753×** | -4.0 | 0.003 | 15/43 (KATO III, SW480, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.815×** | -4.0 | 0.004 | 19/43 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.821×** | -3.9 | 0.004 | 17/42 (HOP62, NCI-H2347, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.756×** | -3.8 | 0.006 | 22/41 (hTERT-HPNE, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.828×** | -3.8 | 0.006 | 22/43 (hTERT-HPNE, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.766×** | -3.8 | 0.006 | 20/42 (A-172, A549, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.783×** | -3.4 | 0.019 | 15/41 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.781×** | -3.3 | 0.026 | 17/41 (SW480, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **0.798×** | -3.2 | 0.042 | 15/42 (KATO III, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2128. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 187 | 0 | 16 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.237× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 36.5 | 10 (5 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 7.48× (z +14.4) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 6.88× (z +13.8) | — |
| [[SW48 (line)]] | wt | 67.3 | 6 | 0 | [[Harringtonine (drug)]] 5 µM 10.3× (z +13.8) | — |
| [[J82 (line)]] | alt | 22.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +24.5) | — |
| [[SW1417 (line)]] | alt | 89.6 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -9.5) |
| [[A498 (line)]] | wt | 85.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +24.2) | — |
| [[HepG2_C3A (line)]] | wt | 240 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 7.14× (z +8.6) | [[Binimetinib (drug)]] 5 µM 0.363× (z -9.3) |
| [[A-172 (line)]] | wt | 47.0 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 8.53× (z +12.1) | — |
| [[A549 (line)]] | wt | 117 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +17.0) | — |
| [[AsPC-1 (line)]] | alt | 88.7 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -10.1) |
| [[COLO 205 (line)]] | alt | 75.6 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 5.88× (z +12.5) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.7) | — |
| [[HEC-1-A (line)]] | alt | 29.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +13.5) | — |
| [[LoVo (line)]] | wt | 66.2 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.57× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -8.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 148 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -16.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 39.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 53.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +12.4) | — |
| [[SW 900 (line)]] | alt | 91.7 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.98× (z +12.9) | — |
| [[BT-474 (line)]] | alt | 23.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +16.9) | — |
| [[HS-578T (line)]] | alt | 175 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 6.36× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 10.6× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 40.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 5.18× (z +10.7) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.203× (z -10.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 43.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +15.3) | — |
| [[PANC-1 (line)]] | alt | 52.6 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 5.40× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 54.4 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 10.4× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 140 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.0) | — |
| [[HOP62 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.641× (z -9.3) ⚠ position not correctable |
| [[Hs 766T (line)]] | wt | 215 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -10.0) |
| [[HT-29 (line)]] | alt | 49.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.8) | — |
| [[KATO III (line)]] | alt | 144 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.380× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 29.1 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 6.48× (z +12.7) | — |
| [[NCI-H23 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.544× (z -10.2) ⚠ position not correctable |
| [[RPMI-7951 (line)]] | alt | 52.6 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 11.4× (z +14.1) | — |
| [[SHP-77 (line)]] | alt | 42.4 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.79× (z +10.3) ⚠ toxic | — |
| [[SK-MEL-2 (line)]] | alt | 27.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.0) | — |
| [[A-427 (line)]] | wt | 5.86 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.91 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2128), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMEPA1]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[F2RL1]] | +0.62 | +0.61 / +0.57 | both halves | 8e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[MAP2K3]] | +0.60 | +0.58 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PHLDA1]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[EPHA2]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 | pathway: RAC1 GTPase cycle |
| [[NAB1]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[LINC00460]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[SLC20A1]] | +0.56 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[VCAN]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_ANGIOGENESIS |
| [[NFE2L3]] | +0.56 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[SMAD3]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 523 |
| [[SPRY2]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 | STRING 474 |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB6A]] | -0.53 | -0.48 / -0.54 | both halves | 2e-05 | pathway: Signaling by NOTCH |
| [[FBXO42]] | -0.51 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SOS1]] | -0.49 | -0.47 / -0.54 | both halves | 2e-05 | pathway: RAC1 GTPase cycle |
| [[VDAC1P8]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[GPR107]] | -0.48 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[HMBOX1]] | -0.46 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP26]] | B | ARHGAP26 activity raises JAG1's level | lines that do not express ARHGAP26 (6) vs lines expressing it (44) | 2.39× lower at baseline in the lines without ARHGAP26 | 0.034 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[PWWP3B]] | B | PWWP3B activity raises JAG1's level | lines that do not express PWWP3B (31) vs lines expressing it (19) | 1.69× lower at baseline in the lines without PWWP3B | 0.085 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, SLC15A5, GTF2I-AS1 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2RL1]] | B | JAG1 activity raises F2RL1's level | lines that do not express JAG1 (6) vs lines expressing it (44) | 4.47× lower at baseline in the lines without JAG1 | 0.055 | ⚠ within organs, on part of the lines; also absent: DENND3, SHB, IER3 |
| [[MAP2K3]] | B | JAG1 activity raises MAP2K3's level | lines that do not express JAG1 (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without JAG1 | 0.067 | ⚠ within organs, on part of the lines; also absent: DENND3, SHB, IER3 |
| [[AP1S3]] | B | JAG1 activity raises AP1S3's level | lines that do not express JAG1 (6) vs lines expressing it (44) | 2.08× lower at baseline in the lines without JAG1 | 0.073 | ⚠ within organs, on part of the lines; also absent: DENND3, SHB, IER3 |
| cells under [[Homoharringtonine (drug)]] 0.5 µM | B | JAG1 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express JAG1 (6) vs lines expressing it (42) | the lines without JAG1: 0.32× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: DENND3, SHB, IER3 |
| cells under [[Homoharringtonine (drug)]] 5 µM | B | JAG1 activity raises the cells' numbers under Homoharringtonine 5 µM (protects the cells) | lines that do not express JAG1 (6) vs lines expressing it (42) | the lines without JAG1: 0.24× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: DENND3, SHB, IER3 |
| [[SHB]] | C | JAG1 activity raises SHB's level | lines that do not express JAG1 (6) vs lines expressing it (44) | 2.84× lower at baseline in the lines without JAG1 | 0.069 | ⚠ within organs, on part of the lines; also absent: DENND3, SHB, IER3; co-absent with the target |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.4, 3.3); signed map (5.4, 43.1). **Vector** length 127, 37.4% of its response variance represented; |z| ≥ 3 in 1,156 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.7 | +16.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +6.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.2 | +8.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +18.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.5 | +1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.6 | +1.4 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.2 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.8 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.2 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -4.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.9 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | jagged canonical Notch ligand 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.2 — chr20:10,637,684-10,673,999 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AHD, AWS, HJ1, CD339; previously AGS, JAGL1 |
| Gene groups (HGNC) | CD molecules; MicroRNA protein coding host genes; Canonical Notch ligands |
| Hallmark sets | ANGIOGENESIS, NOTCH_SIGNALING, WNT_BETA_CATENIN_SIGNALING, CHOLESTEROL_HOMEOSTASIS, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 29 pathways, smallest: Constitutive Signaling by NOTCH1 t(7;9)(NOTCH1:M1580_K2555) Translocation Mutant; Signaling by NOTCH1 t(7;9)(NOTCH1:M1580_K2555) Translocation Mutant; NOTCH4 Activation and Transmission of Signal to the Nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [P78504](https://www.uniprot.org/uniprotkb/P78504) (Protein jagged-1):

> Ligand for multiple Notch receptors and involved in the mediation of Notch signaling. May be involved in cell-fate decisions during hematopoiesis. Seems to be involved in early and late stages of mammalian cardiovascular development. Inhibits myoblast differentiation (By similarity). Enhances fibroblast growth factor-induced angiogenesis (in vitro).

**Summary**, from NCBI Gene [182](https://www.ncbi.nlm.nih.gov/gene/182):

> The jagged 1 protein encoded by JAG1 is the human homolog of the Drosophilia jagged protein. Human jagged 1 is the ligand for the receptor notch 1, the latter is involved in signaling processes. Mutations that alter the jagged 1 protein cause Alagille syndrome. Jagged 1 signalling through notch 1 has also been shown to play a role in hematopoiesis. [provided by RefSeq, Nov 2019]

**Accessions** — [HGNC:6188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6188) · Entrez [182](https://www.ncbi.nlm.nih.gov/gene/182) · UniProt [P78504](https://www.uniprot.org/uniprotkb/P78504) · Ensembl [ENSG00000101384](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101384)

## Data

Gene col 2128: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2128); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2128, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2128]; `tensor/DDL_lfc|DDL_z.npy` [2128]; `embed/gene_vectors.npy` [2128]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2128 or target_col == 2128). Every well: [[JAG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JAG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
