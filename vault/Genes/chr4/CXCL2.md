---
symbol: "CXCL2"
type: "gene"
col: 1303
ensembl_id: "ENSG00000081041"
name: "C-X-C motif chemokine ligand 2"
location: "4q13.3"
module: 14
arm: "+"
pooled_cpm: 35.97
n_lines_expressing: 36
n_dd_up: 30
n_dd_down: 8
n_dd_up_clean: 23
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 13
direction_downstream: 19
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CXCL2

*C-X-C motif chemokine ligand 2* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 24.1× (z +35.7, q 0e+00, up in 33 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.521× (z -5.1, q 1e-04, down in 19 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CXCL3]] (+0.87, fdr 7e-06), [[CXCL1]] (+0.80, fdr 7e-06), [[NFKBIA]] (+0.73, fdr 7e-06); moves opposite to [[ZCCHC17]] (-0.61, fdr 1e-05), [[RARS2]] (-0.56, fdr 2e-05), [[LRRC8A]] (-0.56, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[GBP1]] → it (grade B ⚠); 19 go from it, the strongest it → [[ZC3H12A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1303.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **24.1×** | +35.7 | 0e+00 | 33/34 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **27.0×** | +25.1 | 0e+00 | 34/34 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **11.1×** | +19.1 | 0e+00 | 31/33 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **4.94×** | +12.7 | 1e-34 | 27/34 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.49×** | +11.9 | 1e-30 | 26/34 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.27×** | +11.5 | 1e-28 | 25/33 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **18.6×** | +10.9 | 1e-25 | 33/34 (LoVo, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.60×** | +9.8 | 1e-20 | 30/33 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.99×** | +8.7 | 2e-16 | 25/31 (NCI-H1573, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.17×** | +8.5 | 2e-15 | 23/28 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **3.03×** | +7.6 | 1e-12 | 23/33 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +6.7 | 9e-10 | 26/34 (HT-29, NCI-H1792, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.80×** | +6.6 | 2e-09 | 20/34 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.27×** | +6.5 | 3e-09 | 23/33 (HT-29, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **2.24×** | +6.4 | 6e-09 | 24/34 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.48×** | +6.3 | 1e-08 | 21/33 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.98×** | +5.4 | 2e-06 | 24/34 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **2.01×** | +5.3 | 3e-06 | 19/33 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.86×** | +5.0 | 1e-05 | 15/33 (LS 180, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1303.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.521×** | -5.1 | 1e-04 | 19/33 (NCI-H23, Panc 03.27, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.820×** | -5.1 | 1e-04 | 21/34 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.483×** | -5.0 | 1e-04 | 22/34 (NCI-H23, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.550×** | -4.7 | 3e-04 | 21/33 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.555×** | -4.6 | 4e-04 | 21/34 (NCI-H23, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.557×** | -4.6 | 4e-04 | 20/34 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 5 µM |  | **0.365×** | -3.7 | 0.015 | 14/34 (SW 900, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.616×** | -3.3 | 0.067 | 13/33 (NCI-H2030, SNU-423, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.673× | -3.1 | 0.11 | 9/33 (A498, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1303. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 46.9 | 16 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 57.1× (z +20.0) | — |
| [[NCI-H1573 (line)]] | alt | 48.9 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +19.6) | — |
| [[SW 900 (line)]] | alt | 60.6 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +18.6) | — |
| [[HS-578T (line)]] | alt | 24.2 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 41.1× (z +22.1) | — |
| [[hTERT-HPNE (line)]] | wt | 61.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 204× (z +21.7) | — |
| [[NCI-H1792 (line)]] | alt | 67.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +18.2) | — |
| [[NCI-H2347 (line)]] | alt | 76.7 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 30.0× (z +23.2) | [[Auranofin (drug)]] 5 µM 0.168× (z -8.6) |
| [[A498 (line)]] | wt | 181 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +21.5) | — |
| [[HOP62 (line)]] | alt | 25.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 110× (z +21.5) | — |
| [[LoVo (line)]] | wt | 24.3 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 26.4× (z +22.7) | [[Panobinostat (drug)]] 5 µM 0.144× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 114 | 5 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 30.4× (z +17.5) | — |
| [[AsPC-1 (line)]] | alt | 25.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 94.0× (z +28.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 61.0 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 19.9× (z +16.4) | — |
| [[NCI-H23 (line)]] | alt | 40.7 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0195× (z -16.4) |
| [[Panc 03.27 (line)]] | alt | 29.1 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 44.8× (z +21.8) | [[Auranofin (drug)]] 5 µM 0.119× (z -8.7) |
| [[SNU-423 (line)]] | alt | 19.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 54.0× (z +20.9) | — |
| [[A549 (line)]] | wt | 75.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +15.3) | — |
| [[CFPAC-1 (line)]] | alt | 76.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.1× (z +24.5) | — |
| [[HT-29 (line)]] | alt | 19.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.2× (z +19.4) | — |
| [[J82 (line)]] | alt | 23.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 84.8× (z +22.5) | — |
| [[RPMI-7951 (line)]] | alt | 19.5 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 105× (z +13.7) | — |
| [[SW1417 (line)]] | alt | 15.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +18.3) | — |
| [[SW48 (line)]] | wt | 13.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.3× (z +12.4) | — |
| [[BT-474 (line)]] | alt | 14.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 80.3× (z +19.0) | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 69.0× (z +16.0) | — |
| [[KATO III (line)]] | alt | 27.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.117× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 13.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +12.7) | — |
| [[LS 180 (line)]] | wt | 23.6 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 18.1× (z +12.1) | — |
| [[A-427 (line)]] | wt | 14.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.126× (z -9.1) |
| [[COLO 205 (line)]] | alt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.00× (z +8.6) | — |
| [[H4 (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +9.7) | — |
| [[SW 1088 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 46.4× (z +8.7) | — |
| [[SW 1271 (line)]] | alt | 35.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.1× (z +10.2) | — |
| [[A-172 (line)]] | wt | 7.54 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.50 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.09 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.30 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.16 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1303), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXCL3]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 995 |
| [[CXCL1]] | +0.80 | +0.77 / +0.80 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 996 |
| [[NFKBIA]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 681 |
| [[TNFAIP2]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NFKB1]] | +0.69 | +0.60 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 969 |
| [[TNFAIP3]] | +0.67 | +0.61 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 718 |
| [[LINC02605]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[CSF1]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 711 |
| [[PATL2]] | +0.65 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | +0.65 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[HIVEP2]] | +0.65 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[DRAM1]] | +0.63 | +0.62 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC17]] | -0.61 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[RARS2]] | -0.56 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[LRRC8A]] | -0.56 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[MACO1]] | -0.56 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[SAP130]] | -0.56 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[STARD3]] | -0.56 | -0.48 / -0.50 | both halves | 2e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[DIP2A]] | -0.56 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[ZFYVE21]] | -0.55 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[TPD52L2]] | -0.55 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[GPR89A]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[SDHAP4-1]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[NUP43]] | -0.54 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP1]] | B | GBP1 activity raises CXCL2's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.51× lower at baseline in the lines without GBP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[CXCL1]] | B | CXCL1 activity raises CXCL2's level | lines that do not express CXCL1 (17) vs lines expressing it (33) | 2.98× lower at baseline in the lines without CXCL1 | 0.019 | ⚠ within organs, on part of the lines; also absent: CCL20, CDCP1, C15orf48 |
| [[IL6]] | B | IL6 activity raises CXCL2's level | lines that do not express IL6 (32) vs lines expressing it (18) | 3.04× lower at baseline in the lines without IL6 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[EREG]] | B | EREG activity raises CXCL2's level | lines that do not express EREG (26) vs lines expressing it (24) | 1.71× lower at baseline in the lines without EREG | 0.033 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1 |
| [[CSF3]] | B | CSF3 activity raises CXCL2's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 2.82× lower at baseline in the lines without CSF3 | 0.033 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |
| [[KMO]] | B | KMO activity raises CXCL2's level | lines that do not express KMO (18) vs lines expressing it (32) | 2.59× lower at baseline in the lines without KMO | 0.057 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[ZC3H12A]] | B | ZC3H12A activity raises CXCL2's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 2.83× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[CTSS]] | B | CTSS activity raises CXCL2's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.38× lower at baseline in the lines without CTSS | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises CXCL2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CXCL8]] | C | CXCL8 activity raises CXCL2's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 3.59× lower at baseline in the lines without CXCL8 | 3e-04 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48; co-absent with the target |
| [[CXCL3]] | C | CXCL3 activity raises CXCL2's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 3.60× lower at baseline in the lines without CXCL3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B; co-absent with the target |
| [[CCL20]] | C | CCL20 activity raises CXCL2's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.83× lower at baseline in the lines without CCL20 | 0.030 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 16, C 3. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC3H12A]] | B | CXCL2 activity raises ZC3H12A's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 2.41× lower at baseline in the lines without CXCL2 | 0.008 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[CXCL1]] | B | CXCL2 activity raises CXCL1's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 2.82× lower at baseline in the lines without CXCL2 | 0.010 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[AHR]] | B | CXCL2 activity raises AHR's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 3.24× lower at baseline in the lines without CXCL2 | 0.013 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[EREG]] | B | CXCL2 activity raises EREG's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 2.90× lower at baseline in the lines without CXCL2 | 0.015 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[REL]] | B | CXCL2 activity raises REL's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.22× lower at baseline in the lines without CXCL2 | 0.023 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[TAPBPL]] | B | CXCL2 activity raises TAPBPL's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.29× lower at baseline in the lines without CXCL2 | 0.027 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[EBI3]] | B | CXCL2 activity raises EBI3's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.03× lower at baseline in the lines without CXCL2 | 0.028 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[FOSL2]] | B | CXCL2 activity raises FOSL2's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.51× lower at baseline in the lines without CXCL2 | 0.032 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[CCNL1]] | B | CXCL2 activity raises CCNL1's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.31× lower at baseline in the lines without CXCL2 | 0.036 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[NUP43]] | B | CXCL2 activity lowers NUP43's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.39× higher at baseline in the lines without CXCL2 | 0.071 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[CAPN10]] | B | CXCL2 activity raises CAPN10's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.18× lower at baseline in the lines without CXCL2 | 0.074 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[GBP1]] | B | CXCL2 activity raises GBP1's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 2.27× lower at baseline in the lines without CXCL2 | 0.075 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.8, 6.0); signed map (42.3, 7.2). **Vector** length 117, 36.9% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *IL6 JAK STAT3 signaling* (hallmark, mean cos +0.53 to 11); *IkBA variant leads to EDA-ID* (reactome, mean cos +0.57 to 4); *Toll Like Receptor 3 (TLR3) Cascade* (reactome, mean cos +0.50 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.0 | +6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.4 | +25.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +35.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.2 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.4 | -5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.8 | -5.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.5 | -4.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -4.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | C-X-C motif chemokine ligand 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:74,097,040-74,099,196 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCYB2, GROb, MIP-2a, MGSA-b, CINC-2a; previously GRO2 |
| Gene groups (HGNC) | Chemokine ligands |
| Hallmark sets | UV_RESPONSE_UP, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 10 pathways, smallest: Chemokine receptors bind chemokines; Interleukin-10 signaling; Peptide ligand-binding receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P19875](https://www.uniprot.org/uniprotkb/P19875) (C-X-C motif chemokine 2):

> Produced by activated monocytes and neutrophils and expressed at sites of inflammation. Hematoregulatory chemokine, which, in vitro, suppresses hematopoietic progenitor cell proliferation. GRO-beta(5-73) shows a highly enhanced hematopoietic activity.

**Summary**, from NCBI Gene [2920](https://www.ncbi.nlm.nih.gov/gene/2920):

> This antimicrobial gene is part of a chemokine superfamily that encodes secreted proteins involved in immunoregulatory and inflammatory processes. The superfamily is divided into four subfamilies based on the arrangement of the N-terminal cysteine residues of the mature peptide. This chemokine, a member of the CXC subfamily, is expressed at sites of inflammation and may suppress hematopoietic progenitor cell proliferation. [provided by RefSeq, Sep 2014]

**Accessions** — [HGNC:4603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4603) · Entrez [2920](https://www.ncbi.nlm.nih.gov/gene/2920) · UniProt [P19875](https://www.uniprot.org/uniprotkb/P19875) · Ensembl [ENSG00000081041](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081041)

## Data

Gene col 1303: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1303); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1303, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1303]; `tensor/DDL_lfc|DDL_z.npy` [1303]; `embed/gene_vectors.npy` [1303]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1303 or target_col == 1303). Every well: [[CXCL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CXCL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
