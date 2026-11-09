---
symbol: "RNFT2"
type: "gene"
col: 5658
ensembl_id: "ENSG00000135119"
name: "ring finger protein, transmembrane 2"
location: "12q24.22"
module: 23
arm: "-"
pooled_cpm: 10.3
n_lines_expressing: 47
n_dd_up: 23
n_dd_down: 13
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# RNFT2

*ring finger protein, transmembrane 2* — 12q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 9.09× (z +28.4, q 0e+00, up in 44 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.437× (z -10.7, q 6e-24, down in 35 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC20]] (+0.66, fdr 1e-05), [[COA1]] (+0.63, fdr 1e-05), [[TNFAIP8L1]] (+0.59, fdr 6e-05); moves opposite to [[ATXN1L]] (-0.62, fdr 1e-04), [[CHD1-DT]] (-0.60, fdr 2e-04), [[DNAI4]] (-0.59, fdr 3e-04).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ADAM22]] → it (grade B ⚠); 5 go from it, the strongest it → [[KRBOX5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5658.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **9.09×** | +28.4 | 0e+00 | 44/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.80×** | +26.5 | 0e+00 | 44/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.27×** | +23.6 | 0e+00 | 43/44 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.52×** | +16.2 | 0e+00 | 41/44 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.38×** | +15.8 | 0e+00 | 42/44 (LoVo, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **6.06×** | +12.1 | 6e-32 | 38/44 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **2.04×** | +9.2 | 4e-18 | 21/34 (KATO III, CFPAC-1, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.99×** | +8.8 | 7e-17 | 27/43 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.91×** | +8.3 | 7e-15 | 26/42 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.80×** | +7.0 | 2e-10 | 12/22 (LoVo, J82, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.62×** | +5.9 | 1e-07 | 8/16 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Afatinib (drug)]] 5 µM |  | **1.43×** | +5.0 | 3e-05 | 19/44 (HEC-1-A, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +5.0 | 3e-05 | 12/33 (HT-29, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.31×** | +4.9 | 3e-05 | 13/44 (HT-29, SHP-77, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.31×** | +4.9 | 4e-05 | 15/41 (LS 180, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.004 | 15/44 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.005 | 8/44 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.008 | 10/44 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.009 | 10/45 (A-172, HEC-1-A, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.013 | 7/44 (LoVo, KATO III, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.026 | 10/44 (PANC-1, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5658.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.437×** | -10.7 | 6e-24 | 35/44 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.489×** | -9.3 | 6e-18 | 29/44 (SHP-77, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.526×** | -8.3 | 2e-14 | 25/42 (SHP-77, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.587×** | -6.9 | 7e-10 | 21/43 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.744×** | -5.4 | 6e-06 | 14/44 (LS 180, SHP-77, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.776×** | -4.7 | 3e-04 | 13/44 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.707×** | -4.3 | 0.001 | 18/36 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.710×** | -4.3 | 0.001 | 15/43 (RKO, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.732×** | -4.1 | 0.003 | 17/40 (PANC-1, C-33 A, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.581×** | -3.7 | 0.013 | 12/39 (RKO, J82, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.777×** | -3.3 | 0.053 | 11/44 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.782×** | -3.2 | 0.066 | 13/44 (A-172, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.790×** | -3.1 | 0.092 | 10/44 (NCI-H23, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.73 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5658. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.7 | 4 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 10.9× (z +15.1) | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.146× (z -12.2) |
| [[SW480 (line)]] | alt | 12.8 | 4 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.36× (z +13.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -14.0) |
| [[LoVo (line)]] | wt | 6.71 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 12.6× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 23.8 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 9.88 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.77× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.136× (z -10.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 67.5 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -12.9) |
| [[A-172 (line)]] | wt | 6.63 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.6× (z +11.4) | — |
| [[A-427 (line)]] | wt | 42.3 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -13.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 7.36 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.8× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 4.20 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.7× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 12.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.96× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 8.20 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 12.1× (z +8.5) | [[Econazole (drug)]] 0.05 µM 0.0640× (z -9.4) |
| [[HOP62 (line)]] | alt | 4.71 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 16.0× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 11.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.62× (z +9.3) | — |
| [[KATO III (line)]] | alt | 7.42 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 11.4× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 4.79 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 15.9× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0644× (z -9.5) |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0594× (z -10.4) |
| [[Hs 766T (line)]] | wt | 2.78 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 25.0× (z +9.6) | — |
| [[J82 (line)]] | alt | 11.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.46× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 7.15 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.30× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.05 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 10.7× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 16.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.42× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 11.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.92× (z +9.5) | — |
| [[C32 (line)]] | wt | 2.95 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 33.1× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 2.72 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 20.0× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 2.85 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.0× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 6.06 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 14.3× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 3.27 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 22.4× (z +9.2) | — |
| [[A498 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5658), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC20]] | +0.66 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[COA1]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TNFAIP8L1]] | +0.59 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[CLYBL]] | +0.58 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[PARP1]] | +0.57 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[SNRPD1]] | +0.57 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[UBE2T]] | +0.56 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[ADAM22]] | +0.56 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[SMYD3]] | +0.56 | +0.28 / +0.47 | both halves | 3e-04 |  |
| [[HMBS]] | +0.56 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[GPSM2]] | +0.56 | +0.34 / +0.45 | both halves | 1e-04 |  |
| [[CCDC88C]] | +0.56 | +0.41 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN1L]] | -0.62 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[CHD1-DT]] | -0.60 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[DNAI4]] | -0.59 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[N4BP2L1]] | -0.59 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[LINC01004]] | -0.59 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[GTF2IRD2]] | -0.58 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[LVRN]] | -0.58 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[C14orf28]] | -0.58 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[CCDC59]] | -0.58 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[PPP1R12A-AS2]] | -0.57 | -0.24 / -0.31 | both halves | 5e-04 |  |
| [[KRBOX5]] | -0.57 | -0.29 / -0.32 | both halves | 2e-04 |  |
| [[TAS2R4]] | -0.57 | -0.34 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM22]] | B | ADAM22 activity raises RNFT2's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 1.98× lower at baseline in the lines without ADAM22 | 0.029 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[CBX2]] | B | CBX2 activity raises RNFT2's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 2.69× lower at baseline in the lines without CBX2 | 0.040 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[TMEM170B]] | B | TMEM170B activity raises RNFT2's level | lines that do not express TMEM170B (8) vs lines expressing it (42) | 1.82× lower at baseline in the lines without TMEM170B | 0.066 | ⚠ within organs, on part of the lines; also absent: KCNK13, KDM2B-DT, LINC02609 |
| [[LINC01237]] | B | LINC01237 activity raises RNFT2's level | lines that do not express LINC01237 (7) vs lines expressing it (43) | 1.31× lower at baseline in the lines without LINC01237 | 0.085 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRBOX5]] | C | RNFT2 activity raises KRBOX5's level | lines that do not express RNFT2 (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without RNFT2 | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF37, CSRP1-AS1, DBNDD1; maybe low, not absent |
| [[SCAP]] | C | RNFT2 activity raises SCAP's level | lines that do not express RNFT2 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without RNFT2 | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF37, CSRP1-AS1, DBNDD1; maybe low, not absent |
| [[PIGM]] | C | RNFT2 activity raises PIGM's level | lines that do not express RNFT2 (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without RNFT2 | 0.066 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF37, CSRP1-AS1, DBNDD1; maybe low, not absent |
| [[CCDC88C]] | C | RNFT2 activity raises CCDC88C's level | lines that do not express RNFT2 (3) vs lines expressing it (47) | 3.73× lower at baseline in the lines without RNFT2 | 0.084 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF37, CSRP1-AS1, DBNDD1; maybe low, not absent |
| [[UQCC2]] | C | RNFT2 activity raises UQCC2's level | lines that do not express RNFT2 (3) vs lines expressing it (47) | 1.81× lower at baseline in the lines without RNFT2 | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF37, CSRP1-AS1, DBNDD1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.581). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (19.0, -7.4); signed map (-10.1, -47.8). **Vector** length 80.6, 17.1% of its response variance represented; |z| ≥ 3 in 1,145 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +15.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.6 | +16.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +23.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +28.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +12.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | -0.5 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +3.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.6 | +0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -4.2 | +4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.7 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein, transmembrane 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.22 — chr12:116,738,178-116,853,631 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14627; previously TMEM118 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EX2](https://www.uniprot.org/uniprotkb/Q96EX2) (E3 ubiquitin-protein ligase RNFT2):

> E3 ubiquitin-protein ligase that negatively regulates IL3-dependent cellular responses through IL3RA ubiquitination and degradation by the proteasome, having an anti-inflammatory effect.

**Summary**, from NCBI Gene [84900](https://www.ncbi.nlm.nih.gov/gene/84900):

> Predicted to enable ubiquitin protein ligase activity. Predicted to be involved in positive regulation of ERAD pathway. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25905) · Entrez [84900](https://www.ncbi.nlm.nih.gov/gene/84900) · UniProt [Q96EX2](https://www.uniprot.org/uniprotkb/Q96EX2) · Ensembl [ENSG00000135119](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135119)

## Data

Gene col 5658: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5658); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5658, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5658]; `tensor/DDL_lfc|DDL_z.npy` [5658]; `embed/gene_vectors.npy` [5658]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5658 or target_col == 5658). Every well: [[RNFT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNFT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
